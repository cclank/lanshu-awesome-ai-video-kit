import importlib.util
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = (
    Path(__file__).parents[1]
    / "skills"
    / "kling-prompter"
    / "scripts"
    / "atlas_generate.py"
)
SPEC = importlib.util.spec_from_file_location("atlas_generate", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def contract():
    return {
        "submit_url": "https://api.example.test/generate",
        "result_url_template": "https://api.example.test/result/{request_id}",
        "input_schema": {
            "properties": {
                "aspect_ratio": {"enum": ["16:9", "9:16", "1:1"]},
                "duration": {"enum": [3, 4, 5]},
                "cfg_scale": {"minimum": 0, "maximum": 1},
            }
        },
    }


class AtlasKlingClientTests(unittest.TestCase):
    @mock.patch.object(MODULE, "request_json")
    def test_discovers_endpoints_from_live_schema_shape(self, request_json):
        request_json.side_effect = [
            {
                "data": [
                    {
                        "model": MODULE.DEFAULT_MODEL,
                        "display_console": True,
                        "type": "Video",
                        "schema": "https://schema.test/kling.json",
                    }
                ]
            },
            {
                "paths": {
                    "/api/v1/model/generateVideo": {
                        "post": {},
                        "x-api-name": "model_run",
                    },
                    "/api/v1/model/result/{request_id}": {
                        "get": {},
                        "x-api-name": "model_result",
                    },
                },
                "components": {"schemas": {"Input": {"properties": {}}}},
            },
        ]
        found = MODULE.discover_contract(MODULE.DEFAULT_MODEL)
        self.assertEqual(found["submit_url"], MODULE.DEFAULT_API_BASE + "/api/v1/model/generateVideo")
        self.assertIn("{request_id}", found["result_url_template"])

    def test_payload_is_validated_against_live_enums(self):
        payload = MODULE.build_payload(
            contract(), MODULE.DEFAULT_MODEL, "A crane shot", "16:9", 5, 0.5, True, "watermark"
        )
        self.assertEqual(payload["duration"], 5)
        self.assertEqual(payload["negative_prompt"], "watermark")
        with self.assertRaisesRegex(MODULE.AtlasError, "aspect_ratio"):
            MODULE.build_payload(
                contract(), MODULE.DEFAULT_MODEL, "A crane shot", "4:3", 5, 0.5, True, None
            )

    @mock.patch.object(MODULE, "request_json")
    def test_paid_submit_is_called_exactly_once(self, request_json):
        request_json.return_value = {"data": {"id": "request-1", "status": "processing"}}
        request_id = MODULE.submit_once(contract(), "secret", {"model": MODULE.DEFAULT_MODEL})
        self.assertEqual(request_id, "request-1")
        request_json.assert_called_once()
        self.assertEqual(request_json.call_args.kwargs["method"], "POST")

    @mock.patch.object(MODULE, "request_json")
    def test_ambiguous_submit_is_not_retried(self, request_json):
        request_json.side_effect = MODULE.AtlasError("unknown submit state")
        with self.assertRaisesRegex(MODULE.AtlasError, "unknown submit state"):
            MODULE.submit_once(contract(), "secret", {"model": MODULE.DEFAULT_MODEL})
        request_json.assert_called_once()

    @mock.patch.object(MODULE.time, "sleep")
    @mock.patch.object(MODULE.time, "monotonic", side_effect=[0, 0, 1, 2])
    @mock.patch.object(MODULE, "request_json")
    def test_polling_retries_get_only(self, request_json, monotonic, sleep):
        request_json.side_effect = [
            MODULE.TransientGetError("temporary"),
            {"data": {"status": "processing"}},
            {"data": {"status": "completed", "outputs": ["https://cdn.test/video.mp4"]}},
        ]
        result = MODULE.poll_result(contract(), "secret", "request-1", max_wait=10, interval=1)
        self.assertEqual(result, "https://cdn.test/video.mp4")
        self.assertEqual(request_json.call_count, 3)
        self.assertEqual(sleep.call_count, 2)


if __name__ == "__main__":
    unittest.main()
