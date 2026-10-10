---
name: kling-prompter
description: 生成符合 Kling 3.0（可灵 3.0，快手）规则的视频提示词。三种写法自适应：4 部分基础公式（短视频）/ 5 层进阶公式（剧情+音频）/ 图生视频专用（只描述运动）。Kling 是 2026 年中文理解最强、原生音画同步、最长 2 分钟、支持角色定向发声、Motion Brush 的电影级模型。用于"用 Kling 生成视频"、"可灵 AI 提示词"、"中文视频生成"、"带原生音频的剧情视频"、"图生视频"、"角色对话视频"等触发场景。
---

# kling-prompter

Kling 3.0（可灵 3.0，快手）的三套主流写法：4 部分基础 / 5 层进阶 / 图生视频。

## 何时不用此 skill

- 复杂多镜头分镜叙事（>15s） → 用 [seedance-storyboard](../seedance-storyboard/)
- 5/10/15 秒紧凑短片，对原生音频要求不高 → 用 [happyhorse-prompter](../happyhorse-prompter/)
- 已有 Seedance 提示词需修问题 → 用 [seedance-debugger](../seedance-debugger/)

## 三套写法决策树

```
你的需求是？
├── 5 秒短视频、单一场景        → 写法 1（4 部分基础公式）
├── 带剧情、带音频、多角色      → 写法 2（5 层进阶公式）★ Kling 强项
└── 已有参考图，只需动起来      → 写法 3（图生视频专用）★ Kling 强项
```

## 工作流程

### 步骤 1：判断写法

| 用户的需求关键词 | 写法 |
|---|---|
| 短视频、TikTok、抖音、循环、爆款、变身 | 写法 1（4 部分） |
| 对话、剧情、配音、CTA、广告、多角色 | 写法 2（5 层） |
| 这张图、参考这张照片、让它动起来 | 写法 3（图生视频） |

### 步骤 2：澄清缺失要素（必要时）

如果信息不够，问 2-3 个关键问题（不是全部）：

| 场景 | 必问的 2-3 项 |
|---|---|
| 短视频 | 主体（具体外观）、动作（动词+终点）、风格（电影感/动漫/赛博朋克） |
| 5 层剧情 | 角色（年龄+服装）、对话内容、要不要原生音频（音乐/音效/voiceover） |
| 图生视频 | 主体在图中做什么变化（不要再描述图本身）、镜头怎么动 |

### 步骤 3：按选定写法填充

#### 写法 1：4 部分基础公式

```
[Subject - 具体视觉细节] [Action - 精确运动+终点] [Context - 3-5 环境元素] [Style - 镜头+灯光+氛围].
```

详细参考 [methodology/09-kling-公式.md](../../methodology/09-kling-公式.md)。

#### 写法 2：5 层进阶公式（Kling 的看家本领）

**强烈推荐用结构化格式**，模型按层解析：

```
Scene: [地点 + 时间 + 氛围]
Characters: [每个角色的具体描述，age + 关键服装/外貌]
Action: [按时间顺序的步骤，体现因果与递进]
Camera: [镜头类型 → 运动 → 切换]
Audio & Style: [对话/音效/音乐 + 视觉风格]
```

> ⚠️ **Audio & Style 这层是 Kling 的差异化卖点**，一定要写！Seedance / HappyHorse 都做不到角色定向发声。

#### 写法 3：图生视频专用

**铁律：只描述运动，不重复图中已有的视觉信息**。

❌ 不要写：`A red sports car with chrome wheels on a wet road...`（图已有）
✅ 直接写：`The headlights blaze on and the engine roars to life. The rear tires spin...`

### 步骤 4：6 条 Kling 写作守则自查

- [ ] 用 **active verbs** 替代笼统词（rockets / slams / erupts）
- [ ] 描述 **时序流**（开头 → 中间 → 结尾）
- [ ] 用 **具体光源** 代替 "dramatic lighting"
- [ ] 加 **触感细节**（grain / reflections / sweat / steam）
- [ ] 加 **显式 endpoint**（防 99% 卡死）：`then settles back / fades out`
- [ ] 幻想场景用 **物理交互锚定**（stone crumbles / torches flicker）

### 步骤 5：决定语言（中文还是英文）

| 场景 | 推荐语言 |
|---|---|
| 中式美学、武侠、汉服、中文台词 | **中文**（Kling 中文理解最强） |
| 国际化、Hollywood 风、产品广告 | 英文 |
| 二者混合 | 选主导风格，**不混用** |

### 步骤 6：加负向提示

```
Negative: cartoonish, 3D render, smooth plastic skin, floating limbs,
         sliding feet, text morphing, no watermark, no logo.
```

需要真人感时加 `smiling` 到 negative（让表情自然）。

### 步骤 7：输出格式

```markdown
## 生成的 Kling 提示词（写法 N）

\`\`\`
[完整提示词]
\`\`\`

**推荐参数**：宽高比 [X:Y] · 时长 [N 秒] · 模型 [Kling 3.0 / Kling O1]
**关键技巧**：[1-2 句说明这条提示词的设计思路]
**可调点**：[告诉用户可以怎么改]
```

### 可选：通过 Atlas Cloud 执行生成

本 skill 默认仍然只负责生成和检查 Kling 提示词。只有用户明确要求直接生成视频，
并且环境中已经配置 `ATLASCLOUD_API_KEY` 时，才可以把最终提示词交给
[`scripts/atlas_generate.py`](scripts/atlas_generate.py) 执行：

```bash
python3 skills/kling-prompter/scripts/atlas_generate.py \
  --prompt-file prompt.txt \
  --aspect-ratio 16:9 \
  --duration 5 \
  --output output.mp4
```

执行器会在每次生成前实时读取 Atlas Cloud 模型目录和目标模型 schema。生成请求只
提交一次，不会因超时或网络错误自动重试；只有结果查询使用有界退避。未配置 Atlas
Cloud 时继续输出提示词即可，不影响本 skill 的默认能力。

## 实战示例

### 例 1：用户要"短视频，女孩变成动漫角色"

**判断**：变身爆款 → 写法 1（4 部分基础）

**输出**：

```
A young woman in casual streetwear standing center frame, her body slowly engulfed by glowing particles as she transforms into a vibrant anime version of herself with stylized hair and large expressive eyes, then settles into her new form. TikTok-style vertical framing, neon pink and cyan rim lighting, smooth transition with sparkle bursts, high-energy K-pop MV aesthetic.

Negative: 3D render, plastic skin, floating limbs, text morphing, watermark.
```

**参数**：9:16 · 5s · Kling 3.0
**关键技巧**：4 要素齐全 — Subject（具体服装）+ Action（带终点：`then settles`）+ Context（3 个：neon rim light/sparkle/vertical）+ Style（K-pop MV aesthetic）。
**可调点**：把 `K-pop MV` 换成 `Cyberpunk` / `Studio Ghibli` 改风格；把 `glowing particles` 换成 `glitch effects` 改变身机制。

---

### 例 2：用户要"两个老朋友 10 年后重逢，要带配音"

**判断**：带剧情 + 带音频 → 写法 2（5 层进阶）

**输出**：

```
Scene: A park bench at golden hour in late autumn, fall leaves drifting through the air, soft amber sunlight slanting through bare branches.

Characters: Two reunited friends with a 10-year gap, both early 30s. Character A wears a wool coat and scarf, slightly nervous. Character B wears a denim jacket, more outwardly emotional.

Action: Character A sits down beside Character B, hesitates, then says "It's been a long time." Character B turns slowly, eyes widening with recognition, replies "Too long. I almost didn't recognize you." They both pause, then share a quiet laugh that breaks the tension.

Camera: Slow push-in on Character A as he speaks, then over-the-shoulder cut to Character B's reaction, ending on a held wide two-shot of both on the bench.

Audio & Style: Soft solo piano underscore building gently, ambient park sounds (distant kids playing, leaves rustling), warm cinematic color grade with teal-and-amber accents, naturalistic dialogue delivery.

Negative: smiling broadly, cartoonish, 3D render, plastic skin, sliding feet, watermark.
```

**参数**：16:9 · 12s · Kling 3.0（推荐）
**关键技巧**：5 层全开。Characters 层给两个角色各自的「锚点服装」防漂移；Action 层用因果链（坐下 → 犹豫 → 开口 → 反应 → 共同笑）让叙事自然；Audio & Style 层既给音乐又给环境音，触发 Kling 原生音画同步。
**可调点**：换 `golden hour` → `blue hour` 改基调；换 `piano underscore` → `silence + only ambient` 让情感更克制。

---

### 例 3：用户上传了一张厨房照片，想"让它动起来，厨师颠炒"

**判断**：图生视频 → 写法 3

**输出**：

```
The chef flips the wok hard, launching noodles into the air as a fireball erupts upward. He catches them clean, tilts the wok and slides the dish onto a plate with his spatula, then pushes the plate across the worn counter toward the camera with a grin. Steam billows upward through the lantern light.

Negative: floating limbs, plastic skin, sliding feet, watermark.
```

**参数**：16:9 · 8s · Kling 3.0
**关键技巧**：完全没重描述图中的厨房布局/厨师外貌（图自己有），只写运动序列（flip → fire → catch → slide → push）+ 物理细节（steam billows）。明火创造动态光照是 Kling 的强项。
**可调点**：删 `fireball erupts` 改成温和炒制；把 `with a grin` 删掉让表情更专注。

## 参考资源

- Kling 完整方法论：[methodology/09-kling-公式.md](../../methodology/09-kling-公式.md)
- 36 条实测提示词：[prompts/kling/README.md](../../prompts/kling/README.md)
- 运镜词典（通用）：[methodology/05-运镜词典.md](../../methodology/05-运镜词典.md)
- 官方平台：[klingai.com](https://klingai.com)
