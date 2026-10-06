# 提示词库 · 594 条(484 分散 + 110 跨模型对照)

## 概览

### 📚 分散提示词(按单模型最佳实践)· 484 条 / 22 模型

| 模型 | 数量 | 索引 / JSON 前缀 |
|---|---|---|
| **Doubao Seedance 2.0** | 117 条 | [seedance/README.md](seedance/README.md) · `se-*` |
| **HappyHorse 1.0** | 90 条 | [happyhorse/README.md](happyhorse/README.md) · `ha-*` |
| **Kling 3.0 (可灵)** | 72 条 | [kling/README.md](kling/README.md) · `kl-*` |
| **Kling 4.0 (可灵)** | 12 条 | [kling-4.0/README.md](kling-4.0/README.md) · `kl-*` |
| **Sora 2** | 26 条 | [sora/README.md](sora/README.md) · `so-*` |
| **Veo 3.1** | 31 条 | [veo/README.md](veo/README.md) · `ve-*` |
| **Runway Gen-4.5 / Aleph** | 12 条 | `runway-gen4` (仅在 JSON) |
| **Runway Aleph 2.0** | 2 条 | [runway-aleph-2.0/README.md](runway-aleph-2.0/README.md) · `ru-*` |
| **Pika 2.5** | 12 条 | `pika-2.5` (仅在 JSON) |
| **Hailuo 02 (海螺)** | 12 条 | `hailuo-02` (仅在 JSON) |
| **MiniMax H3** | 10 条 | [minimax-h3/README.md](minimax-h3/README.md) · `mi-*` |
| **Hunyuan Video 1.5** | 12 条 | `hunyuan-video` (仅在 JSON) |
| **Wan 2.7 (通义万相)** | 12 条 | `wan-2.5` (仅在 JSON) |
| **Wan 2.6（万相）** | 1 条 | [wan-2.6/README.md](wan-2.6/README.md) · `wa-*` |
| **即梦 AI (Seedance 2.0 引擎)** | 12 条 | `jimeng-3` (仅在 JSON) |
| **Luma Ray 3.2** | 2 条 | [luma-ray-3.2/README.md](luma-ray-3.2/README.md) · `lu-*` |
| **LTX-Video 0.9.7** | 8 条 | `ltx-video` (仅在 JSON) |
| **Mochi 1** | 8 条 | `mochi-1` (仅在 JSON) |
| **CogVideoX 5B / 1.5** | 8 条 | `cogvideox-5b` (仅在 JSON) |
| **Higgsfield Soul 2.0 / DoP** | 9 条 | `higgsfield-soul` (仅在 JSON) |
| **Gemini Omni (Omni Flash)** | 12 条 | [gemini-omni/README.md](gemini-omni/README.md) · `ge-*` |
| **Seedance 2.5（即梦）** | 4 条 | [seedance-2.5/README.md](seedance-2.5/README.md) · `se-*` |
| **总计** | **484 条** | [data/all-prompts.json](data/all-prompts.json) |

### 🔀 跨模型对照矩阵 · 110 条 / 10 场景 × 11 商业模型

| 资源 | 内容 | 文件 |
|---|---|---|
| 跨模型 JSON | 同一场景在 11 模型上的最佳 prompt 对照 | [data/cross-model-matrix.json](data/cross-model-matrix.json) |
| Markdown 索引 | 10 场景导览 + 各场景方法对照表 | [cross-model/README.md](cross-model/README.md) |
| Web 专页 | Liquid Glass 风格的横向对比 | [`tools/cross-model/index.html`](../tools/cross-model/index.html) |

**10 个场景**:产品广告 / 双人对话 / 物理动作 / 图生视频 / 多人会议 / 恐怖悬疑 / 自然延时 / 抽象艺术 / 武侠 / 萌宠

> 这份矩阵是 `prompt-translator` skill 的查表基准 — 跨模型转换不靠 LLM 直觉,靠真实人工对照数据。

## 怎么用

**人类阅读**:直接看 [seedance/](seedance/) / [happyhorse/](happyhorse/) / [kling/](kling/) / [sora/](sora/) / [veo/](veo/) 的分类索引(其余 10 模型直接读 JSON 或用 Web 工具)。

**程序消费**:[data/all-prompts.json](data/all-prompts.json) 是单一数据源,[Web 浏览器](../tools/prompt-browser/index.html) 直接读这个文件。

**跨模型对比**:[data/cross-model-matrix.json](data/cross-model-matrix.json) — 想知道"同样一个香水广告各家怎么写"就看这个。

## 数据 Schema

每条提示词的字段:

```json
{
  "id": "sd-001",                          // 唯一 ID,前缀对应模型(sd/hh/kl/so/ve/rw/pk/hl/hy/wn/jm/lt/mo/cg/hg)
  "model": "seedance-2.0",                 // 15 个 model id 之一
  "category": "product-commercial",        // 见下方 categories 列表(29 个)
  "title": "奢华产品展示(万能模板)",
  "prompt": "A luxury [product]...",       // 完整提示词
  "tags": ["product", "luxury", "..."],    // 用于筛选
  "params": {                              // 推荐生成参数
    "aspect": "9:16",                      // 宽高比
    "duration": "8s",                      // 时长
    "resolution": "1080p"                  // 分辨率(部分模型可省略)
  },
  "source": {                              // 来源
    "name": "Atlas Cloud",
    "url": "https://..."
  },
  "notes": "替换 [product] 适用于…"        // 可选,使用建议
}
```

## 分类(categories · 29 个)

| ID | 中文 | 主要适用模型 |
|---|---|---|
| `product-commercial` | 产品与商业广告 | 全部 |
| `social-viral` | 社交媒体爆款 | seedance / happyhorse |
| `cinematic` | 电影叙事与戏剧场景 | seedance / sora / veo / higgsfield |
| `cinematic-styles` | 电影风格 | happyhorse / cogvideox |
| `cinematic-timed` | 时序节拍电影感 | happyhorse |
| `dialogue` | 对话驱动 | sora / veo / kling / higgsfield |
| `action` | 动作格斗与追逐 | 全部 |
| `sports` | 体育、赛车与武术 | seedance / hailuo |
| `nature` | 自然、风景与天气 | seedance / happyhorse / hailuo / ltx |
| `nature-timelapse` | 自然延时 | 跨模型 |
| `quiet-moments` | 安静时刻与生活切片 | seedance / ltx / mochi |
| `fantasy-scifi` | 奇幻与科幻 | seedance / sora / runway |
| `creative` | 创意与实验性 | 全部 |
| `experimental` | 实验与超现实 | kling / mochi |
| `abstract-art` | 抽象艺术 | 跨模型 |
| `asmr` | ASMR 与感官体验 | seedance |
| `comedy` | 喜剧与概念性 | seedance / sora |
| `craft` | 工艺、艺术与现场表演 | seedance |
| `portrait` | 人物与肖像 | happyhorse / higgsfield |
| `viral-transform` | 病毒变身与转场 | kling / pika |
| `music-video` | 音乐 MV 与表演 | kling / higgsfield |
| `gaming-ip` | 游戏与 IP 风 | kling |
| `image-to-video` | 图生视频专项 | kling / runway / cogvideox |
| `video-edit` | 视频编辑(add/remove/relight) | runway-aleph |
| `pikaffects` | Pika 特效(Melt/Explode/Squish) | pika |
| `physics-sim` | 物理仿真 | hailuo / mochi |
| `lip-sync` | 数字人唇形同步 | wan / kling |
| `chinese-native` | 中式美学(汉服/水墨/江南) | jimeng / wan / cogvideox |
| `open-source` | 开源专属(本地部署/LoRA) | hunyuan / ltx / mochi / cogvideox |
| `horror-suspense` | 恐怖悬疑 | sora / runway / kling |
| `wuxia-martial` | 武侠 | kling / jimeng / hunyuan |
| `pets-cute` | 萌宠 | 跨模型 |
| `multi-person-meeting` | 多人会议/多角色 | veo / kling / sora |

> 实际 JSON 中可能有未列出的衍生分类,以 [data/all-prompts.json](data/all-prompts.json) 的 `categories` 字段为准。

## 贡献新提示词

1. 用上面 Schema 在 [data/all-prompts.json](data/all-prompts.json) 里加一条
2. 选择最贴近的 `category`(不够用就提 PR 加新 category)
3. 至少打 3 个 `tags`(便于 Web 工具筛选)
4. 提交前在对应平台实测过,最好附带成功率
5. 一站式表单:[New Prompt 模板](../.github/ISSUE_TEMPLATE/new-prompt.yml)

## 来源致谢(按权威度排序)

| 优先级 | 来源 | 贡献 |
|---|---|---|
| ⭐⭐⭐⭐⭐ | [OpenAI Cookbook](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide) | Sora 2 官方分层公式 |
| ⭐⭐⭐⭐⭐ | [Google DeepMind](https://deepmind.google/models/veo/prompt-guide/) | Veo 3 官方 8 元素公式 |
| ⭐⭐⭐⭐⭐ | 火山方舟 PDF | Seedance 2.0 53 页官方指南 |
| ⭐⭐⭐⭐⭐ | [Atlabs AI](https://www.atlabs.ai/blog/kling-3-0-prompting-guide-master-ai-video-generation) | Kling 5 层公式 |
| ⭐⭐⭐⭐⭐ | [Runway](https://help.runwayml.com/) | Gen-4 + Aleph 官方指南 |
| ⭐⭐⭐⭐⭐ | [Lightricks LTX-Video](https://github.com/Lightricks/LTX-Video) | LTX 0.9.7 单段 prose 公式 |
| ⭐⭐⭐⭐⭐ | [Genmo Mochi](https://github.com/genmoai/mochi) | Mochi 1 10B AsymmDiT |
| ⭐⭐⭐⭐⭐ | [智谱 CogVideoX](https://github.com/zai-org/CogVideo) | 226 token 长 prompt + I2V 权重 |
| ⭐⭐⭐⭐⭐ | [Higgsfield AI](https://higgsfield.ai/) | Soul ID + DoP 模板 + AI Director |
| ⭐⭐⭐⭐ | [Tencent HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) | 开源最强 + LoRA |
| ⭐⭐⭐⭐ | [MiniMax 文档](https://platform.minimax.io/docs/guides/video-generation) | Hailuo 02 物理仿真 |
| ⭐⭐⭐⭐ | [Alibaba Wan Guide](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt) | Wan 2.7 数字人 lip-sync |
| ⭐⭐⭐⭐ | [Pika Labs](https://pikaslabs.com/pika-2.5/) | Pikaffects + Pikaframes |
| ⭐⭐⭐⭐ | [Imagine.art](https://www.imagine.art/blogs/seedance-2-0-prompt-guide) | Seedance 70 条精选 |
| ⭐⭐⭐⭐ | [Try Happy Horse AI](https://tryhappyhorseai.com/blog/happy-horse-ai-prompts) | HappyHorse 规则化验证 |
| ⭐⭐⭐ | 其余 8 大测评博客 | Elser AI / CyberLink / GeekVibes / CrePal 等补充示例 |

完整资源:[RESOURCES.md](../RESOURCES.md)
