# Sora 2 · 提示词索引（23 条）

> **Sora 2**（OpenAI，2025 年 9 月 30 日发布）是 OpenAI 的旗舰视频模型。原生音画一体（含对白生成），支持 Cameos 真人客串、极致物理仿真。最大 20 秒、80-150 词最优。

OpenAI 官方提倡两套写法：**结构化分层（Shot List）** 和 **超精细参数化（Format & Look + Lenses + Grade + Lighting + Sound 等 8 层）**。详见 [methodology/11-sora-公式.md](../../methodology/11-sora-公式.md)。

## 目录

- [🎬 电影叙事（OpenAI 官方样板）](#-电影叙事openai-官方样板) (4)
- [😆 喜剧与 meme](#-喜剧与-meme) (4)
- [🎭 安静时刻与情感](#-安静时刻与情感) (3)
- [💬 对话驱动](#-对话驱动) (2)
- [⚡ 动作与电影感](#-动作与电影感) (3)
- [👻 恐怖与悬疑](#-恐怖与悬疑) (3)
- [📰 纪录片](#-纪录片) (1)
- [🆕 2026-10 新增](#🆕-2026-10-新增) (3)

---

## 🎬 电影叙事（OpenAI 官方样板）

### so-001 · 机械工坊小机器人（OpenAI 官方 Shot List 样板）
`sora-cookbook` `animation` `shot-list` `dialogue` `audio` · 16:9 / 4s · [OpenAI Cookbook](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)

```
Style: Hand-painted 2D/3D hybrid animation with soft brush textures, warm tungsten lighting, and tactile stop-motion feel. Mid-2000s storybook animation aesthetic—cozy, imperfect, mechanical charm. Watercolor wash, painterly textures, warm–cool balance, filmic motion blur.

Inside cluttered workshop with gear-laden shelves and blueprints. Small round robot sits on wooden bench, dented body with mismatched patches. Large glowing blue eyes flicker as it fiddles with humming light bulb.

Cinematography: Medium close-up, slow push-in with parallax from hanging tools. 35mm virtual lens, shallow DOF softening background. Warm overhead practical key; cool window spill. Gentle, whimsical, slightly suspenseful mood.

Actions:
- Robot taps bulb; sparks crackle
- Flinches, dropping bulb, eyes widen
- Bulb tumbles in slow motion; catches it
- Steam escapes chest—relief and pride
- Robot says: "Almost lost it… but I got it!"

Background Sound: Rain, ticking clock, soft mechanical hum, faint bulb sizzle.
```
> 💡 Sora 2 官方推荐分层结构：**Style → Scene → Cinematography → Actions（按 beats）→ Sound**

### so-002 · 70 年代屋顶浪漫（OpenAI 官方）
`sora-cookbook` `period` `romance` `35mm` `dialogue` · 16:9 / 8s · [OpenAI Cookbook](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)

```
Style: 1970s romantic drama, shot on 35mm film with natural flares, soft focus, warm halation. Slight gate weave and handheld micro-shake evoke vintage intimacy. Warm Kodak-inspired grade; light halation on bulbs; film grain and soft vignette for period authenticity.

At golden hour, brick tenement rooftop transforms into small stage. Laundry lines strung with white sheets sway in wind. Mismatched fairy bulbs hum overhead. Young woman in flowing red silk dress dances barefoot, curls glowing. Partner—sleeves rolled, suspenders loose—claps along.

Cinematography: Medium-wide shot, slow dolly-in from eye level. 40mm spherical lens, shallow focus isolating couple from skyline. Golden natural key with tungsten bounce; edge from fairy bulbs. Nostalgic, tender, cinematic mood.

Actions:
- She spins; dress flares catching sunlight
- Woman (laughing): "See? Even the city dances with us tonight."
- He steps in, catches her hand, dips her into shadow
- Man (smiling): "Only because you lead."
- Sheets drift across frame, briefly veil skyline before parting

Background Sound: Natural ambience only—wind, fabric flutter, street noise, muffled music. No added score.
```

### so-003 · 通勤站台超精细参数化（OpenAI 官方）
`sora-cookbook` `ultra-detailed` `cinematography` `technical` · 21:9 / 4s · [OpenAI Cookbook](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)

```
Format & Look: Duration 4s; 180° shutter; digital capture emulating 65mm photochemical contrast; fine grain; subtle halation on speculars; no gate weave.

Lenses & Filtration: 32mm / 50mm spherical primes; Black Pro-Mist 1/4; slight CPL rotation to manage glass reflections on train windows.

Grade/Palette: Highlights—clean morning sunlight with amber lift. Mids—balanced neutrals with slight teal cast in shadows. Blacks—soft, neutral with mild lift.

Lighting & Atmosphere: Natural sunlight from camera left (07:30 AM). 4×4 ultrabounce silver; negative fill from opposite wall. Gentle mist; train exhaust drift.

Location & Framing: Urban commuter platform at dawn. Foreground—yellow safety line, coffee cup. Midground—silhouetted passengers in haze. Background—arriving train braking.

Wardrobe: Mid-30s traveler, navy coat, backpack, holding phone loosely.

Sound: Diegetic only—rail screech, train brakes, muffled announcement, ambient hum, footsteps, paper rustle.
```
> 💡 「制作蓝皮书」级模板：Format → Lenses → Grade → Lighting → Location → Wardrobe → Sound

### so-011 · 地铁站台的对视
`romance` `single-moment` · 16:9 / 5s · [CyberLink](https://www.cyberlink.com/blog/ai-prompts/5169/best-sora-2-prompts)

```
A couple locking eyes across a crowded subway platform.
```

### so-014 · 雾中独行英雄
`minimalist` `epic` `title-card` · 21:9 / 5s · [CyberLink](https://www.cyberlink.com/blog/ai-prompts/5169/best-sora-2-prompts)

```
A hero walks alone through fog as a title card fades in.
```

---

## 😆 喜剧与 meme

### so-004 · 西装猫励志演讲
`comedy` `anthropomorphic` `office` · 16:9 / 5s

```
A cat in a business suit delivers a motivational speech to bored office workers.
```

### so-005 · 默片风分心男友 meme
`comedy` `meme` `silent-film` `vintage` · 4:3 / 5s

```
A "Distracted Boyfriend" meme recreated in a 1920s silent film style, grainy texture, over-the-top acting.
```

### so-006 · 松鼠偷零食纪录片
`comedy` `documentary` `voiceover` `audio` · 16:9 / 8s

```
A serious nature documentary voiceover about a squirrel stealing snacks.
```

### so-019 · 戴墨镜冲浪的金毛
`comedy` `pet` `lifestyle` · 9:16 / 5s

```
A Golden Retriever wearing sunglasses dancing on a moving surfboard, looking incredibly chill.
```

---

## 🎭 安静时刻与情感

### so-007 · 钢琴上的时光倒影
`emotional` `metaphor` `music` · 16:9 / 6s

```
Close-up on an elderly woman's hands playing a piano. As she plays, the reflection in the wood shows her younger self's hands.
```

### so-008 · 20 年后的火车站重逢
`emotional` `reunion` · 16:9 / 8s

```
Two old friends reunite at a quiet train station after 20 years.
```

### so-009 · 雨天长椅上的手写信
`emotional` `rain` `atmospheric` · 16:9 / 5s

```
A child leaves a handwritten note on a rainy bus stop bench.
```

---

## 💬 对话驱动

### so-010 · 巴黎雨夜阳台对舞（带对白）
`romance` `35mm` `dialogue` `audio` `paris` · 16:9 / 5s

```
35mm film, golden hour. A couple dances on a rainy Parisian balcony. Dialogue: "Don't let go." Ambience: Soft accordion and rain.
```
> 💡 Sora 2 原生音画 + 对白的紧凑示范，含 ambience 标记

### so-012 · 情书旁白下的夜城
`romance` `voiceover` `audio` `montage` · 16:9 / 8s

```
A handwritten love letter read aloud over city night shots.
```

---

## ⚡ 动作与电影感

### so-013 · 山路无人机追车（带音效）
`action` `drone` `car` `audio` · 21:9 / 8s

```
High-octane drone shot chasing a red sports car through a mountain pass. Sound: Roaring engine and epic orchestral swell.
```

### so-015 · 无声蒙太奇
`montage` `tension` `silence` · 16:9 / 5s

```
A montage of intense close-ups cut to silence.
```

---

## 👻 恐怖与悬疑

### so-016 · 影子独立移动的走廊
`horror` `atmospheric` `supernatural` · 16:9 / 6s

```
A flickering hallway where shadows move independently.
```

### so-017 · 监控录像里站立太久的身影
`horror` `found-footage` `minimal` · 4:3 / 8s

```
A night security camera captures something standing still for too long.
```

### so-018 · 走廊深处飘来的红气球
`horror` `found-footage` `iconic` `slow-burn` · 16:9 / 6s

```
A handheld "found footage" style shot of a long, dark hallway. A single red balloon floats slowly toward the camera.
```

---

## 📰 纪录片

### so-020 · 十张面孔回答同一个问题
`documentary` `interview` `repetition` · 16:9 / 8s

```
A single question answered by ten different faces.
```

---

## 🆕 2026-10 新增（3 条）

### so-021 · 孔雀岛延时巨变：从热带荒岛到璀璨都市
`sora-2` `cinematic` `close-up` `aerial` `drone` `night` · [sifuyik (Substack)](https://sifuyik.substack.com/p/726-viral-video-prompt-timelapse)

```
Theme: A lush tropical island shaped like a peacock undergoes rapid urbanization into a glittering megacity

Visuals: Aerial view of a peacock-shaped island with natural vegetation forming tail-feather patterns, surrounded by turquoise ocean and blue sky. The island transforms through deforestation, construction, city-building, sunset, and finally a luminous night metropolis with a jewel-encrusted peacock head structure.

Camera: Wide high-angle aerial drone view throughout, ending with a rapid zoom-in through the city streets to a low-angle close-up of the glowing peacock head.

Style: Photorealistic, cinematic time-lapse, vibrant tropical colors shifting to warm sunset tones and finally cool night illumination.

Action + Sound Design:
[0-2s] Wide aerial shot of the pristine green peacock-shaped island, vegetation forming detailed eye-spot tail patterns, turquoise water and bright blue sky — calm orchestral strings, gentle ocean waves cut
[2-7s] The island rapidly transforms: green vegetation recedes into brown earth, logging operations begin, heavy machinery and cargo ships appear, construction cranes rise across the landscape — sounds of chainsaws, heavy machinery, building ambience cut
[7-10s] Skyscrapers and city infrastructure rise rapidly across the island, roads and buildings take shape, the peacock head structure begins forming, daylight shifts to late afternoon — construction sounds intensifying, uplifting orchestral build cut
[10-13s] The city is fully built as the sun sets, casting fiery orange and gold light across the water and buildings, the peacock tail pattern now defined by roads and districts, a cruise ship passes in the background — warm sunset orchestral swell, distant city hum cut
[13-16s] Night falls, the city lights turn on illuminating the peacock tail pattern with golden streetlights, the diamond peacock head structure glows brilliantly against the dark sky — nocturnal orchestral score, gentle ocean waves, distant traffic cut
[16-18s] The camera rapidly zooms forward from the wide aerial view, flying through illuminated skyscrapers and busy highways toward the glowing peacock head — rushing wind, building orchestral crescendo cut
[18-20s] Low-angle close-up of the intricate jewel-encrusted peacock head structure glowing magnificently against the night sky, city lights and ocean in the background — powerful orchestral finale, shimmering magical tone
```

> 💡 9 月病毒社区爆款：20 秒分段时间轴 + 全程音效同步的延时转场写法（通用型，Ve o 3/Sora 2 均可）；以异形岛屿形状做贯穿视觉锚点。

### so-022 · 打破画框：从复古电视走进现实，再踏入黑边
`sora-2` `creative` `night` · [sifuyik (Substack)](https://sifuyik.substack.com/p/743-viral-video-prompt)

```
First Frame Image Prompt @Image 1

A wide cinematic shot of a cozy, retro 1970s living room at night, warmly lit by a table lamp with a soft orange shade on the right and a stone fireplace with a glowing fire on the left. The room has earthy tones: warm brown wooden floor and furniture, a muted green mid-century armchair, built-in bookshelves filled with books behind it, and a patterned rug. On the right, a large vintage wooden television set sits on a low wooden console table, next to a rotary phone on a shelf. Inside the TV screen, an Asian man in his 30s, wearing a simple, timeless outfit (a button-up shirt and trousers), stands against a flat, light gray background, looking directly ahead with a calm, composed expression. Thick black cinematic letterbox bars frame the top and bottom of the image. The atmosphere is nostalgic, surreal, and warmly atmospheric.

Image-to-Video Prompt

Theme: A man breaks out of a vintage TV screen, crosses into the physical living room, and ultimately steps beyond the video frame itself into the black letterbox space

Visuals: Cozy 1970s living room with warm lamp and fireplace lighting, vintage wooden TV, green armchair, bookshelves, patterned rug — contrasted against the sterile gray broadcast world inside the television. An Asian man with a calm, confident presence transitions from the flat TV image into a three-dimensional physical presence, with lighting realistically adapting from bright flat broadcast light to warm ambient room light

Camera: Static wide shot holding the room, then a slow, smooth dolly zoom-in toward the man as they walk forward, tilting upward as they climb out of frame, ending on the man standing fully within the black bar space, facing the viewer

Style: Cinematic, magical realism, retro-futuristic, warm earthy color palette, soft atmospheric lighting, surreal fourth-wall break

VO Voice Style: Calm, warm, slightly contemplative male voice — measured pacing, cinematic trailer tone, with a sense of quiet wonder building into inspiration

Action + Sound Design:
[0-2s] The man stands inside the vintage TV screen while the room remains still. Subtle electronic static hum and warm fireplace ambience.
VO: "We spend our whole lives... watching."
On-screen text appears: "Who said you have to stay inside the lines?"
[2-7.5s] The man reaches forward, physically steps out through the TV screen into the living room, and begins walking calmly toward the camera. The lighting on his clothing and skin dynamically shifts from flat broadcast light to warm room light. Soft footsteps on wood, subtle electronic glitch sound as he crosses the threshold.
VO: "But somewhere along the way... we forgot we could step in." @Image 2
On-screen text appears: "Break the frame."
[7.5-10.5s] The man continues walking toward the camera, climb over the sofa and stepping directly into the black letterbox bar at the bottom of the frame. His full body — legs, torso, and head — crosses into the black space, now standing there as if it's solid ground.
VO: "The frame was never the limit."
On-screen text appears: "Step outside."
[10.5-12s] Now standing fully inside the black bar space, facing the viewer, the man raises his right hand and points his index finger directly at the camera, with a subtle, confident smile.
VO: "So— what's stopping you?"
Final on-screen text appears: "Make your own!"
```

> 💡 第四面墙破框创意：首帧图 + I2V + VO + 屏幕文字的完整组合写法（通用型）；灯光从“电视平光”动态切换为“房间暖光”是关键细节。

### so-023 · 古地图活化成微缩世界（4 段定时）
`sora-2` `image-to-video` `aerial` · 9:16 / 3s · [sifuyik (Substack)](https://sifuyik.substack.com/p/15-top-viral-ai-tools-and-tips-today-257)

```
(来源仅给出描述，按其给出的完整描述转录) #745 Viral Video Prompt: Map to Live — a copy-paste vertical 9:16 4K HDR video prompt where an antique paper map physically transforms into a living miniature world. 4 timed scenes: 0 to 3 seconds macro hook of the ordinary map, 3 to 7 transformation, 7 to 11 dive into the world, 11 to 15 aerial reveal. Mountains rise, rivers carve and flow, forests grow, roads emerge and miniature towns build along them. A tiny vintage car drives through a mountain village with glowing windows and pedestrians. Final frame pulls up to reveal the whole living continent still sitting on the paper map. Strict consistency rules: no cuts, no teleporting, no cartoon look, the map stays recognizable throughout.
```

> 💡 “等待-发生了什么”式病毒结构：古董纸地图 4 段定时转场成活微缩大陆，末帧拉回证明地图仍在；严格无剪辑一致性规则（通用型）。
演示视频：https://sifuyik.substack.com/api/v1/video/upload/06424e34-e19b-456d-b21e-3bb31fb6d923/src?override_publication_id=7223942&preview=false&type=hls

---

## 下一步

- 想看 Veo 3（最强原生音频）→ [../veo/](../veo/README.md)
- 想理解 Sora 2 三套写法 → [methodology/11-sora-公式.md](../../methodology/11-sora-公式.md)
- 跨模型对比 → [methodology/10-跨模型对比.md](../../methodology/10-跨模型对比.md)
