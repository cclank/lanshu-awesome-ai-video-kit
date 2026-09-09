<div align="center">

<!-- Banner -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,2,30&height=180&section=header&text=lanshu-awesome-ai-video-kit&fontSize=38&fontColor=ffffff&fontAlignY=38&desc=AI%20Video%20Prompt%20Engineering%20·%2015%20Models%20·%20301%20Prompts&descSize=16&descAlignY=62&descColor=cccccc">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,2,30&height=180&section=header&text=lanshu-awesome-ai-video-kit&fontSize=38&fontColor=ffffff&fontAlignY=38&desc=AI%20Video%20Prompt%20Engineering%20·%2015%20Models%20·%20301%20Prompts&descSize=16&descAlignY=62&descColor=ffffff" alt="banner" width="100%">
</picture>

# 🎬 lanshu-awesome-ai-video-kit

**An awesome curated kit for AI video prompt engineering.**
**The most complete AI video prompt library on the web — 15 models (11 commercial + 4 open source) / 433 standalone + 110 cross-model = 543 prompts / 7 Claude Skills / 21 methodology docs**

🇨🇳 **[中文 README →](README.md)**

<p>
  <img alt="Awesome" src="https://img.shields.io/badge/-Awesome-fc60a8?style=flat&logo=awesome-lists&logoColor=white">
  <img alt="Models" src="https://img.shields.io/badge/models-15-8b5cf6?style=flat">
  <img alt="Prompts" src="https://img.shields.io/badge/prompts-433-f97316?style=flat">
  <img alt="Skills" src="https://img.shields.io/badge/skills-7-06b6d4?style=flat">
  <img alt="Docs" src="https://img.shields.io/badge/methodology-21-34d399?style=flat">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-cccccc?style=flat">
  <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-9333ea?style=flat">
</p>

<p>
  <a href="#-quick-start">🚀 Quick Start</a> ·
  <a href="prompts/README.md">📚 433 Prompts</a> ·
  <a href="methodology/README.md">📖 21 Methodology Docs</a> ·
  <a href="skills/README.md">🛠️ 7 Skills</a> ·
  <a href="tools/prompt-browser/index.html">🌐 Web Browser</a> ·
  <a href="RESOURCES.md">🔗 Resources</a>
</p>

</div>

---

## ✨ What is this?

Prompting AI video models (Sora / Veo / Kling / Runway / Pika / Hailuo / Hunyuan / Seedance / HappyHorse / Wan / Jimeng + 4 open source) is **not writing a description** — it's **directing a shot**.

This repo distills:

- ByteDance Volcano Engine's official **53-page Seedance 2.0 PDF guide**
- Kuaishou Kling official docs + Atlabs 5-layer formula
- **OpenAI Cookbook** official Sora 2 guide
- **Google DeepMind** official Veo 3 prompt guide
- Battle-tested experience from 8 community review blogs
- Official repos & prompt handbooks of **4 open source models** (Lightricks LTX / Genmo Mochi / Zhipu CogVideoX / Higgsfield Soul)

Structured into 4 categories of practical resources:

| Resource | Content | Best for |
|---|---|---|
| 📚 [prompts/](prompts/) | **433 battle-tested prompts** across 16 models / 29 scenarios, with official samples + recommended params | Copy & tweak |
| 📖 [methodology/](methodology/) | **21 methodology SOPs**: advanced formula / storyboarding / emotion externalization / 5 model-specific guides + 6-model quick reference + **4 open source quick reference** + cross-model comparison + 12 pitfalls | Learn to "direct shots" |
| 🛠️ [skills/](skills/) | **7 Claude Code Skills** — Seedance ×3 + HappyHorse + Kling + **model-selector** (15-model shopping advisor) + **prompt-translator** (cross-model converter) | Let Claude pick/write/fix/translate |
| 🌐 [tools/prompt-browser/](tools/prompt-browser/) | Single-page HTML browser (15-model rainbow filter + URL state sharing + keyboard nav + Drawer details) | If you don't want to read markdown |

---

## 📑 Contents

- [✨ What is this?](#-what-is-this)
- [🎯 15 Models at a Glance](#-15-models-at-a-glance)
- [🚀 Quick Start](#-quick-start)
- [📚 Prompts by Model](#-prompts-by-model)
- [📖 Methodology Index](#-methodology-index)
- [🛠️ Claude Code Skills](#%EF%B8%8F-claude-code-skills)
- [🌐 Web Tools](#-web-tools)
- [📁 Directory Structure](#-directory-structure)
- [🤝 Contributing](#-contributing)
- [🙏 Credits](#-credits)
- [📜 License](#-license)

---

## 🎯 15 Models at a Glance

> 📅 **May 2026 snapshot** — Data refreshed monthly. A weekly GitHub Action auto-monitors all 32 official endpoints and files issues when versions change.

### 🏢 11 Commercial Flagships

| Model | Vendor | Headline | Length | CJK | Audio | Physics | Edit | China access |
|---|---|---|---|---|---|---|---|---|
| **Seedance 2.0** ⭐ | ByteDance / Volcano Ark | **Overall SOTA · 53-page official PDF · 8-element formula · powers Jimeng** | 60s 2K | ★★★ | ★★★ | ★★★ | — | ✓ |
| **HappyHorse 1.0** | Alibaba | Tight short-form specialist · 30-55 words · 8s beat structure · native ambient audio | 15s (default 5s) | ★★★ | ★★ | ★★ | — | ✓ |
| **Kling 3.0** | Kuaishou | **S-tier** · CJK + I2V + 48fps 1080p + lip-sync | 2m | ★★★★★ | ★★★★ | ★★★★ | ✓ | ✓ |
| **Veo 3.1** | Google DeepMind | **S-tier** · best native audio + multi-speaker dialogue | 148s chained | ★★ | ★★★★★ | ★★★ | — | △ |
| **Sora 2** ⚠️ | OpenAI | Cinematic + Cameos · **⚠️ web/app sunset 2026-04-26** | 25s (Pro) | ★★ | ★★★★ | ★★★★★ | — | △ |
| **Runway Gen-4.5 / Aleph** | Runway | **#1 ELO overall** + Aleph edit-only features | 10s / Aleph 5s | ★★★ | — | ★★★ | ★★★★★ | ✓ |
| **Pika 2.5** | Pika Labs | **Best price $8/mo** + 15+ Pikaffects | 25s | ★★ | ★ | ★★ | — | ✓ |
| **Hailuo 02** | MiniMax | **#1 physics simulation** + 1080p (also 2.3 budget) | 10s | ★★★ | — | ★★★★★ | — | ✓ |
| **Hunyuan Video 1.5** | Tencent | **Strongest open source** (13B/8.3B) + LoRA + runs on RTX 4090 | 10s | ★★★★ | — | ★★★ | ✓ | ✓ |
| **Wan 2.7** | Alibaba Tongyi | **#1 digital-human lip-sync** · 2.6 OSS stable / 2.7 latest | 15s | ★★★ | ★★★★★ | ★★★ | ✓ | ✓ |
| **Jimeng AI** | ByteDance CapCut | **Strongest CJK + CapCut native** (powered by Seedance 2.0) | 60s 2K | ★★★★★ | ★★★ | ★★★ | — | ✓ |

### 🔓 4 Open Source / Open-Friendly (local deploy + LoRA + extensible)

| Model | Vendor | Headline | License | Length | Resolution |
|---|---|---|---|---|---|
| **LTX-Video 0.9.7** | Lightricks | **Real-time generation** — 5s video in 5s, 30FPS | Apache 2.0 | 10s | 1216×704 |
| **Mochi 1** | Genmo | **Largest open source** (10B AsymmDiT) + **strong prompt adherence** | Apache 2.0 | 5.4s | 480p |
| **CogVideoX 5B / 1.5** | Zhipu · Tsinghua | China-made + **226-token long prompt** + dedicated I2V weights | Apache 2.0 | 10s | 1360×768 |
| **Higgsfield Soul / DoP** | Higgsfield AI | **Industry-best Soul ID character consistency** + Soul Cinema | Partial OSS | 15s / 60s long-form | 1080p+ |

→ Not sure which to pick? Let Claude help → [skills/model-selector](skills/model-selector/SKILL.md) (covers all 15)
→ Commercial decision tree → [methodology/10](methodology/10-跨模型对比.md) + [methodology/13](methodology/13-六大模型公式速查.md)
→ Open source decision tree → [methodology/14](methodology/14-四大开源模型速查.md) ⭐

---

## 🚀 Quick Start

### I just want a usable prompt

**Option A · Recommended**: Use the [Web Browser](tools/prompt-browser/index.html)

```bash
git clone https://github.com/cclank/lanshu-awesome-ai-video-kit.git
cd lanshu-awesome-ai-video-kit
python3 -m http.server 8000
# Open http://localhost:8000/tools/prompt-browser/
```

Filter by scenario / model / tags in the sidebar → hover cards for preview → click for Drawer detail → one-click copy. Supports `/` search, `j`/`k` navigation, `Enter` for detail, `c` to copy, URL shareable filter state.

**Option B**: Read markdown indexes directly

- [Seedance 2.0 · 117 prompts](prompts/seedance/README.md) — commercials / social viral / cinematic / action / sports / nature / ASMR / comedy / craft
- [HappyHorse 1.0 · 90 prompts](prompts/happyhorse/README.md) — 8s tight beats / product / portrait / action / cinematic / nature
- [Kling 3.0 · 72 prompts](prompts/kling/README.md) — product / cinematic / action / **viral transform** / music video / experimental / gaming / **image-to-video specialty**
- [Sora 2 · 20 prompts](prompts/sora/README.md) — incl. OpenAI Cookbook official Shot List & parameterized templates
- [Veo 3.1 · 20 prompts](prompts/veo/README.md) — incl. Google DeepMind official native audio dialogue templates
- **Runway Gen-4.5 / Aleph · 12 prompts** — JSON `rw-*` · Aleph editing ★ #1 ELO overall
- **Pika 2.5 · 12 prompts** — JSON `pk-*` · Pikaffects (Melt/Explode/Squish 15+) + Pikaframes
- **Hailuo 02 · 12 prompts** — JSON `hl-*` · physics simulation (water/fire/smoke/cloth/gravity/material)
- **Hunyuan Video 1.5 · 12 prompts** — JSON `hy-*` · open source + cross-dimensional + LoRA training
- **Wan 2.7 · 12 prompts** — JSON `wn-*` · digital-human lip-sync + Entity+Scene+Motion+Sound formula
- **Jimeng AI · 12 prompts** — JSON `jm-*` · Seedance 2.0 engine, CJK aesthetics (Jiangnan/Hanfu/Xianxia/ink-wash)
- 🔓 **LTX-Video 0.9.7 · 8 prompts** — JSON `lt-*` · single-paragraph prose + real-time + screenplay dialogue format
- 🔓 **Mochi 1 · 8 prompts** — JSON `mo-*` · free prose + physics details (time-lapse / shattering / arcing)
- 🔓 **CogVideoX 5B · 8 prompts** — JSON `cg-*` · long prompts (226 tokens) + T2V/I2V dual mode
- 🔓 **Higgsfield Soul · 8 prompts** — JSON `hg-*` · short directives + Soul ID + DoP templates + Soul Cinema 15s / 60s long-form

### I want Claude to write prompts for me

```bash
cp -r skills/seedance-prompter ~/.claude/skills/
cp -r skills/seedance-storyboard ~/.claude/skills/
cp -r skills/seedance-debugger ~/.claude/skills/
cp -r skills/happyhorse-prompter ~/.claude/skills/
cp -r skills/kling-prompter ~/.claude/skills/
cp -r skills/model-selector ~/.claude/skills/      # ★ 15-model shopping advisor
cp -r skills/prompt-translator ~/.claude/skills/   # ★ cross-model converter (110-prompt baseline)
```

Then in Claude Code just say "make a product ad video" — Claude auto-picks the right skill. Unsure which model? Ask "Sora or Kling?" to trigger `model-selector`. Already have a Sora prompt and want to run it on Kling? Say "translate this to Kling style" to trigger `prompt-translator`.

### I want to learn the methodology systematically

Read [methodology/](methodology/) in order:

1. Basics → 2. Advanced formula → 3. Storyboarding → 4. Emotion externalization → 5. Camera lexicon → 6. Constraint terms → 7. Special characters → 8. 12 pitfalls → 9. Kling formula → 10. Cross-model comparison → 11. Sora formula → 12. Veo formula → 13. Six-model quick reference (Runway/Pika/Hailuo/Hunyuan/Wan/Jimeng) → **14. Four open source quick reference** (LTX/Mochi/CogVideoX/Higgsfield) ⭐

---

## 📖 Methodology Index

| # | Doc | Solves | Read time |
|---|---|---|---|
| 01 | [Basics](methodology/01-基础公式.md) | Which of 4 task types to pick | 3 min |
| 02 | [Advanced formula](methodology/02-进阶公式.md) | 8 elements → engineering-grade prompt | 8 min |
| 03 | [Storyboarding](methodology/03-分镜时序.md) | Break complex plot into Shot 1/2/3 | 5 min |
| 04 | [Emotion externalization](methodology/04-情绪外化表.md) | Replace "very sad" with action details | 3 min |
| 05 | [Camera lexicon](methodology/05-运镜词典.md) | Camera/lighting/style keywords (EN-CN) | reference |
| 06 | [Constraint terms](methodology/06-约束词清单.md) | Avoid subtitle/logo/watermark | reference |
| 07 | [Special chars](methodology/07-特殊字符规范.md) | `()` music / `<>` SFX / `{}` dialogue | 1 min |
| 08 | [12 pitfalls](methodology/08-避坑12问.md) | 12 common issues: symptom → root cause → fix | on-demand |
| 09 | [Kling formula](methodology/09-kling-公式.md) | Kling 3 writing styles + 6 rules | 8 min |
| 10 | [Cross-model comparison](methodology/10-跨模型对比.md) | 5-model decision tree + same need × 5 styles | 10 min ⭐ |
| 11 | [Sora formula](methodology/11-sora-公式.md) | Sora 2 layered Shot List + parameterized | 7 min |
| 12 | [Veo formula](methodology/12-veo-公式.md) | Veo 8 elements + native audio 4-layer | 6 min |
| 13 | [Six-model quick reference](methodology/13-六大模型公式速查.md) | Runway / Pika / Hailuo / Hunyuan / Wan / Jimeng + 11-model selection | 12 min ⭐ |
| 14 | [Four open source quick reference](methodology/14-四大开源模型速查.md) | LTX / Mochi / CogVideoX / Higgsfield formula contrast + **15-model decision tree** | 12 min ⭐ |
| 15 | [Seedance Masterclass](methodology/15-seedance-masterclass.md) ⭐ | 10 YouTube tutorials (500K+ views): 9-element / Timeline / character consistency 5 steps / 5 viral formats / VFX / Bullet Time / 8 templates | 15 min ⭐ |
| 16 | [Gemini Omni Formula](methodology/16-gemini-omni-公式.md) ⭐NEW | Google AI official 5 prompting tips (Real-World anchors / text rendering / camera terms / iterative edits / action change) + 10 official samples | 8 min ⭐ |
| 17 | [HappyHorse Masterclass](methodology/17-happyhorse-masterclass.md) ⭐ | 14 YouTube tutorials: 6-element formula + 20-word single-shot + emotion-to-physics + @tag Omni Reference + Storyboard 45s + 11 pitfalls + 33 prompts | 12 min ⭐ |
| 18 | [Kling Masterclass](methodology/18-kling-masterclass.md) ⭐ | 25 YouTube channels (6M+ views): 5-element + Constraint Sandwich (O1) + Multi-Shot 6 shots/15s + Motion Brush/Library + 3×3 grid + Character Sheet + OmniEdit + 56 prompts | 18 min ⭐ |
| 19 | [Seedance Round 3](methodology/19-seedance-masterclass-round3.md) ⭐ | 8 new YouTube tutorials: 3-type reference + CapCut Video Studio + AI Anime 4-step + 3×3 grid + video extend 30s + 19 prompts | 10 min ⭐ |
| 20 | [Realistic Character Consistency](methodology/20-realistic-character-consistency.md) ⭐ | 20 YouTube tutorials (5M+ views): realistic portrait 5-part formula + Character Sheet + Omni Reference + 3×3 grid + Face Swap + Dan Kieft Prompt Pack + MidJourney→Nano Banana→Kling/VEO full pipeline | 15 min ⭐ |
| 21 | [Playbook #1 · FPV Path Drawing](methodology/21-fpv-航拍路径绘制玩法.md) ⭐NEW | @MrLarus viral technique (45K+158K views): **draw red line on image as flight path, Seedance generates FPV drone shot along the line**. 3-step workflow + 8 prompt design keys + multi-model migration | 8 min ⭐ |

---

## 🛠️ Claude Code Skills

| Skill | Model | Trigger | Output |
|---|---|---|---|
| ★ [model-selector](skills/model-selector/SKILL.md) | **All 15 models** | "which model should I use" / "Sora or Kling" | Recommends 1-3 models with reasoning |
| ★ [prompt-translator](skills/prompt-translator/SKILL.md) | **Across 11 commercial** | "translate this Sora prompt to Kling style" | Target-model formula prompt + mapping table + caveats |
| [seedance-prompter](skills/seedance-prompter/SKILL.md) | Seedance | "make a Seedance video" | 8-element structured prompt |
| [seedance-storyboard](skills/seedance-storyboard/SKILL.md) | Seedance | "split this plot into shots" | 3-5 time-sequenced shots |
| [seedance-debugger](skills/seedance-debugger/SKILL.md) | Seedance | "my prompt is broken" | 12-category diagnosis + fixed version |
| [happyhorse-prompter](skills/happyhorse-prompter/SKILL.md) | HappyHorse | "3-15s tight video + native audio" | 30-55 words + audio path |
| [kling-prompter](skills/kling-prompter/SKILL.md) | Kling | "Kling / CJK drama / image-to-video" | Auto-adapts among 3 styles |

See [skills/README.md](skills/README.md) for the decision tree.

> **Optional external skill (not shipped with this kit)**: to parse a reference video script / PDF / other web page into text before feeding your prompt workflow, you can additionally install **cue-omni-reader** ([`sensedeal/cue-skills`](https://github.com/sensedeal/cue-skills) → [`cue-omni-reader`](https://github.com/sensedeal/cue-skills/tree/main/cue-omni-reader), MIT) — an instruction-only layer that drives the official Cue Omni Reader MCP to parse an HTTP(S) URL or an authorized local document, audio, or video source into Markdown. Install: `npx skills add sensedeal/cue-skills --skill cue-omni-reader`. This kit does not bundle it; follow the upstream README for install and usage.

---

## 🌐 Web Tools

| Tool | Description | Live URL |
|---|---|---|
| [Homepage](index.html) | Liquid-Glass landing — Hero stats + 15-model wall + 6 entry cards | [Live →](https://lanshu-awesome-ai-video-kit.lank.workers.dev) |
| [Prompt Browser](tools/prompt-browser/index.html) | Single-page browser, 15-model rainbow filter + URL state + keyboard nav + Drawer | `tools/prompt-browser/` |
| [Cross-Model Matrix](tools/cross-model/index.html) | 10 scenarios × 11 commercial models = 110 cross-model prompts + video slots | `tools/cross-model/` |

Features:
- **Hero stats**: 433 / 16 / 7 / 21 live counts
- **15-model rainbow filter** — each model has its own glowing color dot
- **3D filtering**: model + category + tags (multi-select)
- **Keyword search** — title / prompt body / tags / notes
- **URL state sync** — `#model=kling-3.0&tags=anime,handheld&q=rain` is shareable
- **Keyboard nav** — `/` search · `j`/`k` up/down · `Enter` detail · `c` copy · `Esc` close
- **Card Drawer detail** — full prompt + similar-category recommendations
- **Dark / light theme** — localStorage persistent
- **Responsive** — mobile single-column, sidebar hidden

---

## 📁 Directory Structure

```
lanshu-awesome-ai-video-kit/
├── README.md                       # Chinese README (primary)
├── README.en.md                    # English README (this file)
├── RESOURCES.md                    # Curated resource links
├── CONTRIBUTING.md                 # Contribution guide
├── CHANGELOG.md                    # Version history
├── awesome.md                      # awesome-list submission entry
├── LICENSE                         # MIT
│
├── prompts/                        # 433 prompts (16 models)
│   ├── data/all-prompts.json       # Single source of truth (web tools consume this)
│   ├── data/cross-model-matrix.json # 110 cross-model prompts (10 × 11)
│   ├── seedance/README.md          # 64 Seedance prompts index
│   ├── happyhorse/README.md        # 57 HappyHorse prompts index
│   ├── kling/README.md             # 36 Kling prompts index
│   ├── sora/README.md              # 20 Sora prompts index
│   ├── veo/README.md               # 20 Veo prompts index
│   └── (other 10 models)           # rw-* pk-* hl-* hy-* wn-* jm-* lt-* mo-* cg-* hg-*
│
├── methodology/                    # 21 methodology SOPs
│   ├── 01-基础公式.md ~ 08-避坑12问.md   # General + Seedance
│   ├── 09-kling-公式.md ~ 12-veo-公式.md # Kling/Sora/Veo + cross-model
│   ├── 13-六大模型公式速查.md      # Runway/Pika/Hailuo/Hunyuan/Wan/Jimeng + 11 selection
│   └── 14-四大开源模型速查.md      # ⭐ LTX/Mochi/CogVideoX/Higgsfield + 15 decision tree
│
├── skills/                         # 7 Claude Code Skills
│   ├── model-selector/SKILL.md     # ⭐ 15-model shopping advisor
│   ├── prompt-translator/SKILL.md  # ⭐ cross-model translator (110-prompt baseline)
│   └── seedance/happyhorse/kling-prompter/...
│
├── scripts/                        # 15-model version auto-monitor
│   ├── monitor_models.py           # SHA-256 hash monitor for 27 endpoints
│   ├── model_endpoints.yaml        # Endpoint config
│   └── known_hashes.json           # Baseline (CI-maintained)
│
├── .github/
│   ├── workflows/model-version-monitor.yml  # Weekly Mon 09:00 auto-check
│   └── ISSUE_TEMPLATE/             # 4 form-based contribution templates
│
└── tools/
    ├── prompt-browser/             # Single-page HTML browser (v2)
    └── cross-model/                # Cross-model matrix page (Liquid Glass)
```

---

## 🤝 Contributing

We welcome:

- 🟢 A battle-tested prompt (highest frequency, easiest) — [New Prompt form](.github/ISSUE_TEMPLATE/new-prompt.yml)
- 🎬 A Cross-Model Matrix test video (fill in one of the 110 slots) — [Test Video form](.github/ISSUE_TEMPLATE/test-video-contribution.yml)
- 🟡 A new methodology doc
- 🔴 A new model / new version (Sora 3 / Veo 4 / Wan 3 etc.) — [New Model/Version form](.github/ISSUE_TEMPLATE/new-version-or-model.yml)
- 🔴 A new Skill

Full schema & process: [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 🙏 Credits

This repo's content draws from these **excellent sources** (in contribution order):

| Source | Contribution |
|---|---|
| 🟢 [OpenAI Cookbook](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) | Sora 2 official layered formula + 3 detailed samples |
| 🟢 [Google DeepMind](https://deepmind.google/models/veo/prompt-guide/) | Veo 3 official 8-element formula + 5 audio demos |
| 🟢 Volcano Ark PDF | Seedance 2.0 official 53-page guide (advanced formula / storyboarding / 12-issue diagnosis) |
| 🟢 [Atlabs AI](https://www.atlabs.ai/blog/kling-3-0-prompting-guide-master-ai-video-generation) | Kling 5-layer advanced formula |
| 🟢 [Runway Help · Gen-4 Guide](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide) / [Aleph Guide](https://help.runwayml.com/hc/en-us/articles/43277392678803-Aleph-Prompting-Guide) | Runway official Gen-4 + Aleph editing formula |
| 🟢 [Pika Labs · Pika 2.5](https://pikaslabs.com/pika-2.5/) | Pika 2.5 + complete Pikaffects catalog |
| 🟢 [MiniMax API docs](https://platform.minimax.io/docs/guides/video-generation) | Hailuo 02 official + physics simulation details |
| 🟢 [Tencent HunyuanVideo GitHub](https://github.com/Tencent-Hunyuan/HunyuanVideo) | Hunyuan open source repo + official prompt handbook |
| 🟢 [Alibaba Cloud · Wan Prompt Guide](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt) | Wan 2.7 official Entity+Scene+Motion+Sound formula |
| 🟢 [Jimeng AI](https://jimeng.jianying.com/) | Jimeng 3.0 official platform |
| 🟢 [Lightricks LTX-Video](https://github.com/Lightricks/LTX-Video) | LTX 0.9.7 official repo + real-time ComfyUI workflows |
| 🟢 [Genmo Mochi 1](https://github.com/genmoai/mochi) | Mochi 1 10B AsymmDiT official code + Replicate API |
| 🟢 [Zhipu CogVideoX](https://github.com/zai-org/CogVideo) | CogVideoX 5B / 1.5 official repo + I2V dedicated weights |
| 🟢 [Higgsfield AI](https://higgsfield.ai/) | Higgsfield Soul ID + DoP templates + AI Director |
| 🟡 8 community blogs | Imagine.art / Elser AI / CyberLink / GeekVibes / vicsee / Atlas Cloud / CrePal / UlazAI / VEED / SeaArt — supplementary examples + cross-model comparison |

More: [RESOURCES.md](RESOURCES.md)

---

## 📜 License

MIT — prompt content sourced from public docs & review blogs, for educational & research use only. All model rights belong to Volcano Engine / Alibaba / Kuaishou / OpenAI / Google DeepMind / Runway / Pika Labs / MiniMax / Tencent / ByteDance CapCut / Lightricks / Genmo / Zhipu · Tsinghua / Higgsfield AI.

---

<div align="center">

**⭐ Star** if this helped you

Made with ❤️ by [lanshu](https://github.com/cclank) · CHANGELOG: [v0.8.0](CHANGELOG.md)

</div>
