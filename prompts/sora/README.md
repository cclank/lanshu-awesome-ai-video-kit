# Sora 2 · 提示词索引（26 条）

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
- [🆕 2026-10 新增](#🆕-2026-10-新增) (6)

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

## 🆕 2026-10 新增（6 条）

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

### so-024 · 名人夜晚离场：旋转门签名+跑车疾驰 10 秒
`sora-2` `cinematic` `night` `crowd` · [sifuyik (Substack)](https://sifuyik.substack.com/p/753-viral-video-prompt-celebrity)

```
Image-to-Video Prompt:

Theme: A celebrity named "Sifu" exits a building at night, signs an autograph for fans behind a barricade, then makes a quick getaway in a sports car

Visuals: Glass revolving door entrance with warm interior light spilling onto a wet dark pavement, a man in a grey shirt and dark trousers walking with two security guards in black suits, a crowd of fans and photographers behind a metal barrier holding up phones and cameras, camera flashes popping, velvet rope stanchions in the foreground, a sleek sports car waiting at the curb

Camera: Handheld documentary/paparazzi style, eye-level medium shot, camera tracks gently forward and follows the man as he walks toward the lens and stops to sign, then pans/follows as he moves to the car and drives off

Style: Realistic, cinematic nighttime street photography, high contrast between bright building interior and dark exterior, dynamic flash lighting, glossy wet ground reflections, energetic celebrity-arrival atmosphere

Action + Sound Design:
[0-1.5s] The man and two security guards emerge from the revolving door into the night, the crowd behind the barricade visible and cheering "Sifu", camera shutters clicking
[1.5-4s] He walks toward the camera with a smile, waving to the fans, while camera flashes pop around him and the guards stay close on either side
[4-7s] He stops, takes a pen, and signs an autograph on a white notebook held out from the lower left of frame, the guards waiting patiently beside him
[7-8.5s] He finishes signing, hands the pen back, waves once more to the crowd, then turns and strides confidently toward the waiting sports car
[8.5-10s] He swings open the door, hops into the driver's seat in one fluid motion, the engine roars to life, and the car peels away from the curb into the night, tail lights streaking across the wet pavement as the crowd reacts with surprise and excitement
```

> 💡 狗仔跟拍式现实主义短片模板：旋转门→签名→跑车离场一镜式调度，湿地面反光+闪光灯氛围，10 秒完整叙事弧，换脸即用
（来源为模型无关 prompt，模型归属为编辑指派；日期为相对时间推算）

### so-025 · 人类 vs 银背大猩猩：竞技场扇耳光大赛
`sora-2` `image-to-video` `close-up` `slow-motion` `neon` `crowd` · [sifuyik (Substack)](https://sifuyik.substack.com/p/756-viral-video-prompt-slap-competition)

```
First-Frame Image Prompt:

A wide, eye-level shot of a brightly lit indoor sports arena. In the center, a slap-fighting competition is about to begin. On the left stands a muscular man wearing a tight black t-shirt with "SLAP" written in white, black sweatpants, and red athletic shoes. On the right stands a massive, realistic silverback gorilla standing upright. Between them is a black cylindrical podium with neon green and pink accents and the text "10X." In the background, between the two competitors, stands a referee in a black polo shirt. Behind them, a large, slightly blurred crowd sits in stadium seating under bright, dramatic overhead lighting. Hyper-realistic, high-definition sports photography, cinematic arena atmosphere.

Image-to-Video Prompt:

Theme: Surreal human vs gorilla slap-fighting showdown in a professional sports arena

Visuals: A packed indoor arena under dramatic overhead lighting, a black cylindrical slap podium with neon green/pink accents and "10X" branding, a muscular man in a tight black "SLAP" t-shirt and red shoes facing an enormous upright silverback gorilla, with a referee standing between them

Camera: Wide establishing shot -> medium close-up on impact -> slow-motion close-up for the final strike

Style: Hyper-realistic sports photography, high-intensity, dark arena atmosphere with spotlighted action, exaggerated impact physics, cinematic slow motion

Action + Sound Design:
[0-2.5s] Wide establishing shot of the arena. The referee raises a hand and shouts "Fight!" as the man and gorilla face off across the podium - ambient crowd noise, tense atmosphere [cut]
[2.5-5s] Medium close-up of the man. The gorilla's massive hand swings in from the right and slaps the man's left cheek with extreme force, sending a cloud of white powder and sweat erupting from the impact - loud exaggerated smack sound + crowd gasp [cut]
[5-7.5s] The man absorbs the blow, his face rippling but staying upright. He clenches his jaw, glares back with determination, and winds up his right arm - heavy breathing + dramatic low-frequency rumble [cut]
[7.5-10s] Slow-motion close-up profile shot. The man's muscular arm swings forward and his open palm connects solidly with the side of the gorilla's face, sending a shockwave through the gorilla's fur and another puff of white powder into the air - heavy impact thud + deep bass drop
```

> 💡 荒诞对决类病毒喜剧：扇耳光竞技的慢动作冲击物理+粉尘爆发，四段式剪辑节奏，强视觉奇观易出爆款
（来源为模型无关 prompt，模型归属为编辑指派；日期为相对时间推算）

### so-026 · 倒霉青蛙 30 秒：珍珠→河狸→毛毛虫连环喜剧
`sora-2` `comedy` `reference` `close-up` `comedy` · [sifuyik (Substack)](https://sifuyik.substack.com/p/757-viral-video-prompt-frog-adventure)

```
Reference Images (generate first):

Frog Character Sheet:
Character reference sheet of the green frog from the unlucky frog slapstick comedy. 3D Pixar/Dreamworks animation style, clean white background, multiple poses and expressions in a grid layout. Show front view, side view, 3/4 view, curious expression reaching for a pearl, nervous smile, pain expression with a swollen red finger, dazed expression after hitting a tree, and final close-up with comically enormous swollen bright red lips. Small plump green body, short limbs, large bulbous expressive eyes, wet glossy skin with lighter green highlights, wide mouth. High quality, detailed textures, vibrant colors, soft natural lighting.

Otter Character Sheet:
Character reference sheet of the grumpy brown otter with beaver-like features from the unlucky frog slapstick comedy. 3D Pixar/Dreamworks animation style, clean white background, multiple poses and expressions in a grid layout. Show front view, side view, 3/4 view, angry glare, chasing pose, tail-swinging batting pose, and with a clam balanced on its head. Stocky brown furry body, short brown fur, grumpy face with narrowed eyes and visible buck teeth, broad flat tail. High quality, detailed fur texture, vibrant colors, soft natural lighting.

Caterpillar Character Sheet:
Character reference sheet of the colorful spiky caterpillar from the unlucky frog slapstick comedy. 3D Pixar/Dreamworks animation style, clean white background, multiple views and poses in a grid layout. Show top view, side view, front view, curled pose, and stretched pose. Small segmented cylindrical body with bright multicolored segments in green, yellow, red, blue and orange, covered in sharp spikes and bristles. High quality, detailed texture, vibrant colors, soft natural lighting.

Video Prompt:

Theme: Unlucky green frog <<<Image2>>> slapstick comedy in a sunny pond

Visuals: A small cartoon green frog with large expressive eyes, wet glossy skin, and a plump body; a grumpy brown beaver with buck teeth, a broad flat tail, and a clam balanced on its head; a tiny multicolored spiky caterpillar with green, yellow, red, orange, and blue segments; a serene pond with lily pads, tall reeds, a muddy bank, and a large tree trunk

Camera: Wide establishing shot at the start, close-ups on facial reactions, quick cuts during the chase, a long tracking shot as the frog flies through the air, and a final extreme close-up on the swollen lips

Style: 3D Pixar/Dreamworks feature animation, vibrant saturated colors, realistic textures on stylized characters, soft warm natural outdoor lighting, exaggerated cartoon physics, slapstick comedy timing

Action + Sound Design:
[0-2s] Wide establishing shot of a sunny pond. The green frog sits on the muddy bank, eyes wide and curious, slowly reaching toward a large glowing pink pearl inside an open clam shell. Soft ambient pond sounds: gentle water lapping, distant birds, light wind through reeds.
[2-3s] Close-up on the frog's face: pupils dilated, tongue slightly out, finger hovering just above the pearl. Tense silence with a faint magical shimmer from the pearl.
[3-4s] The clam snaps shut on the frog's finger with a sharp CLACK. The frog's eyes bulge, mouth drops open in shock. Loud snap sound.
[4-6s] The frog yanks its hand back and hops backward, clutching its throbbing swollen red finger. Pained "YOW!" vocalization, rapid heartbeat sound.
[6-8s] The frog stumbles and accidentally kicks the clam shell, sending it spinning into the air. Whoosh sound, panicked breathing.
[8-9s] The clam arcs through the air and lands squarely on the head of a grumpy brown beaver <<<Image3>>> sitting nearby. Dull thud, beaver's surprised grunt.
[9-11s] The beaver slowly turns its head toward the frog, eyes narrowing, buck teeth gritted, the clam still balanced on its head. Low ominous rumble.
[11-13s] The frog looks up, frozen in fear, then forces a nervous toothy smile with a visible sweat drop. Awkward gulp, nervous giggle.
[13-14s] The frog's smile drops; it spins around and sprints away in panic. Fast scurrying footsteps, splashing mud.
[14-16s] The beaver snarls and charges after the frog on all fours, kicking up dust from the muddy bank. Heavy charging footsteps, angry growl.
[16-18s] The frog leaps into the air trying to escape; the beaver pivots and swings its broad flat tail like a baseball bat. Tail swoosh, frog's scream.
[18-19s] The frog is struck mid-air and spins wildly out of control. Impact smack, whoosh.
[19-21s] Wide tracking shot: the frog flies across the pond in a high arc, limbs flailing, heading toward a large tree trunk on the far bank. Wind rushing sound.
[21-22s] The frog splats flat against the tree trunk with a wet SPLAT, then peels off and slides down into the mud. Squish, mud splatter.
[22-23s] The frog sits dazed in the mud, stars circling its head, tongue lolling out. Dizzy sound effect, tweeting birds.
[23-25s] The frog's eyes refocus and spot a small bright multicolored spiky caterpillar <<<Image1>>> crawling on a nearby leaf. Curious "hmm" sound, leaf rustle.
[25-27s] The frog's tongue shoots out fast, wraps around the caterpillar, and snaps back into its mouth. Tongue snap, slurp.
[27-28s] The frog chews once, eyes widen in pain, and spits the caterpillar out in a puff of dust and spikes. Crunch, "OW!", spitting sound.
[28-30s] Extreme close-up on the frog's face: its lips swell to enormous, glossy bright red proportions. Comic rubber-stretch swelling sound with a pop, ending on a sad groan.
```

> 💡 三角色设定表+30 秒逐秒分镜的完整动画短片方案：皮克斯风 slapstick，角色一致性用 reference sheet 锁定，喜剧号可直接开工
（来源为模型无关 prompt，模型归属为编辑指派；日期为相对时间推算）

## 下一步

- 想看 Veo 3（最强原生音频）→ [../veo/](../veo/README.md)
- 想理解 Sora 2 三套写法 → [methodology/11-sora-公式.md](../../methodology/11-sora-公式.md)
- 跨模型对比 → [methodology/10-跨模型对比.md](../../methodology/10-跨模型对比.md)
