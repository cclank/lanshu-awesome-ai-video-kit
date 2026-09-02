#!/usr/bin/env python3
"""Generate a Kling video through Atlas Cloud without retrying paid submits."""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from urllib import error, parse, request


CATALOG_URL = "https://api.atlascloud.ai/api/v1/models"
DEFAULT_MODEL = "kwaivgi/kling-v3.0-std/text-to-video"
DEFAULT_API_BASE = "https://api.atlascloud.ai"


class AtlasError(RuntimeError):
    pass


class TransientGetError(AtlasError):
    pass


def _read_json_response(response):
    return json.loads(response.read().decode("utf-8"))


def request_json(url, method="GET", api_key=None, payload=None, timeout=120):
    headers = {"Accept": "application/json", "User-Agent": "lanshu-kling-prompter/1.0"}
    body = None
    if api_key:
        headers["Authorization"] = "Bearer " + api_key
    if payload is not None:
        headers["Content-Type"] = "application/json"
        body = json.dumps(payload).encode("utf-8")

    req = request.Request(url, data=body, headers=headers, method=method)
    try:
        with request.urlopen(req, timeout=timeout) as response:
            return _read_json_response(response)
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise AtlasError("Atlas Cloud returned HTTP %s: %s" % (exc.code, detail)) from exc
    except (error.URLError, TimeoutError, OSError) as exc:
        if method == "GET":
            raise TransientGetError("Atlas Cloud GET failed: %s" % exc) from exc
        raise AtlasError(
            "Atlas Cloud submit state is unknown; the paid POST was not retried: %s" % exc
        ) from exc


def unwrap(payload):
    if isinstance(payload, dict) and isinstance(payload.get("data"), dict):
        return payload["data"]
    return payload


def discover_contract(model, timeout=120):
    catalog = request_json(CATALOG_URL, timeout=timeout)
    entries = catalog.get("data", catalog) if isinstance(catalog, dict) else catalog
    match = next((item for item in entries if item.get("model") == model), None)
    if not match:
        raise AtlasError("Model is not present in the live Atlas Cloud catalog: " + model)
    if match.get("display_console") is not True or match.get("type") != "Video":
        raise AtlasError("Model is not an enabled video model in the live catalog: " + model)

    schema_url = match.get("schema")
    if not schema_url:
        raise AtlasError("Live model catalog did not provide a schema URL for: " + model)
    schema = request_json(schema_url, timeout=timeout)

    submit_path = None
    result_path = None
    for path, operations in schema.get("paths", {}).items():
        if operations.get("x-api-name") == "model_run" and "post" in operations:
            submit_path = path
        if operations.get("x-api-name") == "model_result" and "get" in operations:
            result_path = path
    if not submit_path or not result_path:
        raise AtlasError("Live schema is missing model_run or model_result endpoints.")

    input_schema = schema.get("components", {}).get("schemas", {}).get("Input", {})
    return {
        "submit_url": DEFAULT_API_BASE + submit_path,
        "result_url_template": DEFAULT_API_BASE + result_path,
        "input_schema": input_schema,
    }


def _require_enum(input_schema, name, value):
    allowed = input_schema.get("properties", {}).get(name, {}).get("enum")
    if allowed and value not in allowed:
        raise AtlasError("%s must be one of %s; got %r" % (name, allowed, value))


def build_payload(contract, model, prompt, aspect_ratio, duration, cfg_scale, sound, negative_prompt):
    if not prompt.strip():
        raise AtlasError("Prompt must not be empty.")
    if len(prompt) > 2500:
        raise AtlasError("Prompt exceeds the live Kling schema limit of 2500 characters.")

    input_schema = contract["input_schema"]
    _require_enum(input_schema, "aspect_ratio", aspect_ratio)
    _require_enum(input_schema, "duration", duration)
    cfg_schema = input_schema.get("properties", {}).get("cfg_scale", {})
    if not cfg_schema.get("minimum", 0) <= cfg_scale <= cfg_schema.get("maximum", 1):
        raise AtlasError("cfg_scale is outside the live schema range.")

    payload = {
        "model": model,
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "duration": duration,
        "cfg_scale": cfg_scale,
        "sound": sound,
        "multi_shot": False,
    }
    if negative_prompt:
        payload["negative_prompt"] = negative_prompt
    return payload


def submit_once(contract, api_key, payload, timeout=120):
    response = request_json(
        contract["submit_url"],
        method="POST",
        api_key=api_key,
        payload=payload,
        timeout=timeout,
    )
    prediction = unwrap(response)
    request_id = prediction.get("id") if isinstance(prediction, dict) else None
    if not request_id:
        raise AtlasError("Atlas Cloud submit response did not include a request ID.")
    return request_id


def poll_result(contract, api_key, request_id, max_wait=900, interval=8, timeout=120):
    deadline = time.monotonic() + max_wait
    result_url = contract["result_url_template"].replace(
        "{request_id}", parse.quote(request_id, safe="")
    )
    last_error = None
    while time.monotonic() < deadline:
        try:
            prediction = unwrap(request_json(result_url, api_key=api_key, timeout=timeout))
            last_error = None
        except TransientGetError as exc:
            last_error = exc
            time.sleep(interval)
            continue

        status = str(prediction.get("status", "")).lower()
        if status == "completed":
            outputs = prediction.get("outputs") or []
            if not outputs or not outputs[0]:
                raise AtlasError("Completed prediction did not include a video URL.")
            return outputs[0]
        if status == "failed":
            raise AtlasError("Atlas Cloud generation failed: %s" % prediction.get("error", ""))
        time.sleep(interval)

    suffix = ": %s" % last_error if last_error else ""
    raise AtlasError("Timed out while polling; no new generation was submitted" + suffix)


def download_video(url, output, timeout=120):
    output.parent.mkdir(parents=True, exist_ok=True)
    req = request.Request(url, headers={"User-Agent": "lanshu-kling-prompter/1.0"})
    try:
        with request.urlopen(req, timeout=timeout) as response:
            data = response.read()
    except (error.HTTPError, error.URLError, TimeoutError, OSError) as exc:
        raise AtlasError("Could not download completed video: %s" % exc) from exc
    if not data:
        raise AtlasError("Completed video download was empty.")
    output.write_bytes(data)


def read_prompt(args):
    if args.prompt_file:
        return args.prompt_file.read_text(encoding="utf-8").strip()
    return (args.prompt or "").strip()


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--prompt")
    source.add_argument("--prompt-file", type=Path)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--aspect-ratio", default="16:9")
    parser.add_argument("--duration", type=int, default=5)
    parser.add_argument("--cfg-scale", type=float, default=0.5)
    parser.add_argument("--negative-prompt")
    parser.add_argument("--no-sound", action="store_true")
    parser.add_argument("--max-wait", type=int, default=900)
    parser.add_argument("--poll-interval", type=int, default=8)
    parser.add_argument("--request-timeout", type=int, default=120)
    parser.add_argument("--output", type=Path, default=Path("output.mp4"))
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    try:
        prompt = read_prompt(args)
        contract = discover_contract(args.model, timeout=args.request_timeout)
        payload = build_payload(
            contract,
            args.model,
            prompt,
            args.aspect_ratio,
            args.duration,
            args.cfg_scale,
            not args.no_sound,
            args.negative_prompt,
        )
        if args.dry_run:
            print(json.dumps({"submit_url": contract["submit_url"], "payload": payload}, ensure_ascii=False))
            return 0

        api_key = os.environ.get("ATLASCLOUD_API_KEY") or os.environ.get("ATLAS_CLOUD_API_KEY")
        if not api_key:
            raise AtlasError("Set ATLASCLOUD_API_KEY before submitting a generation.")
        request_id = submit_once(contract, api_key, payload, timeout=args.request_timeout)
        video_url = poll_result(
            contract,
            api_key,
            request_id,
            max_wait=args.max_wait,
            interval=args.poll_interval,
            timeout=args.request_timeout,
        )
        download_video(video_url, args.output, timeout=args.request_timeout)
        print(json.dumps({"request_id": request_id, "model": args.model, "output": str(args.output)}, ensure_ascii=False))
        return 0
    except (AtlasError, OSError, ValueError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
