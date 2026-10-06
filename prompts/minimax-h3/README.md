# MiniMax H3 · 提示词索引（10 条）

> **MiniMax H3**（MiniMax）—— 2026-10-06 首次收录。音视频统一 reference、精准台词生成、多角色音色区分。

按场景分类。每条含完整可复制的 prompt、推荐参数、来源。也可以用 [Web 浏览器](../../tools/prompt-browser/index.html) 搜索/筛选。

## 目录

- [💬 对话驱动（原生音频）](#dialogue-driven) (2)
- [🎵 音乐 MV 与表演](#music-video) (3)
- [⚡ 动作、格斗与追逐](#action) (1)
- [🖼️ 图生视频专项](#image-to-video) (1)
- [😄 喜剧与概念性](#comedy) (1)
- [🛍️ 产品与商业广告](#product-commercial) (1)
- [🧩 技巧片段与提示词语法](#technique-snippet) (1)

---

## 💬 对话驱动（原生音频）

### mx-001 · 韩式黑色电影预告：原生韩语对白
`minimax-h3` `dialogue-driven` `dialogue` `night` `rain` `neon` · 16:9 · [imaginevid/awesome-minimax-h3-prompts-and-skills](https://github.com/imaginevid/awesome-minimax-h3-prompts-and-skills)

```
16:9, 15s, hyper-realistic Korean noir crime teaser.

A rain-soaked Korean woman (late 20s, trench coat) enters an abandoned underground nightclub searching for her missing sister. A scarred crime boss (40s), presumed dead for years, emerges from the shadows with a lit cigarette. Atmosphere: 90s Korean noir, practical neon, rain, smoke, film grain, tactile realism, no CGI gloss.

Shots:

1. She enters: "언니... 여기 있어?"

2. Lighter ignites, revealing his scar. "오랜만이네."

3. She freezes: "당신... 죽은 줄 알았는데."

4. Slow push-in. He smiles: "네 언니가 날 죽였다고 생각했겠지."

5. They lock eyes. Thunder. Cut to black.

Audio: Rain, thunder, jazz crackle, lighter click, intimate silence during dialogue. #MiniMaxH3
```

> 💡 H3 首批原生对话验证案例：直接在 prompt 里写韩语对白并配音轨描述，展示 H3 生成精准台词+环境音的原生音频能力

### mx-008 · 纸鸟避雨计划：双语音参考定音配对白
`minimax-h3` `dialogue-driven` `dialogue` `close-up` `rain` · 3s · [aivideoweb/awesome-minimax-h3-prompts](https://github.com/aivideoweb/awesome-minimax-h3-prompts/blob/HEAD/prompts/21-character-dialogue-performance.md)

```
Create a tactile stop-motion paper-craft scene beginning from Image 1. Preserve exactly two characters: the broad indigo bird stays screen left with one folded wing held close; the smaller saffron bird stays screen right with a long pointed tail. Preserve paper colors, fold patterns, fiber texture, scale difference, seed tray, warm lantern, greenhouse structure, rain direction, and open door at far right.

0–3 seconds: establishing medium-wide shot with Audio 3 prominent. A gust rattles the greenhouse; both birds look toward the right-hand door, then at each other. No dialogue. 3–7 seconds: close on the indigo bird using Audio 1, low and steady: “The roof will hold if we brace the west hinge.” Its beak movement is minimal and synchronized; the saffron bird listens without speaking. 7–11 seconds: reverse close-up using Audio 2, quick but clear: “Then I'll tie the twine. You keep the lantern dry.” The indigo bird listens and lowers its tense shoulder fold. 11–15 seconds: return to the two-shot. They each take one end of a loose natural-fiber twine and move together toward the exit; the lantern remains inside. End before they enter the rain.

Use slight stop-motion cadence, consistent eye lines, and one speaker at a time. Sound hierarchy: dialogue first, rain and wooden creaks below, no music. Avoid extra birds, human hands, realistic feathers, changing folds, swapped voices, subtitles, speech bubbles, a repaired roof not yet shown, exaggerated panic, franchise resemblance, logos, or watermark.
```

> 💡 H3 音视频统一 reference 的教科书：图像定角色场景，Audio 1/2 分别授权两个角色的音色，Audio 3 只管雨声环境，一人一句配对口型

---

## 🎵 音乐 MV 与表演

### mx-002 · 面无表情热舞：音频波形驱动节奏
`minimax-h3` `music-video` `reference` · [imaginevid/awesome-minimax-h3-prompts-and-skills](https://github.com/imaginevid/awesome-minimax-h3-prompts-and-skills)

```
Use the supplied 15-second audio slice as the exact rhythm reference. When the parcel arrives, the character's body begins dancing in perfect synchronization with the waveform: fully committed on every beat, while the face remains completely deadpan and the eyes stay locked on camera. Preserve this trigger, contrast, timing rule, and character behavior in every scene so the repeated mechanism gives the film one coherent energy.
```

> 💡 H3 独有音频 reference 用法：把 15 秒音频切片当作精确节奏参考，触发式舞蹈机制可跨场景复用
演示视频：https://video.twimg.com/amplify_video/2083031810494324736/vid/avc1/1920x1440/ep8hqWhyscuF42MY.mp4?tag=29

### mx-006 · 七色 K-pop 回归预告：精准排版字效
`minimax-h3` `music-video` `dialogue` `neon` `anime` · 16:9 · [imaginevid/awesome-minimax-h3-prompts-and-skills](https://github.com/imaginevid/awesome-minimax-h3-prompts-and-skills)

```
Create a 15-second, 16:9, 2K, high-budget K-pop girl-group comeback teaser. The group consists of seven original Korean female idols, all aged 22 or older; they must not resemble real celebrities. Give each member a distinct face, hairstyle, outfit, and signature color while maintaining a photorealistic live-action appearance.

Members: MIA uses purple-and-black styling with violet electricity. IVY uses emerald-and-black styling with green luminous vines. NIA uses ice-blue styling with glass fragments and icy mist. IRIS uses silver-and-white styling with iridescent light. MAY uses black-and-red styling with red sparks. ARI uses gold-and-black styling with golden particles. XENA uses deep-blue styling with blue lasers. Their initials spell MINIMAX.

Only the following text may appear: MIA, IVY, NIA, IRIS, MAY, ARI, XENA, and MINIMAX. Present each name as premium character-introduction typography with condensed uppercase letters, geometric cuts, metallic outlines, translucent echoes, scan lines, small HUD circles, letter fragments, and energy trails. Keep every name accurate and legible without covering a face.

Timeline: 0.0-0.5s, seven colored light trails sweep across black and form an incomplete MINIMAX outline. 0.5-2.0s, MIA in a violet mirrored corridor as the camera pushes in. 2.0-3.5s, violet electricity transforms into green vines and IVY emerges. 3.5-5.0s, green light freezes into ice-blue glass and NIA emerges through cold mist. 5.0-6.5s, glass refracts into iridescent light and IRIS turns in a silver-white mirrored space. 6.5-8.0s, red sparks ignite and MAY swings translucent red fabric toward camera. 8.0-9.5s, sparks become gold particles and ARI walks out from a black-and-gold stage. 9.5-11.0s, the gold ring becomes a deep-blue laser corridor and XENA steps forward. Briefly decelerate each introduction for 0.3s while hair, clothing, mist, and light continue moving; hold each name for at least 0.5s.

From 11.0-15.0s, a blue laser reveals a large black mirrored stage. All seven members enter from different directions and form a clear three-front, four-back formation with every face visible. Pull back slowly from a low angle. Contract each name to its first letter, M I N I M A X, then combine the letters into a large MINIMAX title built from structural lines, geometric cuts, metallic fill, translucent echoes, and a final seven-color sweep. Hold the group looking into camera for one second. Use native stereo sound: electronic bass, percussion, electricity, glass, airflow, sparks, lasers, and typographic lock-on effects. No dialogue. Avoid celebrities, minors, gibberish, misspellings, extra text, text over faces, identity changes, similar-looking members, revealing outfits, anime, game CGI, cheap neon, excessive particles, and unnecessary 3D rotation.
```

> 💡 H3 文字渲染能力的硬核演示：7 位成员名+MINIMAX 标题逐字排版，每段 0.3s 减速持名 0.5s，七色光效随音乐变奏

### mx-010 · 车站双语二重唱：中西歌声对答
`minimax-h3` `music-video` `rain` · 4s · [aivideoweb/awesome-minimax-h3-prompts](https://github.com/aivideoweb/awesome-minimax-h3-prompts/blob/HEAD/prompts/13-music-performance-audio.md)

```
Create an intimate, fictional musical exchange on an almost-empty covered station platform at blue hour. Preserve Performer A from Image 1 in a charcoal coat on screen left and Performer B from Image 2 in a rust scarf on screen right. Preserve the platform roof and bench geometry from Image 3; no real rail operator marks.

0–4 seconds: medium two-shot, distant train hum. Performer A sings one soft Mandarin line, “下一站，我们还会再见,” with a calm, hopeful expression. Performer B listens without lip movement. 4–8 seconds: cut on a station-light flicker to Performer B, who answers in Spanish, “La próxima vez, llegaré temprano.” Performer A now listens. 8–12 seconds: return to the two-shot as they sing a wordless two-note harmony; a train light passes behind them and the camera gently pushes in.

Keep exact voice-to-face ownership, natural breathing, intelligible pronunciation, stable eyelines, consistent platform geography, and modest performance. Sound intent: voices foreground, light rail ambience, no additional lyrics, no non-diegetic music. Avoid translated subtitles baked into the image, overlapping mouth movement, voice swapping, melodramatic gestures, real transit logos, or watermark.
```

> 💡 H3 多语音色绑定的音乐用法：中文+西班牙语两段歌声各有授权音色，规定发声者归属与聆听者闭嘴——双语演唱的可复现模板

---

## ⚡ 动作、格斗与追逐

### mx-003 · 五参考追车大战：沙丘越野车逃脱无人机
`minimax-h3` `action` `dialogue` `reference` `close-up` `aerial` · 16:9 · [imaginevid/awesome-minimax-h3-prompts-and-skills](https://github.com/imaginevid/awesome-minimax-h3-prompts-and-skills)

```
Create a 15-second, 16:9 photoreal cinematic action sequence with native stereo audio. Treat the five images as coordinated multimodal references for identity, vehicle design, environment, performance, action, cinematography, and sound.

Use Image 1 as the strict facial-identity reference for the female racer. Preserve her exact face, dark tied-back hair, amber goggles, dusty skin, black tactical suit, shoulder armor, gloves, and focused expression.

Use Image 2 as the strict reference for her full costume, body proportions, armored black dune buggy, tire scale, exposed suspension, cyan headlights, roll cage, desert lighting, and industrial-outpost background.

Use Image 3 as the action reference for the pursuing drones, vehicle speed, dust trails, fire, debris, chase intensity, and camera proximity.

Use Image 4 as the location reference for Outpost 07, including its rusted towers, pipelines, bridges, rocky terrain, distant mountains, warm sunset atmosphere, and industrial scale.

Use Image 5 as the cockpit and performance reference. Preserve the same steering wheel, open roll cage, goggles, gloves, facial identity, driving posture, and vehicle interior.

Sequence

[0–2.5 seconds]

Open on Image 4 with an extreme-wide aerial establishing shot of Outpost 07 at sunset. The industrial complex fills the right side of frame while an empty desert route curves through the rocky foreground.

The camera dives rapidly toward the road as a small black dune buggy bursts from beneath an elevated pipeline, throwing a long dust plume behind it.

Keep the vehicle moving consistently from left to right toward the outpost. No direction reversal.

Audio begins with dry desert wind, distant industrial machinery, a low cinematic pulse, and the buggy engine approaching rapidly.

[2.5–5 seconds]

Cut at peak engine sound to Image 5.

Tight frontal cockpit shot mounted just ahead of the driver. The vehicle shakes naturally over rough ground. Her hands hold the steering wheel firmly while she makes small, physically accurate corrections.

Her amber goggles remain on top of her head. Loose strands of hair and fabric straps react to wind and vibration. Her eyes briefly check the left mirror, then return immediately to the road.

A red warning light reflects across her face as a targeting alarm begins.

Do not make her turn the steering wheel excessively. Her body, wheel movement, and vehicle direction must remain mechanically connected.

[5–8 seconds]

Cut to a low front three-quarter tracking shot based on Image 3.

Three pursuit drones descend behind the buggy in a triangular formation. Their rotors, stabilizers, and body movement respond realistically to speed and turbulence.

The lead drone fires into the sand beside the buggy. The impact creates a narrow eruption of dirt, sparks, and fragmented rock rather than an oversized fireball.

The racer steers sharply around the impact. The buggy's front wheels turn first, the suspension compresses, the body leans, and the rear tires slide outward before regaining traction.

The camera tracks beside the vehicle without spinning or overtaking it.

[8–11 seconds]

Continue the same drift into a rear three-quarter shot.

The buggy races toward a narrowing passage between a rock wall and the outer structures of Outpost 07. The racer pulls a mechanical handbrake lever for one brief moment, rotating the vehicle through the opening.

One drone follows too closely and clips a rusted overhead pipe. Its wing breaks, sending the drone tumbling into the sand behind her.

Show the collision in the background while keeping the buggy dominant and moving forward. No slow motion.

Audio: tire scrape, suspension impact, metal tearing, drone rotors failing, engine rev rising.

[11–13 seconds]

Cut to a wheel-level macro shot.

The right rear tire bites into loose sand. Stones fire backward while the suspension rebounds. The camera rises naturally along the buggy's side and reveals the two remaining drones closing in.

The racer presses a guarded switch beside the steering wheel.

A compact rear-mounted electromagnetic pulse discharges as a restrained blue-white distortion wave, briefly disrupting the drones' lights and stabilizers.

No magical energy, lightning storm, or giant explosion.

[13–15 seconds]

Cut to a low frontal hero shot as the buggy clears the outpost gate at full speed.

The two disabled drones fall into the dust behind it while the vehicle launches from a shallow ridge. Keep the jump low, heavy, and physically believable.

During the brief airborne moment, cut to Image 1 for a tight close-up of the racer. Preserve her exact identity as warm firelight and cool dashboard light cross her face. Her expression remains controlled and determined.

The buggy lands hard beyond the gate. The suspension compresses, the engine roars, and the vehicle continues directly into the desert.

End with a sharp cut to black on the landing impact.

Visual Direction

Premium live-action science-fiction action trailer with realistic CGI integration, warm orange sunset light, restrained steel-blue technology accents, dusty atmosphere, hard surface detail, cinematic contrast, subtle film grain, realistic motion blur, and 24 FPS movement.

Use wide shots to establish scale, cockpit close-ups for tension, low tracking shots for speed, and mechanical macro shots for physical detail.

Keep the editing fast but readable. Every shot must begin from the physical state established by the previous shot.

Audio Direction

Native stereo sound with:

Aggressive combustion engine

Tire friction over sand and rock

Suspension rattles and chassis vibration

Drone rotors and targeting alarms

Sand impacts, metal collisions, and falling debris

Low percussion and rising electronic tension

One heavy bass impact on the final landing

Keep music underneath the vehicle and environmental sounds. No dialogue or voice-over.

Restrictions

No subtitles, titles, logos, watermarks, additional racers, pedestrians, creatures, motorcycles, futuristic city skyline, nighttime transition, costume changes, facial changes, vehicle redesign, additional wheels, floating vehicle parts, distorted hands, incorrect steering, reversed wheel rotation, teleportation, random explosions, oversized fireballs, weightless motion, impossible jumps, camera spins, circular camera moves, rapid zooms, fluid morphs, soft dissolves, or changes in travel direction. #MiniMaxH3
```

> 💡 H3 多模态 reference 范式标杆：5 张图片各司其职（身份/载具/动作/场景/座舱）+ 原生立体声音轨描述，附结果视频

---

## 🖼️ 图生视频专项

### mx-004 · 孟买季风 FPV：手绘路线图引导航拍
`minimax-h3` `image-to-video` `dialogue` `reference` `drone` `rain` · [imaginevid/awesome-minimax-h3-prompts-and-skills](https://github.com/imaginevid/awesome-minimax-h3-prompts-and-skills)

```
Reference: Use the attached @ Image1 1 as the exact first frame and environment reference. The green drawn line is only the camera flight-path guide. Do not show the green line in the final video.

Create a 15-second hyper-real cinematic FPV drone video over Mumbai in heavy monsoon weather, using the same skyline, interchange, sea edge, road geometry, dense buildings, rainy morning atmosphere, grey clouds, and wet surfaces from the reference image. Keep everything realistic and grounded. The drone must follow the green guideline path as a smooth continuous move: begin near the left side of the interchange, rise and sweep across the middle highway corridor, continue through the right-side city edge, then climb higher into the skyline, perform a tight spiral/orbit near the upper tower cluster, descend back toward the interchange, curve around the large circular loop, and finally glide out toward the lower-right water edge. The move should feel fast, elegant, immersive, and controlled — like a premium FPV drone shot, not a random flyover.

TIMELINE

 0:00–0:03 Start low near the left feeder ramp above the wet interchange. Heavy rain falls across the lens. The drone accelerates forward and slightly upward, revealing slick roads, tiny moving traffic, dark sea barriers, and the circular loop ahead.

0:03–0:06 Follow the path upward across the mid-frame highway corridor. Keep the skyline growing larger. Wet roads shimmer, rain haze softens the distance, and the sea remains visible to the right. Motion is quick but readable.

0:06–0:09 Sweep along the right-side city edge and climb higher. Dense towers, mid-rise blocks, and dark green patches below feel soaked and monsoon-heavy. The camera begins rising toward the upper skyline.

0:09–0:11 Reach the upper skyline cluster and perform a tight spiral/orbit around the central high-rises. Storm clouds loom above, rain streaks rush past, and the city beneath feels deep, layered, and cinematic.

0:11–0:13 Exit the spiral and descend in a smooth arc back toward the interchange. The circular loop becomes dominant again. Maintain realistic drone inertia and readable geography.

0:13–0:15 Curve around the large circular flyover loop and finish with a fast glide toward the lower-right over the water, ending on a dramatic monsoon reveal of wet infrastructure, dark sea, and rain-washed Mumbai.

CAMERA LANGUAGE FPV drone POV, smooth stabilized flight, realistic banking turns, slight motion blur from speed and rain, believable acceleration and inertia, one continuous shot, no teleporting, no abrupt cuts, no impossible passes through buildings.

VISUAL STYLE Hyper-real cinematic realism, heavy monsoon rain, grey storm clouds, wet roads, reflective flyovers, rain haze, cool blue-grey morning light, dark sea, atmospheric depth, realistic Mumbai scale, premium documentary-film look.

AUDIO No voiceover. No dialogue. Use heavy rainfall, rushing wind, distant thunder, soft drone motor whirr, faint traffic hum, sea movement, and subtle cinematic tension music building with the motion.

IMPORTANT Do not show the green route line. No text, captions, logos, or watermark. Keep Mumbai realistic, monsoon-heavy, and geographically believable.
```

> 💡 巧妙的图生视频技巧：在参考图上画绿色引导线定义无人机航线，明确要求隐藏路线线——路线可控性范式

---

## 😄 喜剧与概念性

### mx-005 · 1980s 复古机器人家庭喜剧：开场图转视频
`minimax-h3` `comedy` `rain` `dance` `product` `crowd` · [imaginevid/awesome-minimax-h3-prompts-and-skills](https://github.com/imaginevid/awesome-minimax-h3-prompts-and-skills)

```
Use the supplied image as the exact opening frame. Create a hilarious, high-budget 1980s live-action family comedy movie scene, photographed on a real soundstage with practical robot costumes, animatronics, handmade props, vintage wardrobe, and authentic 35mm film color.

The entire group suddenly hears something above them. Everyone's eyes dart upward at the same moment. The men, women, children, and robots dramatically tilt their heads back, point toward the ceiling, and erupt into chaotic celebration. They gasp, scream, laugh, jump, wave their arms, slap each other on the shoulder, and completely lose their minds with exaggerated 1980s comedy reactions. The children bounce excitedly. The adults stumble into one another. The robots flash their eyes, flap their mechanical arms, spin clumsily, and celebrate with funny practical animatronic movements.

One man shouts:

“OPEN SOURCE?!”

The entire crowd answers together:

“MINIMAX H3!”

They cheer wildly as one robot attempts a victory dance, loses its balance, and is caught by the shocked family at the final second.

Fast, energetic comic timing with believable ensemble choreography. Begin with a brief locked group shot, then a subtle handheld push-in as the chaos escalates. Keep every original person, robot, shirt design, and the large headline clearly recognizable. Preserve facial identity, wardrobe, composition, lighting, and 1980s production design.

Authentic optical softness, warm tungsten lighting, rich film grain, slight gate weave, practical effects, natural motion blur, expressive physical acting, polished studio-comedy sound mix, triumphant synthesizer sting, cheering, robot beeps, and comedic percussion.

No CGI, no digital-looking robots, no morphing, no extra people, no duplicated characters, no distorted faces, no rewritten text, no spelling changes, no modern clothing, no style shifts, and do not turn the scene into animation.
```

> 💡 图生视频喜剧范例：锁定开场图身份/服装/文字，靠群戏调度+喜剧音效设计驱动笑点，展示 H3 原生音频与群戏一致性

---

## 🛍️ 产品与商业广告

### mx-007 · 抹茶新手礼盒晨间 UGC 广告
`minimax-h3` `product-commercial` `reference` `close-up` `one-shot` · [imaginevid/awesome-minimax-h3-prompts-and-skills](https://github.com/imaginevid/awesome-minimax-h3-prompts-and-skills)

```
Use the uploaded reference image as the exact character reference. Preserve her facial identity, hairstyle, eye color, skin tone, body proportions, and facial consistency throughout every shot.

Create a 15-second ultra-realistic UGC-style lifestyle advertisement featuring a realistic young woman sharing her favorite premium Matcha Starter Kit in a bright, minimalist Japanese-inspired kitchen with warm morning sunlight, natural wood textures, soft neutral décor, ceramic tableware, and a calm luxury aesthetic.

She smiles naturally while holding an elegant matcha tin and says this has become her favorite way to start every morning. She opens the premium matcha container, carefully scoops vibrant green matcha powder into a handcrafted ceramic bowl, pours warm water, and whisks it smoothly using a traditional bamboo whisk until a rich, creamy foam forms. She lifts the bowl, takes a small sip, closes her eyes with a genuine smile, and enjoys the peaceful morning moment.

Capture authentic handheld smartphone shots, over-the-shoulder angles, cinematic macro close-ups of the vivid green matcha powder, the bamboo whisk creating silky foam, the handcrafted ceramic bowl, rising steam, natural hand movements, and warm sunlight reflecting across the table. Finish with her holding the completed bowl beside her face, smiling warmly into the camera.

Authentic creator-style content, natural facial expressions, healthy glowing skin, cozy morning atmosphere, luxury lifestyle aesthetic, subtle depth of field, premium color grading, smartphone-shot realism, vertical 9:16, 4K HDR, no text, subtitles, logos, or watermarks.
```

> 💡 H3 的参考身份锁定做带货 UGC：角色身份严格锁定+抹茶打制触感特写，手持手机美学对电商内容有直接参考价值

---

## 🧩 技巧片段与提示词语法

### mx-009 · 相机语法迁移：借运镜节奏不借画面
`minimax-h3` `technique-snippet` `reference` `rain` `product` · 3s · [aivideoweb/awesome-minimax-h3-prompts](https://github.com/aivideoweb/awesome-minimax-h3-prompts/blob/HEAD/prompts/20-multireference-camera-transfer.md)

```
Create an original studio advertisement for the fictional graphite-and-cork portable speaker in Image 1. Transfer only the abstract camera grammar from Video 1: shot lengths, direction of travel, acceleration curve, focal transitions, and cut timing. Do not copy its subject, setting, colors, props, lighting design, composition, campaign idea, text, or recognizable effects.

0–3 seconds: slow three-quarter push toward the full speaker on a charcoal plinth; amber rim light reveals the cork edge. 3–6 seconds: cut on Audio 1's second downbeat to a controlled lateral macro move across the cork pores and metal seam. 6–9 seconds: repeat Video 1's orbit speed around the circular woven grille while the product remains stationary and physically intact. The amber status light turns on once at the final beat of this section. 9–12 seconds: pull back to the original three-quarter product view; a shallow pattern of light crosses the acoustic panel behind it and settles, leaving clean negative space for typography added later.

Preserve the exact silhouette, circular grille, cork panels, seam placement, amber indicator, scale, and material response from Image 1. Sound intent: Audio 1 plus restrained tactile clicks and low room tone; do not imply measured loudness or acoustic performance. Avoid logos, generated copy, extra controls, duplicate speakers, pulsing geometry, visible sound waves, floating product, copied reference-video scenery, or watermark.
```

> 💡 H3 视频 reference 的新玩法：只迁移参考视频的抽象运镜语法（景别/加速度/切点），不复制其内容——解决版权风险的实用技巧

---
