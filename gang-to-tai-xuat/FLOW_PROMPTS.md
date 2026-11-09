# Găng Tơ Tái Xuất — Bộ 108 Prompt Google Flow Omni (27 Cảnh × 4 Clips × 15s)

- **Giọng Người Dẫn Chuyện (cố định cả 108 clip):** Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; đọc nhanh liên thanh như oan-thai-doi-me, ~4.0 âm tiết/giây, liền một hơi, không ngắt giữa câu.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 108 clips × 15s — 67 clip VO + 41 clip thoại (27 clip có hai lượt thoại); lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 19 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 79 clip ảnh nhân vật (Ingredients), 10 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** clip VO được tăng tốc giọng thêm 1.18x khi tải về (`FLOWKIT_VOICE_TEMPO` mặc định 1.18, đặt 1.0 để tắt), giữ nguyên khung hình 15s; clip lip-sync không bao giờ bị tăng tốc để khớp khẩu hình.
- **Màu phim & ánh sáng:** Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py gang-to-tai-xuat` sinh lại toàn bộ clip, README, kịch bản.

---

## Cảnh 01 - Clip 1 (`canh-01/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn aerial over the tiled roofs of Hà Nội's old quarter: an ancient brick city gate, tangled wires, motorbikes streaming, pink-gold light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: motorbike riders streaming through the narrow streets far below
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm aerial drone glide sweeping forward and descending to the city gate arch; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: High aerial view at dawn over a vast sea of mossy tiled roofs in Hà Nội's old quarter, pink-gold sunlight spilling across the rooftops as wisps of morning mist curl between them.
- 3.0–7.0s: The drone glides forward over tangled overhead wires while motorbike riders stream through the narrow streets far below like bright rivers, their headlamps twinkling in the soft golden light.
- 7.0–11.0s: The camera sweeps down to the brick city gate, its curved tiled roof glowing gold, where @Lam wipes the seat of the old cream-colored step-through motorbike with a round chrome headlamp under the arch.
- 11.0–15.0s: @Lam settles a battered green pith helmet on his grey crew cut and gives the seat a fond pat, his mouth closed in a calm half-smile as the sunrise flares through the arch. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Phố cổ Hà Nội buổi sớm, ba mươi sáu phố phường vừa thức giấc trong tiếng rao, và dưới cổng Ô Quan Chưởng có ông Lâm xe ôm, sáu mươi ba tuổi, hiền như đất, chở cụ già đi chợ chẳng bao giờ lấy của ai một đồng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a chorus of distant motorbike horns waking the streets, a faraway street vendor's call, pigeons' wings fluttering past, a cloth squeaking on vinyl. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 2 (`canh-01/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn in Hà Nội's old quarter: an ancient brick city gate with a tiled roof, narrow streets of tube houses with green shutters, tangled overhead wires, street vendors with shoulder poles, pink-gold morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: a tiny old lady with a conical hat and a shopping basket
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm close-up from the front of the motorbike with a slow arc; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Close on the old cream-colored step-through motorbike with a round chrome headlamp parked by the brick city gate, dawn light glinting on the chrome and a woven shopping basket resting on the worn stones.
- 3.0–7.0s: @Lam, astride the motorbike, turns over his shoulder and speaks warmly to a tiny old lady in a conical hat, patting the back seat as she climbs on by herself.
- 7.0–11.0s: The old lady holds out a few folded banknotes, and @Lam keeps talking with a gentle wave of his hand, refusing them until she tucks the money back into her basket.
- 11.0–15.0s: @Lam finishes, closes his mouth into a crinkle-eyed grin and faces forward, while the old lady settles the basket on her lap and nods with her lips pressed in a shy smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.5s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cụ cứ ngồi vững vào, ôm cái giỏ cho chắc, tiền nong gì cụ ơi, cháu chở cụ như chở mẹ cháu thôi, cụ cất tiền đi mà mua mớ rau, con cá." (no subtitles)
- From 3.0s onward, @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the motorbike engine idling, a basket handle creaking, sparrows chirping, distant horns echoing off the gate. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 3 (`canh-01/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn in Hà Nội's old quarter: an ancient brick city gate with a tiled roof, narrow streets of tube houses with green shutters, tangled overhead wires, street vendors with shoulder poles, pink-gold morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: an old street vendor woman in a conical hat with a shoulder pole of fruit baskets, standing on the far pavement
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium side-tracking shot gliding alongside the motorbike; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A narrow old-quarter street of tube houses with green shutters glows in pink-gold morning light, tangled wires sagging overhead and steam curling from a pot on an empty pavement stall.
- 3.0–7.0s: @Lam rides the old cream-colored step-through motorbike with a round chrome headlamp slowly down the street, mouth closed, as an old vendor on the far pavement dips her head low to greet him.
- 7.0–11.0s: @Lam lifts two fingers from the handlebar in a small salute, and a gust of morning wind flips back the loose sleeve of his grey windbreaker on his right forearm.
- 11.0–15.0s: For a heartbeat the clawed tail of a dark-green dragon tattoo gleams on his wrinkled forearm, then the sleeve falls back and @Lam glances down with a faint knowing closed-mouth smile. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Không ai trong phố biết, ba mươi năm trước, chính ông già hiền lành này từng khiến cả phố cổ phải cúi đầu, người ta gọi ông là Lâm Rồng, và con rồng ấy đã ngủ yên dưới lớp tay áo cũ suốt ba mươi năm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft putter of an old motorbike engine, a shoulder pole creaking, a rush of wind flapping fabric, a single low gong-like hum fading. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 4 (`canh-01/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 28mm wide shot with a slow push-in on the shutter; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: A narrow old-quarter alley at night under a single yellow streetlamp, potted plants beside a doorstep and puddles shining on the wet pavement beneath tangled wires.
- 3.0–7.0s: The camera glides toward a closed rolling steel shutter where glossy bright red paint runs down the corrugated steel in long thick streaks, dripping from every ridge.
- 7.0–11.0s: Red paint pools on the doorstep and creeps across the wet pavement toward a puddle, the alley completely empty and silent under the buzzing yellow lamp.
- 11.0–15.0s: The camera settles close on one fresh red drip sliding down the shutter and falling into the puddle, a red ripple spreading across the reflected yellow lamplight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cho đến cái đêm có một bọn nhóc dám hắt sơn đỏ lên cánh cửa nhà ông, ngay trong con ngõ nhỏ ông đã sống hiền lành suốt nửa đời người, và chúng đâu hề biết rằng, mình vừa đánh thức một con rồng đang ngủ say." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: slow wet drips of paint, a dog barking far away, the last motorbike engine fading out of the alley. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 1 (`canh-02/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot with a slow dolly-in toward the table; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the narrow tube house at night, one warm lamp glows over a worn wooden table where an open laptop casts a cool blue light beside a small family altar with curling incense.
- 3.0–7.0s: @Mai sits down at the table in her oversized lavender hoodie, straightens her round glasses and types quickly, her face lit blue by the glowing laptop, her mouth closed.
- 7.0–11.0s: A phone beside the laptop buzzes and rattles against the wood, its blank screen flashing bright white, and @Mai freezes with her fingers on the keys, lips pressed tightly together.
- 11.0–15.0s: @Mai flips the phone face-down and keeps her palm flat on top of it, the buzzing muffled against the wood as her shoulders rise and fall under the lavender hoodie. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Mai, cháu gái ông, hai mươi tuổi, sinh viên công nghệ thông tin, được ông Lâm một tay nuôi lớn từ năm lên ba, nhưng mấy tuần nay, chiếc điện thoại của cô cứ rung lên suốt đêm, toàn những số máy lạ không tên." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: quick soft keyboard taps, a phone vibrating hard against a wooden table, muffled buzzing, a ticking wall fan. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 2 (`canh-02/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm close-up with a slow pull-back from the table; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Mai lifts her palm off the face-down phone and leans back from the table, her lips pressed shut, the laptop's blue glow and the warm lamp lighting her face from two sides.
- 3.0–7.0s: @Mai counts silently on her fingers, one finger after another, her eyes darting across the glowing blank laptop screen as her brow knots tighter.
- 7.0–11.0s: @Mai stops at the last finger, then slowly cups both palms over her mouth and nose, eyes fixed wide on the screen, her shoulders sinking inside the lavender hoodie.
- 11.0–15.0s: As the camera pulls back, @Mai sits small and still at the worn wooden table in the dim tube house, the face-down phone buzzing faintly beside the glowing laptop. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ba tháng trước, cô vay năm triệu qua một ứng dụng trên mạng, lãi mẹ đẻ lãi con, phí chồng lên phí, mới chín mươi ngày mà con số ấy đã phình thành một trăm năm mươi triệu đồng, gấp ba mươi lần số tiền cô vay." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the muffled buzz of a face-down phone, a wall clock ticking, incense crackling softly on the altar, a slow shaky exhale. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 3 (`canh-02/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot at the foot of the staircase with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The steep wooden staircase at the back of the dim tube house, lit only by a sliver of warm lamplight, a small black backpack slumped on the bottom step.
- 3.0–7.0s: @Mai crouches on the bottom step hugging her knees, presses the phone to her ear and whispers fast and pleading into it, her face lit by its pale glow.
- 7.0–11.0s: @Mai keeps whispering into the phone with her face clearly visible, her eyes flicking toward the dark back of the room where the single bed stands.
- 11.0–15.0s: @Mai finishes, closes her mouth and squeezes her eyes shut, the phone still at her ear and her free hand clutching the hood strings of her lavender hoodie. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.5s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh ơi, em xin anh thêm một tuần thôi, em sẽ trả đủ, em hứa mà, nhưng xin anh đừng gọi cho bạn bè với thầy cô của em nữa, em van anh đấy!" (no subtitles)
- From 3.0s onward, @Mai's face and lips stay clearly visible while speaking; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a hushed whisper in the quiet house, a faint buzz from the phone earpiece, the wooden step creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 4 (`canh-02/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up with a slow tilt down onto the pillow; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The camera starts on the shadowy back wall of the tube house, a battered green pith helmet hanging on a nail, lit by a thin sliver of warm lamplight.
- 3.0–7.0s: The camera tilts down to the single bed where @Lam lies still on his back under a thin blanket, his eyes wide open in the dark, catching the lamplight.
- 7.0–11.0s: @Lam keeps perfectly still with his mouth closed, only his eyes sliding toward the staircase, where @Mai, soft in the background, wipes her tears with the sleeve of her lavender hoodie.
- 11.0–15.0s: @Mai tucks the phone deep into her hoodie pocket and turns toward the rolling steel shutter with her lips pressed together, while @Lam's jaw slowly tightens in the foreground. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ở giường trong, ông Lâm vẫn nằm im, nhưng đôi mắt ông mở to trong bóng tối, nghe không sót một lời, còn Mai lau nước mắt, giấu điện thoại đi, không hề biết rằng ngay đêm mai, bọn đòi nợ sẽ tìm đến tận cửa nhà." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft sniff from across the room, a slow creak of the bed frame, a gecko chirping on the wall, a motorbike engine revving far down the alley. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 1 (`canh-03/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
- Extra: four young men in black riding motorbikes into the alley, faces in shadow
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 24mm wide low-angle shot with a slow pan following the headlights; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: The narrow old-quarter alley at night under a single yellow streetlamp, puddles gleaming on the wet pavement, potted plants lining the walls and tangled wires sagging overhead.
- 3.0–7.0s: Four black motorbikes roar into the alley one after another, the young riders in black revving their engines, headlights sweeping across the old walls and their faces lost in shadow.
- 7.0–11.0s: The headlights rake across the potted plants and green shutters as the riders weave down the narrow lane in single file, spraying water from the puddles.
- 11.0–15.0s: The four motorbikes brake to a stop in a tight row before a closed rolling steel shutter, engines idling as their headlights glare through drifting exhaust haze. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đêm hôm sau, bốn chiếc xe máy rồ ga lao vào con ngõ nhỏ, tiếng pô nổ vang cả dãy phố, đèn pha quét loang loáng trên những bức tường cũ, rồi cả bốn chiếc phanh kít, đỗ thành một hàng ngay trước cửa nhà ông Lâm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: four motorbike engines revving and popping, exhaust backfires echoing off the alley walls, tires splashing through puddles, a dog barking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 2 (`canh-03/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium low-angle shot with a smooth lateral dolly toward the shutter; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A parked black motorbike ticks under the yellow streetlamp beside a puddle, a dented bucket of red paint hanging from its handlebar as exhaust haze drifts through the light.
- 3.0–7.0s: @Beo strides into the lamplight in flip-flops, his fake-gold chain swaying over his black tank top, and unhooks the paint bucket from the handlebar with one thick hand, mouth closed in a smirk.
- 7.0–11.0s: @Beo plants his flip-flops a few steps back from the closed rolling steel shutter and heaves the bucket forward, a glossy arc of bright red paint sailing through the lamplight onto the empty steel.
- 11.0–15.0s: Red paint streams down the shutter in thick glossy rivulets onto the doorstep as @Beo steps back admiring his work, the empty bucket dangling from one hand, his lips shut in a smug grin. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cầm đầu là Béo Đầu Sấm, đòi nợ thuê cho công ty Phú Quý, khét tiếng khắp các trường đại học Hà Nội, hắn xách xô sơn xuống xe, chẳng nói chẳng rằng, hắt thẳng lên cánh cửa cuốn, sơn đỏ chảy loang lổ xuống tận bậc thềm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a side stand clanking down, a metal bucket handle squeaking, a heavy wet splash of paint across corrugated steel, paint dripping and trickling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 3 (`canh-03/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide two-shot from the side of the alley with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The paint-soaked rolling steel shutter drips red onto the doorstep under the streetlamp, the old cream-colored step-through motorbike with a round chrome headlamp parked beside it, a battered green pith helmet on its seat.
- 3.0–7.0s: The shutter rattles up to reveal @Lam on screen-right in his half-zipped grey windbreaker, while @Beo on screen-left points at the house and speaks loudly, @Lam listening with his mouth closed.
- 7.0–11.0s: @Beo finishes and shuts his mouth in a smug grin, and @Lam looks up from the dripping paint and answers in a calm low voice, his hands relaxed at his sides.
- 11.0–15.0s: @Lam finishes, closes his mouth and gives a small unhurried nod toward the end of the alley, while @Beo snorts and folds his thick arms over his black tank top, lips shut. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.3s, spoken on camera by @Beo (man of 28, strictly standard Hà Nội Northern accent (never Southern accent), rough loud bass, blustering, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Nhà này có con bé Mai nợ tiền Phú Quý, ba ngày không trả thì lần sau không phải sơn đâu!"
- Turn 2, 8.8–13.5s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Cháu tôi nợ bao nhiêu, ông già này trả, các cậu về đi cho hàng xóm còn ngủ."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a steel shutter rattling and rolling up, paint dripping onto the step, motorbike engines idling behind, a window creaking open somewhere above. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 4 (`canh-03/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot with a slow tilt down to the puddle; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Beo unfolds his arms, strolls to the old cream-colored step-through motorbike with a round chrome headlamp and lifts a battered green pith helmet off its seat, dangling it from two fingers, his mouth still closed.
- 3.0–7.0s: @Beo turns to @Lam and mocks him aloud with a gold-toothed sneer, swinging the helmet by its chin strap, while @Lam stands still by the shutter with his mouth closed.
- 7.0–11.0s: @Beo keeps talking as he holds the helmet out over a wide puddle under the yellow streetlamp, his face and lips clearly visible, while @Lam watches in silence.
- 11.0–15.0s: @Beo finishes, closes his mouth and simply opens his fingers, the helmet dropping into the puddle and rocking upside down while @Lam stands motionless behind it, only watching, his jaw set. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.5s, spoken on camera by @Beo (man of 28, strictly standard Hà Nội Northern accent (never Southern accent), rough loud bass, blustering, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông già xe ôm thì lấy gì mà trả? Bán cái mũ cối rách này đi à? Thôi, tôi trả lại ông đây, ba ngày nữa bọn tôi quay lại đấy, ông già ạ!" (no subtitles)
- @Beo keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a hollow plop and splash of water, ripples lapping, a mocking snort, motorbike engines idling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 1 (`canh-04/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm close-up with a slow tilt up from the puddle; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: In the empty night alley, a battered green pith helmet lies upside down in a puddle under the yellow streetlamp, red paint still dripping from the steel shutter behind it.
- 3.0–7.0s: @Lam crouches down slowly in his grey windbreaker, lifts the helmet out of the puddle with both hands and lets the muddy water pour from it, his mouth closed.
- 7.0–11.0s: @Lam wipes the helmet slowly with his sleeve, round and round, his eyes lowered and his lips pressed together as the camera rises to his quiet weathered face.
- 11.0–15.0s: @Lam holds the helmet against his chest and lifts his gaze to the red-streaked shutter, the yellow lamplight glinting in his cloudy left eye, his mouth firmly closed. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bọn chúng đi rồi, ông Lâm mới chậm rãi cúi xuống nhặt chiếc mũ cối dưới vũng nước, lau thật chậm, hết vòng này đến vòng khác, không nói lấy một lời nào, chỉ có đôi mắt cứ nhìn mãi vào cánh cửa cuốn nhuộm đỏ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water trickling from the helmet, a slow drip of paint, crickets, distant motorbikes fading. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 2 (`canh-04/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide two-shot with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the tube house at night, the worn wooden table glows under one warm lamp, a battered green pith helmet resting damp on it beside a folded towel.
- 3.0–7.0s: @Mai stands at the foot of the staircase on screen-right facing @Lam at the table on screen-left, her eyes brimming, and speaks to him in a trembling rush while he listens, mouth closed.
- 7.0–11.0s: @Mai keeps speaking with her face clearly visible, twisting the hem of her lavender hoodie in both hands, as @Lam slowly lowers the towel and stares at her.
- 11.0–15.0s: @Mai finishes and closes her mouth, while @Lam lifts his fingertips to the corner of his cloudy left eye, his lips quivering but pressed shut. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.8s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông ơi, cháu xin lỗi ông, cháu vay tiền là để ông đi mổ mắt, bác sĩ bảo mắt ông để lâu nữa là mù hẳn, cháu sợ ông lo nên không dám nói ạ." (no subtitles)
- From 3.0s onward, @Mai's face and lips stay clearly visible while speaking; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a shaky breath, the lamp buzzing softly, water dripping from the helmet onto the table. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 3 (`canh-04/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 40mm medium profile two-shot with a slow arc around them; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam sets the towel down and rises from the table, stepping close to @Mai at the foot of the staircase, both of them silent with their mouths closed in the warm lamplight.
- 3.0–7.0s: @Lam speaks to her softly in a low warm voice, his weathered face fully visible and his narrow eyes glistening, while @Mai listens with her lips pressed together.
- 7.0–11.0s: @Lam finishes and closes his mouth, and @Mai shakes her head and answers fast through her tears, holding up her phone with its blank glowing screen.
- 11.0–15.0s: @Mai finishes and closes her mouth, her chin quivering, as @Lam gently takes the phone from her and lays it face-down on the wooden table, his palm flat on top of it. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.2s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Mắt ông mù cũng được con ạ, chứ để con khổ thế này thì ông còn sống làm gì nữa."
- Turn 2, 8.7–14.2s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Mình trả không nổi đâu ông ơi, lãi mỗi ngày một tăng, bọn nó còn dọa gửi ảnh cháu cho cả lớp."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a muffled sob, the lamp humming, a floorboard creaking, a phone buzzing once against wood. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 4 (`canh-04/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up with a slow push-in to his eyes; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam lifts his rough hand and gently strokes @Mai's hair as she bows her head against his shoulder, both of their mouths closed in the warm lamplight.
- 3.0–7.0s: @Mai wipes her eyes under her round glasses and climbs the steep staircase, glancing back once with her lips pressed together before she disappears into the dark upstairs.
- 7.0–11.0s: @Lam stands alone at the foot of the staircase, his tender gaze lingering on the dark stairs, then slowly turns his face toward the red-stained rolling steel shutter.
- 11.0–15.0s: @Lam's narrow eyes harden and his jaw sets as he stares at the shutter, a steely glint rising in his gaze under his thick grey eyebrows while his mouth stays firmly closed. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm khẽ xoa đầu đứa cháu gái đã một mình gánh khoản nợ ấy chỉ vì con mắt mờ đục của ông, rồi quay nhìn ra cánh cửa nhuộm đỏ, và ánh mắt hiền lành suốt ba mươi năm ấy bỗng lạnh đi như thép." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: footsteps fading up the wooden stairs, a slow paint drip outside, a deep low hum swelling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 1 (`canh-05/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- Extra: rows of young callers in headsets at glowing monitors
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide shot with a slow tilt down from the neon ceiling to the aisle; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: High in a glass tower by day, purple and gold neon accent lights without letters glow along the ceiling of a flashy call-center office, the bright Hà Nội skyline shimmering beyond the windows.
- 3.0–7.0s: The camera tilts down over long rows of young callers in headsets hunched at glowing blank monitors, typing fast and tapping their earpieces, every mouth closed.
- 7.0–11.0s: @Hung strides down the aisle between the desks in his oversized black satin bomber jacket, holding a phone on a small selfie gimbal at arm's length with a cocky closed-mouth grin.
- 11.0–15.0s: @Hung stops in the middle of the room, winks at his own phone and smooths his ash-blond undercut, his silver rings flashing under the neon and his lips closed in a smug curl. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trên tầng hai mươi lăm tòa nhà kính, ba chục nhân viên công ty Phú Quý gọi điện đòi nợ suốt ngày đêm, và ông chủ là Hưng, ba mươi mốt tuổi, ứng dụng vay tiền của hắn hút về tiền tỷ mỗi tháng từ những sinh viên nghèo." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a hum of keyboards clattering, phones ringing on every desk, white high-top sneakers squeaking on the polished floor, a gimbal motor whirring. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 2 (`canh-05/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- Extra: rows of young callers in headsets at glowing monitors
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm close-up with a slow pull-back; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Hung raises the phone on its small selfie gimbal close to his face, flicks his ash-blond fringe and flashes a wide grin at the lens, his mouth still closed.
- 3.0–7.0s: @Hung speaks loudly into the phone like a livestream salesman, grinning wide, his gold-rimmed glasses gleaming in the purple and gold neon glow.
- 7.0–11.0s: @Hung keeps talking as he fans out a thick wad of banknotes beside his face, his lips moving fast and clearly, the rows of callers blurred behind him.
- 11.0–15.0s: @Hung finishes his pitch, closes his mouth and poses with the gimbal held high as the camera pulls back, his lips closed in a cocky grin above the rows of desks. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.5s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chào cả nhà, Hưng Phú Quý lên sóng đây, sinh viên cần tiền thì cứ bấm vào, vay nhanh năm phút, không cần thế chấp, không cần giấy tờ, tiền về liền tay, thả tim cho anh nào!" (no subtitles)
- @Hung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a flutter of banknotes, a cheerful notification chime, keyboards clattering, a gimbal motor whirring. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 3 (`canh-05/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 40mm medium two-shot inside the glass room with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the glass-walled boss room, the white leather sofa sits under a glowing ring light, a gold neon strip without letters reflecting on the glass walls.
- 3.0–7.0s: @Hung lounges on the white leather sofa on screen-left as @Beo stands before him on screen-right, rubbing his shaved head and reporting in a loud rough voice while @Hung listens, lips pressed together.
- 7.0–11.0s: @Beo finishes and closes his mouth, and @Hung lets out a short scoff, leans forward and answers him with a mocking smirk, his face clearly visible in the ring light.
- 11.0–15.0s: @Hung finishes, closes his mouth and flicks his ringed fingers toward the door in a lazy wave, and @Beo nods quickly and hurries out of the glass room. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Beo (man of 28, strictly standard Hà Nội Northern accent (never Southern accent), rough loud bass, blustering, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Đại ca, con bé Mai có ông nội chạy xe ôm, lão già bảo sẽ trả nợ thay cháu."
- Turn 2, 8.3–13.6s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Ông già xe ôm à? Càng già càng sợ mất mặt, gửi ảnh con bé cho cả lớp nó xem đi."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the glass door sliding shut, the ring light humming, leather creaking, heavy flip-flop footsteps hurrying away. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 4 (`canh-05/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot with a slow pull-back from the glass wall; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The glass-walled boss room high above the city, its ring light glowing and purple neon reflecting on the glass, the sunlit Hà Nội skyline shimmering beyond the tall windows.
- 3.0–7.0s: @Hung strolls to the window in his black satin bomber jacket and slides his hands into his pockets, looking down at the city with one corner of his lip curled in a closed-mouth smirk.
- 7.0–11.0s: @Hung tilts his head and admires his own reflection in the glass, smoothing his ash-blond undercut with his ringed fingers, his lips still closed.
- 11.0–15.0s: As the camera pulls back, @Hung stands small against the vast window while far below a cloud shadow slides slowly over the tiled roofs of the old quarter. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Hưng đứng bên cửa kính nhìn xuống thành phố, cười khẩy, với hắn, một lão già xe ôm thì có gì mà phải sợ, hắn không hề biết rằng mình vừa chọc vào tổ của một con rồng phố cổ đã ngủ yên suốt ba mươi năm trời." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft air conditioner hum, a faint lift chime, distant traffic far below, a single low gong-like hum. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 1 (`canh-06/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium low-angle shot with a slow dolly-in toward the bed; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The dim back of the tube house at night under one warm lamp, the single bed against the wall and a gap of deep dusty shadow beneath it.
- 3.0–7.0s: @Lam kneels on the tiled floor beside the bed, reaches deep underneath it and slides out a rusty round biscuit tin furred with dust, his mouth closed.
- 7.0–11.0s: @Lam wipes the dust off the lid in a soft grey cloud and pries it open with his thumbs, revealing a nest of yellowed papers covered in faint unreadable lines.
- 11.0–15.0s: @Lam lifts out a faded photo of three young friends from the nineties, their faces tiny, and holds it in the lamplight, his thumb gently stroking its worn edge, his lips pressed together. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đêm ấy, ông Lâm lặng lẽ lôi ra từ gầm giường một chiếc hộp bánh quy bằng sắt rỉ sét, đã ba mươi năm không mở, bên trong là tấm ảnh cũ, ba người bạn trẻ khoác vai nhau giữa phố cổ những năm chín mươi." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: metal scraping across tiles, a soft puff of dust, a rusty lid squeaking open, old paper rustling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 2 (`canh-06/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 100mm extreme close-up with a slow glide along his forearm up to his eyes; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The worn wooden table under the warm lamp, a rusty round biscuit tin lying open beside a faded photo of three young friends from the nineties, their faces tiny, in a curl of incense smoke.
- 3.0–7.0s: @Lam's right forearm moves into the lamplight and his left hand slowly rolls the grey windbreaker sleeve up past his elbow, fold by fold.
- 7.0–11.0s: The full dark-green dragon tattoo is revealed coiling from wrist to elbow over his wrinkled skin, its scaled body, claws and whiskered head gleaming in the warm light as his fingers slowly curl closed.
- 11.0–15.0s: The camera glides up from the tattoo to @Lam's weathered face, his narrow eyes catching the lamplight with a hard bright gleam, his mouth set in a firm closed line. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông chậm rãi xắn tay áo lên, con rồng xanh sẫm cuộn từ cổ tay lên tận khuỷu vẫn còn nguyên từng chiếc vảy, chỉ có làn da là đã già đi, và trong đôi mắt mờ đục ấy, ngọn lửa cũ bắt đầu cháy lại." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: fabric rustling as a sleeve rolls up, a deep low boom, incense crackling softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 3 (`canh-06/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A small shelf by the staircase holds an old cream-colored landline phone with a coiled cord, lit by the warm lamp beside the family altar and its glowing incense.
- 3.0–7.0s: @Lam lifts the receiver to his ear with his tattooed forearm bared and speaks into it in a low, steady voice, his face clearly visible in the lamplight.
- 7.0–11.0s: @Lam keeps talking into the receiver with a dry half-smile, one thick grey eyebrow lifting, his lips moving clearly under the warm lamp.
- 11.0–15.0s: @Lam finishes, closes his mouth and listens, the corner of his lips twitching upward as he holds the receiver against his ear. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.8s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Hoa đấy à? Lâm đây. Ừ, Lâm Rồng đây. Ba mươi năm rồi mới gọi, bà đừng mắng vội. Mai bà gọi cả ông Khoa đến quán, Rồng lại cần Hổ với Báo rồi." (no subtitles)
- From 3.0s onward, @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the click of an old receiver lifting, a faint line crackle, the lamp humming. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 4 (`canh-06/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam holds the receiver to his ear with his mouth closed as a faint raspy chuckle crackles from it, the corners of his narrow eyes crinkling.
- 3.0–7.0s: @Lam sets the receiver back on its cradle with a soft click and lets his hand rest on it for a moment, his tattooed forearm glowing in the warm lamplight.
- 7.0–11.0s: @Lam picks up a battered green pith helmet from the table and settles it firmly on his grey crew cut, tilting the brim down over his eyes with two fingers.
- 11.0–15.0s: @Lam raises his eyes from under the brim and slowly breaks into a sly closed-mouth smile, one thick grey eyebrow lifting, the lamplight glinting in his narrow eyes. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đầu dây bên kia vang lên một tiếng cười khàn khàn, như thể người ấy đã chờ cuộc gọi này suốt ba mươi năm, ông Lâm đội lại mũ cối, và lần đầu tiên sau ngần ấy năm, ông mỉm cười kiểu của Lâm Rồng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a raspy woman's low chuckle crackling faintly from the receiver, a receiver clicking onto its cradle, a deep low boom, the lamp humming warmly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 1 (`canh-07/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- Extra: a long line of customers waiting on the pavement
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide shot with a slow crane-up through the smoke; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Rows of grilled pork patties sizzle and spit over glowing charcoal on the pavement, thick white smoke billowing up through warm sunlight beside baskets of fresh herbs.
- 3.0–7.0s: The camera rises through the smoke over low plastic stools and steel tables, revealing a long line of customers waiting along the pavement to the end of the street, mouths closed.
- 7.0–11.0s: @BaHoa steps up to the grills in her purple floral silk blouse and fans the glowing charcoal briskly with a woven bamboo fan, orange sparks dancing up through the smoke.
- 11.0–15.0s: @BaHoa glances at the camera through the smoke, her red lips closed in a knowing curve, and gives a slow sly wink as her gold hoop earrings swing. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trưa hôm sau, quán bún chả đông nhất phố Hàng Mành khói bay mù mịt, khách xếp hàng dài tận đầu ngõ, bà chủ là Hoa, sáu mươi mốt tuổi, ba mươi năm trước là bộ não của cả băng, giang hồ gọi là Hoa Hổ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pork sizzling over charcoal, a bamboo fan whooshing in quick strokes, chopsticks clinking on bowls, gold bangles jangling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 2 (`canh-07/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot across the grill with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A smoky charcoal grill on the pavement in noon sunlight, pork patties sizzling beside a steel table with a basket of herbs and two low plastic stools.
- 3.0–7.0s: @Lam steps up to the grill with a battered green pith helmet under one arm, and @BaHoa looks up from the smoke and speaks to him teasingly while he listens, mouth closed.
- 7.0–11.0s: @BaHoa finishes and closes her red lips into a smirk, and @Lam leans toward her over the smoking grill and answers in a low conspiratorial voice, his narrow eyes twinkling.
- 11.0–15.0s: @Lam finishes, closes his mouth and taps the edge of the steel table twice with one finger, while @BaHoa stops fanning mid-stroke and stares at him, her lips pressed together. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Ba mươi năm không thấy mặt, nay ông đến ăn bún chả hay đến rủ tôi đi tù đấy?"
- Turn 2, 8.3–13.0s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Rủ bà đi lừa một thằng chuyên lừa đảo, lần này mình làm việc thiện, bà Hoa ạ."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pork sizzling, charcoal popping, two light taps on a steel table, a motorbike horn on the street. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 3 (`canh-07/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up favoring Bà Hoa with a slow arc around the grill to Lâm; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @BaHoa snaps the bamboo fan shut in the drifting smoke and taps it against her palm, eyeing @Lam up and down, both of them silent with their mouths closed.
- 3.0–7.0s: @BaHoa points the closed fan at @Lam and speaks fast and bold, her red lips moving clearly and her gold bangle jangling, while @Lam listens with a calm closed-mouth smile.
- 7.0–11.0s: @BaHoa finishes with a wide red-lipped grin and nudges a low plastic stool toward him with her sandal, and @Lam sits down and answers her dryly as the camera arcs to his face.
- 11.0–15.0s: @Lam finishes and closes his mouth in a crinkle-eyed grin, while @BaHoa tips her head back in silent laughter and flips a pork patty on the grill with long chopsticks. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.0s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Lừa người tốt thì tôi giải nghệ rồi, nhưng lừa thằng lừa đảo thì tôi đi ngay, ông ngồi đi!"
- Turn 2, 8.5–12.9s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Ba mươi năm rồi mà bà vẫn thế, nghe đến lừa đảo là mắt sáng rực lên."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a bamboo fan snapping shut, a plastic stool scraping on the pavement, a fresh burst of sizzling, charcoal crackling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 4 (`canh-07/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot with a slow push-in on the mirror; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A small round hand mirror propped against an unlabeled glass jar on the steel counter, a gold lipstick tube lying beside it in the smoky sunlight.
- 3.0–7.0s: @BaHoa unties the checkered apron from her waist and hangs it on a hook, then steps up to the counter with brisk little strides, her mouth closed.
- 7.0–11.0s: @BaHoa leans toward the small mirror with the gold lipstick tube and paints her closed lips a fresh bold red, then presses them together with a soft smack.
- 11.0–15.0s: @BaHoa's reflected eyes narrow into a razor-sharp gleaming look in the little mirror as the camera closes in, one eyebrow rising above a slow closed-mouth smile. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Chưa nghe hết kế hoạch, bà Hoa đã tháo tạp dề treo lên móc, soi vào chiếc gương nhỏ tô lại son thật đỏ, và ánh mắt sắc lẹm của Hoa Hổ ba mươi năm trước bỗng quay trở lại, còn sắc hơn cả ngày xưa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a lipstick cap clicking off, apron strings rustling, the grill crackling behind, a deep low boom. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 1 (`canh-08/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tiny electronics repair stall tucked under a staircase in an old-quarter alley: shelves of old radios and phones, tangled wires, a soldering iron, a magnifier lamp, a single bare bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot with a slow dolly-in to his hands; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A tiny repair stall tucked under a staircase in an old-quarter alley, shelves crammed with old radios and phones, tangled wires hanging down and a single bare bulb glowing.
- 3.0–7.0s: @Khoa hunches over the cluttered workbench in his brown multi-pocket vest, a soldering iron in hand and a thin curl of smoke rising from a circuit board under the magnifier lamp.
- 7.0–11.0s: @Khoa picks up a locked old phone and slides a tiny steel pick into its edge, his long bony fingers twisting the tiny tools in a quick precise blur.
- 11.0–15.0s: With a soft click the back panel pops open and the blank screen lights up with a plain glow, and @Khoa dusts off his fingertips with a smug closed-mouth smile. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Người thứ ba là Khoa, sáu mươi tuổi, sửa đài sửa điện thoại dưới gầm cầu thang, giang hồ gọi là Khoa Báo, ngày xưa chưa có cái két sắt nào ở phố cổ giữ được bí mật quá năm phút trước đôi tay ông." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soldering iron hissing, tiny metallic clicks and scrapes, a crisp final click, an old radio crackling softly on a shelf. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 2 (`canh-08/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tiny electronics repair stall tucked under a staircase in an old-quarter alley: shelves of old radios and phones, tangled wires, a soldering iron, a magnifier lamp, a single bare bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The cramped stall under the staircase lit by a single bare bulb, a magnifier lamp glowing over a workbench strewn with tiny screws and old radio parts.
- 3.0–7.0s: @Lam ducks under the low staircase into the stall on screen-right, and @Khoa looks up from the workbench on screen-left and speaks to him in a dry nasal deadpan while @Lam listens, mouth closed.
- 7.0–11.0s: @Khoa finishes and closes his mouth, and @Lam sets a locked phone with a dark blank screen on the workbench and answers in a calm low voice, his face clearly visible under the bulb.
- 11.0–15.0s: @Lam finishes, closes his mouth and slides the phone across the bench toward @Khoa with two fingers, one grey eyebrow raised in a playful challenge. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.3s, spoken on camera by @Khoa (man of 60, strictly standard Hà Nội Northern accent (never Southern accent), nasal wry tenor, deadpan and fussy, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Hổ vừa gọi, giờ Rồng lại tìm đến tận gầm cầu thang này, chắc phố cổ sắp có chuyện lớn rồi."
- Turn 2, 8.8–14.0s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Có một cái két sắt làm bằng điện thoại cần mở, tay ông Khoa bây giờ còn mở được không?"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: footsteps on the stairs above, the bare bulb buzzing, a phone sliding across a wooden bench, a radio crackling low. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 3 (`canh-08/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tiny electronics repair stall tucked under a staircase in an old-quarter alley: shelves of old radios and phones, tangled wires, a soldering iron, a magnifier lamp, a single bare bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up favoring Khoa with a slow arc to Lâm; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Khoa picks up the phone and weighs it in his palm with a scoff, turning it over under the magnifier lamp, both men silent with their mouths closed.
- 3.0–7.0s: @Khoa speaks in a wry deadpan, wiggling his eyebrows, his face clearly visible under the bare bulb while @Lam listens with his lips pressed together.
- 7.0–11.0s: @Khoa finishes and closes his mouth, and @Lam's shoulders shake with silent laughter before he answers dryly, pointing at the phone with one finger as the camera arcs to him.
- 11.0–15.0s: @Lam finishes and closes his mouth, while @Khoa spins the phone once on the workbench with one finger and stops it flat under his palm, lips pressed into a cheeky smirk. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Khoa (man of 60, strictly standard Hà Nội Northern accent (never Southern accent), nasal wry tenor, deadpan and fussy, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Két nào tôi cũng mở được hết, trừ mỗi cái két trái tim của bà Hoa là chịu thôi."
- Turn 2, 8.3–13.7s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Cái két ấy thì cả phố cổ chịu, ông cứ lo mở cái két của bọn cho vay kia trước đã."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone spinning on wood, the bare bulb buzzing, a radio crackling, tiny screws rattling on the bench. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 4 (`canh-08/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tiny electronics repair stall tucked under a staircase in an old-quarter alley: shelves of old radios and phones, tangled wires, a soldering iron, a magnifier lamp, a single bare bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The cluttered workbench under the magnifier lamp, a row of tiny screwdrivers and picks laid out beside a locked phone with a dark blank screen under a single bare bulb.
- 3.0–7.0s: @Khoa leans in and pulls his thick magnifier glasses down from his forehead onto his eyes, which swell huge and bright behind the lenses, his mouth closed.
- 7.0–11.0s: @Khoa lines up the tiny screwdrivers one by one in a perfectly straight row with his long bony fingers, nudging the last one neatly into place.
- 11.0–15.0s: @Khoa lifts his hands over the tools and they quiver with eager little twitches as he wiggles his fingers like a boy, grinning with closed lips behind the huge lenses. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Khoa kéo cặp kính lúp dày cộp xuống mắt, xếp từng chiếc tua vít tí hon thẳng hàng trên bàn, và lần đầu sau ba mươi năm, đôi bàn tay từng mở mọi két sắt phố cổ ấy lại run lên, không phải vì già, mà vì háo hức." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: glasses clicking into place, tiny tools rattling on the bench, an old radio crackling, a deep low boom. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 1 (`canh-09/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on an old-quarter street with colorful neon signs without readable letters and wet pavement.

[CHARACTERS]
- Extra: three elderly silhouettes seen from behind walking abreast, faces unseen
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 24mm wide low-angle tracking shot following from behind; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: A night street in the old quarter glows with colorful neon signs without readable letters, magenta, jade and gold light rippling across the wet pavement.
- 3.0–7.0s: Three elderly silhouettes seen from behind walk abreast down the middle of the street at an unhurried pace, their long shadows stretching across the neon puddles.
- 7.0–11.0s: The low camera follows the three silhouettes striding side by side, shoulders squared, a pith helmet outline on the middle one and a fan in the hand of the left one.
- 11.0–15.0s: The three silhouettes stop before a half-lowered shutter spilling warm bulb light onto the wet street and stand still for a moment, framed against the golden glow. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–13.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ba mươi năm sau, bộ ba Rồng, Hổ, Báo lại sóng bước trên phố cổ, chậm rãi mà oai như ngày nào, đi qua những biển hiệu đèn màu rực rỡ, về quán bún chả đã kéo nửa cửa của bà Hoa, nơi một kế hoạch táo bạo sắp ra đời." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: three pairs of slow footsteps in unison on wet pavement, the buzz of neon signs, distant motorbike horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 2 (`canh-09/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in Bà Hoa's bún chả shop after closing: plastic stools stacked, one warm bulb over a steel table, cold grills, the shutter half down, an old red landline phone on the counter.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the closed bún chả shop at night, one warm bulb glows over a steel table where an open laptop casts a cool blue light beside stacked plastic stools.
- 3.0–7.0s: @Mai sits at the steel table with the glowing laptop turned away from the camera and speaks quickly and earnestly, her face lit blue, while @BaHoa listens across from her with her red lips closed.
- 7.0–11.0s: @Mai finishes and closes her mouth, and @BaHoa slips on a pair of big black sunglasses and answers with grand haughty gestures, her red lips moving clearly in the bulb light.
- 11.0–15.0s: @BaHoa finishes, closes her mouth and lifts her chin like a tycoon, fanning herself slowly with a bamboo fan, while @Mai presses her lips together to hold back a grin. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.3s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Ứng dụng này lấy cả danh bạ với ảnh người vay, hàng nghìn sinh viên đang bị nó siết như cháu."
- Turn 2, 8.8–13.8s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Thế thì tôi đóng vai bà trùm bất động sản, mang mười tỷ đến đầu tư vào công ty nó."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the laptop fan whirring, the bulb buzzing, a bamboo fan fluttering, a motorbike passing outside the half-down shutter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 3 (`canh-09/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in Bà Hoa's bún chả shop after closing: plastic stools stacked, one warm bulb over a steel table, cold grills, the shutter half down, an old red landline phone on the counter.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up favoring Lâm with a slow arc to Khoa; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The steel table under the single warm bulb in the closed shop, cold grills behind it, two small cups of steaming tea, a plate of peanuts and a small open velvet box.
- 3.0–7.0s: @Lam leans over the steel table and speaks briskly, counting off each role on his fingers, his face clearly visible in the warm light, while @Khoa listens beside him with his mouth closed.
- 7.0–11.0s: @Lam finishes and lays his hand flat on the table, and @Khoa holds up a large gold flower brooch with a tiny hidden camera and answers dryly as the camera arcs to him.
- 11.0–15.0s: @Khoa finishes, closes his mouth and taps the center of the brooch where a tiny lens glints, raising his eyebrows, while @Lam grins beside him with closed lips. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.9s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Bà Hoa làm bà trùm, tôi làm tài xế, ông Khoa lo máy ghi hình, con Mai ngồi ngoài xe giữ đường dây."
- Turn 2, 9.4–13.9s, spoken on camera by @Khoa (man of 60, strictly standard Hà Nội Northern accent (never Southern accent), nasal wry tenor, deadpan and fussy, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Cái trâm cài áo này có mắt, thằng kia nói câu nào là cả nước nghe câu ấy."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a palm laid flat on a steel table, teacups clinking, a tiny electronic beep, the bulb humming. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 4 (`canh-09/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in Bà Hoa's bún chả shop after closing: plastic stools stacked, one warm bulb over a steel table, cold grills, the shutter half down, an old red landline phone on the counter.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot with a slow pull-back from the table; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The closed bún chả shop at night glows warm under its single bulb, stacked plastic stools, cold grills and the half-down shutter framing a steel table with a cooling teapot.
- 3.0–7.0s: @Lam sits at the steel table shaking with silent laughter, eyes crinkled and mouth closed, wiping the corner of his eye with a knuckle as @Mai sits down beside him with her laptop.
- 7.0–11.0s: @Mai straightens her round glasses and watches her grandfather, her lips pressed together as a slow closed-mouth smile spreads across her face in the warm light.
- 11.0–15.0s: As the camera pulls back over the glowing little shop, @Lam raises his teacup toward @Mai in a small toast and the single bulb sways gently above the steel table. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Mai nhìn ba người già chụm đầu bên ấm trà nguội, cười rộn ràng như lũ trẻ con, như thể ba mươi năm chưa từng trôi qua, và đêm nay cô biết chắc một điều, phố cổ Hà Nội sắp có một phi vụ để đời." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: warm chuckling from just out of frame, teacups clinking, crickets outside the half-down shutter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 1 (`canh-10/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning outside the marble lobby of a gleaming Hà Nội glass tower: a revolving door, potted palms, polished stone steps reflecting the light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: two security guards in grey uniforms standing straight by the door
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide low-angle shot, slow crane-down from the tower facade to the steps; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The gleaming glass tower rises into a crisp blue morning sky, sunlight flashing across its mirrored windows high above the marble lobby, the revolving door and the potted palms.
- 3.0–7.0s: A black luxury sedan with no badge glides up and stops at the foot of the polished stone steps, while the two security guards at the top snap upright beside the revolving door.
- 7.0–11.0s: The driver's door swings open and @Lam steps out wearing a crisp black chauffeur cap in place of his usual helmet, smoothing his grey windbreaker with one hand.
- 11.0–15.0s: @Lam marches stiffly around the gleaming hood and opens the rear door with a deep, precise bow, lips pressed into a straight line, the two guards frozen at attention above him. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Sáng thứ Hai, một chiếc xe sang màu đen đỗ xịch trước tòa nhà kính, mấy anh bảo vệ vội vàng đứng thẳng, người bước xuống mở cửa xe chính là ông Lâm, chiếc mũ cối quen thuộc đã được thay bằng mũ tài xế." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a smooth engine purring to a stop, tires whispering on stone, a car door clicking open, crisp footsteps, distant city traffic. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 2 (`canh-10/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning outside the marble lobby of a gleaming Hà Nội glass tower: a revolving door, potted palms, polished stone steps reflecting the light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm low-angle close-up at the rear door, slow tilt-up; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The open rear door of the black luxury sedan with no badge frames a slice of cream leather seat, morning sunlight glinting on the polished stone step below it.
- 3.0–7.0s: @BaHoa steps out and rises tall in big black sunglasses and a wide-brimmed black hat, her purple floral silk blouse rippling in the light breeze.
- 7.0–11.0s: The camera tilts up to a large gold flower brooch with a tiny hidden camera shining on her chest, its tiny lens glinting once in the morning sun.
- 11.0–15.0s: @BaHoa lifts her chin, slowly lowers her sunglasses with one finger and gazes up at the tower, red lips closed in a regal half smile. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cửa sau vừa mở, bà Hoa bước ra, kính đen to bản, mũ rộng vành, trâm vàng lấp lánh trước ngực, sang trọng như một bà trùm bất động sản thật, mà chẳng ai biết chiếc trâm ấy đang lặng lẽ ghi hình tất cả." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heeled sandals tapping on stone, a gold bangle clinking, a car door thudding shut, a soft breeze in the palms. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 3 (`canh-10/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning outside the marble lobby of a gleaming Hà Nội glass tower: a revolving door, potted palms, polished stone steps reflecting the light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 40mm medium two-shot, slow lateral track along the steps; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The polished stone steps and potted palms before the revolving door shine in the morning sun, the black luxury sedan with no badge waiting at the curb.
- 3.0–7.0s: @BaHoa, in big black sunglasses and a wide-brimmed black hat, turns to @Lam and wags one finger at the car, speaking in a brassy commanding voice while he listens with lips closed.
- 7.0–11.0s: @BaHoa closes her red lips and lifts her chin, as @Lam bows low in his black chauffeur cap and answers in a low husky murmur, eyes lowered to the stone.
- 11.0–15.0s: @Lam finishes, closes his mouth and hides a tiny closed-lip smile under the cap's brim, while @BaHoa sweeps away toward the revolving door with a crisp sniff, chin high. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.5s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Lái xe đâu, đỗ cho cẩn thận, xước một vết sơn là trừ một năm lương đấy nhé!"
- Turn 2, 8.0–12.9s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Dạ vâng bà chủ, tôi nhớ rồi ạ, mà bà diễn còn hay hơn ba mươi năm trước đấy."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a gold bangle clinking, a soft breeze in the palms, a distant car horn, the revolving door turning. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 4 (`canh-10/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Inside a parked white van turned into a surveillance post by day: two laptops glowing, tangled cables, a thermos, tinted windows facing a busy street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide interior shot, slow dolly-in between the two seats; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Two laptops glow on a fold-down shelf inside the parked white van, tangled cables and a thermos beside them, the busy street blurred beyond the tinted windows.
- 3.0–7.0s: @Mai and @Khoa lean in shoulder to shoulder toward the glowing screens, her round glasses reflecting soft light, his magnifier glasses lowered over his eyes.
- 7.0–11.0s: @Mai presses a small headset to one ear and nods quickly, lips pressed together, as the laptop glow brightens across both of their faces.
- 11.0–15.0s: @Khoa raises a slow thumbs-up without looking away from the screens, and @Mai answers with a tiny closed-lip grin, both perfectly still in the soft blue glow. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cùng lúc ấy, trong chiếc xe tải trắng bên kia đường, Mai và ông Khoa ngồi dán mắt vào hai chiếc máy tính đang sáng đèn, hình và tiếng từ chiếc trâm vàng truyền về rõ mồn một, phi vụ để đời chính thức bắt đầu." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: laptop fans humming, muffled street traffic, a faint crackle in a headset. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 1 (`canh-11/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, slow tracking alongside him; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the glass-walled boss room, a ring light glows beside a white leather sofa while purple and gold neon accent lights shimmer across the glass walls.
- 3.0–7.0s: @Hung lowers a phone on a small selfie gimbal, taps it to end his livestream and tugs the collar of his black satin bomber jacket straight.
- 7.0–11.0s: @Hung checks his ash-blond undercut in the dark glass, smooths one side with his silver-ringed fingers and flashes himself a cocky closed-lip grin.
- 11.0–15.0s: @Hung strides briskly out through the glass door with both arms spread wide in welcome, his closed-lip grin stretching from ear to ear. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Nghe tin có một bà trùm mang mười tỷ đến xin đầu tư, Hưng tắt ngay livestream, chỉnh lại cổ áo, soi lại mái tóc vàng hoe trong vách kính, rồi tươi cười chạy ra tận cửa đón, chẳng khác gì đón thần tài vào nhà." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft chime as the livestream ends, phones ringing across the call center, quick sneaker steps, a glass door swinging. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 2 (`canh-11/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide two-shot across the low tea table, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The white leather sofa in the glass-walled boss room sits empty under the glowing ring light, a tea tray with two glass cups waiting on the low table.
- 3.0–7.0s: @BaHoa settles onto the white sofa in her wide-brimmed black hat and big sunglasses and speaks to @Hung with a lazy wave of her hand, while he listens with lips closed.
- 7.0–11.0s: @BaHoa closes her red lips and leans back, and @Hung, perched on the chair opposite, spreads his silver-ringed hands wide and starts answering eagerly.
- 11.0–15.0s: @Hung holds up ten fingers and sweeps them upward as he finishes, then closes his mouth into a lopsided grin while @BaHoa studies him through her dark lenses. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.0s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Tôi có mười tỷ để không, nghe nói cậu làm tiền đẻ ra tiền nhanh lắm."
- Turn 2, 7.5–13.0s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Bà gửi tôi mười tỷ, ba tháng sau tôi trả bà hai mươi, sinh viên bây giờ dễ vay lắm bà ạ."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft creak of leather, distant phones ringing, a glass cup clinking on the tray. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 3 (`canh-11/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, slow arc around the sofa; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @BaHoa slowly lowers her sunglasses an inch and arches one eyebrow at @Hung, red lips still closed, the large gold flower brooch with a tiny hidden camera glinting on her chest.
- 3.0–7.0s: @BaHoa speaks to @Hung in a teasing brassy voice, tapping her chunky gold bangle on the sofa arm, while he listens with a closed-lip smirk.
- 7.0–11.0s: @BaHoa closes her lips and tilts her head, and @Hung answers with a careless shrug, lifting a phone on a small selfie gimbal and waggling it beside his face.
- 11.0–15.0s: @Hung taps the phone's blank glowing screen with a ringed finger as he finishes, closes his mouth and leans back with arms folded, as @BaHoa nods slowly. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Dễ vay thì cũng phải trả chứ, nhỡ chúng nó không trả thì cậu làm thế nào?"
- Turn 2, 7.8–13.1s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Không trả thì tôi gửi ảnh cho cả họ hàng nó, xấu hổ quá thì kiểu gì nó cũng phải trả."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a gold bangle tapping on leather, a phone buzzing, the ring light humming, distant keyboards clicking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 4 (`canh-11/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 100mm close-up, slow push-in to the brooch; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Purple and gold neon light ripples across the glass wall of the boss room, the glowing ring light and the white leather sofa softly out of focus.
- 3.0–7.0s: @BaHoa nods slowly under her wide-brimmed black hat, eyes hidden behind her big black sunglasses, red lips closed in a patient curve.
- 7.0–11.0s: @BaHoa's fingertips stroke the large gold flower brooch with a tiny hidden camera on her chest, her chunky gold bangle sliding down her wrist.
- 11.0–15.0s: The camera settles on the gold brooch as the tiny lens at its center glints once, @BaHoa's red lips closed in a slow curved smile just above it. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Sau cặp kính đen, bà Hoa gật gù như người đã hiểu ra, ngón tay khẽ vuốt chiếc trâm vàng trước ngực, mà Hưng đâu có biết, từng lời khoe khoang của hắn đang chạy thẳng về máy tính của Mai ở bên kia đường." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint electronic click, the soft ring light hum, muffled chatter of the call center. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 1 (`canh-12/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A cold server room in the glass tower: tall black server racks with blinking blue lights, cable trays, a humming air conditioner, a glass door with a keypad lock.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide shot, slow side-tracking along the hallway; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A long bright corporate hallway with grey carpet and frosted glass walls stretches away, ceiling lights glowing and a potted plant standing by a corner.
- 3.0–7.0s: @Khoa ambles into view in a blue technician cap over his grey ponytail, carrying a toolbox, his brown multi-pocket vest bristling with little tools.
- 7.0–11.0s: @Khoa strolls on with a loose, bored gait, swinging the toolbox like any ordinary repairman on his rounds, lips pressed together, eyes half closed.
- 11.0–15.0s: @Khoa stops beside a frosted glass wall, draws a bent hairpin from his vest pocket and holds it up to the light with a dry closed-lip smirk. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cùng lúc ấy, ông Khoa trong bộ đồ thợ sửa điều hòa lững thững đi dọc hành lang, chẳng ai buồn để ý, ổ khóa điện tử của phòng máy chủ, ông chỉ cần ba giây và một chiếc kẹp tóc bẻ cong là xong." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft footsteps on carpet, the hum of ceiling lights, a distant elevator chime. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 2 (`canh-12/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A cold server room in the glass tower: tall black server racks with blinking blue lights, cable trays, a humming air conditioner, a glass door with a keypad lock.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, slow push-in toward the keypad door; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A glass door with a keypad lock of blank buttons glows with a small red light, tall black server racks blinking blue behind the glass.
- 3.0–7.0s: @Khoa kneels by the keypad lock, slides a bent hairpin into a tiny slot beneath it and twists it gently, muttering to himself with a dry smirk.
- 7.0–11.0s: The small red light flips to green with a click and the glass door eases open, as @Khoa keeps muttering and wiggles his steady fingers in the air.
- 11.0–15.0s: @Khoa finishes and closes his mouth, tucks the hairpin into his vest pocket, pats it twice and steps through into the cold blue glow of the server racks. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.8s, spoken on camera by @Khoa (man of 60, strictly standard Hà Nội Northern accent (never Southern accent), nasal wry tenor, deadpan and fussy, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Đấy, khóa điện tử gì mà ba giây đã mở, ba mươi năm rồi mà tay tôi vẫn chưa run tí nào, cái khóa này còn dễ hơn mấy cái két sắt ngày xưa nhiều." (no subtitles)
- From 3.0s onward, @Khoa's face and lips stay clearly visible while speaking; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint metallic scratch, a crisp electronic beep, the hiss of a door seal releasing, the loud hum of the air conditioner. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 3 (`canh-12/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A cold server room in the glass tower: tall black server racks with blinking blue lights, cable trays, a humming air conditioner, a glass door with a keypad lock.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on his hands, slow tilt-up to his face; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Khoa crouches before a tall black server rack and lowers his magnifier glasses over his eyes, the blinking blue lights reflecting in the thick lenses, lips pressed together.
- 3.0–7.0s: @Khoa's long thin fingers slide a small black hard drive into a port on the rack with a soft click, holding it steady for a moment.
- 7.0–11.0s: A row of tiny blue lights on the drive starts blinking faster and faster as the camera tilts up from his hands toward his face.
- 11.0–15.0s: @Khoa sits back on his heels with lips pressed shut, raising his eyebrows above the magnifier lenses as the lights race across the drive. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngồi xổm trước dãy máy chủ, ông Khoa cắm chiếc ổ cứng nhỏ màu đen vào giá máy, những ngọn đèn xanh nhấp nháy liên hồi, và toàn bộ dữ liệu đòi nợ của công ty Phú Quý bắt đầu lặng lẽ chảy về chiếc xe tải trắng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft plastic click, cooling fans rising in pitch, rapid electronic chirps. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 4 (`canh-12/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Inside a parked white van turned into a surveillance post by day: two laptops glowing, tangled cables, a thermos, tinted windows facing a busy street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, slow push-in across the laptops; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Two laptops glow brightly inside the parked white van, tangled cables and a thermos on the narrow shelf, the tinted windows dimming the busy street outside.
- 3.0–7.0s: @Mai leans toward the glowing laptops with a small headset microphone at her cheek and speaks quickly, eyes wide behind her round black-framed glasses.
- 7.0–11.0s: @Mai keeps speaking more softly as her voice catches, her eyes glistening behind the glasses and one hand pressed flat on the shelf.
- 11.0–15.0s: @Mai finishes and closes her mouth, a single tear sliding down her cheek in the laptop glow, then a small closed-lip smile lifts her face. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.8s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông Khoa ơi, dữ liệu về đủ cả rồi, cả danh sách mấy nghìn sinh viên bị nó siết nợ, thế mà ba tháng nay cháu cứ tưởng chỉ có một mình cháu khổ thôi." (no subtitles)
- From 3.0s onward, @Mai's face and lips stay clearly visible while speaking; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: laptop fans whirring, rapid keyboard taps, a quiet exhale, muffled street traffic. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 1 (`canh-13/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot, slow push-in toward the pillar; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Fluorescent strip lights flicker over rows of concrete pillars in the dim underground car park, the black luxury sedan with no badge parked in a far bay.
- 3.0–7.0s: @Beo peeks out from behind a thick concrete pillar, the lightning-bolt pattern on his shaved head catching the light as his small eyes squint toward the sedan.
- 7.0–11.0s: @Beo's small eyes go wide and his jaw tightens with lips pressed shut, and he leans a little further out past the pillar for a better look.
- 11.0–15.0s: @Beo slips back behind the pillar, presses his broad back flat to the concrete and slowly pulls out his phone, lips still shut tight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Nhưng dưới hầm xe, Béo vô tình thấy gã tài xế già xắn tay áo lau xe, để lộ trên cẳng tay hình con rồng xanh sẫm, một hình xăm mà dân giang hồ phố cổ ba mươi năm trước không ai là không biết." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: fluorescent lights buzzing, a distant car door closing, echoing water drips. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 2 (`canh-13/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 40mm medium two-shot by the glass desk, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The glass-walled boss room glows with purple and gold neon, the ring light and white leather sofa standing before rows of glowing desks beyond the glass.
- 3.0–7.0s: @Beo leans in toward @Hung and speaks in a rough low voice, tapping his own thick right forearm with two fingers, while @Hung listens with lips closed.
- 7.0–11.0s: @Beo closes his mouth and raises his eyebrows, as @Hung slowly lowers a phone on a small selfie gimbal and answers with a short mocking laugh in his voice.
- 11.0–15.0s: @Hung flicks a ringed hand dismissively toward the window as he finishes, then closes his mouth and narrows his eyes behind his round gold-rimmed glasses. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Beo (man of 28, strictly standard Hà Nội Northern accent (never Southern accent), rough loud bass, blustering, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Đại ca, lão tài xế của bà kia có hình xăm con rồng xanh, thằng em thấy quen lắm."
- Turn 2, 8.3–13.3s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Lâm Rồng à? Bố tao kể về lão suốt, hóa ra giờ đi lái xe thuê cho một bà già."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the ring light humming, a muffled phone ringing, a chair creaking, a short mocking laugh. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 3 (`canh-13/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot through the glass wall, slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Rows of glowing desks stretch across the call center beyond the glass wall of the boss room, purple and gold neon reflecting on the empty white leather sofa.
- 3.0–7.0s: @Hung stands alone at his glass desk, opens a glossy folder of papers with faint unreadable lines and runs a ringed finger slowly down the page.
- 7.0–11.0s: @Hung pauses on the last page, taps it twice and looks up through the glass with a slow closed-lip smile spreading under his round gold-rimmed glasses.
- 11.0–15.0s: @Hung snaps the folder shut and sets a fountain pen neatly across it like a winning chess move, lips closed in a crooked grin. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Nghe xong, Hưng không hề nổi giận, hắn chỉ khẽ mỉm cười, lật tập hợp đồng đầu tư ra xem lại, rồi quyết định chơi lại bộ ba già bằng chính luật chơi của họ, gài bẫy ngược chính những kẻ đang giăng lưới quanh mình." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper rustling, a folder snapping shut, a pen clicking on the folder, the soft hum of neon. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 4 (`canh-13/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 40mm medium two-shot by the tall window, slow lateral track; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Sunlight pours through the tall windows of the call center high in the glass tower, the busy street far below dotted with tiny traffic and a small white van.
- 3.0–7.0s: @Hung taps the closed folder against his palm and speaks to @Beo in a slick low voice, eyes glinting, while @Beo listens with his thick arms folded.
- 7.0–11.0s: @Hung closes his mouth into a lopsided grin, and @Beo steps to the window, points one thick finger down at the tiny white van and answers in a rough bass.
- 11.0–15.0s: @Beo finishes and closes his mouth, nods once and rolls his thick shoulders, then turns and strides off between the rows of glowing desks. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Cứ để bà ta ký hợp đồng, rồi tao báo công an bắt cả lũ về tội lừa đảo."
- Turn 2, 8.3–13.6s, spoken on camera by @Beo (man of 28, strictly standard Hà Nội Northern accent (never Southern accent), rough loud bass, blustering, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Rõ đại ca, cái xe tải trắng đỗ bên kia đường từ sáng, thằng em dẫn anh em xuống xem ngay."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heavy flip-flop steps, distant ringing phones, a glass door swinging. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 1 (`canh-14/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Inside a parked white van turned into a surveillance post by day: two laptops glowing, tangled cables, a thermos, tinted windows facing a busy street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide interior shot, slow dolly-in toward the side door; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Two laptops glow inside the parked white van, a small black hard drive plugged into one by a short cable, tangled cables and a thermos on the shelf.
- 3.0–7.0s: @Mai unplugs the small black hard drive and hugs it to her chest as the side door of the van slides open, flooding the cabin with noon light.
- 7.0–11.0s: @Beo stands blocking the open doorway with his arms folded across his big chest, lips pressed into a flat line, the sunny street bright behind him.
- 11.0–15.0s: @Mai slides open the far-side door behind her and slips out into the daylight in one quick move, leaving @Beo staring at the empty seat with lips shut. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Mai vừa rút ổ cứng khỏi máy tính thì cửa xe tải trượt mở, Béo đã khoanh tay đứng chắn ngay bên ngoài từ lúc nào, nhưng cô gái nhỏ nhanh tay ôm chặt ổ cứng, lặng lẽ lách ra bằng cánh cửa bên kia." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a cable clicking free, the van door sliding open with a rattle, street horns pouring in, a second door rolling open. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 2 (`canh-14/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Noon on a busy old-quarter street near the railway: honking motorbikes, street vendors, shop awnings, a white van parked at the curb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, fast handheld tracking alongside her; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Shop awnings, street vendors' carts and tangled wires line the sunny old-quarter street, the white van parked at the curb and honking traffic blurred on the far lane.
- 3.0–7.0s: @Mai runs at full speed along the pavement under the shop awnings, clutching a small black hard drive against her lavender hoodie, her backpack bouncing.
- 7.0–11.0s: @Lam rides the old cream-colored step-through motorbike with a round chrome headlamp smoothly out of the far lane of traffic in his battered green pith helmet, beeping the horn twice.
- 11.0–15.0s: @Lam brakes to a neat stop at the curb a few steps ahead of @Mai, one sandal on the ground, lips closed in a calm half smile as she runs up. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cô ôm ổ cứng chạy thục mạng dọc những mái hiên phố cổ, thì một tiếng còi quen thuộc vang lên, ông Lâm phóng chiếc xe máy cũ luồn lách qua dòng xe như cá lượn, rồi phanh xịch bên lề đường chờ cháu gái." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: quick sneaker footsteps, a chorus of honking horns, a cheerful little horn beeping twice, brakes squeaking softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 3 (`canh-14/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Noon on a busy old-quarter street near the railway: honking motorbikes, street vendors, shop awnings, a white van parked at the curb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 40mm close-up two-shot over the chrome headlamp, slow pull-back; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Mai reaches the idling motorbike out of breath and stops beside the seat, hugging the small black hard drive, lips closed, as @Lam glances back at her.
- 3.0–7.0s: @Mai speaks quickly to @Lam, glancing back over her shoulder down the street, while he listens with lips closed and both hands on the handlebars.
- 7.0–11.0s: @Mai closes her mouth, and @Lam pats the seat behind him and answers firmly with a sly glint in his eye, as she swings onto the back seat.
- 11.0–15.0s: @Lam finishes and closes his mouth, then twists the throttle as @Mai wraps both arms around his waist, and the old bike pulls away from the curb. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.5s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Ông ơi, cháu lấy được ổ cứng rồi, mà bọn nó đang đuổi ngay sau lưng kìa ông!"
- Turn 2, 8.0–12.9s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Lên xe ôm chặt vào, Mai, hôm nay ông cho con biết thế nào là chạy xe phố cổ!"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a puttering engine revving, traffic horns, a street vendor calling in the distance. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 4 (`canh-14/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Noon on a busy old-quarter street near the railway: honking motorbikes, street vendors, shop awnings, a white van parked at the curb.

[CHARACTERS]
- Extra: four debt collectors on black motorbikes weaving through traffic in pursuit
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 20mm aerial drone shot, slow forward glide above the narrow streets; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: From high above, the narrow old-quarter streets twist like a maze between tiled roofs, tangled wires and shop awnings, glittering under the noon sun.
- 3.0–7.0s: Four debt collectors on black motorbikes weave through the traffic in a tight line down the middle of the road, revving as they slip past slower motorbikes.
- 7.0–11.0s: The four black motorbikes lean into a sharp turn one after another into an even narrower street hung with laundry, keeping to the center of the lane.
- 11.0–15.0s: Far ahead at the end of the street, a pair of shining railway tracks cuts between the old tube houses, gleaming in the sun as a long train horn echoes. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bốn chiếc xe máy đen lập tức bám đuổi, rú ga len lỏi giữa những con phố chật như ruột gà, nhưng chiếc xe cũ của ông Lâm đã ngoặt thẳng vào phố đường tàu, đúng lúc tiếng còi tàu hỏa rền vang từ phía xa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: engines revving and whining, a chorus of horns, a long distant train horn, echoes bouncing between the houses. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 1 (`canh-15/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Hà Nội's narrow train street at noon: railway tracks running between rows of old tube houses, tiny cafés with low stools pulled back from the rails, laundry and potted plants along the walls.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide low-angle shot along the rails, slow dolly-back; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Low between the shining rails, the narrow train street stretches away under the noon sun, café stools pulled back tight against the walls, a tiny train headlamp glowing very far away.
- 3.0–7.0s: @Lam rides the old cream-colored step-through motorbike with a round chrome headlamp out of a side street with @Mai holding on behind him, the train still only a tiny light far down the track.
- 7.0–11.0s: The bike crosses the empty rails briskly from left to right, tires bumping over the steel, while the distant headlamp stays small at the far end of the street.
- 11.0–15.0s: The bike rolls over the far rail and vanishes into a narrow alley, @Lam's battered green pith helmet bobbing out of sight, the rails left empty and humming. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trên phố đường tàu, các quán cà phê vội vàng kéo ghế vào, khi đoàn tàu vẫn còn ở rất xa, chiếc xe máy cũ của ông Lâm băng qua đường ray nhanh như một cơn gió, rồi mất hút vào ngõ nhỏ bên kia." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rails humming and ticking, coffee cups rattling on saucers, tires thumping over steel rails, a long distant train horn. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 2 (`canh-15/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Hà Nội's narrow train street at noon: railway tracks running between rows of old tube houses, tiny cafés with low stools pulled back from the rails, laundry and potted plants along the walls.

[CHARACTERS]
- Extra: four debt collectors on motorbikes stopped well back from the rails
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 35mm medium shot from the café side, slow lateral drift; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: A long blue and white train rumbles through the narrow street between the old tube houses, its carriages filling the frame and the laundry on the walls fluttering in its wind.
- 3.0–7.0s: Through the gaps between the passing carriages, four debt collectors on motorbikes wait stopped well back from the rails beside the café stools, engines idling.
- 7.0–11.0s: The last carriage rolls away down the street, and the far side of the tracks stands empty, only an alley mouth and a potted plant in the sun.
- 11.0–15.0s: The four debt collectors sit frozen on their motorbikes, turning their heads to one another with mouths shut and shoulders slumped, the empty rails gleaming in front of them. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đoàn tàu rầm rập chạy qua, bốn chiếc xe đuổi theo đành phanh gấp, kẹt cứng ở bên này đường ray, đến khi toa cuối cùng đi khuất, bên kia đã chẳng còn bóng ai, bốn gã đòi nợ chỉ còn biết ngơ ngác nhìn nhau." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a train rumbling and clattering past, its horn blaring, idling engines sputtering, then quiet rails ticking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 3 (`canh-15/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A narrow winding old-quarter alley maze at noon, laundry overhead, tiny doorways, potted plants.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm close-up two-shot from the front of the bike, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A narrow winding alley in the old quarter glows in noon light, laundry hanging overhead between tiny doorways and potted plants along the walls.
- 3.0–7.0s: @Lam rolls the old cream-colored step-through motorbike with a round chrome headlamp to a stop, and @Mai on the back seat speaks breathlessly, one hand pressed to her chest, while he listens with lips closed.
- 7.0–11.0s: @Mai closes her mouth and puffs out a breath, and @Lam turns his head toward her and answers with a dry chuckle in his voice, tapping the brim of his battered green pith helmet.
- 11.0–15.0s: @Lam flicks his hand back toward the railway as he finishes and closes his mouth into a crooked closed-lip grin, while @Mai shakes her head with a wide closed-lip smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.5s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Ông ơi, ông lái xe còn ghê hơn cả trong phim hành động, cháu suýt rơi cả tim!"
- Turn 2, 8.0–12.9s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Ba mươi năm trước cả phố này đuổi ông còn không kịp, mấy thằng nhóc ấy ăn thua gì."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the engine ticking down, a distant train fading away, a caged bird chirping, laundry flapping softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 4 (`canh-15/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A narrow winding old-quarter alley maze at noon, laundry overhead, tiny doorways, potted plants.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot, slow crane-up above the alley; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The winding old-quarter alley lies quiet in the noon sun, laundry stirring overhead and a cat dozing on a doorstep among potted plants.
- 3.0–7.0s: @Lam leans back on the seat of the old cream-colored step-through motorbike with a round chrome headlamp and laughs silently, shoulders shaking, lips closed.
- 7.0–11.0s: The camera rises past the laundry lines and tangled wires as @Lam shrinks below, tipping his battered green pith helmet back with one finger.
- 11.0–15.0s: Above the sea of tiled roofs, a gleaming glass tower appears far off on the sunny skyline, its mirrored windows flashing while @Lam's tiny figure sits still far below. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm bật cười sảng khoái giữa con ngõ vắng, nhưng ông không hề biết, trong lúc hai ông cháu mải chạy, thì ở một nơi khác, Hưng đã lặng lẽ ra tay, nhanh hơn và hiểm hơn những gì ông có thể ngờ tới." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pigeons fluttering off a roof, wind chimes tinkling, distant traffic. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 1 (`canh-16/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- Extra: two police officers in green uniforms walking calmly into the shop
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot, slow dolly-back through the smoke; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Charcoal grills smoke on the pavement in front of the bún chả shop, low plastic stools and steel tables empty after lunch, baskets of fresh herbs glowing in warm sunlight.
- 3.0–7.0s: Two police officers in green uniforms walk calmly into the shop through the drifting smoke, one holding a slim folder of papers with faint unreadable lines.
- 7.0–11.0s: @BaHoa looks up from the grill without a flicker, wipes her hands and unties her red apron with unhurried calm, lips closed in a cool half smile.
- 11.0–15.0s: @BaHoa folds the red apron neatly and lays it on the steel table beside a basket of herbs, as the two officers wait politely by the door with relaxed shoulders. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Chiều hôm ấy, hai cán bộ công an bước vào quán bún chả, trên tay là lá đơn tố cáo lừa đảo của Hưng, bà Hoa không chạy, cũng chẳng cãi nửa lời, chỉ thong thả tháo chiếc tạp dề đỏ, gấp lại gọn gàng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal crackling, pork sizzling, calm footsteps, fabric rustling, a distant street vendor calling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 2 (`canh-16/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- Extra: two police officers in green uniforms waiting calmly by the door
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow pan with her to the grill; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @BaHoa straightens up beside the steel table and raises one palm toward the two officers by the door, red lips still closed, the folded apron under her other hand.
- 3.0–7.0s: @BaHoa speaks in a breezy brassy voice, unhurried, as if chatting with regular customers, turning to the grill and sliding its little vent shut.
- 7.0–11.0s: @BaHoa keeps speaking as she moves the last skewers of pork onto a plate, then lifts her wide-brimmed black hat from a hook on the wall.
- 11.0–15.0s: @BaHoa finishes and closes her mouth, settles the hat on her burgundy curls and strolls out toward the street on her own, chin high, the two officers following at a polite distance. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.5s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Các chú cứ từ từ, để tôi tắt bếp than đã, kẻo cháy hết mẻ chả của khách, rồi tôi đội cái mũ vào, tôi tự đi với các chú cho đàng hoàng, có gì đâu mà vội." (no subtitles)
- @BaHoa keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a metal vent scraping shut, coals hissing, a plate clinking, sandals tapping on the pavement. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 3 (`canh-16/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tiny electronics repair stall tucked under a staircase in an old-quarter alley: shelves of old radios and phones, tangled wires, a soldering iron, a magnifier lamp, a single bare bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot, slow dolly-in under the staircase; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The tiny repair stall under the staircase lies ransacked, drawers hanging open, old radios knocked askew, a clean dust-free rectangle on the workbench where something used to sit.
- 3.0–7.0s: @Khoa steps in under the single bare bulb and stops short, his magnifier glasses on his forehead, staring at the empty rectangle on the workbench.
- 7.0–11.0s: @Khoa stands motionless for a long moment, lips pressed into a thin line, his long fingers resting on the edge of the bare workbench.
- 11.0–15.0s: @Khoa's eyes flick for a split second to an old wooden Soviet-era radio still untouched on the top shelf, and one corner of his closed mouth twitches. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cũng chiều hôm ấy, sạp sửa đài của ông Khoa bị ai đó lục tung, chiếc ổ cứng đen trên bàn đã không cánh mà bay, ông Khoa đứng lặng hồi lâu, chẳng nói chẳng rằng, chỉ khẽ đưa mắt liếc lên chiếc kệ trên cao." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a bare bulb buzzing, a loose wire ticking against a shelf, distant alley chatter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 4 (`canh-16/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning inside Lâm's narrow old-quarter tube house: a ground-floor room with the rolling steel shutter raised, a worn wooden table, a small family altar, sunlight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, slow crane-down to the doorstep; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A phone lies face-up on the worn wooden table in the sunlit room, its blank screen lighting up again and again as it buzzes in a slow circle across the wood.
- 3.0–7.0s: @Mai picks up the buzzing phone, its blank glowing screen lighting her face, and her thumb freezes above it as it keeps vibrating in her hand.
- 7.0–11.0s: @Mai walks to the open doorway and sinks down onto the front step, where faded red paint still stains the edge of the raised steel shutter.
- 11.0–15.0s: @Mai sets the phone face-down beside her and covers her face with both hands, shoulders shaking without a sound in the warm street sunlight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Còn ở nhà, điện thoại của Mai cứ sáng lên liên tục, bọn chúng đã gửi ảnh cô cho cả lớp kèm hai chữ con nợ, Mai ngồi sụp xuống bậc cửa vẫn còn vệt sơn đỏ hôm nào, ôm mặt khóc không thành tiếng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone vibrating nonstop against wood, notification pings stacking up, muffled motorbikes passing, a soft shaky breath. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 1 (`canh-17/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tube-house rooftop in the old quarter at night: potted plants, a steel water tank, a sea of tiled roofs and warm city lights, a lake glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide shot from behind, slow crane-up; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A tube-house rooftop glows under warm city lights at night, potted plants and a steel water tank beside two low plastic stools, the lake shimmering far away.
- 3.0–7.0s: @Lam and @Mai sit side by side on the low stools facing the glittering old quarter, his battered green pith helmet resting on his knee, her hands tucked into her hoodie sleeves.
- 7.0–11.0s: Neither of them moves, both with lips closed, as a soft breeze stirs the potted leaves and @Mai pulls her knees up to her chest.
- 11.0–15.0s: The camera rises over their two small backs and the sea of tiled roofs toward the distant lake glowing in the dark, city lights twinkling all around. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đêm ấy, hai ông cháu ngồi lặng trên sân thượng, nhìn xuống phố cổ lấp lánh ánh đèn mà chẳng ai nói với ai câu nào, chỉ có tiếng gió đêm lành lạnh và tiếng còi xe vọng lên từ những con phố xa phía dưới." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft night breeze, distant motorbike horns, a dog barking far off, wind chimes. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 2 (`canh-17/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tube-house rooftop in the old quarter at night: potted plants, a steel water tank, a sea of tiled roofs and warm city lights, a lake glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, slow arc to their faces; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Mai turns her head toward @Lam in the warm city glow, her round glasses reflecting the lights, fingers twisting her hoodie sleeves, lips still closed.
- 3.0–7.0s: @Mai speaks to @Lam in a small cracked voice, her eyes glistening as she leans her shoulder against his arm, while he listens with lips closed.
- 7.0–11.0s: @Mai falls silent and lowers her head, and @Lam shakes his head gently and answers in a calm husky voice, his cloudy left eye catching the city lights.
- 11.0–15.0s: @Lam keeps speaking as he rests a warm hand on @Mai's head, then closes his mouth and gazes out over the glittering rooftops with a firm, quiet jaw. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Tại cháu mà bà Hoa bị bắt, ông ơi, hay mình trả tiền cho nó rồi thôi đi ông."
- Turn 2, 8.3–14.0s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Không được con ạ, ông trả nó một đồng, thì ngày mai nó lại gài thêm trăm đứa khác khổ như con."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the night breeze, faint traffic below, crickets, a distant boat horn on the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 3 (`canh-17/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tube-house rooftop in the old quarter at night: potted plants, a steel water tank, a sea of tiled roofs and warm city lights, a lake glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm close-up two-shot of both faces in profile, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Mai lifts her phone, its screen glowing blank, sniffs once and taps its edge with one finger, lips closed, as @Lam's hand slides back to his knee.
- 3.0–7.0s: @Mai speaks quickly to @Lam with a wry twist of her lips, holding the phone up high in a showy livestreamer pose, while he listens with lips closed.
- 7.0–11.0s: @Mai lowers the phone and closes her mouth, and @Lam freezes, his thick grey eyebrows rising, then turns to her and speaks low and steady with a sly glint.
- 11.0–15.0s: @Lam taps his own lips with one finger and points out at the city as he finishes, then closes his mouth, while @Mai breaks into a slow closed-lip grin. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Ông ơi, Hưng livestream mỗi tối, có hai triệu người xem, nó thích khoe khoang hơn cả thích tiền."
- Turn 2, 8.3–12.7s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Thế thì mình để chính cái miệng nó tự khai, trước mặt hai triệu người, con ạ."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone buzzing faintly, the night breeze, wind chimes tinkling, distant horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 4 (`canh-17/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tube-house rooftop in the old quarter at night: potted plants, a steel water tank, a sea of tiled roofs and warm city lights, a lake glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow push-in to an extreme close-up of his eyes; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The steel water tank and potted plants on the rooftop glint under warm city light, the glowing lake shimmering beyond the sea of tiled roofs.
- 3.0–7.0s: @Lam sits on his low stool in profile, and his shoulders begin to shake with a silent closed-mouth laugh, his thick grey eyebrows lifting.
- 7.0–11.0s: The camera glides closer to @Lam's weathered face as the laugh fades into a calm, sly closed-lip grin and his narrow eyes fix on the distant glass towers.
- 11.0–15.0s: @Lam's narrow eyes, even the cloudy left one, light up with a sharp sparkle reflecting the city lights, still and steady like a dragon waking. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Nói xong câu ấy, ông Lâm bật cười khẽ, đôi mắt mờ đục của ông bỗng sáng rực lên như ba mươi năm trước, và Mai hiểu rằng, con rồng già của phố cổ vừa nghĩ ra nước cờ cuối cùng để lật ngược ván bài." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft breathy laugh through the nose, wind chimes tinkling, a far-off train horn. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 1 (`canh-18/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning at the front gate of a ward police station on a leafy street: mustard-yellow walls, an open iron gate, a tall tree, parked motorbikes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot, slow dolly-back from the gate; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Morning sunlight filters through a tall tree onto the mustard-yellow walls of the ward police station, the iron gate standing open and motorbikes parked along the curb.
- 3.0–7.0s: @BaHoa strolls out through the open gate in her wide-brimmed black hat and purple floral blouse, her red lipstick bright and perfect.
- 7.0–11.0s: @BaHoa stops on the pavement, stretches both arms lazily toward the sky and rolls her shoulders, gold hoop earrings swinging, lips closed.
- 11.0–15.0s: @BaHoa fans her face with one hand and tilts her chin up to the morning sun, lips closed in a broad smile, as if just back from a seaside holiday. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Sáng hôm sau, cánh cổng đồn công an phường mở ra, bà Hoa thong thả bước ra, son môi vẫn đỏ chót, tóc vẫn bồng bềnh, như vừa đi nghỉ mát ở biển về, chứ chẳng phải vừa ngồi trong đồn suốt cả một đêm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birds chirping in the tree, an iron gate creaking, morning street traffic. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 2 (`canh-18/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning at the front gate of a ward police station on a leafy street: mustard-yellow walls, an open iron gate, a tall tree, parked motorbikes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The old cream-colored step-through motorbike with a round chrome headlamp stands parked under the tall tree outside the mustard-yellow police station wall, leaves dappling its seat.
- 3.0–7.0s: @BaHoa walks up to @Lam waiting beside the motorbike and speaks with a brassy laugh in her voice, flicking her fingers open to show empty palms, while he listens with lips closed.
- 7.0–11.0s: @BaHoa closes her red lips with a crisp sniff, and @Lam, in his battered green pith helmet, shakes his head and answers with a dry husky chuckle.
- 11.0–15.0s: @Lam finishes and closes his mouth into a quiet closed-lip grin, while @BaHoa pats her permed curls and lifts her chin even higher. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Tôi chỉ nói chuyện đầu tư, có cầm của ai đồng nào đâu mà giữ được tôi hả ông!"
- Turn 2, 8.3–12.2s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Ba mươi năm rồi mà cái miệng bà vẫn sắc hơn cả luật sư đấy."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birds chirping, leaves rustling, a passing motorbike. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 3 (`canh-18/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning at the front gate of a ward police station on a leafy street: mustard-yellow walls, an open iron gate, a tall tree, parked motorbikes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide two-shot beside the parked motorbikes, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Parked motorbikes line the leafy street beside the open iron gate, sunlight dappling the mustard-yellow wall through the leaves of the tall tree.
- 3.0–7.0s: @Khoa, with an old wooden Soviet-era radio tucked under one arm, leans toward @Lam and speaks in a dry deadpan voice, wagging one finger, while @Lam listens with lips closed.
- 7.0–11.0s: @Khoa closes his mouth and adjusts the magnifier glasses on his forehead, and @Lam squints at him and answers with a suspicious smile, tilting his head toward the radio.
- 11.0–15.0s: @Lam points one finger at the wooden radio as he finishes, then closes his mouth and folds his arms, as @Khoa hugs the radio a little tighter against his ribs. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Khoa (man of 60, strictly standard Hà Nội Northern accent (never Southern accent), nasal wry tenor, deadpan and fussy, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Cái ổ cứng thằng Béo lấy chỉ là ổ giả, trong đó toàn băng cải lương của tôi thôi."
- Turn 2, 8.3–13.2s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Thế ổ thật ông giấu ở đâu? Đừng bảo là ông lại nhét vào cái đài Liên Xô nhé."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: tree leaves rustling, a distant scooter horn, sparrows chirping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 4 (`canh-18/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning at the front gate of a ward police station on a leafy street: mustard-yellow walls, an open iron gate, a tall tree, parked motorbikes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm close-up two-shot, slow lateral drift from his face to hers; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The tall tree sways over the open iron gate of the police station, sunlight sparkling through its leaves onto the mustard-yellow wall and the parked motorbikes.
- 3.0–7.0s: @Khoa gives a slow exaggerated wink, lips pressed shut, and pats the old wooden Soviet-era radio under his arm twice, its woven speaker cloth catching the light.
- 7.0–11.0s: Beside him, @BaHoa narrows her sharp eyes under her wide-brimmed black hat and curls her red lips into a sly closed smile, gold hoop earrings swinging.
- 11.0–15.0s: @BaHoa flicks open a woven bamboo hand fan with a snap and fans herself slowly, both of them gazing toward the distant glass towers with closed-lip grins. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Khoa nháy mắt một cái, vỗ nhẹ chiếc đài gỗ cũ kẹp dưới nách, bên trong là toàn bộ bằng chứng thật, bà Hoa nheo mắt cười, lần này, đến lượt thằng Hưng bị bộ ba già dắt mũi mà không hề hay biết." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: two hollow knocks on wood, a fan snapping open, birds chirping, rustling leaves. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 1 (`canh-19/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm deep-focus wide shot slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The glass-walled boss room at night, a dark ring light beside a white leather sofa, and beyond the glass a long aisle of glowing monitors ending at closed steel elevator doors, no person in frame.
- 3.0–7.0s: @Hung strides in on screen-right, clicks the ring light into a bright white circle and lifts a phone on a small selfie gimbal to arm's length, lips pressed into a cocky closed-mouth grin.
- 7.0–11.0s: Deep in the background beyond the glass, the elevator doors slide open and @Lam steps out alone on screen-left, battered green pith helmet on, both hands empty at his sides, lips closed.
- 11.0–15.0s: @Lam walks slowly up the aisle toward the boss room between the glowing monitors, while @Hung in the foreground freezes mid-pose and glances back over his shoulder with his mouth shut. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Tám giờ tối, như thường lệ, Hưng bật đèn livestream, hai triệu người đang chờ ông chủ Phú Quý lên sóng khoe tiền, thì đúng lúc ấy cửa thang máy mở, ông Lâm chậm rãi bước ra, mũ cối trên đầu, một mình, tay không." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ring light switch clicking on, soft electronic hum, a few notification chimes, a distant elevator chime, sandals scuffing on carpet. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 2 (`canh-19/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the glass-walled boss room at night, the ring light glowing white beside the white leather sofa, the glass door standing open onto the neon call-center floor, no person in frame.
- 3.0–7.0s: @Lam stands in the open glass doorway on screen-left and speaks in a calm husky voice, face and lips clearly visible, one finger tapping his pith helmet brim, while @Hung listens with closed lips.
- 7.0–11.0s: @Lam closes his mouth and waits without blinking, as @Hung on screen-right swings the gimbal phone toward him and starts talking loudly into it like a livestream salesman, face and lips clearly visible.
- 11.0–15.0s: @Hung finishes with a flourish of his ringed hand toward @Lam and closes his mouth in a smug grin, while @Lam stands perfectly still in the doorway, empty hands relaxed. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.7s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Cậu Hưng, tôi đến trả nợ cho cháu tôi, nhưng cậu phải nhận tiền trước mặt người xem."
- Turn 2, 8.2–13.7s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Cả nhà ơi, ông già xe ôm đến trả nợ này, mọi người xem ông ấy có quỳ xuống xin không nào!"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ring light hum, distant keyboard clicks, a rising flurry of notification chimes, the glass door settling on its hinge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 3 (`canh-19/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot gentle lateral glide; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam ignores the raised gimbal, walks past @Hung to the wide glass desk and pulls out the chrome swivel chair with one hand, lips closed.
- 3.0–7.0s: @Lam sits down unhurried on screen-left, rests his battered green pith helmet on his knee and pours himself a small cup of tea from the teapot on the desk.
- 7.0–11.0s: @Lam crosses one leg over the other and leans back easily with the steaming cup in both hands, a faint knowing smile on closed lips, like an old man at a street tea stall.
- 11.0–15.0s: @Hung stands frozen under the white ring light on screen-right, gimbal still raised and mouth shut, blinking down at the old man who calmly cradles his tea. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm không quỳ, ông kéo ghế ngồi xuống, gác mũ cối lên đùi, tự rót cho mình một chén trà nóng, bình thản như đang ngồi quán trà đá đầu ngõ, còn Hưng thì đứng ngẩn ra trước ống kính, chẳng biết phải nói gì tiếp." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: chair wheels rolling on the floor, leather creaking, tea trickling into a small cup, ring light hum, scattered notification chimes. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 4 (`canh-19/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Inside a parked white van turned into a surveillance post at night: two laptops glowing, tangled cables, a thermos, tinted windows with neon reflections.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium close-up two-shot slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the parked white van at night, two laptops glowing blank on a fold-out desk among tangled cables, a thermos and an old wooden Soviet-era radio with its back panel open, no person in frame.
- 3.0–7.0s: @Mai on screen-left types at lightning speed, her round glasses lit by the blank glowing screens, lips pressed together in concentration.
- 7.0–11.0s: @Khoa on screen-right lifts a small black hard drive out of the opened radio and clicks it into the side of a laptop, his magnifier glasses pulled down over his eyes.
- 11.0–15.0s: @Khoa gives a closed-mouth wink and a thumbs-up, and @Mai hovers one finger above the enter key without pressing it, both faces lit by the glow as neon slides over the tinted windows. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Dưới chân tòa nhà, trong chiếc xe tải trắng, Mai gõ phím như bay, còn ông Khoa đã cắm sẵn ổ cứng thật lấy ra từ bụng chiếc đài Liên Xô cũ, cả hai chỉ còn chờ ông Lâm ra hiệu là bấm nút." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rapid keyboard clatter, a plug clicking into a port, a soft confirmation beep, muffled street traffic outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 1 (`canh-20/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The glass-walled boss room at night, the ring light glowing over a wide glass desk with a steaming teacup beside an empty chrome chair, magenta neon beyond the glass, no person in frame.
- 3.0–7.0s: @Lam sits calmly in the chrome chair on screen-left, pith helmet on his knee, and asks in a husky steady voice, face and lips clearly visible, while @Hung films him with closed lips.
- 7.0–11.0s: @Lam closes his mouth and tilts his head patiently, as @Hung on screen-right leans into the gimbal lens and answers loudly and smugly, face and lips clearly visible in the ring light.
- 11.0–15.0s: @Hung wags three ringed fingers in the air as he finishes, then closes his mouth in a cocky grin, gold-rimmed glasses flashing, while @Lam sits motionless with his hands on his knees. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.7s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Cháu tôi vay năm triệu, ba tháng thành trăm rưỡi, cậu tính lãi bao nhiêu một ngày thế?"
- Turn 2, 8.2–13.5s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Ba phần trăm một ngày, không trả thì tôi gửi ảnh cho cả họ hàng nó, luật nào cấm được tôi?"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ring light hum, distant keyboard clicks, notification chimes multiplying, a leather chair creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 2 (`canh-20/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm low-angle wide shot slow arc; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam sets his teacup down on the glass desk with a soft click and looks up at @Hung, lips closed, as the camera begins to arc around the glowing ring light.
- 3.0–7.0s: @Lam speaks calmly up at @Hung, face and lips clearly visible, one weathered hand gesturing gently toward the glowing gimbal phone, while @Hung listens with closed lips.
- 7.0–11.0s: @Lam closes his mouth and leans back, as @Hung swings the gimbal up to his own face and repeats his boast even louder, face and lips clearly visible, chin raised high.
- 11.0–15.0s: @Hung finishes, closes his mouth and spreads his ringed hands wide for the lens, while @Lam folds his arms on screen-left with a slow closed-mouth smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.4s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Cậu nói to lên một chút nữa, để hai triệu người đang xem cùng nghe cho rõ."
- Turn 2, 7.9–12.9s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Cả nhà nghe rõ chưa, ba phần trăm một ngày, đứa nào không trả là tôi bêu ảnh lên mạng!"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a teacup clicking on glass, ring light hum, a sudden flood of notification chimes, the distant drone of the city. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 3 (`canh-20/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Inside a parked white van turned into a surveillance post at night: two laptops glowing, tangled cables, a thermos, tinted windows with neon reflections.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm extreme close-up slow pull-back; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Extreme close-up of a laptop keyboard inside the parked white van at night, the blank screen's glow pulsing over the keys beside tangled cables and a thermos, no person in frame.
- 3.0–7.0s: @Mai's finger presses the enter key firmly and the blank screen glow flares brighter, flooding her round glasses as the camera pulls back to her face.
- 7.0–11.0s: The two blank laptop screens beside her pulse in alternating bands of white and red light across @Mai's face, her lips pressed into a tight line.
- 11.0–15.0s: @Mai leans back in her seat with a small closed-mouth smile, the laptop light flickering over her lavender hoodie and neon sliding across the tinted window behind her. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đúng lúc ấy, trong xe tải, Mai bấm nút, buổi livestream của Hưng lập tức bị chia đôi, một nửa là gương mặt hắn đang vênh váo khoe lãi, nửa kia là danh sách mấy nghìn nạn nhân thật lấy thẳng từ máy chủ Phú Quý." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a single decisive key click, a rising electronic chime, rapid soft beeps, muffled street traffic. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 4 (`canh-20/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up slow rack focus; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Close on the white ring light and the empty white leather sofa in the boss room at night, the neon of the call center pulsing through the glass wall, no person in frame.
- 3.0–7.0s: @Hung steps into the ring light as the gimbal phone buzzes nonstop in his hand, its blank screen strobing white and red light across his frozen grin and sweating temple.
- 7.0–11.0s: @Hung slowly turns his head toward screen-left, and focus shifts to the foreground, where @Lam sits in the chrome chair raising a small steaming teacup.
- 11.0–15.0s: @Lam sets the cup down on the glass desk with a calm closed-mouth smile, as if nothing at all has happened, while @Hung stands frozen in soft focus behind him. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Điện thoại của Hưng rung liên hồi, bình luận chửi rủa trôi như thác, số người xem vọt lên năm triệu, hắn quay sang thì ông già xe ôm vẫn ngồi yên đó, nhấp một ngụm trà, mỉm cười như chưa hề có chuyện gì." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone buzzing nonstop, a torrent of rapid notification pings, ring light hum, a teacup set gently on glass. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 1 (`canh-21/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
- Extra: young callers pulling off their headsets and walking out between the desks
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 24mm wide shot slow crane-up; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Wide view of the night call center, rows of desks with blank glowing monitors under magenta and gold neon, young callers in headsets sitting stock-still at their screens.
- 3.0–7.0s: One by one the young callers pull off their headsets, lay them on the desks and stand up, picking up their bags with mouths closed.
- 7.0–11.0s: The callers walk out in a quiet line between the desks toward the far elevator, never once looking back at the glass-walled boss room.
- 11.0–15.0s: Rows of empty chairs slowly turn under the glowing monitors as the camera rises over the deserted floor, abandoned headsets glinting in the neon. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trong phòng gọi điện, từng nhân viên một lặng lẽ tháo tai nghe, đứng dậy xách túi bỏ về, những chiếc ghế trống cứ thế xoay tròn, chẳng ai còn muốn dính vào cái công ty sắp sập ấy thêm một phút nào nữa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: headsets clattering softly onto desks, chairs rolling back, quiet footsteps, a distant elevator chime. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 2 (`canh-21/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- Extra: the last few young callers walking away toward the elevator with their bags
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up slow handheld push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The emptying call-center floor at night, abandoned headsets on the desks and chairs left askew under blank glowing monitors, magenta neon pulsing, no person in frame.
- 3.0–7.0s: @Hung bursts out of the glass boss-room door into the aisle and yells after the departing callers, face and lips clearly visible, one ringed hand raised high.
- 7.0–11.0s: @Hung keeps shouting and points at the empty desks, gold-rimmed glasses askew, while far behind him the last young callers step into the elevator without turning around.
- 11.0–15.0s: @Hung closes his mouth and stands panting alone in the empty aisle, satin bomber jacket rumpled, as the steel elevator doors slide shut in the distance. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.0s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ngồi xuống hết! Đứa nào bước ra khỏi cửa là tao trừ hết lương, nghe chưa? Tao trả tiền cho chúng mày để ngồi gọi điện, chứ không phải để đứng dậy bỏ về như thế!" (no subtitles)
- From 3.0s onward, @Hung's face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a glass door swinging open, a lone chair slowly spinning, monitor hum, elevator doors sliding closed. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 3 (`canh-21/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The doorway of the glass-walled boss room at night, the ring light still glowing over the white leather sofa, the long empty aisle stretching back to the elevator, no person in frame.
- 3.0–7.0s: @Beo skids to a stop in the doorway on screen-left, pale and dripping sweat, holds up a glowing phone and blurts out the news, face and lips clearly visible, while @Hung listens.
- 7.0–11.0s: @Beo closes his mouth and wipes his shaved head, as @Hung on screen-right turns sharply toward him and barks orders, face and lips clearly visible, glasses catching the ring light.
- 11.0–15.0s: @Hung finishes, pointing a ringed finger toward the elevator, then closes his mouth and breathes hard, while @Beo nods rapidly with closed lips and backs out of the doorway. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.5s, spoken on camera by @Beo (man of 28, strictly standard Hà Nội Northern accent (never Southern accent), rough loud bass, blustering, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Đại ca ơi, cả mạng đang chia sẻ lại buổi phát trực tiếp, công an kinh tế đang lên tận đây rồi!"
- Turn 2, 9.0–13.8s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Gọi hết anh em ra chặn cổng, tuyệt đối đừng để lão già ấy ra khỏi tòa nhà này!"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heavy running footsteps, flip-flops flapping, a phone buzzing nonstop, a distant siren far below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 4 (`canh-21/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A small empty teacup on the glass desk beside the chrome chair in the boss room, the ring light glowing and the deserted call-center floor visible beyond the glass, no person in frame.
- 3.0–7.0s: @Lam rises from the chrome chair, settles a battered green pith helmet on his head and sets the empty teacup neatly upside down on its saucer, lips closed.
- 7.0–11.0s: @Lam strolls unhurried out of the boss room and down the empty aisle between the glowing monitors, hands clasped behind his back, plastic sandals scuffing the carpet.
- 11.0–15.0s: @Lam steps into the waiting elevator, turns to face the camera and gives a small closed-mouth nod as the steel doors slide shut in front of him. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Giữa lúc cả đế chế Phú Quý đang sụp đổ, ông Lâm đứng dậy, đội lại mũ cối, xếp lại chén trà cho ngay ngắn, rồi thong thả bước vào thang máy, như một ông khách quen vừa uống xong ấm trà ở quán nước đầu ngõ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a teacup set down on glass, unhurried sandal footsteps, an elevator chime, doors sliding closed. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 1 (`canh-22/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on the wide street in front of the glass tower: neon reflections on the asphalt, tall trees, parked motorbikes, warm streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: twenty young debt collectors in black on motorbikes revving and blocking the tower entrance
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 18mm high wide shot slow crane-down; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: High wide view of the empty night street in front of the gleaming glass tower, neon reflections rippling on the asphalt under warm streetlamps and tall trees, no person in frame.
- 3.0–7.0s: Twenty young debt collectors in black roll their motorbikes into a wide half-circle a good distance from the tower's glass doors, revving engines, headlights flaring into a wall of white glare.
- 7.0–11.0s: The glass doors part and @Lam walks out alone into the glare, pith helmet on and hands empty, and stops on the pavement far from the idling motorbikes.
- 11.0–15.0s: @Lam stands perfectly still inside the distant ring of headlights and slowly lifts the brim of his battered green pith helmet with one finger, calm narrow eyes steady and lips closed. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Dưới sảnh, hai chục đàn em của Béo rồ ga chắn kín lối ra, đèn xe chói lòa cả góc phố, thế mà ông Lâm vẫn bước ra một mình, đứng giữa vòng vây, không lùi một bước, chỉ khẽ nâng vành mũ cối." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a chorus of revving motorbike engines, horns blaring, glass doors sliding apart, engines settling into an idle. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 2 (`canh-22/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on the wide street in front of the glass tower: neon reflections on the asphalt, tall trees, parked motorbikes, warm streetlamps.

[CHARACTERS]
- Extra: dozens of cyclos pedaled by old drivers rolling in from both ends of the street, and old-quarter shopkeepers and motorbike-taxi drivers lining the sidewalks in silence
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 24mm aerial drone slow descending glide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Aerial view down the long neon-lit street at night, warm streetlamps and tall trees lining both sidewalks, the white glare of the motorbike half-circle burning in front of the glass tower.
- 3.0–7.0s: From both ends of the street, dozens of cyclos pedaled by old drivers in faded shirts and conical hats roll in slowly side by side, their bells tinkling.
- 7.0–11.0s: The cyclos glide to a quiet stop in two long lines along the curbs, as shop doors swing open and shopkeepers in aprons and motorbike-taxi drivers in pith helmets step out.
- 11.0–15.0s: The silent crowd stands shoulder to shoulder along both sidewalks with arms folded and mouths closed, every gaze turned toward the glass tower under the neon. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Rồi từ hai đầu phố, hàng chục chiếc xích lô của các bác già phố cổ chậm rãi đạp tới, các bà bán hàng, các ông xe ôm cũng lần lượt bước ra, đứng kín hai bên vỉa hè, không ai nói một lời." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: dozens of cyclo bells tinkling, bicycle chains clicking, shop doors creaking open, shuffling sandals, then a deep hush over idling engines. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 3 (`canh-22/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on the wide street in front of the glass tower: neon reflections on the asphalt, tall trees, parked motorbikes, warm streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm medium close-up slow tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The neon-lit sidewalk under tall trees at night, streetlamp light pooling on the paving stones and exhaust haze drifting through the white glare of headlights, no person in frame.
- 3.0–7.0s: @BaHoa strides into frame at the head of the crowd, waving a woven bamboo hand fan in slow lazy strokes, red lips pressed together, gold hoop earrings swinging.
- 7.0–11.0s: @BaHoa stops at the curb, plants one hand on her hip and looks slowly across the ring of motorbikes, her chunky gold bangle glinting in the headlight glare.
- 11.0–15.0s: @BaHoa lowers her chin and narrows her sharp eyes toward screen-right with a closed-mouth smirk, fanning herself like a cook eyeing a grill about to burn. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đi đầu là bà Hoa, son đỏ chót, tay phe phẩy quạt nan, bà chẳng nói câu nào, chỉ đứng nhìn lũ đàn em như nhìn một mẻ chả sắp cháy trên bếp than, thế là đủ cho chúng nó lạnh hết cả gáy." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft flap of a bamboo hand fan, heeled sandals clicking, idling engines sputtering, a hush over the street. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 4 (`canh-22/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on the wide street in front of the glass tower: neon reflections on the asphalt, tall trees, parked motorbikes, warm streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- Extra: young debt collectors walking their motorbikes backward behind him and slipping away
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The wide street in front of the glass tower at night, neon reflections on the asphalt and the white glare of motorbike headlights beneath the tall trees, no person in frame.
- 3.0–7.0s: @Beo stands in the middle of the street turning his shaved head left and right, small eyes darting toward the silent crowds and cyclos lining both sidewalks, lips pressed shut.
- 7.0–11.0s: Behind @Beo, the young debt collectors quietly walk their motorbikes backward, then turn and slip away one by one into the dark side streets.
- 11.0–15.0s: @Beo stands alone in the emptied street under a streetlamp, his cheap fake-gold chain glinting on his black tank top, swallowing hard with his mouth shut. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Béo nhìn quanh, xích lô kín đường, người kín vỉa hè, đám đàn em lần lượt dắt xe lùi lại, rồi từng đứa một lặng lẽ chuồn mất, bỏ lại mình hắn đứng trơ trọi giữa phố với sợi dây chuyền vàng giả lấp lánh." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: motorbike engines cutting off one by one, tires rolling softly backward, footsteps fading, a lonely cricket chirping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 1 (`canh-23/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A dim underground car park with concrete pillars and fluorescent strip lights, a low red sports car with no badge.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A dim underground car park with concrete pillars and flickering fluorescent strip lights, a low red sports car with no badge parked alone with its paint gleaming, no person in frame.
- 3.0–7.0s: @Hung runs in between the pillars clutching his glowing phone, flings the car door open and drops into the low driver's seat, mouth clamped shut.
- 7.0–11.0s: The headlights snap on and the low red sports car pulls out of its bay, swinging toward the exit ramp with its engine screaming through the empty car park.
- 11.0–15.0s: The red taillights streak away up the ramp toward a sliver of neon night at the top, leaving exhaust haze curling under the fluorescent lights. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Hưng chạy xuống hầm, nhảy lên chiếc xe thể thao đỏ, rú ga phóng ra cửa sau tòa nhà, hắn tin rằng chiếc siêu xe mấy tỷ của mình thừa sức bỏ xa một lão già xe ôm với cái xe máy cũ mèm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: hurried sneaker footsteps on concrete, a car door thudding shut, a high-pitched engine roar, tires squealing. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 2 (`canh-23/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Evening rush hour on a wide Hà Nội avenue: a dense river of motorbikes and cars, red taillights, neon and streetlamps, trees along the sidewalks.

[CHARACTERS]
- Extra: a dense crowd of evening commuters on motorbikes in helmets and face masks, among them an old woman with a scooter full of potted flowers, seen from above
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 35mm top-down aerial drone slow descent; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Top-down aerial view of a wide Hà Nội avenue at evening rush hour, a dense river of motorbikes crawling under neon and streetlamps, red taillights glowing.
- 3.0–7.0s: In the middle of the motorbike river, a low red sports car with no badge sits wedged in place, tinted windows dark, inching forward a hand's width at a time while scooters stream around it.
- 7.0–11.0s: An old woman in a conical hat on a scooter loaded with a tall tower of potted flowers putters past the stranded sports car at an easy pace and gives one cheerful honk.
- 11.0–15.0s: The camera sinks toward the gleaming red hood as its hazard lights blink helplessly, the sea of motorbikes flowing on all around it under the neon. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Nhưng đây là Hà Nội giờ tan tầm, chiếc siêu xe đỏ chói chỉ nhích được vài mét giữa biển xe máy, còn một bà cụ chở cả xe hoa vẫn thong thả vượt qua mặt nó, lại còn bấm còi chào một tiếng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a sea of beeping scooter horns, idling engines, a sports car engine revving uselessly, one long comic honk. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 3 (`canh-23/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Evening rush hour on a wide Hà Nội avenue: a dense river of motorbikes and cars, red taillights, neon and streetlamps, trees along the sidewalks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: evening commuters on motorbikes stalled around him, faces hidden by helmets and face masks
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide tracking shot alongside; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A narrow gap snaking between rows of idling motorbike taillights and chrome mirrors on the jammed avenue at evening rush hour, neon and streetlamps glowing, no person in frame.
- 3.0–7.0s: @Lam threads into the gap on the old cream-colored step-through motorbike with a round chrome headlamp, battered green pith helmet low, slipping between the lanes like a fish through reeds.
- 7.0–11.0s: @Lam glides past the stalled commuters with steady hands and a polite tap of his little horn, eyes fixed ahead and lips closed, never brushing a single mirror.
- 11.0–15.0s: Far ahead through the traffic, the low red sports car with no badge glows under the streetlamps as @Lam's round chrome headlamp closes in steadily behind it. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Phía sau, ông Lâm trên chiếc xe máy cũ lách qua dòng xe như cá lội, ba mươi năm chạy xe ôm, ngõ ngách nào của Hà Nội ông cũng thuộc như lòng bàn tay, mỗi lúc một gần chiếc siêu xe đỏ chói." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: an old engine puttering steadily, a cheerful little horn beep, a sea of idling engines and horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 4 (`canh-23/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Evening rush hour on a wide Hà Nội avenue: a dense river of motorbikes and cars, red taillights, neon and streetlamps, trees along the sidewalks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The gleaming roof and dark tinted windows of the low red sports car with no badge, stranded at the curb of the jammed avenue, red taillights blurring all around it, no person in frame.
- 3.0–7.0s: On screen-left, @Lam sits on the old cream-colored step-through motorbike with a round chrome headlamp and starts talking to himself, face and lips clearly visible, as @Hung jumps out of the red car.
- 7.0–11.0s: @Hung sprints away along the tree-lined sidewalk toward a distant steel truss bridge, clutching his glowing phone, while @Lam keeps talking with a dry chuckle and slowly shakes his head.
- 11.0–15.0s: @Lam finishes, closes his mouth, tugs the strap of his battered green pith helmet tight and twists the throttle with a small sly grin. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.8s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chạy bộ lên cầu mà đòi thoát Lâm Rồng à? Ba mươi năm trước ông phóng xe trên cây cầu ấy còn nhiều hơn cậu đi thang máy, thằng nhóc này còn non lắm." (no subtitles)
- From 3.0s onward, @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: an old engine puttering, a car door swinging open, sneakers slapping the pavement, distant horns, the motorbike revving. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 1 (`canh-24/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on a century-old steel truss railway bridge over a wide dark river: rusty iron lattice beams lit by sparse lamps, a narrow motorbike lane beside the tracks, city lights on the far bank.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm high wide shot slow crane-down; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A century-old steel truss railway bridge spanning a wide dark river at night, its rusty iron lattice lit by sparse lamps and city lights shimmering on the far bank, no person in frame.
- 3.0–7.0s: The camera glides down along the bridge's long iron spine toward the narrow motorbike lane beside the tracks, lamplight pooling on the rails as river mist drifts through the beams.
- 7.0–11.0s: @Hung runs into frame along the motorbike lane, panting, phone clutched to his chest, then skids to a halt in the middle of the span.
- 11.0–15.0s: @Hung stares ahead with his mouth clamped shut as blue and red lights flash far away at the end of the bridge, sealing the way down, no figures visible there. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cây cầu sắt trăm tuổi, nơi ba mươi năm trước Lâm Rồng từng làm mưa làm gió, đêm nay lại chứng kiến một cuộc rượt đuổi, Hưng chạy đến giữa cầu thì khựng lại, phía bên kia đèn công an đã chắn kín lối." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind whistling through iron girders, the river lapping far below, sneakers pounding on iron plates, a distant police siren whooping softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 2 (`canh-24/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on a century-old steel truss railway bridge over a wide dark river: rusty iron lattice beams lit by sparse lamps, a narrow motorbike lane beside the tracks, city lights on the far bank.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Low view down the motorbike lane of the old steel truss bridge at night, a warm round headlamp approaching slowly out of the dark between the rusty iron beams, no person visible.
- 3.0–7.0s: @Lam rolls to a stop on screen-left on the old cream-colored step-through motorbike with a round chrome headlamp, and @Hung on screen-right spins around and yells at him, face and lips clearly visible.
- 7.0–11.0s: @Hung keeps shouting with one ringed finger pointed, ash-blond hair wind-tossed and glasses askew, while @Lam calmly sets the motorbike on its stand and swings one leg off.
- 11.0–15.0s: @Hung closes his mouth, chest heaving, as @Lam lifts the battered green pith helmet off his grey crew cut and holds it at his side under a bridge lamp, lips closed. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.8s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông nghĩ ông là cái thá gì mà dám chơi tôi? Bố tôi bảo ông từng là Lâm Rồng gì đấy, nhưng giờ ông chỉ là một lão già chạy xe ôm hết thời thôi!" (no subtitles)
- From 3.0s onward, @Hung's face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: an old engine puttering to a stop, the metal clack of a side stand, wind howling through iron girders, ragged breathing. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 3 (`canh-24/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on a century-old steel truss railway bridge over a wide dark river: rusty iron lattice beams lit by sparse lamps, a narrow motorbike lane beside the tracks, city lights on the far bank.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm low-angle close-up slow tilt-up; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close on @Lam's right forearm as he silently rolls up his sleeve fold by fold, revealing a coiled dark-green dragon tattoo gleaming under the bridge lamp, his lips closed.
- 3.0–7.0s: The camera tilts up to @Lam's face as he lowers the tattooed arm and speaks to @Hung in a calm husky voice, face and lips clearly visible, the lamp haloing his grey crew cut.
- 7.0–11.0s: @Lam keeps talking evenly, one weathered finger resting on the dragon on his forearm, calm narrow eyes never leaving @Hung, who stands frozen in soft focus on screen-right.
- 11.0–15.0s: @Lam finishes with a slow nod and closes his mouth, while @Hung takes a shaky step back with lips pressed tight and knuckles white around his phone. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.5s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bố cậu chưa kể hết à? Ba mươi năm trước, phố cổ này là của Rồng, giờ vẫn thế, mà Rồng thì chưa bao giờ phải động đến một ngón tay, cậu ạ." (no subtitles)
- @Lam keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft rustle of a rolled sleeve, wind whistling through the iron lattice, the deep rumble of the river, distant sirens drawing closer. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 4 (`canh-24/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on a century-old steel truss railway bridge over a wide dark river: rusty iron lattice beams lit by sparse lamps, a narrow motorbike lane beside the tracks, city lights on the far bank.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide shot slow crane-down; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Hung backs away step by step until his back meets the rusty iron railing of the bridge, mouth shut, the wide dark river glittering far below.
- 3.0–7.0s: The phone on its small selfie gimbal slips from @Hung's trembling fingers and tumbles over the railing, its blank screen still glowing as it spins down through the dark.
- 7.0–11.0s: The glowing phone vanishes into the black river with a tiny splash, its light winking out beneath the rippling reflections of the city.
- 11.0–15.0s: @Hung leans on the railing staring down at the spreading ripples with his mouth shut, a small lone figure on the vast lamp-lit iron bridge. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Hưng lùi lại đến sát lan can, chiếc điện thoại tuột khỏi tay rơi tõm xuống dòng sông, nhưng muộn rồi, năm triệu người xem đã kịp thấy hết, nghe hết, và cả đế chế Phú Quý cũng chìm nghỉm theo nó trong làn nước đen." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a sharp gasp, the clatter of a gimbal on iron, a faint distant splash, wind and rushing water. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 1 (`canh-25/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on a century-old steel truss railway bridge over a wide dark river: rusty iron lattice beams lit by sparse lamps, a narrow motorbike lane beside the tracks, city lights on the far bank.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- Extra: two police officers in green uniforms walking up calmly
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The middle span of the old steel truss bridge at night, blue and red lights washing softly over the rusty iron lattice and the empty motorbike lane, no person in frame.
- 3.0–7.0s: @Hung stands alone by the railing on screen-right as two police officers in green uniforms walk up calmly from screen-left and stop a few steps away, hands relaxed at their sides.
- 7.0–11.0s: @Hung slowly raises both his own hands and offers them out in front of him, ringed fingers trembling, face drained pale and lips pressed shut, while the officers wait without moving.
- 11.0–15.0s: @Hung lowers his head, ash-blond hair falling over his gold-rimmed glasses, a small figure under the bridge lamp as the blue and red light keeps washing over him. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trên cầu, hai cán bộ công an thong thả bước tới, Hưng tự giơ hai tay ra trước mặt, gương mặt kiêu ngạo của ông chủ Phú Quý giờ trắng bệch như tờ giấy, chẳng còn nụ cười nào để livestream cho ai xem nữa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: calm footsteps on iron plates, a police radio crackling softly, wind through the girders, the river below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 2 (`canh-25/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- Extra: a police officer standing calmly nearby
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot slow lateral dolly; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The deserted call-center floor at night, rows of empty desks and blank glowing monitors under magenta and gold neon, headsets scattered across the desks, no person in frame.
- 3.0–7.0s: @Beo sits slumped on the floor between the desks hugging his glowing phone to his chest, his closed lips wobbling into a pout like a lost child.
- 7.0–11.0s: A police officer in a green uniform stands calmly a few steps away with hands behind his back, looking down at @Beo without a word.
- 11.0–15.0s: @Beo sniffles and wipes his eyes with his wrist, his cheap fake-gold chain glinting, heavy shoulders sagging under the pulsing magenta neon. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Còn ở văn phòng Phú Quý, Béo Đầu Sấm ngồi bệt dưới sàn, ôm khư khư cái điện thoại, mếu máo như đứa trẻ lạc mẹ, bên cạnh là một chú công an kiên nhẫn đứng chờ, chẳng buồn nói với hắn câu nào." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a loud sniffle, monitor hum, a police radio crackling softly, the whine of the air conditioner. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 3 (`canh-25/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A sunny university schoolyard in the morning with tall trees and old yellow buildings.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- Extra: groups of students looking at their phones and hugging each other
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm aerial drone slow descending glide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Aerial view of a sunny university schoolyard in the morning, tall trees casting dappled shade over the paving and old yellow buildings with green shutters all around, no person in frame.
- 3.0–7.0s: Groups of students gather under the trees staring down at their blank glowing phone screens, then lift their heads and wrap one another in silent tearful hugs.
- 7.0–11.0s: The drone descends toward a bench under a tall tree where @Mai sits in her lavender hoodie, turning over her phone and looking at its softly glowing screen.
- 11.0–15.0s: @Mai lets out a long breath, eyes glistening behind her round glasses, a closed-mouth smile spreading across her face as she presses the phone to her chest. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Sáng hôm sau, ứng dụng Phú Quý bị khóa, hàng nghìn sinh viên được xóa nợ, nhiều đứa ôm nhau khóc giữa sân trường, còn Mai mở điện thoại, lần đầu sau ba tháng, không còn cuộc gọi lạ nào, chỉ có tin nhắn cảm ơn của bạn bè." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong, rustling leaves, soft sniffles, a chorus of gentle message chimes. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 4 (`canh-25/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning inside Lâm's narrow old-quarter tube house: a ground-floor room with the rolling steel shutter raised, a worn wooden table, a small family altar, sunlight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Morning inside the narrow tube house, sunlight spilling over the worn wooden table and the small family altar, the rolling steel shutter raised to the street, no person in frame.
- 3.0–7.0s: @Mai hops onto the stool on screen-left beside @Lam and tells him the news with a beaming grin, face and lips clearly visible, holding up her glowing phone, while @Lam listens.
- 7.0–11.0s: @Mai closes her mouth and nudges her glasses up, as @Lam on screen-right sets down his teacup, waves the compliment away and answers in a dry husky voice, face and lips clearly visible.
- 11.0–15.0s: @Lam finishes with a modest shrug and closes his mouth, putting on his battered green pith helmet to hide a little smile, while @Mai covers her grin with her hand. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Ông ơi, cả lớp cháu bảo ông là ông nội ngầu nhất cái Hà Nội này đấy ông ạ!"
- Turn 2, 8.3–13.2s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Ngầu gì, ông chỉ là ông già xe ôm, mai ông còn phải chở cụ Tý đi chợ sớm."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning street bustle, birdsong, a teacup clinking on wood, a motorbike horn outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 1 (`canh-26/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A bright, clean eye-hospital room in the morning: a white bed, a big window full of sunlight, a small bedside table with a thermos and a vase of daisies.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 35mm wide shot slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: A bright, clean eye-hospital room in the morning, sunlight pouring through the big window over an empty white bed with neatly folded sheets.
- 3.0–7.0s: The camera glides toward the bedside table crowded with gifts from the old quarter: a thermos, a vase of daisies, a bag of oranges, a basket of fresh herbs and a tin lunchbox.
- 7.0–11.0s: Beside the gifts sit a brass cyclo bell, a bundle of sticky rice wrapped in banana leaf and a folded paper with faint unreadable lines, all glowing in the morning sun.
- 11.0–15.0s: The camera settles on a woven bamboo hand fan resting on top of the pile of gifts, glowing in a warm sunbeam beside the daisies. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Một tuần sau, tiền mổ mắt cho ông Lâm do cả phố cổ góp lại, người một ít, bác xích lô góp mấy buổi chạy xe, bà bán xôi góp cả tháng lãi, còn bà Hoa góp nhiều nhất, nhưng cấm ai được kể cho ông nghe." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft hospital hum, birdsong outside the window, a curtain rustling in the breeze. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 2 (`canh-26/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A bright, clean eye-hospital room in the morning: a white bed, a big window full of sunlight, a small bedside table with a thermos and a vase of daisies.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: a nurse in white scrubs seen from behind
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Sunlight glowing through the big window of the bright eye-hospital room onto a small steel tray holding a roll of white gauze, no person in frame.
- 3.0–7.0s: @Lam sits up in the white bed with a gauze bandage over his eyes as a nurse in white scrubs, seen from behind, gently unwinds it layer by layer.
- 7.0–11.0s: The last layer comes away and @Lam blinks several times into the flood of morning light, his once-cloudy left eye now clear, gazing at the leaves outside the window.
- 11.0–15.0s: @Lam slowly turns his head toward the bedside on screen-left, eyes widening and glistening, a slow closed-mouth smile spreading across his weathered face. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–11.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cô y tá từ từ tháo băng, ông Lâm chớp mắt mấy lần trong ánh nắng sớm, mọi thứ mờ mờ rồi rõ dần, lần đầu sau bao nhiêu năm, ông nhìn rõ từng chiếc lá ngoài cửa sổ, và cả người đang đứng bên giường." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft rustle of unwinding gauze, birdsong, a gentle hospital hum, a deep slow breath. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 3 (`canh-26/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A bright, clean eye-hospital room in the morning: a white bed, a big window full of sunlight, a small bedside table with a thermos and a vase of daisies.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot slow arc; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The bedside of the bright eye-hospital room, sunlight streaming through the big window behind a vase of daisies on the small bedside table, no person in frame.
- 3.0–7.0s: @Lam sits up in the white bed on screen-right and looks at @Mai with clear bright eyes, speaking softly in his husky voice, face and lips clearly visible, while @Mai listens with closed lips.
- 7.0–11.0s: @Lam closes his mouth with a teasing smile, as @Mai on screen-left, red-rimmed eyes glistening behind her round glasses, answers through her tears, face and lips clearly visible.
- 11.0–15.0s: @Mai finishes, closes her mouth and wipes her eyes under her glasses with a silent laugh, while @Lam watches her with a warm closed-mouth smile in the sunlight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.9s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter): "Cháu ông xinh thế này mà mấy năm nay ông chỉ nhìn thấy lờ mờ, phí quá con ạ."
- Turn 2, 8.4–12.9s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Thế thì ông ngắm cháu cả đời đi, từ nay cháu không để ông phải lo nữa đâu."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong, a soft sniffle, a curtain swaying in the breeze, distant street horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 4 (`canh-26/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The doorway of the bright eye-hospital room, a white corridor behind, morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The doorway of the bright eye-hospital room in morning light, a clean white corridor stretching behind it and sunlight on the tiled floor, no person in frame.
- 3.0–7.0s: @BaHoa sweeps into the doorway on screen-left with @Khoa beside her on screen-right and calls toward the bed in a brassy teasing voice, face and red lips clearly visible, bamboo fan in hand.
- 7.0–11.0s: @BaHoa closes her mouth and arches one eyebrow, as @Khoa leans toward the bed with a hand cupped beside his mouth and speaks in a dry nasal deadpan, face and lips clearly visible.
- 11.0–15.0s: @Khoa finishes with a sly closed-mouth wink, while @BaHoa flicks her bamboo fan open in front of her face to hide her reddening cheeks, lips pressed tight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Mắt sáng rồi thì nhớ trả tôi tiền bún chả ba mươi năm nay ông ăn chịu đấy nhé!"
- Turn 2, 8.3–12.8s, spoken on camera by @Khoa (man of 60, strictly standard Hà Nội Northern accent (never Southern accent), nasal wry tenor, deadpan and fussy, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Bà ấy nói đùa đấy, thực ra bà ấy khóc cả đêm qua vì lo cho ông đấy."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heeled sandals clicking on tile, a bamboo fan flicking open, a stifled sniff, a quiet hospital corridor hum. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 1 (`canh-27/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium close-up two-shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A steel table at the bustling bún chả shop with bowls of noodles, a basket of fresh herbs and a small paper bill with faint unreadable lines, charcoal smoke drifting, no person in frame.
- 3.0–7.0s: @BaHoa and @Khoa reach for the bill at the same instant from opposite sides of the table, each pinching one end of it, lips pressed together.
- 7.0–11.0s: The little bill tugs back and forth between them as @BaHoa narrows her eyes and @Khoa lifts his chin, neither letting go, grill smoke curling between them.
- 11.0–15.0s: Both freeze and glare across the table with stubborn closed-mouth smiles, the paper bill stretched taut between their fingertips in the warm smoky sunlight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Sáng hôm sau, phố cổ lại bình yên như cũ, ở quán bún chả, bà Hoa và ông Khoa lại tranh nhau trả tiền chầu sáng, tờ hóa đơn bị kéo qua kéo lại, ba mươi năm rồi mà Hổ với Báo vẫn chưa phân thắng bại." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pork sizzling on charcoal, a paper bill crinkling, chopsticks clinking, street bustle. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 2 (`canh-27/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn in Hà Nội's old quarter: an ancient brick city gate with a tiled roof, narrow streets of tube houses with green shutters, tangled overhead wires, street vendors with shoulder poles, pink-gold morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Golden morning light under the ancient brick city gate with its tiled roof, sparrows hopping on the old bricks and tangled wires overhead, the archway empty, no person in frame.
- 3.0–7.0s: The old cream-colored step-through motorbike with a round chrome headlamp rolls slowly in under the arch carrying @Lam in front and @Mai behind him, a laptop hugged to her chest.
- 7.0–11.0s: @Mai hops off, waves with a bright closed-mouth grin and strides away down the sunlit street with her small black backpack and laptop, while @Lam watches her go.
- 11.0–15.0s: @Lam sets the motorbike on its stand under the gate, sits sideways on the seat and folds his arms, lips closed in a quiet smile as golden sunlight spills through the arch. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm lại đội mũ cối, chở cháu gái qua cổng Ô đi học, Mai đang viết một ứng dụng giúp sinh viên nhận ra các app cho vay lừa đảo, còn ông thì dựng xe dưới vòm cổng, đợi khách như chưa từng có chuyện gì." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: sparrows chirping, an old engine puttering to a stop, a broom sweeping the pavement, a vendor's hand bell, distant motorbike horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 3 (`canh-27/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn in Hà Nội's old quarter: an ancient brick city gate with a tiled roof, narrow streets of tube houses with green shutters, tangled overhead wires, street vendors with shoulder poles, pink-gold morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: a young man in a delivery jacket hugging his helmet to his chest
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: A young man in a delivery jacket approaches @Lam from screen-right, glances left and right, then points a hesitant finger at @Lam's right sleeve with eyebrows raised, lips pressed shut.
- 3.0–7.0s: @Lam looks up at him, tugs his sleeve down over his forearm and answers with a warm chuckle in a calm husky voice, face and lips clearly visible.
- 7.0–11.0s: @Lam keeps talking warmly and pats the motorbike's back seat twice with his palm, while the young man listens with closed lips, his hunched shoulders slowly relaxing.
- 11.0–15.0s: @Lam finishes, closes his mouth and gives a knowing wink as the young man climbs onto the back seat behind him in the golden light under the gate. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.5s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Lâm Rồng nào cơ? Cậu nhầm người rồi, tôi chỉ là ông già xe ôm thôi, nhưng cứ ngồi lên xe đi, rồi kể tôi nghe xem đứa nào đang bắt nạt cậu." (no subtitles)
- @Lam keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: sparrows chirping, shuffling footsteps, a palm patting a vinyl seat, the old engine coughing to life. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 4 (`canh-27/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Golden morning aerial over Hà Nội's old quarter: tiled roofs, the ancient brick city gate, a cream motorbike weaving into the streets.

[CHARACTERS]
- Extra: two tiny distant riders on a cream motorbike far below, seen from high above
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 24mm aerial drone slow rising pull-back; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Golden morning aerial low over the ancient brick city gate with its tiled roof as the old cream-colored step-through motorbike with a round chrome headlamp, carrying two tiny riders, rolls out from under the arch.
- 3.0–7.0s: The drone rises and pulls back as the little cream motorbike weaves into the narrow streets between tube houses, tangled wires and fluttering laundry, sunlight flaring off its chrome headlamp.
- 7.0–11.0s: A flock of pigeons sweeps across the frame as the camera soars higher, the tiled roofs of the old quarter spreading out in every direction and glowing gold.
- 11.0–15.0s: The camera hangs high above a vast sea of tiled roofs and the distant gleam of a lake, the whole old quarter of Hà Nội waking below in a grand sunlit panorama. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–12.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Chiếc xe máy cũ chở vị khách mới len vào lòng phố, găng tơ đã tái xuất, phố cổ Hà Nội từ hôm nay lại có một con rồng thức giấc canh giữ, và phi vụ tiếp theo của bộ ba Rồng, Hổ, Báo đã bắt đầu." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a rising morning breeze, a flock of pigeons' wings fluttering, distant motorbike horns and bicycle bells, the old engine puttering away. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```
