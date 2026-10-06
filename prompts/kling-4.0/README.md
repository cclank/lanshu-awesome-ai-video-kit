# Kling 4.0 (可灵) · 提示词索引（12 条）

> **Kling 4.0 (可灵)**（快手）—— 2026-10-06 首次收录。omni reference 多引用叙事、match-cut 藏转场、多语言对白口型同步。

按场景分类。每条含完整可复制的 prompt、推荐参数、来源。也可以用 [Web 浏览器](../../tools/prompt-browser/index.html) 搜索/筛选。

## 目录

- [🧩 技巧片段与提示词语法](#technique-snippet) (1)
- [🍵 安静时刻与生活切片](#quiet-moments) (1)
- [🎬 电影叙事与戏剧场景](#cinematic) (1)
- [💬 对话驱动（原生音频）](#dialogue-driven) (1)
- [🛍️ 产品与商业广告](#product-commercial) (1)
- [🎵 音乐 MV 与表演](#music-video) (1)
- [🏁 体育、赛车与武术](#sports) (1)
- [📱 社交媒体爆款](#social-viral) (1)
- [🌿 自然、风景与天气](#nature) (1)
- [🎥 纪录片与采访](#documentary) (1)
- [🌌 奇幻与科幻](#fantasy-scifi) (1)
- [👤 人物与肖像](#portrait) (1)

---

## 🧩 技巧片段与提示词语法

### k4-001 · Kling 4.0 四世界罗盘 Match Cut
`kling-4.0` `technique-snippet` `match-cut` `reference` `night` `rain` · 16:9 / 12s · [flaqai/awesome-kling-4-0](https://github.com/flaqai/awesome-kling-4-0/blob/main/prompts/reference-editing-and-control.md)

```
[OUTPUT]

12 seconds, 16:9, four-scene cinematic match-cut montage, crisp realistic materials, exactly four shots.

[REFERENCE ROLES]

Object reference locks one palm-sized scratched copper compass with a dark blue needle and plain lid. Environment references control only: coastal cliff at dawn, night train table, desert survey camp, snowy observatory. Do not transfer people or objects between environment references.

[MATCH-CUT RULE]

The compass center remains at 52% frame width and 58% frame height, same apparent size and same 35-degree lid angle at every cut. Each transition occurs during the final six frames of a hand closing the lid; motion direction stays right-to-left.

[TIMED SHOTS]

0–3s — Coastal cliff macro. Weathered adult hand opens the compass; needle settles north, salt mist crosses left-to-right, slow 5cm push-in.

3–6s — Cut under closing fingers to the same compass on a night-train table. Different sleeve, same hand path. Passing lights sweep across copper; needle trembles once with rail vibration.

6–9s — Cut under the lid to a desert survey cloth. Fine sand moves around, never onto, the hinge. Hand rotates the whole compass 20 degrees clockwise; needle independently returns north.

9–12s — Cut under closing fingers to snowy observatory stone. Gloved hand opens the lid fully; camera tilts from compass toward a clear polar star, ending with the compass still visible at lower center.

[AUDIO]

One continuous low musical note bridges all cuts. Distinct layers: surf and lid click; rail rhythm; dry wind; high mountain air. The same metal click lands exactly at 2.8s, 5.8s and 8.8s.

[CONSTRAINTS]

One compass only. Preserve scratches, hinge, needle color, scale and screen position. Cuts happen only behind fingers and lid; no dissolve, portal, morphing map, readable text, logo or watermark.
```

> 💡 omni reference 范式：一个物体 reference 加四个环境 reference 各司其职，match-cut 全部藏进合盖动作，是 4.0 多引用叙事的标杆写法。

---

## 🍵 安静时刻与生活切片

### k4-002 · Kling 4.0 三代人午餐
`kling-4.0` `quiet-moments` `dialogue` `reference` `rain` · 16:9 / 15s · [flaqai/awesome-kling-4-0](https://github.com/flaqai/awesome-kling-4-0/blob/main/prompts/reference-editing-and-control.md)

```
[OUTPUT]

15 seconds, 16:9, intimate family lunch scene, naturalistic cinema, three connected shots with native dialogue.

[REFERENCE ROLES]

Image 1 locks Mei, adult grandmother with short white curls and burgundy cardigan. Image 2 locks adult daughter An, chin-length black hair and olive shirt. Image 3 locks adult grandson Leo, curly dark hair and mustard sweater. Image 4 supplies only the small sunlit dining room and oval wooden table; ignore any people in it.

[GEOGRAPHY]

Mei sits frame left, An frame right, Leo centered on far side. One blue serving bowl in the table center. Their seats, wardrobe and eyelines never swap.

[TIMED SHOTS]

0–5s — Wide locked master. Mei lifts the blue bowl with both hands and passes it clockwise to An. Leo watches the bowl, then glances at Mei.

5–10s — Medium two-shot across table. An receives the bowl from below, sets it down once and says in Mandarin: “还是这个味道。” Mei is soft foreground left, listening without speaking.

10–15s — Close on Mei. She smiles with restrained pride, looks toward An and answers in English: “You remembered.” Focus shifts to Leo quietly taking one dumpling from the bowl; end on all three sharing a small laugh.

[AUDIO]

Quiet midday room, ceramic contact, chair fabric and distant neighborhood birds. Only An speaks the Mandarin line; only Mei speaks the English line. No narrator or subtitles.

[CONSTRAINTS]

Exactly three adults, one bowl and one dumpling lifted. Natural hand contact and table occlusion. Preserve identity, age, hair, clothing, seat and screen direction. No face blending, duplicate people, extra dishes appearing, generated wall text, logo or watermark.
```

> 💡 三人物 reference 加一房间 reference 的身份锁定写法，中英双语原生对白，展示多角色一致性控制。

---

## 🎬 电影叙事与戏剧场景

### k4-003 · Kling 4.0 末班车归家
`kling-4.0` `cinematic` `close-up` `night` `rain` · 16:9 / 15s · [flaqai/awesome-kling-4-0](https://github.com/flaqai/awesome-kling-4-0/blob/main/prompts/cinematic-and-dialogue.md)

```
[OUTPUT]

15 seconds, 16:9, three-shot contemporary drama, restrained naturalism, cool winter night with warm practical bus light.

[CONTINUITY ANCHORS]

Eli: adult man in his early 30s, narrow face, short curly dark hair, charcoal wool coat, faded red scarf, tired eyes.

June: adult woman in her late 50s, silver bob, moss-green quilted jacket, canvas grocery bag, small brass house key in her right hand.

Keep faces, ages, wardrobe, bag, key and left-to-right screen direction unchanged.

[WORLD]

Nearly empty suburban bus at night. Rain tracks down the windows. Eli sits frame left near the rear door; June stands in the aisle frame right. Sodium streetlights sweep across the interior as the bus moves.

[TIMED SHOTS]

0–5s — Medium two-shot from the opposite seat, camera locked with gentle vehicle vibration. June notices the red scarf, stops one step away and tightens her hand around the key. Eli looks up slowly. Neither speaks.

5–10s — Over June’s shoulder into Eli’s close-up; keep his eyeline toward frame right. The passing streetlight reveals recognition. He removes one earbud and says, quietly: “You still have the key.”

10–15s — Reverse close-up on June, eyeline frame left. Her guarded expression softens; she opens her palm to show the brass key and answers: “You never asked for it back.” Hold one second after the line as the bus brakes gently and both sway in the same direction.

[AUDIO]

Continuous engine hum, soft rain on glass and two distant stop-request chimes. Eli (English, low and hesitant), then June (English, warm but controlled). No music until the final second, when one low cello note enters beneath the bus brake.

[CONSTRAINTS]

Only the named speaker’s mouth moves. Preserve the red scarf and brass key. Natural blinking and breathing; no crying, embrace or exaggerated smile. No subtitles, signage text, logos, face drift, age change, jump in seat positions or sudden weather change.
```

> 💡 三镜头情感短片：道具（钥匙/围巾）锚定一致性，眼神线和环境声床贯穿全片，电影感叙事的完整模板。

---

## 💬 对话驱动（原生音频）

### k4-004 · Kling 4.0 站台纸鹤（韩西双语）
`kling-4.0` `dialogue-driven` `dialogue` `close-up` `rain` · 16:9 / 15s · [flaqai/awesome-kling-4-0](https://github.com/flaqai/awesome-kling-4-0/blob/main/prompts/cinematic-and-dialogue.md)

```
[OUTPUT]

15 seconds, 16:9, four-shot independent-film reunion, Korean and Spanish dialogue, native audio, subtle film grain.

[CHARACTER MAP]

Mina: adult Korean woman, shoulder-length wet black hair, rust-red raincoat, small kraft-paper crane in both hands, low warm voice.

Álex: adult Spanish man, wavy dark hair, short beard, navy railway work jacket with one pale reflective stripe and no logo, soft tenor voice.

The paper crane has one blue ink dot on its left wing; preserve it in every shot.

[WORLD]

Small covered coastal train platform at blue hour. Cream-and-teal local train is stationary frame right; rough sea frame left. Warm overhead lamps reflect on wet tiles. Rain blows diagonally beyond the roof.

[TIMED SHOTS]

0–4s — Wide symmetrical platform shot. Mina enters from frame left and stops; Álex steps down from the train at frame right. They recognize each other across six meters. Camera makes a very slow push forward.

4–7s — Close-up on Mina, Álex remains a soft silhouette deep frame right. She unfolds her fingers to reveal the paper crane. Her inhale catches; she says in Korean, almost a whisper: “늦었네.”

7–10s — Shot/reverse-shot close-up on Álex, eyeline frame left. He exhales, gives one small relieved nod and replies in Spanish: “Pero llegué.”

10–15s — Medium-wide two-shot from the side. They each take one step closer but do not embrace. Mina extends the crane; Álex reaches out and stops just before touching it. Hold on the charged gap between their hands.

[AUDIO]

Continuous coastal rain, distant surf and low idling-train hum. No station announcement. Keep Mina’s Korean and Álex’s Spanish exactly in their written languages; no translation. A sparse two-note piano motif begins only after Álex finishes.

[CONSTRAINTS]

One speaking mouth at a time. Preserve faces, coat colors, train position, rain direction and matched eyelines. The paper crane never changes shape, color or hand. Restrained adult emotion; no melodrama. No subtitles, readable signs, logos, extra passengers, facial drift, dry wardrobe between shots or camera-axis reversal.
```

> 💡 韩语加西班牙语双语对白、逐发话人绑定声线与台词，是 4.0 九语言 lip sync 能力的典型用法。

---

## 🛍️ 产品与商业广告

### k4-005 · Kling 4.0 植物气泡饮品广告
`kling-4.0` `product-commercial` `close-up` `rain` `product` · 16:9 / 9s · [flaqai/awesome-kling-4-0](https://github.com/flaqai/awesome-kling-4-0/blob/main/prompts/commercial-and-ugc.md)

```
[OUTPUT]

9 seconds, 16:9, premium non-alcoholic sparkling botanical drink commercial, photorealistic macro finish, three shots.

[PRODUCT LOCK]

One smoked-green glass bottle with a narrow shoulder, silver knurled cap and blank embossed oval on the front. No printed label or text. Preserve bottle silhouette, cap, oval, glass color and fill level exactly across all shots.

[WORLD]

Wet black basalt surface in a dark studio. Deep emerald rim light from frame left, cool silver key light overhead, narrow warm beam from frame right. Fine mist moves left to right.

[TIMED SHOTS]

0–3s — 100mm macro, low three-quarter angle. Camera slides slowly right while staying focused on condensation. One droplet forms at the shoulder and runs straight down; bottle remains motionless and vertical.

3–6s — Match cut to overhead close-up. A single pale-green citrus peel enters from frame left and completes one smooth clockwise spiral around the bottle without touching it. Fine bubbles rise inside the liquid at constant speed.

6–9s — Medium hero shot. Camera performs a slow 25-degree clockwise orbit at constant distance. The cap lifts two millimeters with a clean pressure release; a controlled halo of cold vapor blooms and clears. End with bottle centered and oval facing camera.

[AUDIO]

0–3s: low studio silence plus individual water drops. 3.1s: crisp peel swish. 6.4s: short cap click and delicate carbonation release. 8s: two warm glass-marimba notes, then silence.

[CONSTRAINTS]

The bottle never floats, bends, rotates independently or changes scale. Keep contact shadow attached to basalt. Physically plausible refraction, droplets, vapor and peel trajectory. No splash covering the product, alcohol cues, glassware, people, text, logo, watermark, label mutation or duplicate bottle.
```

> 💡 产品锁定写法：瓶身几何、冷凝水滴、柑橘皮各有独立运动指令，结尾开盖蒸汽有精确时间点，电商级广告模板。

---

## 🎵 音乐 MV 与表演

### k4-006 · Kling 4.0 屋顶打击乐
`kling-4.0` `music-video` `close-up` `rain` · 16:9 / 15s · [flaqai/awesome-kling-4-0](https://github.com/flaqai/awesome-kling-4-0/blob/main/prompts/style-and-performance.md)

```
[OUTPUT]

15 seconds, 16:9, live rooftop percussion performance at dawn, documentary concert energy, original rhythm, four shots.

[PERFORMER MAP]

Aya: adult Japanese woman, red windbreaker, short hair, frame left, plays one shallow metal handpan.

Malik: adult British man, blue overshirt, shaved head, center, plays one wooden cajón.

Camila: adult Colombian woman, yellow knit top, long braid, frame right, plays two small seed shakers.

Preserve faces, instruments, clothing colors and left-center-right positions.

[RHYTHM AND SHOTS]

0–4s — Wide locked shot, pale sunrise behind city roofs. Malik starts a steady low cajón pulse: four evenly spaced hits. The others listen and sway naturally.

4–8s — Medium side track from Aya to Malik. Aya adds a three-note handpan phrase after every second cajón hit. Her fingers contact visible tone fields; each note aligns exactly to contact.

8–12s — Close-up on Camila’s hands and face. She adds a soft double-shake pattern, wrists moving compactly. Camera rack-focuses from seeds inside the translucent shaker to her smile.

12–15s — Return to wide. All three play one synchronized final accent, then freeze their hands while the metal note decays. A flock of ordinary birds crosses far background after the final hit.

[AUDIO]

Native performance only: dry low cajón, warm resonant handpan, fine seed texture, rooftop wind and distant city. No sampled song, vocals, cheering or added orchestra. Maintain room-free outdoor acoustics and realistic decay.

[CONSTRAINTS]

One instrument per performer; accurate hand-to-sound synchronization; fixed stage positions. No extra sticks, changing instruments, impossible hand speed, duplicated fingers, lip movement, visible brand, skyline text or watermark.
```

> 💡 原生音频音乐表演：三乐器的节奏全部写进时间轴、每个音符对应可见的接触动作，声画同步的标杆写法。

---

## 🏁 体育、赛车与武术

### k4-007 · Kling 4.0 湿地赛道精准圈速
`kling-4.0` `sports` `dialogue` `rain` · 21:9 / 15s · [flaqai/awesome-kling-4-0](https://github.com/flaqai/awesome-kling-4-0/blob/main/prompts/genre-action-and-sound.md)

```
[OUTPUT]

15 seconds, 21:9, realistic closed-course driver-training film at dawn, four shots, high energy without collisions.

[VEHICLE AND DRIVER]

One compact cobalt-blue track car with white roof, black seven-spoke wheels, blank number panel and no logo. Adult professional driver wears a white certified helmet, blue suit and secured six-point harness. Preserve vehicle panels, wheel design and driver throughout.

[TRACK GEOGRAPHY]

Private wet handling circuit, right-hand hairpin marked by six orange cones and a white apex line. Empty runoff, barriers and marshals safely behind fence. Car travels left-to-right before turning away from camera.

[TIMED SHOTS]

0–4s — Interior footwell insert. Right foot releases brake progressively and applies throttle; left foot stays on dead pedal. Water beads move backward on side window. Engine note rises smoothly.

4–8s — Low exterior side tracking. Car approaches left-to-right at controlled speed; tire spray trails behind wheels, never ahead. Camera remains outside barriers.

8–12s — High fixed hairpin view. Driver brakes before cone one, turns once toward the apex and follows the white line without sliding or hitting cones. Brake lights illuminate during deceleration only.

12–15s — Rear three-quarter from safe long lens. Car straightens, accelerates away and spray narrows as it reaches drier pavement. End with all six cones standing.

[AUDIO]

Authentic single engine layer matched across cuts, wet tire hiss, two gear changes and no music until a restrained pulse enters at 12s. No dialogue.

[CONSTRAINTS]

Private course, one car, trained adult, correct harness and intact safety zone. No public traffic, passenger, collision, drift, jump, hydroplane, cone strike, speed claim, dashboard text, badge or watermark.
```

> 💡 21:9 宽画幅赛车短片：赛道地理、喷水方向、刹车灯时机、锥桶数量全部量化，高速动作的稳定写法。

---

## 📱 社交媒体爆款

### k4-008 · Kling 4.0 归来的地铁卡
`kling-4.0` `social-viral` `rain` · 9:16 / 15s · [flaqai/awesome-kling-4-0](https://github.com/flaqai/awesome-kling-4-0/blob/main/prompts/short-drama-and-viral-social.md)

```
[OUTPUT]

15 seconds, 9:16, contemporary vertical micro-drama, restrained realism, four fast but readable shots, episode-one cliffhanger.

[CONTINUITY ANCHORS]

Mina: adult woman, short black bob, camel coat, canvas tote on left shoulder. Theo: adult station attendant, shaved head, navy uniform with no badge. Prop: one scratched green transit card with a small crescent-shaped corner chip; no readable printing.

[GEOGRAPHY]

Quiet underground station after the evening rush. Mina stands outside the closed service window, Theo inside. The card begins in Mina's right hand. Camera never crosses the service-window axis.

[TIMED SHOTS]

0–4s — Tight handheld medium. Mina slides the green card through the tray and says in Mandarin: “这张卡不是我的。” Theo looks down, then freezes before touching it.

4–8s — Insert from Mina's side. Theo turns the card over with one gloved fingertip. The crescent chip is clearly visible. He asks quietly in English: “Where did you find this?”

8–12s — Close on Mina. Her defensive expression softens; she answers: “Inside my locked apartment.” A train passes behind camera, briefly sweeping light across her face without hiding the cut.

12–15s — Close behind Theo's shoulder. He opens a shallow drawer containing one second, identical chipped green card in a clear evidence sleeve. He does not remove it. Mina sees it and steps back once. Cut to black before either speaks.

[AUDIO]

Station ventilation, distant train, tray scrape and drawer rail. Only Mina speaks the Mandarin line and final English line; only Theo asks the question. One low tonal hit when the drawer opens; no subtitles.

[CONSTRAINTS]

Two adults and exactly two matching cards by the final shot. Preserve chip position, wardrobe, tote shoulder, window axis and eyelines. No police insignia, threat, weapon, supernatural glow, generated text, logo or watermark.
```

> 💡 竖屏 9:16 微剧悬念：缺口地铁卡道具贯穿四镜、中英对白、切黑收尾，短剧第一集病毒式模板。

---

## 🌿 自然、风景与天气

### k4-009 · Kling 4.0 茶杯里的风暴
`kling-4.0` `nature` `dialogue` `rain` · 1:1 / 8s · [flaqai/awesome-kling-4-0](https://github.com/flaqai/awesome-kling-4-0/blob/main/prompts/action-and-vfx.md)

```
[OUTPUT]

8 seconds, 1:1, one locked macro shot, photorealistic tabletop surrealism, physically coherent miniature storm.

[SCENE]

Plain white porcelain teacup on a worn oak table beside a closed book. Tea surface visible from a high three-quarter angle. Warm afternoon window light from frame left; cup handle points right. No branding or text.

[ACTION TIMELINE]

0–2s — Tea is almost still. One tiny circular cloud forms two centimeters above the liquid, rotating clockwise. The room outside the cup remains calm.

2–5s — Cloud darkens and releases localized rain only into the cup. Concentric ripples spread to the porcelain edge. Three miniature lightning filaments illuminate the tea from within, each separated by half a second; no bolt leaves the cup.

5–7s — A thumb-sized waterspout rises from the center and rotates once, pulling three loose tea leaves into orbit without spilling liquid over the rim.

7–8s — Storm collapses into one soft puff; surface settles toward stillness. A final single droplet falls into the exact center for a loopable end.

[AUDIO]

Quiet room, magnified rain taps, three delicate electrical ticks synchronized to light, low water swirl, final droplet. No thunder boom, dialogue or music.

[CONSTRAINTS]

Cup, handle, book, table, camera and room light remain fixed. Weather is contained entirely within cup boundaries. Realistic reflections and ripple propagation. No overflow, broken cup, fire, giant ocean, camera movement, text, logo or watermark.
```

> 💡 微观天气奇观：风暴能量严格限定在杯内并按时间衰减，结尾可循环，尺度反差的 VFX 写法。

---

## 🎥 纪录片与采访

### k4-010 · Kling 4.0 极光之上的静默对接
`kling-4.0` `documentary` `rain` `explosion` · 21:9 / 15s · [flaqai/awesome-kling-4-0](https://github.com/flaqai/awesome-kling-4-0/blob/main/prompts/genre-action-and-sound.md)

```
[OUTPUT]

15 seconds, 21:9, realistic near-future orbital docking visualization, calm procedural tone, three shots.

[VEHICLE LOCKS]

Service craft: small white cylinder, four folded rectangular solar panels, black circular docking ring at nose, no crew visible. Station: gray research module with matching axial port and two long blue solar arrays. Blank surfaces, no national or company marks.

[ORIENTATION]

Station docking axis runs screen left-to-right. Station port faces frame left; service craft approaches from frame left nose-first. Earth limb remains low background with a faint auroral band. Sunlight direction stays upper right.

[TIMED SHOTS]

0–5s — Long-lens side view. Craft closes distance slowly at less than one body length over five seconds. Two tiny lateral thruster pulses correct upward drift; exhaust is brief and subtle. Station remains inertially steady.

5–10s — Camera cuts to station-port view looking outward. Craft nose stays centered using one short roll correction under five degrees, then stops all visible rotation. No rapid zoom.

10–15s — Exterior three-quarter. Docking rings meet at near-zero relative speed, compress slightly and lock with one small mechanical movement. Solar arrays do not flex. End with both vehicles moving as one while Earth drifts slowly behind.

[AUDIO]

Exterior shots have no diegetic sound. A restrained non-diegetic tonal bed continues. At contact, cut briefly to an interior structural microphone perspective for one muted latch thump and two confirmation clicks; no voice-over.

[CONSTRAINTS]

Visualization, not operational instruction. Preserve ports, axes, solar panels, light and low relative speed. No explosion, debris, visible exterior sound wave, large flame, astronaut, flag, readable UI, mission claim, logo or watermark.
```

> 💡 轨道对接物理可视化：固定轴线、低相对速度、接触瞬间切内部麦克风视角收音，硬科幻纪录片模板。

---

## 🌌 奇幻与科幻

### k4-011 · Kling 4.0 玻璃蝠鲼盐峡追逐
`kling-4.0` `fantasy-scifi` `dialogue` `aerial` `rain` `explosion` · 12s · [flaqai/awesome-kling-4-0](https://github.com/flaqai/awesome-kling-4-0/blob/main/prompts/action-and-vfx.md)

```
[OUTPUT]

12 seconds, ultra-wide science-fantasy pursuit, photorealistic materials, three shots, fast but readable action, no weapons.

[CONTINUITY ANCHORS]

Courier Nara: adult rider, sand-colored protective suit, compact backpack, opaque bronze visor.

Skimmer: one-seat rectangular solar skimmer, weathered cream shell, two dark solar panels on its nose, no wheels or logo.

Sky creature: colossal translucent manta-shaped cloud organism, glasslike membrane with slow internal light currents.

Preserve all designs, scale relationships and travel direction left-to-right.

[WORLD]

Pale salt canyon after a storm. Hard slope descends left-to-right toward mirrored pools. Late sun frame left; wind carries loose crystalline dust downhill.

[TIMED SHOTS]

0–4s — Low parallel tracking shot on Nara’s left side, camera and skimmer moving downhill at equal speed. Skimmer banks 20 degrees into one right curve; Nara leans with it. The rear edge throws one continuous dust ribbon that follows the curve and settles under gravity.

4–8s — Wide aerial trailing shot, never crossing the travel axis. The glass manta glides overhead in the same direction but slower, casting a broad moving shadow that overtakes Nara. Its wings complete one heavy downstroke; canyon dust reacts half a second later.

8–12s — Front three-quarter low shot moving backward at matched speed. A narrow salt ridge breaks ahead. Nara pulls the skimmer nose upward and clears one two-meter gap; suspension compresses visually on landing through a brief body dip and dense dust burst. The manta passes above, filling the sky as camera holds horizon level.

[AUDIO]

Steady electric turbine whine, granular salt hiss and strong crosswind. Wing downstroke produces a deep airy pressure pulse at 6s. Landing has one low impact plus settling crystals. No dialogue or music.

[CONSTRAINTS]

Skimmer remains in ground effect, never becomes an aircraft. Rider stays seated with both hands on controls. Physically delayed dust and shadow reaction. One gap, one jump, one creature. No collision, explosion, weapon, duplicate vehicle, changing visor, impossible camera teleport, backwards dust, logos, text or watermark.
```

> 💡 科幻追逐：每拍只做一个特技、尘埃与阴影延迟半秒反应，三镜头保持轴线，动作可读性的写作方法。

---

## 👤 人物与肖像

### k4-012 · Kling 4.0 未发送的语音备忘
`kling-4.0` `portrait` `dialogue` `close-up` `night` `rain` · 9:16 / 12s · [flaqai/awesome-kling-4-0](https://github.com/flaqai/awesome-kling-4-0/blob/main/prompts/cinematic-and-dialogue.md)

```
[OUTPUT]

12 seconds, 9:16 vertical, one uninterrupted handheld close-up, natural smartphone night footage, no cuts.

[CONTINUITY ANCHOR]

Noor: adult woman in her late 20s, warm brown skin, short coiled hair, oversized gray sweatshirt, tiny silver stud earrings. She sits on a kitchen floor against pale cabinets. Plain phone in her left hand; right thumb hovers above an unmarked send area.

[CAMERA]

Phone-camera viewpoint from a friend sitting on the opposite floor, chest-height close-up. Small breathing drift only; lens and distance remain constant. Focus stays on Noor’s eyes, then briefly shifts to her hovering thumb at 8s and returns to her face.

[PERFORMANCE TIMELINE]

0–3s — Noor listens to the end of her own recorded message through one earbud. Her jaw is held tight; breathing shallow.

3–7s — She mouths the first word of a reply but makes no sound. Her eyes become wet without tears falling. She gives a tiny self-conscious laugh and looks away.

7–10s — Her right thumb lowers toward the phone, pauses one centimeter above it, then deliberately moves away. The phone stays supported in her left palm.

10–12s — Shoulders release on a slow exhale. She locks the phone with one soft click and looks directly into the camera, calm rather than defeated.

[AUDIO]

Refrigerator hum, faint traffic through a closed window, sweatshirt fabric and breath. A barely audible voice-note tail from the earbud is unintelligible. One phone lock click at 10.7s. No dialogue, music or notification sound.

[CONSTRAINTS]

No visible app UI, readable text, tears falling, beauty filter or theatrical sobbing. Preserve face, earrings, phone, hands and floor position. Natural fingers and phone contact; no screen glow changing color; no cuts, zoom, orbit or background change.
```

> 💡 一镜到底竖屏微表演：情绪按秒渐进的时间轴加焦点调度，手机夜拍质感的肖像叙事上限。

---
