# Resources · 资源链接清单

> 给视频生成方向的同学准备的"开荒包"。按使用场景而非按模型分类。

## 目录

- [官方文档](#官方文档)
- [提示词学习](#提示词学习)
- [实测与对比博客](#实测与对比博客)
- [API 与代码](#api-与代码)
- [社区与讨论](#社区与讨论)
- [Prompt 互联工具](#prompt-互联工具)
- [姊妹方向：图生](#姊妹方向图生)

---

## 官方文档

### Doubao Seedance 2.0（字节 / 火山方舟）
- [火山方舟控制台](https://www.volcengine.com/product/ark) — 接入入口
- [Seedance 模型介绍](https://www.volcengine.com/) — 产品页
- 官方 PDF《Doubao Seedance 2.0 系列提示词指南》— 53 页（已沉淀到 [methodology/](methodology/)）

### HappyHorse 1.0（阿里巴巴）
- [Try Happy Horse AI](https://tryhappyhorseai.com/) — 在线体验
- [tryhappyhorseai.com 50 prompts](https://tryhappyhorseai.com/blog/happy-horse-ai-prompts)

### Kling 3.0（快手）
- [klingai.com](https://klingai.com/) — 官方平台（国际版）
- [可灵 AI 官网](https://www.aigc.cn/kling-ai) — 国内入口
- [可灵官方教程 · 知乎](https://zhuanlan.zhihu.com/p/714829166)

### Sora 2（OpenAI）
- [OpenAI Cookbook · Sora 2 Prompting Guide](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) ⭐ 必读
- [OpenAI Sora 主页](https://openai.com/sora/)

### Veo 3 / 3.1（Google DeepMind）
- [DeepMind Veo Prompt Guide](https://deepmind.google/models/veo/prompt-guide/) ⭐ 必读
- [Google Cloud · Ultimate Prompting Guide for Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)

### Gemini Omni（Google AI / DeepMind, 2026-05 新发布）⭐ NEW
- [Google AI · Mastering Gemini Omni: The Ultimate Video Prompting Guide](https://x.com/GoogleAI/status/2059381218660270435) ⭐ 必读 — Google AI 官方推文,5 大 prompting tips + 完整样板
- 试用平台:[Gemini App](https://gemini.google.com/) · [Flow by Google](https://flow.google.com/) · [Google Flow Music](https://flow.google.com/music) · YouTube Shorts/Create
- 核心差异化:跨模态(any-input-to-anything) · 文字渲染业界强项 · 迭代编辑 targeted updates · 中途改动作保连续性 · Real-World 知识利用
- 本仓库 [methodology/16-gemini-omni-公式.md](methodology/16-gemini-omni-公式.md) — 5 tips 详解 + 与 Veo 3.1/Sora 2 对比

### Runway Gen-4 / Aleph
- [Runway Gen-4 Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide) ⭐ 官方
- [Runway Aleph Prompting Guide](https://help.runwayml.com/hc/en-us/articles/43277392678803-Aleph-Prompting-Guide) ⭐ 官方
- [Creating with Aleph](https://help.runwayml.com/hc/en-us/articles/43176400374419-Creating-with-Aleph)
- [Runway Aleph - The Essentials | Scenario](https://help.scenario.com/en/articles/runway-aleph-the-essentials/)
- [Runway 官方平台](https://runwayml.com/)

### Pika 2.5（Pika Labs）
- [Pika 2.5 主页](https://pikaslabs.com/pika-2.5/) ⭐
- [Promptomania · Pika 2.5 模板](https://promptomania.com/models/pika/pika-2-5)
- [Pika Labs 完整教程](https://pikalabsai.org/pika-labs-prompting-guide/)
- iOS Pikaffects 独立 App（App Store 搜 "Pikaffects"）

### Hailuo 02（MiniMax）
- [MiniMax API 文档](https://platform.minimax.io/docs/guides/video-generation) ⭐ 官方
- [Segmind · Hailuo Prompt Guide](https://blog.segmind.com/hailuo-minimax-ai-video-prompt-guide/)
- [getimg · Hailuo 02 物理细节解析](https://getimg.ai/blog/minimax-hailuo-02-the-1080p-ai-video-model-that-gets-physics-right)
- [Cliprise · Hailuo 02 完整指南](https://www.cliprise.app/learn/guides/model-guides/hailuo-02-complete-guide)

### Hunyuan Video 1.5（腾讯）
- [GitHub · Tencent-Hunyuan/HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) ⭐ 官方仓库
- [GitHub · HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5)
- [HuggingFace · tencent/HunyuanVideo-1.5](https://huggingface.co/tencent/HunyuanVideo-1.5)
- [官方 Prompt Handbook](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/assets/HunyuanVideo_1_5_Prompt_Handbook_EN.md) ⭐
- [ComfyUI Hunyuan Video 教程](https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video)
- [Replicate Hunyuan 示例](https://replicate.com/tencent/hunyuan-video/examples)

### Wan 2.7（阿里通义万相）
- [Alibaba Cloud · Wan 文生视频 Prompt 指南](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt) ⭐ 官方
- [Alibaba Cloud · Model Studio Wan Recipe](https://www.alibabacloud.com/blog/model-studio-wan-video-generation-prompts-recipe_602777)
- [Wan 2.7 完整指南 | HappyHorse Model](https://happyhorsemodel.ai/en/articles/wan-2-5-complete-guide)
- [Kie.ai · Wan 2.7 API](https://kie.ai/wan-2-5)

### 即梦 3.0（字节剪映）
- [即梦 AI 官网](https://jimeng.jianying.com/) ⭐
- [即梦 AI 创作平台入口](https://jimeng.aigc.cn/)
- [火山引擎即梦 API](https://www.volcengine.com/product/jimeng)
- [知乎 · 即梦 Seedance 2.0 喂饭教程](https://zhuanlan.zhihu.com/p/2004623893273519265)
- [知乎 · 即梦智能体全流程实训指南](https://zhuanlan.zhihu.com/p/1992324916876423186)

### LTX-Video 0.9.7（Lightricks / 开源 Apache 2.0）
- [GitHub · Lightricks/LTX-Video](https://github.com/Lightricks/LTX-Video) ⭐ 官方仓库
- [HuggingFace · LTX-Video](https://huggingface.co/Lightricks/LTX-Video)
- [HuggingFace · LTX-Video-0.9.7-dev](https://huggingface.co/Lightricks/LTX-Video-0.9.7-dev)
- [ComfyUI 工作流示例](https://comfyanonymous.github.io/ComfyUI_examples/ltxv/)
- [film.fun · LTX-2 Prompting Guide](https://www.film.fun/articles/ltx-2-prompting-guide) ⭐ 含 screenplay 格式样板
- [VEED · LTX-Video Prompting Guide](https://www.veed.io/learn/ltx-video-prompting-guide)
- [Modal Cloud 一键部署](https://modal.com/docs/examples/ltx)

### Mochi 1（Genmo / 开源 Apache 2.0）
- [GitHub · genmoai/mochi](https://github.com/genmoai/mochi) ⭐ 官方仓库
- [Genmo 官方博客](https://www.genmo.ai/blog/mochi-1-a-new-sota-in-open-text-to-video) ⭐
- [Genmo Playground 在线试用](https://www.genmo.ai/)
- [Replicate · genmoai/mochi-1](https://replicate.com/genmoai/mochi-1)

### CogVideoX 5B / 1.5（智谱 AI · 清华 / 开源 Apache 2.0）
- [GitHub · zai-org/CogVideo](https://github.com/zai-org/CogVideo) ⭐ 官方仓库
- [HuggingFace · zai-org/CogVideoX-5b](https://huggingface.co/zai-org/CogVideoX-5b)
- [HuggingFace · CogVideoX-5b-I2V](https://huggingface.co/zai-org/CogVideoX-5b-I2V)
- [Promptomania · CogVideoX 模板](https://promptomania.com/models/zhipu/cogvideox)
- [Open Laboratory · CogVideoX 1.5 5B](https://openlaboratory.ai/models/cog-video-x1_5-5b)

### Higgsfield Soul 2.0 / DoP（Higgsfield AI）
- [Higgsfield 官网](https://higgsfield.ai/) ⭐
- [Higgsfield Skills 系统](https://higgsfield.ai/skills)
- [Higgsfield Soul 介绍](https://higgsfield.ai/soul-intro)
- [GitHub · higgsfield-ai-prompt-skill](https://github.com/OSideMedia/higgsfield-ai-prompt-skill) ⭐ Claude AI 集成
- [Higgsfield Blog · AI 短片完整 Prompt 库](https://higgsfield.ai/blog/ai-short-film-youtube-guide)
- [Segmind · Higgsfield Prompt Guide](https://blog.segmind.com/higgsfield-ai-prompt-guide-video-creation/)

---

## 提示词学习

### 综合公式
- 本仓库 [methodology/](methodology/) — 12 篇方法论 SOP（基础公式/进阶公式/分镜时序/情绪外化/运镜词典/约束词/特殊字符/避坑12问/Kling/跨模型对比/Sora/Veo）

### 单模型深入
| 模型 | 推荐资源 |
|---|---|
| Seedance | [Imagine.art 70 条](https://www.imagine.art/blogs/seedance-2-0-prompt-guide) · [Atlas Cloud 含成功率](https://www.atlascloud.ai/blog/guides/best-seedance-2-0-prompts-guide) |
| HappyHorse | [SeaArt 教程](https://www.seaart.ai/blog/happyhorse-prompt-guide) · [CrePal 时序节拍](https://crepal.ai/blog/aivideo/aivideo-happyhorse-1-0-prompts/) |
| Kling | [Atlabs 5 层公式](https://www.atlabs.ai/blog/kling-3-0-prompting-guide-master-ai-video-generation) · [Elser AI 25 条](https://www.elser.ai/blog/kling-ai-prompts-guide-25-cinematic-prompts-that-actually-work-2026) · [vicsee 图生视频 8 条](https://vicsee.com/blog/kling-3-prompts) |
| Sora 2 | [CyberLink 30 条](https://www.cyberlink.com/blog/ai-prompts/5169/best-sora-2-prompts) · [Imagine.art Sora 指南](https://www.imagine.art/blogs/sora-2-prompt-guide) · [Superprompt 完整指南](https://superprompt.com/blog/openai-sora-2-complete-guide) |
| Veo 3 | [GeekVibes 100+ 实测](https://geekvibesnation.com/google-veo-3-prompts-100-tested-examples-that-actually-work-2026/) · [UlazAI 模板](https://ulazai.com/veo3-prompt-examples/) · [Replicate Veo 3 博文](https://replicate.com/blog/using-and-prompting-veo-3) |

---

## 实测与对比博客
- [Leonardo.Ai · Kling Prompts](https://leonardo.ai/news/kling-ai-prompts)
- [Leonardo.Ai · Veo 3 Mastering Prompts](https://leonardo.ai/news/mastering-prompts-for-veo-3)
- [VEED · Kling AI Prompting Guide](https://www.veed.io/learn/kling-ai-prompting-guide) — 含 Kling 子版本对比
- [WaveSpeed · Sora 2 Tips](https://wavespeed.ai/blog/posts/sora-2-prompting-tips-better-videos-2026/)
- [Phygital+ · Kling 3 for Filmmaking](https://phygital.plus/blog/kling-3-ai-video-prompts-guide/)

---

## API 与代码

### Python SDK / 客户端
- **OpenAI**：[openai Python](https://github.com/openai/openai-python) — Sora 2 通过 OpenAI API
- **Google**：[google-genai](https://github.com/googleapis/python-genai) — Veo 3 通过 Vertex AI
- **火山方舟**：[volcengine-python-sdk](https://github.com/volcengine/volcengine-python-sdk)
- **可灵开放平台**：[Kling API 文档](https://klingai.com/document-api)
- **Replicate**（多模型聚合）：[replicate Python](https://github.com/replicate/replicate-python)

### Node / JS
- [openai Node](https://github.com/openai/openai-node)
- [@google/genai](https://www.npmjs.com/package/@google/genai)
- [replicate](https://www.npmjs.com/package/replicate)

---

## 社区与讨论
- **OpenAI Developer Community** — Sora 相关板块
- **r/aivideo**（Reddit） — 跨模型作品分享
- **小红书 #AI视频** — 国内创作者主战场
- **B 站 AI 视频教程** — 中文新手友好

---

## Prompt 互联工具
- **本仓库 [tools/prompt-browser](tools/prompt-browser/)** — 197 条可搜索 / 筛选 / URL 分享 / Drawer 详情
- **本仓库 [skills/](skills/)** — 5 个 Claude Code Skill 自动生成提示词
- **OpenAI Playground** — Sora 在线体验
- **Replicate Playground** — 多模型快速对比
- **AlchemyStudio / Leonardo.Ai** — 集成多模型 + 提示词市场
- **[Vivideo](https://vivideo.ai)** — 集成多模型的文生/图生视频工作台,自动配音

---

## 姊妹方向：图生
视频提示词高度依赖参考图，配套学习这些图生模型很有用：

- **Seedream**（字节）— Seedance 的图生配套
- **Nano Banana**（Google） — Imagen 系
- **FLUX**（Black Forest Labs） — 开源高质量
- **Midjourney v7**

---

## 贡献新资源

发现好资源？通过 PR 加到对应分类下。要求：
- 必须是公开可访问的链接（不要付费墙背后的）
- 写清楚"它解决什么"（一行话）
- 中英文资源都欢迎
