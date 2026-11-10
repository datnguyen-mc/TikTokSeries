# Găng Tơ Tái Xuất — Bộ 108 Prompt Google Flow Omni (27 Cảnh × 4 Clips × 15s)

- **Không có người dẫn chuyện:** 100% lời thoại do nhân vật nói trên hình — cả 108 clip là thoại khớp khẩu hình. Giọng gốc của mỗi nhân vật (tuổi, chất giọng, giọng Hà Nội) giữ nguyên văn ở mọi clip để Omni không đổi người nói.
- **Nhịp giọng theo cảnh:** mỗi lượt thoại có nhịp riêng nối sau giọng gốc — **nhanh** (cãi vã, hoảng hốt, rượt đuổi, khoe khoang; tốc độ ×1.2), **vừa** (trò chuyện thường), **chậm** (xúc động, thú nhận, câu chốt lặng người; tốc độ ×0.9). Khung thoại tính theo nhịp nên câu chậm ít chữ hơn. Cả phim: 72 lượt nhanh, 70 lượt vừa, 34 lượt chậm.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 108 clips × 15s, tất cả là clip thoại (32 clip có hai lượt thoại); lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 20 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 88 clip ảnh nhân vật (Ingredients), 0 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** không có clip VO nên runner không tăng tốc giọng clip nào; tốc độ nói nằm trong prompt (nhịp từng lượt) để khớp khẩu hình.
- **Màu phim & ánh sáng:** Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py gang-to-tai-xuat` sinh lại toàn bộ clip, README, kịch bản.

---

## Cảnh 01 - Clip 1 (`canh-01/clip-1.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn aerial over the tiled roofs of Hà Nội's old quarter: an ancient brick city gate, tangled wires, motorbikes streaming, pink-gold light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: motorbike riders streaming past the gate in the distance
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the old man wiping his motorbike under the brick gate arch, slow push-in.
- Shot 2, 4–8s: 85mm close-up of the old man's face over the round chrome headlamp, locked off.
- Shot 3, 8–11s: 50mm medium shot from the side of the motorbike, slow arc.
- Shot 4, 11–13s: 85mm close-up of the old man settling his pith helmet, locked off.
- Shot 5, 13–15s: 24mm aerial drone shot rising from the brick city gate over the tiled roofs at sunrise.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Under the ancient brick city gate at dawn, @Lam wipes the seat of the old cream-colored step-through motorbike with a cloth and is already speaking to it fondly, his face clearly visible.
- 1–2s (Shot 1): @Lam keeps talking to the motorbike with a crooked grin, patting the handlebar like an old horse's neck.
- 2–3s (Shot 1): @Lam leans down and taps the round chrome headlamp with one knuckle as he goes on, eyebrows raised.
- 3–4s (Shot 1): @Lam keeps speaking in a teasing tone while motorbike riders stream past the gate far behind him.
- 4–5s (CUT to Shot 2): @Lam polishes the round chrome headlamp in slow circles with the cloth, talking to it face to face.
- 5–6s (Shot 2): @Lam breathes on the chrome and keeps talking, his face curving in its reflection.
- 6–7s (Shot 2): @Lam rubs the headlamp until it gleams, still talking to it with a fond smile.
- 7–8s (Shot 2): @Lam wags one finger at the headlamp as he speaks, a teasing warning in his narrow eyes.
- 8–9s (CUT to Shot 3): @Lam straightens up beside the motorbike and keeps talking, tucking the cloth into his windbreaker pocket.
- 9–10s (Shot 3): @Lam pats the cream seat twice and goes on, nodding toward the street.
- 10–11s (Shot 3): @Lam lifts a battered green pith helmet from the handlebar and keeps talking.
- 11–12s (CUT to Shot 4): @Lam says the last words with a mock-stern frown at the motorbike.
- 12–13s (Shot 4): @Lam finishes, closes his mouth and settles the pith helmet on his grey crew cut.
- 13–14s (CUT to Shot 5): The view lifts away from the gate arch, @Lam small below swinging onto the motorbike, mouth closed, as the engine coughs awake.
- 14–15s (Shot 5): Pink-gold sunrise spills across a sea of mossy tiled roofs and tangled wires while motorbikes stream past the ancient gate. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, fond and teasing, like to an old friend), in Vietnamese with exact lip-sync, said exactly once: "Nào, con ngựa sắt. Hôm qua mày khục khặc cả buổi chiều, sáng nay đã khoẻ chưa? Để ông lau cái đèn cho bóng đã nào. Lát chở các cụ đi chợ, đi cho êm vào, đừng giở chứng giữa đường mà ông mất mặt đấy." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a chorus of distant motorbike horns waking the streets, a faraway street vendor's call, pigeons' wings fluttering past, a cloth squeaking on chrome. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 2 (`canh-01/clip-2.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn in Hà Nội's old quarter: an ancient brick city gate with a tiled roof, narrow streets of tube houses with green shutters, tangled overhead wires, street vendors with shoulder poles, pink-gold morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: a tiny old lady with a conical hat and a shopping basket
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot from the front of the motorbike on the old man turning toward the back seat, slow arc.
- Shot 2, 4–7s: 85mm close-up of the old man looking over his shoulder, locked off.
- Shot 3, 7–10s: 40mm medium shot from the side, the old man in front and the old lady on the back seat, slow push-in.
- Shot 4, 10–13s: 85mm close-up of the old man's crinkled smile, locked off.
- Shot 5, 13–15s: 35mm wide shot of the motorbike rolling out from under the brick city gate, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam sits astride the old cream-colored step-through motorbike under the brick city gate, turns over his shoulder and is already speaking warmly, patting the back seat.
- 1–2s (Shot 1): @Lam keeps talking gently as a tiny old lady in a conical hat steps up beside the back seat with her woven basket.
- 2–3s (Shot 1): @Lam nods at each careful step and keeps fussing while she climbs on slowly by herself.
- 3–4s (Shot 1): @Lam keeps talking over his shoulder as she settles and hugs her basket on her lap.
- 4–5s (CUT to Shot 2): @Lam gestures at the basket and goes on, his crinkled eyes warm.
- 5–6s (Shot 2): @Lam's eyebrows rise at the folded banknotes she holds out, and he keeps speaking.
- 6–7s (Shot 2): @Lam shakes his head and talks on with a gentle wave of his hand, refusing the money.
- 7–8s (CUT to Shot 3): @Lam keeps talking softly, his palm still raised, as the old lady slowly tucks the banknotes back into her basket.
- 8–9s (Shot 3): @Lam nods with satisfaction and goes on, tapping the handlebar.
- 9–10s (Shot 3): @Lam keeps speaking with a sly grin, as if sealing a deal.
- 10–11s (CUT to Shot 4): @Lam adds a last little request with a playful wink over his shoulder.
- 11–12s (Shot 4): @Lam keeps talking for a moment more, his crinkled eyes smiling.
- 12–13s (Shot 4): @Lam finishes, closes his mouth into a crinkle-eyed grin and faces forward.
- 13–14s (CUT to Shot 5): The motorbike rolls out from under the brick city gate into the pink-gold morning, @Lam's mouth closed.
- 14–15s (Shot 5): The old lady sits snug on the back seat hugging her basket as they putter away down the street. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, warm and fussing), in Vietnamese with exact lip-sync, said exactly once: "Cụ Tý lên đi, từ từ thôi, bước chân này trước. Ngồi vững chưa ạ? Ôm cái giỏ cho chắc vào. Ơ kìa, lại tiền. Cụ cất đi, cháu chở cụ như chở mẹ cháu, lấy tiền gì. Cụ muối dưa thì cho cháu một bát." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the motorbike engine idling, a basket handle creaking, sparrows chirping, distant horns echoing off the gate. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 3 (`canh-01/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn in Hà Nội's old quarter: an ancient brick city gate with a tiled roof, narrow streets of tube houses with green shutters, tangled overhead wires, street vendors with shoulder poles, pink-gold morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: an old street vendor woman in a conical hat with a shoulder pole of fruit baskets, standing on the far pavement
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium side-tracking shot gliding alongside the rider.
- Shot 2, 4–8s: 85mm close-up of the old man's face and bared forearm at the handlebar, tracking.
- Shot 3, 8–13s: 50mm medium shot from the front, the rider coming toward the lens, slow pull-back.
- Shot 4, 13–15s: 100mm extreme close-up of the grey sleeve sliding over the tattoo, tracking.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam rides the old cream motorbike slowly down a narrow street of tube houses as a gust flips back his windbreaker sleeve, and he glances down and is already speaking under his breath.
- 1–2s (Shot 1): @Lam keeps muttering to his bare forearm, one eyebrow raised, steering with his left hand.
- 2–3s (Shot 1): @Lam shakes his head at the forearm and goes on, dry and hushed.
- 3–4s (Shot 1): @Lam keeps talking softly, pink-gold light flickering across his face between the houses.
- 4–5s (CUT to Shot 2): The clawed tail of a dark-green dragon tattoo gleams on his wrinkled forearm just below @Lam's face as he keeps speaking to it softly.
- 5–6s (Shot 2): @Lam narrows his cloudy left eye at the tattoo and goes on talking, scolding it like a child.
- 6–7s (Shot 2): @Lam's lips keep moving in a hushed mutter as golden light slides across his face.
- 7–8s (Shot 2): @Lam tilts his head at the tattoo and asks it something dryly, half amused.
- 8–9s (CUT to Shot 3): @Lam lifts his eyes to the road and keeps talking, the motorbike rolling toward the lens.
- 9–10s (Shot 3): @Lam passes an old street vendor woman with a shoulder pole on the far pavement, still murmuring.
- 10–11s (Shot 3): @Lam keeps talking under his breath with a faint knowing smile.
- 11–12s (Shot 3): @Lam says the last words and glances at the vendor.
- 12–13s (Shot 3): @Lam finishes, closes his mouth and lifts two fingers in a small salute toward the vendor.
- 13–14s (CUT to Shot 4): @Lam's fingers tug the grey sleeve back down over the dragon's clawed tail.
- 14–15s (Shot 4): The sleeve settles flat over the tattoo as the motorbike putters on in the morning light. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, hushed and dry, half to himself), in Vietnamese with exact lip-sync, said exactly once: "Gió với chả gió. Thò đuôi ra làm gì hả con? Ngủ tiếp đi, ngoan nào. Mấy chục năm rồi, còn nhớ phố à? Phố bây giờ chỉ có các bà đi chợ với trẻ con đi học thôi, chẳng ai cần đến mày nữa đâu." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft putter of an old motorbike engine, a shoulder pole creaking, a rush of wind flapping fabric, a single low gong-like hum fading. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 4 (`canh-01/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the old man walking his motorbike to the closed shutter, gentle tracking.
- Shot 2, 4–8s: 85mm close-up of the old man's face tilted toward the shutter, locked off.
- Shot 3, 8–13s: 40mm medium shot from inside the alley, the old man beside the shutter facing the lens.
- Shot 4, 13–15s: 100mm extreme close-up of the thin line of warm light under the shutter, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam walks the old cream motorbike into the narrow night alley under a single yellow streetlamp, stops at his closed rolling shutter and is already speaking under his breath.
- 1–2s (Shot 1): @Lam keeps muttering as he lowers the side stand with his sandal.
- 2–3s (Shot 1): @Lam takes off the battered green pith helmet and keeps talking quietly, eyes on the shutter.
- 3–4s (Shot 1): @Lam keeps speaking low, nodding at the thin line of warm light under the shutter.
- 4–5s (CUT to Shot 2): @Lam tilts his head toward the light under the shutter as he goes on, his face lit yellow by the lamp.
- 5–6s (Shot 2): @Lam narrows his cloudy left eye and keeps speaking low, listening between phrases.
- 6–7s (Shot 2): @Lam asks himself a question under his breath, one grey eyebrow lifting.
- 7–8s (Shot 2): @Lam answers himself with a small dry shake of the head, still murmuring.
- 8–9s (CUT to Shot 3): @Lam turns his face toward the lens and keeps speaking quietly, the helmet hanging from his hand.
- 9–10s (Shot 3): @Lam rubs his thumb along the helmet brim and keeps talking to himself.
- 10–11s (Shot 3): @Lam shakes his head slowly as he goes on, his voice dropping.
- 11–12s (Shot 3): @Lam says the last words almost in a whisper.
- 12–13s (Shot 3): @Lam finishes, closes his mouth and stands very still beside the shutter.
- 13–14s (CUT to Shot 4): The line of warm light under the shutter flickers as someone moves inside.
- 14–15s (Shot 4): A shadow passes across the line of light under the shutter, then everything goes still. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, low and uneasy, thinking aloud), in Vietnamese with exact lip-sync, said exactly once: "Lại thì thầm. Đêm qua cũng thế, đêm kia cũng thế. Gọi cho ai mà cứ phải đợi ông ngủ mới dám gọi? Người yêu à? Thế thì đã cười. Con bé này giấu ai chứ giấu ông sao được, giọng run thế kia cơ mà." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a motorbike engine ticking as it cools, a faint muffled whisper behind the steel shutter, a dog barking far away, water dripping from the wires. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 1 (`canh-02/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 85mm close-up of the granddaughter glaring at the buzzing phone in the laptop glow, slow push-in.
- Shot 2, 4–8s: 50mm medium shot of the granddaughter at the table, locked off.
- Shot 3, 8–12s: 85mm close-up of her face over the phone, locked off.
- Shot 4, 12–15s: 50mm medium shot of the granddaughter at the table, the dark bed soft behind her, slow drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Inside the narrow tube house at night, @Mai leans into the lamplight in her oversized lavender hoodie, glares at a buzzing phone with a glowing blank screen and is already speaking to it in a hushed, exasperated voice.
- 1–2s (Shot 1): @Mai keeps talking to the phone, her face lit blue by the open laptop, nudging her round glasses up her nose.
- 2–3s (Shot 1): @Mai taps the glowing blank screen to reject the call and goes on muttering.
- 3–4s (Shot 1): @Mai keeps talking as the phone lights up and buzzes again at once.
- 4–5s (CUT to Shot 2): @Mai leans closer to the phone and hisses on at it, her brow knotted.
- 5–6s (Shot 2): @Mai taps the screen again with one finger, still talking under her breath.
- 6–7s (Shot 2): @Mai spreads both hands in disbelief and keeps whispering.
- 7–8s (Shot 2): @Mai rolls her eyes behind her round glasses and keeps complaining in a whisper.
- 8–9s (CUT to Shot 3): @Mai glances at the glowing laptop and goes on, lips tight, voice low.
- 9–10s (Shot 3): @Mai glances over her shoulder toward the dark back of the room and keeps whispering.
- 10–11s (Shot 3): @Mai turns back to the phone and goes on, hissing at it.
- 11–12s (Shot 3): @Mai says the last words through her teeth, then closes her mouth.
- 12–13s (CUT to Shot 4): @Mai flips the phone face-down and keeps her palm flat on top of it, mouth closed.
- 13–14s (Shot 4): @Mai glances toward the single bed at the dark back of the room, holding her breath, mouth closed.
- 14–15s (Shot 4): @Mai turns back to the table, her palm still on the phone, lips pressed together. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking at a natural, even conversational pace, hushed and exasperated), in Vietnamese with exact lip-sync, said exactly once: "Số lạ nữa, khuya thế này còn gọi. Chặn số này nó gọi số khác, chặn tiếp nó lại đổi số. Một đêm mười cuộc, điên mất. Học công nghệ thông tin mà chịu chết với chúng nó. Im đi, ông mà dậy là lộ hết." (no subtitles)
- @Mai starts talking within the first second; whenever @Mai speaks, the face and lips are clearly visible in that shot; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone vibrating hard against a wooden table, a quick soft tap on glass, muffled buzzing, a ticking wall fan. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 2 (`canh-02/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the granddaughter at the table, the dark bed soft behind her, holding the previous framing.
- Shot 2, 4–8s: 85mm close-up of her face in the blue and amber light, very slow push-in.
- Shot 3, 8–12s: 40mm medium shot from the side of the table, slow arc.
- Shot 4, 12–15s: 100mm extreme close-up of her eyes above her cupped hands, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Mai lifts her palm off the face-down phone, leans back from the table and is already whispering numbers to herself, the laptop's blue glow and the warm lamp lighting her face.
- 1–2s (Shot 1): @Mai keeps whispering, staring at the glowing blank laptop screen.
- 2–3s (Shot 1): @Mai raises one hand and folds down her thumb as she counts, still whispering.
- 3–4s (Shot 1): @Mai folds down a second finger, her lips moving quickly.
- 4–5s (CUT to Shot 2): @Mai keeps whispering the figures, her eyes fixed on the screen, her brow knotting.
- 5–6s (Shot 2): @Mai folds down a third and a fourth finger, still whispering.
- 6–7s (Shot 2): @Mai pauses between phrases and swallows, then goes on counting.
- 7–8s (Shot 2): @Mai's lips tremble as she whispers on, blinking fast behind her round glasses.
- 8–9s (CUT to Shot 3): @Mai shakes her head slightly, whispering the big final figure.
- 9–10s (Shot 3): @Mai presses a hand to her forehead and keeps whispering.
- 10–11s (Shot 3): @Mai glances toward the dark bed at the back as she whispers the last words.
- 11–12s (Shot 3): @Mai finishes in a near-silent breath, then closes her mouth.
- 12–13s (CUT to Shot 4): @Mai slowly presses her fingertips to her lips, eyes wide on the glowing screen.
- 13–14s (Shot 4): @Mai's eyes glisten behind her round glasses.
- 14–15s (Shot 4): @Mai lowers her hands to the table, squeezes her eyes shut and breathes out slowly. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking at a natural, even conversational pace, numb, counting in a whisper), in Vietnamese with exact lip-sync, said exactly once: "Mình vay có năm triệu thôi. Tuần đầu phí hồ sơ, tuần sau phí gia hạn, rồi phí nhắc nợ, phí phạt, lãi đẻ ra lãi. Ba tháng thôi mà, trời ơi, một trăm năm mươi triệu. Để ông biết thì ông ngủ làm sao được." (no subtitles)
- @Mai starts talking within the first second; whenever @Mai speaks, the face and lips are clearly visible in that shot; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the muffled buzz of a face-down phone, a wall clock ticking, incense crackling softly on the altar, a slow shaky exhale. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 3 (`canh-02/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the granddaughter crouched on the bottom step of the staircase, slow push-in.
- Shot 2, 4–8s: 85mm close-up of her face with the phone at her ear, locked off.
- Shot 3, 8–12s: 40mm medium shot from the foot of the stairs, slow arc.
- Shot 4, 12–15s: 100mm extreme close-up of her hand lowering the phone to her knee, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Mai crouches on the bottom step of the steep wooden staircase hugging her knees, the phone pressed to her ear, and is already whispering fast and pleading into it.
- 1–2s (Shot 1): @Mai keeps whispering quickly, one hand cupped around the phone to muffle her voice.
- 2–3s (Shot 1): @Mai nods hard as she pleads on, her face lit by the phone's pale glow.
- 3–4s (Shot 1): @Mai keeps whispering quickly, promising something with small nods.
- 4–5s (CUT to Shot 2): @Mai's brow knots and she asks a sharp whispered question into the phone.
- 5–6s (Shot 2): @Mai listens for a beat, then shakes her head and whispers faster, her eyes squeezing shut.
- 6–7s (Shot 2): @Mai's lips move fast and pleading, her eyes flicking toward the dark back of the room.
- 7–8s (Shot 2): @Mai keeps whispering, tears welling behind her round glasses.
- 8–9s (CUT to Shot 3): @Mai presses the phone harder to her ear and keeps pleading.
- 9–10s (Shot 3): @Mai whispers on in a broken rush, her free hand gripping her knee.
- 10–11s (Shot 3): @Mai begs once more in a tiny whisper, then calls softly into the phone.
- 11–12s (Shot 3): @Mai finishes, closes her mouth and listens to the silent line.
- 12–13s (CUT to Shot 4): @Mai slowly lowers the phone from her ear as the line goes dead, its screen fading to black.
- 13–14s (Shot 4): @Mai's fingers let the phone rest on her knee and clutch the hood strings of her lavender hoodie.
- 14–15s (Shot 4): @Mai's knuckles whiten around the hood strings as she holds very still. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.5s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, frantic pleading whisper), in Vietnamese with exact lip-sync, said exactly once: "Vâng, em biết rồi ạ. Anh cho em thêm một tuần thôi, em đi làm thêm trả dần mà. Sao hôm nay lại tăng nữa ạ? Không, em không trốn. Anh đừng nhắn cho bạn em nữa, cả cô chủ nhiệm cũng nhận được rồi. Em xin anh đấy. Anh ơi? A lô?" (no subtitles)
- @Mai starts talking within the first second; whenever @Mai speaks, the face and lips are clearly visible in that shot; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the quiet house ticking, a faint tinny buzz from the phone earpiece, the wooden step creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 4 (`canh-02/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 40mm medium two-shot across the dark room, the old man lying awake on the single bed in the foreground and the granddaughter at the foot of the stairs behind, slow push-in.
- Shot 2, 6–11s: 85mm close-up of the granddaughter at the foot of the stairs, locked off.
- Shot 3, 11–15s: 50mm medium shot from the foot of the bed on the old man, the staircase soft behind him, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam lies on his back under a thin blanket in the dark with his eyes open and is already speaking softly toward the staircase, where @Mai freezes on the bottom step with the phone at her chest, mouth closed.
- 1–2s (Shot 1): @Lam keeps speaking slowly, turning his head on the pillow toward the stairs.
- 2–3s (Shot 1): @Lam lifts himself onto one elbow as he asks, his voice low and even.
- 3–4s (Shot 1): @Lam keeps talking quietly, his narrow eyes on @Mai, who stays still with her mouth closed.
- 4–5s (Shot 1): @Lam adds one more quiet remark, watching her face.
- 5–6s (Shot 1): @Lam finishes and closes his mouth, and @Mai quickly wipes her eyes with her hoodie sleeve and starts answering fast with a bright forced smile.
- 6–7s (CUT to Shot 2): @Mai keeps talking quickly, nodding too much, her eyes red behind her round glasses.
- 7–8s (Shot 2): @Mai waves a hand toward the steep staircase as she rattles on.
- 8–9s (Shot 2): @Mai tucks the phone into her hoodie pocket and keeps talking brightly.
- 9–10s (Shot 2): @Mai says the last words with a too-wide smile.
- 10–11s (Shot 2): @Mai finishes, closes her mouth and holds the forced smile.
- 11–12s (CUT to Shot 3): @Lam lies back on the pillow and says one more gentle line toward the stairs, while @Mai hurries up the steep staircase behind him, mouth closed.
- 12–13s (Shot 3): @Lam keeps speaking gently as the creak of the stairs fades above.
- 13–14s (Shot 3): @Lam finishes his words softly, his eyes on the dark ceiling.
- 14–15s (Shot 3): @Lam closes his mouth and stares up at the dark ceiling, his jaw slowly tightening. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.3s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft, quietly probing): "Mai à, khuya rồi, con còn nói chuyện với ai đấy? Ông nghe tiếng con từ nãy."
- Turn 2, 5.8–10.6s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, too bright, covering a lie): "Dạ, bạn cùng lớp hỏi bài ạ. Sáng mai nó nộp đồ án. Cháu lên giường luôn đây, ông ngủ tiếp đi ạ."
- Turn 3, 11.1–14.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, gentle, letting it go): "Ừ. Uống cốc nước rồi hẵng ngủ, giọng khản đặc cả rồi."
- Pacing: @Lam speaks slowly and calmly, then @Mai answers quickly, then @Lam answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft sniff, a slow creak of the bed frame, quick light footsteps on wooden stairs, a gecko chirping on the wall. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 1 (`canh-03/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- Extra: three young men in black riding motorbikes behind him, faces in shadow
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium tracking shot of the lead rider, moving backward ahead of him.
- Shot 2, 4–8s: 85mm close-up of the bald rider shouting over his shoulder, tracking.
- Shot 3, 8–12s: 50mm medium shot of the lead rider braking before the shutter, slow push-in.
- Shot 4, 12–15s: 28mm wide shot of the four motorbikes lined up before the closed shutter, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Beo rides the lead black motorbike into the narrow wet alley, headlights sweeping the walls, turns his round face toward the riders behind him and is already shouting orders, his gold front tooth flashing.
- 1–2s (Shot 1): @Beo keeps shouting over his shoulder, pointing ahead with one thick arm at a cream motorbike parked by a closed shutter.
- 2–3s (Shot 1): @Beo revs the throttle and bellows on as the bikes weave down the lane in single file.
- 3–4s (Shot 1): @Beo keeps barking orders, water spraying from the puddles under his wheels.
- 4–5s (CUT to Shot 2): @Beo thumbs the horn and shouts on, grinning wide.
- 5–6s (Shot 2): @Beo jabs a thumb back at the last rider and keeps yelling.
- 6–7s (Shot 2): @Beo's voice booms off the walls as he keeps shouting, his shaved lightning-bolt head gleaming.
- 7–8s (Shot 2): @Beo jerks his chin toward the houses and keeps shouting, eyes on the green shutters.
- 8–9s (CUT to Shot 3): @Beo slows down, still bellowing, the yellow streetlamp sliding over his face.
- 9–10s (Shot 3): @Beo points at the closed rolling steel shutter ahead and keeps shouting.
- 10–11s (Shot 3): @Beo shouts the last words, his fake-gold chain swinging.
- 11–12s (Shot 3): @Beo finishes, closes his mouth into a smug grin and brakes before the shutter.
- 12–13s (CUT to Shot 4): @Beo plants one flip-flop on the wet pavement, engine idling, mouth closed.
- 13–14s (Shot 4): Four black motorbikes stand lined up before the closed shutter, three riders in black beside @Beo, engines idling.
- 14–15s (Shot 4): Exhaust haze drifts through the yellow lamplight over the idling bikes. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.3s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, loud swaggering bark), in Vietnamese with exact lip-sync, said exactly once: "Anh em ơi, cái xe máy màu kem đỗ trước cửa cuốn kia kìa! Rồ ga lên chúng mày, bấm còi cho thật to vào! Đứa đi cuối nẹt pô liên tục cho tao, nghe chưa! Đêm nay cả cái ngõ này phải dậy xem nhà nào dám quỵt tiền Phú Quý!" (no subtitles)
- @Beo starts talking within the first second; whenever @Beo speaks, the face and lips are clearly visible in that shot; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: four motorbike engines revving and popping, horns blaring, tires splashing through puddles, a dog barking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 2 (`canh-03/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium low-angle shot of the bald man with the bucket, smooth lateral dolly.
- Shot 2, 4–8s: 85mm close-up of the bald man bellowing up at the windows, locked off.
- Shot 3, 8–12s: 50mm medium shot of the bald man walking toward the shutter, slow arc.
- Shot 4, 12–15s: 28mm wide shot of the closed rolling steel shutter with the bald man in the foreground, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Beo strides into the lamplight in flip-flops, unhooks a dented bucket of red paint from a parked black motorbike's handlebar and is already shouting up at the dark windows of the alley.
- 1–2s (Shot 1): @Beo keeps bellowing, his fake-gold chain swaying over his black tank top as he turns in a circle.
- 2–3s (Shot 1): @Beo waves his free arm at the shuttered windows above, shouting on with a gold-toothed grin.
- 3–4s (Shot 1): @Beo jabs a finger at his own grinning face as he keeps shouting.
- 4–5s (CUT to Shot 2): @Beo leers up at a window and keeps mocking loudly, his gold front tooth glinting.
- 5–6s (Shot 2): @Beo spreads his arms wide and keeps shouting, the heavy bucket swinging.
- 6–7s (Shot 2): @Beo asks a mocking question up at the windows, cupping a hand to his ear.
- 7–8s (Shot 2): @Beo wipes his nose with the back of his hand and shouts on, eyes gleaming.
- 8–9s (CUT to Shot 3): @Beo walks toward the closed rolling steel shutter, still shouting.
- 9–10s (Shot 3): @Beo plants his flip-flops a few steps back from the shutter and keeps bellowing.
- 10–11s (Shot 3): @Beo raises his eyebrows comically and shouts the last mocking words.
- 11–12s (Shot 3): @Beo finishes, closes his mouth and lifts the bucket with both hands.
- 12–13s (CUT to Shot 4): @Beo heaves the bucket forward and a glossy arc of bright red paint splashes across the empty steel shutter.
- 13–14s (Shot 4): Red paint streams down the steel and pools on the doorstep.
- 14–15s (Shot 4): @Beo steps back to admire it, swinging the empty bucket, mouth closed in a smug grin. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.3s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, boastful mocking bellow), in Vietnamese with exact lip-sync, said exactly once: "Kính thưa bà con cô bác, mở cửa sổ ra mà xem! Sinh viên trường nào ở Hà Nội cũng biết mặt anh. Vay thì vui, đến lúc trả thì trốn à? Trốn được mấy hôm hả em? Không sao, bọn anh sơn lại cửa cho, miễn phí nhé, khỏi cảm ơn!" (no subtitles)
- @Beo starts talking within the first second; whenever @Beo speaks, the face and lips are clearly visible in that shot; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a metal bucket handle squeaking, a heavy wet splash of paint across corrugated steel, paint dripping and trickling, a dog barking two houses away. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 3 (`canh-03/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium two-shot from the side of the alley, the bald man on screen-left and the doorway on screen-right, slow push-in.
- Shot 2, 6–11s: 85mm close-up of the old man in the doorway, locked off.
- Shot 3, 11–15s: 50mm over-the-shoulder shot from behind the old man onto the bald man beside the cream motorbike, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): The red-streaked rolling shutter rattles up to reveal @Lam in his half-zipped grey windbreaker on screen-right, and @Beo on screen-left points at the house and is already speaking fast and loud, while @Lam's mouth stays closed.
- 1–2s (Shot 1): @Beo keeps talking loudly, jabbing a thick finger toward the doorway from a few steps away, his chain swinging.
- 2–3s (Shot 1): @Beo cocks his head and asks a mocking question, while @Lam stands still, mouth closed.
- 3–4s (Shot 1): @Beo leans forward with a gold-toothed sneer and goes on.
- 4–5s (Shot 1): @Beo holds up three fingers as he barks on.
- 5–6s (Shot 1): @Beo finishes and shuts his mouth in a smug grin, arms spread wide.
- 6–7s (CUT to Shot 2): @Lam looks up from the dripping paint and starts answering slowly in a calm low voice, his hands relaxed at his sides.
- 7–8s (Shot 2): @Lam keeps speaking slowly, his narrow eyes steady and unblinking.
- 8–9s (Shot 2): @Lam pauses, then goes on in the same low voice, nodding at the idling motorbikes.
- 9–10s (Shot 2): @Lam keeps talking evenly, unhurried.
- 10–11s (Shot 2): @Lam finishes, closes his mouth and gives a small nod toward the end of the alley.
- 11–12s (CUT to Shot 3): @Beo snorts and fires back a mocking question, standing beside the cream motorbike.
- 12–13s (Shot 3): @Beo keeps talking fast, looking @Lam up and down.
- 13–14s (Shot 3): @Beo finishes, folds his thick arms over his black tank top and closes his mouth.
- 14–15s (Shot 3): @Beo eyes the battered green pith helmet on the motorbike seat beside him, lips shut, while @Lam's shoulder stays still in the foreground. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, loud, smug and menacing): "Ra rồi à? Cháu ông nợ tiền bọn tôi, ông biết chưa? Ba ngày nữa không có tiền thì lần sau không phải sơn đâu!"
- Turn 2, 6.2–10.8s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, calm, low and unshaken): "Nó nợ bao nhiêu, tôi trả. Giờ thì tắt máy, về đi cho hàng xóm ngủ."
- Turn 3, 11.3–13.6s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, scoffing, thrown for a second): "Ông á? Ông chạy xe ôm thì lấy gì mà trả?"
- Pacing: @Beo speaks quickly, then @Lam answers slowly and calmly, then @Beo answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a steel shutter rattling and rolling up, paint dripping onto the step, motorbike engines idling behind, a window creaking open somewhere above. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 4 (`canh-03/clip-4.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm over-the-shoulder shot from behind the old man onto the bald man beside the cream motorbike, holding the previous framing.
- Shot 2, 4–8s: 50mm medium shot of the bald man swinging the pith helmet, slow arc.
- Shot 3, 8–11s: 85mm close-up of the bald man's sneering face, locked off.
- Shot 4, 11–13s: 40mm medium two-shot over the wide puddle, the old man by the shutter behind, slow tilt down.
- Shot 5, 13–15s: 100mm extreme close-up of the pith helmet rocking upside down in the puddle, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Beo unfolds his arms, lifts the battered green pith helmet off the cream motorbike seat and is already speaking fast with a gold-toothed sneer, dangling it from two fingers.
- 1–2s (Shot 1): @Beo keeps talking, turning the helmet around with a mock frown.
- 2–3s (Shot 1): @Beo pokes a finger through the frayed chin strap and keeps mocking, wrinkling his nose.
- 3–4s (Shot 1): @Beo sniffs the helmet with a grimace and goes on mocking loudly.
- 4–5s (CUT to Shot 2): @Beo swings the helmet by its chin strap and keeps talking, strolling toward a wide puddle under the yellow streetlamp.
- 5–6s (Shot 2): @Beo holds the helmet out toward @Lam with mock politeness, still talking.
- 6–7s (Shot 2): @Beo pulls it back with a wink and keeps sneering.
- 7–8s (Shot 2): @Beo stops at the edge of the puddle and goes on fast, the helmet swaying.
- 8–9s (CUT to Shot 3): @Beo holds the helmet out over the puddle and keeps sneering, his face and lips clearly visible.
- 9–10s (Shot 3): @Beo raises his eyebrows mockingly and goes on fast.
- 10–11s (Shot 3): @Beo leans forward and says the last mocking words, his gold tooth flashing in a wide grin.
- 11–12s (CUT to Shot 4): @Beo finishes and closes his mouth, the helmet dangling over the puddle, while @Lam stands still by the shutter, mouth closed.
- 12–13s (Shot 4): @Beo simply opens his fingers and the helmet drops into the puddle with a splash.
- 13–14s (CUT to Shot 5): The battered green pith helmet rocks upside down in the muddy puddle.
- 14–15s (Shot 5): Ripples spread under the yellow lamplight around the helmet as it settles, the reflected streetlamp trembling. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.3s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, sneering and mocking), in Vietnamese with exact lip-sync, said exactly once: "Ồ, hay là bán cái mũ cối này? Mũ gì mà sờn hết cả quai, lại còn hôi mùi dầu máy, mang ra đồng nát người ta cũng chê. Thôi, trả ông đây, giữ cho kỹ vào. Hôm nào bọn này quay lại, nhớ để sẵn tiền trong mũ nhé, ông già!" (no subtitles)
- @Beo starts talking within the first second; whenever @Beo speaks, the face and lips are clearly visible in that shot; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a hollow plop and splash of water, ripples lapping, a mocking snort, motorbike engines idling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 1 (`canh-04/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in a narrow old-quarter alley outside Lâm's tube house: a rolling steel shutter, wet pavement with puddles, a single yellow streetlamp, potted plants, tangled wires overhead.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the old man crouching over the puddle, slow tilt up.
- Shot 2, 4–8s: 85mm close-up of his weathered face above the helmet, locked off.
- Shot 3, 8–13s: 50mm medium low-angle shot of the old man standing with the helmet, locked off.
- Shot 4, 13–15s: 100mm extreme close-up of his cloudy left eye catching the lamplight, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam crouches slowly over the puddle under the yellow streetlamp in his grey windbreaker, lifts the battered green pith helmet out of the water with both hands and is already speaking to it under his breath.
- 1–2s (Shot 1): @Lam tips the helmet and lets the muddy water pour out of it, still murmuring.
- 2–3s (Shot 1): @Lam peers inside at the soaked lining and keeps talking softly, shaking his head.
- 3–4s (Shot 1): @Lam shakes the last drops off the brim as he goes on.
- 4–5s (CUT to Shot 2): @Lam wipes the helmet with his sleeve, round and round, speaking to it in a hushed voice.
- 5–6s (Shot 2): @Lam's lips move tenderly as he rubs a smear of mud from the brim.
- 6–7s (Shot 2): @Lam keeps talking softly to the helmet, turning it in his hands.
- 7–8s (Shot 2): @Lam taps the worn crown with one finger as he goes on.
- 8–9s (CUT to Shot 3): @Lam rises to his feet, still talking to the helmet.
- 9–10s (Shot 3): @Lam keeps wiping the brim with the hem of his windbreaker, murmuring.
- 10–11s (Shot 3): @Lam's voice drops lower as he keeps talking, a cold edge in his narrow eyes.
- 11–12s (Shot 3): @Lam says the last words, holding the helmet against his chest.
- 12–13s (Shot 3): @Lam finishes and closes his mouth, red paint dripping from the shutter behind him.
- 13–14s (CUT to Shot 4): @Lam's cloudy left eye catches the yellow lamplight as he lifts his gaze to the red-streaked shutter.
- 14–15s (Shot 4): @Lam's eye narrows slowly and stays fixed on the shutter, unblinking. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, hushed, tender, with a cold edge), in Vietnamese with exact lip-sync, said exactly once: "Ướt sũng cả rồi. Bùn ngấm vào tận cái lót mũ đây này. Mày theo ông bao nhiêu năm, nắng cũng đội, mưa cũng đội, chưa đứa nào dám thả mày xuống nước thế này. Lau khô đã nào. Rồi ông tính sau với chúng nó." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water trickling from the helmet, a slow drip of paint, crickets, distant motorbikes fading. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 2 (`canh-04/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 85mm close-up of the granddaughter at the foot of the stairs, locked off.
- Shot 2, 6–10s: 50mm over-the-shoulder shot from behind the granddaughter onto the old man at the table.
- Shot 3, 10–15s: 40mm medium profile two-shot of the granddaughter and the old man at the table, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Inside the tube house at night, @Mai stands at the foot of the staircase, eyes brimming, and is already speaking slowly in a breaking voice.
- 1–2s (Shot 1): @Mai keeps speaking, her chin trembling, both hands twisting the hem of her lavender hoodie.
- 2–3s (Shot 1): @Mai pauses to swallow, then goes on slowly, tears welling behind her round glasses.
- 3–4s (Shot 1): @Mai keeps talking, her voice cracking on the words.
- 4–5s (Shot 1): @Mai lifts her eyes toward the table as she says the last words.
- 5–6s (Shot 1): @Mai finishes and closes her mouth, lips pressed tight.
- 6–7s (CUT to Shot 2): @Lam at the table slowly lowers a towel from the damp pith helmet and asks a quiet question, his face clearly visible past @Mai's shoulder.
- 7–8s (Shot 2): @Lam keeps talking, very quiet, a stunned half-smile on his face.
- 8–9s (Shot 2): @Lam taps the corner of his cloudy left eye as he goes on.
- 9–10s (Shot 2): @Lam finishes and closes his mouth, staring at @Mai.
- 10–11s (CUT to Shot 3): @Mai steps up to the table and answers fast through her tears, while @Lam listens in profile, mouth closed.
- 11–12s (Shot 3): @Mai keeps talking quickly, wiping her cheek with her sleeve.
- 12–13s (Shot 3): @Mai points at her own eyes as she rushes on, tears spilling.
- 13–14s (Shot 3): @Mai finishes and closes her mouth, breathing hard.
- 14–15s (Shot 3): @Lam lifts his fingertips to the corner of his cloudy left eye, his lips quivering but pressed shut, his face in profile in the warm lamplight. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking slowly and softly, unhurried, with a short natural pause between phrases, close to tears, voice breaking): "Ông ơi, cháu xin lỗi. Cháu giấu ông mãi. Tiền ấy là cháu vay để ông đi mổ mắt."
- Turn 2, 6.2–9.8s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, stunned, very quiet): "Mổ mắt? Ai bảo con thế? Ông vẫn chạy xe ngon lành cơ mà."
- Turn 3, 10.3–13.7s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, rushing, tears spilling): "Hôm đưa ông đi khám, bác sĩ dặn riêng cháu. Để lâu nữa là mù hẳn."
- Pacing: @Mai speaks slowly and calmly, then @Lam answers at an even everyday pace, then @Mai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a shaky breath, the lamp buzzing softly, water dripping from the helmet onto the table. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 3 (`canh-04/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 13s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 40mm medium profile two-shot of the granddaughter and the old man at the table, holding the previous framing.
- Shot 2, 4–7s: 85mm close-up of the old man rising from his chair, slow push-in.
- Shot 3, 7–13s: 50mm over-the-shoulder shot from behind the old man onto the granddaughter.
- Shot 4, 13–15s: 40mm medium two-shot across the table, the old man's palm on the face-down phone, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam lowers his fingertips from his eye and is already speaking to @Mai softly in a low warm voice, while @Mai listens with her lips pressed together.
- 1–2s (Shot 1): @Lam keeps speaking slowly, shaking his head a little, his narrow eyes glistening.
- 2–3s (Shot 1): @Lam pauses between phrases and swallows, then goes on, @Mai's mouth closed.
- 3–4s (Shot 1): @Lam gives a small tired smile and keeps talking softly.
- 4–5s (CUT to Shot 2): @Lam keeps speaking slowly as he rises from his chair at the table.
- 5–6s (Shot 2): @Lam's voice catches as he asks his question, his weathered face in the warm lamplight.
- 6–7s (Shot 2): @Lam finishes the question and closes his mouth, eyes on his granddaughter.
- 7–8s (CUT to Shot 3): @Mai shakes her head and starts answering fast through her tears, her face clearly visible past @Lam's shoulder.
- 8–9s (Shot 3): @Mai keeps talking quickly, holding up her phone with its glowing blank screen.
- 9–10s (Shot 3): @Mai's voice rises as she rushes on, the phone trembling in her hand.
- 10–11s (Shot 3): @Mai keeps pleading fast, tears running under her round glasses.
- 11–12s (Shot 3): @Mai lowers the phone and keeps talking in a broken rush.
- 12–13s (Shot 3): @Mai says the last words, her chin quivering.
- 13–14s (CUT to Shot 4): @Mai finishes and closes her mouth, laying the phone face-down on the wooden table.
- 14–15s (Shot 4): @Lam rests his palm flat on top of the phone and looks up at @Mai, breathing slowly, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.0s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, tender and choked): "Mắt ông mờ thì cứ để nó mờ. Ông quen rồi. Con khổ thế này, ông nhìn rõ để làm gì hả con?"
- Turn 2, 7.5–13.6s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, panicked and pleading): "Nhưng mình trả không nổi đâu ông. Lãi mỗi ngày một tăng, bọn nó còn dọa gửi ảnh cháu cho cả lớp xem. Cháu chẳng dám đi học nữa."
- Pacing: @Lam speaks slowly and calmly, then @Mai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a muffled sob, the lamp humming, a floorboard creaking, a phone buzzing once against wood. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 4 (`canh-04/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot across the table, the old man's palm on the face-down phone, holding the previous framing.
- Shot 2, 5–9s: 85mm close-up of the granddaughter on the bottom stair, locked off.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the granddaughter on the bottom stair onto the old man, slow push-in.
- Shot 4, 13–15s: 85mm close-up of the old man turning toward the shutter, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam keeps his palm on the face-down phone and is already speaking to @Mai slowly and softly, while @Mai wipes her eyes under her round glasses, mouth closed.
- 1–2s (Shot 1): @Lam keeps speaking gently, nodding toward the steep staircase.
- 2–3s (Shot 1): @Lam touches his own cheek to show her, still talking softly.
- 3–4s (Shot 1): @Mai turns toward the staircase, mouth closed, as @Lam goes on, his face clearly visible in the warm lamplight.
- 4–5s (Shot 1): @Lam finishes, closes his mouth and watches her go.
- 5–6s (CUT to Shot 2): @Mai stops on the bottom stair, turns back and starts asking a small worried question.
- 6–7s (Shot 2): @Mai keeps talking softly, hugging herself in the lavender hoodie.
- 7–8s (Shot 2): @Mai's voice drops as she names the amount, eyes wide behind her round glasses.
- 8–9s (Shot 2): @Mai keeps talking in a small voice, biting her lip between words.
- 9–10s (CUT to Shot 3): @Mai closes her mouth, and @Lam starts answering slowly in a low steady voice, his face and lips clearly visible past @Mai's shoulder.
- 10–11s (Shot 3): @Lam keeps speaking slowly, his palm still flat on the phone, while @Mai listens, mouth closed.
- 11–12s (Shot 3): @Mai nods with her mouth closed and climbs the stairs out of frame as @Lam goes on, low and steady.
- 12–13s (Shot 3): @Lam's voice turns cold as he keeps talking, his eyes drifting toward the shutter.
- 13–14s (CUT to Shot 4): @Lam turns his face toward the rolling steel shutter and says the last words, cold as steel.
- 14–15s (Shot 4): @Lam closes his mouth, his narrow eyes hardening as he stares at a thin trickle of red paint seeping under the shutter. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.0s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, gentle and coaxing): "Thôi, lên ngủ đi con. Rửa cái mặt cho mát. Sáng mai còn lên giảng đường."
- Turn 2, 5.5–9.3s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking at a natural, even conversational pace, small and worried): "Thế còn nợ thì sao hả ông? Tận một trăm rưỡi đấy, đâu phải ít."
- Turn 3, 9.8–14.1s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft, then cold as steel): "Nợ của con thì ông lo. Ông trả chúng nó đủ cả gốc lẫn lãi."
- Pacing: @Lam speaks slowly and calmly, then @Mai answers at an even everyday pace, then @Lam answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: footsteps fading up the wooden stairs, a slow paint drip outside, a deep low hum swelling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 1 (`canh-05/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- Extra: rows of young callers in headsets at glowing monitors
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium tracking shot of the boss striding down the aisle, moving backward ahead of him.
- Shot 2, 4–7s: 85mm close-up of the boss's face as he walks, tracking.
- Shot 3, 7–10s: 50mm over-the-shoulder shot from behind a young caller onto the boss.
- Shot 4, 10–15s: 50mm medium shot of the boss stopped in the middle of the office, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): High in a glass tower under purple and gold neon, @Hung strides down the aisle between rows of callers in his oversized black satin bomber jacket and is already speaking loudly, his face clearly visible.
- 1–2s (Shot 1): @Hung keeps talking fast, a phone on a small selfie gimbal in one hand, snapping the fingers of the other at the callers.
- 2–3s (Shot 1): Young callers in headsets type faster as @Hung barks on, their mouths closed.
- 3–4s (Shot 1): @Hung spins around mid-stride and keeps shouting, pointing down the rows.
- 4–5s (CUT to Shot 2): @Hung sneers and goes on fast, his gold-rimmed glasses gleaming in the neon.
- 5–6s (Shot 2): @Hung taps his temple with a ringed finger as he keeps talking.
- 6–7s (Shot 2): @Hung counts off on his ringed fingers as he rattles on.
- 7–8s (CUT to Shot 3): @Hung leans over a caller's shoulder and keeps talking, his face clearly visible above the glowing monitor.
- 8–9s (Shot 3): @Hung mimes typing a message in the air and goes on fast.
- 9–10s (Shot 3): @Hung straightens up, grinning wide, still talking.
- 10–11s (CUT to Shot 4): @Hung stops in the middle of the room and says the last words with a flourish of his hand.
- 11–12s (Shot 4): @Hung finishes and closes his mouth, the callers bent over their keyboards behind him.
- 12–13s (Shot 4): @Hung winks at his own phone on the gimbal, mouth closed.
- 13–14s (Shot 4): @Hung smooths his ash-blond undercut with his ringed fingers.
- 14–15s (Shot 4): @Hung's silver rings flash under the neon as he raises the gimbal phone close to his face, lips closed in a smirk. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.3s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, loud, bossy and smug), in Vietnamese with exact lip-sync, said exactly once: "Gọi liên tục vào, nhanh tay lên! Tháng này mới thu được hai tỷ, các em định để anh ăn mì tôm à? Đứa nào khất thì gọi cho bố mẹ, cho người yêu, cho cả sếp nó. Không nghe máy thì nhắn tin. Sĩ diện là ra tiền đấy, nhớ chưa!" (no subtitles)
- @Hung starts talking within the first second; whenever @Hung speaks, the face and lips are clearly visible in that shot; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: keyboards clattering, phones ringing on every desk, white high-top sneakers squeaking on the polished floor, a gimbal motor whirring. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 2 (`canh-05/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the boss stopped in the middle of the office, holding the previous framing.
- Shot 2, 4–8s: 85mm close-up of the boss talking into his phone on the gimbal, locked off.
- Shot 3, 8–12s: 50mm medium shot of the boss fanning banknotes, the rows of desks blurred behind him, slow arc.
- Shot 4, 12–15s: 24mm wide shot pulling back over the rows of desks.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung holds the phone on its small selfie gimbal close to his face, flashes a wide grin at the lens and is already speaking loudly into it like a livestream salesman.
- 1–2s (Shot 1): @Hung keeps talking fast, flicking his ash-blond fringe, his gold-rimmed glasses gleaming in the purple and gold neon.
- 2–3s (Shot 1): @Hung points at the lens with a ringed finger as he hypes on.
- 3–4s (Shot 1): @Hung taps an imaginary button in the air and keeps talking fast.
- 4–5s (CUT to Shot 2): @Hung holds up five fingers to the lens and keeps talking.
- 5–6s (Shot 2): @Hung wags one finger as he rattles on, eyebrows raised.
- 6–7s (Shot 2): @Hung pulls a thick wad of banknotes from his bomber jacket and keeps talking.
- 7–8s (Shot 2): @Hung fans out the banknotes beside his face as he talks, his lips moving fast and clearly.
- 8–9s (CUT to Shot 3): @Hung waves the fanned banknotes at the phone and rattles on, the rows of callers blurred behind him.
- 9–10s (Shot 3): @Hung makes a heart shape with his fingers and keeps hyping.
- 10–11s (Shot 3): @Hung beckons the lens with two fingers as he says the last words.
- 11–12s (Shot 3): @Hung finishes his pitch and closes his mouth in a cocky grin.
- 12–13s (CUT to Shot 4): @Hung poses with the gimbal held high, the banknotes fanned in his other hand, mouth closed.
- 13–14s (Shot 4): The camera pulls back over the rows of callers in headsets typing at glowing monitors, @Hung small and posing in the middle.
- 14–15s (Shot 4): Purple and gold neon pulses along the ceiling above the busy desks while @Hung holds the pose, lips closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.5s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, slick livestream hype), in Vietnamese with exact lip-sync, said exactly once: "Chào cả nhà, anh lên sóng đây, hôm nay hai triệu người xem rồi! Sinh viên cần tiền gấp thì bấm cái nút vàng, năm phút có tiền, không thế chấp, lãi thấp nhất thị trường! Tiền thật đây này, thả tim cho anh đi các em, rủ cả bạn vào vay nữa!" (no subtitles)
- @Hung starts talking within the first second; whenever @Hung speaks, the face and lips are clearly visible in that shot; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a flutter of banknotes, a cheerful notification chime, keyboards clattering, a gimbal motor whirring. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 3 (`canh-05/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 50mm over-the-shoulder shot from behind the boss on the sofa onto the bald man.
- Shot 2, 7–12s: 85mm close-up of the boss on the white sofa, locked off.
- Shot 3, 12–15s: 40mm medium two-shot of the sofa and the glass door, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Inside a glass-walled boss room, @Beo stands before a white leather sofa rubbing his shaved head and is already reporting fast in a loud rough voice, his face clearly visible past @Hung's shoulder.
- 1–2s (Shot 1): @Beo keeps talking breathlessly, miming an old man riding a motorbike with his hands.
- 2–3s (Shot 1): @Beo waves both arms wide as he goes on.
- 3–4s (Shot 1): @Beo leans in eagerly, still talking fast, his gold front tooth flashing.
- 4–5s (Shot 1): @Beo jabs his thumb toward the window as he keeps talking.
- 5–6s (Shot 1): @Beo pulls a stiff blank face to imitate the old man and keeps talking.
- 6–7s (Shot 1): @Beo finishes and closes his mouth, waiting for an answer.
- 7–8s (CUT to Shot 2): @Hung lounges on the white leather sofa, lets out a short scoff and starts answering with a lazy mocking smirk.
- 8–9s (Shot 2): @Hung leans forward, elbows on his knees, and keeps talking coldly.
- 9–10s (Shot 2): @Hung twirls a silver ring on his finger as he goes on.
- 10–11s (Shot 2): @Hung's smirk widens as he lays out the plan, unhurried.
- 11–12s (Shot 2): @Hung tilts his head and keeps talking with a lazy shrug.
- 12–13s (CUT to Shot 3): @Hung says the last words and closes his mouth, flicking his ringed fingers toward the door.
- 13–14s (Shot 3): @Beo nods quickly and hurries out of the glass room, mouth closed.
- 14–15s (Shot 3): @Hung sinks back into the white sofa under the ring light, mouth closed in a smirk. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.7s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, eager breathless report): "Anh Hưng, vụ con bé Mai ấy, nhà nó có ông nội chạy xe ôm. Lão bảo nợ bao nhiêu lão trả hết. Lão nhìn bọn em, mặt lạnh tanh."
- Turn 2, 7.2–12.7s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking at a natural, even conversational pace, lazy, cold and mocking): "Xe ôm à? Già thì càng sợ mất mặt. Tung ảnh con bé lên nhóm lớp nó, xem lão có trả không."
- Pacing: @Beo speaks quickly, then @Hung answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the ring light humming, leather creaking, the glass door sliding shut, heavy flip-flop footsteps hurrying away. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 4 (`canh-05/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the boss at the window in three-quarter profile, slow arc.
- Shot 2, 4–8s: 85mm close-up of his face beside his reflection in the glass, locked off.
- Shot 3, 8–13s: 50mm medium shot of the boss facing the window, his reflection beside him, slow push-in.
- Shot 4, 13–15s: 24mm wide shot pulling back from the tall window over the city.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung strolls to the tall window of the glass boss room, slides his hands into his pockets and is already speaking to his own reflection in a smug drawl.
- 1–2s (Shot 1): @Hung keeps talking, his face in three-quarter profile against the glass.
- 2–3s (Shot 1): @Hung chuckles between words and goes on, rocking on his heels.
- 3–4s (Shot 1): @Hung waves one hand as if brushing away an old story, still talking.
- 4–5s (CUT to Shot 2): @Hung pulls a mocking face at his reflection as he asks a scornful question.
- 5–6s (Shot 2): @Hung bares his teeth at the glass in a mock toothless grin and keeps talking.
- 6–7s (Shot 2): @Hung smooths his ash-blond undercut with his ringed fingers and keeps talking.
- 7–8s (Shot 2): @Hung's smirk curls between his words as he stares down at the city.
- 8–9s (CUT to Shot 3): @Hung nods down at the old quarter far below and goes on, savoring each word.
- 9–10s (Shot 3): @Hung raises one eyebrow at his reflection and keeps speaking.
- 10–11s (Shot 3): @Hung taps the glass with one ringed knuckle as he says the last words.
- 11–12s (Shot 3): @Hung finishes with a scoff and closes his mouth in a smirk.
- 12–13s (Shot 3): @Hung admires his own reflection in the glass, mouth closed.
- 13–14s (CUT to Shot 4): The camera pulls back as @Hung stands small against the vast window, hands in his pockets.
- 14–15s (Shot 4): Far below, a cloud shadow slides slowly over the tiled roofs of the old quarter while @Hung stays still, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking at a natural, even conversational pace, smug, savoring every word), in Vietnamese with exact lip-sync, said exactly once: "Bố cứ kể mãi chuyện mấy ông trùm phố cổ hồi trước, nghe như phim. Rồng với Hổ gì? Giờ chắc rụng hết răng rồi. Nhìn mà xem này, cả cái khu dưới kia toàn con nợ. Đứa nào dám ngẩng mặt lên với tao, hả?" (no subtitles)
- @Hung starts talking within the first second; whenever @Hung speaks, the face and lips are clearly visible in that shot; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft air conditioner hum, a faint lift chime, distant traffic far below, a single low gong-like hum. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 1 (`canh-06/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium low-angle shot of the old man kneeling by the bed, locked off.
- Shot 2, 4–8s: 85mm close-up of his face over the rusty tin, slow push-in.
- Shot 3, 8–13s: 50mm medium shot of the old man holding the photo up in the lamplight, locked off.
- Shot 4, 13–15s: 100mm extreme close-up of the faded photo under his thumb, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam kneels on the tiled floor beside the single bed, slides a rusty round biscuit tin out of the dust and is already speaking to it under his breath.
- 1–2s (Shot 1): @Lam blows the dust off the lid and keeps murmuring.
- 2–3s (Shot 1): @Lam rubs the rust with his thumb and goes on softly, shaking his head.
- 3–4s (Shot 1): @Lam keeps talking as he wedges his thumbs under the stiff lid.
- 4–5s (CUT to Shot 2): @Lam pries the lid open with a creak and keeps speaking softly, peering inside.
- 5–6s (Shot 2): @Lam's eyebrows lift as he reaches into the tin, still murmuring.
- 6–7s (Shot 2): @Lam lifts out a faded photo of three young friends from the nineties, their faces tiny, and keeps talking.
- 7–8s (Shot 2): @Lam taps the tiny figures one by one with a fingertip as he names them.
- 8–9s (CUT to Shot 3): @Lam holds the photo up in the lamplight and chuckles as he keeps talking.
- 9–10s (Shot 3): @Lam shakes his head at the photo with a fond grin, still speaking softly.
- 10–11s (Shot 3): @Lam keeps talking, his eyes far away, the warm lamp lighting his face.
- 11–12s (Shot 3): @Lam says the last words with a soft laugh.
- 12–13s (Shot 3): @Lam finishes and closes his mouth, eyes on the photo.
- 13–14s (CUT to Shot 4): @Lam's thumb gently strokes the worn edge of the faded photo.
- 14–15s (Shot 4): The warm lamplight trembles across the three tiny faces in the photo as @Lam's thumb rests on its corner. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, hushed and nostalgic), in Vietnamese with exact lip-sync, said exactly once: "Rỉ hết cả rồi. Ba mươi năm không mở, chẳng biết còn gì bên trong. Mở xem nào. À, đây rồi. Hoa, Khoa, với thằng này. Tóc tai dựng ngược, trông láo chưa. Ngày ấy ba đứa đi đến phố nào là phố ấy dạt ra." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: metal scraping across tiles, a soft puff of dust, a rusty lid squeaking open, old paper rustling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 2 (`canh-06/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the old man at the table, locked off.
- Shot 2, 4–8s: 85mm close-up framing his face and raised tattooed forearm, slow push-in.
- Shot 3, 8–13s: 40mm medium shot across the table, locked off.
- Shot 4, 13–15s: 100mm extreme close-up of the dragon tattoo as his fingers curl closed, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam sits at the worn wooden table beside the open rusty tin, raises his right forearm into the lamplight and is already speaking to it in a low voice.
- 1–2s (Shot 1): @Lam slowly rolls the grey windbreaker sleeve up past his wrist as he keeps speaking.
- 2–3s (Shot 1): @Lam keeps talking low, rolling the sleeve higher toward his elbow.
- 3–4s (Shot 1): @Lam keeps speaking as the sleeve passes his elbow, his face clearly visible beside his arm.
- 4–5s (CUT to Shot 2): The full dark-green dragon tattoo coils from wrist to elbow beside @Lam's face as he keeps speaking to it.
- 5–6s (Shot 2): @Lam's lips move close above the tattoo, its scales and claws gleaming in the warm light.
- 6–7s (Shot 2): @Lam turns his forearm slowly, the whiskered dragon head catching the light, still talking.
- 7–8s (Shot 2): @Lam's voice hardens as he goes on, his eyes locked on the dragon.
- 8–9s (CUT to Shot 3): @Lam lowers his forearm to the table and keeps speaking, low and cold.
- 9–10s (Shot 3): @Lam glances up at the staircase where his granddaughter sleeps and keeps talking.
- 10–11s (Shot 3): @Lam looks back down at the dragon and goes on, his jaw set.
- 11–12s (Shot 3): @Lam says the last words slowly, almost a promise.
- 12–13s (Shot 3): @Lam finishes and closes his mouth, set in a firm line.
- 13–14s (CUT to Shot 4): @Lam slowly curls his fingers closed, the dragon tattoo flexing on his forearm.
- 14–15s (Shot 4): The dragon's scales ripple in the warm lamplight as his grip tightens. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, low, with cold resolve), in Vietnamese with exact lip-sync, said exactly once: "Dậy đi con, ngủ thế đủ rồi. Hôm nọ ông còn bảo mày nằm im. Sơn lên cửa, ông nhịn. Mũ xuống nước, ông cũng nhịn. Nhưng chúng nó làm con bé khóc cả đêm. Cái đấy thì ông không nhịn được, mà mày cũng không." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: fabric rustling as a sleeve rolls up, a deep low boom, incense crackling softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 3 (`canh-06/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night inside Lâm's narrow old-quarter tube house: a ground-floor room behind a rolling steel shutter, a worn wooden table, a small family altar with incense, a single bed at the back, a steep staircase, one warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the old man at the shelf with the receiver, slow push-in.
- Shot 2, 4–9s: 85mm close-up of his face with the receiver at his ear, locked off.
- Shot 3, 9–15s: 40mm medium shot from beside the staircase on the old man at the shelf, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam stands at a small shelf by the staircase, lifts the receiver of an old cream-colored landline phone to his ear with his tattooed forearm bared and is already speaking into it in a low, steady voice.
- 1–2s (Shot 1): @Lam keeps talking, winding the coiled cord around one finger.
- 2–3s (Shot 1): @Lam asks a dry question into the receiver, one thick grey eyebrow raised.
- 3–4s (Shot 1): @Lam raises his free hand as if to calm the voice on the line and goes on.
- 4–5s (CUT to Shot 2): @Lam keeps speaking evenly, a dry half-smile forming.
- 5–6s (Shot 2): @Lam's face hardens a little as he lowers his voice and keeps talking.
- 6–7s (Shot 2): @Lam pauses to listen, nods once and goes on.
- 7–8s (Shot 2): @Lam's lips move clearly under the warm lamp as he keeps talking.
- 8–9s (Shot 2): @Lam leans his shoulder against the wall and keeps speaking.
- 9–10s (CUT to Shot 3): @Lam glances at the dragon on his forearm as he keeps talking.
- 10–11s (Shot 3): @Lam says the last words slowly, almost amused.
- 11–12s (Shot 3): @Lam keeps speaking the final words, his narrow eyes glinting.
- 12–13s (Shot 3): @Lam finishes, closes his mouth and listens.
- 13–14s (Shot 3): @Lam holds the receiver against his ear, listening, mouth closed.
- 14–15s (Shot 3): The corner of @Lam's lips twitches upward as he listens, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, low and steady, with dry humor), in Vietnamese with exact lip-sync, said exactly once: "Hoa đấy à? Ừ, tôi đây. Còn nhận ra giọng tôi cơ à? Thôi, bà đừng mắng vội, nghe tôi nói đã. Có đứa động vào cháu tôi. Ừ, đúng cái Mai. Bà gọi giúp cả ông Khoa nữa nhé. Rồng cần Hổ với Báo rồi." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the click of an old receiver lifting, a faint line crackle, the lamp humming. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 4 (`canh-06/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 40mm medium shot from beside the staircase on the old man at the shelf, holding the previous framing.
- Shot 2, 4–8s: 85mm close-up of his face with the receiver, slow push-in.
- Shot 3, 8–13s: 50mm medium shot of the old man at the shelf reaching for the pith helmet, locked off.
- Shot 4, 13–15s: 85mm close-up of the old man settling the pith helmet on his head, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): The corners of @Lam's narrow eyes crinkle at the laugh down the line, and he is already speaking into the receiver again with dry warmth.
- 1–2s (Shot 1): @Lam keeps talking, a smile tugging at his mouth.
- 2–3s (Shot 1): @Lam keeps speaking warmly, nodding along to himself.
- 3–4s (Shot 1): @Lam taps his own chest with his thumb as he asks a wry question.
- 4–5s (CUT to Shot 2): @Lam taps his temple with one finger and keeps talking with a dry grin.
- 5–6s (Shot 2): @Lam nods along to himself as he goes on.
- 6–7s (Shot 2): @Lam raises one finger as if placing an order and keeps talking.
- 7–8s (Shot 2): @Lam keeps talking as he reaches for the battered green pith helmet on the shelf with his free hand.
- 8–9s (CUT to Shot 3): @Lam lifts the helmet and turns it in his hand, still speaking warmly.
- 9–10s (Shot 3): @Lam brushes a speck of dust off the brim as he goes on.
- 10–11s (Shot 3): @Lam tucks the helmet under his arm and keeps talking, a playful glint in his eye.
- 11–12s (Shot 3): @Lam says the last words with a dry grin.
- 12–13s (Shot 3): @Lam finishes, closes his mouth and sets the receiver on its cradle with a soft click.
- 13–14s (CUT to Shot 4): @Lam settles the battered green pith helmet on his grey crew cut.
- 14–15s (Shot 4): @Lam tilts the brim down and breaks into a sly closed-mouth smile. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, warm, wry and amused), in Vietnamese with exact lip-sync, said exactly once: "Bà vẫn cười cái kiểu ấy, nghe là biết chưa già. Còn tôi á? Già rồi, nhưng chưa lẩm cẩm đâu. Trưa mai tôi qua quán. Bà để phần tôi một suất, cứ ghi sổ như ngày trước, ăn no rồi còn đi làm việc lớn." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint line crackle, a receiver clicking onto its cradle, a deep low boom, the lamp humming warmly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 1 (`canh-07/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- Extra: a long line of customers waiting on the pavement
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the shop owner at the grills, the queue soft behind her, slow crane-up.
- Shot 2, 4–8s: 85mm close-up of her face in the smoke, locked off.
- Shot 3, 8–12s: 50mm medium shot of the shop owner pointing her fan at a steel table, locked off.
- Shot 4, 12–15s: 85mm close-up of the shop owner's face turning to the lens, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Thick smoke billows from charcoal grills on a sunny old-quarter pavement as @BaHoa, in her purple floral silk blouse, fans the coals briskly with a woven bamboo fan and is already shouting orders in a loud sing-song to a long line of customers.
- 1–2s (Shot 1): @BaHoa keeps calling out fast in a sing-song voice, flipping a pork patty with long chopsticks.
- 2–3s (Shot 1): @BaHoa points the bamboo fan toward a far table and shouts on.
- 3–4s (Shot 1): @BaHoa points the bamboo fan down the line of customers and keeps calling.
- 4–5s (CUT to Shot 2): @BaHoa's red lips rattle off the orders fast as orange sparks dance up through the smoke.
- 5–6s (Shot 2): @BaHoa narrows her eyes at the queue and keeps scolding in sing-song.
- 6–7s (Shot 2): @BaHoa wags the fan at someone in the queue, still calling, eyebrows raised.
- 7–8s (Shot 2): @BaHoa jerks her chin to one side and keeps calling, gold hoop earrings swinging.
- 8–9s (CUT to Shot 3): @BaHoa points the fan at a steel table and keeps shouting, her gold bangle jangling.
- 9–10s (Shot 3): @BaHoa waves the fan over the sizzling patties and keeps calling.
- 10–11s (Shot 3): @BaHoa sniffs the smoke with relish and calls out the last words.
- 11–12s (Shot 3): @BaHoa finishes and closes her red lips in a knowing curve.
- 12–13s (CUT to Shot 4): @BaHoa fans the charcoal twice more, mouth closed.
- 13–14s (Shot 4): @BaHoa glances toward the camera and gives a slow sly wink.
- 14–15s (Shot 4): @BaHoa's gold hoop earrings swing as she turns back to the grill, lips closed in a smirk. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.3s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking quickly in short lively phrases, every word still clear, brassy, bossy market sing-song), in Vietnamese with exact lip-sync, said exactly once: "Bàn ba hai suất, thêm đĩa nem, hai cốc trà đá! Bàn năm tính tiền! Ai đến sau thì xếp hàng cho tử tế, chen ngang là bà cho ăn bún không đấy nhé! Cái cậu áo xanh kia, đứng gọn vào cho người ta đi! Chả vừa ra lò, thơm chưa!" (no subtitles)
- @BaHoa starts talking within the first second; whenever @BaHoa speaks, the face and lips are clearly visible in that shot; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pork sizzling over charcoal, a bamboo fan whooshing in quick strokes, chopsticks clinking on bowls, gold bangles jangling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 2 (`canh-07/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 50mm medium shot of the shop owner at the grill, the old man stepping in at frame right, slow push-in.
- Shot 2, 7–13s: 85mm close-up of the old man leaning over the smoking grill, locked off.
- Shot 3, 13–15s: 50mm over-the-shoulder shot from behind the old man onto the shop owner at the grill, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam steps up to the smoky grill on screen-right with a battered green pith helmet under one arm, and @BaHoa looks up from the smoke and is already speaking to him fast and teasingly, while @Lam listens, mouth closed.
- 1–2s (Shot 1): @BaHoa keeps talking fast, waving the bamboo fan at him in mock disbelief.
- 2–3s (Shot 1): @BaHoa looks him up and down and points the fan at him across the grill, still teasing.
- 3–4s (Shot 1): @BaHoa cackles between words and goes on with a sharp grin.
- 4–5s (Shot 1): @BaHoa flips a patty and keeps talking without missing a beat.
- 5–6s (Shot 1): @BaHoa jerks her chin at the long queue as she rattles off the last words.
- 6–7s (Shot 1): @BaHoa finishes and closes her red lips into a smirk, one eyebrow cocked.
- 7–8s (CUT to Shot 2): @Lam leans toward her over the smoking grill and starts answering slowly in a low conspiratorial voice, his narrow eyes twinkling.
- 8–9s (Shot 2): @Lam keeps speaking slowly, smoke curling past his weathered face.
- 9–10s (Shot 2): @Lam shakes his head with a faint smile as he goes on.
- 10–11s (Shot 2): @Lam lowers his voice further and keeps talking, glancing once along the street.
- 11–12s (Shot 2): @Lam says the last words with a faint smile.
- 12–13s (Shot 2): @Lam finishes and closes his mouth, holding her gaze.
- 13–14s (CUT to Shot 3): @Lam taps the edge of the steel table twice with one finger, while @BaHoa stops fanning mid-stroke, lips pressed together.
- 14–15s (Shot 3): @BaHoa stares at @Lam over the grill, the bamboo fan frozen in her hand, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.5s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking quickly in short lively phrases, every word still clear, sharp, teasing jab): "Ối giời, ông còn sống đấy à? Ba mươi năm không thấy mặt, nay đến ăn chịu tiếp hay rủ tôi đi tù đấy? Nói nhanh tôi còn bán."
- Turn 2, 7.0–12.5s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, low and conspiratorial): "Rủ bà đi làm một vố. Không ai phải đi tù đâu. Lần này là việc thiện, bà ạ."
- Pacing: @BaHoa speaks quickly, then @Lam answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pork sizzling, charcoal popping, two light taps on a steel table, a motorbike horn on the street. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 3 (`canh-07/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm over-the-shoulder shot from behind the old man onto the shop owner at the grill, holding the previous framing.
- Shot 2, 3–8s: 85mm close-up of the old man in the drifting smoke, locked off.
- Shot 3, 8–13s: 40mm medium two-shot across the grill, both in profile, slow arc.
- Shot 4, 13–15s: 85mm close-up of the shop owner grinning in the smoke, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaHoa snaps the bamboo fan shut in the drifting smoke, points it at @Lam and is already asking quick questions, her red lips moving clearly, while @Lam's shoulder stays still in the foreground.
- 1–2s (Shot 1): @BaHoa keeps talking fast, rubbing her thumb and fingers together with a greedy grin.
- 2–3s (Shot 1): @BaHoa finishes and closes her mouth, eyebrows raised, waiting.
- 3–4s (CUT to Shot 2): @Lam leans in over the grill and starts answering slowly in a low calm voice.
- 4–5s (Shot 2): @Lam keeps speaking quietly, his eyes level and deadly calm.
- 5–6s (Shot 2): @Lam pauses between phrases, smoke drifting past his face, and goes on.
- 6–7s (Shot 2): @Lam keeps talking low, tapping two fingers on the steel table.
- 7–8s (Shot 2): @Lam says the last words almost in a whisper, then closes his mouth.
- 8–9s (CUT to Shot 3): @BaHoa breaks into a wide red-lipped grin and starts speaking fast and bold, while @Lam listens in profile, mouth closed.
- 9–10s (Shot 3): @BaHoa keeps talking fast and gleeful, wagging the closed fan.
- 10–11s (Shot 3): @BaHoa nudges a low plastic stool forward with her sandal as she goes on, her gold bangle jangling.
- 11–12s (Shot 3): @BaHoa taps the stool seat with the fan and keeps talking.
- 12–13s (Shot 3): @BaHoa beckons him down with the fan as she keeps talking.
- 13–14s (CUT to Shot 4): @BaHoa says the last words with a gleeful flick of the fan, then closes her mouth.
- 14–15s (Shot 4): @BaHoa tips her head back in silent laughter, lips closed, as smoke swirls past her face. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–2.5s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking quickly in short lively phrases, every word still clear, pouncing, eyes lit up): "Vố gì? Con mồi là ai, có béo bở không?"
- Turn 2, 3.0–7.9s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and deadly calm): "Thằng cho vay nặng lãi. Nó đang siết cháu tôi, với cả nghìn đứa sinh viên khác."
- Turn 3, 8.4–13.4s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking quickly in short lively phrases, every word still clear, bold and gleeful): "Lừa người tốt thì tôi giải nghệ rồi, chứ lừa thằng lừa đảo thì tôi đi ngay! Ông ngồi xuống đây, kể tôi nghe!"
- Pacing: @BaHoa speaks quickly, then @Lam answers slowly and calmly, then @BaHoa answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a bamboo fan snapping shut, a plastic stool scraping on the pavement, a fresh burst of sizzling, charcoal crackling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 4 (`canh-07/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the shop owner at the counter in profile, slow push-in.
- Shot 2, 4–8s: 85mm close-up of her face reflected in the round mirror, slow push-in.
- Shot 3, 8–12s: 50mm medium shot of the shop owner leaning to the mirror, locked off.
- Shot 4, 12–15s: 100mm extreme close-up of her lips as she paints them red, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaHoa hangs her checkered apron on a hook, leans toward a small round hand mirror propped on the steel counter and is already speaking to her own reflection in a low purr.
- 1–2s (Shot 1): @BaHoa keeps talking to the mirror, turning her face from side to side.
- 2–3s (Shot 1): @BaHoa widens her eyes at herself and keeps purring.
- 3–4s (Shot 1): @BaHoa pats her burgundy curls into place as she goes on.
- 4–5s (CUT to Shot 2): @BaHoa sucks in her waist, glances down at it and keeps talking with a wry pout.
- 5–6s (Shot 2): @BaHoa waves the thought away with one hand and keeps talking.
- 6–7s (Shot 2): @BaHoa's face fills the round mirror as she purses her lips and keeps speaking to it.
- 7–8s (Shot 2): @BaHoa uncaps a gold lipstick tube without looking, still talking to the mirror.
- 8–9s (CUT to Shot 3): @BaHoa tilts her chin up and goes on, eyes sharp.
- 9–10s (Shot 3): @BaHoa points the lipstick at the mirror as she keeps speaking, low and dangerous.
- 10–11s (Shot 3): @BaHoa gives a slow smile and keeps talking.
- 11–12s (Shot 3): @BaHoa says the last words and closes her mouth, lifting the lipstick.
- 12–13s (CUT to Shot 4): @BaHoa paints her lips a fresh bold red in two slow strokes.
- 13–14s (Shot 4): @BaHoa presses her lips together with a soft pop.
- 14–15s (Shot 4): @BaHoa's freshly painted red lips curve into a closed, dangerous smile. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking at a natural, even conversational pace, purring and dangerous), in Vietnamese with exact lip-sync, said exactly once: "Để xem còn dùng được không nào. Mắt vẫn sắc, tóc vẫn đẹp, còn eo thì, thôi bỏ qua. Chỉ có cái môi là nhạt quá. Đứa nào sắp được gặp bà thì cứ chuẩn bị sẵn khăn mà lau nước mắt đi. Tô lại tí." (no subtitles)
- @BaHoa starts talking within the first second; whenever @BaHoa speaks, the face and lips are clearly visible in that shot; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: apron strings rustling, a lipstick cap clicking off, the grill crackling behind, a deep low boom. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 1 (`canh-08/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tiny electronics repair stall tucked under a staircase in an old-quarter alley: shelves of old radios and phones, tangled wires, a soldering iron, a magnifier lamp, a single bare bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the repairman hunched over the workbench, locked off.
- Shot 2, 4–8s: 85mm close-up of his face and hands under the magnifier lamp, locked off.
- Shot 3, 8–13s: 50mm medium shot of the repairman holding up the opened phone, locked off.
- Shot 4, 13–15s: 100mm extreme close-up of the opened phone glowing on the bench, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In a tiny repair stall under a staircase, @Khoa hunches over the cluttered workbench in his brown multi-pocket vest, turns a locked old phone with a dark blank screen in his long bony fingers and is already speaking to it in a dry nasal deadpan.
- 1–2s (Shot 1): @Khoa sniffs at the phone and keeps talking, unimpressed.
- 2–3s (Shot 1): @Khoa keeps talking to the phone with a fussy little frown.
- 3–4s (Shot 1): @Khoa wags a bony finger at it as he goes on.
- 4–5s (CUT to Shot 2): @Khoa picks a tiny steel pick from the bench as he keeps talking.
- 5–6s (Shot 2): @Khoa peels back a tiny sticker on the phone's back and keeps talking, eyebrows raised.
- 6–7s (Shot 2): @Khoa scoffs and goes on, sliding the tiny pick into the phone's edge under the magnifier lamp.
- 7–8s (Shot 2): @Khoa murmurs to the phone soothingly, his fingers steady.
- 8–9s (CUT to Shot 3): @Khoa counts out loud as his fingers twist the tiny tools in a quick blur.
- 9–10s (Shot 3): The back panel pops open with a soft click and @Khoa keeps talking, unimpressed.
- 10–11s (Shot 3): @Khoa holds up the opened phone, its blank screen lighting with a plain glow, and keeps talking.
- 11–12s (Shot 3): @Khoa says the last words with a sniff, then closes his mouth.
- 12–13s (Shot 3): @Khoa dusts off his fingertips with a smug smile, mouth closed.
- 13–14s (CUT to Shot 4): @Khoa sets the opened phone down on the cluttered bench, its blank screen glowing.
- 14–15s (Shot 4): The phone's plain glow lights the scattered tiny screws on the bench. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, dry, fussy deadpan), in Vietnamese with exact lip-sync, said exactly once: "Khoá ba lớp cơ à? Oách nhỉ. Hồi tao còn đi mở két thì mày chưa được sinh ra đâu. Vít giấu dưới tem à? Trò trẻ con thôi. Nào, ngoan. Một, hai, ba. Đấy, bốn giây. Bảo chủ mày mua cái khoá xịn hơn đi." (no subtitles)
- @Khoa starts talking within the first second; whenever @Khoa speaks, the face and lips are clearly visible in that shot; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soldering iron hissing, tiny metallic clicks and scrapes, a crisp final click, an old radio crackling softly on a shelf. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 2 (`canh-08/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tiny electronics repair stall tucked under a staircase in an old-quarter alley: shelves of old radios and phones, tangled wires, a soldering iron, a magnifier lamp, a single bare bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 50mm medium shot of the repairman looking up from the workbench, the old man ducking in at frame right, locked off.
- Shot 2, 7–11s: 85mm close-up of the old man under the bare bulb, locked off.
- Shot 3, 11–15s: 40mm medium two-shot across the cluttered workbench, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam ducks under the low staircase into the cramped repair stall on screen-right, and @Khoa glances up from the workbench and is already speaking to him in a dry nasal deadpan, while @Lam listens, mouth closed.
- 1–2s (Shot 1): @Khoa keeps talking without getting up, pointing a tiny screwdriver at the low step above @Lam's head.
- 2–3s (Shot 1): @Khoa keeps talking, pointing the screwdriver at @Lam, who listens, mouth closed.
- 3–4s (Shot 1): @Khoa pulls a long heavy face to mimic him and goes on deadpan.
- 4–5s (Shot 1): @Khoa taps the screwdriver on the bench as he keeps talking.
- 5–6s (Shot 1): @Khoa nods to himself with a smug sniff as he says the last words.
- 6–7s (Shot 1): @Khoa finishes and closes his mouth, one eyebrow cocked.
- 7–8s (CUT to Shot 2): @Lam sets a locked phone with a dark blank screen on the workbench and starts answering in a calm low voice, his face clearly visible under the bulb.
- 8–9s (Shot 2): @Lam keeps speaking calmly, tapping the phone once with one finger.
- 9–10s (Shot 2): @Lam leans in slightly as he goes on, a glint in his narrow eyes.
- 10–11s (Shot 2): @Lam holds his thumb and finger a little apart, showing how small it is, and keeps talking.
- 11–12s (CUT to Shot 3): @Lam keeps talking, nodding at the phone, while @Khoa looks at it, mouth closed.
- 12–13s (Shot 3): @Lam raises one grey eyebrow and asks his playful last question.
- 13–14s (Shot 3): @Lam finishes, closes his mouth and slides the phone across the bench toward @Khoa with two fingers.
- 14–15s (Shot 3): @Khoa eyes the phone over his glasses, lips pressed together, while @Lam waits beside the bench. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.7s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, wry deadpan, not looking up): "Cúi đầu kẻo cộc cầu thang. Hoa Hổ gọi từ sáng, bảo thể nào ông cũng mò đến, mặt nặng như đeo đá. Đúng thật."
- Turn 2, 7.2–13.4s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, calm, playful challenge): "Có một cái két cần mở, nằm gọn trong cái điện thoại này. Két thời nay bé thế đấy. Tay ông còn nhanh không?"
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: footsteps on the stairs above, the bare bulb buzzing, a phone sliding across a wooden bench, a radio crackling low. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 3 (`canh-08/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 11s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium two-shot across the cluttered workbench, holding the previous framing.
- Shot 2, 3–7s: 85mm close-up of the repairman under the magnifier lamp, locked off.
- Shot 3, 7–11s: 50mm over-the-shoulder shot from behind the repairman onto the old man.
- Shot 4, 11–15s: 85mm close-up of the old man under the bare bulb, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khoa picks up the phone, weighs it in his palm with a scoff and is already speaking in a wry deadpan, wiggling his eyebrows, while @Lam listens, mouth closed.
- 1–2s (Shot 1): @Khoa keeps talking smugly, flipping the phone between his fingers.
- 2–3s (Shot 1): @Khoa ticks off items on his bony fingers as he goes on.
- 3–4s (CUT to Shot 2): @Khoa leans back on his stool and keeps talking, deadpan, his face clearly visible under the magnifier lamp.
- 4–5s (Shot 2): @Khoa sighs theatrically, one hand on his chest, still talking.
- 5–6s (Shot 2): @Khoa shakes his head with mock sorrow as he goes on.
- 6–7s (Shot 2): @Khoa finishes and closes his mouth, sniffing.
- 7–8s (CUT to Shot 3): @Lam's shoulders shake with silent laughter, then he starts answering slowly and dryly, his face clearly visible past @Khoa's shoulder.
- 8–9s (Shot 3): @Lam keeps speaking slowly, wiping the corner of his eye with a knuckle.
- 9–10s (Shot 3): @Lam taps his own chest as he goes on with a rueful grin.
- 10–11s (Shot 3): @Lam goes on in a dry low voice, a grin tugging at his mouth.
- 11–12s (CUT to Shot 4): @Lam points at the phone with one finger as he keeps talking.
- 12–13s (Shot 4): @Lam keeps speaking slowly, one eyebrow raised in mock warning.
- 13–14s (Shot 4): @Lam says the last words with a sly little smile.
- 14–15s (Shot 4): @Lam finishes and closes his mouth, still pointing at the phone, his eyes twinkling. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.7s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, smug, wiggling his eyebrows): "Thứ gì có khoá là tôi mở được hết. Cửa, két, xe. Trừ mỗi trái tim bà Hoa, bốn mươi năm rồi vẫn chịu chết."
- Turn 2, 7.2–14.1s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, dry and amused): "Cái khoá ấy thì cả phố này chịu, kể cả tôi. Ông cứ mở cái này trước đã, còn chuyện tình thì để sau."
- Pacing: @Khoa speaks at an even everyday pace, then @Lam answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone spinning on wood, the bare bulb buzzing, a radio crackling, tiny screws rattling on the bench. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 4 (`canh-08/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tiny electronics repair stall tucked under a staircase in an old-quarter alley: shelves of old radios and phones, tangled wires, a soldering iron, a magnifier lamp, a single bare bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the repairman leaning over the bench, locked off.
- Shot 2, 4–8s: 85mm close-up of his huge magnified eyes and face behind the thick lenses, locked off.
- Shot 3, 8–12s: 50mm medium shot of the repairman lining up his tools, locked off.
- Shot 4, 12–15s: 85mm close-up of his quivering hands raised over the tools, his grinning face behind them, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khoa pulls his thick magnifier glasses down from his forehead onto his eyes, stares at his own trembling hands over the workbench and is already speaking to them in a dry nasal voice.
- 1–2s (Shot 1): @Khoa holds up his trembling hands and keeps talking to them, frowning.
- 2–3s (Shot 1): @Khoa shakes his hands out and goes on deadpan.
- 3–4s (Shot 1): @Khoa keeps talking as his eyes swell huge and bright behind the thick lenses.
- 4–5s (CUT to Shot 2): @Khoa waves at an old radio on the shelf with disdain as he keeps talking.
- 5–6s (Shot 2): @Khoa peers at his fingers through the huge lenses and keeps talking, barely hiding a grin.
- 6–7s (Shot 2): @Khoa blinks his magnified eyes and goes on in a fussy murmur.
- 7–8s (Shot 2): @Khoa's lips twitch with glee as he keeps talking.
- 8–9s (CUT to Shot 3): @Khoa takes a slow deep breath through his nose, still murmuring to himself.
- 9–10s (Shot 3): @Khoa breathes out slowly, his shoulders dropping, as he keeps talking.
- 10–11s (Shot 3): @Khoa lines up the tiny screwdrivers one by one in a straight row as he says the last words.
- 11–12s (Shot 3): @Khoa nudges the last screwdriver into line and closes his mouth.
- 12–13s (CUT to Shot 4): @Khoa lifts his hands over the tools and wiggles his fingers like an eager boy, mouth closed.
- 13–14s (Shot 4): @Khoa's fingers quiver with little twitches above the row of tools.
- 14–15s (Shot 4): @Khoa grins with closed lips behind the huge lenses, his hands hovering over the tools. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, deadpan, barely hiding glee), in Vietnamese with exact lip-sync, said exactly once: "Ô hay, run à? Không phải tại già đâu nhé. Mười năm nay chỉ toàn thay pin với hàn dây loa, giờ mới có một vụ ra hồn. Sướng quá nên run thôi. Nào, hít một hơi sâu, thở ra. Từ từ nào, từng cái một." (no subtitles)
- @Khoa starts talking within the first second; whenever @Khoa speaks, the face and lips are clearly visible in that shot; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: glasses clicking into place, tiny tools rattling on the bench, an old radio crackling, a deep low boom. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 1 (`canh-09/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on an old-quarter street with colorful neon signs without readable letters and wet pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 35mm medium two-shot moving backward ahead of the two old men, low angle.
- Shot 2, 7–13s: 85mm close-up of the old man in the pith helmet, tracking.
- Shot 3, 13–15s: 50mm medium two-shot of the two old men reaching a half-lowered shutter, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): On a night street of the old quarter glowing with colorful neon signs without readable letters, @Khoa and @Lam walk abreast toward the low camera, and @Khoa on screen-left is already speaking out of the side of his mouth in a dry deadpan, while @Lam listens, mouth closed.
- 1–2s (Shot 1): @Khoa keeps talking, chin up, hands clasped behind his back.
- 2–3s (Shot 1): @Khoa sweeps one hand at the pavement ahead with a flourish as he goes on.
- 3–4s (Shot 1): @Khoa keeps talking with a secretly proud smile, his little ponytail bobbing.
- 4–5s (Shot 1): @Khoa puffs out his thin chest and keeps talking, glancing sideways at @Lam, whose mouth stays closed.
- 5–6s (Shot 1): @Khoa says the last words with a grand nod.
- 6–7s (Shot 1): @Khoa finishes and closes his mouth, strutting.
- 7–8s (CUT to Shot 2): @Lam starts answering slowly with a dry sidelong look, his face clearly visible in the neon glow under the battered green pith helmet.
- 8–9s (Shot 2): @Lam keeps speaking slowly, tilting his head toward his old friend.
- 9–10s (Shot 2): @Lam glances down at their slow shuffling feet and goes on, deadpan.
- 10–11s (Shot 2): @Lam's eyes crinkle as he keeps talking dryly.
- 11–12s (Shot 2): @Lam keeps speaking slowly, unhurried.
- 12–13s (Shot 2): @Lam waves @Khoa along with one hand and says the last words, while @Khoa listens, mouth closed.
- 13–14s (CUT to Shot 3): @Lam finishes and closes his mouth as they near a half-lowered shutter spilling warm bulb light onto the wet street.
- 14–15s (Shot 3): @Khoa and @Lam stop beside the half-lowered shutter, mouths closed, magenta and jade light rippling on the wet pavement. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.7s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, dry, secretly proud): "Lâu lắm mới lại được đi giữa phố đêm thế này. Ông thấy không, người ta vẫn dạt ra nhường đường. Oai như ngày xưa."
- Turn 2, 7.2–13.5s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, dry deadpan): "Người ta nhường vì hai ông già đi chậm quá. Con rùa bò còn vượt được. Nhanh lên, bà ấy đợi đấy."
- Pacing: @Khoa speaks at an even everyday pace, then @Lam answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: two pairs of slow footsteps in unison on wet pavement, the buzz of neon signs, distant motorbike horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 2 (`canh-09/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in Bà Hoa's bún chả shop after closing: plastic stools stacked, one warm bulb over a steel table, cold grills, the shutter half down, an old red landline phone on the counter.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 85mm close-up of the granddaughter's face lit blue by the laptop, locked off.
- Shot 2, 4–8s: 50mm over-the-shoulder shot from behind the shop owner onto the granddaughter at the laptop.
- Shot 3, 8–12s: 85mm close-up of the shop owner putting on big black sunglasses, locked off.
- Shot 4, 12–15s: 40mm medium two-shot across the steel table, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Inside the closed bún chả shop at night, @Mai sits at the steel table under one warm bulb with a glowing laptop turned away from the camera and is already speaking quickly and earnestly, her face lit blue.
- 1–2s (Shot 1): @Mai keeps talking, frowning at the screen and adjusting her round glasses.
- 2–3s (Shot 1): @Mai taps the edge of the laptop and goes on.
- 3–4s (Shot 1): @Mai looks up and keeps explaining, her voice low and quick.
- 4–5s (CUT to Shot 2): @Mai turns the laptop slightly toward @BaHoa and keeps talking, while @BaHoa listens, mouth closed.
- 5–6s (Shot 2): @Mai points at the glowing blank screen as she goes on.
- 6–7s (Shot 2): @Mai spreads her hands as she makes her point.
- 7–8s (Shot 2): @Mai jabs a finger toward the street as she says the last words, then closes her mouth.
- 8–9s (CUT to Shot 3): @BaHoa slips on a pair of big black sunglasses and starts answering fast with a grand haughty gesture.
- 9–10s (Shot 3): @BaHoa keeps talking fast, flicking her fingers like a grand lady, her red lips moving clearly.
- 10–11s (Shot 3): @BaHoa jangles her gold bangle and goes on in a grand voice.
- 11–12s (Shot 3): @BaHoa pats an imaginary stack of money on the table as she keeps talking.
- 12–13s (CUT to Shot 4): @BaHoa says the last words and closes her mouth, lifting her chin like a tycoon.
- 13–14s (Shot 4): @BaHoa fans herself slowly with a bamboo fan, mouth closed.
- 14–15s (Shot 4): @Mai presses her lips together to hold back a grin, while @BaHoa keeps fanning, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.9s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking at a natural, even conversational pace, earnest and quick): "Ứng dụng này đọc trộm cả danh bạ với ảnh trong máy người vay. Cháu đoán không chỉ mình cháu bị đâu. Máy chủ đặt ngay tại văn phòng nó."
- Turn 2, 8.4–12.8s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking quickly in short lively phrases, every word still clear, gleeful scheming): "Thế thì bà vào vai bà trùm bất động sản, xách mười tỷ đến tận nơi xin góp vốn với nó!"
- Pacing: @Mai speaks at an even everyday pace, then @BaHoa answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the laptop fan whirring, the bulb buzzing, a bamboo fan fluttering, a motorbike passing outside the half-down shutter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 3 (`canh-09/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in Bà Hoa's bún chả shop after closing: plastic stools stacked, one warm bulb over a steel table, cold grills, the shutter half down, an old red landline phone on the counter.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the old man leaning over the steel table, locked off.
- Shot 2, 4–7s: 85mm close-up of the old man, locked off.
- Shot 3, 7–11s: 40mm medium two-shot across the steel table, slow arc.
- Shot 4, 11–15s: 85mm close-up of the repairman holding up the brooch, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam leans over the steel table under the single warm bulb in the closed shop and is already speaking briskly, while @Khoa sits listening on screen-left, mouth closed.
- 1–2s (Shot 1): @Lam keeps talking, counting off the first role on his fingers.
- 2–3s (Shot 1): @Lam folds down a second finger and taps his own chest with his thumb as he goes on.
- 3–4s (Shot 1): @Lam folds down a third finger, pointing at @Khoa, and keeps speaking.
- 4–5s (CUT to Shot 2): @Lam folds down a fourth finger and keeps talking, brisk and commanding, his face clearly visible in the warm light.
- 5–6s (Shot 2): @Lam points toward the street outside as he goes on.
- 6–7s (Shot 2): @Lam asks a short sharp question and lays his hand flat on the table.
- 7–8s (CUT to Shot 3): @Lam closes his mouth, and @Khoa holds up a large gold flower brooch and starts answering dryly.
- 8–9s (Shot 3): @Khoa keeps talking, turning the brooch in the bulb light, while @Lam listens, mouth closed.
- 9–10s (Shot 3): @Khoa holds the brooch beside his face and goes on smugly.
- 10–11s (Shot 3): @Khoa taps the tiny glint at the center of the brooch and keeps talking.
- 11–12s (CUT to Shot 4): @Khoa wiggles the brooch like a magician and keeps talking dryly, his face clearly visible.
- 12–13s (Shot 4): @Khoa lowers his voice for the last words, eyebrows raised.
- 13–14s (Shot 4): @Khoa keeps the brooch raised as he finishes speaking.
- 14–15s (Shot 4): @Khoa closes his mouth and raises his eyebrows at @Lam, the brooch glinting. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.1s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, brisk and commanding): "Chia việc thế này. Bà ấy diễn, tôi lái xe, ông lo cái máy ghi hình, con bé ngồi ngoài xe giữ đường dây. Rõ chưa?"
- Turn 2, 7.6–14.1s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, dry and smug): "Có ngay, tôi làm từ chiều rồi. Cái trâm này có mắt, có cả tai. Thằng kia nói câu nào là cả nước nghe câu ấy."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a palm laid flat on a steel table, teacups clinking, a tiny electronic beep, the bulb humming. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 4 (`canh-09/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in Bà Hoa's bún chả shop after closing: plastic stools stacked, one warm bulb over a steel table, cold grills, the shutter half down, an old red landline phone on the counter.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm over-the-shoulder shot from behind the old man onto the granddaughter.
- Shot 2, 6–11s: 85mm close-up of the old man, locked off.
- Shot 3, 11–15s: 40mm medium two-shot across the steel table, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Mai sits down at the steel table hugging her laptop and is already speaking softly to @Lam, her face clearly visible past his shoulder, while @Lam shakes with silent laughter, mouth closed.
- 1–2s (Shot 1): @Mai keeps talking softly, smiling at him.
- 2–3s (Shot 1): @Mai tilts her head and goes on, her eyes shining behind her round glasses.
- 3–4s (Shot 1): @Mai keeps speaking warmly, her voice catching a little.
- 4–5s (Shot 1): @Mai points at him with a teasing smile as she goes on.
- 5–6s (Shot 1): @Mai says the last words with a little laugh.
- 6–7s (CUT to Shot 2): @Mai closes her mouth into a slow smile, and @Lam wipes the corner of his eye with a knuckle and starts answering slowly with a twinkle in his narrow eyes.
- 7–8s (Shot 2): @Lam keeps speaking slowly and warmly, his face clearly visible in the warm light.
- 8–9s (Shot 2): @Lam raises one finger like a solemn promise as he goes on.
- 9–10s (Shot 2): @Lam slips on a pair of big black sunglasses with a sly little shrug as he says the last words.
- 10–11s (Shot 2): @Lam finishes and closes his mouth, grinning behind the dark lenses.
- 11–12s (CUT to Shot 3): @Mai bursts out with a quick teasing question, eyes crinkling.
- 12–13s (Shot 3): @Mai keeps talking fast, giggling as she points at the sunglasses.
- 13–14s (Shot 3): @Mai keeps giggling through the last words.
- 14–15s (Shot 3): @Mai closes her mouth, holding back a laugh, while @Lam raises his small teacup toward her in a quiet toast, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.2s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking at a natural, even conversational pace, soft and moved): "Ba ông bà cười cứ như trẻ con. Cả năm nay cháu chưa thấy ông vui thế này. Ông cười to nhất đấy."
- Turn 2, 6.7–10.7s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, warm, with a sly twinkle): "Già rồi còn được đi chơi một chuyến, con ạ. Chuyến cuối, ông hứa."
- Turn 3, 11.2–14.2s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, teasing, holding back a giggle): "Chơi gì mà đeo kính đen ban đêm ạ? Ông định đóng phim à?"
- Pacing: @Mai speaks at an even everyday pace, then @Lam answers slowly and calmly, then @Mai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: teacups clinking, the bulb humming, crickets outside the half-down shutter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 1 (`canh-10/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning outside the marble lobby of a gleaming Hà Nội glass tower: a revolving door, potted palms, polished stone steps reflecting the light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; a crisp black chauffeur cap, faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a dark-green dragon tattoo on his right forearm hidden by his sleeve.
- Wardrobe: in this shot @Lam wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: two security guards in grey uniforms standing by the revolving door
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the chauffeur at the open driver's door of the black sedan, the glass tower behind him, gentle push-in.
- Shot 2, 4–8s: 85mm close-up of the chauffeur's face under the black cap, locked off.
- Shot 3, 8–12s: 40mm over-the-shoulder shot from behind a security guard onto the chauffeur, slow drift.
- Shot 4, 12–15s: 28mm wide shot of the black sedan at the foot of the stone steps, slow lateral track.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam stands at the open driver's door of the black sedan in a crisp black chauffeur cap and is already speaking toward the two guards by the revolving door, stern and mock-formal.
- 1–2s (Shot 1): @Lam keeps talking as he squares his shoulders and tugs his grey windbreaker straight.
- 2–3s (Shot 1): @Lam flicks two fingers upward at the guards as he goes on, thick grey eyebrows drawn together.
- 3–4s (Shot 1): @Lam taps the top button of his own windbreaker while he keeps speaking.
- 4–5s (CUT to Shot 2): @Lam keeps speaking with a stiff formal frown, his narrow eyes sliding from one guard to the other.
- 5–6s (Shot 2): @Lam glances pointedly down at the guards' shoes while he talks.
- 6–7s (Shot 2): @Lam keeps talking, his eyes travelling slowly back up to their faces.
- 7–8s (Shot 2): @Lam keeps talking, lowering his voice and raising one thick grey eyebrow.
- 8–9s (CUT to Shot 3): Over a guard's grey shoulder, @Lam keeps talking sternly and twirls one finger in a turning-around motion.
- 9–10s (Shot 3): @Lam keeps speaking as the two guards straighten up by the revolving door, chins raised.
- 10–11s (Shot 3): @Lam spreads both hands wide as he names the big sum, lips moving fast.
- 11–12s (Shot 3): @Lam keeps talking and taps his own chest with a curt nod.
- 12–13s (CUT to Shot 4): @Lam finishes the warning and closes his mouth, lips pressed into a straight line.
- 13–14s (Shot 4): @Lam marches stiffly around the gleaming hood of the black sedan, mouth closed.
- 14–15s (Shot 4): @Lam opens the rear door with a deep, precise bow and holds it wide, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, stern and mock-formal), in Vietnamese with exact lip-sync, said exactly once: "Này, hai cậu. Đứng thẳng lưng lên tí nào, cài cúc áo vào. Bà chủ tôi khó tính lắm, nhìn giày trước rồi mới nhìn mặt. Ai lôi thôi là bà ấy quay xe, công ty các cậu mất toi mười tỷ, rồi đừng trách tôi." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a smooth engine purring to a stop, a car door clicking open, two pairs of heels clicking together, distant city traffic. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 2 (`canh-10/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning outside the marble lobby of a gleaming Hà Nội glass tower: a revolving door, potted palms, polished stone steps reflecting the light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; a wide-brimmed black hat, big black sunglasses, purple floral silk blouse with a large gold flower brooch with a tiny hidden camera on the chest, black wide trousers, chunky gold bangle, low heeled sandals.
- Wardrobe: in this shot @BaHoa wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 40mm medium shot of the woman rising from the open rear door of the black sedan, slow tilt-up.
- Shot 2, 4–8s: 85mm close-up of her face and the gold brooch under the hat brim, locked off.
- Shot 3, 8–12s: 50mm medium shot from the side along the stone steps, slow arc.
- Shot 4, 12–15s: 28mm wide low-angle shot of her before the glass tower, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaHoa steps out of the black sedan's open rear door in big black sunglasses and a wide-brimmed black hat, dips her chin toward the large gold flower brooch on her chest and is already speaking softly into it.
- 1–2s (Shot 1): @BaHoa keeps whispering into the brooch as she rises tall, one hand smoothing her purple silk blouse.
- 2–3s (Shot 1): @BaHoa rolls her eyes with a tiny shrug while she speaks, as if remembering something.
- 3–4s (Shot 1): @BaHoa taps the brooch lightly with one fingertip as she talks.
- 4–5s (CUT to Shot 2): @BaHoa touches her own ear and shakes her head as she keeps speaking.
- 5–6s (Shot 2): @BaHoa flaps one hand dismissively at the brooch, still talking low.
- 6–7s (Shot 2): @BaHoa keeps talking as she straightens her shoulders and settles her chunky gold bangle.
- 7–8s (Shot 2): @BaHoa lifts her chin like an actress stepping on stage, still murmuring.
- 8–9s (CUT to Shot 3): @BaHoa purses her red lips between phrases and keeps talking.
- 9–10s (Shot 3): @BaHoa keeps murmuring as the tiny lens at the center of the gold brooch glints once in the sun.
- 10–11s (Shot 3): @BaHoa wags one finger at the brooch as she goes on, a warning half smile on her lips.
- 11–12s (Shot 3): @BaHoa finishes the aside and closes her red lips.
- 12–13s (CUT to Shot 4): @BaHoa slowly lowers her sunglasses with one finger, mouth closed.
- 13–14s (Shot 4): @BaHoa gazes up at the glass tower with a regal half smile, mouth closed.
- 14–15s (Shot 4): @BaHoa sets one sandal on the first polished stone step, mouth closed, chin high. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking at a natural, even conversational pace, hushed and sly, a private aside), in Vietnamese with exact lip-sync, said exactly once: "Mai ơi, hình về rõ chưa cháu? À quên mất, cái trâm này có mắt mà không có tai, bà hỏi cũng bằng thừa. Thôi kệ, vào vai rồi thì cứ thế mà diễn, hỏng một câu là không được quay lại lần hai đâu đấy." (no subtitles)
- @BaHoa starts talking within the first second; whenever @BaHoa speaks, the face and lips are clearly visible in that shot; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heeled sandals tapping on stone, a gold bangle clinking, a soft breeze in the palms, a car door thudding shut. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 3 (`canh-10/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning outside the marble lobby of a gleaming Hà Nội glass tower: a revolving door, potted palms, polished stone steps reflecting the light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; a wide-brimmed black hat, big black sunglasses, purple floral silk blouse with a large gold flower brooch with a tiny hidden camera on the chest, black wide trousers, chunky gold bangle, low heeled sandals.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; a crisp black chauffeur cap, faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a dark-green dragon tattoo on his right forearm hidden by his sleeve.
- Wardrobe: in this shot @BaHoa and @Lam wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the chauffeur onto the woman in the black hat by the sedan.
- Shot 2, 5–10s: 85mm close-up of the chauffeur bowing, locked off.
- Shot 3, 10–13s: 50mm medium shot of the woman in the black hat hissing sideways, slow push-in.
- Shot 4, 13–15s: 28mm wide two-shot along the stone steps, slow lateral track.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaHoa, in big black sunglasses and a wide-brimmed black hat, turns on @Lam beside the black sedan and is already speaking fast in a loud bossy voice.
- 1–2s (Shot 1): @BaHoa wags one finger at the car as she keeps talking, her chunky gold bangle clinking.
- 2–3s (Shot 1): @BaHoa keeps scolding loudly and points at the shiny paint, while @Lam listens, mouth closed.
- 3–4s (Shot 1): @BaHoa keeps talking and holds up one finger for one year of pay.
- 4–5s (Shot 1): @BaHoa finishes, closes her red lips and lifts her chin with a sniff.
- 5–6s (CUT to Shot 2): @Lam bows low in his black chauffeur cap and answers slowly in a low husky murmur, eyes lowered to the stone.
- 6–7s (Shot 2): @Lam keeps murmuring, a grin tugging at one corner of his mouth.
- 7–8s (Shot 2): @Lam peeks up from under the cap brim as he goes on, the grin widening.
- 8–9s (Shot 2): @Lam keeps murmuring softly, his narrow eyes twinkling.
- 9–10s (Shot 2): @Lam finishes and closes his mouth, quickly ducking his head again.
- 10–11s (CUT to Shot 3): @BaHoa hisses a quick sharp remark at @Lam through a frozen smile.
- 11–12s (Shot 3): @BaHoa keeps hissing through the smile and flaps one hand downward for him to lower his head.
- 12–13s (Shot 3): @BaHoa keeps talking sharply out of the side of her mouth, eyes on the revolving door.
- 13–14s (CUT to Shot 4): @BaHoa finishes, closes her red lips and turns toward the revolving door with a crisp sniff, while @Lam drops his eyes, mouth closed.
- 14–15s (Shot 4): @BaHoa sweeps away up the steps, while @Lam stays bowed by the car and presses his lips together to hide the grin. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking quickly in short lively phrases, every word still clear, loud and bossy, showing off): "Lái xe đâu! Đỗ cho cẩn thận vào, xước một vết sơn là trừ một năm lương, liệu hồn đấy!"
- Turn 2, 5.1–10.0s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, low servile murmur, hiding a grin): "Dạ vâng, bà chủ. Bà diễn hăng thế này, tôi suýt nữa thì tin là thật đấy."
- Turn 3, 10.5–13.5s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking quickly in short lively phrases, every word still clear, a sharp hiss through a smile): "Suỵt! Tài xế thì phải cúi đầu, cấm cười, cấm nháy mắt với tôi."
- Pacing: @BaHoa speaks quickly, then @Lam answers slowly and calmly, then @BaHoa answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a gold bangle clinking, a soft breeze in the palms, a distant car horn, the revolving door turning. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 4 (`canh-10/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Inside a parked white van turned into a surveillance post by day: two laptops glowing, tangled cables, a thermos, tinted windows facing a busy street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 50mm medium shot of the girl at the glowing laptops inside the van, locked off.
- Shot 2, 7–10s: 85mm close-up of the old man lowering his magnifier glasses, slow push-in.
- Shot 3, 10–13s: 35mm medium two-shot between the two seats, gentle drift.
- Shot 4, 13–15s: 100mm extreme close-up of a fingertip on the laptop keyboard, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Mai, a small headset pressed to one ear, leans toward the two glowing laptops and is already speaking fast with bright eyes.
- 1–2s (Shot 1): @Mai keeps talking excitedly, pointing at one glowing blank screen.
- 2–3s (Shot 1): @Mai shakes her wrist beside her ear to mimic a jingling bangle as she goes on, grinning.
- 3–4s (Shot 1): @Mai keeps speaking fast, pressing the headset closer to her ear.
- 4–5s (Shot 1): @Mai keeps talking, tapping her own chest where a brooch would sit.
- 5–6s (Shot 1): @Mai covers both ears with her hands in a playful imitation and keeps talking, giggling.
- 6–7s (Shot 1): @Mai finishes and closes her mouth, bouncing in her seat.
- 7–8s (CUT to Shot 2): @Khoa lowers his magnifier glasses over his eyes and answers in a dry nasal voice without looking away from the screens.
- 8–9s (Shot 2): @Khoa keeps talking flatly, one corner of his mouth twitching upward.
- 9–10s (Shot 2): @Khoa glances up at the van roof as he goes on, eyebrows raised.
- 10–11s (CUT to Shot 3): @Khoa keeps speaking and scratches one cheek as if remembering old mosquito bites.
- 11–12s (Shot 3): @Khoa keeps talking, turning to @Mai and lifting one long finger, while @Mai listens, mouth closed.
- 12–13s (Shot 3): @Khoa points the long finger at a key as he finishes, and @Mai nods, mouth closed.
- 13–14s (CUT to Shot 4): @Mai's fingertip presses the key at once, the blue glow of the screen on her knuckle.
- 14–15s (Shot 4): The fingertip lifts away from the keyboard in the soft blue glow, the laptop fan humming. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.7s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, bubbling with excitement): "Hình về rồi ông ơi! Nét lắm, đến tiếng vòng vàng của bà kêu leng keng cũng nghe rõ mồn một. Bà còn tưởng cái trâm không có tai cơ!"
- Turn 2, 7.2–13.0s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, dry deadpan, secretly pleased): "Hồi trẻ muốn nghe trộm, ông phải bò trên mái nhà cả đêm, muỗi đốt sưng cả mặt. Thôi, bấm ghi đi cháu."
- Pacing: @Mai speaks quickly, then @Khoa answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: laptop fans humming, muffled street traffic, a faint crackle in a headset. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 1 (`canh-11/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium tracking shot alongside the livestreamer in the glass-walled boss room, the ring light behind him.
- Shot 2, 4–8s: 50mm close-up of his face lit by the phone, locked off.
- Shot 3, 8–12s: 40mm medium shot from the dark glass wall facing him, gentle push-in.
- Shot 4, 12–15s: 24mm wide shot from the call-center floor toward the glass door.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung holds a phone on a small selfie gimbal at arm's length in the glass-walled boss room, its blank screen glowing, and is already talking fast into it with a cocky grin.
- 1–2s (Shot 1): @Hung keeps talking as he walks past the ring light, tugging the collar of his black satin bomber jacket straight.
- 2–3s (Shot 1): @Hung winks at the phone and gives the gimbal a quick little wave while he talks.
- 3–4s (Shot 1): @Hung keeps talking fast, spreading one hand wide like a grand announcement.
- 4–5s (CUT to Shot 2): @Hung leans close to the lens, eyebrows dancing, and keeps talking fast.
- 5–6s (Shot 2): @Hung rubs his silver-ringed thumb and fingers together as he goes on, grinning.
- 6–7s (Shot 2): @Hung keeps speaking and flashes both hands open twice at the lens.
- 7–8s (Shot 2): @Hung keeps speaking and mimes knocking on a door with two knuckles.
- 8–9s (CUT to Shot 3): @Hung keeps talking as he checks his ash-blond undercut in the dark glass.
- 9–10s (Shot 3): @Hung smooths one side of his undercut with his silver-ringed fingers while he talks.
- 10–11s (Shot 3): @Hung makes a heart shape with his fingers at the phone as he keeps talking.
- 11–12s (Shot 3): @Hung finishes with a wink, closes his mouth and taps the glowing phone to end the stream.
- 12–13s (CUT to Shot 4): @Hung strides out through the glass door with both arms spread wide in welcome, mouth closed.
- 13–14s (Shot 4): @Hung crosses the call-center floor between the rows of glowing desks, a closed-lip grin stretching ear to ear.
- 14–15s (Shot 4): @Hung stops by the entrance and straightens his bomber jacket, mouth closed, ready to greet his guest. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.5s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, slick, giddy showman), in Vietnamese with exact lip-sync, said exactly once: "Cả nhà ơi, anh tắt sóng mười phút nhé! Có một bà trùm bất động sản đang lên tận đây xin rót vốn cho anh, nghe đâu mấy chục tỷ. Thần tài gõ cửa thì phải chạy ra đón chứ, đúng không nào. Thả tim đi các em, lát nữa anh kể hết!" (no subtitles)
- @Hung starts talking within the first second; whenever @Hung speaks, the face and lips are clearly visible in that shot; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: phones ringing across the call center, a soft chime as the livestream ends, quick sneaker steps, a glass door swinging. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 2 (`canh-11/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; a wide-brimmed black hat, big black sunglasses, purple floral silk blouse with a large gold flower brooch with a tiny hidden camera on the chest, black wide trousers, chunky gold bangle, low heeled sandals.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- Wardrobe: in this shot @BaHoa wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 50mm medium shot of the woman settling onto the white leather sofa, locked off.
- Shot 2, 7–11s: 50mm over-the-shoulder shot from behind the woman onto the young boss, slow push-in.
- Shot 3, 11–13s: 85mm close-up of the young boss, locked off.
- Shot 4, 13–15s: 40mm medium two-shot across the low tea table, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaHoa settles onto the white leather sofa in her wide-brimmed black hat and big sunglasses and is already speaking with a lazy wave of her hand.
- 1–2s (Shot 1): @BaHoa keeps drawling grandly, crossing her legs and smoothing her purple silk blouse.
- 2–3s (Shot 1): @BaHoa flicks her fingers dismissively as she goes on, her gold bangle clinking.
- 3–4s (Shot 1): @BaHoa keeps talking and lifts a glass cup from the tea tray without drinking.
- 4–5s (Shot 1): @BaHoa tilts her head as she asks her question, the large gold flower brooch glinting on her chest.
- 5–6s (Shot 1): @BaHoa keeps asking with a lazy smile, studying @Hung over the rim of the cup.
- 6–7s (Shot 1): @BaHoa finishes, closes her red lips and sets the cup down with a soft clink, and @Hung leans forward and starts answering fast.
- 7–8s (CUT to Shot 2): @Hung, perched on the chair opposite, counts three fingers in the air as he keeps pitching eagerly.
- 8–9s (Shot 2): @Hung keeps talking fast and flashes both hands open twice.
- 9–10s (Shot 2): @Hung taps his own chest with a ringed hand as he keeps talking, nodding hard.
- 10–11s (Shot 2): @Hung leans forward, elbows on his knees, still talking fast.
- 11–12s (CUT to Shot 3): @Hung keeps pitching fast and mimes popping a candy into his mouth.
- 12–13s (Shot 3): @Hung taps an imaginary phone screen with one thumb as he keeps talking.
- 13–14s (CUT to Shot 4): @Hung finishes, closes his mouth and sits back with a lopsided closed-lip grin, while @BaHoa studies him through her dark lenses, mouth closed.
- 14–15s (Shot 4): @BaHoa taps her chunky gold bangle on the sofa arm, mouth closed, as @Hung waits, grinning. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.4s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking at a natural, even conversational pace, grand and lazy, a rich drawl): "Tôi có mười tỷ nằm im trong ngân hàng, lãi chẳng bõ tiền trà. Nghe nói cậu làm tiền đẻ ra tiền nhanh lắm?"
- Turn 2, 6.9–13.2s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, eager salesman pitch): "Ba tháng thôi, bà nhận về gấp đôi, bà cứ tin em! Sinh viên bây giờ thiếu tiền lắm, vay dễ như ăn kẹo, bấm một cái là có ngay."
- Pacing: @BaHoa speaks at an even everyday pace, then @Hung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft creak of leather, distant phones ringing, a glass cup clinking on the tray. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 3 (`canh-11/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; a wide-brimmed black hat, big black sunglasses, purple floral silk blouse with a large gold flower brooch with a tiny hidden camera on the chest, black wide trousers, chunky gold bangle, low heeled sandals.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- Wardrobe: in this shot @BaHoa wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot across the low tea table, holding the previous framing.
- Shot 2, 5–8s: 50mm over-the-shoulder shot from behind the woman onto the young boss.
- Shot 3, 8–11s: 85mm close-up of the young boss, locked off.
- Shot 4, 11–15s: 50mm medium shot of the woman on the sofa with the gold brooch, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaHoa slowly lowers her sunglasses an inch and is already speaking slowly and sweetly to @Hung, her eyes above the dark lenses.
- 1–2s (Shot 1): @BaHoa keeps speaking, drawing out each word with a honeyed smile, while @Hung leans back, mouth closed.
- 2–3s (Shot 1): @BaHoa taps her chunky gold bangle on the sofa arm as she goes on.
- 3–4s (Shot 1): @BaHoa tilts her head as she asks, one eyebrow climbing higher.
- 4–5s (Shot 1): @BaHoa finishes the question and closes her red lips, waiting.
- 5–6s (CUT to Shot 2): @Hung answers fast with a careless shrug, lifting a phone on a small selfie gimbal.
- 6–7s (Shot 2): @Hung keeps bragging, waggling the phone beside his face.
- 7–8s (Shot 2): @Hung keeps talking fast and taps the glowing blank screen with a ringed finger.
- 8–9s (CUT to Shot 3): @Hung spreads his arms along the chair back as he goes on, grinning wide.
- 9–10s (Shot 3): @Hung keeps talking, pulling a mock-ashamed face and hiding it behind one hand.
- 10–11s (Shot 3): @Hung finishes, closes his mouth and folds his arms with a smug nod.
- 11–12s (CUT to Shot 4): @BaHoa nods slowly and starts a short purring reply, red lips curling.
- 12–13s (Shot 4): @BaHoa keeps purring, pressing one hand to her chest in mock admiration.
- 13–14s (Shot 4): @BaHoa finishes and closes her red lips into a sweet smile.
- 14–15s (Shot 4): @BaHoa slides her sunglasses back up with one finger, mouth closed, the gold brooch glinting. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking slowly and softly, unhurried, with a short natural pause between phrases, sweet, baiting him): "Kẹo thì ngọt thật đấy. Nhưng nhỡ chúng nó không chịu trả, cậu làm thế nào?"
- Turn 2, 5.4–10.9s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, smug, bragging): "Không trả à? Em gửi ảnh nó cho cả họ hàng, cả lớp, cả thầy cô. Xấu hổ quá, kiểu gì chẳng phải bò về trả!"
- Turn 3, 11.4–13.7s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking slowly and softly, unhurried, with a short natural pause between phrases, purring, mock-impressed): "Ồ, cao tay thật. Tôi phục cậu đấy."
- Pacing: @BaHoa speaks slowly and calmly, then @Hung answers quickly, then @BaHoa answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a gold bangle tapping on leather, a phone buzzing, the ring light humming, distant keyboards clicking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 4 (`canh-11/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; a wide-brimmed black hat, big black sunglasses, purple floral silk blouse with a large gold flower brooch with a tiny hidden camera on the chest, black wide trousers, chunky gold bangle, low heeled sandals.
- Wardrobe: in this shot @BaHoa wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the woman alone on the white sofa, the glass door behind her, locked off.
- Shot 2, 4–8s: 85mm close-up of her face and the gold brooch, slow push-in.
- Shot 3, 8–12s: 40mm medium shot from beside the glass door looking back at her on the sofa.
- Shot 4, 12–15s: 100mm extreme close-up of the gold flower brooch and its tiny lens, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaHoa, alone on the white sofa, glances toward the glass door, dips her chin toward the gold flower brooch and is already whispering into it.
- 1–2s (Shot 1): @BaHoa keeps whispering, red lips clearly moving, one hand shielding her mouth from the door.
- 2–3s (Shot 1): @BaHoa keeps whispering fast and holds up two fingers by her chin.
- 3–4s (Shot 1): @BaHoa keeps whispering with a sly curl of her red lips, fingertips stroking the brooch.
- 4–5s (CUT to Shot 2): @BaHoa's eyes dart to the door and back while she keeps talking low.
- 5–6s (Shot 2): @BaHoa keeps whispering, her chunky gold bangle sliding down her wrist.
- 6–7s (Shot 2): @BaHoa twists her fingers in a tight little screw motion as she keeps whispering.
- 7–8s (Shot 2): @BaHoa keeps whispering and taps two fingers on the brooch twice.
- 8–9s (CUT to Shot 3): @BaHoa keeps talking low, leaning back on the sofa, eyes on the door.
- 9–10s (Shot 3): @BaHoa holds up two fingers again as she whispers her instruction.
- 10–11s (Shot 3): @BaHoa keeps whispering, then gives a small rueful pout and a shrug.
- 11–12s (Shot 3): @BaHoa finishes and closes her lips in a slow curved smile.
- 12–13s (CUT to Shot 4): The tiny lens at the center of the gold flower brooch glints once.
- 13–14s (Shot 4): The brooch rises and falls slowly with @BaHoa's calm breath, its gold petals gleaming in the neon.
- 14–15s (Shot 4): Purple neon light slides across the gold petals of the brooch, still and silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking at a natural, even conversational pace, low gleeful whisper), in Vietnamese with exact lip-sync, said exactly once: "Nó vừa ra ngoài lấy hợp đồng rồi. Bà mới hỏi có hai câu mà nó khai sạch sành sanh, lãi bao nhiêu một ngày, ép người ta thế nào. Cháu nhớ lưu ra làm hai bản cho chắc nhé, không thì bà diễn công cốc." (no subtitles)
- @BaHoa starts talking within the first second; whenever @BaHoa speaks, the face and lips are clearly visible in that shot; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint electronic click, the soft ring light hum, muffled chatter of the call center. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 1 (`canh-12/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A bright corporate hallway high in the glass tower by day: grey carpet, frosted glass walls, ceiling lights, a potted plant by a corner.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; a blue technician cap over his grey ponytail, a tiny earpiece in one ear, brown multi-pocket vest bristling with little tools over a blue checkered shirt, grey trousers, canvas shoes.
- Wardrobe: in this shot @Khoa wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium tracking shot backing away ahead of the repairman down the bright hallway.
- Shot 2, 4–8s: 85mm close-up of his face and the tiny earpiece, tracking backward.
- Shot 3, 8–12s: 50mm medium three-quarter shot as he walks past the frosted glass, gentle drift.
- Shot 4, 12–15s: 100mm extreme close-up of a bent hairpin held up to the light, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khoa ambles toward the camera down the bright hallway in a blue technician cap, swinging a toolbox, touches the tiny earpiece in his ear and is already speaking in a dry nasal voice.
- 1–2s (Shot 1): @Khoa keeps talking with a loose, bored gait like any ordinary repairman on his rounds.
- 2–3s (Shot 1): @Khoa tugs the brim of his blue technician cap as he goes on, face deadpan.
- 3–4s (Shot 1): @Khoa keeps speaking and nods at an empty frosted doorway.
- 4–5s (CUT to Shot 2): @Khoa keeps talking flatly and waves one long hand in front of his own face.
- 5–6s (Shot 2): @Khoa keeps speaking, eyes half closed, the toolbox swinging at his side.
- 6–7s (Shot 2): @Khoa keeps talking, glancing sideways at nobody in particular.
- 7–8s (Shot 2): @Khoa presses the earpiece a little deeper while he talks.
- 8–9s (CUT to Shot 3): @Khoa keeps speaking and lets one corner of his mouth droop, eyebrows lifting.
- 9–10s (Shot 3): @Khoa pats his chest lightly with two fingers as he keeps talking.
- 10–11s (Shot 3): @Khoa lifts his chin with a wistful little sniff as he goes on, smoothing his grey ponytail.
- 11–12s (Shot 3): @Khoa finishes, closes his mouth and stops beside a glass door.
- 12–13s (CUT to Shot 4): @Khoa's long fingers draw a bent hairpin from his vest pocket.
- 13–14s (Shot 4): @Khoa holds the bent hairpin up to the ceiling light, turning it slowly.
- 14–15s (Shot 4): The bent hairpin glints under the ceiling light between @Khoa's long fingers. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, deadpan, faintly miffed), in Vietnamese with exact lip-sync, said exactly once: "Ông vào trong được rồi đấy, cháu ạ. Đội cái mũ thợ điều hoà lên là thành người vô hình, cả tầng chẳng ai thèm liếc ông lấy một cái. Nói thật là cũng hơi chạnh lòng, hồi ấy đi đâu cũng có người ngoái nhìn." (no subtitles)
- @Khoa starts talking within the first second; whenever @Khoa speaks, the face and lips are clearly visible in that shot; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft footsteps on carpet, the hum of ceiling lights, a toolbox handle creaking, a distant elevator chime. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 2 (`canh-12/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A cold server room in the glass tower: tall black server racks with blinking blue lights, cable trays, a humming air conditioner, a glass door with a keypad lock.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; a blue technician cap over his grey ponytail, a tiny earpiece in one ear, brown multi-pocket vest bristling with little tools over a blue checkered shirt, grey trousers, canvas shoes.
- Wardrobe: in this shot @Khoa wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the repairman kneeling at the keypad of the glass door, slow push-in.
- Shot 2, 4–8s: 85mm close-up of his face beside the keypad, locked off.
- Shot 3, 8–12s: 50mm medium shot of the repairman in the open glass doorway, gentle drift.
- Shot 4, 12–15s: 28mm wide shot from deep inside the server room toward the glass door, slow drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khoa kneels by the keypad lock of the glass door, slides a bent hairpin into a tiny slot beneath it and is already muttering to himself in a fussy nasal voice.
- 1–2s (Shot 1): @Khoa keeps muttering with a dry smirk, eyeing the small red light above the blank buttons.
- 2–3s (Shot 1): @Khoa keeps talking, twisting the hairpin gently.
- 3–4s (Shot 1): @Khoa counts under his breath, giving the hairpin three tiny twists.
- 4–5s (CUT to Shot 2): The small red light flips to green with a click beside @Khoa's face as he keeps muttering.
- 5–6s (Shot 2): @Khoa holds up his steady hand and wiggles his fingers in the air while he talks.
- 6–7s (Shot 2): @Khoa keeps muttering proudly, eyebrows lifting under the magnifier glasses on his forehead.
- 7–8s (Shot 2): @Khoa keeps talking and mimes wiping sweat from his brow with the back of his wrist.
- 8–9s (CUT to Shot 3): The glass door eases open with a hiss as @Khoa keeps talking and rises to his feet.
- 9–10s (Shot 3): @Khoa keeps muttering with a scornful glance back at the keypad.
- 10–11s (Shot 3): @Khoa mimes peeling the lid off a yogurt cup with two fingers as he finishes the thought.
- 11–12s (Shot 3): @Khoa closes his mouth and tucks the hairpin into his vest pocket.
- 12–13s (CUT to Shot 4): @Khoa picks up his toolbox and steps through into the cold blue glow of the server racks, mouth closed.
- 13–14s (Shot 4): @Khoa walks toward the camera between the tall humming racks, mouth closed.
- 14–15s (Shot 4): @Khoa stops at one rack and lowers his magnifier glasses, his face lit blue, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, fussy, proud muttering), in Vietnamese with exact lip-sync, said exactly once: "Ối giời, khoá điện tử cơ đấy, trông thì oai lắm. Một, hai, ba, xong. Tay này vẫn chưa run tí nào đâu, cháu thấy chưa. Két sắt hồi trước còn bắt ông toát cả mồ hôi, chứ loại này dễ như bóc hộp sữa chua." (no subtitles)
- @Khoa starts talking within the first second; whenever @Khoa speaks, the face and lips are clearly visible in that shot; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint metallic scratch, a crisp electronic beep, the hiss of a door seal releasing, the loud hum of the air conditioner. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 3 (`canh-12/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A cold server room in the glass tower: tall black server racks with blinking blue lights, cable trays, a humming air conditioner, a glass door with a keypad lock.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; a blue technician cap over his grey ponytail, a tiny earpiece in one ear, brown multi-pocket vest bristling with little tools over a blue checkered shirt, grey trousers, canvas shoes.
- Wardrobe: in this shot @Khoa wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 28mm wide shot from deep inside the server room toward the glass door, holding the previous framing.
- Shot 2, 3–7s: 85mm close-up at the server rack, slow tilt-up from the hard drive to his face.
- Shot 3, 7–12s: 50mm medium shot of him crouching at the rack, locked off.
- Shot 4, 12–15s: 100mm extreme close-up of the small black hard drive and its racing lights.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khoa crouches before a tall black server rack, slides a small black hard drive into a port with a soft click and is already speaking low and dry into his earpiece.
- 1–2s (Shot 1): @Khoa keeps speaking quietly, eyes fixed on the drive.
- 2–3s (Shot 1): @Khoa tilts his head as he asks, listening to the earpiece.
- 3–4s (CUT to Shot 2): @Khoa keeps talking as a row of tiny blue lights on the drive begins to blink, racing across his thick lenses.
- 4–5s (Shot 2): @Khoa keeps speaking with a satisfied little nod, his face lit blue.
- 5–6s (Shot 2): @Khoa keeps speaking as he points one long finger at the tiny lights blinking faster and faster.
- 6–7s (Shot 2): @Khoa keeps talking, one eyebrow raised above the magnifier lenses.
- 7–8s (CUT to Shot 3): @Khoa keeps talking, counting things off on his long fingers one by one.
- 8–9s (Shot 3): @Khoa twirls his finger in a quick circle as he goes on.
- 9–10s (Shot 3): @Khoa keeps speaking calmly, holding up two fingers beside his face.
- 10–11s (Shot 3): @Khoa pats the air gently with one palm as he keeps talking.
- 11–12s (Shot 3): @Khoa finishes, closes his mouth and sits back on his heels with a smug closed-lip smile.
- 12–13s (CUT to Shot 4): The row of tiny blue lights races across the small black hard drive.
- 13–14s (Shot 4): The lights blink faster still against the black casing, the cables trembling in the fan breeze.
- 14–15s (Shot 4): The tiny blue lights race on along the drive in the cold hum of the racks. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, low, quietly smug), in Vietnamese with exact lip-sync, said exactly once: "Cắm rồi đấy. Bên cháu nhận chưa? Đèn nháy nhanh thế này là cả kho bí mật của thằng Hưng đang chạy sang máy cháu, sổ sách, tin nhắn, cả tên tuổi người vay. Cứ để nó chạy hết, mất chừng hai phút, đừng sốt ruột." (no subtitles)
- @Khoa starts talking within the first second; whenever @Khoa speaks, the face and lips are clearly visible in that shot; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft plastic click, cooling fans rising in pitch, rapid electronic chirps. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 4 (`canh-12/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Inside a parked white van turned into a surveillance post by day: two laptops glowing, tangled cables, a thermos, tinted windows facing a busy street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the girl at the laptops inside the van, slow push-in.
- Shot 2, 4–8s: 85mm close-up of her face in the laptop glow, locked off.
- Shot 3, 8–12s: 50mm medium shot from the end of the shelf, gentle drift.
- Shot 4, 12–15s: 85mm close-up of her face, very slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Mai leans toward the two glowing laptops in the van with a small headset microphone at her cheek and is already speaking breathlessly.
- 1–2s (Shot 1): @Mai keeps talking fast, eyes wide behind her round black-framed glasses, two fingers sliding on the trackpad.
- 2–3s (Shot 1): @Mai keeps speaking as she scrolls on and on, the screen glow flickering over her face.
- 3–4s (Shot 1): @Mai keeps talking, lifting her hand off the trackpad and staring at the screen.
- 4–5s (CUT to Shot 2): @Mai keeps speaking more slowly, her lips parting between phrases.
- 5–6s (Shot 2): @Mai keeps talking softly, shaking her head slowly at the screen.
- 6–7s (Shot 2): @Mai keeps speaking as she slowly leans back, the screen glow on her face.
- 7–8s (Shot 2): @Mai's voice catches as she keeps speaking, her eyes glistening behind the glasses.
- 8–9s (CUT to Shot 3): @Mai keeps speaking, swallowing hard between phrases.
- 9–10s (Shot 3): @Mai keeps talking softly, one hand pressed flat on the shelf.
- 10–11s (Shot 3): @Mai keeps talking quietly, touching her own chest with her fingertips.
- 11–12s (Shot 3): @Mai finishes and closes her mouth, breathing out slowly.
- 12–13s (CUT to Shot 4): A single tear slides down @Mai's cheek in the laptop glow, mouth closed.
- 13–14s (Shot 4): A small closed-lip smile lifts @Mai's face as she wipes the tear with her sleeve.
- 14–15s (Shot 4): @Mai sits still before the glowing screens, mouth closed, the headset microphone at her cheek. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking at a natural, even conversational pace, breathless, then her voice catches), in Vietnamese with exact lip-sync, said exactly once: "Về đủ rồi ông ạ, không thiếu dòng nào. Danh sách dài lắm, mấy nghìn người, toàn sinh viên như cháu, có bạn còn học năm nhất. Thế mà suốt ba tháng nay cứ tưởng chỉ mình cháu dại. Hoá ra cháu không phải một mình." (no subtitles)
- @Mai starts talking within the first second; whenever @Mai speaks, the face and lips are clearly visible in that shot; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: laptop fans whirring, rapid keyboard taps, a quiet exhale, muffled street traffic. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 1 (`canh-13/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A dim underground car park beneath the glass tower: rows of concrete pillars, flickering fluorescent strip lights, a black luxury sedan with no badge parked in a far bay.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot from beside a concrete pillar onto the heavyset collector peeking out, slow push-in.
- Shot 2, 4–8s: 85mm close-up of his face at the edge of the pillar, locked off.
- Shot 3, 8–12s: 50mm medium shot of him leaning out past the pillar, the black sedan far behind, gentle drift.
- Shot 4, 12–15s: 85mm close-up of him pressed against the pillar with the phone, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Beo peeks out from behind a thick concrete pillar in the dim car park toward the far black sedan and is already whispering fast to himself, small eyes squinting.
- 1–2s (Shot 1): @Beo keeps whispering, the lightning-bolt pattern on his shaved head catching the flickering light.
- 2–3s (Shot 1): @Beo mimes wiping a car hood with one hand as he whispers, eyes fixed on the far bay.
- 3–4s (Shot 1): @Beo's small eyes go wide and he keeps whispering, tracing a long curving line along his own forearm.
- 4–5s (CUT to Shot 2): @Beo wiggles his fingers along his forearm like scales as he goes on.
- 5–6s (Shot 2): @Beo keeps whispering, his gold front tooth glinting in the flickering light.
- 6–7s (Shot 2): @Beo frowns hard and keeps muttering, scratching his shaved head.
- 7–8s (Shot 2): @Beo leans a little further out past the pillar for a better look, still whispering fast.
- 8–9s (CUT to Shot 3): @Beo sniffs the air twice like a hound as he keeps talking.
- 9–10s (Shot 3): @Beo keeps whispering, spreading his thick hands wide with a greedy grin.
- 10–11s (Shot 3): @Beo snaps his fingers softly as he keeps talking.
- 11–12s (Shot 3): @Beo finishes, closes his mouth, slips back behind the pillar and flattens his broad back against the concrete.
- 12–13s (CUT to Shot 4): @Beo pulls out a phone with a glowing blank screen, mouth closed.
- 13–14s (Shot 4): @Beo taps the glowing screen with a thick thumb, mouth closed.
- 14–15s (Shot 4): @Beo lifts the phone to his ear and holds his breath, eyes darting toward the far bay. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.5s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, hushed, gaping, half to himself), in Vietnamese with exact lip-sync, said exactly once: "Ơ kìa! Lão ấy xắn tay áo lau xe, trên cánh tay có cả một con rồng xanh to tướng, vảy nào ra vảy nấy. Làm tài xế gì mà xăm trổ như dân giang hồ thế kia? Có mùi rồi đây, vụ này to đấy. Phải gọi cho sếp ngay mới được." (no subtitles)
- @Beo starts talking within the first second; whenever @Beo speaks, the face and lips are clearly visible in that shot; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: fluorescent lights buzzing, a cloth squeaking on a car hood far away, echoing water drips, a sharp breath. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 2 (`canh-13/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the young boss onto the heavyset collector.
- Shot 2, 5–9s: 85mm close-up of the young boss, locked off.
- Shot 3, 9–13s: 50mm medium shot of the young boss by the glass desk, slow push-in.
- Shot 4, 13–15s: 28mm wide two-shot by the glass desk, the neon-lit glass wall behind them.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Beo leans in toward @Hung beside the glass desk and is already speaking fast in a rough low voice, tapping his own thick right forearm with two fingers.
- 1–2s (Shot 1): @Beo keeps reporting breathlessly, tracing a dragon shape along his forearm, while @Hung listens, mouth closed.
- 2–3s (Shot 1): @Beo spreads his fingers over the whole forearm as he goes on.
- 3–4s (Shot 1): @Beo squints and taps his temple as he keeps talking.
- 4–5s (Shot 1): @Beo shrugs with both palms up, still talking, frowning.
- 5–6s (CUT to Shot 2): @Beo's last word trails off as @Hung slowly lowers a phone on a small selfie gimbal and starts answering slowly with a cold amused curl of his lips.
- 6–7s (Shot 2): @Hung tilts his head as he says the old nickname, a slow smile spreading.
- 7–8s (Shot 2): @Hung keeps speaking slowly and holds one flat hand low, as if measuring a small boy.
- 8–9s (Shot 2): @Hung keeps talking, tapping the gimbal against his chin, eyes narrowing behind his round gold-rimmed glasses.
- 9–10s (CUT to Shot 3): @Hung keeps speaking slowly and sweeps a ringed hand toward the window and the street below.
- 10–11s (Shot 3): @Hung keeps talking with a dismissive flick of his fingers.
- 11–12s (Shot 3): @Hung keeps speaking, miming a steering wheel with a sneer.
- 12–13s (Shot 3): @Hung finishes with a scornful little laugh and closes his mouth.
- 13–14s (CUT to Shot 4): @Hung narrows his eyes behind his round gold-rimmed glasses, mouth closed, while @Beo shifts his weight.
- 14–15s (Shot 4): @Beo rubs his shaved head, mouth closed, as @Hung turns toward the window. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, breathless, eager to report): "Đại ca ơi, thằng cha lái xe cho bà kia xăm rồng kín cả tay. Em nhìn quen lắm mà không nhớ ra."
- Turn 2, 5.7–13.0s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking slowly and softly, unhurried, with a short natural pause between phrases, cold, slowly amused): "Rồng à? Lâm Rồng. Hồi bé bố tao kể suốt, cả phố sợ lão một phép. Giờ đi lái thuê cho một bà già cơ đấy."
- Pacing: @Beo speaks quickly, then @Hung answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the ring light humming, a muffled phone ringing, a chair creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 3 (`canh-13/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the young boss at the glass desk with a glossy folder, slow push-in.
- Shot 2, 4–8s: 85mm close-up of his face behind the gold-rimmed glasses, locked off.
- Shot 3, 8–11s: 35mm low-angle medium shot across the glass desk, gentle drift.
- Shot 4, 11–15s: 85mm close-up of his ringed hands, the folder and the fountain pen, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung sits alone at his glass desk, flips open a glossy folder and is already talking fast to himself, eyes glinting behind his round gold-rimmed glasses.
- 1–2s (Shot 1): @Hung holds up two fingers side by side as he goes on.
- 2–3s (Shot 1): @Hung runs a ringed finger down a page of faint unreadable lines while he keeps talking.
- 3–4s (Shot 1): @Hung keeps talking, a slow grin spreading, eyebrows dancing.
- 4–5s (CUT to Shot 2): @Hung twirls a lock of his own hair and taps his lips as he keeps talking.
- 5–6s (Shot 2): @Hung keeps talking with a short snorting laugh, shaking his head.
- 6–7s (Shot 2): @Hung keeps speaking and wags one finger in mock scolding at the empty sofa beyond the glass.
- 7–8s (Shot 2): @Hung keeps talking as he flips to the last page and taps it twice.
- 8–9s (CUT to Shot 3): @Hung looks up toward the empty sofa and keeps speaking, raising both hands like an actor taking a bow.
- 9–10s (Shot 3): @Hung keeps talking with a crooked grin, miming a curtain falling with both hands.
- 10–11s (Shot 3): @Hung points one finger at the floor as he finishes the thought, a crooked grin on his face.
- 11–12s (CUT to Shot 4): @Hung closes his mouth and snaps the folder shut with one hand.
- 12–13s (Shot 4): @Hung sets the fountain pen neatly across the folder like a winning chess move.
- 13–14s (Shot 4): @Hung drums his silver-ringed fingers once on the folder, then lifts them away slowly.
- 14–15s (Shot 4): The fountain pen gleams on the closed folder under the ring light. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.1s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, gleeful, scheming), in Vietnamese with exact lip-sync, said exactly once: "Có Rồng thì kiểu gì chẳng có Hổ. Mụ trùm nhà đất ấy chính là Hoa Hổ chứ ai, tóc đỏ, son đỏ, đúng như lời đồn. Định lừa cả tao cơ à? Được, các cụ thích diễn thì tao diễn cùng, rồi xem cuối cùng đứa nào phải đi tù." (no subtitles)
- @Hung starts talking within the first second; whenever @Hung speaks, the face and lips are clearly visible in that shot; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper rustling, a folder snapping shut, a pen clicking on the folder, the soft hum of neon. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 4 (`canh-13/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The flashy call-center office of a loan app company high in a Hà Nội glass tower by day: rows of desks with young callers in headsets at glowing monitors, purple and gold neon accent lights without letters, a glass-walled boss room with a white leather sofa and a ring light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 50mm medium shot of the young boss by the tall window over the street, locked off.
- Shot 2, 7–10s: 50mm over-the-shoulder shot from behind the young boss onto the heavyset collector at the window.
- Shot 3, 10–13s: 85mm close-up of the heavyset collector, handheld.
- Shot 4, 13–15s: 24mm wide shot of the call center as the collector strides off between the desks.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung stands by the tall window over the street, taps the closed folder against his palm and is already speaking slowly in a cold slick voice.
- 1–2s (Shot 1): @Hung mimes a signature in the air with one finger as he goes on.
- 2–3s (Shot 1): @Hung keeps speaking quietly, eyes glinting, the folder still in hand.
- 3–4s (Shot 1): @Hung keeps speaking coldly, lifting an invisible phone to his ear with his ringed hand.
- 4–5s (Shot 1): @Hung keeps talking slowly, a lopsided grin creeping across his face.
- 5–6s (Shot 1): @Hung keeps speaking and taps the folder where a signature would go.
- 6–7s (Shot 1): @Hung keeps talking slowly, then closes his mouth into the lopsided grin.
- 7–8s (CUT to Shot 2): @Beo steps up to the window, points one thick finger down at the street and answers fast in a rough bass.
- 8–9s (Shot 2): @Beo keeps talking fast, pointing at a tiny white van parked at the curb far below.
- 9–10s (Shot 2): @Beo taps the glass above the van, still talking fast.
- 10–11s (CUT to Shot 3): @Beo turns from the window, still talking, eyebrows up, his thick arms unfolding.
- 11–12s (Shot 3): @Beo jerks his thumb toward the door as he asks eagerly.
- 12–13s (Shot 3): @Beo keeps asking, bouncing on his heels with an eager grin.
- 13–14s (CUT to Shot 4): @Beo finishes and closes his mouth as @Hung flicks two fingers toward the door, mouth closed.
- 14–15s (Shot 4): @Beo nods once and strides off between the rows of glowing desks, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.1s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking slowly and softly, unhurried, with a short natural pause between phrases, cold, quiet order): "Cứ để mụ ấy ký hợp đồng. Ký xong, tao gọi công an, tố cả bọn tội lừa đảo, có chữ ký làm bằng."
- Turn 2, 7.6–13.3s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, eager and rough): "Rõ, đại ca. Cái xe tải trắng đỗ bên kia đường từ sáng đến giờ, chắc là của chúng nó. Em dẫn anh em xuống luôn nhé?"
- Pacing: @Hung speaks slowly and calmly, then @Beo answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heavy flip-flop steps, distant ringing phones, a glass door swinging. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 1 (`canh-14/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Inside a parked white van turned into a surveillance post by day: two laptops glowing, tangled cables, a thermos, tinted windows facing a busy street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 40mm over-the-shoulder shot from behind the girl onto the man filling the van's open side door, handheld.
- Shot 2, 6–10s: 85mm close-up of the girl hugging the hard drive, handheld.
- Shot 3, 10–13s: 35mm medium shot of the man in the doorway turning toward the street, quick handheld pan.
- Shot 4, 13–15s: 28mm wide interior shot of the van as the far-side door slides open, handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): The van's side door stands open and @Beo fills the doorway with his arms folded, already speaking fast in a rough bass at @Mai.
- 1–2s (Shot 1): @Beo keeps talking loudly and holds out one big palm, his gold front tooth flashing.
- 2–3s (Shot 1): @Beo leans into the doorway and keeps blustering, while in the foreground @Mai pulls the small black hard drive free of its cable, mouth closed.
- 3–4s (Shot 1): @Beo jerks his thumb up toward the glass tower as he keeps talking, smirking.
- 4–5s (Shot 1): @Beo keeps talking with a smug shrug, palm still held out.
- 5–6s (Shot 1): @Beo finishes with a smug grin and closes his mouth.
- 6–7s (CUT to Shot 2): @Mai, hugging the drive to her chest, points past his shoulder toward the street with wide eyes and answers fast, her voice high and urgent.
- 7–8s (Shot 2): @Mai keeps talking fast, pointing toward the street again.
- 8–9s (Shot 2): @Mai keeps talking, miming someone wheeling a motorbike away.
- 9–10s (Shot 2): @Mai finishes and closes her mouth, eyes still wide, finger pointing.
- 10–11s (CUT to Shot 3): @Beo spins his head toward the street and barks a quick question.
- 11–12s (Shot 3): @Beo keeps barking, leaning half out of the doorway and glaring up the pavement.
- 12–13s (Shot 3): @Beo finishes, closes his mouth and stares at the empty pavement, while behind him @Mai slides open the far-side door.
- 13–14s (CUT to Shot 4): @Mai slips out through the far-side door into the daylight, the drive under her arm, mouth closed.
- 14–15s (Shot 4): @Beo turns back to the empty seat and blinks at the glowing laptops, lips pressed shut. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.9s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, blustering and smug): "Con bé kia, đưa cái ổ đây! Sếp tao biết hết trò của bọn mày rồi, bà trùm cũng toi, không ai cứu được mày đâu."
- Turn 2, 6.4–10.0s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, high and urgent, a quick bluff): "Anh ơi, xe máy của anh đang bị người ta dắt đi kìa, chiếc màu đen đấy!"
- Turn 3, 10.5–12.8s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, a startled bark): "Đâu? Thằng nào to gan dám động vào xe của tao?"
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the van door sliding open with a rattle, street horns pouring in, a second door rolling open, quick sneaker steps fading. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 2 (`canh-14/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Noon on a busy old-quarter street near the railway: honking motorbikes, street vendors, shop awnings, a white van parked at the curb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 85mm close-up of the girl's face and headset as she runs along the sunny old-quarter pavement, handheld.
- Shot 2, 3–6s: 35mm medium tracking shot running alongside her, fast handheld.
- Shot 3, 6–11s: 85mm close-up tracking shot of the old man riding the cream motorbike out of the far lane, handheld.
- Shot 4, 11–15s: 40mm medium two-shot at the curb over the chrome headlamp, gentle handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Mai runs at full speed along the sunny pavement, clutching a small black hard drive against her lavender hoodie, already speaking fast into the small headset at her cheek.
- 1–2s (Shot 1): @Mai keeps talking breathlessly, ducking under a low shop awning.
- 2–3s (Shot 1): @Mai keeps speaking fast, panting, her round glasses bouncing on her nose.
- 3–4s (CUT to Shot 2): @Mai glances back over her shoulder as she keeps talking.
- 4–5s (Shot 2): @Mai keeps talking between gasps, one hand pressed to her side.
- 5–6s (Shot 2): @Mai asks her question into the headset, eyes searching the street ahead.
- 6–7s (CUT to Shot 3): @Mai's last gasp fades as @Lam rides the old cream-colored step-through motorbike with a round chrome headlamp out of the far lane in his battered green pith helmet, beeps twice and calls out with a calm half smile.
- 7–8s (Shot 3): @Lam keeps talking calmly as he weaves around a vendor's cart, one hand raised in a jaunty wave.
- 8–9s (Shot 3): @Lam keeps speaking and pats the seat behind him with a wink.
- 9–10s (Shot 3): @Lam keeps talking, waving one hand as if refusing payment.
- 10–11s (Shot 3): @Lam keeps speaking, waving away an imaginary bargain with a grin.
- 11–12s (CUT to Shot 4): @Lam finishes, closes his mouth and brakes to a neat stop at the curb, as @Mai runs up beside the bike and starts a gasping reply.
- 12–13s (Shot 4): @Mai keeps talking, half laughing, hugging the drive.
- 13–14s (Shot 4): @Mai closes her mouth, chest heaving, as @Lam glances back at her with a grin.
- 14–15s (Shot 4): @Mai stops beside the seat out of breath, as @Lam waits with both hands on the handlebars, both mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.1s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, breathless, running hard): "Ông ơi, bọn Béo chặn xe tải rồi! Cháu đang ôm ổ cứng chạy về phía đường tàu, sắp hết hơi rồi, ông nghe thấy cháu không?"
- Turn 2, 6.6–11.3s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, calm and playful, unhurried): "Xe ôm đây! Cháu đi đâu ông chở, chuyến này ông không lấy tiền, khỏi cần mặc cả."
- Turn 3, 11.8–12.9s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, a gasping half laugh): "Ông còn đùa được à!"
- Pacing: @Mai speaks quickly, then @Lam answers at an even everyday pace, then @Mai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: quick sneaker footsteps, a chorus of honking horns, a cheerful little horn beeping twice, brakes squeaking softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 3 (`canh-14/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 40mm medium two-shot at the curb over the chrome headlamp, holding the previous framing.
- Shot 2, 6–9s: 50mm over-the-shoulder shot from behind the girl onto the old man, handheld.
- Shot 3, 9–13s: 85mm close-up of the old man under the pith helmet, handheld.
- Shot 4, 13–15s: 24mm wide shot down the street as the bike pulls away, fast handheld follow.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Mai stands beside the idling motorbike hugging the small black hard drive and is already speaking fast to @Lam, pointing back down the street.
- 1–2s (Shot 1): @Mai keeps talking in a panicky rush, holding up four fingers.
- 2–3s (Shot 1): @Mai spreads both arms wide as she goes on, miming someone huge.
- 3–4s (Shot 1): @Mai keeps talking fast, glancing back over her shoulder down the street.
- 4–5s (Shot 1): @Mai eyes the old cream bike doubtfully and taps its worn seat as she asks.
- 5–6s (Shot 1): @Mai keeps asking, chest heaving, while @Lam listens, mouth closed, both hands on the handlebars.
- 6–7s (CUT to Shot 2): @Mai closes her mouth, and @Lam pats the seat behind him and answers firmly with a sly glint in his eye.
- 7–8s (Shot 2): @Lam keeps speaking calmly, tightening the strap of his battered green pith helmet.
- 8–9s (Shot 2): @Lam keeps talking as @Mai swings onto the back seat, mouth closed.
- 9–10s (CUT to Shot 3): @Lam revs the engine gently and keeps speaking, a slow grin creasing his sun-wrinkled face.
- 10–11s (Shot 3): @Lam keeps talking, patting the old fuel tank like a loyal horse.
- 11–12s (Shot 3): @Lam keeps speaking, his narrow eyes on the street ahead.
- 12–13s (Shot 3): @Lam says his last words with a nod as @Mai wraps both arms around his waist, the drive pressed between them.
- 13–14s (CUT to Shot 4): @Lam closes his mouth and twists the throttle, and the old bike pulls away from the curb with @Mai clinging on behind.
- 14–15s (Shot 4): The cream motorbike weaves into the stream of traffic and shrinks down the sunny street, a puff of exhaust hanging in the noon light. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.1s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, panicky, glancing back): "Chúng nó ngay sau lưng kìa ông! Bốn xe máy, thằng nào cũng to như cái tủ lạnh, xe mình cũ thế này chạy có nổi không?"
- Turn 2, 6.6–13.1s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, firm, a glint in his eye): "Lên đi, ôm thật chặt vào. Xe cũ nhưng máy còn khoẻ, hôm nay ông cho con biết thế nào là chạy xe phố cổ."
- Pacing: @Mai speaks quickly, then @Lam answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a puttering engine revving, traffic horns, a street vendor calling in the distance. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 4 (`canh-14/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Noon on a busy old-quarter street near the railway: honking motorbikes, street vendors, shop awnings, a white van parked at the curb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- Extra: three debt collectors on black motorbikes riding close behind him
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium tracking shot from a camera motorbike riding alongside him down a narrow old-quarter street.
- Shot 2, 4–8s: 85mm close-up of his face as he rides, tracking.
- Shot 3, 8–12s: 40mm low-angle medium shot riding just ahead of him, the other bikes trailing.
- Shot 4, 12–15s: 28mm wide shot from behind the riders toward the railway tracks at the end of the street.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Beo rides a black motorbike down the center of a narrow old-quarter street, the three debt collectors close behind, and is already shouting back at them over the engines, his face turned toward the camera.
- 1–2s (Shot 1): @Beo keeps shouting over the engines, his gold front tooth flashing.
- 2–3s (Shot 1): @Beo jerks his chin forward as he goes on, laundry fluttering overhead.
- 3–4s (Shot 1): @Beo keeps barking orders and points one thick finger toward a turning ahead.
- 4–5s (CUT to Shot 2): @Beo keeps shouting, squinting into the wind, the lightning-bolt pattern on his shaved head gleaming.
- 5–6s (Shot 2): @Beo keeps yelling and shakes his head with a scornful grin.
- 6–7s (Shot 2): @Beo keeps shouting and draws a small square in the air with one finger.
- 7–8s (Shot 2): @Beo keeps barking, glancing back over his shoulder at the three riders.
- 8–9s (CUT to Shot 3): @Beo keeps shouting and mimes lifting a beer glass with a grin.
- 9–10s (Shot 3): @Beo keeps yelling as the four bikes lean one after another into an even narrower street hung with laundry, waving the riders on.
- 10–11s (Shot 3): @Beo keeps shouting and points back at the slowest rider with a scowl.
- 11–12s (Shot 3): @Beo finishes and closes his mouth, squinting ahead.
- 12–13s (CUT to Shot 4): At the end of the street, a pair of shining railway tracks cuts between the old tube houses, still empty.
- 13–14s (Shot 4): The empty rails gleam in the noon sun, the train street quiet.
- 14–15s (Shot 4): A long train horn echoes between the houses from far away, and @Beo squints ahead at the distant tracks, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.3s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, barking orders over the engines), in Vietnamese with exact lip-sync, said exactly once: "Bám sát vào, đừng để mất dấu! Lão với con bé vừa rẽ vào phố đường tàu kia rồi, chạy đằng trời cũng không thoát. Đứa nào lấy lại được cái hộp đen ấy, anh Hưng bao bia hơi cả tháng! Nhanh lên chúng mày, chậm là tao trừ lương cả lũ!" (no subtitles)
- @Beo starts talking within the first second; whenever @Beo speaks, the face and lips are clearly visible in that shot; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: engines revving and whining, a chorus of horns, a long distant train horn, echoes bouncing between the houses. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 1 (`canh-15/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Hà Nội's narrow train street at noon: railway tracks running between rows of old tube houses, tiny cafés with low stools pulled back from the rails, laundry and potted plants along the walls.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium two-shot of the riders stopped at the edge of the empty rails, the tiny headlamp far down the street, slow pan.
- Shot 2, 5–9s: 85mm close-up of the old man under the pith helmet, the girl peeking over his shoulder.
- Shot 3, 9–11s: 40mm medium tracking shot alongside the bike as it rolls across the empty rails.
- Shot 4, 11–15s: 50mm close-up of the girl clinging on the back seat as the bike turns into an alley.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam slows the old cream-colored step-through motorbike at the edge of the empty rails, and @Mai, holding on behind him, points far down the train street and is already speaking fast.
- 1–2s (Shot 1): @Mai keeps talking in a high squeak, pointing at a tiny train headlamp glowing very far away at the end of the street, while @Lam listens, mouth closed.
- 2–3s (Shot 1): @Mai keeps pleading fast, hugging the hard drive to her chest.
- 3–4s (Shot 1): @Mai keeps talking, squeezing her eyes shut with a comic wail.
- 4–5s (Shot 1): @Mai finishes and closes her mouth, peeking out with one eye.
- 5–6s (CUT to Shot 2): @Lam starts answering slowly in a calm husky voice, his narrow eyes on the far headlamp, still tiny in the distance.
- 6–7s (Shot 2): @Lam keeps answering unhurriedly, lifting one finger toward the distant headlamp.
- 7–8s (Shot 2): @Lam keeps speaking with a dry little smile, easing the throttle.
- 8–9s (Shot 2): @Lam keeps talking calmly, tapping the handlebar as if keeping time.
- 9–10s (CUT to Shot 3): @Lam keeps answering slowly as he rolls the bike briskly across the empty rails from left to right, the distant headlamp still tiny at the far end of the street.
- 10–11s (Shot 3): @Lam keeps talking calmly while the front wheel bumps over the far rail, @Mai clinging on behind him, mouth closed.
- 11–12s (CUT to Shot 4): @Lam finishes and closes his mouth, the bike clear of the tracks, and @Mai starts a breathless squeaky reply behind him.
- 12–13s (Shot 4): @Mai keeps talking, half laughing, her teeth chattering.
- 13–14s (Shot 4): @Mai finishes and closes her mouth, clinging on as the bike turns into a narrow alley.
- 14–15s (Shot 4): Behind @Mai, the empty rails gleam and hum in the sun, the train still far away. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, alarmed, high-pitched): "Tàu đến kìa ông! Đèn pha sáng tít đằng kia rồi, mình phanh lại đã, cháu còn chưa lấy chồng!"
- Turn 2, 5.1–11.1s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, unhurried, dry reassurance): "Còn xa lắm. Ông chạy đường này từ hồi con chưa đẻ, thuộc giờ tàu hơn cả nhà ga. Ngồi yên."
- Turn 3, 11.6–13.5s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, squeaky, half laughing): "Cháu vẫn run cầm cập, ông ơi là ông!"
- Pacing: @Mai speaks quickly, then @Lam answers slowly and calmly, then @Mai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rails humming and ticking, coffee cups rattling on saucers, tires thumping over steel rails, a long distant train horn. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 2 (`canh-15/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Hà Nội's narrow train street at noon: railway tracks running between rows of old tube houses, tiny cafés with low stools pulled back from the rails, laundry and potted plants along the walls.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- Extra: three debt collectors on black motorbikes idling behind him, well back from the rails
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the heavyset rider stopped beside the café stools well back from the rails, locked off.
- Shot 2, 4–8s: 85mm close-up of his face, the passing carriages a blur far behind him.
- Shot 3, 8–12s: 35mm medium shot of the rider and his crew, the emptying tracks beyond them.
- Shot 4, 12–15s: 28mm wide shot of the empty rails and the alley mouth across them.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Beside the café stools well back from the rails, @Beo sits stopped on his black motorbike while a long blue and white train rumbles past beyond them, and he is already shouting fast over the clatter.
- 1–2s (Shot 1): @Beo keeps ranting, waving one hand at the endless carriages.
- 2–3s (Shot 1): @Beo keeps shouting, stretching his arms wide to show how long the train is.
- 3–4s (Shot 1): @Beo turns to the three debt collectors behind him and keeps ranting, small eyes squeezed into slits.
- 4–5s (CUT to Shot 2): @Beo keeps shouting and mimes pouring a pot of tea with one hand, scowling.
- 5–6s (Shot 2): @Beo keeps yelling, rubbing his shaved head hard with one palm.
- 6–7s (Shot 2): @Beo keeps ranting, the carriages blurring past far behind him.
- 7–8s (Shot 2): @Beo keeps shouting and wags a thick finger at the three collectors.
- 8–9s (CUT to Shot 3): @Beo keeps barking, tapping his bare wrist as if checking a schedule, as the last carriage rolls away down the street behind him.
- 9–10s (Shot 3): @Beo keeps shouting, glaring at the three collectors, who sit frozen on their bikes.
- 10–11s (Shot 3): @Beo keeps yelling and flaps his arm toward the street behind them.
- 11–12s (Shot 3): @Beo finishes, closes his mouth and slumps on his motorbike.
- 12–13s (CUT to Shot 4): The far side of the tracks stands empty, only an alley mouth and a potted plant in the sun, the rails gleaming.
- 13–14s (Shot 4): The three debt collectors stare at one another with mouths shut and shoulders drooping.
- 14–15s (Shot 4): @Beo sags over his handlebars, mouth closed, as the train horn fades far away. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.3s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, frustrated rant), in Vietnamese with exact lip-sync, said exactly once: "Trời đất, tàu gì mà dài như sớ thế này! Đợi nó qua hết thì hai ông cháu kia về đến nhà, pha xong cả ấm trà rồi. Lần sau đi đòi nợ, chúng mày nhớ xem lịch tàu trước cho tao, nghe chưa! Đứng đực ra đấy làm gì, quay xe!" (no subtitles)
- @Beo starts talking within the first second; whenever @Beo speaks, the face and lips are clearly visible in that shot; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a train rumbling and clattering past, idling engines sputtering, then quiet rails ticking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 3 (`canh-15/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A narrow winding old-quarter alley maze at noon, laundry overhead, tiny doorways, potted plants.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the old man onto the girl on the back seat.
- Shot 2, 5–8s: 85mm close-up of the old man turning his head, slow push-in.
- Shot 3, 8–11s: 40mm medium two-shot from the front of the bike, locked off.
- Shot 4, 11–15s: 85mm close-up of the girl on the back seat, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam rolls the old cream-colored motorbike to a stop in the winding alley, and @Mai on the back seat is already speaking fast and breathlessly, one hand pressed to her chest.
- 1–2s (Shot 1): @Mai keeps talking giddily, fanning her face, while @Lam listens, mouth closed.
- 2–3s (Shot 1): @Mai keeps gushing, fluttering one hand over her heart.
- 3–4s (Shot 1): @Mai keeps talking and straightens her crooked round glasses with one finger.
- 4–5s (Shot 1): @Mai finishes, closes her mouth and puffs out a long breath.
- 5–6s (CUT to Shot 2): @Lam turns his head toward her and answers in a dry husky voice, tapping the brim of his battered green pith helmet.
- 6–7s (Shot 2): @Lam keeps speaking with quiet pride, chin lifted.
- 7–8s (Shot 2): @Lam keeps talking and flicks his hand back toward the railway.
- 8–9s (CUT to Shot 3): @Lam keeps speaking with a scornful little wave of his hand.
- 9–10s (Shot 3): @Lam keeps talking, rolling one shoulder as if barely warmed up.
- 10–11s (Shot 3): @Lam keeps speaking, one thick grey eyebrow raised, a crooked grin forming.
- 11–12s (CUT to Shot 4): @Mai laughs as @Lam's last word lands and starts a quick teasing reply.
- 12–13s (Shot 4): @Mai keeps teasing, wagging a finger at @Lam's back.
- 13–14s (Shot 4): @Mai finishes and closes her mouth, shaking her head with a wide closed-lip smile.
- 14–15s (Shot 4): @Mai hugs the small black hard drive and grins, mouth closed, while @Lam's shoulders shake with silent laughter. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, giddy, catching her breath): "Ghê thật đấy! Ông lái còn hơn cả phim hành động, tim cháu suýt rơi ra ngoài, kính lệch cả rồi."
- Turn 2, 5.3–11.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, dry, quietly proud): "Cả phố này từng đuổi ông còn không kịp. Mấy thằng nhóc ấy thì ăn thua gì, chưa đủ cho ông khởi động."
- Turn 3, 11.7–13.6s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, teasing, grinning): "Lại khoe rồi đấy! Ông khiêm tốn tí đi."
- Pacing: @Mai speaks quickly, then @Lam answers at an even everyday pace, then @Mai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the engine ticking down, a distant train fading away, a caged bird chirping, laundry flapping softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 4 (`canh-15/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A narrow winding old-quarter alley maze at noon, laundry overhead, tiny doorways, potted plants.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 85mm close-up of the girl on the back seat, holding the previous framing.
- Shot 2, 7–10s: 40mm medium two-shot from the front of the bike, slow push-in.
- Shot 3, 10–13s: 85mm close-up of the old man, slow push-in.
- Shot 4, 13–15s: 24mm wide shot rising from the bike above the laundry lines toward the skyline.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Mai lifts the small black hard drive beside @Lam's shoulder and is already speaking quickly in a bright, easy voice.
- 1–2s (Shot 1): @Mai keeps talking cheerfully, pointing down the alley.
- 2–3s (Shot 1): @Mai keeps chirping, patting the drive like a treasure.
- 3–4s (Shot 1): @Mai keeps talking with a confident nod, holding the drive close.
- 4–5s (Shot 1): @Mai spreads her free hand wide as if over shelves full of radios, still talking.
- 5–6s (Shot 1): @Mai keeps talking with a little shrug of total confidence.
- 6–7s (Shot 1): @Mai finishes and closes her mouth with a satisfied smile.
- 7–8s (CUT to Shot 2): @Lam's grin drains away and he starts answering slowly in a low husky voice, while @Mai listens, mouth closed.
- 8–9s (Shot 2): @Lam keeps speaking slowly, his narrow eyes drifting up past the laundry lines.
- 9–10s (Shot 2): @Lam keeps talking low, his jaw tightening.
- 10–11s (CUT to Shot 3): @Lam keeps speaking slowly, his cloudy left eye narrowing at the sky.
- 11–12s (Shot 3): @Lam keeps talking, his thick grey eyebrows drawing together.
- 12–13s (Shot 3): @Lam speaks his last words in a low murmur, eyes fixed on the distance.
- 13–14s (CUT to Shot 4): @Lam closes his mouth with his jaw set, and the camera rises above the bike past the laundry lines.
- 14–15s (Shot 4): The camera rises past tangled wires toward a gleaming glass tower far off on the sunny skyline. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.5s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, relieved and chirpy): "Giờ mình mang cái ổ sang sạp ông Khoa luôn nhé ông. Cất ở chỗ ông ấy là chắc ăn nhất, hàng trăm cái đài, ai mà tìm ra."
- Turn 2, 7.0–13.0s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, low, a sudden unease): "Ừ. Nhưng hôm nay mọi chuyện trôi êm quá đấy, con ạ. Hồi trước, êm thế này là sắp có biến."
- Pacing: @Mai speaks quickly, then @Lam answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pigeons fluttering off a roof, wind chimes tinkling, distant traffic. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 1 (`canh-16/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- Extra: two police officers in green uniforms walking calmly into the shop
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the shop owner at the smoking grill, locked off.
- Shot 2, 4–8s: 85mm close-up of her face through the drifting smoke, slow push-in.
- Shot 3, 8–12s: 40mm over-the-shoulder shot from behind a police officer onto the shop owner.
- Shot 4, 12–15s: 35mm medium shot of the shop owner by the steel table, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaHoa, in a red apron at the smoking grill, looks up without a flicker as two police officers in green uniforms walk calmly in, and is already speaking in a cool, knowing brassy voice.
- 1–2s (Shot 1): @BaHoa keeps talking, turning a skewer of pork on the grill with unhurried calm.
- 2–3s (Shot 1): @BaHoa keeps speaking and nods at the empty stools around her.
- 3–4s (Shot 1): @BaHoa keeps talking with a knowing half smile, eyes on the officers through the smoke.
- 4–5s (CUT to Shot 2): @BaHoa keeps speaking, tilting her head toward the officers with a dry look.
- 5–6s (Shot 2): @BaHoa holds up one palm as she goes on, waving away a paper she has not seen.
- 6–7s (Shot 2): @BaHoa keeps speaking, tapping her temple with one finger.
- 7–8s (Shot 2): @BaHoa keeps talking, raising her painted eyebrows high.
- 8–9s (CUT to Shot 3): @BaHoa counts two words off on her fingers as she keeps talking, while the two officers stop politely beside a steel table.
- 9–10s (Shot 3): @BaHoa keeps speaking with a short brassy laugh, shaking her head.
- 10–11s (Shot 3): @BaHoa keeps talking as she wipes her hands on a cloth and unties her red apron.
- 11–12s (Shot 3): @BaHoa finishes and closes her mouth into a cool half smile.
- 12–13s (CUT to Shot 4): @BaHoa folds the red apron neatly, mouth closed.
- 13–14s (Shot 4): @BaHoa lays the folded apron on the steel table beside a basket of herbs, mouth closed.
- 14–15s (Shot 4): @BaHoa straightens up beside the steel table, red lips closed, as the officers wait with relaxed shoulders. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking at a natural, even conversational pace, cool and knowing, unhurried), in Vietnamese with exact lip-sync, said exactly once: "Hai chú đến đúng lúc quán vừa vãn khách, khéo chọn giờ thật đấy. Đơn của cậu Hưng chứ gì? Khỏi đọc, tôi đoán được nó viết gì rồi. Lừa đảo với chả chiếm đoạt, đúng không? Thằng bé ấy học đâu ra lắm chữ thế." (no subtitles)
- @BaHoa starts talking within the first second; whenever @BaHoa speaks, the face and lips are clearly visible in that shot; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal crackling, pork sizzling, calm footsteps, fabric rustling, a distant street vendor calling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 2 (`canh-16/clip-2.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium shot of the shop owner by the steel table, holding the previous framing.
- Shot 2, 3–5s: 85mm close-up of her face over the grill smoke, slow pan.
- Shot 3, 5–8s: 50mm medium shot as she takes the hat from the wall and settles it on her curls, locked off.
- Shot 4, 8–12s: 85mm close-up of her face under the hat brim, slow push-in.
- Shot 5, 12–15s: 28mm wide shot of the shopfront as she strolls out toward the street.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaHoa raises one palm toward the two officers by the door and is already speaking in a breezy brassy voice, unhurried, as if chatting with regular customers.
- 1–2s (Shot 1): @BaHoa keeps talking, turning toward the grill with a casual wave.
- 2–3s (Shot 1): @BaHoa slides the grill's little vent shut while she keeps talking.
- 3–4s (CUT to Shot 2): @BaHoa keeps talking, moving the last skewers of pork onto a plate through the smoke.
- 4–5s (Shot 2): @BaHoa shakes her head at the thought of wasted pork as she goes on.
- 5–6s (CUT to Shot 3): @BaHoa lifts her wide-brimmed black hat from a hook on the wall, still talking.
- 6–7s (Shot 3): @BaHoa settles the hat on her burgundy curls as she keeps speaking.
- 7–8s (Shot 3): @BaHoa keeps chatting, walking two fingers through the air like little legs.
- 8–9s (CUT to Shot 4): @BaHoa flaps one hand to say she needs no escort, still talking.
- 9–10s (Shot 4): @BaHoa keeps speaking breezily with a short laugh.
- 10–11s (Shot 4): @BaHoa keeps talking, tipping the brim with one finger and winking at the officers.
- 11–12s (Shot 4): @BaHoa finishes and closes her mouth with a cheeky grin.
- 12–13s (CUT to Shot 5): @BaHoa strolls out toward the street on her own, chin high, mouth closed.
- 13–14s (Shot 5): The two officers follow at a polite distance as @BaHoa walks ahead into the sunlight.
- 14–15s (Shot 5): @BaHoa's black hat and purple blouse move away down the sunny pavement, grill smoke drifting behind her. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking at a natural, even conversational pace, breezy, like chatting with regulars), in Vietnamese with exact lip-sync, said exactly once: "Các chú đợi tôi một tí. Tắt cái bếp than đã, kẻo cháy mẻ chả của khách thì tiếc lắm. Rồi tôi đội mũ, tự đi bộ ra phường cho đàng hoàng, chẳng cần ai dẫn. Có gì đâu mà vội, phường có chạy mất đâu." (no subtitles)
- @BaHoa starts talking within the first second; whenever @BaHoa speaks, the face and lips are clearly visible in that shot; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a metal vent scraping shut, coals hissing, a plate clinking, sandals tapping on the pavement. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 3 (`canh-16/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tiny electronics repair stall tucked under a staircase in an old-quarter alley: shelves of old radios and phones, tangled wires, a soldering iron, a magnifier lamp, a single bare bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the repairman stopping at the bare workbench of his ransacked stall, locked off.
- Shot 2, 4–8s: 85mm close-up of his face under the bare bulb, locked off.
- Shot 3, 8–12s: 40mm medium shot across the workbench, slow arc.
- Shot 4, 12–15s: 100mm extreme close-up of the old wooden radio on the top shelf.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khoa stands under the single bare bulb of his ransacked stall, stares at a clean dust-free rectangle on the bare workbench and is already muttering under his breath in a dry nasal voice.
- 1–2s (Shot 1): @Khoa keeps muttering, running one long finger around the clean rectangle.
- 2–3s (Shot 1): @Khoa keeps talking flatly, sliding an open drawer shut with one knuckle.
- 3–4s (Shot 1): @Khoa keeps muttering and holds his finger and thumb a small box-width apart.
- 4–5s (CUT to Shot 2): @Khoa sniffs and keeps talking, glancing at old radios knocked askew on the shelves.
- 5–6s (Shot 2): @Khoa keeps muttering, shaking his head slowly in mock pity.
- 6–7s (Shot 2): @Khoa keeps talking with a deadpan face, his magnifier glasses on his forehead.
- 7–8s (Shot 2): @Khoa keeps muttering, one eyebrow lifting slowly.
- 8–9s (CUT to Shot 3): @Khoa keeps talking, waving one long hand toward the doorway as his eyes sweep the mess.
- 9–10s (Shot 3): @Khoa keeps muttering and gives a small mock bow toward the doorway.
- 10–11s (Shot 3): @Khoa keeps talking dryly, cupping one hand behind his ear.
- 11–12s (Shot 3): @Khoa finishes with a tiny mock sniffle, closes his mouth, and one corner of it twitches as his eyes flick to the top shelf.
- 12–13s (CUT to Shot 4): An old wooden Soviet-era radio sits untouched on the top shelf, its brass knobs glinting.
- 13–14s (Shot 4): The bare bulb sways gently, light sliding across the wooden radio's grille.
- 14–15s (Shot 4): The wooden radio sits silent and dusty on the shelf, its brass knobs catching the swaying light. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, dry, under his breath), in Vietnamese with exact lip-sync, said exactly once: "Lục tung cả sạp lên, thế mà chỉ thèm cầm mỗi cái ổ cứng đen. Đài cổ thì chê. Bọn trẻ bây giờ đúng là không biết hàng. Được thôi, các cậu cứ mang về mà thưởng thức cho đã tai. Khóc được thì càng tốt." (no subtitles)
- @Khoa starts talking within the first second; whenever @Khoa speaks, the face and lips are clearly visible in that shot; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a bare bulb buzzing, a loose wire ticking against a shelf, distant alley chatter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 4 (`canh-16/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning inside Lâm's narrow old-quarter tube house: a ground-floor room with the rolling steel shutter raised, a worn wooden table, a small family altar, sunlight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the girl at the wooden table with the phone at her ear, locked off.
- Shot 2, 4–8s: 85mm close-up of her face with the phone at her ear, locked off.
- Shot 3, 8–12s: 35mm medium shot from the street toward the doorstep, slow crane-down.
- Shot 4, 12–15s: 28mm wide shot of the open doorway and the red-stained shutter.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Mai stands at the worn wooden table holding a buzzing phone to her ear and is already speaking in a small shaky voice, her eyes glistening behind her round glasses.
- 1–2s (Shot 1): @Mai keeps talking quietly, nodding at the phone, one hand gripping the edge of the table.
- 2–3s (Shot 1): @Mai keeps speaking, swallowing hard, her chin trembling.
- 3–4s (Shot 1): @Mai keeps talking, staring at the floor, her free hand twisting her hoodie sleeve.
- 4–5s (CUT to Shot 2): @Mai keeps speaking, blinking fast behind the round glasses.
- 5–6s (Shot 2): @Mai keeps talking, pressing her free hand flat to her chest.
- 6–7s (Shot 2): @Mai keeps speaking as she walks toward the open doorway.
- 7–8s (Shot 2): @Mai forces a little smile as she keeps talking, shaking her head.
- 8–9s (CUT to Shot 3): @Mai keeps talking softly as she sinks down onto the front step.
- 9–10s (Shot 3): @Mai keeps speaking, faded red paint staining the edge of the raised steel shutter beside her.
- 10–11s (Shot 3): @Mai keeps talking, her voice thinning, eyes on the passing street.
- 11–12s (Shot 3): @Mai finishes, closes her mouth and lowers the phone from her ear.
- 12–13s (CUT to Shot 4): @Mai sets the phone face-down on the step beside her, mouth closed.
- 13–14s (Shot 4): @Mai covers her face with both hands, shoulders shaking without a sound.
- 14–15s (Shot 4): Motorbikes blur past in the street as @Mai sits huddled on the step in the warm sunlight. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking at a natural, even conversational pace, small and shaky, pretending to be fine), in Vietnamese with exact lip-sync, said exactly once: "Ừ, tớ xem rồi, từ sáng cơ. Cả lớp nhận được ảnh tớ, kèm hai chữ con nợ in đậm, cả nhóm câu lạc bộ cũng có. Không, tớ không sao. Thật mà. Cậu đừng gửi lại cho tớ nữa nhé. Thôi, tớ cúp máy đây." (no subtitles)
- @Mai starts talking within the first second; whenever @Mai speaks, the face and lips are clearly visible in that shot; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone vibrating against wood, notification pings stacking up, muffled motorbikes passing, a soft shaky breath. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 1 (`canh-17/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tube-house rooftop in the old quarter at night: potted plants, a steel water tank, a sea of tiled roofs and warm city lights, a lake glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot of both on their low stools from the front, the city lights behind, locked off.
- Shot 2, 5–10s: 85mm close-up of the girl hugging her knees, slow push-in.
- Shot 3, 10–15s: 50mm medium two-shot of both on their stools, slow drift toward their faces.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam and @Mai sit side by side on low plastic stools facing the glittering old quarter, and @Lam is already speaking softly to her, his battered green pith helmet on his knee.
- 1–2s (Shot 1): @Lam keeps speaking gently, nodding toward her hood, while @Mai stares at the lights, mouth closed.
- 2–3s (Shot 1): @Lam keeps talking softly and mimes pulling up a hood.
- 3–4s (Shot 1): @Lam keeps speaking, glancing up at the damp night air.
- 4–5s (Shot 1): @Lam finishes and closes his mouth, watching her.
- 5–6s (CUT to Shot 2): @Mai answers in a small hollow voice, hands tucked into her hoodie sleeves.
- 6–7s (Shot 2): @Mai keeps speaking as she pulls her knees up to her chest, her eyes on the city lights.
- 7–8s (Shot 2): @Mai keeps talking quietly, her round glasses reflecting the lights.
- 8–9s (Shot 2): @Mai keeps speaking, fingers twisting the ends of her sleeves.
- 9–10s (Shot 2): @Mai finishes and closes her mouth, resting her chin on her knees.
- 10–11s (CUT to Shot 3): @Lam answers quietly with his eyes on the distant lake, while @Mai listens, mouth closed.
- 11–12s (Shot 3): @Lam keeps speaking steadily and lifts his own chin a little.
- 12–13s (Shot 3): @Lam keeps talking, turning his calm narrow eyes to her.
- 13–14s (Shot 3): @Lam finishes and closes his mouth, his jaw working quietly.
- 14–15s (Shot 3): A soft breeze stirs the potted leaves as the two sit side by side, mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.0s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft and gentle): "Gió lên rồi. Kéo mũ áo lên kẻo lạnh, con. Sương xuống ướt tóc bây giờ."
- Turn 2, 5.5–10.0s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking at a natural, even conversational pace, small, hollow voice): "Cháu không lạnh đâu. Cháu chỉ đang nghĩ mai đến lớp, nhìn mặt các bạn kiểu gì đây."
- Turn 3, 10.5–13.9s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, quiet and steady): "Thì cứ ngẩng mặt lên mà đi. Con có làm gì sai đâu."
- Pacing: @Lam speaks slowly and calmly, then @Mai answers at an even everyday pace, then @Lam answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft night breeze, distant motorbike horns, a dog barking far off, wind chimes. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 2 (`canh-17/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 11s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium two-shot of both on their stools, holding the previous framing.
- Shot 2, 4–7s: 85mm close-up of the girl, slow push-in.
- Shot 3, 7–11s: 50mm over-the-shoulder shot from behind the girl onto the old man.
- Shot 4, 11–15s: 40mm medium two-shot of both on their stools, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Mai turns her head toward @Lam in the warm city glow and is already speaking in a small cracked voice, her eyes glistening.
- 1–2s (Shot 1): @Mai keeps talking, leaning her shoulder against @Lam's arm.
- 2–3s (Shot 1): @Mai keeps speaking, a tear gathering behind her glasses.
- 3–4s (Shot 1): @Mai keeps talking, twisting her hoodie sleeves in her fingers.
- 4–5s (CUT to Shot 2): @Mai keeps speaking, shaking her head at herself.
- 5–6s (Shot 2): @Mai keeps talking, shrugging with both palms up.
- 6–7s (Shot 2): @Mai keeps speaking, her voice dropping almost to a whisper.
- 7–8s (CUT to Shot 3): @Mai finishes and lowers her head, mouth closed, and @Lam shakes his head gently and starts answering slowly in a calm husky voice.
- 8–9s (Shot 3): @Lam keeps speaking gently, his cloudy left eye catching the city lights.
- 9–10s (Shot 3): @Lam keeps speaking firmly, holding up a single finger.
- 10–11s (Shot 3): @Lam keeps talking slowly, opening his hand wide.
- 11–12s (CUT to Shot 4): @Lam keeps speaking as he rests a warm hand on @Mai's head.
- 12–13s (Shot 4): @Lam keeps talking tenderly, his hand still on her head, while @Mai listens, mouth closed.
- 13–14s (Shot 4): @Lam finishes and closes his mouth, gazing out over the glittering rooftops with a firm, quiet jaw.
- 14–15s (Shot 4): @Mai wipes her eyes with her sleeve, mouth closed, as @Lam's hand slides back to his knee. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.2s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking at a natural, even conversational pace, cracked and pleading): "Sai chứ ông. Tại cháu mà bà Hoa phải về đồn, sạp ông Khoa thì bị bới tung. Hay là mình trả tiền cho nó, rồi thôi."
- Turn 2, 7.7–14.0s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, firm and tender): "Không được, con ạ. Mình trả một đồng, ngày mai nó gài thêm trăm đứa nữa, đứa nào cũng khóc như con."
- Pacing: @Mai speaks at an even everyday pace, then @Lam answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the night breeze, faint traffic below, crickets, a distant boat horn on the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 3 (`canh-17/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 40mm medium two-shot of both on their stools, holding the previous framing.
- Shot 2, 6–10s: 50mm over-the-shoulder shot from behind the girl onto the old man.
- Shot 3, 10–13s: 50mm close-up two-shot of both faces in profile, slow push-in.
- Shot 4, 13–15s: 35mm wide shot of both on their stools facing the city, slow pull-back.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Mai lifts her phone, its screen glowing blank, sits up straight and is already speaking fast to @Lam with a wry twist of her lips.
- 1–2s (Shot 1): @Mai keeps talking quickly, holding the phone up high in a showy livestreamer pose.
- 2–3s (Shot 1): @Mai keeps speaking, sweeping her free hand wide like a huge crowd.
- 3–4s (Shot 1): @Mai keeps talking, flashing an imaginary watch on her wrist with a mocking pout.
- 4–5s (Shot 1): @Mai keeps talking, tapping the phone with a knowing smirk.
- 5–6s (Shot 1): @Mai lowers the phone as she finishes and closes her mouth.
- 6–7s (CUT to Shot 2): @Lam's thick grey eyebrows rise as he turns to her and starts answering slowly, low and steady.
- 7–8s (Shot 2): @Lam keeps speaking slowly with a sly glint, while @Mai listens, mouth closed.
- 8–9s (Shot 2): @Lam keeps talking and taps his own lips with one finger.
- 9–10s (Shot 2): @Lam keeps speaking low, a slow smile creasing his face.
- 10–11s (CUT to Shot 3): @Lam keeps talking steadily and points out at the city lights.
- 11–12s (Shot 3): @Lam keeps speaking, nodding toward the distant glass towers.
- 12–13s (Shot 3): @Lam finishes and closes his mouth, while @Mai breaks into a slow closed-lip grin.
- 13–14s (CUT to Shot 4): @Mai and @Lam look out at the glittering city side by side, mouths closed.
- 14–15s (Shot 4): The two small figures sit still on their stools above the sea of tiled roofs, the lake glowing far off. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.9s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, wry, quickening with an idea): "Khoan, ông ơi. Tối nào Hưng cũng lên sóng, người xem đông như hội, khoe xe, khoe đồng hồ. Nó thích khoe còn hơn thích tiền."
- Turn 2, 6.4–13.0s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, low and steady, an idea dawning): "Thích khoe à? Thế thì mình để chính cái miệng nó tự khai, ngay trên sóng của nó, trước mặt cả triệu người."
- Pacing: @Mai speaks quickly, then @Lam answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone buzzing faintly, the night breeze, wind chimes tinkling, distant horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 4 (`canh-17/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A tube-house rooftop in the old quarter at night: potted plants, a steel water tank, a sea of tiled roofs and warm city lights, a lake glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the old man alone on his low stool, the city lights behind, locked off.
- Shot 2, 4–8s: 85mm close-up of his weathered face, slow push-in.
- Shot 3, 8–13s: 50mm medium shot from the empty stool beside him, slow arc.
- Shot 4, 13–15s: 135mm extreme close-up of his eyes, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam sits alone on his low stool on the rooftop, his face clearly visible in the warm glow, and is already speaking quietly toward the rooftop stairs with a soft chuckle in his voice.
- 1–2s (Shot 1): @Lam keeps talking, shaking his head at himself with a little smile.
- 2–3s (Shot 1): @Lam keeps speaking, rubbing his right forearm through the sleeve where the dragon tattoo hides.
- 3–4s (Shot 1): @Lam flexes the fingers of his right hand slowly as he goes on.
- 4–5s (CUT to Shot 2): @Lam keeps talking and nods toward the rooftop stairs.
- 5–6s (Shot 2): @Lam keeps speaking, waving one hand gently toward the stairs as if sending someone to bed.
- 6–7s (Shot 2): @Lam keeps talking quietly, his thick grey eyebrows lifting.
- 7–8s (Shot 2): @Lam keeps speaking as a calm, sly grin spreads across his weathered face.
- 8–9s (CUT to Shot 3): @Lam counts softly on two fingers as he keeps talking.
- 9–10s (Shot 3): @Lam keeps talking, setting his battered green pith helmet on his knee.
- 10–11s (Shot 3): @Lam keeps speaking slowly, tapping the helmet once like moving a chess piece.
- 11–12s (Shot 3): @Lam keeps talking, lifting his chin toward the distant glass towers.
- 12–13s (Shot 3): @Lam finishes and closes his mouth, still smiling.
- 13–14s (CUT to Shot 4): @Lam's narrow eyes, even the cloudy left one, light up with a sharp sparkle reflecting the city lights.
- 14–15s (Shot 4): @Lam's eyes stay still and steady, like a dragon waking. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, quiet, a slow-burning grin), in Vietnamese with exact lip-sync, said exactly once: "Lâu lắm rồi, ông mới lại thấy ngứa nghề thế này, cái tay cứ râm ran. Con đi ngủ sớm đi. Sáng mai ông cháu mình ra đồn đón bà Hoa, gọi thêm ông Khoa, rồi bàn nước cờ cuối cùng. Lần này ông đi trước." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind chimes tinkling, a soft night breeze, a far-off train horn. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 1 (`canh-18/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning at the front gate of a ward police station on a leafy street: mustard-yellow walls, an open iron gate, a tall tree, parked motorbikes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; a wide-brimmed black hat, purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- Wardrobe: in this shot @BaHoa wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot, slow dolly-back ahead of her from the open iron gate.
- Shot 2, 4–8s: 85mm close-up of her face under the hat brim, locked off.
- Shot 3, 8–12s: 50mm medium shot from the side of the pavement, slow arc.
- Shot 4, 12–15s: 85mm close-up of her face tilted up to the sun, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaHoa strolls out through the open iron gate of the ward police station in her wide-brimmed black hat, waves back toward the gate and is already speaking in a breezy brassy voice.
- 1–2s (Shot 1): @BaHoa keeps talking cheekily, her red lipstick bright and perfect.
- 2–3s (Shot 1): @BaHoa presses one palm to her chest in a little bow of thanks as she goes on.
- 3–4s (Shot 1): @BaHoa keeps speaking and stretches both arms lazily toward the sky.
- 4–5s (CUT to Shot 2): @BaHoa keeps talking, rolling her shoulders loosely.
- 5–6s (Shot 2): @BaHoa keeps speaking and pats her own cheek with a satisfied smile.
- 6–7s (Shot 2): @BaHoa wags a finger in the air as she goes on, eyes twinkling.
- 7–8s (Shot 2): @BaHoa keeps talking, cupping one hand by her mouth like a customer calling for more.
- 8–9s (CUT to Shot 3): @BaHoa keeps talking as she fans her face with one hand, gold hoop earrings swinging.
- 9–10s (Shot 3): @BaHoa keeps speaking with a theatrical roll of her eyes.
- 10–11s (Shot 3): @BaHoa keeps talking, framing her eyes with her fingers like sunglasses.
- 11–12s (Shot 3): @BaHoa pats both cheeks proudly as she finishes, then closes her mouth.
- 12–13s (CUT to Shot 4): @BaHoa tilts her chin up to the morning sun with a broad closed-lip smile.
- 13–14s (Shot 4): @BaHoa closes her eyes in the warm light, mouth closed, as if just back from a seaside holiday.
- 14–15s (Shot 4): Leaves drift down past @BaHoa's hat brim as she breathes in the morning air, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking at a natural, even conversational pace, cheeky, pleased with herself), in Vietnamese with exact lip-sync, said exactly once: "Chào các chú, tôi về nhé, cảm ơn trà đá! Ôi dào, ngủ một đêm ở phường mà còn ngon hơn ở nhà. Chẳng đứa nào réo thêm suất bún chả, cứ như vừa đi nghỉ mát ở Sầm Sơn về ấy, da dẻ hồng hào." (no subtitles)
- @BaHoa starts talking within the first second; whenever @BaHoa speaks, the face and lips are clearly visible in that shot; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birds chirping in the tree, an iron gate creaking, morning street traffic. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 2 (`canh-18/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning at the front gate of a ward police station on a leafy street: mustard-yellow walls, an open iron gate, a tall tree, parked motorbikes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; a wide-brimmed black hat, purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Wardrobe: in this shot @BaHoa wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm over-the-shoulder shot from behind the old man onto the woman in the black hat.
- Shot 2, 4–8s: 85mm close-up of the old man in the pith helmet, locked off.
- Shot 3, 8–11s: 50mm over-the-shoulder shot from behind the woman onto the old man by the motorbike.
- Shot 4, 11–15s: 40mm medium two-shot beside the motorbike, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaHoa walks up to @Lam waiting beside the old cream-colored motorbike under the tall tree and is already speaking fast with a brassy laugh in her voice.
- 1–2s (Shot 1): @BaHoa keeps talking, flicking her fingers open to show empty palms.
- 2–3s (Shot 1): @BaHoa keeps speaking sharply, wagging her empty palms side to side, while @Lam listens, mouth closed.
- 3–4s (Shot 1): @BaHoa keeps talking, jerking her thumb toward the station gate behind her.
- 4–5s (CUT to Shot 2): @BaHoa finishes her boast with a crisp sniff, and @Lam, in his battered green pith helmet, shakes his head and starts answering slowly with a dry husky chuckle.
- 5–6s (Shot 2): @Lam keeps speaking, one corner of his mouth lifting.
- 6–7s (Shot 2): @Lam keeps talking dryly, pointing at his own mouth with one finger.
- 7–8s (Shot 2): @Lam keeps speaking, eyebrows raised in mock admiration.
- 8–9s (CUT to Shot 3): @Lam keeps talking, patting the worn motorbike seat beside him.
- 9–10s (Shot 3): @Lam keeps speaking, nodding up at the sun climbing above the tree.
- 10–11s (Shot 3): @Lam finishes and closes his mouth into a quiet grin.
- 11–12s (CUT to Shot 4): @BaHoa retorts quickly with a brassy cackle, flapping one hand in the air.
- 12–13s (Shot 4): @BaHoa finishes her retort and closes her red lips, patting her wide-brimmed black hat.
- 13–14s (Shot 4): @BaHoa lifts her chin even higher, mouth closed, while @Lam chuckles silently beside the bike.
- 14–15s (Shot 4): @Lam pats the motorbike seat for her, mouth closed, as @BaHoa sniffs and pretends not to smile. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking quickly in short lively phrases, every word still clear, triumphant and sharp-tongued): "Tôi chỉ bàn chuyện đầu tư, có cầm của ai đồng nào đâu mà giữ được tôi hả ông!"
- Turn 2, 4.9–10.6s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, dry and amused): "Đi đâu cũng thế, cái miệng bà vẫn sắc hơn luật sư. Tôi đứng đây đợi từ sáng sớm đấy."
- Turn 3, 11.1–13.0s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking quickly in short lively phrases, every word still clear, a brassy cackle): "Không sắc thì sống sao nổi với các ông!"
- Pacing: @BaHoa speaks quickly, then @Lam answers slowly and calmly, then @BaHoa answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birds chirping, leaves rustling, a passing motorbike. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 3 (`canh-18/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning at the front gate of a ward police station on a leafy street: mustard-yellow walls, an open iron gate, a tall tree, parked motorbikes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 40mm medium shot of the lanky man with a radio under his arm by the parked motorbikes, locked off.
- Shot 2, 4–7s: 85mm close-up of his deadpan face, slow push-in.
- Shot 3, 7–11s: 50mm over-the-shoulder shot from behind the lanky man onto the old man.
- Shot 4, 11–15s: 40mm medium two-shot beside the parked motorbikes, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khoa, with an old wooden Soviet-era radio tucked under one arm, leans toward @Lam beside the parked motorbikes and is already speaking in a dry deadpan voice.
- 1–2s (Shot 1): @Khoa keeps talking flatly, wagging one long finger.
- 2–3s (Shot 1): @Khoa keeps talking, settling the magnifier glasses on his forehead.
- 3–4s (Shot 1): @Khoa keeps speaking smugly, swaying his head as if to an old opera tune.
- 4–5s (CUT to Shot 2): @Khoa keeps talking, counting on his long fingers.
- 5–6s (Shot 2): @Khoa keeps speaking, flashing both open hands twice.
- 6–7s (Shot 2): @Khoa presses a hand to his heart with mock tenderness as he finishes.
- 7–8s (CUT to Shot 3): @Khoa closes his mouth, eyebrows raised smugly, and @Lam squints at him and starts answering with a suspicious smile.
- 8–9s (Shot 3): @Lam keeps speaking, amused, miming a sob with one knuckle at his eye.
- 9–10s (Shot 3): @Lam keeps talking, raising both palms in a question.
- 10–11s (Shot 3): @Lam tilts his head toward the radio as he goes on.
- 11–12s (CUT to Shot 4): @Lam points one finger at the wooden radio, still talking.
- 12–13s (Shot 4): @Lam keeps talking with a knowing squint.
- 13–14s (Shot 4): @Lam finishes and closes his mouth, folding his arms.
- 14–15s (Shot 4): @Khoa hugs the radio a little tighter against his ribs, mouth closed, as the two trade a long look. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.2s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, deadpan and smug): "Cái ổ thằng Béo cầm về là ổ giả. Trong đấy toàn băng cải lương của tôi, chép đủ hai chục vở, có cả Lan và Điệp."
- Turn 2, 7.7–13.1s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, amused and suspicious): "Nghe xong chắc nó khóc thật. Thế ổ thật đâu? Đừng bảo ông lại nhét vào cái đài Liên Xô nhé."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: tree leaves rustling, a distant scooter horn, sparrows chirping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 4 (`canh-18/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning at the front gate of a ward police station on a leafy street: mustard-yellow walls, an open iron gate, a tall tree, parked motorbikes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; a wide-brimmed black hat, purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- Wardrobe: in this shot @BaHoa wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 40mm medium shot of the lanky man with the wooden radio under the tall tree, locked off.
- Shot 2, 4–6s: 85mm close-up of his face and the radio grille, slow drift.
- Shot 3, 6–11s: 50mm over-the-shoulder shot from behind the lanky man onto the woman in the black hat.
- Shot 4, 11–15s: 40mm medium two-shot of the two under the tree, slow lateral drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khoa gives a slow exaggerated wink and is already speaking in a dry, smug voice, the old wooden Soviet-era radio under his arm.
- 1–2s (Shot 1): @Khoa keeps talking, patting the wooden radio twice.
- 2–3s (Shot 1): @Khoa keeps speaking, tapping the radio's grille with one fingertip.
- 3–4s (Shot 1): @Khoa keeps talking quietly, glancing left and right along the street.
- 4–5s (CUT to Shot 2): @Khoa keeps speaking, holding the radio up a little like a proud father.
- 5–6s (Shot 2): @Khoa keeps talking, giving the radio's wooden side an affectionate rub.
- 6–7s (CUT to Shot 3): @Khoa finishes with a smug little nod, and @BaHoa narrows her sharp eyes under her wide-brimmed black hat and starts answering slowly with a sly curl of her red lips.
- 7–8s (Shot 3): @BaHoa keeps speaking slowly, savoring each word, gold hoop earrings swinging.
- 8–9s (Shot 3): @BaHoa mimes raising a toast with a mocking little smile as she goes on.
- 9–10s (Shot 3): @BaHoa keeps talking, glancing toward the distant glass towers.
- 10–11s (Shot 3): @BaHoa twirls one finger in the air like a puppeteer as she goes on.
- 11–12s (CUT to Shot 4): @BaHoa keeps speaking slowly, while @Khoa grins beside her, mouth closed.
- 12–13s (Shot 4): @BaHoa keeps talking, tapping the tip of her own nose with one finger.
- 13–14s (Shot 4): @BaHoa finishes, closes her mouth and flicks open a woven bamboo hand fan.
- 14–15s (Shot 4): @BaHoa fans herself slowly as both gaze toward the distant glass towers with closed-lip grins. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.4s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, proud, conspiratorial): "Đoán trúng phóc. Nó nằm ngay trong bụng em này, bằng chứng còn nguyên, chưa ai sờ đến. Đồ cổ thế mà được việc."
- Turn 2, 6.9–13.6s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking slowly and softly, unhurried, with a short natural pause between phrases, sly, savoring every word): "Thằng Hưng tưởng nó thắng rồi, chắc đang mở rượu ăn mừng. Lần này đến lượt nó bị mấy ông bà già dắt mũi."
- Pacing: @Khoa speaks at an even everyday pace, then @BaHoa answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: two hollow knocks on wood, a fan snapping open, birds chirping, rustling leaves. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 1 (`canh-19/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the livestreamer under the ring light, handheld.
- Shot 2, 4–8s: 85mm close-up of the livestreamer's face lit by the ring light, locked off.
- Shot 3, 8–12s: 50mm medium shot from in front of the livestreamer, deep focus on the far elevator beyond the glass.
- Shot 4, 12–15s: 28mm wide shot down the call-center aisle past the livestreamer's shoulder toward the glass door, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung clicks the ring light into a bright white circle on screen-right, raises his phone on its small selfie gimbal and is already speaking fast into it like a livestream salesman.
- 1–2s (Shot 1): @Hung keeps talking to the lens with a cocky grin, his free hand beckoning the viewers in.
- 2–3s (Shot 1): @Hung spins once on his white sneakers, still talking fast, silver rings flashing.
- 3–4s (Shot 1): @Hung leans close to the gimbal and keeps up the patter, eyebrows bouncing over his gold-rimmed glasses.
- 4–5s (CUT to Shot 2): @Hung keeps talking in close-up, the ring light a white circle in his glasses, and taps the phone's glowing blank screen.
- 5–6s (Shot 2): @Hung pats the chest of his black satin bomber jacket and keeps selling, voice slick and loud.
- 6–7s (Shot 2): @Hung winks at the lens and keeps talking, rubbing his thumb and fingers together as if counting cash.
- 7–8s (Shot 2): @Hung keeps talking fast, flashing a wide grin at the phone.
- 8–9s (CUT to Shot 3): @Hung's eyes flick up past the phone and he breaks off mid-pitch, then keeps talking, slower and puzzled.
- 9–10s (Shot 3): Deep behind @Hung beyond the glass on screen-left, the steel elevator doors slide open and @Lam steps out alone in a battered green pith helmet, mouth closed, while @Hung keeps talking toward the lens.
- 10–11s (Shot 3): @Hung lowers the gimbal a little and asks his puzzled question, squinting at the far figure in the green helmet.
- 11–12s (Shot 3): @Hung finishes the question and closes his mouth, frozen mid-pose with the gimbal half raised.
- 12–13s (CUT to Shot 4): @Lam walks slowly up the aisle between the glowing monitors toward the boss room, both hands empty, mouth closed.
- 13–14s (Shot 4): @Lam keeps coming at an unhurried pace, plastic sandals scuffing the carpet, mouth closed.
- 14–15s (Shot 4): @Hung glances back over his shoulder in the foreground, mouth closed, as @Lam reaches the open glass door of the boss room. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.5s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, slick showman, then caught off guard), in Vietnamese with exact lip-sync, said exactly once: "Lên sóng rồi đây các em ơi! Đông thật đấy, vào muộn là hết chỗ nhé. Anh hứa từ hôm qua rồi, tối nay anh mở két, cho các em ngắm tiền thật tận mắt, đếm hộ anh luôn. Ơ, khoan đã. Cụ nào đội mũ cối mò lên tận đây thế kia?" (no subtitles)
- @Hung starts talking within the first second; whenever @Hung speaks, the face and lips are clearly visible in that shot; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ring light switch clicking on, soft electronic hum, a few notification chimes, a distant elevator chime, sandals scuffing on carpet. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 2 (`canh-19/clip-2.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the old man standing in the open glass doorway, slow push-in.
- Shot 2, 3–7s: 85mm close-up of the old man's face under the brim of his helmet, locked off.
- Shot 3, 7–10s: 50mm over-the-shoulder shot from behind the old man onto the livestreamer under the ring light.
- Shot 4, 10–13s: 85mm close-up of the livestreamer grinning into the gimbal, handheld.
- Shot 5, 13–15s: 35mm medium two-shot across the boss room, the old man in the doorway on the left and the livestreamer on the right.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam stands in the open glass doorway of the boss room on screen-left, one finger tapping the brim of his battered green pith helmet, and is already speaking slowly in a calm husky voice.
- 1–2s (Shot 1): @Lam keeps speaking courteously, almost formally, his calm narrow eyes on the ring light.
- 2–3s (Shot 1): @Lam lifts one open empty hand a little as he goes on, voice level.
- 3–4s (CUT to Shot 2): @Lam keeps speaking in close-up, deep sun wrinkles creasing as he nods toward the glowing gimbal phone.
- 4–5s (Shot 2): @Lam goes on slowly, the cloudy left eye catching the white light.
- 5–6s (Shot 2): @Lam keeps talking evenly, both empty hands now resting at his sides.
- 6–7s (Shot 2): @Lam finishes the offer, closes his mouth and waits without blinking.
- 7–8s (CUT to Shot 3): @Hung swings the gimbal phone toward the doorway and starts talking loudly into it like a livestream salesman, a mocking grin spreading.
- 8–9s (Shot 3): @Hung keeps talking fast to his viewers, one ringed hand flourishing toward the old man in the doorway.
- 9–10s (Shot 3): @Hung leans toward the lens and keeps up the gleeful mockery, eyebrows high.
- 10–11s (CUT to Shot 4): @Hung keeps talking in close-up, pointing two ringed fingers at the floor as if ordering a bow.
- 11–12s (Shot 4): @Hung bounces on his heels with glee as he goes on.
- 12–13s (Shot 4): @Hung pinches two fingers together for a tiny discount and keeps mocking, voice loud.
- 13–14s (CUT to Shot 5): @Hung finishes with a flourish and closes his mouth in a smug grin, while @Lam stands perfectly still in the doorway, mouth closed.
- 14–15s (Shot 5): @Lam's empty hands hang relaxed at his sides as he looks past the raised gimbal toward the glass desk, both men silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.0s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, level and courteous, almost formal): "Cậu Hưng đấy à? Tôi đến trả nợ thay cháu. Nhưng cậu nhận tiền ngay trên sóng, cho thiên hạ cùng làm chứng."
- Turn 2, 7.5–13.4s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, gleeful mockery for the viewers): "Mọi người ơi, có cụ xe ôm đến trả nợ hộ cháu này! Cụ quỳ xuống xin em một câu cho tử tế, em bớt cho ít lãi."
- Pacing: @Lam speaks slowly and calmly, then @Hung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ring light hum, distant keyboard clicks, a rising flurry of notification chimes, the glass door settling on its hinge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 3 (`canh-19/clip-3.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium two-shot across the boss room, holding the previous framing.
- Shot 2, 3–7s: 85mm close-up of the old man in the chrome chair, slow push-in.
- Shot 3, 7–10s: 40mm medium two-shot, the old man seated on the left and the livestreamer standing on the right under the ring light.
- Shot 4, 10–13s: 85mm close-up of the livestreamer under the ring light, handheld.
- Shot 5, 13–15s: 35mm medium two-shot from the side of the glass desk, gentle lateral glide.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam walks past @Hung's raised gimbal toward the wide glass desk and is already speaking slowly in a dry husky voice, rubbing one knee as if it aches.
- 1–2s (Shot 1): @Lam keeps speaking as he pulls out the chrome swivel chair, while @Hung turns after him, mouth closed, gimbal still raised.
- 2–3s (Shot 1): @Lam sits down unhurried, rests his battered green pith helmet on his knee and goes on talking.
- 3–4s (CUT to Shot 2): @Lam keeps speaking in close-up, pouring himself a small cup of tea from the teapot.
- 4–5s (Shot 2): @Lam lifts the steaming cup and keeps talking slowly, unhurried.
- 5–6s (Shot 2): @Lam blows across the tea, eyes half closed, as he goes on.
- 6–7s (Shot 2): @Lam lands the last words slowly, a faint smile at the corner of his mouth.
- 7–8s (CUT to Shot 3): @Lam closes his mouth and sips, as @Hung on screen-right swings the gimbal back to his own face and starts talking fast to his viewers.
- 8–9s (Shot 3): @Hung keeps talking fast, eyebrows flying up, his free hand jabbing toward the old man in the chair.
- 9–10s (Shot 3): @Hung's voice goes squeaky as he keeps talking, gold-rimmed glasses slipping down his nose.
- 10–11s (CUT to Shot 4): @Hung keeps talking in close-up, sweat beading under his ash-blond fringe.
- 11–12s (Shot 4): @Hung turns the lens toward the chair and keeps squeaking out his complaint to the viewers.
- 12–13s (Shot 4): @Hung asks his viewers the last question straight into the lens, eyes darting.
- 13–14s (CUT to Shot 5): @Hung finishes, closes his mouth and stands frozen under the white ring light, gimbal still raised.
- 14–15s (Shot 5): @Lam leans back in the chrome chair with the cup, a faint closed-mouth smile, like an old man at a street tea stall. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.3s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, dry, unhurried, settling in): "Già rồi, quỳ thì mỏi gối lắm, cậu ạ. Cho tôi ngồi nhờ cái ghế này, xin chén trà nóng đã, rồi mình tính."
- Turn 2, 7.8–13.7s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, flustered, voice going squeaky): "Ơ kìa, cụ ngồi luôn vào ghế của em, lại còn tự rót trà uống ngon lành thế kia! Ai quen cụ này thì nhắn em ngay với!"
- Pacing: @Lam speaks slowly and calmly, then @Hung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: chair wheels rolling on the floor, leather creaking, tea trickling into a small cup, ring light hum, scattered notification chimes. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 4 (`canh-19/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Inside a parked white van turned into a surveillance post at night: two laptops glowing, tangled cables, a thermos, tinted windows with neon reflections.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot at the fold-out desk, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the gadget man holding the hard drive, locked off.
- Shot 3, 10–13s: 35mm medium two-shot of both at the fold-out desk, slow push-in.
- Shot 4, 13–15s: 50mm close-up of the granddaughter's face above the laptop, her finger hovering over the enter key.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Inside the parked white van, @Mai on screen-left types at lightning speed and is already speaking fast to @Khoa in an excited whisper, her round glasses lit by the screens.
- 1–2s (Shot 1): @Mai keeps whispering fast and points at the glowing blank screen, while @Khoa on screen-right listens, mouth closed.
- 2–3s (Shot 1): @Mai keeps talking, bouncing a little in her seat, one hand hovering over the keys.
- 3–4s (Shot 1): @Mai keeps whispering fast, eyes wide behind her glasses.
- 4–5s (Shot 1): @Mai rushes through the rest of her plan and closes her mouth, as @Khoa lifts a small black hard drive out of the opened wooden radio.
- 5–6s (CUT to Shot 2): @Khoa clicks the hard drive into the side of a laptop and starts answering in a dry deadpan voice, magnifier glasses perched on his bald crown.
- 6–7s (Shot 2): @Khoa raises one eyebrow as he goes on, quietly smug.
- 7–8s (Shot 2): @Khoa keeps talking in close-up, tapping the old radio's wooden case with two fingers.
- 8–9s (Shot 2): @Khoa keeps speaking to @Mai, nodding toward the glowing laptop.
- 9–10s (Shot 2): @Khoa keeps talking flatly, the corner of his mouth twitching.
- 10–11s (CUT to Shot 3): @Khoa finishes with a sly wink and closes his mouth, while @Mai presses her lips together to hold back a giggle.
- 11–12s (Shot 3): @Mai lowers her hand and starts whispering quickly again, beaming at @Khoa.
- 12–13s (Shot 3): @Mai keeps whispering fast, giving @Khoa a double thumbs-up.
- 13–14s (CUT to Shot 4): @Mai finishes her last words and closes her mouth with a delighted grin, turning back to the laptop.
- 14–15s (Shot 4): @Mai's finger hovers above the enter key as she presses her lips together and waits, neon sliding over the tinted window behind her. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, excited whisper): "Ông Khoa ơi, ông cháu vào tận phòng nó rồi! Ông cháu ra hiệu một cái là cháu bấm nút ngay."
- Turn 2, 5.3–10.3s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, flat deadpan, quietly smug): "Ổ thật cắm rồi đây, chạy ngon. Cái ổ cải lương thì thằng Béo vẫn ôm khư khư như vàng."
- Turn 3, 10.8–13.3s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, giggling whisper): "Ông đúng là phù thuỷ, cháu phục ông sát đất luôn ấy!"
- Pacing: @Mai speaks quickly, then @Khoa answers at an even everyday pace, then @Mai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rapid keyboard clatter, a plug clicking into a port, a soft confirmation beep, muffled street traffic outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 1 (`canh-20/clip-1.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium shot of the old man in the chrome chair across the glass desk, slow push-in.
- Shot 2, 3–7s: 85mm close-up of the old man in the chrome chair, locked off.
- Shot 3, 7–10s: 50mm over-the-shoulder shot from behind the seated old man onto the livestreamer.
- Shot 4, 10–13s: 85mm close-up of the livestreamer leaning into the gimbal, handheld.
- Shot 5, 13–15s: 40mm medium two-shot across the glass desk, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam sits calmly in the chrome chair on screen-left with his pith helmet on his knee and is already speaking slowly in a husky steady voice toward the gimbal.
- 1–2s (Shot 1): @Lam keeps speaking quietly, holding up five weathered fingers.
- 2–3s (Shot 1): @Lam turns his open palm upward as he goes on, eyes narrowing.
- 3–4s (CUT to Shot 2): @Lam keeps talking in close-up, voice level and pointed.
- 4–5s (Shot 2): @Lam tilts his head and goes on, the cloudy left eye catching the ring light.
- 5–6s (Shot 2): @Lam asks his question slowly, his eyes on the gimbal lens.
- 6–7s (Shot 2): @Lam finishes and closes his mouth, waiting patiently with his hands on his knees.
- 7–8s (CUT to Shot 3): @Hung on screen-right leans into the gimbal lens and starts answering loudly and smugly.
- 8–9s (Shot 3): @Hung keeps talking fast, wagging three ringed fingers in the air.
- 9–10s (Shot 3): @Hung smirks at the lens and goes on, gold-rimmed glasses flashing in the ring light.
- 10–11s (CUT to Shot 4): @Hung keeps bragging in close-up, chin up, silver rings glinting.
- 11–12s (Shot 4): @Hung mimes tapping send on the glowing blank screen as he keeps talking.
- 12–13s (Shot 4): @Hung shrugs with both palms up as he asks his last question.
- 13–14s (CUT to Shot 5): @Hung closes his mouth in a cocky grin, while @Lam sits motionless with his hands on his knees, mouth closed.
- 14–15s (Shot 5): @Lam lifts the steaming teacup slowly, eyes still on @Hung, both men silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.4s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and pointed): "Cháu tôi vay có năm triệu, ba tháng thành trăm rưỡi. Lãi gì mà đẻ nhanh thế, cậu tính kiểu gì?"
- Turn 2, 6.9–13.0s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, smug, showing off): "Ba phần trăm một ngày, cụ ạ, rẻ chán! Đứa nào không trả thì em gửi ảnh nó cho cả họ hàng, cả lớp. Luật nào cấm được em?"
- Pacing: @Lam speaks slowly and calmly, then @Hung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ring light hum, distant keyboard clicks, notification chimes multiplying, a leather chair creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 2 (`canh-20/clip-2.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium two-shot across the glass desk, holding the previous framing.
- Shot 2, 3–6s: 85mm low-angle close-up of the old man in the chrome chair, slow arc.
- Shot 3, 6–9s: 50mm over-the-shoulder shot from behind the seated old man onto the livestreamer.
- Shot 4, 9–13s: 35mm low-angle close-up of the livestreamer bragging into the gimbal, handheld.
- Shot 5, 13–15s: 28mm low-angle wide shot arcing around the ring light.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam sets his teacup down on the glass desk with a soft click and is already speaking slowly and calmly up at @Hung.
- 1–2s (Shot 1): @Lam keeps speaking softly, one hand gesturing gently toward the glowing gimbal phone.
- 2–3s (Shot 1): @Lam keeps talking, each word weighty, his narrow eyes steady toward screen-right.
- 3–4s (CUT to Shot 2): @Lam goes on slowly in a low-angle close-up, a faint glint in his eyes.
- 4–5s (Shot 2): @Lam nods once toward the phone as he goes on.
- 5–6s (Shot 2): @Lam lands the last words, closes his mouth and leans back in the chrome chair.
- 6–7s (CUT to Shot 3): @Hung swings the gimbal up to his own face and starts bragging loudly, chin raised high.
- 7–8s (Shot 3): @Hung keeps boasting fast, spreading his ringed hands wide for the lens.
- 8–9s (Shot 3): @Hung jabs a thumb at his own chest and goes on, louder.
- 9–10s (CUT to Shot 4): @Hung keeps bragging in a low-angle close-up, grin stretched wide, gold-rimmed glasses gleaming.
- 10–11s (Shot 4): @Hung rubs his thumb and fingers together for the lens as he keeps talking.
- 11–12s (Shot 4): @Hung keeps bragging fast, strutting a step under the ring light.
- 12–13s (Shot 4): @Hung tips his head back with a laugh as he lands the last words.
- 13–14s (CUT to Shot 5): @Hung closes his mouth with his chin high, while @Lam folds his arms on screen-left with a slow closed-mouth smile.
- 14–15s (Shot 5): The blank screen of the gimbal phone flickers with a flood of light in @Hung's raised hand, both men silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.9s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft but weighty): "Hay đấy. Cậu nói to lên một chút nữa, để hai triệu người đang xem cùng nghe cho rõ."
- Turn 2, 6.4–13.1s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, loud bragging, chin up): "Nói thì nói! Tháng nào anh cũng siết vài nghìn đứa sinh viên. Chậm một hôm thôi là bố mẹ nó, người yêu nó nhận ảnh ngay. Thế mới ra tiền chứ!"
- Pacing: @Lam speaks slowly and calmly, then @Hung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a teacup clicking on glass, ring light hum, a sudden flood of notification chimes, the distant drone of the city. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 3 (`canh-20/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Inside a parked white van turned into a surveillance post at night: two laptops glowing, tangled cables, a thermos, tinted windows with neon reflections.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot of both at the fold-out desk, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the gadget man peering through his magnifier glasses, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the gadget man onto the granddaughter.
- Shot 4, 13–15s: 50mm medium shot of the granddaughter leaning back in her seat, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Inside the parked white van, @Mai on screen-left presses the enter key firmly and is already speaking fast in a breathless whisper, the screen glow flaring in her round glasses.
- 1–2s (Shot 1): @Mai keeps talking fast, pointing at the screen, eyes wide.
- 2–3s (Shot 1): @Mai leans closer to the screen and goes on, breathless.
- 3–4s (Shot 1): @Mai keeps whispering fast, two halves of light splitting across her glasses.
- 4–5s (Shot 1): @Mai finishes and closes her mouth, as @Khoa on screen-right pulls his magnifier glasses down over his eyes and starts answering in a dry nasal deadpan.
- 5–6s (CUT to Shot 2): @Khoa keeps speaking flatly, peering at the two blank laptop screens pulsing in bands of white and red light.
- 6–7s (Shot 2): @Khoa traces a bony finger down the glowing screen as he goes on, precise and unhurried.
- 7–8s (Shot 2): @Khoa keeps speaking in close-up, eyes huge behind the magnifier glasses.
- 8–9s (Shot 2): @Khoa keeps talking, his finger sliding lower and lower down the endless glow.
- 9–10s (Shot 2): @Khoa finishes with a tiny satisfied nod and closes his mouth.
- 10–11s (CUT to Shot 3): @Mai gasps and starts blurting out a quick line, staring at the screen.
- 11–12s (Shot 3): @Mai keeps talking fast in disbelief, both hands on her cheeks.
- 12–13s (Shot 3): @Mai keeps whispering, shaking her head, eyes shining.
- 13–14s (CUT to Shot 4): @Mai says her last words, closes her mouth and leans back in her seat with a small tight-lipped smile.
- 14–15s (Shot 4): The laptop light flickers over @Mai's lavender hoodie as neon slides across the tinted window behind her. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, breathless, finger on the key): "Ông cháu ra hiệu rồi! Cháu bấm đây. Ông nhìn này, màn hình nó tách làm đôi rồi kìa!"
- Turn 2, 4.9–9.9s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, dry and precise, peering close): "Ừ. Nửa này mặt nó đang khoe, nửa kia mấy nghìn cái tên với số lãi thật, dài dằng dặc."
- Turn 3, 10.4–13.2s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, a gasp of disbelief): "Người xem vọt lên năm triệu rồi ông ơi! Cháu không tin nổi!"
- Pacing: @Mai speaks quickly, then @Khoa answers at an even everyday pace, then @Mai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a single decisive key click, a rising electronic chime, rapid soft beeps, muffled street traffic. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 4 (`canh-20/clip-4.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the livestreamer under the ring light, handheld.
- Shot 2, 3–7s: 85mm close-up of the livestreamer's face strobed by the phone light, handheld.
- Shot 3, 7–10s: 50mm over-the-shoulder shot from behind the livestreamer onto the old man in the chrome chair.
- Shot 4, 10–13s: 85mm close-up of the old man holding his teacup, locked off.
- Shot 5, 13–15s: 35mm medium two-shot with the old man sharp in the foreground and the livestreamer soft behind him.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung stands under the ring light as the gimbal phone buzzes nonstop in his hand, its blank screen strobing white and red over his face, and he is already speaking fast in a panic.
- 1–2s (Shot 1): @Hung keeps talking fast, jabbing at the glowing screen with his thumb, sweat on his temple.
- 2–3s (Shot 1): @Hung's voice cracks as he shouts toward the call-center floor beyond the glass.
- 3–4s (CUT to Shot 2): @Hung keeps jabbing the screen in close-up and talking, his glasses askew.
- 4–5s (Shot 2): @Hung shakes the phone hard and keeps shouting, eyes bulging.
- 5–6s (Shot 2): @Hung keeps jabbing the screen, voice cracking higher.
- 6–7s (Shot 2): @Hung finishes in a cracked panic and closes his mouth, the screen still strobing in his hand.
- 7–8s (CUT to Shot 3): @Lam in the chrome chair lowers a small steaming teacup and starts speaking slowly, calm and faintly amused.
- 8–9s (Shot 3): @Lam keeps speaking slowly, one hand raised in a gentle wait gesture.
- 9–10s (Shot 3): @Lam goes on calmly, eyes crinkling.
- 10–11s (CUT to Shot 4): @Lam keeps talking softly in close-up, a faint smile tugging at his mouth.
- 11–12s (Shot 4): @Lam keeps speaking, unhurried, tapping one finger on the glass desk.
- 12–13s (Shot 4): @Lam says the last words slowly and closes his mouth.
- 13–14s (CUT to Shot 5): @Lam sets the cup down on the glass desk with a calm closed-mouth smile, as if nothing at all has happened.
- 14–15s (Shot 5): @Hung stands frozen in soft focus behind him, the phone still strobing in his hand, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.5s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, panicked, voice cracking): "Cái gì đây? Ai đưa danh sách khách nợ của tôi lên sóng thế? Tắt đi! Tắt ngay đi! Sao bấm mãi mà nó không tắt được thế này?"
- Turn 2, 7.0–13.0s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, calm, faintly amused): "Đừng tắt vội, cậu ạ. Cậu khai hay lắm cơ mà. Giờ thì ai nghe cũng nhớ từng chữ một rồi."
- Pacing: @Hung speaks quickly, then @Lam answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone buzzing nonstop, a torrent of rapid notification pings, ring light hum, a teacup set gently on glass. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 1 (`canh-21/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: young callers beyond the glass pulling off their headsets and walking out between the desks
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the old man in the chrome chair with the call-center floor beyond the glass, slow lateral glide.
- Shot 2, 4–8s: 85mm close-up of the old man's face, locked off.
- Shot 3, 8–13s: 50mm medium profile shot of the old man with the emptying floor beyond the glass, slow push-in.
- Shot 4, 13–15s: 28mm wide shot from the call-center floor back toward the lit glass room.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam sits in the chrome chair on screen-left of the glass-walled boss room, teacup in hand, and is already speaking calmly toward screen-right, as young callers beyond the glass pull off their headsets.
- 1–2s (Shot 1): @Lam keeps talking low and weary, nodding toward the glass.
- 2–3s (Shot 1): @Lam rests the cup on his knee and goes on, matter-of-fact.
- 3–4s (Shot 1): @Lam keeps speaking while beyond the glass the callers rise from their seats with bags on their shoulders.
- 4–5s (CUT to Shot 2): @Lam keeps talking in close-up, deep sun wrinkles around his calm narrow eyes.
- 5–6s (Shot 2): @Lam lowers his voice as he goes on, his eyes softening.
- 6–7s (Shot 2): @Lam keeps speaking, glancing toward the glass with a slight shake of his head.
- 7–8s (Shot 2): @Lam keeps talking quietly, one weathered hand open on his knee.
- 8–9s (CUT to Shot 3): @Lam keeps talking softly in profile, while far beyond the glass the callers walk out in a quiet line toward the elevator, never looking back.
- 9–10s (Shot 3): @Lam keeps speaking as he watches them go.
- 10–11s (Shot 3): @Lam lifts one hand in a small easy wave toward the leaving callers as he goes on.
- 11–12s (Shot 3): @Lam keeps talking, the last words slow and gentle.
- 12–13s (Shot 3): @Lam finishes and closes his mouth.
- 13–14s (CUT to Shot 4): Rows of empty chairs slowly turn under the glowing monitors, abandoned headsets glinting in the neon.
- 14–15s (Shot 4): @Lam takes a slow sip of tea, small and calm inside the lit glass room at the end of the deserted floor, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, low and weary, matter-of-fact), in Vietnamese with exact lip-sync, said exactly once: "Cậu nhìn kìa, người ta tháo tai nghe cả rồi. Họ đi làm thuê kiếm bát cơm thôi, chứ ai muốn vào tù thay cậu đâu. Ai chẳng có bố mẹ ở quê đang ngóng. Cứ để họ về, mai còn đi tìm việc tử tế." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: headsets set down softly on desks, chairs rolling back, quiet footsteps, a distant elevator chime, a teacup lifted from glass. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 2 (`canh-21/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- Extra: the last few young callers walking away toward the elevator with their bags
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium shot of the livestreamer bursting into the aisle, handheld.
- Shot 2, 3–7s: 85mm close-up of the livestreamer, handheld push-in.
- Shot 3, 7–12s: 35mm medium shot of the livestreamer in the aisle with the far elevator behind him, locked off.
- Shot 4, 12–15s: 24mm wide shot down the empty aisle toward the elevator, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung bursts out of the glass boss-room door into the aisle, one ringed hand raised high, and is already shouting fast after the departing callers.
- 1–2s (Shot 1): @Hung keeps shouting, jabbing a finger at the empty chairs.
- 2–3s (Shot 1): @Hung stamps one white sneaker and keeps yelling, face flushed.
- 3–4s (CUT to Shot 2): @Hung keeps shouting in close-up, a vein standing out on his temple.
- 4–5s (Shot 2): @Hung's voice drops and his eyebrows tilt up as he keeps talking.
- 5–6s (Shot 2): @Hung presses both palms together and keeps talking, now pleading, gold-rimmed glasses askew.
- 6–7s (Shot 2): @Hung keeps begging, nodding rapidly, a forced smile trembling.
- 7–8s (CUT to Shot 3): @Hung keeps pleading with palms together, while far behind him the last young callers walk toward the elevator without turning around.
- 8–9s (Shot 3): @Hung holds up two fingers, then three, still talking fast.
- 9–10s (Shot 3): @Hung spreads his arms wide and keeps promising, voice cracking.
- 10–11s (Shot 3): @Hung keeps calling after them, one hand outstretched toward the elevator.
- 11–12s (Shot 3): @Hung finishes his plea and closes his mouth, hand still outstretched.
- 12–13s (CUT to Shot 4): Far down the aisle, the steel elevator doors slide shut on the last callers.
- 13–14s (Shot 4): @Hung stands panting alone in the empty aisle, satin bomber jacket rumpled, mouth closed.
- 14–15s (Shot 4): @Hung's hands drop to his sides among the abandoned desks, a lone chair still turning slowly beside him. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.3s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, yelling, then begging), in Vietnamese with exact lip-sync, said exactly once: "Này, đi đâu đấy? Ngồi xuống hết cho tao! Đứa nào bước ra khỏi cửa là tao trừ sạch lương, nghe chưa? Thôi, các em ơi, quay lại đi mà. Tháng này anh thưởng gấp đôi, gấp ba cũng được, anh xin đấy! Ai ở lại anh cho làm trưởng phòng luôn!" (no subtitles)
- @Hung starts talking within the first second; whenever @Hung speaks, the face and lips are clearly visible in that shot; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a glass door swinging open, a lone chair slowly spinning, monitor hum, elevator doors sliding closed. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 3 (`canh-21/clip-3.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium two-shot at the boss-room doorway, handheld.
- Shot 2, 3–7s: 85mm close-up of the heavyset collector, handheld.
- Shot 3, 7–10s: 50mm over-the-shoulder shot from behind the heavyset collector onto the livestreamer.
- Shot 4, 10–13s: 85mm close-up of the livestreamer, slow push-in.
- Shot 5, 13–15s: 28mm wide shot of the doorway and the long aisle, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Beo skids to a stop in the boss-room doorway on screen-left, dripping sweat, holds up a phone with a glowing blank screen and is already speaking fast, blurting the news, while @Hung on screen-right listens, mouth closed.
- 1–2s (Shot 1): @Beo keeps talking fast and out of breath, waving the phone.
- 2–3s (Shot 1): @Beo points back toward the elevator, still blurting, gold front tooth flashing.
- 3–4s (CUT to Shot 2): @Beo keeps gasping out the words in close-up, wiping his shaved head with his palm.
- 4–5s (Shot 2): @Beo jabs a thick finger at the glowing phone as he goes on.
- 5–6s (Shot 2): @Beo keeps talking fast, eyes darting back down the aisle.
- 6–7s (Shot 2): @Beo finishes and closes his mouth, panting.
- 7–8s (CUT to Shot 3): @Hung turns slowly toward him and starts answering low and cold through gritted teeth.
- 8–9s (Shot 3): @Hung keeps speaking slowly, glasses catching the ring light, jaw tight.
- 9–10s (Shot 3): @Hung goes on in a cold low voice, eyes narrowing.
- 10–11s (CUT to Shot 4): @Hung keeps talking in close-up, lifting one ringed finger toward the elevator.
- 11–12s (Shot 4): @Hung keeps speaking coldly, the ringed finger still pointing.
- 12–13s (Shot 4): @Hung lands the last words slowly and closes his mouth, jaw clenched.
- 13–14s (CUT to Shot 5): @Beo nods rapidly, mouth closed, and backs out of the doorway.
- 14–15s (Shot 5): @Beo turns and lumbers off down the long aisle, flip-flops flapping, while @Hung stands rigid under the ring light. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.3s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, panicked and out of breath): "Đại ca ơi, toang thật rồi! Cả mạng đang chia sẻ lại buổi live của anh, công an kinh tế đang đi thang máy lên đến nơi rồi!"
- Turn 2, 6.8–13.0s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking slowly and softly, unhurried, with a short natural pause between phrases, low and cold through gritted teeth): "Gọi hết anh em xuống chặn cổng ngay. Lão ấy mà lọt ra được đến đường, thì mày cũng khỏi về nữa."
- Pacing: @Beo speaks quickly, then @Hung answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heavy running footsteps, flip-flops flapping, a phone buzzing nonstop, a distant siren far below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 4 (`canh-21/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium shot of the old man rising from the chrome chair, locked off.
- Shot 2, 3–7s: 85mm close-up of the old man settling his pith helmet, locked off.
- Shot 3, 7–13s: 50mm medium shot of the old man by the glass desk, slow pull-back.
- Shot 4, 13–15s: 24mm wide shot down the empty aisle toward the elevator, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam rises from the chrome chair, sets the empty teacup neatly upside down on its saucer and is already speaking calmly toward screen-right with a polite crinkle-eyed smile.
- 1–2s (Shot 1): @Lam keeps talking politely, with a small bow of the head toward someone off screen-right.
- 2–3s (Shot 1): @Lam picks up the battered green pith helmet from the desk as he goes on.
- 3–4s (CUT to Shot 2): @Lam keeps speaking calmly, eyes twinkling, as he settles the helmet on his grey crew cut.
- 4–5s (Shot 2): @Lam fastens the strap under his chin, still talking with dry humor.
- 5–6s (Shot 2): @Lam raises his thick grey eyebrows in close-up as he adds the next remark.
- 6–7s (Shot 2): @Lam keeps talking, the corner of his mouth lifting in a sly smile.
- 7–8s (CUT to Shot 3): @Lam keeps speaking as he tugs his grey windbreaker straight, hands calm.
- 8–9s (Shot 3): @Lam glances down through the glass wall toward the street far below as he goes on.
- 9–10s (Shot 3): @Lam clasps his hands behind his back and keeps talking, polite and dry.
- 10–11s (Shot 3): @Lam keeps speaking with a small shrug, as if warning about the weather.
- 11–12s (Shot 3): @Lam goes on, the last words slow and dry.
- 12–13s (Shot 3): @Lam finishes, closes his mouth and gives one small nod toward screen-right.
- 13–14s (CUT to Shot 4): @Lam strolls away down the empty aisle between the glowing monitors toward the open elevator, hands behind his back.
- 14–15s (Shot 4): @Lam's plastic sandals scuff the carpet as he walks on, a small figure under the neon, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, polite, with a sly dry humor), in Vietnamese with exact lip-sync, said exactly once: "Trà ngon đấy, cảm ơn cậu. Tôi xin phép về trước. À, cậu dặn đàn em dưới cổng đứng cho ngay ngắn vào. Lát nữa hàng xóm tôi kéo nhau ra đón, đông lắm, toàn người già, kẻo chúng nó lại giật mình mà ngã xe." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a teacup set down on glass, a helmet strap clicking, unhurried sandal footsteps, a distant elevator chime. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 1 (`canh-22/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on the wide street in front of the glass tower: neon reflections on the asphalt, tall trees, parked motorbikes, warm streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: twenty young debt collectors in black on motorbikes revving in a wide half-circle far from the tower doors, seen only as blurred helmets and handlebars in the glare
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the old man on the pavement facing the glare, locked off.
- Shot 2, 4–8s: 85mm close-up of the old man's face in the headlight glare, slow push-in.
- Shot 3, 8–13s: 35mm over-the-shoulder shot from behind a blurred helmeted rider onto the old man.
- Shot 4, 13–15s: 85mm extreme close-up of the old man's eyes under the helmet brim, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam walks out alone through the sliding glass doors of the tower onto the pavement, pith helmet on and hands empty, shades his eyes from a wall of white headlight glare and is already speaking calmly in a husky voice.
- 1–2s (Shot 1): @Lam keeps talking, squinting into the glare with an amused twist of the mouth.
- 2–3s (Shot 1): @Lam lowers his hand and goes on, counting the headlights with a slow sweep of one finger.
- 3–4s (Shot 1): @Lam keeps speaking calmly, eyebrows raised, the white light bleaching one side of his face.
- 4–5s (CUT to Shot 2): @Lam holds up both empty palms in close-up as he goes on, unbothered.
- 5–6s (Shot 2): @Lam keeps talking with a dry little chuckle.
- 6–7s (Shot 2): @Lam shakes his head as he mentions the fuel, still speaking easily.
- 7–8s (Shot 2): @Lam keeps speaking in close-up, one eyebrow cocked.
- 8–9s (CUT to Shot 3): @Lam keeps talking into the glare, while the blurred helmet and handlebars of a debt collector rev in the foreground.
- 9–10s (Shot 3): @Lam tilts his head and starts his last question slowly, a sly glint in his eyes.
- 10–11s (Shot 3): @Lam keeps talking, glancing past the riders toward both ends of the dark street.
- 11–12s (Shot 3): @Lam keeps speaking, the corner of his mouth lifting.
- 12–13s (Shot 3): @Lam finishes and closes his mouth.
- 13–14s (CUT to Shot 4): @Lam slowly lifts the brim of his battered green pith helmet with one finger, mouth closed.
- 14–15s (Shot 4): @Lam's calm narrow eyes hold steady in the white light, mouth closed, as the engines settle into an idle. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, amused and unbothered), in Vietnamese with exact lip-sync, said exactly once: "Này, các cậu tắt bớt đèn đi, chói hết cả mắt. Hai chục cậu, hai chục cái xe, chỉ để chặn một ông già tay không à? Tốn xăng quá, xăng bây giờ đắt lắm đấy. Ai bảo các cậu là tôi đến đây một mình?" (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a chorus of revving motorbike engines, horns blaring, glass doors sliding apart, engines settling into an idle. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 2 (`canh-22/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on the wide street in front of the glass tower: neon reflections on the asphalt, tall trees, parked motorbikes, warm streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
- Extra: dozens of cyclos pedaled by old drivers in conical hats rolling in from both ends of the street, and old-quarter shopkeepers and motorbike-taxi drivers lining the far sidewalks in silence
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium tracking shot alongside the gadget man in the front seat of a cyclo.
- Shot 2, 4–8s: 85mm close-up of the gadget man, tracking.
- Shot 3, 8–12s: 50mm medium shot of the gadget man in the stopped cyclo, cyclos lining up behind him.
- Shot 4, 12–15s: 24mm high wide shot of the street lined with cyclos and silent neighbors, slow crane-up.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khoa rides in the front seat of a cyclo pedaled by an old driver, magnifier glasses on his forehead, and is already speaking, calling out in a dry nasal voice toward screen-left.
- 1–2s (Shot 1): @Khoa keeps talking with a deadpan smirk, one hand raised like a tour guide.
- 2–3s (Shot 1): @Khoa jerks a thumb back over his shoulder as he goes on, the cyclo rolling smoothly.
- 3–4s (Shot 1): @Khoa keeps speaking flatly, while behind him more cyclos roll in side by side, their bells tinkling.
- 4–5s (CUT to Shot 2): @Khoa keeps talking in close-up, one eyebrow raised, his long grey ponytail swaying.
- 5–6s (Shot 2): @Khoa wags a bony finger as he goes on, deadpan.
- 6–7s (Shot 2): @Khoa mimes a phone at his ear, still talking flatly.
- 7–8s (Shot 2): @Khoa keeps speaking with the faintest smirk.
- 8–9s (CUT to Shot 3): @Khoa's cyclo glides to a stop at the curb and he keeps talking, while cyclos line up behind him.
- 9–10s (Shot 3): @Khoa spreads one hand toward the sidewalks as he goes on.
- 10–11s (Shot 3): @Khoa keeps talking, nodding at a shopkeeper stepping out of her shop.
- 11–12s (Shot 3): @Khoa finishes, closes his mouth and folds his arms in the cyclo seat.
- 12–13s (CUT to Shot 4): Shopkeepers in aprons and motorbike-taxi drivers in pith helmets step out and stand in silence along the far sidewalks.
- 13–14s (Shot 4): Long lines of cyclos fill both curbs under the streetlamps.
- 14–15s (Shot 4): @Khoa sits small among them with his arms folded, mouth closed, as the street falls into a deep hush. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, deadpan with a smirk), in Vietnamese with exact lip-sync, said exactly once: "Ông Lâm ơi, hàng xóm đến đủ cả rồi đây! Bà Hoa chỉ gọi một vòng, dọa nhà nào không ra thì từ mai cấm bén mảng đến quán bún chả. Thế là cả phố dắt nhau ra hết, đến bà bán xôi cũng bỏ hàng." (no subtitles)
- @Khoa starts talking within the first second; whenever @Khoa speaks, the face and lips are clearly visible in that shot; after the last word @Khoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: dozens of cyclo bells tinkling, bicycle chains clicking, shop doors creaking open, shuffling sandals, then a deep hush over idling engines. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 3 (`canh-22/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on the wide street in front of the glass tower: neon reflections on the asphalt, tall trees, parked motorbikes, warm streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- Extra: a silent crowd of old-quarter neighbors standing far behind her, out of focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium tracking shot of the bún chả lady striding at the head of the crowd.
- Shot 2, 4–8s: 85mm close-up of the bún chả lady, locked off.
- Shot 3, 8–12s: 40mm medium shot of the bún chả lady at the curb with the crowd soft behind her, slow push-in.
- Shot 4, 12–15s: 85mm extreme close-up of her sharp eyes over the bamboo fan, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaHoa strides along the neon-lit sidewalk at the head of a silent crowd, waving a woven bamboo hand fan, and is already speaking fast toward screen-right in a brassy scolding voice.
- 1–2s (Shot 1): @BaHoa keeps talking, fanning in lazy strokes, gold hoop earrings swinging.
- 2–3s (Shot 1): @BaHoa wrinkles her nose at the distant ring of motorbikes and goes on in a sing-song.
- 3–4s (Shot 1): @BaHoa keeps scolding as she reaches the curb and plants one hand on her hip.
- 4–5s (CUT to Shot 2): @BaHoa keeps talking in close-up, eyebrows arched, red lips moving fast.
- 5–6s (Shot 2): @BaHoa sniffs the air theatrically as she goes on.
- 6–7s (Shot 2): @BaHoa tilts her head and asks her question in a mock-sweet tone.
- 7–8s (Shot 2): @BaHoa taps the folded fan against her palm as she keeps talking.
- 8–9s (CUT to Shot 3): @BaHoa points the fan down the street toward home and keeps scolding, the silent crowd standing far behind her out of focus.
- 9–10s (Shot 3): @BaHoa raises one finger, ready to count, still talking fast.
- 10–11s (Shot 3): @BaHoa keeps talking, her chunky gold bangle glinting as she lifts the fan.
- 11–12s (Shot 3): @BaHoa calls out the first count and closes her mouth, one finger held high.
- 12–13s (CUT to Shot 4): @BaHoa's sharp eyes narrow over the edge of the bamboo fan, mouth closed.
- 13–14s (Shot 4): @BaHoa's eyes flick from rider to rider over the fan, mouth closed.
- 14–15s (Shot 4): @BaHoa fans herself slowly with a closed-mouth smirk. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.3s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking quickly in short lively phrases, every word still clear, brassy mock-scolding), in Vietnamese with exact lip-sync, said exactly once: "Ối giời ơi, trông các cháu kìa, mặt đỏ như mẻ chả sắp cháy! Đứng thêm tí nữa là khét cả lũ. Mẹ ở nhà có biết con mình đi làm cái nghề này không? Tắt máy, quay xe về nhà ăn cơm đi, bà đếm đến ba thôi đấy nhé. Một!" (no subtitles)
- @BaHoa starts talking within the first second; whenever @BaHoa speaks, the face and lips are clearly visible in that shot; after the last word @BaHoa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft flap of a bamboo hand fan, heeled sandals clicking, idling engines sputtering, a hush over the street. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 4 (`canh-22/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on the wide street in front of the glass tower: neon reflections on the asphalt, tall trees, parked motorbikes, warm streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- Extra: young debt collectors walking their motorbikes backward behind him and slipping away
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the heavyset collector in the middle of the street, handheld.
- Shot 2, 3–7s: 85mm close-up of the heavyset collector looking over his shoulder, handheld.
- Shot 3, 7–12s: 50mm medium shot of the heavyset collector with the collectors slipping away behind him, slow push-in.
- Shot 4, 12–15s: 24mm wide shot of the emptied street under a streetlamp, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Beo stands in the middle of the wide street in front of the glass tower, turning his shaved head toward the riders behind him, and is already shouting fast.
- 1–2s (Shot 1): @Beo keeps shouting over his shoulder, both arms spread wide.
- 2–3s (Shot 1): @Beo stamps a flip-flop and keeps calling out, gold front tooth flashing.
- 3–4s (CUT to Shot 2): @Beo keeps talking fast in close-up, eyes darting, sweat shining on his shaved head.
- 4–5s (Shot 2): @Beo holds up one thick finger as he goes on, voice rising.
- 5–6s (Shot 2): @Beo keeps shouting, glancing sideways toward the sidewalk.
- 6–7s (Shot 2): @Beo's voice turns whiny as he keeps calling out, eyebrows pinched.
- 7–8s (CUT to Shot 3): @Beo keeps whining over his shoulder, while behind him the young debt collectors quietly walk their motorbikes backward.
- 8–9s (Shot 3): @Beo reaches one hand out after them, still talking, as they turn and slip away into the dark side streets.
- 9–10s (Shot 3): @Beo keeps pleading fast, hopping from one flip-flop to the other.
- 10–11s (Shot 3): @Beo hugs his own arms and keeps whining, glancing back toward the sidewalk.
- 11–12s (Shot 3): @Beo finishes and closes his mouth, one hand still outstretched.
- 12–13s (CUT to Shot 4): @Beo stands alone in the emptied street under a streetlamp, his cheap fake-gold chain glinting on his black tank top.
- 13–14s (Shot 4): @Beo lowers his hand slowly and swallows hard, mouth closed.
- 14–15s (Shot 4): @Beo shifts on his flip-flops in the empty glare, a lone cricket chirping at the curb. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.3s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, blustering, then whining), in Vietnamese with exact lip-sync, said exactly once: "Ê, chúng mày dắt xe đi đâu thế? Đứng lại! Sếp dặn chặn cổng cơ mà! Bà ấy mới đếm được có một, mà đã chạy sạch rồi! Thôi chết, đợi anh với, đừng bỏ anh đứng trơ trọi giữa đường thế này! Anh cũng sợ bà ấy chết khiếp đây này!" (no subtitles)
- @Beo starts talking within the first second; whenever @Beo speaks, the face and lips are clearly visible in that shot; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: motorbike engines cutting off one by one, tires rolling softly backward, footsteps fading, a lonely cricket chirping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 1 (`canh-23/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A dim underground car park with concrete pillars and fluorescent strip lights, a low red sports car with no badge.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium tracking shot following the livestreamer between the pillars.
- Shot 2, 3–7s: 85mm close-up of the livestreamer at the open car door, handheld.
- Shot 3, 7–12s: 50mm medium shot of the livestreamer in the low driver's seat lit by the dashboard.
- Shot 4, 12–15s: 24mm low wide shot as the red sports car swings out toward the exit ramp.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung runs in between the concrete pillars of the dim car park, clutching his phone with a glowing blank screen, and is already muttering fast to himself with a manic grin.
- 1–2s (Shot 1): @Hung keeps talking as he jogs toward a low red sports car with no badge, glancing back over his shoulder.
- 2–3s (Shot 1): @Hung keeps muttering fast, fishing a key fob out of his bomber jacket.
- 3–4s (CUT to Shot 2): @Hung flings the car door open, still talking to himself.
- 4–5s (Shot 2): @Hung leans on the open door in close-up and keeps gloating, eyebrows bouncing.
- 5–6s (Shot 2): @Hung scoffs with a laugh and goes on, flicking his ash-blond fringe.
- 6–7s (Shot 2): @Hung keeps talking, miming a tiny scooter with two fingers.
- 7–8s (CUT to Shot 3): @Hung drops into the low driver's seat, still talking, his face lit by the dashboard glow.
- 8–9s (Shot 3): @Hung keeps talking as the headlights snap on, both hands on the steering wheel.
- 9–10s (Shot 3): @Hung revs the engine and keeps gloating to himself, tapping the wheel with his silver rings.
- 10–11s (Shot 3): @Hung keeps muttering, grinning at himself in the rear-view mirror.
- 11–12s (Shot 3): @Hung finishes with a smug laugh, closes his mouth and pulls the door shut.
- 12–13s (CUT to Shot 4): The low red sports car swings out of its bay toward the exit ramp.
- 13–14s (Shot 4): The car's red taillights streak past the concrete pillars.
- 14–15s (Shot 4): The car disappears up the exit ramp, leaving the empty car park flickering under fluorescent light. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.1s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, manic, gloating to himself), in Vietnamese with exact lip-sync, said exactly once: "Cổng trước bị chặn thì tao ra cửa sau, khó gì đâu. Cái xe máy cũ mèm của lão mà đòi đuổi kịp con này à? Mơ đi nhé! Đạp ga một cái là bay. Mười phút nữa là tao lên cao tốc rồi, để xem thằng nào bắt được tao." (no subtitles)
- @Hung starts talking within the first second; whenever @Hung speaks, the face and lips are clearly visible in that shot; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: hurried sneaker footsteps on concrete, a car door thudding shut, a high-pitched engine roar, tires squealing. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 2 (`canh-23/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Evening rush hour on a wide Hà Nội avenue: a dense river of motorbikes and cars, red taillights, neon and streetlamps, trees along the sidewalks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- Extra: an old woman in a conical hat on a scooter loaded with a tall tower of potted flowers, and evening commuters on motorbikes in helmets and face masks streaming around the car
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot through the windshield of the livestreamer at the wheel, locked off.
- Shot 2, 5–8s: 35mm over-the-shoulder shot from behind the old flower seller onto the livestreamer in the car.
- Shot 3, 8–13s: 85mm close-up of the livestreamer through the side window, locked off.
- Shot 4, 13–15s: 28mm high wide shot of the sea of motorbikes flowing around the stranded red car.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Through the windshield of the low red sports car stuck in traffic, @Hung grips the steering wheel, presses the horn again and again and is already speaking fast, ranting at the traffic.
- 1–2s (Shot 1): @Hung keeps ranting, both hands flung up off the wheel.
- 2–3s (Shot 1): @Hung shakes one sore hand and keeps complaining fast.
- 3–4s (Shot 1): @Hung points at the dashboard as he goes on, gold-rimmed glasses fogging.
- 4–5s (Shot 1): @Hung inches the car forward a hand's width and keeps talking fast.
- 5–6s (CUT to Shot 2): An old woman in a conical hat on a scooter loaded with a tall tower of potted flowers pulls up beside his side window, as @Hung keeps ranting at the traffic.
- 6–7s (Shot 2): @Hung turns his head to stare at her, still talking fast in disbelief.
- 7–8s (Shot 2): The old woman putters past at an easy pace and gives one cheerful honk, while @Hung points after her and keeps ranting.
- 8–9s (CUT to Shot 3): @Hung keeps complaining in close-up, eyes bulging behind his fogged glasses.
- 9–10s (Shot 3): @Hung leans on the horn once more and keeps ranting, voice cracking.
- 10–11s (Shot 3): @Hung keeps talking fast, flapping one hand at the endless taillights.
- 11–12s (Shot 3): @Hung finishes his rant with a groan and closes his mouth.
- 12–13s (Shot 3): @Hung drops his forehead onto the steering wheel, mouth closed.
- 13–14s (CUT to Shot 4): The sea of motorbikes flows on around the stranded red car under the neon.
- 14–15s (Shot 4): The flower scooter disappears into the river of taillights ahead, the red car still not moving. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.3s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, exasperated, ranting at traffic), in Vietnamese with exact lip-sync, said exactly once: "Nhích lên đi chứ! Còi tao bấm đến mỏi tay rồi đấy! Con xe này chạy hai trăm cây số một giờ, thế mà giờ đi từng mét một. Trời đất, đến bà cụ chở chậu hoa cũng vượt mặt tao, lại còn quay sang bấm còi chào nữa chứ! Nhục thật!" (no subtitles)
- @Hung starts talking within the first second; whenever @Hung speaks, the face and lips are clearly visible in that shot; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a sea of beeping scooter horns, idling engines, a sports car engine revving uselessly, one long comic honk. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 3 (`canh-23/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Evening rush hour on a wide Hà Nội avenue: a dense river of motorbikes and cars, red taillights, neon and streetlamps, trees along the sidewalks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: evening commuters on motorbikes stalled around him, faces hidden by helmets and face masks
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium tracking shot alongside the old man on his motorbike.
- Shot 2, 4–8s: 85mm close-up of the old man riding, tracking.
- Shot 3, 8–13s: 50mm medium shot from the front, tracking backward ahead of the old man.
- Shot 4, 13–15s: 24mm wide shot past the old man's shoulder toward the red sports car far ahead.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam rides the old cream-colored step-through motorbike with a round chrome headlamp into a narrow gap in the jammed avenue, pith helmet low, and is already talking to the motorbike with a fond grin.
- 1–2s (Shot 1): @Lam keeps murmuring to the bike, patting its handlebar.
- 2–3s (Shot 1): @Lam tilts the motorbike gently between two cars, still talking softly.
- 3–4s (Shot 1): @Lam nods politely to a helmeted commuter he slips past and keeps talking.
- 4–5s (CUT to Shot 2): @Lam keeps talking in close-up, tucking one elbow in as his mirror slides past a car's mirror with a finger's width to spare.
- 5–6s (Shot 2): @Lam gives a polite tap of his little horn and goes on fondly.
- 6–7s (Shot 2): @Lam keeps talking as he slips between the lanes like a fish through reeds.
- 7–8s (Shot 2): @Lam grins wider as he goes on, steady hands on the grips.
- 8–9s (CUT to Shot 3): @Lam keeps murmuring, half closing his eyes for a moment with a sly smile.
- 9–10s (Shot 3): @Lam keeps talking fondly, weaving smoothly around a stalled scooter.
- 10–11s (Shot 3): @Lam's eyes lift toward the far end of the avenue as he keeps talking.
- 11–12s (Shot 3): @Lam keeps speaking, the last words low and amused.
- 12–13s (Shot 3): @Lam finishes with a quiet chuckle and closes his mouth.
- 13–14s (CUT to Shot 4): Far ahead, the low red sports car with no badge glows under the streetlamps, stuck in the jam.
- 14–15s (Shot 4): @Lam rolls forward toward it, his round chrome headlamp cutting through the jam, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, relaxed, fond, murmuring to the bike), in Vietnamese with exact lip-sync, said exactly once: "Nào, ngựa sắt. Lách nhẹ thôi, khe này vừa đủ. Cho tôi nhờ tí nhé. Đừng quẹt gương nhà người ta đấy. Cả đời chở khách rồi, ngõ ngách nào mình chả thuộc. Đường này nhắm mắt cũng đi được. Thằng nhóc ấy chạy đằng trời." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: an old engine puttering steadily, a cheerful little horn beep, a sea of idling engines and horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 4 (`canh-23/clip-4.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Evening rush hour on a wide Hà Nội avenue: a dense river of motorbikes and cars, red taillights, neon and streetlamps, trees along the sidewalks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the livestreamer scrambling out of the red car, handheld.
- Shot 2, 3–5s: 85mm close-up of the livestreamer, handheld.
- Shot 3, 5–8s: 40mm medium two-shot along the curb, the old man on his motorbike on the left and the livestreamer sprinting away on the right.
- Shot 4, 8–12s: 85mm close-up of the old man astride his motorbike, locked off.
- Shot 5, 12–15s: 50mm medium side shot of the old man with the distant steel bridge beyond, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung flings open the door of the low red sports car stranded at the curb, scrambles out clutching his glowing phone and is already speaking fast to himself in gasps.
- 1–2s (Shot 1): @Hung keeps talking frantically, looking up and down the jammed avenue.
- 2–3s (Shot 1): @Hung points toward the distant steel bridge, still gasping out words.
- 3–4s (CUT to Shot 2): @Hung keeps talking fast in close-up, sweat on his temple, hopping on the spot.
- 4–5s (Shot 2): @Hung blurts his last words, closes his mouth and turns to run.
- 5–6s (CUT to Shot 3): @Hung sprints away along the tree-lined sidewalk, while on screen-left @Lam, idling on the old cream-colored step-through motorbike, watches him go and starts speaking to himself with a dry chuckle.
- 6–7s (Shot 3): @Lam keeps talking half to himself, thick grey eyebrows raised, slowly shaking his head.
- 7–8s (Shot 3): @Lam goes on with a small amused snort, eyes following the runner.
- 8–9s (CUT to Shot 4): @Lam keeps talking in close-up, leaning on the handlebars.
- 9–10s (Shot 4): @Lam keeps speaking, a dry smile spreading.
- 10–11s (Shot 4): @Lam taps the fuel tank of the old motorbike fondly as he goes on.
- 11–12s (Shot 4): @Lam keeps talking, eyes on the tiny running figure heading for the bridge.
- 12–13s (CUT to Shot 5): @Lam says the last words with a dry chuckle and closes his mouth.
- 13–14s (Shot 5): @Lam tugs the strap of his battered green pith helmet tight, mouth closed.
- 14–15s (Shot 5): @Lam twists the throttle with a small sly grin, the old engine revving. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, frantic, gasping to himself): "Thôi, bỏ xe ở đây! Kệ nó! Chạy bộ lên cầu, sang được bên kia sông là thoát. Chân ơi, nhanh lên nào!"
- Turn 2, 5.7–12.9s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, dry chuckle, half to himself): "Bỏ cả siêu xe mà chạy bộ lên cầu à? Cái cầu ấy, hồi trẻ ông phóng qua còn nhiều hơn cậu đi thang máy. Cứ chạy đi."
- Pacing: @Hung speaks quickly, then @Lam answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: an old engine puttering, a car door swinging open, sneakers pounding the pavement, distant horns, the motorbike revving. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 1 (`canh-24/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on a century-old steel truss railway bridge over a wide dark river: rusty iron lattice beams lit by sparse lamps, a narrow motorbike lane beside the tracks, city lights on the far bank.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium tracking shot of the livestreamer running along the motorbike lane.
- Shot 2, 3–7s: 85mm close-up of the livestreamer, handheld.
- Shot 3, 7–12s: 50mm medium shot of the livestreamer turning between the iron beams, locked off.
- Shot 4, 12–15s: 24mm high wide shot of the lone figure on the vast bridge, slow crane-up.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung runs along the narrow motorbike lane of the century-old steel bridge, panting, his phone with a glowing blank screen held up to his mouth, and is already shouting fast into it.
- 1–2s (Shot 1): @Hung keeps shouting into the phone as he runs, satin bomber jacket flapping.
- 2–3s (Shot 1): @Hung jabs the screen with his thumb and keeps talking, panting hard.
- 3–4s (CUT to Shot 2): @Hung slows down mid-span in close-up, still talking frantically into the phone.
- 4–5s (Shot 2): @Hung keeps shouting, shaking the phone as if it were broken.
- 5–6s (Shot 2): @Hung skids to a halt and keeps talking, staring ahead as blue and red lights flash far away at the end of the bridge, no figures visible there.
- 6–7s (Shot 2): @Hung's eyes widen behind his gold-rimmed glasses as he goes on, voice cracking.
- 7–8s (CUT to Shot 3): @Hung glances back over his shoulder, still talking fast.
- 8–9s (Shot 3): @Hung keeps talking in a ragged voice, looking from one end of the bridge to the other.
- 9–10s (Shot 3): @Hung turns in a half circle between the iron beams, still talking.
- 10–11s (Shot 3): @Hung asks his last frantic question into the phone, voice breaking.
- 11–12s (Shot 3): @Hung finishes, closes his mouth and lowers the phone, chest heaving.
- 12–13s (CUT to Shot 4): @Hung stands alone in the middle of the vast lamp-lit bridge, the river glittering far below.
- 13–14s (Shot 4): Blue and red lights flash at the far end of the bridge, no figures visible there.
- 14–15s (Shot 4): @Hung spins around toward the way he came, mouth closed, the wind tugging at his ash-blond hair. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.5s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, panting and frantic), in Vietnamese with exact lip-sync, said exactly once: "Béo! Nghe máy đi chứ! Gọi hết bọn nó ra cầu đón tao, ngay bây giờ! Mày trốn đâu rồi? Lại tắt máy à? Chết, phía trước đèn xanh đỏ chặn kín cả lối rồi. Sau lưng thì lão ấy đang tới gần. Giờ tao chạy đường nào đây, trời ơi là trời?" (no subtitles)
- @Hung starts talking within the first second; whenever @Hung speaks, the face and lips are clearly visible in that shot; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind whistling through iron girders, the river lapping far below, sneakers pounding on iron plates, a phone ringing out unanswered, a distant police siren whooping softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 2 (`canh-24/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on a century-old steel truss railway bridge over a wide dark river: rusty iron lattice beams lit by sparse lamps, a narrow motorbike lane beside the tracks, city lights on the far bank.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium two-shot along the motorbike lane, slow push-in.
- Shot 2, 3–7s: 85mm close-up of the livestreamer, handheld.
- Shot 3, 7–10s: 40mm medium two-shot along the motorbike lane, locked off.
- Shot 4, 10–15s: 85mm close-up of the old man under the bridge lamp, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung on screen-right spins around on the bridge's motorbike lane as @Lam rolls to a stop on screen-left on the old cream-colored step-through motorbike, and @Hung is already shouting at him fast.
- 1–2s (Shot 1): @Hung keeps shouting, jabbing a ringed finger toward @Lam, who sits still, mouth closed.
- 2–3s (Shot 1): @Hung keeps shouting, ash-blond hair wind-tossed, glasses askew.
- 3–4s (CUT to Shot 2): @Hung keeps shouting spitefully in close-up, chest heaving.
- 4–5s (Shot 2): @Hung sneers as he goes on, voice cracking on the old nickname.
- 5–6s (Shot 2): @Hung keeps sneering, spitting out the insult fast.
- 6–7s (Shot 2): @Hung finishes and closes his mouth, panting.
- 7–8s (CUT to Shot 3): @Lam sets the motorbike on its side stand and starts answering slowly in a dry husky voice.
- 8–9s (Shot 3): @Lam swings one leg off the motorbike and keeps speaking quietly, eyes on @Hung.
- 9–10s (Shot 3): @Lam stands beside the bike and goes on, dry and cutting, while @Hung stands rigid, mouth closed.
- 10–11s (CUT to Shot 4): @Lam keeps speaking slowly in close-up, a faint dry smile under the bridge lamp.
- 11–12s (Shot 4): @Lam tilts his head and goes on, unhurried.
- 12–13s (Shot 4): @Lam keeps talking, nodding toward screen-right.
- 13–14s (Shot 4): @Lam says his last words and closes his mouth, lifting the battered green pith helmet off his grey crew cut.
- 14–15s (Shot 4): @Lam holds the helmet at his side, calm narrow eyes fixed toward screen-right, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.7s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, shouting, cornered and spiteful): "Ông nghĩ ông là ai mà dám chơi tôi? Bố tôi kể ông từng là Lâm Rồng gì đấy, nhưng giờ ông chỉ là lão già xe ôm hết thời!"
- Turn 2, 7.2–13.5s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, dry and cutting): "Hết thời thì cậu chạy làm gì cho mệt, cậu Hưng? Đứng lại thở một tí đã, kẻo đứt hơi giữa cầu."
- Pacing: @Hung speaks quickly, then @Lam answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: an old engine puttering to a stop, the metal clack of a side stand, wind howling through iron girders, ragged breathing. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 3 (`canh-24/clip-3.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 85mm close-up of the old man under the bridge lamp, holding the previous framing.
- Shot 2, 3–6s: 28mm low-angle medium shot of the old man rolling up his sleeve, slow tilt-up.
- Shot 3, 6–8s: 85mm low-angle close-up of the old man's face, locked off.
- Shot 4, 8–12s: 50mm over-the-shoulder shot from behind the old man onto the livestreamer.
- Shot 5, 12–15s: 35mm medium two-shot along the iron lattice, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam tucks the pith helmet under his left arm, looks steadily toward screen-right and is already speaking slowly in a calm husky voice.
- 1–2s (Shot 1): @Lam keeps speaking low and heavy, the bridge lamp haloing his grey crew cut.
- 2–3s (Shot 1): @Lam keeps talking, his narrow eyes fixed toward screen-right.
- 3–4s (CUT to Shot 2): @Lam rolls up his right sleeve fold by fold as he keeps speaking slowly, and a coiled dark-green dragon tattoo appears on his weathered forearm under the bridge lamp.
- 4–5s (Shot 2): @Lam raises the tattooed forearm a little and keeps talking, one weathered finger resting on the dragon.
- 5–6s (Shot 2): @Lam takes one small step forward as he goes on, unhurried.
- 6–7s (CUT to Shot 3): @Lam keeps speaking in close-up, the words slow and heavy, wind tugging at his windbreaker.
- 7–8s (Shot 3): @Lam lands the last words slowly, his calm narrow eyes unblinking, then closes his mouth.
- 8–9s (CUT to Shot 4): @Hung holds up his glowing phone like a shield and starts talking back fast in a shaking voice.
- 9–10s (Shot 4): @Hung keeps talking fast, the phone trembling in his raised hand.
- 10–11s (Shot 4): @Hung's voice climbs higher as he goes on, knuckles white around the phone.
- 11–12s (Shot 4): @Hung keeps blustering, shuffling half a step back on the iron plates.
- 12–13s (CUT to Shot 5): @Hung finishes and closes his mouth, lips pressed tight.
- 13–14s (Shot 5): @Hung takes a shaky step back along the narrow walkway, mouth closed.
- 14–15s (Shot 5): @Lam gives one slow closed-mouth nod, while @Hung stands stiffly on the narrow walkway beside the rusty iron lattice. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.6s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, low, heavy and calm): "Bố cậu chưa kể hết à? Thế thì để tôi nói nốt. Ba mươi năm trước, phố cổ này là của Rồng, giờ vẫn thế."
- Turn 2, 8.1–12.9s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, shrill bluster, voice shaking): "Ông định làm gì thế hả? Đứng yên đấy! Tôi vẫn đang quay, ông mà động vào tôi là cả mạng thấy hết!"
- Pacing: @Lam speaks slowly and calmly, then @Hung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft rustle of a rolled sleeve, wind whistling through the iron lattice, the deep rumble of the river, distant sirens drawing closer. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 4 (`canh-24/clip-4.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on a century-old steel truss railway bridge over a wide dark river: rusty iron lattice beams lit by sparse lamps, a narrow motorbike lane beside the tracks, city lights on the far bank.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium two-shot along the iron lattice, holding the previous framing.
- Shot 2, 3–6s: 85mm close-up of the livestreamer leaning over the iron lattice, handheld.
- Shot 3, 6–10s: 50mm over-the-shoulder shot from behind the livestreamer onto the old man.
- Shot 4, 10–13s: 85mm close-up of the old man, locked off.
- Shot 5, 13–15s: 35mm medium two-shot on the bridge walkway, slow crane-up pull-back.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung stands stiffly on the narrow walkway beside the rusty iron lattice and is already shouting fast toward @Lam, the phone trembling in his raised hand, while @Lam stands still a few steps away on screen-left.
- 1–2s (Shot 1): The phone slips from @Hung's trembling fingers and slips through a gap in the iron lattice, its blank screen still glowing, and he keeps shouting after it.
- 2–3s (Shot 1): @Hung grips the iron lattice with both hands, staring after it, and keeps crying out as the glowing phone tumbles toward the black river.
- 3–4s (CUT to Shot 2): @Hung keeps wailing in close-up, staring down at the water, eyes wide.
- 4–5s (Shot 2): @Hung keeps talking in a breaking voice, both hands still on the lattice.
- 5–6s (Shot 2): @Hung finishes the wail and closes his mouth, still staring down.
- 6–7s (CUT to Shot 3): @Lam starts speaking slowly and softly from a few steps away, his empty hand open at his side.
- 7–8s (Shot 3): @Lam keeps speaking gently, the helmet hanging from his other hand.
- 8–9s (Shot 3): @Lam shakes his head slightly as he goes on, calm and final.
- 9–10s (Shot 3): @Lam keeps talking softly, glancing toward the dark river beyond the lattice.
- 10–11s (CUT to Shot 4): @Lam keeps speaking in close-up, a small weary smile in his narrow eyes.
- 11–12s (Shot 4): @Lam keeps talking slowly, the bridge lamp warm on his grey crew cut.
- 12–13s (Shot 4): @Lam says the last words softly.
- 13–14s (CUT to Shot 5): @Lam closes his mouth, while @Hung sags down onto his heels on the walkway with lips pressed shut.
- 14–15s (Shot 5): The camera rises as ripples spread on the black river far below, two small figures on the vast lamp-lit iron bridge. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking quickly in short lively phrases, every word still clear, sharp wail, panicky): "Đừng có lại gần tôi! Ơ, chết! Điện thoại! Điện thoại của tôi! Cả cơ nghiệp nằm hết trong cái máy ấy đấy, trời ơi!"
- Turn 2, 6.2–13.1s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft and final): "Tôi có chạm vào cậu đâu, nó tự rơi đấy chứ. Mà rơi thì thôi, năm triệu người xem hết cả rồi, cậu ạ."
- Pacing: @Hung speaks quickly, then @Lam answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a sharp gasp, the clatter of a gimbal on iron, a faint distant splash, wind and rushing water. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 1 (`canh-25/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night on a century-old steel truss railway bridge over a wide dark river: rusty iron lattice beams lit by sparse lamps, a narrow motorbike lane beside the tracks, city lights on the far bank.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hưng, 31, flashy boss of a loan app company and a show-off livestreamer; tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin; oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers, several silver rings, a phone on a small selfie gimbal.
- Extra: two police officers in green uniforms walking up calmly and stopping a few steps away
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium shot of the livestreamer on the bridge walkway as two officers walk up calmly, washed in blue and red light.
- Shot 2, 3–8s: 85mm close-up of the livestreamer, slow push-in.
- Shot 3, 8–12s: 50mm over-the-shoulder shot from behind an officer onto the livestreamer.
- Shot 4, 12–15s: 24mm high wide shot of the bridge span, slow crane-up.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung stands alone on the bridge walkway on screen-right with empty hands as two police officers in green uniforms walk up calmly from screen-left, and he is already speaking in a hollow, drained voice.
- 1–2s (Shot 1): The officers stop a few steps away without coming closer, while @Hung keeps talking quietly.
- 2–3s (Shot 1): @Hung slowly raises both his own hands as he goes on, ringed fingers trembling.
- 3–4s (CUT to Shot 2): @Hung keeps speaking barely above a murmur in close-up, face drained pale, eyes glistening.
- 4–5s (Shot 2): @Hung's knees sag a little as he keeps talking.
- 5–6s (Shot 2): @Hung glances toward the river below as he goes on.
- 6–7s (Shot 2): @Hung keeps talking hollowly, a crooked bitter smile flickering.
- 7–8s (Shot 2): @Hung keeps speaking in a flat murmur, eyes on the dark water.
- 8–9s (CUT to Shot 3): @Hung offers both hands out in front of him and keeps speaking quietly, while an officer stands still a few steps away.
- 9–10s (Shot 3): @Hung keeps murmuring, gold-rimmed glasses sliding down his nose.
- 10–11s (Shot 3): @Hung gives a short hollow laugh as he goes on.
- 11–12s (Shot 3): @Hung says the last words and closes his mouth.
- 12–13s (CUT to Shot 4): @Hung lowers his head, ash-blond hair falling over his glasses, mouth closed.
- 13–14s (Shot 4): The two officers wait calmly a few steps away, hands at their sides.
- 14–15s (Shot 4): @Hung stands small under the bridge lamp as the blue and red light keeps washing over him, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Hung (man of 31, loud slick nasal tenor of a livestream salesman, smug and showy, speaking at a natural, even conversational pace, hollow, drained, barely above a murmur), in Vietnamese with exact lip-sync, said exactly once: "Hai anh cứ đứng đấy, tôi tự giơ tay đây. Không chạy nữa đâu, chân cũng rã rời hết rồi. Máy cũng rơi xuống sông mất rồi. Cả đời tôi chỉ sống để khoe, giờ đến cái để khoe cũng chẳng còn. Buồn cười thật đấy." (no subtitles)
- @Hung starts talking within the first second; whenever @Hung speaks, the face and lips are clearly visible in that shot; after the last word @Hung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: calm footsteps on iron plates, a police radio crackling softly, wind through the girders, the river below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 2 (`canh-25/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Night in the loan app call center high in the glass tower: rows of desks with glowing monitors, magenta and gold neon accent lights without letters, city lights beyond the windows, a ring light glowing in the glass-walled boss room.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Beo = Béo, 28, Hưng's heavyset debt-collector leader; big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, gold front tooth; black tank top, camouflage shorts, flip-flops, a cheap fake-gold chain.
- Extra: a police officer in a green uniform standing calmly a few steps away with hands behind his back
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the heavyset collector slumped on the floor between the desks.
- Shot 2, 3–7s: 35mm over-the-shoulder shot from behind the standing officer onto the heavyset collector.
- Shot 3, 7–12s: 85mm close-up of the heavyset collector's wet eyes, locked off.
- Shot 4, 12–15s: 28mm wide shot of the officer and the slumped collector among the empty desks.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Beo sits slumped on the floor between the desks of the deserted call center, hugging a phone with a glowing blank screen to his chest, and is already speaking fast, blubbering up at a police officer standing a few steps away.
- 1–2s (Shot 1): @Beo keeps talking, lower lip wobbling, big wet eyes looking up.
- 2–3s (Shot 1): @Beo keeps pleading, hugging the phone tighter to his chest.
- 3–4s (CUT to Shot 2): @Beo keeps blubbering up at the officer, who stands calmly with hands behind his back.
- 4–5s (Shot 2): @Beo taps his own phone screen as he goes on, sniffling.
- 5–6s (Shot 2): @Beo keeps talking fast, shaking his head miserably.
- 6–7s (Shot 2): @Beo turns out the empty pockets of his camouflage shorts as he goes on.
- 7–8s (CUT to Shot 3): @Beo keeps pleading in close-up, palms pressed together, tears welling.
- 8–9s (Shot 3): @Beo's voice wobbles higher as he goes on.
- 9–10s (Shot 3): @Beo keeps blubbering fast, wiping his nose with the back of his wrist.
- 10–11s (Shot 3): @Beo keeps talking, chin trembling, eyes fixed on the officer.
- 11–12s (Shot 3): @Beo finishes and closes his mouth, sniffling.
- 12–13s (CUT to Shot 4): @Beo wipes his eyes with his wrist, heavy shoulders sagging under the pulsing magenta neon, mouth closed.
- 13–14s (Shot 4): The police officer in a green uniform looks down at him without a word, hands still behind his back.
- 14–15s (Shot 4): @Beo's cheap fake-gold chain glints as he hugs his knees, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.3s, spoken on camera by @Beo (man of 28, booming rough bass, blustering and a little hoarse from shouting, speaking quickly in short lively phrases, every word still clear, blubbering and sniffling), in Vietnamese with exact lip-sync, said exactly once: "Anh công an ơi, em chỉ đi đòi thuê thôi mà! Nói ra anh không tin, chứ em cũng đang nợ chính cái app ấy hai chục triệu, lãi mẹ đẻ lãi con. Lương còn chưa được trả. Em xin anh, cho em về với mẹ em, mẹ em đang đợi cơm!" (no subtitles)
- @Beo starts talking within the first second; whenever @Beo speaks, the face and lips are clearly visible in that shot; after the last word @Beo closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a loud sniffle, monitor hum, a police radio crackling softly, the whine of the air conditioner. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 3 (`canh-25/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A sunny university schoolyard in the morning with tall trees and old yellow buildings.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- Extra: a classmate in a white shirt sitting beside her on the bench seen from behind, and groups of students hugging under the trees in the soft-focus distance
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the granddaughter on the bench beside a classmate seen from behind.
- Shot 2, 4–8s: 85mm close-up of the granddaughter, locked off.
- Shot 3, 8–12s: 50mm over-the-shoulder shot from behind the classmate onto the granddaughter.
- Shot 4, 12–15s: 40mm medium shot of the granddaughter on the bench, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Mai sits on a wooden bench in the sunny schoolyard in her lavender hoodie, turns her phone with a glowing blank screen toward a classmate seen from behind, and is already speaking with a beaming smile.
- 1–2s (Shot 1): @Mai keeps talking, tapping the glowing screen, eyes shining.
- 2–3s (Shot 1): @Mai goes on, voice catching, a laugh bubbling up.
- 3–4s (Shot 1): @Mai keeps speaking, scrolling with her thumb.
- 4–5s (CUT to Shot 2): @Mai keeps speaking in close-up, eyes glistening behind her round glasses.
- 5–6s (Shot 2): @Mai nudges her glasses up and keeps talking, voice wobbling a little.
- 6–7s (Shot 2): @Mai shakes her head in disbelief as she goes on.
- 7–8s (Shot 2): @Mai keeps talking, a tear sliding down her cheek under the frame of her glasses.
- 8–9s (CUT to Shot 3): @Mai keeps speaking to her classmate, holding the phone up between them.
- 9–10s (Shot 3): @Mai keeps talking, while in the soft-focus distance groups of students wrap one another in silent hugs.
- 10–11s (Shot 3): @Mai laughs softly through her words as she goes on.
- 11–12s (Shot 3): @Mai says the last words and closes her mouth.
- 12–13s (CUT to Shot 4): @Mai lets out a long breath, mouth closed.
- 13–14s (Shot 4): @Mai presses the phone to her chest, a closed-mouth smile spreading across her face.
- 14–15s (Shot 4): Sunlit leaves sway over the bench as @Mai sits smiling in silence beside her classmate. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–11.9s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking at a natural, even conversational pace, teary and beaming), in Vietnamese with exact lip-sync, said exactly once: "Cậu xem này, Phú Quý bị khoá rồi! Nợ của cả nghìn người được xoá sạch. Ba tháng nay, sáng nào điện thoại tớ cũng réo, hôm nay không có lấy một cuộc gọi lạ. Toàn là tin nhắn cảm ơn thôi, đọc mãi không hết." (no subtitles)
- @Mai starts talking within the first second; whenever @Mai speaks, the face and lips are clearly visible in that shot; after the last word @Mai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong, rustling leaves, soft sniffles, a chorus of gentle message chimes. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 4 (`canh-25/clip-4.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Morning inside Lâm's narrow old-quarter tube house: a ground-floor room with the rolling steel shutter raised, a worn wooden table, a small family altar, sunlight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium two-shot at the worn wooden table, slow push-in.
- Shot 2, 3–7s: 85mm close-up of the granddaughter, locked off.
- Shot 3, 7–10s: 50mm over-the-shoulder shot from behind the granddaughter onto the old man.
- Shot 4, 10–13s: 85mm close-up of the old man at the table, locked off.
- Shot 5, 13–15s: 35mm medium two-shot at the table in the morning light, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Mai hops onto the stool on screen-left beside @Lam at the worn wooden table, holding up her phone with a glowing blank screen, and is already telling him the news fast with a beaming grin, while @Lam listens, mouth closed.
- 1–2s (Shot 1): @Mai keeps talking fast, bouncing on the stool.
- 2–3s (Shot 1): @Mai mimes signing an autograph in the air as she goes on.
- 3–4s (CUT to Shot 2): @Mai keeps talking proudly in close-up, eyes sparkling behind her round glasses.
- 4–5s (Shot 2): @Mai keeps talking fast, counting classmates on her fingers.
- 5–6s (Shot 2): @Mai leans in with a sly grin as she goes on.
- 6–7s (Shot 2): @Mai finishes, closes her mouth and nudges her glasses up.
- 7–8s (CUT to Shot 3): @Lam sets down his teacup and starts answering slowly in a dry husky voice.
- 8–9s (Shot 3): @Lam waves the compliment away with one hand and keeps speaking slowly.
- 9–10s (Shot 3): @Lam keeps talking, thick grey eyebrows lifting in mock dismay.
- 10–11s (CUT to Shot 4): @Lam wiggles his fingers in the air in close-up like a hen scratching the dirt as he goes on.
- 11–12s (Shot 4): @Lam keeps speaking modestly, shrugging one shoulder.
- 12–13s (Shot 4): @Lam goes on about the early market run, a smile tugging at his mouth.
- 13–14s (CUT to Shot 5): @Lam says the last words, closes his mouth and puts on his battered green pith helmet to hide a little smile.
- 14–15s (Shot 5): @Mai covers her grin with her hand, both silent in the morning light. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.5s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, bubbly and proud): "Ông ơi, cả lớp cháu bảo ông là ông nội ngầu nhất Hà Nội, bạn nào cũng đòi xin chữ ký! Cô chủ nhiệm cũng hỏi thăm ông đấy."
- Turn 2, 7.0–13.6s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, modest, waving it off): "Ngầu gì. Chữ ông như gà bới ấy. Sáng mai ông còn phải chở các cụ đi chợ sớm, ký với chả cọt."
- Pacing: @Mai speaks quickly, then @Lam answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning street bustle, birdsong, a teacup clinking on wood, a motorbike horn outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 1 (`canh-26/clip-1.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 8s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A bright, clean eye-hospital room in the morning: a white bed, a big window full of sunlight, a small bedside table with a thermos and a vase of daisies.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium two-shot at the bedside table, slow push-in.
- Shot 2, 3–8s: 85mm close-up of the gadget man by the gifts, locked off.
- Shot 3, 8–10s: 50mm over-the-shoulder shot from behind the gadget man onto the granddaughter.
- Shot 4, 10–13s: 85mm close-up of the granddaughter, locked off.
- Shot 5, 13–15s: 40mm medium two-shot at the bedside table, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the bright eye-hospital room, @Khoa on screen-right sets a bag of oranges among the gifts on the bedside table and is already speaking in a low dry nasal voice to @Mai, while @Mai on screen-left holds a tin lunchbox, mouth closed.
- 1–2s (Shot 1): @Khoa keeps talking deadpan, nodding at a brass cyclo bell among the gifts.
- 2–3s (Shot 1): @Khoa points at the lunchbox in @Mai's hands as he goes on.
- 3–4s (CUT to Shot 2): @Khoa keeps speaking flatly in close-up, magnifier glasses perched on his forehead.
- 4–5s (Shot 2): @Khoa counts on his bony fingers as he goes on.
- 5–6s (Shot 2): @Khoa lowers his voice and leans in as he keeps talking.
- 6–7s (Shot 2): @Khoa tucks a fat red envelope with no writing beside the daisies, still talking deadpan.
- 7–8s (Shot 2): @Khoa says his last words, closes his mouth and taps the envelope for emphasis.
- 8–9s (CUT to Shot 3): @Mai starts answering with a teasing grin, holding back a giggle.
- 9–10s (Shot 3): @Mai keeps talking, eyebrows raised over her round glasses.
- 10–11s (CUT to Shot 4): @Mai keeps speaking in close-up, wagging one finger toward screen-right.
- 11–12s (Shot 4): @Mai keeps talking playfully, pretending to dial a number on her phone.
- 12–13s (Shot 4): @Mai keeps talking, pressing her lips together between words to stop a laugh.
- 13–14s (CUT to Shot 5): @Mai finishes and closes her mouth, eyes dancing.
- 14–15s (Shot 5): @Khoa freezes, glances at the envelope and lifts one finger to his closed lips, while @Mai giggles silently behind the lunchbox. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.9s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, deadpan, lowering his voice): "Tiền mổ là cả phố góp đấy. Bác xích lô bỏ ra mấy cuốc xe, bà bán xôi góp cả tháng lãi. Nhiều nhất là bà Hoa, nhưng cấm kể."
- Turn 2, 8.4–13.2s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking at a natural, even conversational pace, teasing, holding back a giggle): "Thế là ông vừa kể xong rồi đấy ạ. Cháu mà mách bà thì ông chết với bà nhé!"
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft hospital hum, birdsong outside the window, a paper bag rustling, a curtain stirring in the breeze. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 2 (`canh-26/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A bright, clean eye-hospital room in the morning: a white bed, a big window full of sunlight, a small bedside table with a thermos and a vase of daisies.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: a nurse in white scrubs seen from behind
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the old man propped against the pillows, slow push-in.
- Shot 2, 4–8s: 85mm close-up of the old man's face as the last layer comes away, slow push-in.
- Shot 3, 8–13s: 50mm over-the-shoulder shot from behind the nurse onto the old man.
- Shot 4, 13–15s: 28mm wide shot of the sunlit room with the old man on the bed facing the big window.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam sits propped against white pillows with a gauze bandage over his eyes as a nurse in white scrubs, seen from behind, begins unwinding it, and he is already speaking softly.
- 1–2s (Shot 1): @Lam keeps talking softly, hands resting calmly on the sheet.
- 2–3s (Shot 1): @Lam keeps speaking with a patient smile under the bandage, as another layer comes away.
- 3–4s (Shot 1): @Lam goes on quietly, chin lifted toward the window light.
- 4–5s (CUT to Shot 2): @Lam keeps talking in close-up as the last layer of gauze comes away from his eyes.
- 5–6s (Shot 2): @Lam blinks several times into the flood of morning light and keeps talking in surprise.
- 6–7s (Shot 2): @Lam's once-cloudy left eye is clear now, and he keeps talking in wonder toward the window.
- 7–8s (Shot 2): @Lam keeps speaking, gazing past the nurse toward the green leaves outside.
- 8–9s (CUT to Shot 3): @Lam lifts one finger as if counting the leaves, still talking softly.
- 9–10s (Shot 3): @Lam keeps talking in wonder, a slow smile spreading.
- 10–11s (Shot 3): @Lam shakes his head gently at himself as he goes on.
- 11–12s (Shot 3): @Lam keeps speaking, the last words hushed.
- 12–13s (Shot 3): @Lam finishes and closes his mouth, eyes glistening.
- 13–14s (CUT to Shot 4): Outside the big window, green leaves shimmer in the morning sun.
- 14–15s (Shot 4): @Lam slowly turns his head toward the bedside on screen-left, a slow closed-mouth smile spreading across his weathered face. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, hushed, breaking into wonder), in Vietnamese with exact lip-sync, said exactly once: "Cô cứ tháo từ từ thôi, tôi không vội đâu. Mấy hôm nay nằm trong bóng tối cũng quen rồi. Ơ, sáng quá. Lá ngoài cửa sổ xanh thế này cơ à? Đếm được từng chiếc một. Thế mà cứ ngỡ trời Hà Nội vốn mờ." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft rustle of unwinding gauze, birdsong, a gentle hospital hum, a deep slow breath. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 3 (`canh-26/clip-3.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 8s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
A bright, clean eye-hospital room in the morning: a white bed, a big window full of sunlight, a small bedside table with a thermos and a vase of daisies.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium two-shot at the bedside in the sunlight, slow arc.
- Shot 2, 3–8s: 85mm close-up of the old man's face and clear eyes, locked off.
- Shot 3, 8–11s: 50mm over-the-shoulder shot from behind the old man onto the granddaughter.
- Shot 4, 11–13s: 85mm close-up of the granddaughter, locked off.
- Shot 5, 13–15s: 40mm medium two-shot in the sunlight, slow arc.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam sits on the edge of the white hospital bed on screen-right, looking at @Mai on screen-left with clear bright eyes, and is already speaking softly and slowly to her, while @Mai listens, mouth closed.
- 1–2s (Shot 1): @Lam keeps speaking, studying @Mai's face.
- 2–3s (Shot 1): @Lam tilts his head as he goes on, gently teasing.
- 3–4s (CUT to Shot 2): @Lam keeps talking softly in close-up, his once-cloudy left eye now clear and bright.
- 4–5s (Shot 2): @Lam shakes his head slowly as he goes on, smiling tenderly.
- 5–6s (Shot 2): @Lam keeps speaking slowly, a soft laugh in his voice.
- 6–7s (Shot 2): @Lam beckons her closer with one weathered hand as he goes on.
- 7–8s (Shot 2): @Lam says the last words and closes his mouth with a teasing smile.
- 8–9s (CUT to Shot 3): @Mai steps closer, red-rimmed eyes glistening behind her round glasses, and starts answering quickly through her tears with a wet laugh.
- 9–10s (Shot 3): @Mai keeps talking fast, words tumbling out, nodding hard.
- 10–11s (Shot 3): @Mai presses one hand to her chest as she goes on.
- 11–12s (CUT to Shot 4): @Mai keeps talking in close-up through a sniffle, smiling wide.
- 12–13s (Shot 4): @Mai wags a finger at herself as she adds her last promise.
- 13–14s (CUT to Shot 5): @Mai finishes, closes her mouth and wipes her eyes under her glasses with a silent laugh.
- 14–15s (Shot 5): @Lam watches her with a warm closed-mouth smile in the sunlight. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.6s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking slowly and softly, unhurried, with a short natural pause between phrases, tender, gently teasing): "Cháu ông xinh thế này, mà bao năm ông chỉ thấy lờ mờ. Phí quá, con ạ. Lại gần đây cho ông nhìn kỹ nào."
- Turn 2, 8.1–13.8s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, laughing through tears, words tumbling): "Thế thì từ giờ ông ngắm cháu bù đi! Cháu hứa, không để ông phải lo thêm ngày nào nữa. Cũng không vay app nào nữa đâu!"
- Pacing: @Lam speaks slowly and calmly, then @Mai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong, a soft sniffle, a curtain swaying in the breeze, distant street horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 26 - Clip 4 (`canh-26/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
The doorway of the bright eye-hospital room, a white corridor behind, morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot of the pair in the doorway, locked off.
- Shot 2, 5–10s: 85mm close-up of the gadget man, locked off.
- Shot 3, 10–13s: 40mm medium two-shot of the pair in the doorway, slow push-in.
- Shot 4, 13–15s: 85mm close-up of the bún chả lady behind her fan, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaHoa sweeps into the doorway of the bright hospital room on screen-left with @Khoa beside her on screen-right, bamboo fan in hand, and is already speaking fast toward the bed in a brassy teasing voice, while @Khoa keeps his mouth closed.
- 1–2s (Shot 1): @BaHoa keeps talking, wagging the folded fan toward the bed.
- 2–3s (Shot 1): @BaHoa goes on with a teasing grin, gold hoop earrings swinging.
- 3–4s (Shot 1): @BaHoa keeps talking fast, counting years on her fingers with mock outrage.
- 4–5s (Shot 1): @BaHoa finishes, closes her mouth and arches one eyebrow, as @Khoa leans toward the bed and starts speaking in a dry nasal deadpan.
- 5–6s (CUT to Shot 2): @Khoa keeps talking flatly, nodding sideways toward @BaHoa.
- 6–7s (Shot 2): @Khoa lowers his voice as he goes on, a sly glint behind his glasses.
- 7–8s (Shot 2): @Khoa keeps speaking deadpan in close-up.
- 8–9s (Shot 2): @Khoa keeps talking, the corner of his mouth twitching.
- 9–10s (Shot 2): @Khoa closes his mouth with a sly wink.
- 10–11s (CUT to Shot 3): @BaHoa turns on @Khoa and starts speaking in a quick flustered hiss, red in the face.
- 11–12s (Shot 3): @BaHoa keeps hissing at him, pointing the folded fan at him.
- 12–13s (Shot 3): @BaHoa finishes her last words and closes her mouth, red lips pressed tight.
- 13–14s (CUT to Shot 4): @BaHoa huffs, mouth closed, her gold hoop earrings still swinging.
- 14–15s (Shot 4): @BaHoa flicks her bamboo fan open in front of her face to hide her reddening cheeks. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking quickly in short lively phrases, every word still clear, brassy and teasing): "Sáng mắt rồi thì nhớ trả tôi tiền bún chả ông ăn chịu bao nhiêu năm nay đấy nhé!"
- Turn 2, 4.9–9.9s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, dry deadpan aside): "Bà ấy nói đùa thôi. Đêm qua khóc mãi, cứ sợ mổ xong ông không nhận ra bà ấy nữa."
- Turn 3, 10.4–12.9s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking quickly in short lively phrases, every word still clear, flustered hiss): "Ông Khoa, im ngay đi! Ai khóc? Bụi bay vào mắt thôi!"
- Pacing: @BaHoa speaks quickly, then @Khoa answers at an even everyday pace, then @BaHoa answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heeled sandals clicking on tile, a bamboo fan flicking open, a stifled sniff, a quiet hospital corridor hum. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 1 (`canh-27/clip-1.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Bà Hoa's bustling bún chả shop on an old-quarter street by day: charcoal grills smoking on the pavement, low plastic stools, steel tables, baskets of fresh herbs, warm sunlight through the smoke.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaHoa = Bà Hoa, 61, the old gang's sharp-tongued brains, now owner of a bún chả shop; plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings; purple floral silk blouse, black wide trousers, chunky gold bangle, low heeled sandals.
- @Khoa = Ông Khoa, 60, the old gang's lock and gadget wizard, now repairs radios and phones; thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead; brown multi-pocket vest over a blue checkered shirt, grey trousers, canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium two-shot across the steel table, locked off.
- Shot 2, 3–6s: 85mm close-up of the gadget man, locked off.
- Shot 3, 6–9s: 50mm over-the-shoulder shot from behind the gadget man onto the bún chả lady.
- Shot 4, 9–12s: 85mm close-up of the bún chả lady, locked off.
- Shot 5, 12–15s: 40mm medium two-shot across the steel table, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): At a steel table in the bustling bún chả shop, @BaHoa on screen-left and @Khoa on screen-right each pinch one end of a small paper bill, and @Khoa is already speaking in a dry deadpan voice, while @BaHoa keeps her red lips pressed together.
- 1–2s (Shot 1): @Khoa keeps talking flatly, not letting go of his end of the bill.
- 2–3s (Shot 1): @Khoa tugs the bill an inch toward himself as he goes on.
- 3–4s (CUT to Shot 2): @Khoa keeps speaking stubbornly in close-up, chin lifted, magnifier glasses glinting on his forehead.
- 4–5s (Shot 2): @Khoa keeps talking, nodding solemnly toward the street.
- 5–6s (Shot 2): @Khoa finishes his last words, closes his mouth and raises his eyebrows in triumph.
- 6–7s (CUT to Shot 3): @BaHoa narrows her eyes and starts retorting fast in a brassy voice, tugging the bill back.
- 7–8s (Shot 3): @BaHoa keeps talking quick-fire, gold hoop earrings swinging.
- 8–9s (Shot 3): @BaHoa nods at the magnifier glasses on @Khoa's forehead as she goes on.
- 9–10s (CUT to Shot 4): @BaHoa keeps scolding in close-up with mock indignation, gold bangle glinting.
- 10–11s (Shot 4): @BaHoa keeps talking fast, the little bill tugging back and forth between them.
- 11–12s (Shot 4): @BaHoa finishes and closes her mouth, glaring across the table.
- 12–13s (CUT to Shot 5): @Khoa answers in a flat deadpan murmur, peering at her over the bill with a tiny sly smile.
- 13–14s (Shot 5): @Khoa says the last words and closes his mouth, while @BaHoa's cheeks turn pink.
- 14–15s (Shot 5): Both hold their stubborn closed-mouth smiles, the paper bill stretched taut between their fingertips in the warm smoky sunlight. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, deadpan and stubborn): "Bà buông ra đi. Bao lần bà mời rồi, hôm nay đến lượt tôi, coi như ăn mừng cho ông Lâm."
- Turn 2, 6.2–11.5s, spoken on camera by @BaHoa (woman of 61, loud brassy alto with a teasing rasp and a sing-song market-seller cadence, speaking quickly in short lively phrases, every word still clear, mock-indignant, quick-fire): "Quán của tôi thì tôi mời! Ông giữ tiền mà sắm cặp kính lúp mới đi, cái cũ nứt từ năm nảo năm nao rồi."
- Turn 3, 12.0–14.0s, spoken on camera by @Khoa (man of 60, thin nasal tenor, flat deadpan delivery, fussy precise consonants, speaking at a natural, even conversational pace, deadpan, a sly flirt): "Nứt mới hay, nhìn bà thành hai người."
- Pacing: @Khoa speaks at an even everyday pace, then @BaHoa answers quickly, then @Khoa answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pork sizzling on charcoal, a paper bill crinkling, chopsticks clinking, street bustle. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 2 (`canh-27/clip-2.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Dawn in Hà Nội's old quarter: an ancient brick city gate with a tiled roof, narrow streets of tube houses with green shutters, tangled overhead wires, street vendors with shoulder poles, pink-gold morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- @Mai = Mai, 20, Lâm's granddaughter, an IT student; petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes; oversized lavender hoodie, black jeans, chunky white sneakers, small black backpack.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium two-shot of the motorbike under the arch, slow dolly-in.
- Shot 2, 3–7s: 85mm close-up of the granddaughter hugging her laptop, locked off.
- Shot 3, 7–10s: 50mm over-the-shoulder shot from behind the granddaughter onto the old man astride the motorbike.
- Shot 4, 10–13s: 85mm close-up of the old man on his motorbike, locked off.
- Shot 5, 13–15s: 40mm medium shot of the old man on his motorbike under the gate, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): The old cream-colored step-through motorbike rolls to a stop under the ancient brick city gate with @Lam in front and @Mai behind him, and @Mai is already speaking fast and eagerly over his shoulder.
- 1–2s (Shot 1): @Mai hops off on screen-right hugging a laptop and keeps talking eagerly, while @Lam listens, mouth closed.
- 2–3s (Shot 1): @Mai taps the laptop lid as she goes on, bright and quick.
- 3–4s (CUT to Shot 2): @Mai keeps talking fast in close-up, eyes bright behind her round glasses.
- 4–5s (Shot 2): @Mai nods eagerly as she goes on, hugging the laptop tighter.
- 5–6s (Shot 2): @Mai points toward screen-left with a grin as she keeps talking.
- 6–7s (Shot 2): @Mai finishes with a bright smile and closes her mouth.
- 7–8s (CUT to Shot 3): @Lam, still astride the motorbike on screen-left, starts answering with a dry fond grumble.
- 8–9s (Shot 3): @Lam keeps talking, patting the old phone in his windbreaker pocket.
- 9–10s (Shot 3): @Lam waves her off toward the street with the back of his hand as he goes on.
- 10–11s (CUT to Shot 4): @Lam keeps grumbling fondly in close-up, a smile hiding at the corner of his mouth.
- 11–12s (Shot 4): @Lam keeps talking, eyebrows raised in mock sternness.
- 12–13s (Shot 4): @Lam adds his last words and closes his mouth, eyes following someone off screen-right.
- 13–14s (CUT to Shot 5): Down the sunlit street behind him, @Mai waves once and strides away with her small black backpack, while @Lam smiles after her, mouth closed.
- 14–15s (Shot 5): @Lam sets the motorbike on its stand under the gate and sits sideways on the seat with a quiet closed-mouth smile. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.3s, spoken on camera by @Mai (young woman of 20, bright clear high voice, quick and earnest, a little breathless when worried, speaking quickly in short lively phrases, every word still clear, bright and eager): "Ông này, cháu đang viết một cái app, giúp các bạn nhận ra mấy chỗ cho vay lừa đảo. Làm xong cháu cài cho ông đầu tiên nhé!"
- Turn 2, 6.8–13.0s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, fond grumble): "Ông chỉ cần cái app nào gọi được khách là đủ. Vào lớp đi, muộn rồi. Đi cẩn thận, nhớ ăn sáng đấy, con."
- Pacing: @Mai speaks quickly, then @Lam answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: sparrows chirping, an old engine puttering to a stop, a broom sweeping the pavement, a vendor's hand bell, distant motorbike horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 3 (`canh-27/clip-3.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

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

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium shot of the old man on his motorbike under the gate, holding the previous framing.
- Shot 2, 3–7s: 85mm close-up of the old man, locked off.
- Shot 3, 7–10s: 50mm over-the-shoulder shot from behind the young delivery rider onto the old man.
- Shot 4, 10–13s: 35mm medium shot of the old man leaning on the handlebars, slow push-in.
- Shot 5, 13–15s: 28mm wide shot under the golden gate, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam sits sideways on his motorbike seat under the golden gate, looking up at a young man in a delivery jacket who has just stopped beside him on screen-right hugging his helmet, and is already speaking with a warm chuckle in a husky voice.
- 1–2s (Shot 1): @Lam tugs his right sleeve down over his forearm as he keeps talking, shaking his head with a sly smile.
- 2–3s (Shot 1): @Lam taps his own chest as he goes on, warm and unhurried.
- 3–4s (CUT to Shot 2): @Lam keeps talking in close-up, his eyes crinkling.
- 4–5s (Shot 2): @Lam keeps speaking, studying the young man's pale face.
- 5–6s (Shot 2): @Lam pats the motorbike's back seat twice with his palm as he goes on.
- 6–7s (Shot 2): @Lam keeps talking, nodding toward the street ahead.
- 7–8s (CUT to Shot 3): @Lam keeps speaking warmly, while the young man's hunched shoulders slowly relax.
- 8–9s (Shot 3): @Lam leans forward on the handlebars and keeps speaking, a knowing look in his calm eyes.
- 9–10s (Shot 3): @Lam keeps talking softly, his brows drawing together.
- 10–11s (CUT to Shot 4): @Lam keeps talking, one hand resting on the seat behind him.
- 11–12s (Shot 4): @Lam asks his last question gently, inviting him with a tilt of the head.
- 12–13s (Shot 4): @Lam finishes, closes his mouth and gives a knowing wink.
- 13–14s (CUT to Shot 5): The young man climbs onto the back seat behind @Lam in the golden light under the gate.
- 14–15s (Shot 5): @Lam thumbs the starter and the old engine coughs to life, mouth closed, the two small figures framed by the golden arch. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, warm, sly chuckle), in Vietnamese with exact lip-sync, said exactly once: "Cậu hỏi tôi có phải Lâm Rồng không à? Nhầm người rồi, cậu ạ, tôi chỉ là ông già chạy xe ôm thôi. Nhưng cứ lên xe đi, đường còn dài. Mặt cậu tái mét thế kia, kể tôi nghe, đứa nào bắt nạt cậu thế?" (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: sparrows chirping, shuffling footsteps, a palm patting a vinyl seat, the old engine coughing to life. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 27 - Clip 4 (`canh-27/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese caper comedy film set in Hà Nội's old quarter today; vibrant warm grade with saturated golden yellows, jade greens and magenta neon at night, crisp bright daylight, natural skin texture, subtle 35mm film grain, energetic handheld feel.

[LIGHTING]
Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.

[LOCATION]
Golden morning at the ancient brick city gate of Hà Nội's old quarter, opening into a vast aerial view of tiled roofs, tangled wires and narrow streets.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Ông Lâm, 63, humble motorbike-taxi driver who was once the old quarter's legendary gang boss; wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles; faded grey zip-up windbreaker over a white tank top, loose khaki trousers, plastic sandals, a battered green pith helmet, a dark-green dragon tattoo on his right forearm usually hidden by his sleeve.
- Extra: a young man in a delivery jacket riding on the back seat behind him
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the old man on his motorbike at the curb with a phone at his ear, the young passenger behind him.
- Shot 2, 4–8s: 85mm close-up of the old man on the phone, locked off.
- Shot 3, 8–13s: 50mm medium shot from the front of the motorbike, the young passenger waiting behind, locked off.
- Shot 4, 13–15s: drone aerial shot rising and pulling back over the old quarter rooftops.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam sits on the old cream-colored step-through motorbike at the curb outside the ancient brick gate with the young man on the back seat, holds an old phone with a glowing blank screen to his ear and is already speaking quietly.
- 1–2s (Shot 1): @Lam keeps talking into the phone with a sly knowing smile.
- 2–3s (Shot 1): @Lam glances back at the young man as he goes on, voice low.
- 3–4s (Shot 1): @Lam keeps speaking quietly, nodding at what he hears.
- 4–5s (CUT to Shot 2): @Lam keeps speaking quietly in close-up, his calm narrow eyes now bright and clear.
- 5–6s (Shot 2): @Lam nods once as he goes on, the corner of his mouth lifting.
- 6–7s (Shot 2): @Lam keeps talking, his thick grey eyebrows drawing together.
- 7–8s (Shot 2): @Lam keeps speaking into the phone, half turning toward the young man behind him.
- 8–9s (CUT to Shot 3): @Lam rolls his right sleeve back an inch, the dragon tattoo peeking out, as he goes on, while the young man behind him hugs his helmet and waits, mouth closed.
- 9–10s (Shot 3): @Lam keeps talking with a slow smile, glancing up at the old gate.
- 10–11s (Shot 3): @Lam keeps speaking, his voice dropping low and warm.
- 11–12s (Shot 3): @Lam says the last words slowly, a spark in his eyes.
- 12–13s (Shot 3): @Lam closes his mouth and tucks the phone into his windbreaker.
- 13–14s (CUT to Shot 4): @Lam twists the throttle and the little cream motorbike weaves into the narrow streets as the drone soars up and back.
- 14–15s (Shot 4): The golden tiled roofs of the old quarter spread out in every direction, the tiny motorbike threading between them. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.2s, spoken on camera by @Lam (man of 63, low husky voice with a slow dry drawl, slightly gravelly, calm even when angry, speaking at a natural, even conversational pace, quiet, with a knowing smile), in Vietnamese with exact lip-sync, said exactly once: "Bà Hoa à? Tôi đây. Ông Khoa còn ở quán không? Giữ chân ông ấy lại. Ừ, lại có việc rồi. Thằng bé này gặp rắc rối to, to hơn vụ vừa rồi nhiều. Bà đặt sẵn ấm trà đi, Rồng lại cần Hổ với Báo." (no subtitles)
- @Lam starts talking within the first second; whenever @Lam speaks, the face and lips are clearly visible in that shot; after the last word @Lam closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a rising morning breeze, a flock of pigeons' wings fluttering, distant motorbike horns and bicycle bells, the old engine puttering away. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```
