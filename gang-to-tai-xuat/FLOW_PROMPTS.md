# Găng Tơ Tái Xuất — Bộ 162 Prompt Google Flow Omni (27 Cảnh × 6 Clips × 10s)

- **Giọng Người Dẫn Chuyện (cố định cả 162 clip):** Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; đọc nhanh liên thanh như oan-thai-doi-me, ~4.0 âm tiết/giây, liền một hơi, không ngắt giữa câu.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 162 clips × 10s — 102 clip VO + 60 clip thoại; lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 45 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 96 clip ảnh nhân vật (Ingredients), 21 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** clip VO được tăng tốc giọng thêm 1.18x khi tải về (`FLOWKIT_VOICE_TEMPO` mặc định 1.18, đặt 1.0 để tắt), giữ nguyên khung hình 10s; clip lip-sync không bao giờ bị tăng tốc để khớp khẩu hình.
- **Màu phim & ánh sáng:** Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py gang-to-tai-xuat` sinh lại toàn bộ clip, README, kịch bản.

---

## Cảnh 01 - Clip 1 (`canh-01/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn aerial over the tiled roofs of Hà Nội's old quarter: an ancient brick city gate, tangled wires, motorbikes streaming, pink-gold light.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 24mm aerial drone glide sweeping forward and descending toward the city gate; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: High aerial view at dawn over a vast sea of mossy tiled roofs in Hà Nội's old quarter, pink-gold sunlight spilling across the rooftops as wisps of morning mist curl between them.
- 3.0–7.0s: The drone glides forward over tangled overhead wires while streams of motorbikes pour through the narrow streets below like bright rivers, their headlamps twinkling in the soft golden light.
- 7.0–10.0s: The camera sweeps down toward the ancient brick city gate, its curved tiled roof glowing gold as motorbikes flow through the arch and the rising sun flares over the old quarter. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Phố cổ Hà Nội buổi sớm, ba mươi sáu phố phường vừa thức giấc trong tiếng rao và tiếng còi xe." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a chorus of distant motorbike horns waking the streets, a faraway street vendor calling out, pigeons' wings fluttering past, a soft morning breeze. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 2 (`canh-01/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn in Hà Nội's old quarter: an ancient brick city gate with a tiled roof, narrow streets of tube houses with green shutters, tangled overhead wires, street vendors with shoulder poles, pink-gold morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot with a slow dolly-in under the gate arch; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Under the arch of the ancient brick city gate in pink-gold dawn light, the old cream-colored step-through motorbike with a round chrome headlamp stands parked on the worn stones, its chrome glinting.
- 3.0–7.0s: @Lam walks into frame from screen-left, pulls a soft rag from his windbreaker pocket and wipes the cracked vinyl seat with slow, careful strokes, his mouth closed in a calm half-smile.
- 7.0–10.0s: @Lam lifts a battered green pith helmet from the handlebar and settles it on his grey crew cut, then gives the seat a final fond pat as the sunrise warms his face. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ở cổng Ô Quan Chưởng có ông Lâm xe ôm, sáu mươi ba tuổi, hiền như đất, chở cụ già đi chợ chẳng bao giờ lấy tiền." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a cloth squeaking on vinyl, morning birds chirping, motorbikes puttering past the gate, a vendor's bamboo shoulder pole creaking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 3 (`canh-01/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: Close on the old cream-colored step-through motorbike with a round chrome headlamp parked by the brick city gate, dawn light glinting on the chrome and a woven shopping basket resting on the stones.
- 3.0–7.0s: @Lam, astride the motorbike, turns his head over his shoulder and speaks warmly to a tiny old lady in a conical hat as she climbs onto the back seat by herself.
- 7.0–10.0s: @Lam finishes, closes his mouth into a crinkle-eyed grin and faces forward, while the old lady settles her basket on her lap and nods with her lips pressed in a shy smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.2s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cụ cứ ngồi vững vào, tiền nong gì, cháu chở cụ như chở mẹ cháu thôi." (no subtitles)
- From 3.0s onward, @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the motorbike engine idling, a basket handle creaking, sparrows chirping, distant horns echoing off the gate. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 4 (`canh-01/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm wide side-tracking shot gliding alongside the motorbike; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A narrow old-quarter street of tube houses with green shutters glows in pink-gold morning light, tangled wires sagging overhead and steam rising from a pavement food stall.
- 3.0–7.0s: @Lam rides the old cream-colored step-through motorbike with a round chrome headlamp slowly down the street, his mouth closed, as an old street vendor on the far pavement dips her head to greet him.
- 7.0–10.0s: @Lam lifts two fingers from the handlebar in a small friendly salute and rides on alone, the sun flaring behind him as the vendor slips out of the frame. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Không ai trong phố biết, ba mươi năm trước, chính ông già này từng khiến cả phố cổ phải cúi đầu." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft putter of an old motorbike engine, a shoulder pole creaking, a bicycle bell, sizzling from a street food stall. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 5 (`canh-01/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn in Hà Nội's old quarter: an ancient brick city gate with a tiled roof, narrow streets of tube houses with green shutters, tangled overhead wires, street vendors with shoulder poles, pink-gold morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up tracking shot alongside his right forearm on the handlebar; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam rides on through the golden street, his right hand resting on the handlebar as a gust of morning wind tugs at the loose sleeve of his grey windbreaker.
- 3.0–7.0s: The wind flips the sleeve back for a heartbeat, revealing the curled clawed tail of a dark-green dragon tattoo coiled across the wrinkled skin of his right forearm, its scales catching the sunlight.
- 7.0–10.0s: The sleeve falls back over the tattoo and @Lam glances down at it, his mouth closed in a faint knowing smile under the battered green pith helmet. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–4.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Người ta gọi ông là Lâm Rồng, và con rồng ấy đã ngủ yên suốt ba mươi năm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a rush of wind flapping fabric, the steady putter of the motorbike engine, a single low gong-like hum fading. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 6 (`canh-01/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 35mm medium shot with a slow push-in on the shutter; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: A narrow old-quarter alley at night under a single yellow streetlamp, the rolling steel shutter of the tube house closed, potted plants beside the step and puddles shining on the wet pavement.
- 3.0–7.0s: Glossy bright red paint runs down the corrugated steel shutter in long thick streaks, dripping from every ridge and pooling on the doorstep while the alley stays completely empty.
- 7.0–10.0s: The camera settles close on one fresh red drip sliding down the shutter and falling into a puddle, a red ripple spreading across the reflected yellow lamplight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cho đến cái đêm có một bọn nhóc dám hắt sơn đỏ lên cánh cửa nhà ông, và đánh thức con rồng dậy." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: slow wet drips of paint, a dog barking far away, the last motorbike engine fading out of the alley. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 1 (`canh-02/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: @Mai pauses with her fingers on the keys and glances fondly toward the dark back of the room, a small closed-mouth smile tugging at the corners of her lips. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Mai, cháu gái ông, hai mươi tuổi, sinh viên công nghệ thông tin, được ông Lâm một tay nuôi lớn từ năm lên ba." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: quick soft keyboard taps, a ticking wall fan, a faint motorbike passing outside the shutter. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 2 (`canh-02/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm close-up with a slow push-in on her hands and the phone; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Mai keeps typing as a phone lying beside the laptop buzzes and rattles against the wooden table, its blank screen flashing bright white with nothing written on it.
- 3.0–7.0s: @Mai stops typing and stares at the glowing blank screen while it buzzes again and again, her lips pressed tightly together as she slowly reaches toward it.
- 7.0–10.0s: @Mai flips the phone face-down on the table and keeps her palm flat on top of it, the buzzing muffled against the wood as her shoulders rise and fall. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–4.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Nhưng mấy tuần nay, điện thoại của Mai rung suốt đêm, toàn những số máy lạ không tên." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone vibrating hard against a wooden table, muffled buzzing, a slow exhale through the nose. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 3 (`canh-02/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 28mm wide shot with a slow pull-back from the table; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Mai leans back from the table and counts silently on her fingers, her lips pressed shut, the laptop's blue glow and the warm lamp lighting her face from two sides.
- 3.0–7.0s: @Mai stops counting at the last finger, then slowly cups both palms over her mouth and nose, eyes fixed wide on the glowing screen, her shoulders sinking inside the lavender hoodie.
- 7.0–10.0s: As the camera pulls back, @Mai sits small and still at the worn wooden table in the dim tube house, the face-down phone buzzing faintly beside the glowing laptop. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ba tháng trước, cô vay năm triệu qua một ứng dụng trên mạng, giờ con số ấy đã phình thành một trăm năm mươi triệu." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the muffled buzz of a face-down phone, a wall clock ticking, incense crackling softly on the altar. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 4 (`canh-02/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The steep wooden staircase at the back of the dim tube house, lit only by a sliver of warm lamplight, a small backpack slumped on the bottom step.
- 3.0–7.0s: @Mai crouches on the bottom step hugging her knees, presses the phone to her ear and whispers fast and pleading into it, her face lit by its pale glow.
- 7.0–10.0s: @Mai finishes, closes her mouth and squeezes her eyes shut, the phone still at her ear and her free hand clutching the hood strings of her lavender hoodie. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Em xin anh thêm một tuần thôi, em sẽ trả, xin anh đừng gọi cho bạn bè em nữa!" (no subtitles)
- From 3.0s onward, @Mai's face and lips stay clearly visible while speaking; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a hushed whisper in the quiet house, a faint muffled male voice from the phone speaker, the wooden step creaking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 5 (`canh-02/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up with a slow tilt down onto the pillow; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The camera starts on the shadowy back wall of the tube house, a battered green pith helmet hanging on a nail, lit by a thin sliver of warm lamplight.
- 3.0–7.0s: The camera tilts down to the single bed where @Lam lies still on his back under a thin blanket, his eyes wide open in the dark, catching the lamplight.
- 7.0–10.0s: @Lam keeps perfectly still with his mouth closed, only his eyes sliding toward the staircase as he listens, his jaw slowly tightening under the grey stubble. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ở giường trong, ông Lâm vẫn nằm im, nhưng đôi mắt ông mở to trong bóng tối, nghe không sót một lời." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a distant hushed whisper from the staircase, a slow creak of the bed frame, a gecko chirping on the wall. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 6 (`canh-02/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium shot with a gentle handheld drift; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The worn wooden table under the warm lamp, the laptop now closed beside a small family altar where a thin line of incense smoke curls upward.
- 3.0–7.0s: @Mai stands by the table and wipes tears from under her round glasses with the sleeve of her lavender hoodie, her lips pressed tightly together.
- 7.0–10.0s: @Mai tucks the phone deep into her hoodie pocket and pats it flat, then turns her head toward the rolling steel shutter at the front of the house as the lamp flickers once. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Mai lau nước mắt, giấu điện thoại vào túi áo, không biết rằng đêm mai bọn đòi nợ sẽ tìm đến tận cửa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft sniff, the lamp buzzing faintly, a motorbike engine revving far down the alley. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 1 (`canh-03/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 3.0–7.0s: Four black motorbikes roar into the alley one after another, the young riders in black revving their engines, headlights sweeping across the walls and their faces lost in shadow.
- 7.0–10.0s: The four motorbikes brake to a stop in a tight row near the closed rolling steel shutter, engines idling as their headlights glare through drifting exhaust haze. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đêm hôm sau, bốn chiếc xe máy rồ ga lao vào con ngõ nhỏ, tiếng pô nổ vang cả dãy phố." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: four motorbike engines revving and popping, exhaust backfires echoing off the alley walls, tires splashing through puddles, a dog barking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 2 (`canh-03/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium low-angle shot with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A black motorbike idles under the yellow streetlamp beside a puddle, a dented bucket of red paint hanging from its handlebar as exhaust smoke drifts through the light.
- 3.0–7.0s: @Beo swings his heavy leg off the motorbike, his fake-gold chain swaying over his black tank top, and unhooks the paint bucket with one thick hand.
- 7.0–10.0s: @Beo stands tall under the streetlamp with the bucket of red paint, rolling his big shoulders, the lightning-bolt pattern on his shaved head gleaming above a smug closed-mouth smirk. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cầm đầu là Béo Đầu Sấm, đòi nợ thuê cho công ty Phú Quý, khét tiếng khắp các trường đại học Hà Nội." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a side stand clanking down, a metal bucket handle squeaking, flip-flops flapping on wet pavement, engines idling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 3 (`canh-03/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot with a smooth lateral dolly toward the shutter; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Beo walks up to the closed rolling steel shutter under the yellow streetlamp, plants his flip-flops a few steps back from it and swings the paint bucket back in both hands.
- 3.0–7.0s: @Beo heaves the bucket forward and a huge glossy arc of bright red paint sails through the lamplight and splashes across the empty corrugated steel shutter in a wide spray.
- 7.0–10.0s: Red paint streams down the shutter in thick glossy rivulets onto the doorstep as @Beo steps back admiring his work, the empty bucket dangling from one hand, his mouth closed in a smirk. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Hắn hắt cả xô sơn đỏ lên cánh cửa cuốn, sơn đỏ chảy loang lổ xuống tận bậc thềm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a heavy wet splash of paint across corrugated steel, paint dripping and trickling, motorbike engines idling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 4 (`canh-03/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium two-shot from the side of the alley with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The paint-soaked rolling steel shutter drips red onto the doorstep under the yellow streetlamp, the old cream-colored step-through motorbike with a round chrome headlamp parked beside it, a battered green pith helmet on its seat.
- 3.0–7.0s: The shutter rattles up to reveal @Lam on screen-right in his grey windbreaker half-zipped over a white tank top, while @Beo, a few steps away on screen-left, points at the house and speaks loudly.
- 7.0–10.0s: @Beo finishes his words and shuts his mouth in a smug grin, while @Lam stands still in the lamplight with his hands at his sides, gazing at the red paint. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Beo (man of 28, strictly standard Hà Nội Northern accent (never Southern accent), rough loud bass, blustering, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Nhà này có con bé Mai nợ tiền Phú Quý, ba ngày không trả thì lần sau không phải sơn đâu!" (no subtitles)
- From 3.0s onward, @Beo's face and lips stay clearly visible while speaking; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a steel shutter rattling and rolling up, paint dripping onto the step, motorbike engines idling behind. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 5 (`canh-03/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on Lâm with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam looks up from the dripping shutter to @Beo and speaks in a calm, low voice, his weathered face steady and his hands relaxed at his sides.
- 3.0–7.0s: @Lam finishes, closes his mouth and gives a small unhurried nod toward the end of the alley, his cloudy left eye catching the yellow streetlamp.
- 7.0–10.0s: @Beo, at the edge of the frame, snorts and folds his thick arms over his black tank top, his small eyes narrowing as his mouth stays shut. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.1s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cháu tôi nợ bao nhiêu, ông già này trả, các cậu về đi cho hàng xóm còn ngủ." (no subtitles)
- @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: engines idling low, a soft drip of paint, a window shutter creaking open somewhere above. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 6 (`canh-03/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium shot with a slow tilt down to the puddle; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Beo strolls to the old cream-colored step-through motorbike with a round chrome headlamp, lifts a battered green pith helmet off its seat, dangles it from two fingers and mocks @Lam aloud with a gold-toothed sneer.
- 3.0–7.0s: @Beo finishes his taunt, closes his mouth, holds the helmet out over a wide puddle and simply opens his fingers, letting it drop into the water with a splash.
- 7.0–10.0s: The battered green pith helmet rocks upside down in the puddle under the yellow streetlamp while @Lam stands motionless a few steps behind it, only watching, his jaw set. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Beo (man of 28, strictly standard Hà Nội Northern accent (never Southern accent), rough loud bass, blustering, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông già xe ôm thì lấy gì mà trả? Bán cái mũ cối rách này đi à, ông già?" (no subtitles)
- @Beo keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a hollow plop and splash of water, ripples lapping, a mocking snort, engines idling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 1 (`canh-04/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: @Lam wipes the helmet slowly with his sleeve, round and round, his eyes lowered and his lips pressed together as the camera rises to his quiet face. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–4.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm nhặt chiếc mũ cối dưới vũng nước, lau thật chậm, không nói một lời nào." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water trickling from the helmet, a slow drip of paint, crickets, distant motorbikes fading. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 2 (`canh-04/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium two-shot with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the tube house at night, the worn wooden table glows under one warm lamp, a damp battered green pith helmet resting on it beside a folded towel.
- 3.0–7.0s: @Mai stands at the foot of the staircase on screen-right facing @Lam at the table on screen-left, her eyes brimming, and speaks to him quickly in a trembling rush.
- 7.0–10.0s: @Mai finishes, closes her mouth and twists the hem of her lavender hoodie in both hands, while @Lam slowly lowers the towel and stares at her. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.5s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông ơi, cháu xin lỗi, cháu vay tiền là để ông đi mổ mắt, bác sĩ bảo để lâu ông sẽ mù." (no subtitles)
- From 3.0s onward, @Mai's face and lips stay clearly visible while speaking; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a shaky breath, the lamp buzzing softly, water dripping from the helmet onto the table. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 3 (`canh-04/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up with a slow push-in on Lâm's face; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam sits frozen at the table with the towel still in his hand, his mouth closed as he stares across at @Mai.
- 3.0–7.0s: @Lam slowly lifts his free hand and touches the corner of his cloudy left eye with his fingertips, his lips quivering but pressed shut.
- 7.0–10.0s: @Lam lowers his hand and looks at @Mai with wet shining eyes, while she stands soft in the background with her lips pressed together, hugging her own elbows. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm lặng người, hóa ra đứa cháu gái gánh khoản nợ ấy chỉ vì con mắt mờ đục của ông." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft sniff, the ticking of a wall clock, incense crackling on the altar. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 4 (`canh-04/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm over-the-shoulder shot from behind Mai onto Lâm with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam rises from the table, steps close to @Mai and speaks to her softly, his weathered face fully visible past her shoulder, his voice low and warm.
- 3.0–7.0s: @Lam finishes, closes his mouth and rests his rough hand gently on her shoulder, his narrow eyes soft and glistening in the lamplight.
- 7.0–10.0s: @Mai shakes her head hard, her shoulders trembling under the lavender hoodie, while @Lam keeps his hand on her shoulder and nods slowly. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.6s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mắt ông mù cũng được con ạ, chứ để con khổ thế này thì ông còn sống làm gì nữa." (no subtitles)
- @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a muffled sob, the lamp humming, a floorboard creaking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 5 (`canh-04/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot with a slow arc around the table; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Mai looks up at @Lam and speaks fast through her tears, her face clearly visible in the lamplight, holding up her phone with its blank glowing screen.
- 3.0–7.0s: @Mai finishes, closes her mouth and lowers the phone, her chin quivering as her eyes drop to the floor between them.
- 7.0–10.0s: @Mai sets the phone face-down on the wooden table, and @Lam lays his palm flat on top of it, his lips pressed together and his eyes steady on her. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.9s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mình trả không nổi đâu ông ơi, lãi mỗi ngày một tăng, bọn nó còn dọa gửi ảnh cháu cho cả lớp." (no subtitles)
- @Mai's face and lips stay clearly visible while speaking; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone buzzing once against wood, a shaky breath, the lamp humming. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 6 (`canh-04/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up with a slow push-in to his eyes; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The inside of the rolling steel shutter in warm lamplight, a thin line of red paint seeping under its bottom edge onto the tiled floor.
- 3.0–7.0s: @Lam steps into frame at the foot of the staircase, glances up the dark stairs with a soft tender look, then slowly turns his face toward the shutter.
- 7.0–10.0s: @Lam's eyes narrow and his jaw sets hard as he stares at the red-stained shutter, a steely glint rising in his gaze while his mouth stays firmly closed. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông xoa đầu cháu, rồi nhìn ra cánh cửa nhuộm đỏ, ánh mắt hiền lành ấy bỗng lạnh đi như thép." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: footsteps fading up the wooden stairs, a slow paint drip outside, a deep low hum swelling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 1 (`canh-05/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
- Extra: rows of young callers in headsets at glowing monitors
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 24mm wide shot with a slow overhead glide down the rows; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: A flashy call-center office high in a glass tower by day, purple and gold neon accent lights without letters glowing over long rows of desks and the bright city skyline beyond the glass.
- 3.0–7.0s: Rows of young callers in headsets hunch at their glowing blank monitors, typing fast and tapping their earpieces, every mouth closed as they stare at the bright screens.
- 7.0–10.0s: The camera glides to the far end of the room and settles on the empty glass-walled boss room, its white leather sofa and tall ring light glowing in the center. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trên tầng hai mươi lăm tòa nhà kính là công ty Phú Quý, nơi ba chục nhân viên gọi điện đòi nợ suốt ngày đêm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a hum of keyboards clattering, phones ringing on every desk, an air conditioner whirring. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 2 (`canh-05/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium tracking shot moving backward ahead of him; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: An empty aisle between rows of desks with glowing monitors, purple neon accent lights reflected on the polished floor and gold light flickering along the glass walls.
- 3.0–7.0s: @Hung strides down the aisle in his oversized black satin bomber jacket, holding a phone on a small selfie gimbal at arm's length and filming himself with a cocky closed-mouth grin.
- 7.0–10.0s: @Hung swings the gimbal around to film the room, winks at the lens and smooths his ash-blond undercut, his silver rings flashing under the neon, lips closed. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông chủ là Hưng, ba mươi mốt tuổi, ứng dụng vay tiền của hắn kiếm tiền tỷ mỗi tháng từ những sinh viên nghèo." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: white high-top sneakers squeaking on the polished floor, keyboards clattering, a gimbal motor whirring. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 3 (`canh-05/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm close-up with a slow pull-back; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Hung holds the phone on a small selfie gimbal close to his face and speaks loudly into it like a livestream salesman, grinning wide, his gold-rimmed glasses gleaming.
- 3.0–7.0s: @Hung finishes his pitch, closes his mouth and fans out a thick wad of banknotes beside his face with a smug wink at the phone.
- 7.0–10.0s: As the camera pulls back, @Hung poses with the gimbal held high in the purple and gold neon glow, lips closed in a cocky grin, the rows of desks behind him. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.2s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chào cả nhà, Hưng Phú Quý đây, vay nhanh năm phút, không cần thế chấp, tiền về liền tay!" (no subtitles)
- @Hung's face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a cash-counter flutter of banknotes, a cheerful notification chime, keyboards clattering. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 4 (`canh-05/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 3.0–7.0s: @Hung lounges on the white leather sofa on screen-left as @Beo stands before him on screen-right, rubbing his shaved head and reporting in a loud rough voice.
- 7.0–10.0s: @Beo finishes, closes his mouth and shrugs his heavy shoulders, while @Hung raises one eyebrow over his gold-rimmed glasses, his lips pressed together. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Beo (man of 28, strictly standard Hà Nội Northern accent (never Southern accent), rough loud bass, blustering, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Đại ca, con bé Mai có ông nội chạy xe ôm, lão già bảo sẽ trả nợ thay cháu." (no subtitles)
- From 3.0s onward, @Beo's face and lips stay clearly visible while speaking; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the glass door sliding shut, the ring light humming, muffled phones ringing outside the glass. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 5 (`canh-05/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on Hưng with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Hung lets out one short scoff, then leans forward on the sofa and speaks to @Beo with a mocking smirk, his face clearly visible in the ring light.
- 3.0–7.0s: @Hung finishes, closes his mouth and flicks his ringed fingers toward the door in a lazy wave, his gold-rimmed glasses catching the ring light.
- 7.0–10.0s: @Beo nods quickly at the edge of the frame and hurries out of the glass room, while @Hung sinks back into the white leather sofa, lips closed in a smug grin. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.7s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông già xe ôm à? Càng già càng sợ mất mặt, gửi ảnh con bé cho cả lớp nó xem đi." (no subtitles)
- @Hung's face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: leather creaking, silver rings clinking, heavy flip-flop footsteps hurrying away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 6 (`canh-05/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The glass-walled boss room high above the city, its ring light glowing and purple neon reflecting on the glass, the sunlit Hà Nội skyline shimmering beyond the windows.
- 3.0–7.0s: @Hung stands at the window in his black satin bomber jacket with his hands in his pockets, looking down at the city with one corner of his lip curled in a closed-mouth smirk.
- 7.0–10.0s: @Hung tilts his head and admires his own reflection in the glass as the camera pulls back, the busy streets far below looking tiny beneath him. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Hưng cười khẩy, hắn không biết mình vừa chọc vào tổ của một con rồng đã ngủ suốt ba mươi năm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft air conditioner hum, a faint lift chime, distant traffic far below. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 1 (`canh-06/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: @Lam wipes the dust off the lid with his palm in a soft grey cloud and rests the tin on his knees, his weathered thumbs on its rusty rim. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đêm ấy, ông Lâm lôi ra từ gầm giường một chiếc hộp bánh quy bằng sắt đã rỉ sét, ba mươi năm không mở." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: metal scraping across tiles, a soft puff of dust, the old bed frame creaking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 2 (`canh-06/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up over his hands with a slow push-in on the photo; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam pries open the squeaking lid of the rusty tin with his thumbs, revealing a nest of yellowed papers covered in faint unreadable lines.
- 3.0–7.0s: @Lam lifts out a faded photo of three young friends from the nineties, their faces tiny, arms slung over each other's shoulders on an old-quarter street.
- 7.0–10.0s: The camera holds close on the faded photo resting in his fingers, three tiny young figures with linked arms, as his thumb gently strokes its worn edge. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bên trong là một tấm ảnh cũ, ba người trẻ tuổi khoác vai nhau giữa phố cổ những năm chín mươi." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a rusty lid squeaking open, old paper rustling, a slow breath out through the nose. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 3 (`canh-06/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 100mm extreme close-up with a slow tracking glide along his forearm; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The worn wooden table under the warm lamp, a rusty round biscuit tin lying open beside the faded photo as a curl of incense smoke drifts through the golden light.
- 3.0–7.0s: @Lam's right forearm moves into the lamplight and his left hand slowly rolls the grey windbreaker sleeve up past his elbow, fold by fold.
- 7.0–10.0s: The full dark-green dragon tattoo is revealed coiling from wrist to elbow over his wrinkled skin, its scaled body, claws and whiskered head gleaming in the warm light as his fingers slowly curl closed. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông xắn tay áo lên, con rồng xanh sẫm trên cánh tay vẫn còn nguyên, chỉ có làn da là đã già đi." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: fabric rustling as a sleeve rolls up, a deep low boom, incense crackling softly. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 4 (`canh-06/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: @Lam finishes, closes his mouth and listens, the corner of his lips twitching upward as he holds the receiver against his ear. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.7s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Hoa đấy à? Lâm đây, mai gọi cả Khoa đến quán bà, Rồng cần Hổ với Báo rồi." (no subtitles)
- From 3.0s onward, @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the click of an old receiver lifting, a rotary dial whirring back, a faint line crackle. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 5 (`canh-06/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in Bà Hoa's bún chả shop after closing: plastic stools stacked, one warm bulb over a steel table, cold grills, the shutter half down, an old red landline phone on the counter.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 35mm wide shot with a slow push-in toward the counter; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: A bún chả shop after closing at night, plastic stools stacked high, cold grills on the pavement and the shutter half down, one warm bulb glowing over a steel table.
- 3.0–7.0s: On the counter, an old red landline phone sits with its receiver lifted off the cradle and lying on its side, the coiled cord still swaying gently in the bulb light.
- 7.0–10.0s: The camera settles close on the red receiver resting on the counter beside a woven bamboo fan, the warm bulb swaying slowly overhead and nobody in sight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ở đầu dây bên kia, có một tiếng cười khàn khàn vang lên, như thể người ấy đã chờ cuộc gọi này suốt ba mươi năm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a raspy woman's low chuckle from somewhere just out of sight, the bulb buzzing, a cord swinging against the counter. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 6 (`canh-06/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The worn wooden table under the warm lamp, a battered green pith helmet resting beside the open rusty biscuit tin and the hung-up cream landline phone.
- 3.0–7.0s: @Lam picks up the battered green pith helmet and settles it firmly on his grey crew cut, tilting the brim down over his eyes with two fingers.
- 7.0–10.0s: @Lam raises his eyes from under the brim and slowly breaks into a sly closed-mouth smile, one thick grey eyebrow lifting, the lamplight glinting in his narrow eyes. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm đội lại chiếc mũ cối, và lần đầu sau ba mươi năm, ông mỉm cười kiểu của Lâm Rồng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a helmet strap clicking, a deep low boom, the lamp humming warmly. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 1 (`canh-07/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
- Extra: a long line of customers waiting on the pavement
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 24mm wide shot with a slow crane-up through the smoke; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Rows of grilled pork patties sizzle and spit over glowing charcoal on the pavement, thick white smoke billowing up through warm sunlight beside baskets of fresh herbs.
- 3.0–7.0s: The camera rises through the smoke over low plastic stools and steel tables, the golden light catching the swirling haze under the shop awnings.
- 7.0–10.0s: The view opens onto a long line of customers waiting along the pavement to the end of the alley, fanning themselves and craning toward the grills with their mouths closed. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trưa hôm sau, quán bún chả đông nhất phố Hàng Mành khói bay mù mịt, khách xếp hàng dài tận đầu ngõ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pork sizzling over charcoal, a bamboo fan whooshing, chopsticks clinking on bowls, the low hum of a busy street. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 2 (`canh-07/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A row of charcoal grills smoking on the pavement in warm sunlight, pork patties sizzling on wire racks and a woven bamboo fan resting on a stool.
- 3.0–7.0s: @BaHoa steps up to the grills in her purple floral silk blouse and fans the glowing charcoal briskly with the woven bamboo fan, orange sparks dancing up through the smoke.
- 7.0–10.0s: @BaHoa glances at the camera through the smoke, her red lips closed in a knowing curve, and gives a slow sly wink as her gold hoop earrings swing. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bà chủ là Hoa, sáu mươi mốt tuổi, ba mươi năm trước là bộ não của cả băng, giang hồ gọi là Hoa Hổ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal crackling, a bamboo fan whooshing in quick strokes, fat sizzling, gold bangles jangling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 3 (`canh-07/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 40mm over-the-shoulder shot past Lâm onto Bà Hoa with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A smoky charcoal grill on the pavement in noon sunlight, pork patties sizzling beside a steel table with a basket of herbs and two low plastic stools.
- 3.0–7.0s: @Lam steps up to the grill holding his battered green pith helmet under one arm, and @BaHoa looks up from the smoke and speaks to him teasingly, one eyebrow arched.
- 7.0–10.0s: @BaHoa finishes, closes her red lips into a smirk and props one hand on her hip, the bamboo fan resting on her shoulder as @Lam scratches the back of his neck. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ba mươi năm không thấy mặt, nay ông đến ăn bún chả hay đến rủ tôi đi tù đấy?" (no subtitles)
- From 3.0s onward, @BaHoa's face and lips stay clearly visible while speaking; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pork sizzling, charcoal popping, a motorbike horn on the street. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 4 (`canh-07/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on Lâm with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam leans toward @BaHoa over the smoking grill and speaks in a low conspiratorial voice, his narrow eyes twinkling under his thick grey eyebrows.
- 3.0–7.0s: @Lam finishes, closes his mouth and raises his eyebrows meaningfully, tapping the edge of the steel table twice with one finger.
- 7.0–10.0s: @BaHoa, soft in the foreground, stops fanning mid-stroke, while @Lam holds her gaze with a calm closed-mouth half-smile through the drifting smoke. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.1s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Rủ bà đi lừa một thằng chuyên lừa đảo, lần này mình làm việc thiện, bà Hoa ạ." (no subtitles)
- @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: two light taps on a steel table, charcoal crackling, the fan going quiet. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 5 (`canh-07/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium two-shot with a slow arc around the grill; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @BaHoa snaps the bamboo fan shut, points it at @Lam and speaks fast and bold, her red lips moving clearly and her gold bangle jangling.
- 3.0–7.0s: @BaHoa finishes, closes her mouth in a wide red-lipped grin and nudges a low plastic stool toward him with the toe of her sandal.
- 7.0–10.0s: @Lam sits down on the low plastic stool with a closed-mouth grin, as @BaHoa flips a pork patty on the grill with long chopsticks, her eyes sparkling. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.4s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Lừa người tốt thì tôi giải nghệ rồi, nhưng lừa thằng lừa đảo thì tôi đi ngay, ông ngồi đi!" (no subtitles)
- @BaHoa's face and lips stay clearly visible while speaking; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a bamboo fan snapping shut, a plastic stool scraping on the pavement, a fresh burst of sizzling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 6 (`canh-07/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up with a slow push-in on the mirror; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A small round hand mirror propped against an unlabeled glass jar on the steel counter, a gold lipstick tube lying beside it in the smoky sunlight.
- 3.0–7.0s: @BaHoa unties the checkered apron from her waist and hangs it on a hook, then leans toward the small mirror with the gold lipstick tube in hand.
- 7.0–10.0s: @BaHoa paints her closed lips a fresh bold red, presses them together, and her reflected eyes narrow into a razor-sharp gleaming look in the little mirror. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–4.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bà Hoa tháo tạp dề, tô lại son, ánh mắt sắc lẹm ngày nào đã quay trở lại." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a lipstick cap clicking off, apron strings rustling, the grill crackling behind. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 1 (`canh-08/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 28mm wide shot with a slow dolly-in under the staircase; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A tiny repair stall tucked under a staircase in an old-quarter alley, shelves crammed with old radios and phones, tangled wires hanging down and a single bare bulb glowing.
- 3.0–7.0s: @Khoa hunches over the cluttered workbench in his brown multi-pocket vest, a soldering iron in hand and a thin curl of smoke rising from a circuit board under the magnifier lamp.
- 7.0–10.0s: @Khoa sets down the soldering iron and lifts the circuit board to the light, squinting at it with his lips pursed shut as his small grey ponytail bobs. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Người thứ ba là Khoa, sáu mươi tuổi, sửa đài sửa điện thoại dưới gầm cầu thang, giang hồ gọi là Khoa Báo." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soldering iron hissing, an old radio crackling softly on a shelf, a fan rattling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 2 (`canh-08/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tiny electronics repair stall tucked under a staircase in an old-quarter alley: shelves of old radios and phones, tangled wires, a soldering iron, a magnifier lamp, a single bare bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 100mm extreme close-up on his hands with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Khoa picks up a locked old smartphone and slides a tiny steel pick into its edge, his long bony fingers moving with delicate precision under the magnifier lamp.
- 3.0–7.0s: His fingers flick and twist the tiny tools in a blur of speed until, with a soft click, the back panel pops open and the blank screen lights up with a plain glow.
- 7.0–10.0s: @Khoa sets the opened phone down and dusts off his fingertips, his lips curled in a smug closed-mouth smile under the bright magnifier lamp. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngày xưa, chưa có cái két sắt nào ở phố cổ giữ được bí mật quá năm phút trước đôi tay của ông." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: tiny metallic clicks and scrapes, a crisp final click, a soft startup chime. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 3 (`canh-08/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 3.0–7.0s: @Lam ducks under the low staircase into the stall on screen-right, and @Khoa looks up from the workbench on screen-left and speaks to him in a dry nasal deadpan.
- 7.0–10.0s: @Khoa finishes, closes his mouth and leans back on his stool, folding his arms over his vest while @Lam takes off his battered green pith helmet. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Khoa (man of 60, strictly standard Hà Nội Northern accent (never Southern accent), nasal wry tenor, deadpan and fussy, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Rồng với Hổ cùng tìm đến tận gầm cầu thang này, chắc phố cổ sắp có chuyện lớn rồi." (no subtitles)
- From 3.0s onward, @Khoa's face and lips stay clearly visible while speaking; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: footsteps on the stairs above, the bare bulb buzzing, a radio crackling low. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 4 (`canh-08/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tiny electronics repair stall tucked under a staircase in an old-quarter alley: shelves of old radios and phones, tangled wires, a soldering iron, a magnifier lamp, a single bare bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on Lâm with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam sets a locked phone with a dark blank screen on the workbench and speaks to @Khoa in a calm low voice, his face clearly visible under the bare bulb.
- 3.0–7.0s: @Lam finishes, closes his mouth and slides the phone across the bench toward @Khoa with two fingers, one grey eyebrow raised in a playful challenge.
- 7.0–10.0s: @Lam rests his hands on the bench and waits, a faint closed-mouth smile at the corner of his lips as the bare bulb sways gently above them. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.6s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Có một cái két sắt làm bằng điện thoại cần mở, tay ông Khoa bây giờ còn mở được không?" (no subtitles)
- @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone sliding across a wooden bench, the bulb buzzing, a radio crackling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 5 (`canh-08/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 40mm over-the-shoulder shot past Lâm onto Khoa with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Khoa picks up the phone, weighs it in his palm with a scoff and speaks in a wry deadpan, his face clearly visible past @Lam's shoulder.
- 3.0–7.0s: @Khoa finishes, closes his mouth and wiggles his eyebrows, while @Lam's shoulders shake with silent laughter in the foreground.
- 7.0–10.0s: @Khoa spins the phone once on the workbench with one finger and stops it flat under his palm, his lips pressed into a cheeky little smirk. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.2s, spoken on camera by @Khoa (man of 60, strictly standard Hà Nội Northern accent (never Southern accent), nasal wry tenor, deadpan and fussy, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Két nào tôi cũng mở được hết, trừ mỗi cái két trái tim của bà Hoa là chịu thôi." (no subtitles)
- @Khoa's face and lips stay clearly visible while speaking; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone spinning on wood, a soft wheeze of laughter, the bulb buzzing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 6 (`canh-08/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The cluttered workbench under the magnifier lamp, a row of tiny screwdrivers and picks laid out neatly beside a locked phone with a dark blank screen.
- 3.0–7.0s: @Khoa leans in and pulls his thick magnifier glasses down from his forehead onto his eyes, which swell huge and bright behind the lenses, his mouth closed.
- 7.0–10.0s: @Khoa lifts his long bony hands over the tools and they quiver with eager little twitches as he wiggles his fingers like a boy, grinning with closed lips. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Khoa kéo cặp kính lúp xuống mắt, và lần đầu sau ba mươi năm, đôi bàn tay ấy lại run lên vì háo hức." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: glasses clicking into place, tiny tools rattling on the bench, an old radio crackling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 1 (`canh-09/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: The low camera holds as the three silhouettes stride on side by side toward the glowing end of the street, shoulders squared, a pith helmet outline on the one in the middle. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ba mươi năm sau, bộ ba Rồng, Hổ, Báo lại sóng bước trên phố cổ, chậm rãi mà oai như ngày nào." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: three pairs of slow footsteps in unison on wet pavement, the buzz of neon signs, distant motorbike horns. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 2 (`canh-09/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in Bà Hoa's bún chả shop after closing: plastic stools stacked, one warm bulb over a steel table, cold grills, the shutter half down, an old red landline phone on the counter.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the closed bún chả shop at night, one warm bulb glows over a steel table where an open laptop casts a cool blue light beside stacked plastic stools.
- 3.0–7.0s: @Mai sits at the steel table with the glowing laptop turned away from the camera and speaks quickly and earnestly, her face lit blue and her round glasses reflecting the light.
- 7.0–10.0s: @Mai finishes, closes her mouth and taps the edge of the laptop firmly with one finger, her jaw set and her eyes bright behind her glasses. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.5s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ứng dụng này lấy cả danh bạ với ảnh của người vay, hàng nghìn sinh viên đang bị nó siết như cháu." (no subtitles)
- From 3.0s onward, @Mai's face and lips stay clearly visible while speaking; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the laptop fan whirring, the bulb buzzing, a motorbike passing outside the half-down shutter. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 3 (`canh-09/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in Bà Hoa's bún chả shop after closing: plastic stools stacked, one warm bulb over a steel table, cold grills, the shutter half down, an old red landline phone on the counter.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 40mm over-the-shoulder shot past Lâm onto Bà Hoa with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The steel table under the single warm bulb in the closed shop, cold grills behind it, two small cups of steaming tea and a plate of peanuts waiting.
- 3.0–7.0s: @BaHoa sits across from @Lam, slips on a pair of big black sunglasses and speaks with grand haughty gestures, her red lips moving clearly in the bulb light.
- 7.0–10.0s: @BaHoa finishes, closes her mouth and lifts her chin like a tycoon, fanning herself slowly with the bamboo fan as @Lam nods along. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Tôi sẽ đóng vai bà trùm bất động sản, mang mười tỷ đến xin đầu tư vào công ty nó." (no subtitles)
- From 3.0s onward, @BaHoa's face and lips stay clearly visible while speaking; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: tea being poured, a bamboo fan fluttering, a gold bangle clinking on steel. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 4 (`canh-09/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in Bà Hoa's bún chả shop after closing: plastic stools stacked, one warm bulb over a steel table, cold grills, the shutter half down, an old red landline phone on the counter.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on Lâm with a slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam leans over the steel table and speaks briskly to @BaHoa, counting off each role on his fingers, his face clearly visible in the warm bulb light.
- 3.0–7.0s: @Lam finishes the last count, closes his mouth and lays his flat hand on the table like a card dealer, his narrow eyes glinting.
- 7.0–10.0s: @BaHoa lowers her sunglasses in the soft background and nods once, while @Lam leans back on his stool with a satisfied closed-mouth smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.1s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Tôi làm tài xế cho bà, ông Khoa lo cái máy ghi hình, còn con Mai ngồi ngoài xe giữ đường dây." (no subtitles)
- @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a palm laid flat on a steel table, teacups clinking, the bulb humming. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 5 (`canh-09/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in Bà Hoa's bún chả shop after closing: plastic stools stacked, one warm bulb over a steel table, cold grills, the shutter half down, an old red landline phone on the counter.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot with a slow push-in on the brooch; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The steel table under the warm bulb, a small open velvet box and a tiny screwdriver lying beside a tangle of thin copper wires.
- 3.0–7.0s: @Khoa holds up a large gold flower brooch with a tiny hidden camera between two fingers, lets it sparkle in the bulb light and speaks in a dry deadpan.
- 7.0–10.0s: @Khoa finishes, closes his mouth and taps the center of the brooch where a tiny lens glints, then raises his eyebrows above his magnifier glasses. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Khoa (man of 60, strictly standard Hà Nội Northern accent (never Southern accent), nasal wry tenor, deadpan and fussy, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cái trâm cài áo này có mắt, nó nói câu nào là cả nước nghe câu ấy." (no subtitles)
- From 3.0s onward, @Khoa's face and lips stay clearly visible while speaking; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a velvet box snapping shut, a tiny electronic beep, the bulb buzzing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 6 (`canh-09/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The closed bún chả shop at night glows warm under its single bulb, stacked plastic stools, cold grills and the half-down shutter framing the steel table.
- 3.0–7.0s: @Lam sits at the steel table shaking with silent laughter, eyes crinkled and mouth closed, wiping the corner of his eye with a knuckle while @Mai watches beside him.
- 7.0–10.0s: @Mai straightens her round glasses and breaks into a slow closed-mouth smile, gazing at her grandfather as the camera pulls back over the glowing little shop. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Mai nhìn ba người già cười rộn ràng như trẻ con, và cô biết, phố cổ sắp có một phi vụ để đời." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: warm chuckling from just out of frame, teacups clinking, crickets outside the half-down shutter. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 1 (`canh-10/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning outside the marble lobby of a gleaming Hà Nội glass tower: a revolving door, potted palms, polished stone steps reflecting the light.

[CHARACTERS]
- Extra: two security guards in grey uniforms standing straight by the door
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 24mm wide low-angle shot, slow crane-down from the tower facade to the steps; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: The gleaming glass tower rises into a crisp blue morning sky, sunlight flashing across its mirrored windows high above the marble lobby and the revolving door.
- 3.0–7.0s: A black luxury sedan with no badge glides up and stops at the foot of the polished stone steps, its mirror-black paint reflecting the potted palms.
- 7.0–10.0s: At the top of the steps the two security guards in grey uniforms snap upright beside the revolving door, chins raised, hands flat at their sides, eyes fixed on the car. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Sáng thứ Hai, một chiếc xe sang màu đen đỗ xịch trước tòa nhà kính, cả dãy bảo vệ vội vàng đứng thẳng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a smooth engine purring to a stop, tires whispering on stone, a revolving door turning softly, distant city traffic. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 2 (`canh-10/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning outside the marble lobby of a gleaming Hà Nội glass tower: a revolving door, potted palms, polished stone steps reflecting the light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, slow dolly-in toward the driver's door; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The driver's side of the black luxury sedan with no badge gleams beside the polished stone steps, morning sun sliding across its dark windows and chrome handle.
- 3.0–7.0s: The driver's door swings open and @Lam steps out wearing a crisp black chauffeur cap instead of his usual helmet, smoothing his grey windbreaker with one hand.
- 7.0–10.0s: @Lam marches around the gleaming hood with stiff formal steps and opens the rear door with a deep, precise bow, his lips pressed into a straight line. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Người cầm lái là ông Lâm, mũ cối được thay bằng mũ tài xế, bước xuống mở cửa xe rất đúng điệu." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a car door clicking open, crisp footsteps on stone, a soft breeze through the potted palms. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 3 (`canh-10/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The open rear door of the black luxury sedan with no badge frames a slice of cream leather seat, sunlight glinting on the polished stone step below.
- 3.0–7.0s: @BaHoa steps out and rises tall in big black sunglasses and a wide-brimmed black hat, a large gold flower brooch with a tiny hidden camera shining on her chest.
- 7.0–10.0s: @BaHoa lifts her chin, slowly lowers her sunglasses with one finger and gazes up at the tower, red lips closed in a regal half smile. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bà Hoa bước ra, kính đen, mũ rộng vành, trâm vàng trước ngực, sang trọng như một bà trùm bất động sản thật." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heeled sandals tapping on stone, a gold bangle clinking, a car door thudding shut. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 4 (`canh-10/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 3.0–7.0s: @BaHoa, in big black sunglasses and a wide-brimmed black hat, turns to @Lam and wags one finger at the car, speaking in a brassy commanding voice.
- 7.0–10.0s: @BaHoa closes her red lips and sweeps away toward the lobby, while @Lam, in his black chauffeur cap, bows low with both hands at his sides. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Lái xe đâu, đỗ cho cẩn thận, xước một vết sơn là trừ một năm lương đấy nhé!" (no subtitles)
- From 3.0s onward, @BaHoa's face and lips stay clearly visible while speaking; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a gold bangle clinking, a soft breeze in the palms, a distant car horn, the revolving door turning. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 5 (`canh-10/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning outside the marble lobby of a gleaming Hà Nội glass tower: a revolving door, potted palms, polished stone steps reflecting the light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow push-in on his face; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Close on the gleaming black hood of the luxury sedan with no badge, the revolving door and potted palms reflected and swaying across the polished paint.
- 3.0–7.0s: @Lam, in his black chauffeur cap, bows his head politely beside the open car door, eyes lowered humbly to the polished stone steps.
- 7.0–10.0s: One corner of @Lam's mouth curls into a tiny hidden smile with lips closed, his narrow eyes glinting under the cap's brim as he glances sideways toward the lobby. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm cúi đầu dạ vâng, khóe miệng giấu một nụ cười, bà Hoa diễn còn hay hơn ba mươi năm trước." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: fading heel taps, the revolving door swishing, a sparrow chirping in the palms. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 6 (`canh-10/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: @Khoa raises a slow thumbs-up without looking away while @Mai nods quickly, both with lips pressed together and eyes locked on the glowing screens. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trong chiếc xe tải trắng bên kia đường, Mai và ông Khoa dán mắt vào hai chiếc máy tính đang sáng đèn." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: laptop fans humming, muffled street traffic, a faint crackle in a headset. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 1 (`canh-11/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: Inside the glass-walled boss room, a ring light glows beside a white leather sofa while purple and gold neon accent lights shimmer across the glass.
- 3.0–7.0s: @Hung lowers a phone on a small selfie gimbal, taps it to end his livestream and tugs the collar of his black satin bomber jacket straight.
- 7.0–10.0s: @Hung checks his ash-blond undercut in the dark glass, flashes a cocky closed-lip grin and strides briskly toward the glass door. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Nghe có bà trùm mang mười tỷ đến, Hưng tắt livestream, chỉnh lại cổ áo, ra tận cửa đón." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft chime as the livestream ends, phones ringing across the call center, quick sneaker steps. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 2 (`canh-11/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm over-the-shoulder shot past @Hung onto her, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The white leather sofa in the glass-walled boss room sits empty under the glowing ring light, a tea tray with two glasses on the low table.
- 3.0–7.0s: @BaHoa sits on the white sofa in her wide-brimmed black hat and big sunglasses and speaks to @Hung with a lazy wave of her hand, a large gold flower brooch with a tiny hidden camera on her chest.
- 7.0–10.0s: @BaHoa closes her red lips and leans back, while @Hung, standing opposite, rubs his silver-ringed fingers together with a hungry grin. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Tôi có mười tỷ để không trong ngân hàng, nghe nói cậu làm tiền đẻ ra tiền nhanh lắm." (no subtitles)
- From 3.0s onward, @BaHoa's face and lips stay clearly visible while speaking; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft creak of leather, distant phones ringing, a glass clinking on the tray. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 3 (`canh-11/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot, slow arc around the sofa; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Hung perches on the arm of a chair facing @BaHoa and starts speaking eagerly, spreading his hands wide as his silver rings flash under the ring light.
- 3.0–7.0s: @Hung keeps talking fast and leans forward, holding up ten fingers and then sweeping them upward, his round gold-rimmed glasses catching the neon.
- 7.0–10.0s: @Hung finishes and closes his mouth into a smug grin, while @BaHoa tilts her hat brim and studies him through her dark sunglasses. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.9s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bà gửi tôi mười tỷ, ba tháng sau tôi trả bà hai mươi, sinh viên bây giờ dễ vay lắm bà ạ." (no subtitles)
- @Hung's face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: leather creaking, an air conditioner humming, muffled ringing phones. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 4 (`canh-11/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on her, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @BaHoa lowers her sunglasses an inch and speaks to @Hung in a teasing brassy voice, one eyebrow arched high above the dark lenses.
- 3.0–7.0s: @BaHoa keeps speaking while tapping her chunky gold bangle on the sofa arm, the large gold flower brooch with a tiny hidden camera glinting on her chest.
- 7.0–10.0s: @BaHoa closes her red lips and waits with her head tilted, as @Hung's shoulder at the edge of the frame leans in toward her. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–4.7s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Dễ vay thì cũng phải trả chứ, nhỡ chúng nó không trả thì cậu làm thế nào?" (no subtitles)
- @BaHoa's face and lips stay clearly visible while speaking; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a gold bangle tapping on leather, the ring light humming, distant keyboards clicking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 5 (`canh-11/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot on him, slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Hung speaks to @BaHoa with a careless shrug, lifting a phone on a small selfie gimbal and waggling it in the air beside his face.
- 3.0–7.0s: @Hung keeps speaking smugly, tapping the phone's blank glowing screen with a ringed finger as if sending photos, his cocky grin widening.
- 7.0–10.0s: @Hung closes his mouth and leans back in his chair with arms folded, while @BaHoa nods slowly across from him, lips closed. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.7s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Không trả thì tôi gửi ảnh cho cả họ hàng nó, xấu hổ quá thì kiểu gì nó cũng phải trả." (no subtitles)
- @Hung's face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone buzzing, leather creaking, a soft electronic hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 6 (`canh-11/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: Neon light ripples across the glass wall of the boss room, the glowing ring light and the white leather sofa softly out of focus.
- 3.0–7.0s: @BaHoa nods slowly in her wide-brimmed black hat, her fingertips stroking the large gold flower brooch with a tiny hidden camera on her chest.
- 7.0–10.0s: The camera settles on the gold brooch as a tiny lens at its center glints, @BaHoa's red lips closed in a satisfied curve just above it. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bà Hoa gật gù, ngón tay khẽ vuốt chiếc trâm vàng, từng lời của Hưng đang chạy thẳng về máy của Mai." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint electronic click, the soft ring light hum, muffled chatter of the call center. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 1 (`canh-12/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A bright corporate hallway in the glass tower with grey carpet and frosted glass walls.

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
- 3.0–7.0s: @Khoa ambles into view wearing a blue technician cap over his grey ponytail and carrying a toolbox, his brown multi-pocket vest bristling with little tools.
- 7.0–10.0s: @Khoa strolls on with a loose, bored gait, lips pressed together, swinging the toolbox like any ordinary repairman on his daily rounds. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cùng lúc ấy, ông Khoa trong bộ đồ thợ sửa điều hòa lững thững đi dọc hành lang, chẳng ai buồn để ý." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft footsteps on carpet, the hum of ceiling lights, a distant elevator chime. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 2 (`canh-12/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm close-up on the keypad, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A glass door with a keypad lock of blank buttons glows with a small red light, tall black server racks blinking blue behind the glass.
- 3.0–7.0s: @Khoa kneels by the keypad lock, slides a bent hairpin into a tiny slot beneath it and twists it gently with his long thin fingers.
- 7.0–10.0s: The small red light flips to green with a click, and @Khoa raises his eyebrows with lips pressed together as the glass door eases open. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ổ khóa điện tử của phòng máy chủ, ông chỉ cần ba giây và một chiếc kẹp tóc bẻ cong là xong." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint metallic scratch, a crisp electronic beep, the hiss of a door seal releasing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 3 (`canh-12/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium shot, slow dolly-in following him inside; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Khoa steps into the cold server room, holds the bent hairpin up to the blue light and mutters to himself with a dry little smirk.
- 3.0–7.0s: @Khoa keeps muttering as he wiggles his steady fingers in the air, then tucks the hairpin into a vest pocket.
- 7.0–10.0s: @Khoa closes his mouth, pats the vest pocket twice and turns toward the tall black server racks with blinking blue lights. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.2s, spoken on camera by @Khoa (man of 60, strictly standard Hà Nội Northern accent (never Southern accent), nasal wry tenor, deadpan and fussy, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ba mươi năm rồi mà tay vẫn chưa run, cái khóa này còn dễ hơn két sắt ngày xưa." (no subtitles)
- @Khoa's face and lips stay clearly visible while speaking; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the loud hum of the air conditioner, cooling fans whirring, a soft door click behind. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 4 (`canh-12/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: @Khoa crouches before a server rack and lowers his magnifier glasses over his eyes, the blinking blue lights reflecting in the thick lenses.
- 3.0–7.0s: @Khoa's long fingers slide a small black hard drive into a port on the rack, and a row of tiny blue lights starts blinking faster.
- 7.0–10.0s: @Khoa sits back on his heels with lips pressed together, watching the lights race across the drive as the data streams in. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông cắm một chiếc ổ cứng nhỏ màu đen vào giá máy, toàn bộ dữ liệu đòi nợ bắt đầu chảy về." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft plastic click, cooling fans rising in pitch, rapid electronic chirps. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 5 (`canh-12/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 40mm medium shot, slow push-in across the laptops; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Two laptops glow brightly inside the parked white van, tangled cables and a thermos on the narrow shelf, the tinted windows dimming the busy street.
- 3.0–7.0s: @Mai leans toward the glowing laptops with a small headset microphone at her cheek and speaks quickly, eyes wide behind her round black-framed glasses.
- 7.0–10.0s: @Mai finishes, closes her mouth and presses both hands flat on the shelf, staring at the screens as their glow flickers faster. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông Khoa ơi, dữ liệu về đủ rồi, cả danh sách mấy nghìn sinh viên bị nó siết nợ!" (no subtitles)
- From 3.0s onward, @Mai's face and lips stay clearly visible while speaking; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: laptop fans whirring, rapid keyboard taps, muffled street traffic. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 6 (`canh-12/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Inside a parked white van turned into a surveillance post by day: two laptops glowing, tangled cables, a thermos, tinted windows facing a busy street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow push-in on her face; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Mai sits back from the glowing laptops and squeezes her hands together tightly in her lap, her lips pressed shut.
- 3.0–7.0s: @Mai's eyes glisten behind her round glasses and she blinks hard as one tear slides down her cheek in the soft laptop glow.
- 7.0–10.0s: @Mai lets out a long slow breath, and a small closed-lip smile lifts her face as she straightens up in her lavender hoodie. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Mai nắm chặt tay, mắt rưng rưng, lần đầu tiên sau ba tháng, cô thấy mình không còn đơn độc." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet exhale, laptop fans humming, a faint distant motorbike horn. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 1 (`canh-13/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A dim underground car park with concrete pillars and fluorescent strip lights, a black luxury sedan with no badge parked.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, slow push-in toward the pillar; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Fluorescent strip lights flicker over rows of concrete pillars in the dim underground car park, the black luxury sedan with no badge parked in a far bay.
- 3.0–7.0s: @Beo peeks out from behind a thick concrete pillar, the lightning-bolt pattern on his shaved head catching the light as his small eyes squint toward the sedan.
- 7.0–10.0s: @Beo's small eyes go wide and his jaw tightens with lips pressed shut, then he slips back behind the pillar and slowly pulls out his phone. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Nhưng dưới hầm xe, Béo vô tình thấy gã tài xế già xắn tay áo, để lộ hình con rồng xanh sẫm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: fluorescent lights buzzing, a distant car door closing, echoing water drips. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 2 (`canh-13/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm over-the-shoulder shot past @Hung onto @Beo, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The glass-walled boss room glows with purple and gold neon, the ring light and white leather sofa standing before rows of glowing desks beyond the glass.
- 3.0–7.0s: @Beo leans in toward @Hung and speaks in a rough low voice, tapping his own thick right forearm with two fingers.
- 7.0–10.0s: @Beo closes his mouth and raises his eyebrows, while @Hung slowly lowers a phone on a small selfie gimbal and turns his head. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Beo (man of 28, strictly standard Hà Nội Northern accent (never Southern accent), rough loud bass, blustering, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Đại ca, lão tài xế kia có hình xăm con rồng, thằng em thấy quen quen lắm." (no subtitles)
- From 3.0s onward, @Beo's face and lips stay clearly visible while speaking; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the ring light humming, a muffled phone ringing, a chair creaking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 3 (`canh-13/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on @Hung, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Hung turns to @Beo and speaks with a short mocking laugh in his voice, one eyebrow arched above his round gold-rimmed glasses.
- 3.0–7.0s: @Hung keeps talking, flicking a ringed hand dismissively toward the call center beyond the glass, his cocky grin spreading wide under the neon.
- 7.0–10.0s: @Hung stops and closes his mouth, his eyes narrowing behind the glasses as he taps the gimbal handle slowly against his palm. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.4s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Lâm Rồng à? Bố tao kể về lão suốt, hóa ra giờ đi lái xe thuê cho một bà già." (no subtitles)
- @Hung's face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a short mocking laugh, the hum of the air conditioner, distant ringing phones. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 4 (`canh-13/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: @Hung looks up with a slow closed-lip smile, snaps the folder shut and sets a fountain pen neatly on top of it like a winning chess move. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Hưng không nổi giận, hắn mỉm cười, quyết định chơi lại bộ ba già bằng chính luật chơi của họ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper rustling, a folder snapping shut, the soft hum of neon. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 5 (`canh-13/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, slow arc around the desk; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Hung taps the closed folder and speaks over his shoulder in a slick low voice, eyes glinting behind his round gold-rimmed glasses.
- 3.0–7.0s: @Hung keeps speaking as he picks up the fountain pen and mimes signing with a flourish in the air, his silver rings flashing.
- 7.0–10.0s: @Hung closes his mouth into a smug grin and drops the pen back onto the folder with a light click. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.7s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cứ để bà ta ký hợp đồng đầu tư, rồi tao báo công an bắt cả lũ về tội lừa đảo." (no subtitles)
- @Hung's face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a pen clicking on the folder, the ring light humming, faint ringing phones. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 6 (`canh-13/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- Extra: three debt collectors in black following him
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide shot, slow tracking behind him; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Sunlight pours through the tall windows of the call center high in the glass tower, the busy street far below dotted with tiny traffic and a small white van.
- 3.0–7.0s: @Beo stands at the window looking down at the tiny white van across the street, nods once with lips pressed together and rolls his thick shoulders.
- 7.0–10.0s: @Beo turns and walks off between the rows of glowing desks as three debt collectors in black fall into step behind him, quiet and purposeful. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Béo gật đầu, lẳng lặng dẫn ba đàn em đi về phía chiếc xe tải trắng bên kia đường." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heavy flip-flop steps, a glass door swinging, ringing phones fading. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 1 (`canh-14/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 3.0–7.0s: @Mai unplugs the small black hard drive and hugs it to her chest as the side door of the van slides open, flooding the van with noon light.
- 7.0–10.0s: @Beo stands blocking the open doorway with his arms folded across his big chest, his lips pressed into a smug line, the sunny street bright behind him. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Mai vừa rút ổ cứng khỏi máy tính thì cửa xe tải trượt mở, Béo đã đứng chắn ngay bên ngoài." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a cable clicking free, the van door sliding open with a rattle, street horns pouring in. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 2 (`canh-14/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Noon on a busy old-quarter street near the railway: honking motorbikes, street vendors, shop awnings, a white van parked at the curb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, fast handheld tracking alongside her; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Honking motorbikes stream along the sunny old-quarter street past shop awnings and street vendors' carts, the white van parked at the curb with its far-side door shut.
- 3.0–7.0s: The far-side door of the van slides open and @Mai slips out, clutching a small black hard drive against her lavender hoodie, her backpack bouncing.
- 7.0–10.0s: @Mai runs at full speed along the crowded pavement under the shop awnings, ducking past a parked fruit cart while the river of motorbikes flows on the road beside her. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cô ôm chặt ổ cứng, chui ra cửa bên kia, chạy thục mạng giữa dòng xe máy đông nghịt." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: quick sneaker footsteps, a chorus of honking horns, a vendor's bell ringing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 3 (`canh-14/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Noon on a busy old-quarter street near the railway: honking motorbikes, street vendors, shop awnings, a white van parked at the curb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide low-angle shot, slow push-in as the bike arrives; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The busy noon street fills the frame from a low angle, motorbikes streaming under shop awnings and tangled wires as a familiar horn beeps somewhere in the traffic.
- 3.0–7.0s: @Lam rides the old cream-colored step-through motorbike with a round chrome headlamp, weaving smoothly between the motorbikes in his battered green pith helmet.
- 7.0–10.0s: @Lam glides out of the traffic and brakes to a neat stop at the curb facing the camera, one sandal on the ground, lips closed in a calm half smile. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Một tiếng còi quen thuộc vang lên, ông Lâm phóng chiếc xe máy cũ tới, phanh xịch ngay trước mặt cháu." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a cheerful little horn beeping twice, a puttering old engine, brakes squeaking softly. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 4 (`canh-14/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Noon on a busy old-quarter street near the railway: honking motorbikes, street vendors, shop awnings, a white van parked at the curb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, slow pull-back from the headlamp; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Close on the round chrome headlamp of the old cream-colored step-through motorbike idling at the curb, honking traffic blurring past behind it.
- 3.0–7.0s: As the camera eases back, @Lam sits astride the seat and turns his head to @Mai climbing on behind him, speaking firmly with a sly glint in his eye.
- 7.0–10.0s: @Lam closes his mouth and twists the throttle as @Mai wraps both arms around his waist, the small black hard drive tucked safely between them. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.9s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Lên xe ôm chặt vào, Mai, hôm nay ông cho con biết thế nào là chạy xe phố cổ!" (no subtitles)
- From 3.0s onward, @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a puttering engine revving, traffic horns, a street vendor calling in the distance. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 5 (`canh-14/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: From above, the narrow old-quarter streets twist like a maze between tiled roofs, tangled wires and shop awnings, dense rivers of motorbikes glittering under the noon sun.
- 3.0–7.0s: Four debt collectors on black motorbikes weave through the traffic in a tight line, revving as they slip between slower motorbikes and street carts.
- 7.0–10.0s: The four black motorbikes lean into a sharp turn one after another and vanish into an even narrower street hung with laundry. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bốn chiếc xe máy đen lập tức bám đuổi, rú ga len lỏi giữa những con phố chật như ruột gà." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: engines revving and whining, a chorus of horns, echoes bouncing between the houses. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 6 (`canh-14/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Noon on a busy old-quarter street near the railway: honking motorbikes, street vendors, shop awnings, a white van parked at the curb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium tracking shot, slow pan following the turn; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A street corner opens onto a narrow lane where railway tracks run between old tube houses, laundry swaying and café stools lined against the walls.
- 3.0–7.0s: @Lam leans the old cream-colored step-through motorbike with a round chrome headlamp into a smooth sharp turn onto the rail-side lane, @Mai hugging his waist behind him.
- 7.0–10.0s: @Mai glances back over her shoulder with her lips pressed tight as a long train horn echoes from far away down the empty tracks. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–4.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm ngoặt vào phố đường tàu, đúng lúc tiếng còi tàu hỏa rền vang từ phía xa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a distant train horn wailing, the bike engine puttering, a crossing bell ringing far away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 1 (`canh-15/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Hà Nội's narrow train street at noon: railway tracks running between rows of old tube houses, tiny cafés with low stools pulled back from the rails, laundry and potted plants along the walls.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 24mm wide low-angle shot along the rails, slow dolly-back; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Low between the shining rails, the narrow train street stretches away under the noon sun, laundry fluttering and potted plants lining the old tube-house walls.
- 3.0–7.0s: Tiny café tables and low plastic stools sit pulled back tight against the walls, coffee cups trembling on the tabletops as the rails begin to hum.
- 7.0–10.0s: Far in the distance at the end of the street, a single train headlamp glows small and bright, still very far away. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trên phố đường tàu, các quán cà phê vội vàng kéo ghế vào, đoàn tàu đang từ xa lao tới." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rails humming and ticking, coffee cups rattling on saucers, a long distant train horn. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 2 (`canh-15/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium side shot, slow pan following the bike; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The empty rails cut across the frame between café stools and potted plants, and far down the track a tiny train headlamp glows in the distance.
- 3.0–7.0s: @Lam rides the old cream-colored step-through motorbike with a round chrome headlamp briskly across the rails with @Mai holding on behind him, the train still far away.
- 7.0–10.0s: The bike rolls over the far rail and disappears into a narrow alley on the other side, @Lam's battered green pith helmet bobbing out of sight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Chiếc xe máy cũ băng qua đường ray trong gang tấc, rồi mất hút vào một con ngõ bên kia." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: tires thumping over steel rails, the bike engine buzzing, a distant train horn. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 3 (`canh-15/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Hà Nội's narrow train street at noon: railway tracks running between rows of old tube houses, tiny cafés with low stools pulled back from the rails, laundry and potted plants along the walls.

[CHARACTERS]
- Extra: four debt collectors on motorbikes stopped behind the passing train
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 28mm wide shot from the café side, slow lateral drift; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: A long blue and white train rumbles through the narrow street, its carriages filling the frame and the laundry on the walls fluttering in its wind.
- 3.0–7.0s: Through the gaps between the passing carriages, four debt collectors on motorbikes wait stopped well back from the rails beside the café stools, engines idling.
- 7.0–10.0s: The last carriage rolls away and the far side of the tracks stands empty, while the four debt collectors sit frozen on their motorbikes staring across with mouths shut. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đoàn tàu ầm ầm chạy qua, bốn chiếc xe đuổi theo đành phanh gấp, kẹt cứng ở bên này đường ray." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a train rumbling and clattering past, its horn blaring, idling engines sputtering. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 4 (`canh-15/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 40mm medium two-shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A narrow winding alley in the old quarter glows in noon light, laundry hanging overhead between tiny doorways and potted plants along the walls.
- 3.0–7.0s: @Lam rolls the old cream-colored step-through motorbike with a round chrome headlamp to a stop, and @Mai on the back seat speaks breathlessly, one hand pressed to her chest.
- 7.0–10.0s: @Mai closes her mouth, puffs out a breath through her nose and straightens her round glasses, still clutching the small black hard drive in her other hand. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông ơi, ông lái xe còn ghê hơn cả trong phim hành động, cháu suýt rơi cả tim!" (no subtitles)
- From 3.0s onward, @Mai's face and lips stay clearly visible while speaking; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the engine ticking down, a distant train fading away, a caged bird chirping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 5 (`canh-15/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A narrow winding old-quarter alley maze at noon, laundry overhead, tiny doorways, potted plants.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on @Lam, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam turns his head toward @Mai and speaks with a dry chuckle in his voice, tapping the brim of his battered green pith helmet with one finger.
- 3.0–7.0s: @Lam keeps speaking calmly, flicking his hand back toward the railway as if brushing away dust, his thick grey eyebrows lifting.
- 7.0–10.0s: @Lam closes his mouth into a crooked closed-lip grin while @Mai, behind his shoulder, shakes her head with a wide closed-lip smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.3s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ba mươi năm trước cả phố này đuổi ông còn không kịp, mấy thằng nhóc ấy ăn thua gì." (no subtitles)
- @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the idling engine, laundry flapping softly, a neighbor's radio murmuring far away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 6 (`canh-15/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: The camera rises above tangled wires and tiled roofs as @Lam grows small below, and a gleaming glass tower appears far off on the sunny skyline. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm bật cười, nhưng ông không biết, trong lúc mình chạy, Hưng đã ra tay ở một nơi khác." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pigeons fluttering off a roof, wind chimes tinkling, distant traffic. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 1 (`canh-16/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
- Extra: two police officers in green uniforms walking calmly into the shop
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 35mm wide shot, slow dolly-back through the smoke; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Charcoal grills smoke on the pavement in front of the bún chả shop, low plastic stools and steel tables empty after lunch, baskets of fresh herbs glowing in warm sunlight.
- 3.0–7.0s: Two police officers in green uniforms walk calmly into the shop through the drifting smoke, one holding a slim folder of papers with faint unreadable lines.
- 7.0–10.0s: The two officers stop politely beside a steel table and wait with relaxed shoulders, looking toward the grills as smoke curls lazily in the sunlight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Chiều hôm ấy, hai cán bộ công an bước vào quán bún chả, trên tay là đơn tố cáo lừa đảo của Hưng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal crackling, pork sizzling, calm footsteps, a distant street vendor calling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 2 (`canh-16/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A charcoal grill glows beside a steel table lined with skewers of pork, and a wide-brimmed black hat hangs on a hook on the wall above.
- 3.0–7.0s: @BaHoa unties her red apron with unhurried calm, folds it neatly and lays it on the steel table beside a basket of fresh herbs.
- 7.0–10.0s: @BaHoa lifts the wide-brimmed black hat from its hook, settles it on her burgundy curls and glances toward the doorway with closed red lips and a cool half smile. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bà Hoa không chạy, cũng không cãi, bà thong thả tháo tạp dề, đội mũ rộng vành rồi đi theo họ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal popping, fat sizzling, fabric rustling, a gold bangle clinking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 3 (`canh-16/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow pan with her to the grill; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @BaHoa raises one palm toward the doorway off-frame and speaks in a breezy brassy voice, unhurried, as if chatting with regular customers.
- 3.0–7.0s: @BaHoa keeps speaking as she turns to the grill, slides its little vent shut and moves the last skewers of pork onto a plate.
- 7.0–10.0s: @BaHoa closes her mouth, dusts off her hands, straightens her hat and strolls out toward the street on her own, chin held high. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–4.9s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Các chú cứ từ từ, để tôi tắt bếp than đã, kẻo cháy hết mẻ chả của khách." (no subtitles)
- @BaHoa's face and lips stay clearly visible while speaking; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a metal vent scraping shut, coals hissing, sandals tapping on the pavement. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 4 (`canh-16/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The tiny repair stall under the staircase lies ransacked, drawers hanging open, old radios knocked askew, and a clean dust-free rectangle on the workbench where something used to sit.
- 3.0–7.0s: @Khoa steps in under the bare bulb and stops short, his magnifier glasses on his forehead, staring at the empty rectangle on the workbench.
- 7.0–10.0s: @Khoa's eyes flick for a split second to an old wooden Soviet-era radio still untouched on the top shelf, and his lips press into a thin line. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cùng lúc ấy, sạp sửa đài của ông Khoa bị lục tung, chiếc ổ cứng đen trên bàn đã biến mất." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a bare bulb buzzing, a loose wire ticking against a shelf, distant alley chatter. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 5 (`canh-16/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm close-up, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A phone lies face-up on the worn wooden table, its blank screen lighting up again and again as it buzzes in a slow circle across the wood.
- 3.0–7.0s: @Mai picks up the buzzing phone, its blank glowing screen lighting her face, and her thumb freezes above it as it keeps vibrating in her hand.
- 7.0–10.0s: @Mai lowers the phone slowly, her round glasses reflecting its endless flashing glow, her lips pressed tight and her chin trembling. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Còn điện thoại của Mai sáng liên tục, bọn chúng đã gửi ảnh cô cho cả lớp, kèm hai chữ con nợ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone vibrating nonstop against wood, notification pings stacking up, street noise outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 6 (`canh-16/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning inside Lâm's narrow old-quarter tube house: a ground-floor room with the rolling steel shutter raised, a worn wooden table, a small family altar, sunlight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot, slow crane-down to the doorstep; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Mai walks to the open doorway, where faded red paint still stains the edge of the raised steel shutter and the front step.
- 3.0–7.0s: @Mai sinks down onto the paint-stained doorstep, sets the phone face-down beside her and covers her face with both hands.
- 7.0–10.0s: @Mai's shoulders shake without a sound as warm street sunlight falls across her lavender hoodie and the stained shutter edge above her. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–4.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Mai ngồi sụp xuống bậc cửa còn vệt sơn đỏ, ôm mặt khóc không thành tiếng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: muffled motorbikes passing, a soft shaky breath, the phone buzzing faintly on the step. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 1 (`canh-17/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: Neither of them moves, both with lips closed, as the camera rises over the sea of tiled roofs toward the distant lake glowing in the dark. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đêm ấy, hai ông cháu ngồi trên sân thượng, nhìn xuống phố cổ lấp lánh mà chẳng ai nói câu nào." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft night breeze, distant motorbike horns, a dog barking far off, wind chimes. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 2 (`canh-17/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: @Mai turns toward @Lam and speaks in a small cracked voice, her round glasses reflecting the city lights, her fingers twisting her hoodie sleeves.
- 3.0–7.0s: @Mai keeps speaking and leans her shoulder against @Lam's arm, her eyes glistening as she looks up at him.
- 7.0–10.0s: @Mai falls silent and closes her mouth, lowering her head, while @Lam looks out at the city with his jaw set. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.2s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Tại cháu mà bà Hoa bị bắt, ông ơi, hay mình trả tiền cho nó rồi thôi đi ông." (no subtitles)
- @Mai's face and lips stay clearly visible while speaking; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the night breeze, faint traffic below, a distant boat horn on the lake. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 3 (`canh-17/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tube-house rooftop in the old quarter at night: potted plants, a steel water tank, a sea of tiled roofs and warm city lights, a lake glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on @Lam, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam shakes his head gently and speaks in a calm husky voice, his cloudy left eye catching the warm city lights.
- 3.0–7.0s: @Lam keeps speaking as he rests a warm hand on @Mai's head, his thick grey eyebrows drawn low and steady.
- 7.0–10.0s: @Lam closes his mouth and keeps his hand on her head, gazing out over the glittering rooftops with a firm, quiet jaw. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.1s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông trả nó một đồng, thì ngày mai nó lại gài thêm trăm đứa khác khổ như con." (no subtitles)
- @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft breeze rustling potted leaves, a distant traffic hum, crickets. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 4 (`canh-17/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot, slow dolly-in on @Mai; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Mai lifts her phone, its screen glowing blank, and speaks quickly with a sniff, tapping its edge with one finger.
- 3.0–7.0s: @Mai keeps speaking and holds the phone up high in a showy livestreamer pose, rolling her eyes with a wry twist of her lips.
- 7.0–10.0s: @Mai stops and closes her mouth, lowering the phone, while @Lam turns his head sharply toward her with his eyebrows rising. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–4.7s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Hưng livestream mỗi tối, có hai triệu người xem, nó thích khoe khoang hơn cả thích tiền." (no subtitles)
- @Mai's face and lips stay clearly visible while speaking; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone buzzing faintly, the night breeze, distant horns. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 5 (`canh-17/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up, slow push-in to his eyes; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The steel water tank and potted plants on the rooftop glint under warm city light, the glowing lake shimmering beyond the sea of tiled roofs.
- 3.0–7.0s: @Lam freezes on his stool, then his shoulders begin to shake with a silent closed-mouth laugh, his thick grey eyebrows lifting.
- 7.0–10.0s: @Lam's narrow eyes, even the cloudy left one, light up with a sharp sparkle reflecting the city lights as a sly grin spreads with lips closed. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm khựng lại, rồi bật cười, đôi mắt mờ đục của ông bỗng sáng lên như ba mươi năm trước." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft breathy laugh through the nose, wind chimes tinkling, distant traffic. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 6 (`canh-17/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium two-shot, slow lateral track; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The sea of tiled roofs glitters with warm city lights under the night sky, the lake glowing in the distance beyond the potted plants.
- 3.0–7.0s: @Lam turns to @Mai with a sly glint and speaks low and steady, tapping his own lips with one finger and then pointing out at the city.
- 7.0–10.0s: @Lam closes his mouth and nods once, while @Mai straightens her round glasses and breaks into a slow closed-lip grin. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.4s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thế thì mình để chính cái miệng nó tự khai, trước mặt hai triệu người, con ạ." (no subtitles)
- From 3.0s onward, @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the night breeze, a far-off train horn, wind chimes tinkling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 1 (`canh-18/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: @BaHoa stops on the pavement, stretches her arms lazily toward the sky and fans her face with one hand, lips closed in a pleased smile. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Sáng hôm sau, cánh cổng đồn công an phường mở ra, bà Hoa bước ra, son môi vẫn đỏ chót." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birds chirping in the tree, an iron gate creaking, morning street traffic. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 2 (`canh-18/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The old cream-colored step-through motorbike with a round chrome headlamp stands parked under the tall tree outside the mustard-yellow police station wall.
- 3.0–7.0s: @BaHoa walks up to @Lam waiting beside the motorbike and speaks with a brassy laugh in her voice, flicking her fingers open to show empty palms.
- 7.0–10.0s: @BaHoa closes her red lips with a proud sniff, while @Lam, in his battered green pith helmet, shakes his head with a quiet closed-lip chuckle. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Tôi chỉ nói chuyện đầu tư, có cầm của ai đồng nào đâu mà giữ được tôi hả ông!" (no subtitles)
- From 3.0s onward, @BaHoa's face and lips stay clearly visible while speaking; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birds chirping, leaves rustling, a passing motorbike. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 3 (`canh-18/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm over-the-shoulder shot past @Lam onto @Khoa, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Parked motorbikes line the leafy street beside the open iron gate, sunlight dappling the mustard-yellow wall through the leaves of the tall tree.
- 3.0–7.0s: @Khoa, with an old wooden Soviet-era radio tucked under one arm, leans toward @Lam and speaks in a dry deadpan voice, wagging one finger.
- 7.0–10.0s: @Khoa closes his mouth and adjusts the magnifier glasses on his forehead, while @Lam stares at him with his thick grey eyebrows raised. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Khoa (man of 60, strictly standard Hà Nội Northern accent (never Southern accent), nasal wry tenor, deadpan and fussy, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cái ổ cứng thằng Béo lấy chỉ là ổ giả, trong đó toàn băng cải lương của tôi thôi." (no subtitles)
- From 3.0s onward, @Khoa's face and lips stay clearly visible while speaking; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: tree leaves rustling, a distant scooter horn, sparrows chirping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 4 (`canh-18/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning at the front gate of a ward police station on a leafy street: mustard-yellow walls, an open iron gate, a tall tree, parked motorbikes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, slow arc around them; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam squints at @Khoa and speaks with a dry, suspicious smile, tilting his head toward the wooden radio under @Khoa's arm.
- 3.0–7.0s: @Lam keeps speaking, pointing one finger at the old wooden Soviet-era radio and narrowing his calm eyes under the battered green pith helmet.
- 7.0–10.0s: @Lam closes his mouth and folds his arms, waiting, as @Khoa hugs the radio a little tighter against his ribs. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.3s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thế ổ thật ông giấu ở đâu? Đừng bảo là ông lại nhét vào cái đài Liên Xô nhé." (no subtitles)
- @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: leaves rustling, birds chirping, a motorbike puttering past. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 5 (`canh-18/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning at the front gate of a ward police station on a leafy street: mustard-yellow walls, an open iron gate, a tall tree, parked motorbikes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow tilt-down from his face to the radio; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Khoa gives @Lam a slow exaggerated wink, lips pressed shut, the morning sun gleaming on his bald crown.
- 3.0–7.0s: @Khoa pats the old wooden Soviet-era radio under his arm twice with his long fingers, its woven speaker cloth and worn knobs catching the light.
- 7.0–10.0s: @Lam's thick eyebrows rise slowly into a closed-lip grin, as @Khoa taps the side of his nose with one finger. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Khoa nháy mắt, vỗ vỗ chiếc đài gỗ cũ kẹp dưới nách, bên trong là toàn bộ bằng chứng thật." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: two hollow knocks on wood, sparrows chirping, a soft breeze. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 6 (`canh-18/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The tall tree sways over the open iron gate of the police station, sunlight sparkling through its leaves onto the mustard-yellow wall.
- 3.0–7.0s: @BaHoa narrows her sharp eyes under her wide-brimmed black hat and curls her red lips into a sly closed smile, gold hoop earrings swinging.
- 7.0–10.0s: @BaHoa flicks open a woven bamboo hand fan with a snap and fans herself slowly, eyes glinting toward the city like a tiger eyeing its next meal. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–4.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bà Hoa nheo mắt cười, lần này, đến lượt Hưng bị bộ ba già dắt mũi." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a fan snapping open, birds chirping, rustling leaves, distant traffic. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 1 (`canh-19/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The glass-walled boss room at night, a white leather sofa and a dark ring light on its stand, the magenta and gold neon of the call-center floor glowing beyond the glass, no person in frame.
- 3.0–7.0s: @Hung strides in and clicks on the ring light, which blooms into a bright white circle, then lifts a phone on a small selfie gimbal to arm's length, lips pressed into a cocky closed-mouth grin.
- 7.0–10.0s: @Hung smooths his ash-blond undercut in the blank glowing phone screen, straightens his gold-rimmed glasses and poses chin-up, the white ring reflected in both lenses. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Tám giờ tối, như thường lệ, Hưng bật đèn livestream, hai triệu người đang chờ ông chủ Phú Quý lên sóng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ring light switch clicking on, soft electronic hum, office air conditioning, a few faint notification chimes. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 2 (`canh-19/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 24mm low-angle wide shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Low wide view down the long aisle of the night call center toward closed brushed-steel elevator doors, blank monitors glowing on both sides under magenta and gold neon, nobody in the aisle.
- 3.0–7.0s: The elevator doors slide open with a soft chime and @Lam steps out alone, wearing a battered green pith helmet and his faded grey windbreaker, both hands empty at his sides.
- 7.0–10.0s: @Lam walks slowly up the aisle toward the camera between the glowing monitors, plastic sandals scuffing the carpet, calm narrow eyes fixed ahead and lips closed. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đúng lúc ấy, cửa thang máy mở, ông Lâm bước ra, mũ cối trên đầu, một mình, tay không." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: elevator chime, steel doors sliding open, sandals scuffing on carpet, rows of monitors humming. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 3 (`canh-19/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm over-the-shoulder shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the glass-walled boss room at night, the ring light glowing beside the white leather sofa and the glass door standing open onto the neon call-center floor, no person in frame.
- 3.0–7.0s: Over @Hung's shoulder on screen-right, @Lam stands in the open glass doorway on screen-left and speaks in a calm husky voice, face and lips clearly visible, one finger tapping the brim of his pith helmet.
- 7.0–10.0s: @Lam finishes, closes his mouth and waits without blinking, while @Hung, gimbal still raised, cocks one eyebrow with a silent closed-mouth smirk. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.7s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cậu Hưng, tôi đến trả nợ cho cháu tôi, nhưng cậu phải nhận tiền trước mặt người xem." (no subtitles)
- From 3.0s onward, @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ring light hum, distant keyboard clicks, the glass door settling on its hinge. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 4 (`canh-19/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot slow arc; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Hung swings the phone on its small selfie gimbal toward @Lam, the blank screen glowing, and starts talking loudly into it like a livestream salesman, face and lips clearly visible.
- 3.0–7.0s: @Hung finishes his taunt with a flourish of his ringed hand toward @Lam, then closes his mouth in a smug grin, holding the gimbal steady.
- 7.0–10.0s: @Lam stands perfectly still in the doorway on screen-left, helmet on and empty hands relaxed, while @Hung on screen-right waits for him to kneel. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.4s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cả nhà ơi, ông già xe ôm đến trả nợ này, xem ông ấy có quỳ xuống xin không nào!" (no subtitles)
- @Hung's face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ring light hum, a rising flurry of notification chimes, distant city traffic far below. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 5 (`canh-19/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 28mm wide shot gentle lateral glide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The glass-walled boss room under the white ring light, a chrome swivel chair standing empty in front of a wide glass desk with a small teapot and cups, neon spilling over the floor, no person in frame.
- 3.0–7.0s: @Lam walks into frame, pulls the chrome chair out with one hand and sits down unhurried, crossing one leg over the other, lips closed.
- 7.0–10.0s: @Lam rests his pith helmet on his knee, pours himself a small cup of tea and leans back easily, a faint knowing smile on closed lips, like an old man at a street tea stall. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm không quỳ, ông kéo ghế ngồi xuống, bình thản như đang ngồi quán trà đá đầu ngõ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: chair wheels rolling on the floor, leather creaking, tea trickling into a small cup, ring light hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 6 (`canh-19/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the parked white van at night, two laptops glowing blank on a fold-out desk among tangled cables and a thermos, neon reflections sliding over the tinted windows, no person in frame.
- 3.0–7.0s: @Mai on screen-left types at lightning speed, round glasses lit by the glow, while @Khoa on screen-right clicks a small black hard drive into the side of a laptop.
- 7.0–10.0s: @Khoa gives a closed-mouth wink and a thumbs-up, and @Mai nods once without looking up, lips pressed together, both faces lit by the blank glowing screens. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Dưới chân tòa nhà, trong xe tải trắng, Mai gõ phím như bay, ông Khoa đã cắm sẵn ổ cứng thật." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rapid keyboard clatter, a plug clicking into a port, a soft confirmation beep, muffled street traffic outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 1 (`canh-20/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The glass-walled boss room at night, the ring light glowing over a wide glass desk with a steaming teacup beside a chrome chair, the call-center floor beyond bathed in magenta and gold neon, no person in frame.
- 3.0–7.0s: @Lam sits calmly in the chrome chair on screen-left, pith helmet on his knee, and asks in a husky steady voice, face and lips clearly visible, while @Hung on screen-right films him with the gimbal.
- 7.0–10.0s: @Lam closes his mouth and tilts his head patiently, while @Hung lowers the gimbal an inch and lets out a closed-mouth scoff. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.7s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cháu tôi vay năm triệu, ba tháng thành trăm rưỡi, cậu tính lãi bao nhiêu một ngày thế?" (no subtitles)
- From 3.0s onward, @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ring light hum, distant keyboard clicks, a faint notification chime. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 2 (`canh-20/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Hung leans into the gimbal lens and starts talking loudly and smugly, face and lips clearly visible in the white ring light.
- 3.0–7.0s: @Hung wags three ringed fingers in the air as he finishes, then closes his mouth in a cocky grin, his gold-rimmed glasses flashing.
- 7.0–10.0s: @Hung spreads his hands wide and raises his chin toward the lens, while @Lam sits motionless at the soft-focus edge of frame on screen-left. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.7s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ba phần trăm một ngày, không trả thì tôi gửi ảnh cho cả họ hàng nó, luật nào cấm được tôi?" (no subtitles)
- @Hung's face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ring light hum, notification chimes multiplying, a leather chair creaking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 3 (`canh-20/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm over-the-shoulder shot slow arc; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Over @Hung's shoulder, @Lam sits in the chrome chair and speaks calmly up at him, face and lips clearly visible, one weathered hand gesturing gently toward the glowing gimbal phone.
- 3.0–7.0s: @Lam finishes with a slow nod and closes his mouth, his calm narrow eyes holding @Hung's gaze.
- 7.0–10.0s: @Hung freezes with the gimbal half-raised and his grin slipping, while @Lam leans back and folds his arms with a closed-mouth smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–4.8s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cậu nói to lên một chút nữa, để hai triệu người đang xem cùng nghe cho rõ." (no subtitles)
- @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ring light hum, a sudden flood of notification chimes, the distant drone of the city. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 4 (`canh-20/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: @Mai leans back in her seat with a tight closed-mouth smile, the laptop light pulsing across her face and neon sliding over the tinted window behind her. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Mai bấm nút, buổi livestream của Hưng bị chia đôi, một nửa là danh sách nạn nhân thật lấy từ máy chủ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a single decisive key click, a rising electronic chime, rapid soft beeps, muffled street traffic. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 5 (`canh-20/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Close on the white ring light and the empty white leather sofa in the boss room at night, the neon of the call center pulsing through the glass wall, no person in frame.
- 3.0–7.0s: @Hung steps into the ring light holding the gimbal as the phone buzzes nonstop in his hand, its blank screen flickering rapid white and red light across his face.
- 7.0–10.0s: @Hung's cocky grin freezes stiff on his closed lips, a bead of sweat sliding down his temple as the flicker keeps strobing over his gold-rimmed glasses. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Điện thoại của Hưng rung liên hồi, bình luận chửi rủa trôi như thác, số người xem vọt lên năm triệu." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone buzzing nonstop, a torrent of rapid notification pings, ring light hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 6 (`canh-20/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot slow rack focus; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Hung slowly lowers the buzzing gimbal, its blank screen still flickering, the frozen grin fading on his closed lips.
- 3.0–7.0s: @Hung turns his head toward screen-left and stares off-frame, swallowing hard, his ringed fingers loosening on the gimbal handle.
- 7.0–10.0s: Focus shifts to the glass desk in the foreground, where a small teacup still steams beside a battered green pith helmet, while @Hung stands motionless in soft focus behind it. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Hắn quay sang, ông già xe ôm vẫn ngồi đó, nhấp một ngụm trà, mỉm cười như chưa có chuyện gì." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: phone buzzing, a teacup set gently on glass, a slow contented sip, ring light hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 1 (`canh-21/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: The callers walk out in a quiet line between the desks toward the elevator, leaving rows of empty chairs slowly turning under the glowing monitors. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trong phòng gọi điện, từng nhân viên tháo tai nghe, lặng lẽ đứng dậy bỏ về, không ai muốn dính vào nữa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: headsets clattering softly onto desks, chairs rolling back, quiet footsteps, a distant elevator chime. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 2 (`canh-21/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot handheld slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The emptying call-center floor at night, abandoned headsets on the desks and chairs left askew under blank glowing monitors, magenta neon pulsing, no person in frame.
- 3.0–7.0s: @Hung bursts out of the glass boss-room door into the aisle and yells toward the empty elevator at the far end, face and lips clearly visible, one ringed hand raised high.
- 7.0–10.0s: @Hung closes his mouth and stands panting alone in the empty aisle, satin bomber jacket rumpled, staring at the rows of abandoned chairs. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.0s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ngồi xuống hết! Đứa nào bước ra khỏi cửa là tao trừ hết lương, nghe chưa?" (no subtitles)
- From 3.0s onward, @Hung's face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a glass door swinging open, a lone chair slowly spinning, monitor hum, a distant elevator chime. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 3 (`canh-21/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot fast tracking dolly; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The long aisle of the night call center, empty chairs and blank glowing monitors on both sides, the steel elevator doors standing open at the far end, no person in frame.
- 3.0–7.0s: @Beo charges up the aisle from the elevator, his heavy frame bouncing and flip-flops flapping, clutching a phone whose blank screen flickers in his hand.
- 7.0–10.0s: @Beo skids to a stop, face drained pale and shiny with sweat, small eyes wide and closed lips trembling, holding the glowing phone out in front of him. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Béo chạy vào, mặt cắt không còn giọt máu, tay cầm điện thoại đang phát lại chính buổi livestream của đại ca." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heavy running footsteps, flip-flops flapping, wheezing breath, a phone buzzing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 4 (`canh-21/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm over-the-shoulder shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The doorway of the glass-walled boss room at night, the ring light still glowing over the white leather sofa, magenta neon reflected in the glass, no person in frame.
- 3.0–7.0s: Over @Hung's shoulder on screen-right, @Beo stands in the doorway on screen-left holding up the glowing phone and blurts out the news, face and lips clearly visible, gold front tooth flashing.
- 7.0–10.0s: @Beo closes his mouth and wipes the sweat off his shaved head, while @Hung's shoulders stiffen and his ringed hand tightens around the gimbal. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Beo (man of 28, strictly standard Hà Nội Northern accent (never Southern accent), rough loud bass, blustering, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Đại ca ơi, cả mạng đang chia sẻ, công an kinh tế đang lên tận đây rồi!" (no subtitles)
- From 3.0s onward, @Beo's face and lips stay clearly visible while speaking; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: panting breath, a phone buzzing nonstop, ring light hum, a distant siren far below. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 5 (`canh-21/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Hung turns sharply to @Beo and starts barking orders, face and lips clearly visible, his gold-rimmed glasses catching the white ring light.
- 3.0–7.0s: @Hung finishes, pointing a ringed finger toward the elevator, then closes his mouth and breathes hard through his nose, a vein standing out on his neck.
- 7.0–10.0s: @Beo nods rapidly and scurries out of frame, leaving @Hung alone in the ring light, jaw clenched and lips pressed tight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Gọi hết anh em ra chặn cổng, tuyệt đối đừng để lão già ấy ra khỏi tòa nhà này!" (no subtitles)
- @Hung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ring light hum, a phone buzzing, hurried flip-flop footsteps fading away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 6 (`canh-21/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A small empty teacup on the glass desk beside the chrome chair in the boss room, the ring light glowing, the deserted call-center floor visible beyond the glass, no person in frame.
- 3.0–7.0s: @Lam rises from the chrome chair, settles a battered green pith helmet on his head and tugs his windbreaker straight, lips closed in a calm smile.
- 7.0–10.0s: @Lam strolls unhurried down the empty aisle into the waiting elevator, turns to face the camera and gives a small nod as the steel doors slide shut. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm đứng dậy, đội lại mũ cối, thong thả bước vào thang máy như một ông khách vừa uống xong chén trà." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a teacup set down on glass, unhurried sandal footsteps, elevator chime, doors sliding closed. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 1 (`canh-22/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on the wide street in front of the glass tower: neon reflections on the asphalt, tall trees, parked motorbikes, warm streetlamps.

[CHARACTERS]
- Extra: twenty young debt collectors in black on motorbikes revving and blocking the tower entrance
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 18mm high wide shot slow crane-down; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: High wide view of the night street in front of the gleaming glass tower, neon reflections rippling on the asphalt under warm streetlamps and tall trees.
- 3.0–7.0s: Twenty young debt collectors in black roll their motorbikes into a wide half-circle a few meters in front of the tower's glass doors, revving engines, faces hidden in shadow.
- 7.0–10.0s: Their headlights flare into a wall of white glare across the glass doors as exhaust haze curls up through the neon light. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Dưới sảnh, hai chục đàn em của Béo rồ ga chắn kín lối ra, đèn xe chói lòa cả một góc phố." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a chorus of revving motorbike engines, horns blaring, exhaust rumbling, engines settling into an idle. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 2 (`canh-22/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on the wide street in front of the glass tower: neon reflections on the asphalt, tall trees, parked motorbikes, warm streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot slow orbit; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The glass doors of the tower lobby at night, bathed in the white glare of many motorbike headlights shining from the darkness several meters away, exhaust haze drifting, no person in frame.
- 3.0–7.0s: The glass doors part and @Lam walks out alone into the glare, pith helmet on and hands empty, and stops in the middle of the pavement.
- 7.0–10.0s: @Lam stands perfectly still inside the distant ring of headlights and slowly lifts the brim of his battered green pith helmet with one finger, calm narrow eyes steady and lips closed. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm bước ra một mình, đứng giữa vòng vây, không lùi một bước, chỉ khẽ nâng vành mũ cối lên." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: idling motorbike engines all around, glass doors sliding apart, one horn honk dying away, wind in the trees. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 3 (`canh-22/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on the wide street in front of the glass tower: neon reflections on the asphalt, tall trees, parked motorbikes, warm streetlamps.

[CHARACTERS]
- Extra: dozens of cyclos pedaled by old drivers rolling in from both ends of the street
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 24mm aerial drone slow descending glide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Aerial view down the long neon-lit street, warm streetlamps and tall trees lining both sidewalks, the white glare of the motorbike half-circle burning in front of the glass tower.
- 3.0–7.0s: From both ends of the street, dozens of cyclos pedaled by old drivers in faded shirts and conical hats roll in slowly side by side, bells tinkling.
- 7.0–10.0s: The cyclos glide to a quiet stop in two long lines along the curbs at a respectful distance, the old drivers sitting upright on their saddles, mouths closed and faces calm. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Rồi từ hai đầu phố, hàng chục chiếc xích lô chậm rãi đạp tới, những bác xích lô già của phố cổ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: dozens of cyclo bells tinkling, bicycle chains clicking, thin wheels rolling over asphalt, motorbike engines falling quiet. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 4 (`canh-22/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on the wide street in front of the glass tower: neon reflections on the asphalt, tall trees, parked motorbikes, warm streetlamps.

[CHARACTERS]
- Extra: old-quarter shopkeepers and motorbike-taxi drivers stepping out and lining the pavement in silence
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 35mm medium tracking shot along the sidewalk; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Along the neon-lit sidewalk, the doors of small shops and tea stalls swing open one after another under warm streetlamps.
- 3.0–7.0s: Old-quarter shopkeepers in aprons and motorbike-taxi drivers in pith helmets step out and line the pavement side by side, arms folded, mouths closed.
- 7.0–10.0s: The silent crowd stands unmoving along the whole length of the sidewalk, faces lit by neon and streetlamps, every gaze turned toward the glass tower. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Các bà bán hàng, các ông xe ôm, cả dãy phố lần lượt bước ra, đứng kín vỉa hè, không ai nói một lời." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: shop doors creaking open, shuffling sandals, a dog barking once, then a deep hush over idling engines. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 5 (`canh-22/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The neon-lit sidewalk under tall trees at night, streetlamp light pooling on the paving stones and exhaust haze drifting through the white glare, no person in frame.
- 3.0–7.0s: @BaHoa strides into frame at the head of the crowd, waving a woven bamboo hand fan in slow lazy strokes, red lips pressed together, gold hoop earrings swinging.
- 7.0–10.0s: @BaHoa stops, lowers her chin and narrows her sharp eyes toward screen-right with a closed-mouth smirk, fanning herself like a cook eyeing a grill about to burn. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đi đầu là bà Hoa, tay phe phẩy quạt nan, nhìn lũ đàn em như nhìn mẻ chả sắp cháy." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft flap of a bamboo hand fan, heeled sandals clicking, idling engines sputtering. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 6 (`canh-22/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on the wide street in front of the glass tower: neon reflections on the asphalt, tall trees, parked motorbikes, warm streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- Extra: young debt collectors walking their motorbikes backward behind him
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The wide street in front of the glass tower at night, neon reflections on the asphalt and the white glare of motorbike headlights burning beneath the tall trees.
- 3.0–7.0s: @Beo stands in the middle of the street turning his shaved head left and right, small eyes darting toward the silent crowds lining both sidewalks, lips pressed shut.
- 7.0–10.0s: Behind @Beo, the young debt collectors quietly walk their motorbikes backward, then turn and slip away one by one into the side streets, leaving him alone in the glare. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Béo nhìn quanh, đám đàn em lần lượt dắt xe lùi lại, rồi từng đứa một lặng lẽ chuồn mất." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: motorbike engines cutting off one by one, tires rolling softly backward, footsteps fading, a lonely cricket chirping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 1 (`canh-23/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: The headlights snap on and the red sports car roars off toward the exit ramp, its taillights streaking red through the empty car park. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Hưng chạy xuống hầm, nhảy lên chiếc xe thể thao đỏ, rú ga phóng ra cửa sau tòa nhà." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: hurried sneaker footsteps on concrete, a car door thudding shut, a high-pitched engine roar, tires squealing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 2 (`canh-23/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Evening rush hour on a wide Hà Nội avenue: a dense river of motorbikes and cars, red taillights, neon and streetlamps, trees along the sidewalks.

[CHARACTERS]
- Extra: a dense crowd of evening commuters on motorbikes in helmets and face masks, seen from above
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 35mm top-down aerial drone slow descent; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Top-down aerial view of a wide Hà Nội avenue at evening rush hour, a dense river of motorbikes crawling under neon and streetlamps, red taillights glowing.
- 3.0–7.0s: In the middle of the motorbike river, a low red sports car with no badge sits wedged in place with its tinted windows dark, inching forward a hand's width at a time while scooters stream around it.
- 7.0–10.0s: The camera sinks toward the gleaming red hood as an old scooter loaded with a tall tower of potted flowers putters past the stranded sports car, whose hazard lights blink helplessly. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Nhưng đây là Hà Nội giờ tan tầm, chiếc siêu xe đỏ chói chỉ nhích được vài mét giữa biển xe máy." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a sea of beeping scooter horns, idling engines, a sports car engine revving uselessly, one long comic honk. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 3 (`canh-23/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium tracking shot alongside; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Close on a narrow gap between rows of idling motorbike taillights and chrome mirrors on the jammed avenue, neon and streetlamps blurring in the background, no person in frame.
- 3.0–7.0s: @Lam threads into the gap on the old cream-colored step-through motorbike with a round chrome headlamp, his battered green pith helmet low, slipping between the lanes like a fish through reeds.
- 7.0–10.0s: @Lam glides past the stalled commuters with steady hands, eyes fixed ahead and lips closed, the round chrome headlamp throwing a warm beam through the traffic. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Phía sau, ông Lâm trên chiếc xe máy cũ lách qua dòng xe như cá lội, mỗi lúc một gần hơn." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: an old engine puttering steadily, a cheerful little horn beep, a sea of idling engines. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 4 (`canh-23/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Evening rush hour on a wide Hà Nội avenue: a dense river of motorbikes and cars, red taillights, neon and streetlamps, trees along the sidewalks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide shot slow pan; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A low red sports car with no badge stands stranded at the edge of the jammed avenue with its engine running, red taillights glowing all around it, no person in frame.
- 3.0–7.0s: The driver's door swings open and @Hung scrambles out onto the tree-lined sidewalk, clutching his glowing phone to his chest, satin bomber jacket flapping.
- 7.0–10.0s: @Hung sprints away along the sidewalk past the trees toward a distant steel truss bridge lit by sparse lamps, white sneakers flashing and mouth clamped shut. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Hưng bỏ lại siêu xe giữa đường, ôm điện thoại cắm đầu chạy bộ về phía cây cầu sắt bên sông." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a car door swinging open, a chorus of honking horns, sneakers pounding the pavement, ragged panting. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 5 (`canh-23/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Evening rush hour on a wide Hà Nội avenue: a dense river of motorbikes and cars, red taillights, neon and streetlamps, trees along the sidewalks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm close-up tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Close on the round chrome headlamp and cream front fender of an old step-through motorbike idling at the edge of the jammed avenue, neon reflections sliding over the chrome, no person in frame.
- 3.0–7.0s: @Lam, seated on the old cream-colored step-through motorbike with a round chrome headlamp, gazes ahead toward the distant bridge and says this to himself with a dry chuckle, face and lips clearly visible.
- 7.0–10.0s: @Lam closes his mouth, tugs the strap of his battered green pith helmet tight and twists the throttle with a small sly grin. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.2s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chạy bộ lên cầu mà đòi thoát Lâm Rồng à, thằng nhóc này còn non lắm." (no subtitles)
- From 3.0s onward, @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: an old engine puttering, distant horns, a helmet strap buckle clicking, the motorbike revving. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 6 (`canh-23/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on a century-old steel truss railway bridge over a wide dark river: rusty iron lattice beams lit by sparse lamps, a narrow motorbike lane beside the tracks, city lights on the far bank.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 24mm aerial drone slow forward glide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Aerial view of a century-old steel truss railway bridge spanning a wide dark river at night, its rusty iron lattice lit by sparse lamps.
- 3.0–7.0s: The drone glides along the bridge's long iron spine, the narrow motorbike lane beside the tracks glowing under the lamps and city lights shimmering on the far bank.
- 7.0–10.0s: The camera settles over the empty middle span, lamplight pooling on the rails as river mist drifts through the iron beams. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cây cầu sắt trăm tuổi, nơi ba mươi năm trước Lâm Rồng từng làm mưa làm gió, đêm nay lại chứng kiến một cuộc rượt đuổi." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind whistling through iron girders, the river lapping far below, distant city traffic. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 1 (`canh-24/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The narrow motorbike lane beside the tracks on the old steel truss bridge at night, rusty iron beams lit by sparse lamps and the far end lost in darkness, no person in frame.
- 3.0–7.0s: @Hung runs into frame along the motorbike lane, panting, phone clutched to his chest, then skids to a halt in the middle of the span.
- 7.0–10.0s: @Hung stares ahead with his mouth clamped shut as blue and red lights start flashing far away at the end of the bridge, sealing the way down, no figures visible. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Hưng chạy đến giữa cầu thì khựng lại, phía bên kia, đèn xe công an đã chắn kín lối xuống." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: sneakers pounding on iron plates, ragged panting, a distant police siren whooping softly, wind through the girders. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 2 (`canh-24/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on a century-old steel truss railway bridge over a wide dark river: rusty iron lattice beams lit by sparse lamps, a narrow motorbike lane beside the tracks, city lights on the far bank.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm low-angle wide shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Low view down the motorbike lane of the old steel truss bridge, a warm round headlamp approaching slowly out of the dark between the rusty iron beams, no person visible.
- 3.0–7.0s: The old cream-colored step-through motorbike with a round chrome headlamp rolls to a gentle stop and @Lam sets it on its stand, swinging one leg off the seat.
- 7.0–10.0s: @Lam lifts the battered green pith helmet off his grey crew cut and holds it at his side, standing tall under a bridge lamp with lips closed and calm eyes forward. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Phía sau, tiếng xe máy cũ chậm rãi dừng lại, ông Lâm dựng xe, tháo mũ cối cầm trên tay." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: an old engine puttering to a stop, the metal clack of a side stand, wind through the iron beams, a distant siren. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 3 (`canh-24/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm over-the-shoulder shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The middle span of the old steel truss bridge at night, sparse lamps glowing on the rusty iron lattice and blue and red lights flickering far away at the end, no person in frame.
- 3.0–7.0s: Over @Lam's shoulder on screen-left, @Hung spins around a few steps away on screen-right and yells at him, face and lips clearly visible, ash-blond hair wind-tossed and glasses askew.
- 7.0–10.0s: @Hung closes his mouth, chest heaving, clutching his glowing phone, while @Lam stands still on screen-left holding the pith helmet at his side. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Hung (man of 31, strictly standard Hà Nội Northern accent (never Southern accent), loud slick tenor of a livestream salesman, smug and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông là cái thá gì mà dám chơi tôi? Ông chỉ là một lão già chạy xe ôm thôi!" (no subtitles)
- From 3.0s onward, @Hung's face and lips stay clearly visible while speaking; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind howling through iron girders, ragged breathing, the river rushing below. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 4 (`canh-24/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm low-angle close-up slow tilt-down; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam meets @Hung's stare without a word, lips closed, the bridge lamp above casting a warm halo over his grey crew cut as the wind ripples his windbreaker.
- 3.0–7.0s: The camera tilts down as @Lam slowly rolls up his right sleeve fold by fold, his weathered fingers steady in the lamplight.
- 7.0–10.0s: A coiled dark-green dragon tattoo stands revealed along @Lam's bare right forearm, its scales gleaming under the bridge lamp, while @Hung stops dead in soft focus beyond it, lips pressed shut. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lâm không trả lời, ông chậm rãi xắn tay áo, con rồng xanh sẫm hiện ra dưới ánh đèn cầu." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind whistling through the iron lattice, the soft rustle of a rolled sleeve, the deep rumble of the river, one distant temple bell. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 5 (`canh-24/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium two-shot slow arc; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam lowers his tattooed arm to his side and speaks to @Hung in a calm husky voice, face and lips clearly visible, the bridge lamp glowing behind him.
- 3.0–7.0s: @Lam finishes with a slow nod and closes his mouth, the dark-green dragon tattoo still bare on his forearm, as the camera arcs to frame both men several steps apart.
- 7.0–10.0s: @Hung takes a shaky step back on screen-right, lips pressed tight and knuckles white around his phone, while @Lam stands unmoving on screen-left under the lamp. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.3s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bố cậu chưa kể hết à? Ba mươi năm trước, phố cổ này là của Rồng, giờ vẫn thế." (no subtitles)
- @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind through the iron girders, the river rushing below, distant sirens drawing closer. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 6 (`canh-24/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 24mm wide shot slow crane-down; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The rusty iron railing of the old steel truss bridge at night, the wide dark river glittering far below with the reflected city lights, no person in frame.
- 3.0–7.0s: @Hung backs up to the railing and a phone on a small selfie gimbal slips from his trembling fingers, tumbling over the edge with its blank screen still glowing.
- 7.0–10.0s: The glowing phone spins down through the dark and vanishes into the river with a tiny splash, while @Hung leans on the railing above, staring down with his mouth shut. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Hưng lùi lại, chiếc điện thoại tuột khỏi tay rơi xuống dòng sông, nhưng năm triệu người đã kịp thấy hết." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a sharp gasp, the clatter of a gimbal on iron, a faint distant splash, wind and rushing water. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 1 (`canh-25/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: @Hung slowly raises both his own hands to shoulder height, ringed fingers spread, face drained pale and lips pressed shut, while the officers wait without moving. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Hai cán bộ công an bước tới, Hưng tự giơ hai tay lên, gương mặt kiêu ngạo giờ trắng bệch như tờ giấy." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: calm footsteps on iron plates, a police radio crackling softly, wind through the girders, the river below. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 2 (`canh-25/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: A police officer in a green uniform stands calmly nearby with hands behind his back as @Beo sniffles and wipes his eyes with his wrist, fake-gold chain glinting. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ở văn phòng Phú Quý, Béo Đầu Sấm ngồi bệt dưới sàn, ôm điện thoại, mếu máo như đứa trẻ lạc mẹ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a loud sniffle, monitor hum, a police radio crackling softly, the whine of the air conditioner. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 3 (`canh-25/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A sunny university schoolyard in the morning with tall trees and old yellow buildings.

[CHARACTERS]
- Extra: groups of students looking at their phones and hugging each other
No named characters appear in this shot; the extras above are the only people in it.

[SHOT]
- Framing & motion: 35mm aerial drone slow descending glide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Aerial view of a sunny university schoolyard in the morning, tall trees casting dappled shade over the paving and old yellow buildings with green shutters all around.
- 3.0–7.0s: Groups of students gather under the trees staring down at their phones, the blank screens glowing, then slowly lift their heads and turn to one another.
- 7.0–10.0s: The students wrap each other in silent tearful hugs, lips pressed together and eyes wet, as sunlight falls through the leaves over the whole schoolyard. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Sáng hôm sau, ứng dụng Phú Quý bị khóa, hàng nghìn sinh viên được xóa nợ, nhiều đứa ôm nhau khóc giữa sân trường." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong, rustling leaves, soft sniffles, a chorus of phone chimes. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 4 (`canh-25/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Morning inside the narrow tube house, sunlight from the street pouring through the raised steel shutter onto the worn wooden table, a phone lying face-down on it, no person in frame.
- 3.0–7.0s: @Mai sits down at the table, turns the phone over and looks at its softly glowing screen, her round glasses catching the light as she holds her breath.
- 7.0–10.0s: @Mai lets out a long breath, eyes glistening behind her glasses, a closed-mouth smile spreading across her face as she presses the phone to her chest. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Mai mở điện thoại, lần đầu sau ba tháng, không còn cuộc gọi lạ nào, chỉ có tin nhắn cảm ơn của bạn bè." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: gentle message chimes one after another, birdsong from the street, a motorbike passing outside, a soft exhale. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 5 (`canh-25/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 3.0–7.0s: @Mai hops onto the stool beside @Lam at the table and tells him the news with a beaming grin, face and lips clearly visible, holding up her glowing phone.
- 7.0–10.0s: @Mai closes her mouth and nudges her glasses up, eyes sparkling, while @Lam on screen-right lowers his teacup and raises his thick grey eyebrows. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Mai (young woman of 20, strictly standard Hà Nội Northern accent (never Southern accent), clear lively soprano, quick and earnest, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông ơi, cả lớp cháu bảo ông là ông nội ngầu nhất cái Hà Nội này đấy ông ạ!" (no subtitles)
- From 3.0s onward, @Mai's face and lips stay clearly visible while speaking; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning street bustle, birdsong, a teacup clinking on wood, a motorbike horn outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 6 (`canh-25/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning inside Lâm's narrow old-quarter tube house: a ground-floor room with the rolling steel shutter raised, a worn wooden table, a small family altar, sunlight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam sets down his teacup and waves the compliment away with one hand, speaking in a dry husky voice, face and lips clearly visible.
- 3.0–7.0s: @Lam finishes with a modest shrug and closes his mouth, reaching for a battered green pith helmet on the table.
- 7.0–10.0s: @Lam puts on the pith helmet to hide a proud little smile, while @Mai at the edge of frame covers her grin with her hand. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.3s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ngầu gì, ông chỉ là ông già xe ôm, mai ông còn phải chở cụ Tý đi chợ sớm." (no subtitles)
- @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a teacup set on wood, morning street bustle, a rooster crowing far away, birdsong. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 1 (`canh-26/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: The camera settles on a woven bamboo hand fan resting on top of the pile of gifts, glowing in a warm sunbeam. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Một tuần sau, tiền mổ mắt cho ông Lâm do cả phố cổ góp lại, mỗi người một ít, bà Hoa góp nhiều nhất." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft hospital hum, birdsong outside the window, a curtain rustling in the breeze. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 2 (`canh-26/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 7.0–10.0s: The last layer comes away and @Lam blinks several times into the flood of morning light, his once-cloudy left eye now clear, a slow closed-mouth smile spreading. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cô y tá từ từ tháo băng, ông Lâm chớp mắt mấy lần, ánh nắng sớm tràn vào căn phòng trắng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft rustle of unwinding gauze, birdsong, a gentle hospital hum, a deep slow breath. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 3 (`canh-26/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A bright, clean eye-hospital room in the morning: a white bed, a big window full of sunlight, a small bedside table with a thermos and a vase of daisies.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder shot slow rack focus; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The bedside of the bright eye-hospital room, sunlight streaming through the big window behind a vase of daisies, everything softly out of focus, no person in frame.
- 3.0–7.0s: Over @Lam's shoulder, a blurry figure beside the bed slowly sharpens into @Mai, standing in her lavender hoodie with her hands clasped at her chest.
- 7.0–10.0s: @Mai's eyes are red-rimmed and glistening behind her round glasses as she smiles with closed lips, sunlight haloing her black bob. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–4.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Người đầu tiên ông nhìn thấy rõ là Mai, đứng bên giường, mắt đỏ hoe mà vẫn cười." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong, a soft sniffle, a faint hospital hum, a curtain swaying. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 4 (`canh-26/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A bright, clean eye-hospital room in the morning: a white bed, a big window full of sunlight, a small bedside table with a thermos and a vase of daisies.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot slow arc; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam looks at @Mai with clear bright eyes and speaks softly in his husky voice, face and lips clearly visible, a teasing smile at the corners of his mouth.
- 3.0–7.0s: @Lam finishes and closes his mouth, slowly shaking his head with a wistful look as the camera arcs around the sunlit bed.
- 7.0–10.0s: @Mai shakes with a silent laugh through her tears, lips pressed together, and wipes her eyes under her glasses while @Lam watches her with a warm closed-mouth smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.3s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cháu ông xinh thế này mà mấy năm nay ông chỉ nhìn thấy lờ mờ, phí quá con ạ." (no subtitles)
- @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong, a soft sniffle, a curtain swaying in the breeze, distant street horns. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 5 (`canh-26/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 3.0–7.0s: @BaHoa sweeps into the doorway on screen-left with @Khoa beside her on screen-right and calls toward the bed in a brassy teasing voice, face and red lips clearly visible, a woven bamboo fan in hand.
- 7.0–10.0s: @BaHoa closes her mouth and arches one eyebrow with a smug look, while @Khoa nudges his thick magnifier glasses up his forehead and rolls his eyes. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @BaHoa (woman of 61, strictly standard Hà Nội Northern accent (never Southern accent), bold brassy alto, quick-witted and teasing, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mắt sáng rồi thì nhớ trả tôi tiền bún chả ba mươi năm nay ông ăn chịu đấy nhé!" (no subtitles)
- From 3.0s onward, @BaHoa's face and lips stay clearly visible while speaking; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heeled sandals clicking on tile, the flap of a bamboo fan, a quiet hospital corridor hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 6 (`canh-26/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The doorway of the bright eye-hospital room, a white corridor behind, morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Khoa leans toward the bed and speaks in a dry nasal deadpan, face and lips clearly visible, one hand cupped beside his mouth as if sharing a secret.
- 3.0–7.0s: @Khoa finishes, closes his mouth and gives a sly little wink, as @BaHoa's fan stops mid-stroke beside him.
- 7.0–10.0s: @BaHoa snaps her bamboo fan open in front of her face to hide her reddening cheeks, lips pressed tight, while @Khoa grins with closed lips. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–4.9s, spoken on camera by @Khoa (man of 60, strictly standard Hà Nội Northern accent (never Southern accent), nasal wry tenor, deadpan and fussy, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bà ấy nói đùa đấy, thực ra bà ấy khóc cả đêm qua vì lo cho ông đấy." (no subtitles)
- @Khoa's face and lips stay clearly visible while speaking; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a bamboo fan snapping open, a stifled sniff, a soft corridor hum, birdsong through a window. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 1 (`canh-27/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn in Hà Nội's old quarter: an ancient brick city gate with a tiled roof, narrow streets of tube houses with green shutters, tangled overhead wires, street vendors with shoulder poles, pink-gold morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Golden morning light under the ancient brick city gate with its tiled roof, the old cream-colored step-through motorbike with a round chrome headlamp parked in the archway, sparrows hopping on the old bricks, no person in frame.
- 3.0–7.0s: @Lam walks into frame, settles a battered green pith helmet on his head and sits sideways on the motorbike seat, his clear eyes scanning the waking street.
- 7.0–10.0s: @Lam folds his arms and leans back on the motorbike under the gate, lips closed in a contented smile, as golden sunlight spills through the arch around him. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Sáng hôm sau, ông Lâm lại đội mũ cối, dựng xe dưới cổng Ô, đợi khách như chưa từng có chuyện gì." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: sparrows chirping, a broom sweeping the pavement, a vendor's hand bell, distant motorbike horns. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 2 (`canh-27/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: A steel table at the bustling bún chả shop with bowls of noodles, a basket of fresh herbs and a small paper bill with faint unreadable lines in the middle, charcoal smoke drifting, no person in frame.
- 3.0–7.0s: @BaHoa and @Khoa reach for the bill at the same instant from opposite sides of the table, each pinching one end of it and glaring across at the other.
- 7.0–10.0s: Neither lets go: @BaHoa narrows her eyes and @Khoa lifts his chin, both lips pressed into stubborn little smiles as grill smoke curls between them. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ở quán bún chả, bà Hoa và ông Khoa lại tranh nhau trả tiền chầu sáng, không ai chịu nhường ai." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pork sizzling on charcoal, a paper bill crinkling, chopsticks clinking, street bustle. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 3 (`canh-27/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A bright university campus gate with tall trees and students passing in the morning.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- Extra: a few students walking past in the background
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide shot slow crane-down; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A bright university campus gate in the morning, tall trees swaying over the entrance path and sunlight dappling the pavement, no person in frame.
- 3.0–7.0s: @Mai strides through the gate past a few students with her small black backpack, a laptop hugged under one arm, bright eyes behind her round glasses.
- 7.0–10.0s: @Mai sits on a bench under a tree, opens the laptop on her knees and types fast, its blank screen glowing on her face, lips set in a determined closed-mouth smile. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Mai trở lại giảng đường, cô đang viết một ứng dụng mới giúp sinh viên nhận ra các app cho vay lừa đảo." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong, rustling leaves, bicycle bells, rapid keyboard clicks. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 4 (`canh-27/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn in Hà Nội's old quarter: an ancient brick city gate with a tiled roof, narrow streets of tube houses with green shutters, tangled overhead wires, street vendors with shoulder poles, pink-gold morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: a nervous young man in a delivery jacket approaching
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The ancient brick city gate in golden morning light, the old cream-colored step-through motorbike with a round chrome headlamp parked under the arch and a vendor's shoulder pole leaning against the wall, no person in frame.
- 3.0–7.0s: @Lam sits sideways on the motorbike under the gate as a young man in a delivery jacket approaches from screen-right, glancing left and right, hugging his helmet to his chest.
- 7.0–10.0s: The young man stops a step away with lips pressed shut and points a hesitant finger at @Lam's right sleeve, eyebrows raised in a silent question, while @Lam looks up at him with calm narrow eyes. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Rồi một cậu thanh niên rụt rè tiến lại gần, nhìn quanh, rồi khẽ hỏi ông có phải là Lâm Rồng không." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: sparrows chirping, morning traffic hum, shuffling footsteps, a distant vendor's bell. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 5 (`canh-27/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn in Hà Nội's old quarter: an ancient brick city gate with a tiled roof, narrow streets of tube houses with green shutters, tangled overhead wires, street vendors with shoulder poles, pink-gold morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: a nervous young man in a delivery jacket approaching
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Lam smiles up at the young man and answers in a calm husky voice, face and lips clearly visible, tugging his sleeve down over his forearm.
- 3.0–7.0s: @Lam finishes warmly, pats the motorbike's back seat twice with his palm, then closes his mouth and tilts his head toward the seat.
- 7.0–10.0s: @Lam gives a knowing closed-mouth wink as the young man's shoulders relax and he climbs onto the back seat behind him. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.8s, spoken on camera by @Lam (man of 63, strictly standard Hà Nội Northern accent (never Southern accent), calm husky low voice with dry humor, speaking at a brisk, steady pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cậu nhầm người rồi, tôi chỉ là ông già xe ôm thôi, nhưng cứ ngồi lên, kể tôi nghe chuyện gì." (no subtitles)
- @Lam's face and lips stay clearly visible while speaking; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a palm patting a vinyl seat, sparrows chirping, the old engine coughing to life. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 6 (`canh-27/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: Golden morning aerial low over the ancient brick city gate with its tiled roof as the old cream-colored step-through motorbike with a round chrome headlamp, carrying two tiny riders, rolls out from under the arch into the street.
- 3.0–7.0s: The drone rises and pulls back as the little cream motorbike weaves into the narrow streets between tube houses, tangled wires and fluttering laundry, sunlight flaring off its chrome headlamp.
- 7.0–10.0s: A flock of pigeons sweeps across the frame as the camera soars high above a vast sea of tiled roofs glowing gold, the whole old quarter of Hà Nội waking below in a grand sunlit panorama. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Găng tơ đã tái xuất, và phố cổ Hà Nội từ hôm nay lại có một con rồng thức giấc canh giữ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a rising morning breeze, a flock of pigeons' wings fluttering, distant motorbike horns and bicycle bells, the old engine puttering away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```
