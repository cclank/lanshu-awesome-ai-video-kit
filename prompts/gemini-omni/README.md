# Gemini Omni · 提示词索引（12 条）

> **Gemini Omni / Omni Flash**(Google AI / DeepMind,2026-05-19 发布)是 Google 的跨模态统一模型 — any input(text/image/video/audio/script)→ any output,starting with video。已上线 Gemini App / Flow / GoogleFlowMusic / YouTube Shorts / Create 多平台。

**核心差异化能力**(其他模型不具备或弱):
- 🔥 **迭代编辑**(targeted updates 不重写)— 一句话改一个细节,核心结构保留
- 🔥 **文字渲染**(typography / 空间放置 / 动画风格 / motion-tracked 3D hover / leader lines)
- 🔥 **Real-World 知识利用**(用文化锚点 / 历史时代 / 科学术语直接当 prompt)
- 🔥 **中途改动作**(修改 pacing/emotion 保持角色连续性)

权威源:[Google AI 官方推文 — Mastering Gemini Omni](https://x.com/GoogleAI/status/2059381218660270435)(全部 10 条 prompt source.tier = `official`)。详见方法论 [methodology/16-gemini-omni-公式.md](../../methodology/16-gemini-omni-公式.md)。

## 目录

- [🎨 文字渲染(Gemini Omni 强项)](#-文字渲染gemini-omni-强项) (3)
- [🧠 Real-World 锚点(极简 prompt)](#-real-world-锚点极简-prompt) (2)
- [✂️ 迭代编辑(targeted updates)](#-迭代编辑targeted-updates) (3)
- [🎬 动作即时修改](#-动作即时修改) (2)
- [🆕 2026-10 新增](#🆕-2026-10-新增) (2)

---

## 🎨 文字渲染（Gemini Omni 强项）

### gm-001 · 26 字母物品节拍剪辑（Google AI 官方样板)
`text-rendering` `rapid-fire` `alphabet` `educational` `google-official` · 16:9 / ~10s · [Google AI · Mastering Gemini Omni](https://x.com/GoogleAI/status/2059381218660270435)

```
The video shows items of the alphabet. An unusual item starting with each letter is shown sitting on a table (like a Capybara for C, disco globe for D and Lava Lamp for L). All 26 letters must be represented by 26 items with matching lower thirds displaying the letter. Only one item and lower third at a time. Each lower third must look like a black marker written on a slip of paper in the bottom left. Rapid fire, roughly 9 frames per item at 24FPS. Last frame is a slip of paper "THE END." The whole video is accompanied by calm smooth music.
```

> 💡 展示 Gemini Omni 复杂 text rendering 能力(lower thirds + 黑色 marker 风格 + 严格 24FPS 节拍 + 26 物品逐个 + 收尾文字帧)。

### gm-004 · 节拍逐词文字 sizzle reel
`text-rendering` `typography` `rhythm` `sizzle-reel` `google-official` · 16:9 / 5s · [Google AI · Tip 2 Text Rendering](https://x.com/GoogleAI/status/2059381218660270435)

```
word by word, one word on the screen at a time: did, you, know, that, this, model, can, do, pretty, good, text!? Each word appears with a different animated style, perfect pacing to a rhythm, sizzle reel.
```

> 💡 关键词:`word by word` + `Each word ... different animated style` + `perfect pacing to a rhythm`。

### gm-005 · 浮动 3D 文字 Intrusive Thoughts
`text-rendering` `motion-tracked` `3d-text` `monologue` `absurd` `google-official` · 16:9 / 10s · [Google AI · Tip 2 Text Rendering (Intrusive Thoughts)](https://x.com/GoogleAI/status/2059381218660270435)

```
Overlay motion-tracked, minimalist text commentary onto the physical environment of the video. This text represents [the subject] deadpan, immediate inner monologue that's observant, slightly absurd, and life-contemplating. Think "intrusive thoughts." Clean, white, lowercase sans-serif text (like Helvetica or Inter). The text hovers in 3D space, connected to the subjects being commented on via ultra-thin, crisp, white leader lines.
```

> 💡 业界独家能力 — `motion-tracked` + `3D space hover` + `ultra-thin white leader lines` 把内心独白可视化。

---

## 🧠 Real-World 锚点（极简 prompt）

### gm-002 · 火星宇航员 POV（4 个词极简）
`minimal-prompt` `pov` `space` `real-world-knowledge` `google-official` · 16:9 / 8s · [Google AI · Tip 1 Real-World Knowledge](https://x.com/GoogleAI/status/2059381218660270435)

```
Astronaut's POV on Mars
```

> 💡 4 个词出整片 — Gemini Omni 自动还原火星地貌 + EVA 服 + POV 视角。**核心理念:不要过度描述,锚点足够**。

### gm-003 · Rube Goldberg 大理石链反应
`minimal-prompt` `physics` `marble` `continuous-shot` `google-official` · 16:9 / 8s · [Google AI · Tip 1 Real-World Knowledge](https://x.com/GoogleAI/status/2059381218660270435)

```
A marble rolling fast on a chain reaction style track, continuous smooth shot
```

> 💡 用 `chain reaction style` 这一个锚点 → 模型还原 Rube Goldberg 复杂物理装置。

---

## ✂️ 迭代编辑（targeted updates,Gemini Omni 核心差异化）

> 工作流:第一次生成完整视频 → 用极简 prompt 改一个细节 → 模型**保留其他元素只改你说的部分** → 可叠加多次迭代。

### gm-006 · 迭代编辑:把小提琴移到新环境
`iterative-edit` `environment-change` `minimal-prompt` `google-official` · 16:9 / 5s · [Google AI · Tip 4 Edit Iteratively](https://x.com/GoogleAI/status/2059381218660270435)

```
Transport the violin to a new environment
```

### gm-007 · 迭代编辑:小提琴隐形
`iterative-edit` `vfx` `invisibility` `minimal-prompt` `google-official` · 16:9 / 5s · [Google AI · Tip 4 Edit Iteratively](https://x.com/GoogleAI/status/2059381218660270435)

```
Make the violin invisible
```

### gm-008 · 迭代编辑:换镜头角度(over-shoulder)
`iterative-edit` `camera-angle` `over-shoulder` `minimal-prompt` `google-official` · 16:9 / 5s · [Google AI · Tip 4 Edit Iteratively](https://x.com/GoogleAI/status/2059381218660270435)

```
Change the camera angle so it's looking over the violinist's shoulder
```

> 💡 这 3 条是连续迭代示例 — 同一基础视频上叠加 3 次极简编辑。**其他模型无此能力**(都得重写完整 prompt 从头跑)。

---

## 🎬 动作即时修改

> 修改角色 pacing / emotion / interaction,**保持角色模型连续性不破坏**。

### gm-009 · 动作即时修改:踮脚走
`action-modify` `character-control` `minimal-prompt` `google-official` · 16:9 / 5s · [Google AI · Tip 5 Change Action on the Fly](https://x.com/GoogleAI/status/2059381218660270435)

```
Make the character walk on their tiptoes
```

### gm-010 · 动作即时修改:跳起
`action-modify` `character-control` `minimal-prompt` `google-official` · 16:9 / 5s · [Google AI · Tip 5 Change Action on the Fly](https://x.com/GoogleAI/status/2059381218660270435)

```
Have them leap into the air
```

> 💡 关键句式:`Make X verb` / `Have them <action>` / `Now they <action>`。保连续性是关键。

---

## 📚 相关资源

- 方法论:[methodology/16-gemini-omni-公式.md](../../methodology/16-gemini-omni-公式.md) — 5 大 prompting tips 详解 + 与 Veo 3.1/Sora 2 对比
- 跨模型对比:[methodology/10-跨模型对比.md](../../methodology/10-跨模型对比.md)
- Google AI 官方推文(唯一权威源):[X · Mastering Gemini Omni](https://x.com/GoogleAI/status/2059381218660270435)
- 在线试用平台:
  - [Gemini App](https://gemini.google.com/)
  - [Flow by Google](https://flow.google.com/)
  - [Google Flow Music](https://flow.google.com/music)
  - YouTube Shorts(Create 入口)

## 🆕 2026-10 新增（2 条）

### gm-011 · Gemini Omni 一句话转绘
`gemini-omni` `video-edit` · [explainx.ai](https://explainx.ai/blog/runway-aleph-2-vs-gemini-omni-video-2026)

```
Turn this cooking video into a Studio Ghibli animation
```

> 💡 Gemini Omni “remix”重绘范式代表：一句话整体转绘，与 Aleph 精确编辑形成对照

### gm-012 · Gemini Omni Vids 航拍雪山
`gemini-omni` `nature` `aerial` · [aitoolharbor.blogspot.com](http://aitoolharbor.blogspot.com/2026/09/google-vids-ai-video-generator-2026.html)

```
A cinematic aerial view of snow-covered mountains at sunrise, with clouds moving slowly through the valley and warm golden lighting.
```

> 💡 Google Vids 9-23 免费开放 Gemini Omni 1.1 Flash 后的官方写法示例，配合 exact duration 与 scene extension 新功能

---

## 一句话总结

**如果你需要文字渲染 / 迭代编辑 / 不重写改细节** → Gemini Omni。
**如果你需要原生音频 + 多人对话 + 长片** → 仍然 Veo 3.1。
**如果你需要电影质感 + 物理仿真** → 仍然 Sora 2。
