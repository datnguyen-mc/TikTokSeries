# Vợ Tôi Mất Trí Nhớ Có Chọn Lọc — Bộ 100 Prompt Google Flow Omni (25 Cảnh × 4 Clips × 15s)

- **Không có người dẫn chuyện:** 100% lời thoại do nhân vật nói trên hình — cả 100 clip là thoại khớp khẩu hình. Giọng gốc của mỗi nhân vật (tuổi, chất giọng, giọng Hà Nội) giữ nguyên văn ở mọi clip để Omni không đổi người nói.
- **Nhịp giọng theo cảnh:** mỗi lượt thoại có nhịp riêng nối sau giọng gốc — **nhanh** (cãi vã, hoảng hốt, rượt đuổi, khoe khoang; tốc độ ×1.2), **vừa** (trò chuyện thường), **chậm** (xúc động, thú nhận, câu chốt lặng người; tốc độ ×0.9). Khung thoại tính theo nhịp nên câu chậm ít chữ hơn. Cả phim: 113 lượt nhanh, 106 lượt vừa, 81 lượt chậm.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 100 clips × 15s, tất cả là clip thoại; lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 59 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 41 clip ảnh nhân vật (Ingredients), 0 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** không có clip VO nên runner không tăng tốc giọng clip nào; tốc độ nói nằm trong prompt (nhịp từng lượt) để khớp khẩu hình.
- **Màu phim & ánh sáng:** Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py vo-toi-mat-tri-nho` sinh lại toàn bộ clip, README, kịch bản.

---

## Cảnh 01 - Clip 1 (`canh-01/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A luxurious rooftop restaurant terrace at night high above a wide city lake, privately booked and empty of other guests: one candlelit table with white linen and red roses, a glass balustrade, the city's golden lights and the dark lake below, potted olive trees, warm string lights overhead, a private brass elevator at the end of the terrace.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; floor-length emerald-green satin evening gown with thin straps, diamond drop earrings, a slim gold clutch.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the assistant, locked off.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the assistant onto the elegant wife, gentle handheld drift.
- Shot 3, 10–13s: 50mm medium shot of the assistant with the candlelit rooftop terrace softly behind, slow dolly-in.
- Shot 4, 13–15s: 24mm wide shot of the candlelit rooftop terrace with the assistant and the elegant wife, subtle rack focus.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tuan is hurrying across the terrace holding out a huge bouquet of red roses and is already speaking quickly (flustered, over-cheerful).
- 1–2s (Shot 1): @Tuan keeps talking, bowing his head with an awkward grin.
- 2–3s (Shot 1): @Tuan keeps talking, shifting from foot to foot.
- 3–4s (Shot 1): @Tuan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Tuan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking slowly and softly (cool and unimpressed), sitting alone at the candlelit table in her emerald gown, slowly turning her wine glass, while @Tuan listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, raising one perfect eyebrow.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Tuan.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Tuan starts speaking quickly (babbling), nodding far too many times, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Tuan keeps talking, forcing a wide dimpled smile.
- 12–13s (Shot 3): @Tuan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh takes the roses and lays them face-down on the tablecloth without a word.
- 14–15s (Shot 4): @Linh rises and walks toward the glass balustrade, her gown catching the candlelight. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, flustered, over-cheerful): "Chị Linh ơi, anh Quân bận họp gấp với đối tác Nhật, anh ấy gửi chị bó hoa này ạ!"
- Turn 2, 5.1–9.3s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, cool and unimpressed): "Kỷ niệm mười năm ngày cưới, chồng chị gửi hoa thay cho chính mình à?"
- Turn 3, 9.8–13.0s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, babbling): "Dạ, hoa đẹp lắm chị ạ! Chín mươi chín bông, em đếm hai lần rồi!"
- Pacing: @Tuan speaks quickly, then @Linh answers slowly and calmly, then @Tuan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft city hum far below, a gentle night breeze, the faint clink of glassware, distant traffic horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 2 (`canh-01/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A luxurious rooftop restaurant terrace at night high above a wide city lake, privately booked and empty of other guests: one candlelit table with white linen and red roses, a glass balustrade, the city's golden lights and the dark lake below, potted olive trees, warm string lights overhead, a private brass elevator at the end of the terrace.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; floor-length emerald-green satin evening gown with thin straps, diamond drop earrings, a slim gold clutch.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the assistant onto the elegant wife, gentle handheld drift.
- Shot 2, 5–9s: 85mm close-up of the assistant, slow dolly-in.
- Shot 3, 9–13s: 50mm medium shot of the elegant wife with the candlelit rooftop terrace softly behind, subtle rack focus.
- Shot 4, 13–15s: 24mm wide shot of the candlelit rooftop terrace with the elegant wife and the assistant, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is standing at the glass balustrade, staring down at the hotel entrance far below and is already speaking at an easy conversational pace (quietly certain).
- 1–2s (Shot 1): @Linh keeps talking, her knuckles whitening on the glass rail.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Tuan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Tuan starts speaking quickly (panicking), rushing up beside her and peering over the edge, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Tuan keeps talking, waving both hands wildly.
- 7–8s (Shot 2): @Tuan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Tuan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Linh starts speaking slowly and softly (sweetly cutting), turning slowly to face him, while @Tuan listens with the mouth closed.
- 10–11s (Shot 3): @Linh keeps talking, smiling without warmth.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Tuan's face drains of colour; he hugs the empty flower wrapper to his chest.
- 14–15s (Shot 4): @Linh looks back down at the city lights, perfectly still. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, quietly certain): "Đối tác Nhật gì mà mặc váy trắng, khoác tay chồng chị đi vào khách sạn kia?"
- Turn 2, 5.2–8.6s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, panicking): "Chắc là phiên dịch ạ! Bên Nhật họ chuộng phiên dịch trẻ, xinh, biết khoác tay!"
- Turn 3, 9.1–12.8s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, sweetly cutting): "Tuấn này, lần sau nói dối thì nhớ tập trước gương đã nhé."
- Pacing: @Linh speaks at an even everyday pace, then @Tuan answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft city hum far below, a gentle night breeze, the faint clink of glassware, distant traffic horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 3 (`canh-01/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A luxurious rooftop restaurant terrace at night high above a wide city lake, privately booked and empty of other guests: one candlelit table with white linen and red roses, a glass balustrade, the city's golden lights and the dark lake below, potted olive trees, warm string lights overhead, a private brass elevator at the end of the terrace.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; floor-length emerald-green satin evening gown with thin straps, diamond drop earrings, a slim gold clutch.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of the elegant wife and the assistant, slow dolly-in.
- Shot 2, 5–9s: 85mm close-up of the assistant, subtle rack focus.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the assistant onto the elegant wife, slow arc.
- Shot 4, 13–15s: 24mm wide shot of the candlelit rooftop terrace with the elegant wife and the assistant, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is stepping closer to him, eyes level and calm and is already speaking at an easy conversational pace (calm and dangerous).
- 1–2s (Shot 1): @Linh keeps talking, lowering her voice.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Tuan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Tuan starts speaking quickly (blurting the truth), backing up against the glass balustrade, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Tuan keeps talking, raising both palms like a captured man.
- 7–8s (Shot 2): @Tuan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Tuan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Linh starts speaking slowly and softly (a bitter half smile), patting his lapel lightly, while @Tuan listens with the mouth closed.
- 10–11s (Shot 3): @Linh keeps talking, turning away.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh picks up her gold clutch and walks toward the brass elevator with straight shoulders.
- 14–15s (Shot 4): @Tuan presses both palms to his cheeks, mouth hanging open. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, calm and dangerous): "Họ lên tầng mấy? Em nói đi, chị hứa không làm ầm, chỉ xuống chào một câu thôi."
- Turn 2, 5.4–9.0s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, blurting the truth): "Em thề em không biết! Em chỉ được giao mỗi việc mang hoa với nói dối thôi!"
- Turn 3, 9.5–12.9s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, a bitter half smile): "Ít ra em còn thật thà hơn chồng chị đấy, Tuấn ạ."
- Pacing: @Linh speaks at an even everyday pace, then @Tuan answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft city hum far below, a gentle night breeze, the faint clink of glassware, distant traffic horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 4 (`canh-01/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A luxurious rooftop restaurant terrace at night high above a wide city lake, privately booked and empty of other guests: one candlelit table with white linen and red roses, a glass balustrade, the city's golden lights and the dark lake below, potted olive trees, warm string lights overhead, a private brass elevator at the end of the terrace.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; floor-length emerald-green satin evening gown with thin straps, diamond drop earrings, a slim gold clutch.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the assistant with the candlelit rooftop terrace softly behind, subtle rack focus.
- Shot 2, 4–9s: 85mm close-up of the elegant wife, slow arc.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the elegant wife onto the assistant, slow push-in.
- Shot 4, 13–15s: 24mm wide shot of the candlelit rooftop terrace with the assistant and the elegant wife, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tuan is hurrying after her across the terrace and is already speaking quickly (begging).
- 1–2s (Shot 1): @Tuan keeps talking, spreading his arms wide.
- 2–3s (Shot 1): @Tuan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Tuan finishes the line and closes the mouth.
- 4–5s (CUT to Shot 2): @Linh starts speaking slowly and softly (gracious and deadly), pausing to look back over her shoulder with a cool smile, while @Tuan listens with the mouth closed.
- 5–6s (Shot 2): @Linh keeps talking, pressing the brass elevator call button.
- 6–7s (Shot 2): @Linh keeps talking, one hand moving lightly with the words.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Tuan.
- 8–9s (Shot 2): @Linh finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Tuan starts speaking quickly (doomed whisper), turning away and hunching over his phone, while @Linh listens with the mouth closed.
- 10–11s (Shot 3): @Tuan keeps talking, covering his mouth with one hand.
- 11–12s (Shot 3): @Tuan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Tuan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): The brass elevator doors slide shut on @Linh's calm, beautiful face.
- 14–15s (Shot 4): @Tuan stands alone among the candles, phone still at his ear. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.0s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, begging): "Chị ơi chị đi đâu đấy? Chị đừng xuống, dưới ấy chỉ có toàn người Nhật thôi!"
- Turn 2, 4.5–9.0s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, gracious and deadly): "Chị xuống chào hỏi đối tác của chồng. Vợ giám đốc thì phải lịch sự chứ."
- Turn 3, 9.5–12.7s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, doomed whisper): "Chết em rồi, chết thật rồi. Anh Quân ơi, anh tự lo lấy thân nhé."
- Pacing: @Tuan speaks quickly, then @Linh answers slowly and calmly, then @Tuan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft city hum far below, a gentle night breeze, the faint clink of glassware, distant traffic horns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 1 (`canh-02/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The grand lobby of a five-star hotel at night, quiet and empty: polished cream marble floor, a sweeping crystal chandelier, tall marble pillars, velvet emerald sofas, a bank of brass elevator doors, huge white orchid arrangements.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; chic short white bouclé jacket dress, a pearl hair clip, white heels.
- Wardrobe: in this shot @MaiAnh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young yoga teacher, slow arc.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the young yoga teacher onto the husband, slow push-in.
- Shot 3, 10–13s: 50mm medium shot of the young yoga teacher with the marble hotel lobby softly behind, locked off.
- Shot 4, 13–15s: 24mm wide shot of the marble hotel lobby with the young yoga teacher and the husband, gentle handheld drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is linking her arm through his beside the white orchids and is already speaking at an easy conversational pace (coy, a little pouty).
- 1–2s (Shot 1): @MaiAnh keeps talking, looking up at him with wide doe eyes.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking at an easy conversational pace (smooth and practiced), adjusting his silver cufflink, while @MaiAnh listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, glancing toward the brass elevators.
- 7–8s (Shot 2): @Quan keeps talking, giving a practiced smile.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @MaiAnh starts speaking quickly (delighted), bouncing on her toes, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @MaiAnh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): An elevator chime rings; @Quan's eyes flick toward the brass doors.
- 14–15s (Shot 4): @Quan slides his arm free and takes a step back, his smile frozen in place. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, coy, a little pouty): "Anh hứa sau ngày kỷ niệm ấy là anh nói chuyện ly hôn cho xong. Anh nhớ chứ?"
- Turn 2, 5.4–9.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, smooth and practiced): "Anh nhớ. Bọn anh ly thân hai năm rồi, giờ chỉ còn tờ giấy thôi."
- Turn 3, 9.7–12.9s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, delighted): "Thế tối nay anh ở lại ăn tối với em nhé, em đặt bàn rồi!"
- Pacing: @MaiAnh speaks at an even everyday pace, then @Quan answers at an even everyday pace, then @MaiAnh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft piano-free hush of a grand lobby, footsteps echoing on marble, a gentle elevator chime, a fountain trickling somewhere. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 2 (`canh-02/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The grand lobby of a five-star hotel at night, quiet and empty: polished cream marble floor, a sweeping crystal chandelier, tall marble pillars, velvet emerald sofas, a bank of brass elevator doors, huge white orchid arrangements.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; chic short white bouclé jacket dress, a pearl hair clip, white heels.
- Wardrobe: in this shot @MaiAnh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm over-the-shoulder shot from behind the young yoga teacher onto the husband, slow push-in.
- Shot 2, 4–8s: 85mm close-up of the young yoga teacher, locked off.
- Shot 3, 8–12s: 50mm medium shot of the husband with the marble hotel lobby softly behind, gentle handheld drift.
- Shot 4, 12–15s: 24mm wide shot of the marble hotel lobby with the husband and the young yoga teacher, slow dolly-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is gesturing her toward a tall marble pillar and is already speaking quickly (rattled).
- 1–2s (Shot 1): @Quan keeps talking, glancing back over his shoulder.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @MaiAnh.
- 3–4s (Shot 1): @Quan finishes the line and closes the mouth.
- 4–5s (CUT to Shot 2): @MaiAnh starts speaking quickly (puzzled), craning her neck past him toward the elevators, while @Quan listens with the mouth closed.
- 5–6s (Shot 2): @MaiAnh keeps talking, frowning.
- 6–7s (Shot 2): @MaiAnh keeps talking, one hand moving lightly with the words.
- 7–8s (Shot 2): @MaiAnh finishes the line and closes the mouth.
- 8–9s (CUT to Shot 3): @Quan starts speaking quickly (frantic), flapping one hand at her, while @MaiAnh listens with the mouth closed.
- 9–10s (Shot 3): @Quan keeps talking, never looking away from @MaiAnh.
- 10–11s (Shot 3): @Quan keeps talking, holding @MaiAnh's gaze.
- 11–12s (Shot 3): @Quan finishes the line and closes the mouth.
- 12–13s (CUT to Shot 4): @MaiAnh hurries behind the tall marble pillar, clutching her little handbag.
- 13–14s (Shot 4): @Quan straightens his navy jacket and turns toward the elevators.
- 14–15s (Shot 4): @Quan stretches his face into a broad, stiff smile. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.6s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, rattled): "Em ra sau cột kia đứng đợi anh một lát, anh có cuộc gọi gấp!"
- Turn 2, 4.1–7.7s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, puzzled): "Cuộc gọi gì mà mặt anh trắng bệch thế kia? Ai vừa ra khỏi thang máy thế?"
- Turn 3, 8.2–11.4s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, frantic): "Đối tác! Đối tác Nhật lai Hàn, khó tính lắm! Em đi đi, nhanh lên!"
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft piano-free hush of a grand lobby, footsteps echoing on marble, a gentle elevator chime, a fountain trickling somewhere. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 3 (`canh-02/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The grand lobby of a five-star hotel at night, quiet and empty: polished cream marble floor, a sweeping crystal chandelier, tall marble pillars, velvet emerald sofas, a bank of brass elevator doors, huge white orchid arrangements.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; floor-length emerald-green satin evening gown with thin straps, diamond drop earrings, a slim gold clutch.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium two-shot of the husband and the elegant wife, locked off.
- Shot 2, 4–10s: 85mm close-up of the elegant wife, gentle handheld drift.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the elegant wife onto the husband, slow dolly-in.
- Shot 4, 13–15s: 24mm wide shot of the marble hotel lobby with the husband and the elegant wife, subtle rack focus.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is striding across the marble floor toward her with open arms and is already speaking quickly (far too loud).
- 1–2s (Shot 1): @Quan keeps talking, laughing a beat too loudly.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan finishes the line and closes the mouth.
- 4–5s (CUT to Shot 2): @Linh starts speaking slowly and softly (soft and lethal), standing perfectly still in her emerald gown, while @Quan listens with the mouth closed.
- 5–6s (Shot 2): @Linh keeps talking, tilting her head toward the marble pillar.
- 6–7s (Shot 2): @Linh keeps talking, one hand moving lightly with the words.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Quan starts speaking quickly (laughing too hard), stepping sideways to block her view, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh looks at him for a long silent moment.
- 14–15s (Shot 4): @Linh lifts two fingers to her temple and sways on her heels. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.0s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, far too loud): "Vợ ơi! Sao em lại xuống đây? Anh vừa họp xong, đang định lên với em đây!"
- Turn 2, 4.5–9.3s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft and lethal): "Em xuống chào đối tác Nhật của anh. Cô ấy đứng sau cái cột kia phải không?"
- Turn 3, 9.8–13.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, laughing too hard): "Cột nào? Ở đấy làm gì có ai! Khách sạn này toàn cột thôi em ạ!"
- Pacing: @Quan speaks quickly, then @Linh answers slowly and calmly, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft piano-free hush of a grand lobby, footsteps echoing on marble, a gentle elevator chime, a fountain trickling somewhere. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 4 (`canh-02/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The grand lobby of a five-star hotel at night, quiet and empty: polished cream marble floor, a sweeping crystal chandelier, tall marble pillars, velvet emerald sofas, a bank of brass elevator doors, huge white orchid arrangements.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; floor-length emerald-green satin evening gown with thin straps, diamond drop earrings, a slim gold clutch.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the elegant wife with the marble hotel lobby softly behind, gentle handheld drift.
- Shot 2, 5–10s: 85mm close-up of the husband, slow dolly-in.
- Shot 3, 10–15s: 35mm medium two-shot of the elegant wife and the husband, subtle rack focus.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is swaying on her heels, one hand at her forehead and is already speaking slowly and softly (faint and dazed).
- 1–2s (Shot 1): @Linh keeps talking, blinking slowly up at the chandelier.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking quickly (alarmed), guiding her gently down onto an emerald velvet sofa, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, waving his free hand toward the empty reception desk.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking slowly and softly (blank and puzzled), gazing up at him with blank, puzzled eyes, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh closes her eyes and goes limp against the velvet cushions. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.3s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, faint and dazed): "Anh Quân, sao đèn ở đây quay nhiều thế? Em thấy chóng mặt quá."
- Turn 2, 4.8–9.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, alarmed): "Vợ ơi, em sao thế? Em ngồi xuống đây đã, ngồi xuống đây! Có ai không, gọi cấp cứu giúp tôi!"
- Turn 3, 9.7–13.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, blank and puzzled): "Lạ thật, anh là ai nhỉ? Sao anh cứ gọi tôi là vợ?"
- Pacing: @Linh speaks slowly and calmly, then @Quan answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft piano-free hush of a grand lobby, footsteps echoing on marble, a gentle elevator chime, a fountain trickling somewhere. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 1 (`canh-03/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A bright private VIP hospital room by day: a white adjustable hospital bed with crisp sheets, a bedside monitor showing only soft wave lines, a vase of white lilies, a large window with sheer curtains over the city, a pale-wood visitor chair.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; pale-blue cotton hospital gown under a soft white knit cardigan.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the husband, slow dolly-in.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, subtle rack focus.
- Shot 3, 10–12s: 50mm medium shot of the husband with the bright hospital room softly behind, slow arc.
- Shot 4, 12–15s: 24mm wide shot of the bright hospital room with the husband and the elegant wife, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is sitting on the edge of the visitor chair holding her hand and is already speaking at an easy conversational pace (tender, exhausted).
- 1–2s (Shot 1): @Quan keeps talking, leaning closer with red-rimmed eyes.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking quickly (alarmed and bright), pulling her hand back and hugging the blanket to her chest, while @Quan listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, scooting back against the pillows.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Quan starts speaking quickly (aghast), pointing at himself, then at her, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Quan finishes the line and closes the mouth.
- 12–13s (CUT to Shot 4): @Linh stares at him with wide suspicious eyes and slowly shakes her head.
- 13–14s (Shot 4): @Quan rubs his face hard with both hands.
- 14–15s (Shot 4): @Linh and @Quan stay silent, mouths closed, as the moment settles. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, tender, exhausted): "Em tỉnh rồi à? Anh đây, anh ngồi đây cả đêm. Em thấy trong người thế nào?"
- Turn 2, 5.2–9.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, alarmed and bright): "Anh là ai? Sao anh lại cầm tay tôi? Bỏ ra, tôi còn chưa có người yêu đâu đấy!"
- Turn 3, 9.7–12.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, aghast): "Người yêu gì? Anh là chồng em! Chồng mười năm nay rồi!"
- Pacing: @Quan speaks at an even everyday pace, then @Linh answers quickly, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft beep of a bedside monitor, a quiet air conditioner, distant hospital footsteps, birds outside the window. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 2 (`canh-03/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A bright private VIP hospital room by day: a white adjustable hospital bed with crisp sheets, a bedside monitor showing only soft wave lines, a vase of white lilies, a large window with sheer curtains over the city, a pale-wood visitor chair.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; pale-blue cotton hospital gown under a soft white knit cardigan.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, subtle rack focus.
- Shot 2, 5–10s: 85mm close-up of the husband, slow arc.
- Shot 3, 10–13s: 50mm medium shot of the elegant wife with the bright hospital room softly behind, slow push-in.
- Shot 4, 13–15s: 24mm wide shot of the bright hospital room with the elegant wife and the husband, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is tossing her long hair over one shoulder and is already speaking quickly (playful and indignant).
- 1–2s (Shot 1): @Linh keeps talking, doing a little model pose against the pillows.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking at an easy conversational pace (stunned), holding up seven fingers, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, searching her face.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking slowly and softly (sweet, then flat), breaking into a soft smile, then letting it drop, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Quan's mouth opens and closes with no sound.
- 14–15s (Shot 4): @Linh turns to the window and hums to herself, swinging one bare foot. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, playful and indignant): "Chồng á? Anh đùa à? Tôi năm nay mới hai mươi hai tuổi, đang đi thi người mẫu cơ mà!"
- Turn 2, 5.1–9.6s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, stunned): "Em ba mươi hai tuổi rồi. Mình có con gái bảy tuổi, tên là Bống, em nhớ không?"
- Turn 3, 10.1–12.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, sweet, then flat): "Bống thì tôi nhớ. Còn anh thì chịu."
- Pacing: @Linh speaks quickly, then @Quan answers at an even everyday pace, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft beep of a bedside monitor, a quiet air conditioner, distant hospital footsteps, birds outside the window. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 3 (`canh-03/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The quiet hospital corridor outside the VIP room by day: pale walls, a long window with soft daylight, a wooden bench, a potted fern, a closed pale-wood door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium two-shot of the doctor and the husband, slow arc.
- Shot 2, 6–10s: 85mm close-up of the husband, slow push-in.
- Shot 3, 10–15s: 35mm medium two-shot of the doctor and the husband, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang is walking beside him down the corridor holding a blank white folder and is already speaking at an easy conversational pace (clinical).
- 1–2s (Shot 1): @Khang keeps talking, adjusting his rimless glasses.
- 2–3s (Shot 1): @Khang keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Khang keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Khang keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Khang finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Quan starts speaking quickly (disbelieving), stopping short in the middle of the corridor, while @Khang listens with the mouth closed.
- 7–8s (Shot 2): @Quan keeps talking, spreading his hands wide.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Khang starts speaking slowly and softly (dry deadpan), tucking his pen into his coat pocket, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @Khang keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Khang keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Khang finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan sinks onto the wooden bench, staring at the floor. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking at a natural, even conversational pace, clinical): "Chị nhà bị mất trí nhớ ngược dòng. Tạm thời chị ấy quên mất khoảng mười năm gần nhất."
- Turn 2, 5.7–9.1s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, disbelieving): "Mười năm? Đúng mười năm lấy tôi? Sao quên chính xác thế được hả bác sĩ?"
- Turn 3, 9.6–14.1s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking slowly and softly, unhurried, with a short natural pause between phrases, dry deadpan): "Trí nhớ có chọn lọc, anh ạ. Cái gì đau quá thì não tự cất đi."
- Pacing: @Khang speaks at an even everyday pace, then @Quan answers quickly, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft beep of a bedside monitor, a quiet air conditioner, distant hospital footsteps, birds outside the window. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 4 (`canh-03/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The quiet hospital corridor outside the VIP room by day: pale walls, a long window with soft daylight, a wooden bench, a potted fern, a closed pale-wood door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the husband with the bright hospital room softly behind, slow push-in.
- Shot 2, 6–11s: 85mm close-up of the doctor, locked off.
- Shot 3, 11–15s: 35mm medium two-shot of the husband and the doctor, gentle handheld drift.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is rising from the bench and is already speaking at an easy conversational pace (pressing).
- 1–2s (Shot 1): @Quan keeps talking, rubbing the back of his neck.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Khang.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Khang starts speaking at an easy conversational pace (polite and immovable), calmly closing the white folder, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @Khang keeps talking, meeting his eyes over the rimless glasses.
- 8–9s (Shot 2): @Khang keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Khang keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Khang finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Quan starts speaking quickly (exasperated), throwing up both hands, while @Khang listens with the mouth closed.
- 12–13s (Shot 3): @Quan keeps talking, leaning a little toward @Khang.
- 13–14s (Shot 3): @Quan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Khang gives a small sympathetic shrug and walks away down the corridor. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, pressing): "Vậy bao giờ cô ấy nhớ lại? Tuần sau tôi có việc quan trọng cần cô ấy ký giấy."
- Turn 2, 5.7–10.7s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking at a natural, even conversational pace, polite and immovable): "Giấy tờ thì chưa ký được đâu. Về pháp lý, chị ấy đang là cô gái hai mươi hai tuổi."
- Turn 3, 11.2–13.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, exasperated): "Thế tôi là cái gì trong chuyện này? Chồng của ai đây?"
- Pacing: @Quan speaks at an even everyday pace, then @Khang answers at an even everyday pace, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft beep of a bedside monitor, a quiet air conditioner, distant hospital footsteps, birds outside the window. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 1 (`canh-04/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A bright private VIP hospital room by day: a white adjustable hospital bed with crisp sheets, a bedside monitor showing only soft wave lines, a vase of white lilies, a large window with sheer curtains over the city, a pale-wood visitor chair.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; pale-blue cotton hospital gown under a soft white knit cardigan.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the doctor, locked off.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the doctor onto the elegant wife, gentle handheld drift.
- Shot 3, 10–13s: 50mm medium shot of the doctor with the bright hospital room softly behind, slow dolly-in.
- Shot 4, 13–15s: 24mm wide shot of the bright hospital room with the doctor and the elegant wife, subtle rack focus.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang is closing the door softly behind him and is already speaking at an easy conversational pace (dry deadpan).
- 1–2s (Shot 1): @Khang keeps talking, folding his arms.
- 2–3s (Shot 1): @Khang keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Khang keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Khang finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking quickly (grinning, delighted), sitting bolt upright with a dazzling grin, while @Khang listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, fluffing her long hair.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Khang.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Khang starts speaking slowly and softly (half amused), shaking his head with a tiny smile, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Khang keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Khang finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh pats the edge of the bed, inviting him to sit.
- 14–15s (Shot 4): @Khang sighs and sits down beside the bed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking at a natural, even conversational pace, dry deadpan): "Anh ấy đi rồi. Cậu mở mắt ra được rồi đấy, diễn viên xuất sắc nhất năm."
- Turn 2, 5.2–9.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, grinning, delighted): "Tớ diễn thế nào? Lúc ngất ở sảnh có đẹp không? Tớ tập trước ở nhà ba lần đấy!"
- Turn 3, 9.7–13.1s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking slowly and softly, unhurried, with a short natural pause between phrases, half amused): "Đẹp. Nhưng tớ là bác sĩ, không phải đồng phạm đâu nhé."
- Pacing: @Khang speaks at an even everyday pace, then @Linh answers quickly, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft beep of a bedside monitor, a door clicking shut, a quiet air conditioner, birds outside the window. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 2 (`canh-04/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A bright private VIP hospital room by day: a white adjustable hospital bed with crisp sheets, a bedside monitor showing only soft wave lines, a vase of white lilies, a large window with sheer curtains over the city, a pale-wood visitor chair.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; pale-blue cotton hospital gown under a soft white knit cardigan.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm over-the-shoulder shot from behind the doctor onto the elegant wife, gentle handheld drift.
- Shot 2, 6–10s: 85mm close-up of the doctor, slow dolly-in.
- Shot 3, 10–15s: 35mm medium two-shot of the elegant wife and the doctor, subtle rack focus.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is dropping her smile and twisting the blanket in her fingers and is already speaking at an easy conversational pace (serious now).
- 1–2s (Shot 1): @Linh keeps talking, looking down at her wedding ring.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Khang.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Linh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Khang starts speaking at an easy conversational pace (gentle), leaning forward with his elbows on his knees, while @Linh listens with the mouth closed.
- 7–8s (Shot 2): @Khang keeps talking, watching her face.
- 8–9s (Shot 2): @Khang keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Khang finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking slowly and softly (steady, eyes shining), lifting her chin, while @Khang listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, blinking back a shine of tears.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @Khang.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Khang studies her for a long moment, then gives one slow nod. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, serious now): "Khang, hôm qua tớ thấy tận mắt rồi. Anh ấy định ly hôn tớ ngay sau ngày kỷ niệm."
- Turn 2, 5.7–9.2s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking at a natural, even conversational pace, gentle): "Thế sao cậu không làm ầm lên? Cậu có đủ bằng chứng cơ mà."
- Turn 3, 9.7–14.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, steady, eyes shining): "Làm ầm thì mất chồng. Diễn thì còn được xem anh ấy thật lòng đến đâu."
- Pacing: @Linh speaks at an even everyday pace, then @Khang answers at an even everyday pace, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft beep of a bedside monitor, a door clicking shut, a quiet air conditioner, birds outside the window. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 3 (`canh-04/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A bright private VIP hospital room by day: a white adjustable hospital bed with crisp sheets, a bedside monitor showing only soft wave lines, a vase of white lilies, a large window with sheer curtains over the city, a pale-wood visitor chair.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; pale-blue cotton hospital gown under a soft white knit cardigan.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium two-shot of the elegant wife and the doctor, slow dolly-in.
- Shot 2, 6–10s: 85mm close-up of the doctor, subtle rack focus.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the doctor onto the elegant wife, slow arc.
- Shot 4, 13–15s: 24mm wide shot of the bright hospital room with the elegant wife and the doctor, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is counting on her fingers with a sly smile and is already speaking at an easy conversational pace (mischievous).
- 1–2s (Shot 1): @Linh keeps talking, wiggling her eyebrows.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Khang.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Linh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Khang starts speaking quickly (skeptical), raising both palms, while @Linh listens with the mouth closed.
- 7–8s (Shot 2): @Khang keeps talking, tilting his head.
- 8–9s (Shot 2): @Khang keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Khang finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking slowly and softly (quiet resolve), shrugging lightly, while @Khang listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Khang takes off his glasses and polishes them slowly on his coat.
- 14–15s (Shot 4): @Linh holds out her pinky finger toward him, waiting. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, mischievous): "Mười năm trước anh ấy tán tớ ba năm mới đổ. Giờ tớ muốn anh ấy tán lại từ đầu."
- Turn 2, 5.9–9.3s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking quickly in short lively phrases, every word still clear, skeptical): "Thế nhỡ anh ta không thèm tán, mà chạy sang với cô kia luôn thì sao?"
- Turn 3, 9.8–13.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet resolve): "Thì tớ biết sớm, đỡ phí thêm mười năm nữa, cậu ạ."
- Pacing: @Linh speaks at an even everyday pace, then @Khang answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft beep of a bedside monitor, a door clicking shut, a quiet air conditioner, birds outside the window. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 4 (`canh-04/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A bright private VIP hospital room by day: a white adjustable hospital bed with crisp sheets, a bedside monitor showing only soft wave lines, a vase of white lilies, a large window with sheer curtains over the city, a pale-wood visitor chair.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; pale-blue cotton hospital gown under a soft white knit cardigan.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the doctor with the bright hospital room softly behind, subtle rack focus.
- Shot 2, 5–9s: 85mm close-up of the elegant wife, slow arc.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the elegant wife onto the doctor, slow push-in.
- Shot 4, 13–15s: 24mm wide shot of the bright hospital room with the doctor and the elegant wife, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang is hooking his pinky around hers with a sigh and is already speaking at an easy conversational pace (resigned).
- 1–2s (Shot 1): @Khang keeps talking, putting his glasses back on.
- 2–3s (Shot 1): @Khang keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Khang keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Khang finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking quickly (gleeful), ticking items off on her fingers, while @Khang listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, beaming.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Khang.
- 8–9s (Shot 2): @Linh finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Khang starts speaking slowly and softly (dry deadpan), writing slowly on the blank folder, while @Linh listens with the mouth closed.
- 10–11s (Shot 3): @Khang keeps talking, holding @Linh's gaze.
- 11–12s (Shot 3): @Khang keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Khang finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh flops back onto the pillows and closes her eyes like a perfect patient.
- 14–15s (Shot 4): @Khang shakes his head, smiling, and walks to the door. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking at a natural, even conversational pace, resigned): "Được rồi. Bệnh án ghi mất trí nhớ có chọn lọc. Cậu định chọn lọc những gì?"
- Turn 2, 5.2–9.0s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, gleeful): "Nhớ con gái, nhớ mật khẩu thẻ ngân hàng, và nhớ rất rõ chồng nợ tớ những gì!"
- Turn 3, 9.5–12.9s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking slowly and softly, unhurried, with a short natural pause between phrases, dry deadpan): "Và chỉ quên đúng mỗi một người. Phụ nữ đáng sợ thật."
- Pacing: @Khang speaks at an even everyday pace, then @Linh answers quickly, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft beep of a bedside monitor, a door clicking shut, a quiet air conditioner, birds outside the window. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 1 (`canh-05/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa in the evening: double-height glass walls onto a garden, a long cream sofa, a walnut coffee table, a large abstract painting, warm amber floor lamps, a floating staircase with glass rails.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.
- @Bong = Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; yellow cotton dress with a white Peter Pan collar, white socks, small red shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the little girl, slow arc.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the little girl onto the elegant wife, slow push-in.
- Shot 3, 10–15s: 35mm medium two-shot of the little girl and the elegant wife, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bong is running across the living room into her mother's open arms and is already speaking quickly (overjoyed).
- 1–2s (Shot 1): @Bong keeps talking, looking up with huge sparkling eyes.
- 2–3s (Shot 1): @Bong keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Bong keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Bong finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking slowly and softly (warm and tender), kneeling to hold her daughter close, while @Bong listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, touching the tip of her nose.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Bong.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Bong starts speaking quickly (excited, curious), tilting her head to one side, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Bong keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Bong keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @Bong finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh glances toward the front door, her smile turning cool. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking quickly in short lively phrases, every word still clear, overjoyed): "Mẹ ơi! Mẹ về rồi! Bố bảo mẹ bị ốm, quên hết mọi thứ, mẹ có nhớ con không?"
- Turn 2, 5.1–9.6s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, warm and tender): "Nhớ chứ. Bống của mẹ, thích sữa dâu, sợ sâu róm, ngủ phải ôm thỏ bông."
- Turn 3, 10.1–13.7s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking quickly in short lively phrases, every word still clear, excited, curious): "Đúng hết luôn! Thế còn bố thì sao? Mẹ có nhớ bố là ai không ạ?"
- Pacing: @Bong speaks quickly, then @Linh answers slowly and calmly, then @Bong answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the hush of a big quiet house, a door closing softly, wind in the garden trees, the faint hum of the city. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 2 (`canh-05/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa in the evening: double-height glass walls onto a garden, a long cream sofa, a walnut coffee table, a large abstract painting, warm amber floor lamps, a floating staircase with glass rails.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the husband, locked off.
- Shot 3, 10–13s: 50mm medium shot of the elegant wife with the villa living room softly behind, gentle handheld drift.
- Shot 4, 13–15s: 24mm wide shot of the villa living room with the elegant wife and the husband, slow dolly-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is pointing politely at the floor by the door and is already speaking at an easy conversational pace (polite as to a stranger).
- 1–2s (Shot 1): @Linh keeps talking, offering a small gracious nod.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking quickly (outraged), setting down the little suitcase with a thump, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, gesturing at the glass walls and staircase.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking slowly and softly (sweetly cutting), running a fingertip along the walnut table, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh walks past him toward the glass staircase without looking back.
- 14–15s (Shot 4): @Quan stands holding nothing, mouth half open. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, polite as to a stranger): "Anh ơi, anh để vali ở đấy được rồi. Cảm ơn anh tài xế nhé, anh về đi."
- Turn 2, 5.4–9.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, outraged): "Tài xế nào? Đây là nhà anh! Anh xây cái nhà này, anh chọn từng viên gạch đấy!"
- Turn 3, 9.7–13.1s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, sweetly cutting): "Thế à? Gu chọn gạch đẹp đấy. Chọn người thì chưa chắc."
- Pacing: @Linh speaks at an even everyday pace, then @Quan answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the hush of a big quiet house, a door closing softly, wind in the garden trees, the faint hum of the city. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 3 (`canh-05/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa in the evening: double-height glass walls onto a garden, a long cream sofa, a walnut coffee table, a large abstract painting, warm amber floor lamps, a floating staircase with glass rails.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Bong = Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; yellow cotton dress with a white Peter Pan collar, white socks, small red shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 35mm medium two-shot of the little girl and the husband, locked off.
- Shot 2, 7–10s: 85mm close-up of the husband, gentle handheld drift.
- Shot 3, 10–15s: 35mm medium two-shot of the little girl and the husband, slow dolly-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bong is tugging at the sleeve of her father's jacket and is already speaking at an easy conversational pace (innocent and puzzled).
- 1–2s (Shot 1): @Bong keeps talking, counting on her small fingers.
- 2–3s (Shot 1): @Bong keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Bong keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Bong keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Bong keeps talking, never looking away from @Quan.
- 6–7s (Shot 1): @Bong finishes the line and closes the mouth.
- 7–8s (CUT to Shot 2): @Quan starts speaking slowly and softly (hollow), crouching down to her height, while @Bong listens with the mouth closed.
- 8–9s (Shot 2): @Quan keeps talking, lowering his eyes.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Bong starts speaking quickly (eager), climbing onto the cream sofa beside him, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @Bong keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Bong keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Bong finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan opens his mouth, closes it, and looks away toward the dark garden. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.2s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking at a natural, even conversational pace, innocent and puzzled): "Bố ơi, sao mẹ nhớ con, nhớ cả bà ngoại, nhớ cả con mèo nhà hàng xóm, mà lại quên mỗi bố?"
- Turn 2, 6.7–9.5s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, hollow): "Bác sĩ bảo mẹ quên những gì làm mẹ buồn."
- Turn 3, 10.0–13.3s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking quickly in short lively phrases, every word still clear, eager): "Thế bố làm mẹ buồn à? Bố làm gì thế, bố kể con nghe đi!"
- Pacing: @Bong speaks at an even everyday pace, then @Quan answers slowly and calmly, then @Bong answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the hush of a big quiet house, a door closing softly, wind in the garden trees, the faint hum of the city. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 4 (`canh-05/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa in the evening: double-height glass walls onto a garden, a long cream sofa, a walnut coffee table, a large abstract painting, warm amber floor lamps, a floating staircase with glass rails.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the elegant wife with the villa living room softly behind, gentle handheld drift.
- Shot 2, 5–9s: 85mm close-up of the husband, slow dolly-in.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, subtle rack focus.
- Shot 4, 13–15s: 24mm wide shot of the villa living room with the elegant wife and the husband, slow arc.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is leaning over the glass rail of the staircase and is already speaking quickly (breezy and bright).
- 1–2s (Shot 1): @Linh keeps talking, waving her fingers down at him.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking quickly (spluttering), hurrying to the foot of the stairs, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, jabbing a finger upward.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Quan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Linh starts speaking slowly and softly (sweet and final), tossing a cushion down the stairs to him, while @Quan listens with the mouth closed.
- 10–11s (Shot 3): @Linh keeps talking, holding @Quan's gaze.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Quan catches the cushion against his chest.
- 14–15s (Shot 4): @Quan looks from the cushion to the long cream sofa and sighs. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, breezy and bright): "Anh gì ơi, phòng ngủ lớn trên tầng hai tôi lấy nhé. Anh ngủ phòng khách cho tiện."
- Turn 2, 4.7–8.3s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, spluttering): "Đấy là phòng của hai vợ chồng mình! Giường ấy em đòi mua mãi mới được đấy!"
- Turn 3, 8.8–12.5s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, sweet and final): "Thì đúng rồi. Gu của tôi mà. Chúc anh ngủ ngon trên sofa."
- Pacing: @Linh speaks quickly, then @Quan answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the hush of a big quiet house, a door closing softly, wind in the garden trees, the faint hum of the city. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 1 (`canh-06/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The bright modern kitchen of the villa in the morning: a white marble island with tall stools, matte sage-green cabinets, copper pendant lamps, a bowl of lemons, a large window onto the sunny garden.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; oversized pastel-yellow hoodie, short pleated white tennis skirt over light leggings, chunky white sneakers, a pink scrunchie on the wrist.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; rumpled grey T-shirt and navy pajama trousers, barefoot.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 85mm close-up of the elegant wife, slow dolly-in.
- Shot 2, 4–9s: 50mm over-the-shoulder shot from behind the elegant wife onto the husband, subtle rack focus.
- Shot 3, 9–13s: 50mm medium shot of the elegant wife with the sunny villa kitchen softly behind, slow arc.
- Shot 4, 13–15s: 24mm wide shot of the sunny villa kitchen with the elegant wife and the husband, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is perched on a tall stool at the marble island sipping milk and is already speaking quickly (chirpy morning voice).
- 1–2s (Shot 1): @Linh keeps talking, pointing her spoon at the fridge.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh finishes the line and closes the mouth.
- 4–5s (CUT to Shot 2): @Quan starts speaking at an easy conversational pace (groggy, disbelieving), shuffling in with bed-flattened hair and a sofa cushion crease on his cheek, while @Linh listens with the mouth closed.
- 5–6s (Shot 2): @Quan keeps talking, squinting at the pastel sheet on the fridge.
- 6–7s (Shot 2): @Quan keeps talking, one hand moving lightly with the words.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Quan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Linh starts speaking quickly (delighted), clapping her hands once, while @Quan listens with the mouth closed.
- 10–11s (Shot 3): @Linh keeps talking, giving him a thumbs-up.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Quan slowly turns from the fridge to stare at her.
- 14–15s (Shot 4): @Linh swings her sneakers under the stool and keeps sipping her milk. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.0s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, chirpy morning voice): "Chào buổi sáng, anh hàng xóm! Tôi dán nội quy lên tủ lạnh rồi, anh đọc chưa?"
- Turn 2, 4.5–8.8s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, groggy, disbelieving): "Điều một: không gọi em là vợ. Điều hai: muốn ăn sáng chung thì phải hẹn trước?"
- Turn 3, 9.3–12.5s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, delighted): "Chuẩn! Điều ba: muốn làm chồng thì phải tán lại từ đầu, đúng quy trình!"
- Pacing: @Linh speaks quickly, then @Quan answers at an even everyday pace, then @Linh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong from the garden, a kettle softly boiling, a spoon tapping a cup, the hum of a fridge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 2 (`canh-06/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The bright modern kitchen of the villa in the morning: a white marble island with tall stools, matte sage-green cabinets, copper pendant lamps, a bowl of lemons, a large window onto the sunny garden.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; oversized pastel-yellow hoodie, short pleated white tennis skirt over light leggings, chunky white sneakers, a pink scrunchie on the wrist.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; rumpled grey T-shirt and navy pajama trousers, barefoot.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the elegant wife onto the husband, subtle rack focus.
- Shot 2, 5–9s: 85mm close-up of the elegant wife, slow arc.
- Shot 3, 9–13s: 50mm medium shot of the husband with the sunny villa kitchen softly behind, slow push-in.
- Shot 4, 13–15s: 24mm wide shot of the sunny villa kitchen with the husband and the elegant wife, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is planting both palms on the marble island and is already speaking quickly (exasperated).
- 1–2s (Shot 1): @Quan keeps talking, leaning toward her.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking slowly and softly (innocent and sweet), batting her long lashes, while @Quan listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, sliding off the stool.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Linh finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Quan starts speaking quickly (proud of himself), tapping his temple with one finger, while @Linh listens with the mouth closed.
- 10–11s (Shot 3): @Quan keeps talking, holding @Linh's gaze.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh's smile flickers for a heartbeat, then she skips out of the kitchen.
- 14–15s (Shot 4): @Quan is left alone, frowning at the pastel sheet on the fridge. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, exasperated): "Tán lại? Mười năm trước anh tán em ba năm, giờ em bắt anh làm lại từ đầu à?"
- Turn 2, 4.9–8.8s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, innocent and sweet): "Mười năm trước tôi đâu có quen anh. Anh nhầm với cô nào rồi."
- Turn 3, 9.3–13.1s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, proud of himself): "Nhầm làm sao được! Em uống cà phê đen không đường, ăn phở không hành, anh thuộc lòng!"
- Pacing: @Quan speaks quickly, then @Linh answers slowly and calmly, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong from the garden, a kettle softly boiling, a spoon tapping a cup, the hum of a fridge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 3 (`canh-06/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Quân's glass-walled CEO office high above the city by day: a long walnut desk, a white leather sofa, shelves of interior-design fabric and wood samples, a panoramic city view, two envelopes on the desk, one blue and one pink.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium two-shot of the husband and the assistant, slow arc.
- Shot 2, 4–9s: 85mm close-up of the assistant, slow push-in.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the assistant onto the husband, locked off.
- Shot 4, 13–15s: 24mm wide shot of the sunny villa kitchen with the husband and the assistant, gentle handheld drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is pacing behind the long walnut desk and is already speaking quickly (beside himself).
- 1–2s (Shot 1): @Quan keeps talking, loosening his collar.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Tuan.
- 3–4s (Shot 1): @Quan finishes the line and closes the mouth.
- 4–5s (CUT to Shot 2): @Tuan starts speaking quickly (cheerfully unhelpful), perched on the white leather sofa with his tablet, while @Quan listens with the mouth closed.
- 5–6s (Shot 2): @Tuan keeps talking, grinning with both dimples.
- 6–7s (Shot 2): @Tuan keeps talking, one hand moving lightly with the words.
- 7–8s (Shot 2): @Tuan keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Tuan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Quan starts speaking slowly and softly (grim), dropping into his desk chair, while @Tuan listens with the mouth closed.
- 10–11s (Shot 3): @Quan keeps talking, holding @Tuan's gaze.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Tuan's grin fades; he scratches his head.
- 14–15s (Shot 4): @Quan swivels his chair to stare out at the city. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.0s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, beside himself): "Tuấn, cô ấy bắt tôi đi theo đuổi lại vợ mình, ngay trong nhà của chính tôi!"
- Turn 2, 4.5–8.7s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, cheerfully unhelpful): "Thế thì anh lợi quá còn gì! Đề thi cũ, đáp án anh thuộc hết rồi, cứ thế mà chép!"
- Turn 3, 9.2–12.3s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, grim): "Đáp án mười năm trước. Giờ cô ấy đổi đề rồi."
- Pacing: @Quan speaks quickly, then @Tuan answers quickly, then @Quan answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong from the garden, a kettle softly boiling, a spoon tapping a cup, the hum of a fridge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 4 (`canh-06/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Quân's glass-walled CEO office high above the city by day: a long walnut desk, a white leather sofa, shelves of interior-design fabric and wood samples, a panoramic city view, two envelopes on the desk, one blue and one pink.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the assistant with the sunny villa kitchen softly behind, slow push-in.
- Shot 2, 6–10s: 85mm close-up of the husband, locked off.
- Shot 3, 10–15s: 35mm medium two-shot of the assistant and the husband, gentle handheld drift.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tuan is leaning across the desk and is already speaking at an easy conversational pace (lowering his voice).
- 1–2s (Shot 1): @Tuan keeps talking, glancing at the glass door.
- 2–3s (Shot 1): @Tuan keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Tuan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Tuan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Tuan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Quan starts speaking slowly and softly (quiet, surprised at himself), turning his wedding ring slowly on his finger, while @Tuan listens with the mouth closed.
- 7–8s (Shot 2): @Quan keeps talking, looking out at the skyline.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Tuan starts speaking quickly (teasing), throwing up both hands, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @Tuan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Tuan keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Tuan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan doesn't laugh; he keeps turning the ring. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking at a natural, even conversational pace, lowering his voice): "Hay là anh nhân lúc chị ấy quên, chia tay luôn cho gọn? Cô Mai Anh đang đợi đấy."
- Turn 2, 5.7–9.9s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, surprised at himself): "Lúc cô ấy nhìn tôi như người lạ, tự nhiên tôi thấy khó chịu lắm."
- Turn 3, 10.4–13.4s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, teasing): "Ôi giời, anh ghen với chính anh à? Cái này thì em chịu thật!"
- Pacing: @Tuan speaks at an even everyday pace, then @Quan answers slowly and calmly, then @Tuan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong from the garden, a kettle softly boiling, a spoon tapping a cup, the hum of a fridge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 1 (`canh-07/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor by day: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, floor-to-ceiling windows with soft white daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; lilac long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet.
- Wardrobe: in this shot @MaiAnh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young yoga teacher, locked off.
- Shot 2, 5–11s: 50mm over-the-shoulder shot from behind the young yoga teacher onto the husband, gentle handheld drift.
- Shot 3, 11–15s: 35mm medium two-shot of the young yoga teacher and the husband, slow dolly-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is rolling up a lilac yoga mat and is already speaking quickly (eager).
- 1–2s (Shot 1): @MaiAnh keeps talking, tossing her glossy hair.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking at an easy conversational pace (weary), standing by the window with his hands in his pockets, while @MaiAnh listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, rubbing his tired eyes.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @MaiAnh.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Quan finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @MaiAnh starts speaking quickly (pushy and sweet), hopping up and patting his lapel, while @Quan listens with the mouth closed.
- 12–13s (Shot 3): @MaiAnh keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan gives a thin smile that does not reach his eyes. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.0s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, eager): "Vợ anh mất trí nhớ thì càng tốt chứ sao! Anh cứ đưa giấy ly hôn cho chị ấy ký là xong."
- Turn 2, 5.5–10.8s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, weary): "Bác sĩ bảo về pháp lý cô ấy chưa ký được gì. Mà cô ấy còn chẳng nhận mình có chồng."
- Turn 3, 11.3–14.1s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, pushy and sweet): "Thì anh cứ thử đi! Đưa luôn tối nay, em đợi tin anh!"
- Pacing: @MaiAnh speaks quickly, then @Quan answers at an even everyday pace, then @MaiAnh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft city noise through the windows, bare feet on wood, a water bottle cap clicking, a ceiling fan turning. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 2 (`canh-07/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor by day: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, floor-to-ceiling windows with soft white daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; lilac long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet.
- Wardrobe: in this shot @MaiAnh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm over-the-shoulder shot from behind the husband onto the young yoga teacher, gentle handheld drift.
- Shot 2, 6–9s: 85mm close-up of the husband, slow dolly-in.
- Shot 3, 9–15s: 35mm medium two-shot of the young yoga teacher and the husband, subtle rack focus.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is sitting on the mat hugging her knees and is already speaking at an easy conversational pace (sulky).
- 1–2s (Shot 1): @MaiAnh keeps talking, pouting at the mirror.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Quan starts speaking quickly (defensive), checking his watch, while @MaiAnh listens with the mouth closed.
- 7–8s (Shot 2): @Quan keeps talking, turning toward the door.
- 8–9s (Shot 2): @Quan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @MaiAnh starts speaking slowly and softly (cool and knowing), rising to her feet, while @Quan listens with the mouth closed.
- 10–11s (Shot 3): @MaiAnh keeps talking, folding her arms.
- 11–12s (Shot 3): @MaiAnh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @MaiAnh keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan freezes with one hand on the door handle. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, sulky): "Anh hứa với em ly thân hai năm rồi cơ mà. Sao giờ anh cứ chần chừ mãi thế?"
- Turn 2, 5.7–8.9s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, defensive): "Anh không chần chừ! Anh chỉ đang tính toán cho thật chu đáo thôi em."
- Turn 3, 9.4–13.3s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking slowly and softly, unhurried, with a short natural pause between phrases, cool and knowing): "Đàn ông tính toán lâu quá thường là đang tính đường lui đấy anh."
- Pacing: @MaiAnh speaks at an even everyday pace, then @Quan answers quickly, then @MaiAnh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft city noise through the windows, bare feet on wood, a water bottle cap clicking, a ceiling fan turning. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 3 (`canh-07/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor by day: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, floor-to-ceiling windows with soft white daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; lilac long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
- Wardrobe: in this shot @MaiAnh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of the young yoga teacher and the assistant, slow dolly-in.
- Shot 2, 5–10s: 85mm close-up of the assistant, subtle rack focus.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the assistant onto the young yoga teacher, slow arc.
- Shot 4, 13–15s: 24mm wide shot of the airy yoga studio with the young yoga teacher and the assistant, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is blocking the doorway with a sweet smile and is already speaking at an easy conversational pace (sugary interrogation).
- 1–2s (Shot 1): @MaiAnh keeps talking, fluttering her lashes.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Tuan.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Tuan starts speaking quickly (lying badly), hugging his tablet like a shield, while @MaiAnh listens with the mouth closed.
- 6–7s (Shot 2): @Tuan keeps talking, waving one hand dismissively.
- 7–8s (Shot 2): @Tuan keeps talking, leaning a little toward @MaiAnh.
- 8–9s (Shot 2): @Tuan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Tuan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @MaiAnh starts speaking quickly (incredulous), planting her hands on her hips, while @Tuan listens with the mouth closed.
- 11–12s (Shot 3): @MaiAnh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Tuan opens his mouth, shuts it, and stares at the ceiling fan.
- 14–15s (Shot 4): @MaiAnh narrows her big doe eyes at him. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, sugary interrogation): "Anh Tuấn, nói thật với em đi. Vợ anh Quân trông thế nào? Có đẹp bằng em không?"
- Turn 2, 5.4–9.2s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, lying badly): "Chị ấy á? Bình thường thôi! Ngày xưa đi thi hoa khôi, nhưng chỉ được giải nhất thôi."
- Turn 3, 9.7–12.9s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, incredulous): "Giải nhất mà anh bảo bình thường à? Anh có biết nói dối không đấy?"
- Pacing: @MaiAnh speaks at an even everyday pace, then @Tuan answers quickly, then @MaiAnh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft city noise through the windows, bare feet on wood, a water bottle cap clicking, a ceiling fan turning. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 4 (`canh-07/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor by day: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, floor-to-ceiling windows with soft white daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; lilac long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
- Wardrobe: in this shot @MaiAnh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the assistant with the airy yoga studio softly behind, subtle rack focus.
- Shot 2, 6–10s: 85mm close-up of the young yoga teacher, slow arc.
- Shot 3, 10–15s: 35mm medium two-shot of the assistant and the young yoga teacher, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tuan is lowering his voice and leaning in and is already speaking at an easy conversational pace (earnest warning).
- 1–2s (Shot 1): @Tuan keeps talking, shaking his head slowly.
- 2–3s (Shot 1): @Tuan keeps talking, leaning a little toward @MaiAnh.
- 3–4s (Shot 1): @Tuan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Tuan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Tuan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @MaiAnh starts speaking slowly and softly (determined), turning to study herself in the long mirror, while @Tuan listens with the mouth closed.
- 7–8s (Shot 2): @MaiAnh keeps talking, lifting her chin.
- 8–9s (Shot 2): @MaiAnh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @MaiAnh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Tuan starts speaking quickly (panicking), clapping a palm over his own mouth, while @MaiAnh listens with the mouth closed.
- 11–12s (Shot 3): @Tuan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Tuan keeps talking, leaning a little toward @MaiAnh.
- 13–14s (Shot 3): @Tuan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Tuan backs out of the studio, bowing apologetically. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking at a natural, even conversational pace, earnest warning): "Em khuyên thật, cô đừng tìm gặp chị ấy. Đứng cạnh chị ấy, ai cũng thành người qua đường."
- Turn 2, 5.7–9.9s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking slowly and softly, unhurried, with a short natural pause between phrases, determined): "Càng nói em càng tò mò. Em phải tận mắt xem người đó thế nào."
- Turn 3, 10.4–13.6s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, panicking): "Thôi chết, em lại lỡ mồm rồi. Anh Quân mà biết thì em mất việc!"
- Pacing: @Tuan speaks at an even everyday pace, then @MaiAnh answers slowly and calmly, then @Tuan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft city noise through the windows, bare feet on wood, a water bottle cap clicking, a ceiling fan turning. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 1 (`canh-08/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa in the evening: double-height glass walls onto a garden, a long cream sofa, a walnut coffee table, a large abstract painting, warm amber floor lamps, a floating staircase with glass rails.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; oversized pastel-yellow hoodie, short pleated white tennis skirt over light leggings, chunky white sneakers, a pink scrunchie on the wrist.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the husband, slow arc.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, slow push-in.
- Shot 3, 10–13s: 50mm medium shot of the husband with the villa living room softly behind, locked off.
- Shot 4, 13–15s: 24mm wide shot of the villa living room with the husband and the elegant wife, gentle handheld drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is sliding a white sheet and a fountain pen across the walnut table and is already speaking at an easy conversational pace (too casual).
- 1–2s (Shot 1): @Quan keeps talking, giving a small cough.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking at an easy conversational pace (reading, then indignant), curled on the cream sofa, holding the sheet up to the lamp, while @Quan listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, lowering it with wide eyes.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Quan starts speaking quickly (flustered), picking up a framed wedding photo from the shelf, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Quan keeps talking, holding it out to her.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh leans in and studies the photo very seriously.
- 14–15s (Shot 4): @Quan waits, holding the frame with both hands. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, too casual): "Em ký giúp anh tờ giấy này được không? Giấy tờ hành chính thôi mà."
- Turn 2, 4.7–9.5s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, reading, then indignant): "Đơn ly hôn? Tôi đã lấy ai đâu mà ly hôn. Anh định lừa con gái nhà lành à?"
- Turn 3, 10.0–12.8s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, flustered): "Không phải lừa! Mình lấy nhau thật mà, có cả ảnh cưới đây!"
- Pacing: @Quan speaks at an even everyday pace, then @Linh answers at an even everyday pace, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the hush of the house at night, paper rustling and folding, wind in the garden trees, a clock ticking softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 2 (`canh-08/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa in the evening: double-height glass walls onto a garden, a long cream sofa, a walnut coffee table, a large abstract painting, warm amber floor lamps, a floating staircase with glass rails.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; oversized pastel-yellow hoodie, short pleated white tennis skirt over light leggings, chunky white sneakers, a pink scrunchie on the wrist.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the husband, locked off.
- Shot 3, 10–13s: 50mm medium shot of the elegant wife with the villa living room softly behind, gentle handheld drift.
- Shot 4, 13–15s: 24mm wide shot of the villa living room with the elegant wife and the husband, slow dolly-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is holding up her phone as if to dial and is already speaking quickly (mock alarmed).
- 1–2s (Shot 1): @Linh keeps talking, scooting away to the far end of the sofa.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking quickly (wounded), pressing the frame to his chest, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, pointing at the photo.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking slowly and softly (soft and pointed), looking from the photo to the white sheet, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Quan lowers the frame slowly.
- 14–15s (Shot 4): @Quan's shoulders drop; he cannot meet her eyes. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, mock alarmed): "Ảnh này chỉnh sửa khéo đấy. Anh còn ghép mặt tôi vào nữa, tôi gọi công an bây giờ!"
- Turn 2, 4.9–9.1s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, wounded): "Ghép cái gì! Hôm ấy em khóc ướt cả vai áo anh, em bảo cả đời chỉ yêu mình anh!"
- Turn 3, 9.6–13.0s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft and pointed): "Cô ấy nói thế à? Thế mà anh nỡ đưa đơn này."
- Pacing: @Linh speaks quickly, then @Quan answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the hush of the house at night, paper rustling and folding, wind in the garden trees, a clock ticking softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 3 (`canh-08/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa in the evening: double-height glass walls onto a garden, a long cream sofa, a walnut coffee table, a large abstract painting, warm amber floor lamps, a floating staircase with glass rails.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; oversized pastel-yellow hoodie, short pleated white tennis skirt over light leggings, chunky white sneakers, a pink scrunchie on the wrist.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of the husband and the elegant wife, locked off.
- Shot 2, 5–10s: 85mm close-up of the elegant wife, gentle handheld drift.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the elegant wife onto the husband, slow dolly-in.
- Shot 4, 13–15s: 24mm wide shot of the villa living room with the husband and the elegant wife, subtle rack focus.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is sitting heavily on the arm of the sofa and is already speaking slowly and softly (caught out).
- 1–2s (Shot 1): @Quan keeps talking, staring at his hands.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking at an easy conversational pace (breezy), folding the white sheet in half with neat quick creases, while @Quan listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, running a thumbnail along each fold.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Quan starts speaking quickly (aghast), reaching out a hand too late, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh keeps folding, humming, completely calm.
- 14–15s (Shot 4): @Quan watches the sheet become smaller and smaller. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.1s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, caught out): "Anh không định thế đâu. Chỉ là dạo này anh mệt mỏi quá."
- Turn 2, 4.6–9.6s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, breezy): "Mệt thì nghỉ. Tờ giấy này để tôi gấp thuyền cho Bống chơi, giấy đẹp, dày, gấp chắc tay lắm."
- Turn 3, 10.1–13.1s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, aghast): "Em ơi, đấy là đơn ly hôn! Luật sư soạn mất ba ngày đấy!"
- Pacing: @Quan speaks slowly and calmly, then @Linh answers at an even everyday pace, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the hush of the house at night, paper rustling and folding, wind in the garden trees, a clock ticking softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 4 (`canh-08/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa in the evening: double-height glass walls onto a garden, a long cream sofa, a walnut coffee table, a large abstract painting, warm amber floor lamps, a floating staircase with glass rails.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; oversized pastel-yellow hoodie, short pleated white tennis skirt over light leggings, chunky white sneakers, a pink scrunchie on the wrist.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the elegant wife with the villa living room softly behind, gentle handheld drift.
- Shot 2, 5–9s: 85mm close-up of the husband, slow dolly-in.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, subtle rack focus.
- Shot 4, 13–15s: 24mm wide shot of the villa living room with the elegant wife and the husband, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is holding up a perfect little paper boat and is already speaking quickly (proud of her work).
- 1–2s (Shot 1): @Linh keeps talking, sailing it through the air.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking slowly and softly (a reluctant smile), watching her hands with a soft, faraway look, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, one hand moving lightly with the words.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Quan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Linh starts speaking at an easy conversational pace (covering quickly), biting her lip, then lifting her chin, while @Quan listens with the mouth closed.
- 10–11s (Shot 3): @Linh keeps talking, holding @Quan's gaze.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh hops up and hurries to the staircase, the paper boat in her hand.
- 14–15s (Shot 4): @Quan stays on the sofa arm, a slow puzzled smile spreading. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, proud of her work): "Xong! Thuyền đẹp chưa? Mai tôi mang ra hồ thả cho nó trôi thật xa, khỏi ai tìm thấy."
- Turn 2, 4.9–8.6s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, a reluctant smile): "Mười năm rồi, em vẫn gấp thuyền khéo y như hồi sinh viên."
- Turn 3, 9.1–12.6s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, covering quickly): "Hồi sinh viên? Sao anh biết? Anh theo dõi tôi từ hồi ấy à?"
- Pacing: @Linh speaks quickly, then @Quan answers slowly and calmly, then @Linh answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the hush of the house at night, paper rustling and folding, wind in the garden trees, a clock ticking softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 1 (`canh-09/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A cosy lakeside street-food corner at night: low plastic stools and a small steel table with bowls of bún chả, a charcoal grill with rising smoke, strings of yellow bulbs, reflections dancing on the dark water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; pastel-pink cropped cardigan over a white cotton sundress, white sneakers, a small pearl hair clip.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; white polo shirt, beige chinos, white leather sneakers.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 85mm close-up of the husband, slow dolly-in.
- Shot 2, 6–10s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, subtle rack focus.
- Shot 3, 10–15s: 35mm medium two-shot of the husband and the elegant wife, slow arc.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is sitting on a tiny plastic stool, knees up near his chin and is already speaking at an easy conversational pace (proud and nostalgic).
- 1–2s (Shot 1): @Quan keeps talking, sliding a glass of black coffee toward her.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Linh starts speaking slowly and softly (flat), nudging the coffee glass back toward him with one finger, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Quan starts speaking quickly (baffled), holding up two fingers, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Quan keeps talking, looking from the glass to her face.
- 12–13s (Shot 3): @Quan keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @Quan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh looks out at the dark lake, silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, proud and nostalgic): "Đây là quán đầu tiên anh đưa em đi. Em gọi bún chả, cà phê đen không đường, đúng không?"
- Turn 2, 5.9–9.3s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, flat): "Cà phê đen à? Tôi ghét cà phê đen nhất trên đời."
- Turn 3, 9.8–14.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, baffled): "Sao lại ghét? Mười năm nay sáng nào em cũng pha hai cốc, một cốc cho anh, một cốc cho em!"
- Pacing: @Quan speaks at an even everyday pace, then @Linh answers slowly and calmly, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal sizzling on the grill, motorbikes passing slowly, laughter from far away, gentle water lapping at the lake edge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 2 (`canh-09/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A cosy lakeside street-food corner at night: low plastic stools and a small steel table with bowls of bún chả, a charcoal grill with rising smoke, strings of yellow bulbs, reflections dancing on the dark water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; pastel-pink cropped cardigan over a white cotton sundress, white sneakers, a small pearl hair clip.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; white polo shirt, beige chinos, white leather sneakers.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, subtle rack focus.
- Shot 2, 6–11s: 85mm close-up of the husband, slow arc.
- Shot 3, 11–15s: 35mm medium two-shot of the elegant wife and the husband, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is tracing a finger around the rim of the glass and is already speaking slowly and softly (quiet, far away).
- 1–2s (Shot 1): @Linh keeps talking, watching the bulbs reflected in the lake.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Linh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Quan starts speaking slowly and softly (stunned), leaning forward on his little stool, while @Linh listens with the mouth closed.
- 7–8s (Shot 2): @Quan keeps talking, searching her face.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Quan finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Linh starts speaking quickly (snapping back to bright), waving brightly toward the stall, while @Quan listens with the mouth closed.
- 12–13s (Shot 3): @Linh keeps talking, flashing a big fake smile.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan keeps staring at her, the bún chả forgotten. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.0s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, far away): "Có lẽ vì ngày xưa có người thích cà phê đen, nên cô ấy uống cùng cho có đôi thôi."
- Turn 2, 6.5–10.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, stunned): "Em mười năm uống thứ mình ghét, chỉ vì anh thích thôi à?"
- Turn 3, 10.7–14.1s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, snapping back to bright): "Tôi nói cô ấy chứ! Tôi thì gọi trà sữa trân châu, full topping, ít đá!"
- Pacing: @Linh speaks slowly and calmly, then @Quan answers slowly and calmly, then @Linh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal sizzling on the grill, motorbikes passing slowly, laughter from far away, gentle water lapping at the lake edge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 3 (`canh-09/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A cosy lakeside street-food corner at night: low plastic stools and a small steel table with bowls of bún chả, a charcoal grill with rising smoke, strings of yellow bulbs, reflections dancing on the dark water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; pastel-pink cropped cardigan over a white cotton sundress, white sneakers, a small pearl hair clip.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; white polo shirt, beige chinos, white leather sneakers.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium two-shot of the husband and the elegant wife, slow arc.
- Shot 2, 6–11s: 85mm close-up of the elegant wife, slow push-in.
- Shot 3, 11–15s: 35mm medium two-shot of the husband and the elegant wife, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is taking out his phone and opening a blank note and is already speaking at an easy conversational pace (sincere).
- 1–2s (Shot 1): @Quan keeps talking, holding his thumb ready.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Linh starts speaking quickly (counting, merciless), counting on her fingers, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @Linh keeps talking, folding down the last finger with a pointed look.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Linh finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Quan starts speaking slowly and softly (wincing), slowly putting the phone face-down on the table, while @Linh listens with the mouth closed.
- 12–13s (Shot 3): @Quan keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @Quan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh hides a smile behind her cup of milk tea. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, sincere): "Thế em còn ghét những gì nữa? Em kể đi, anh muốn biết, lần này anh ghi nhớ hết."
- Turn 2, 5.7–10.1s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, counting, merciless): "Ghét hành, ghét mưa phùn, ghét đàn ông nghe điện thoại ngoài ban công rồi bảo là gọi cho đối tác."
- Turn 3, 10.6–13.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, wincing): "Cái cuối cùng ấy, anh ghi nhớ kỹ rồi, em ạ."
- Pacing: @Quan speaks at an even everyday pace, then @Linh answers quickly, then @Quan answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal sizzling on the grill, motorbikes passing slowly, laughter from far away, gentle water lapping at the lake edge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 4 (`canh-09/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A cosy lakeside street-food corner at night: low plastic stools and a small steel table with bowls of bún chả, a charcoal grill with rising smoke, strings of yellow bulbs, reflections dancing on the dark water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; pastel-pink cropped cardigan over a white cotton sundress, white sneakers, a small pearl hair clip.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; white polo shirt, beige chinos, white leather sneakers.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the elegant wife with the lakeside food stall softly behind, slow push-in.
- Shot 2, 5–9s: 85mm close-up of the husband, locked off.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, gentle handheld drift.
- Shot 4, 13–15s: 24mm wide shot of the lakeside food stall with the elegant wife and the husband, slow dolly-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is dipping a piece of grilled pork into the sauce and is already speaking at an easy conversational pace (grudging).
- 1–2s (Shot 1): @Linh keeps talking, chewing with closed eyes.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking quickly (hopeful), leaning in eagerly, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, rubbing his palms together.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Quan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Linh starts speaking slowly and softly (hiding a smile), holding up five fingers, while @Quan listens with the mouth closed.
- 10–11s (Shot 3): @Linh keeps talking, holding @Quan's gaze.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Quan grins like a schoolboy and holds up five fingers back at her.
- 14–15s (Shot 4): @Linh rolls her eyes and looks away at the lake, smiling. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, grudging): "Nhưng mà công nhận, bún chả quán này ngon thật. Anh dẫn gái cũng có gu đấy."
- Turn 2, 5.2–8.6s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, hopeful): "Thế buổi hẹn hôm nay được mấy điểm? Có được hẹn lần thứ hai không em?"
- Turn 3, 9.1–13.0s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, hiding a smile): "Năm điểm thôi. Trừ năm điểm vì cái tội đến muộn mất mười năm."
- Pacing: @Linh speaks at an even everyday pace, then @Quan answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal sizzling on the grill, motorbikes passing slowly, laughter from far away, gentle water lapping at the lake edge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 1 (`canh-10/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa by day: double-height glass walls onto a sunny garden, a long cream sofa, a walnut coffee table, a large abstract painting, a floating staircase with glass rails, bright soft daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; oversized pastel-yellow hoodie, short pleated white tennis skirt over light leggings, chunky white sneakers, a pink scrunchie on the wrist.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the doctor, locked off.
- Shot 2, 5–9s: 50mm over-the-shoulder shot from behind the doctor onto the elegant wife, gentle handheld drift.
- Shot 3, 9–13s: 50mm medium shot of the doctor with the sunlit villa living room softly behind, slow dolly-in.
- Shot 4, 13–15s: 24mm wide shot of the sunlit villa living room with the doctor and the elegant wife, subtle rack focus.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang is sitting beside her on the sofa holding up a family photo and is already speaking at an easy conversational pace (professional, a little loud).
- 1–2s (Shot 1): @Khang keeps talking, tapping the photo.
- 2–3s (Shot 1): @Khang keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Khang keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Khang finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking quickly (loud and flirty on purpose), fluttering her lashes theatrically, while @Khang listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, twirling a strand of hair.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Khang.
- 8–9s (Shot 2): @Linh finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Khang starts speaking slowly and softly (hushed deadpan), keeping his eyes on the photo, while @Linh listens with the mouth closed.
- 10–11s (Shot 3): @Khang keeps talking, barely moving his lips.
- 11–12s (Shot 3): @Khang keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Khang finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh glances sideways toward the glass staircase and beams even wider.
- 14–15s (Shot 4): @Khang gives a small cough and shuffles the photos. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking at a natural, even conversational pace, professional, a little loud): "Hôm nay mình tập phục hồi trí nhớ. Em nhìn ảnh này, có nhớ ra ai không?"
- Turn 2, 5.2–9.0s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, loud and flirty on purpose): "Không nhớ ai cả. Nhưng bác sĩ đẹp trai thế này thì em nhớ ngay từ lần đầu!"
- Turn 3, 9.5–12.9s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking slowly and softly, unhurried, with a short natural pause between phrases, hushed deadpan): "Diễn vừa thôi. Anh ấy đang đứng ở cầu thang nghe đấy."
- Pacing: @Khang speaks at an even everyday pace, then @Linh answers quickly, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong from the sunny garden, a clock ticking, photographs shuffling, soft footsteps on the stairs. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 2 (`canh-10/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa by day: double-height glass walls onto a sunny garden, a long cream sofa, a walnut coffee table, a large abstract painting, a floating staircase with glass rails, bright soft daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; oversized pastel-yellow hoodie, short pleated white tennis skirt over light leggings, chunky white sneakers, a pink scrunchie on the wrist.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the elegant wife onto the husband, gentle handheld drift.
- Shot 2, 5–10s: 85mm close-up of the elegant wife, slow dolly-in.
- Shot 3, 10–13s: 50mm medium shot of the husband with the sunlit villa living room softly behind, subtle rack focus.
- Shot 4, 13–15s: 24mm wide shot of the sunlit villa living room with the husband and the elegant wife, slow arc.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is marching down the glass staircase and is already speaking quickly (jealous).
- 1–2s (Shot 1): @Quan keeps talking, pointing at the gap on the sofa.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking at an easy conversational pace (wide-eyed innocence), standing up and crossing her arms, while @Quan listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, tilting her head sweetly.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Quan starts speaking quickly (indignant), jabbing a thumb at his own chest, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh blinks at him, then turns and pats the sofa cushion where the doctor sits.
- 14–15s (Shot 4): @Quan's jaw tightens. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, jealous): "Bác sĩ khám bệnh gì mà phải ngồi sát thế? Em ra đây, anh có chuyện cần nói!"
- Turn 2, 4.7–9.5s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, wide-eyed innocence): "Anh hàng xóm lại ghen à? Bác sĩ Khang độc thân, tôi cũng độc thân, có gì sai đâu?"
- Turn 3, 10.0–13.0s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, indignant): "Sai hết! Em có chồng rồi, chồng em đang đứng sờ sờ ở đây!"
- Pacing: @Quan speaks quickly, then @Linh answers at an even everyday pace, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong from the sunny garden, a clock ticking, photographs shuffling, soft footsteps on the stairs. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 3 (`canh-10/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa by day: double-height glass walls onto a sunny garden, a long cream sofa, a walnut coffee table, a large abstract painting, a floating staircase with glass rails, bright soft daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium two-shot of the husband and the doctor, slow dolly-in.
- Shot 2, 4–9s: 85mm close-up of the doctor, subtle rack focus.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the doctor onto the husband, slow arc.
- Shot 4, 13–15s: 24mm wide shot of the sunlit villa living room with the husband and the doctor, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is standing over the coffee table with his hands on his hips and is already speaking at an easy conversational pace (cold and polite).
- 1–2s (Shot 1): @Quan keeps talking, staring down at the doctor.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Khang.
- 3–4s (Shot 1): @Quan finishes the line and closes the mouth.
- 4–5s (CUT to Shot 2): @Khang starts speaking at an easy conversational pace (unruffled), calmly packing photos into his bag, while @Quan listens with the mouth closed.
- 5–6s (Shot 2): @Khang keeps talking, looking up over his rimless glasses.
- 6–7s (Shot 2): @Khang keeps talking, one hand moving lightly with the words.
- 7–8s (Shot 2): @Khang keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Khang finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Quan starts speaking quickly (stubborn), hauling an armchair right up to the coffee table and sitting down hard, while @Khang listens with the mouth closed.
- 10–11s (Shot 3): @Quan keeps talking, holding @Khang's gaze.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Khang raises his eyebrows and closes his bag.
- 14–15s (Shot 4): @Quan folds his arms and does not blink. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, cold and polite): "Bác sĩ, anh đến chữa bệnh hay đến làm tình địch của tôi?"
- Turn 2, 4.2–8.7s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking at a natural, even conversational pace, unruffled): "Trong bệnh án, chị ấy hai mươi hai tuổi, chưa chồng. Tôi cũng chưa vợ. Anh nghĩ sao?"
- Turn 3, 9.2–12.4s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, stubborn): "Tôi nghĩ là từ mai, buổi tập nào tôi cũng ngồi ngay đây mà xem!"
- Pacing: @Quan speaks at an even everyday pace, then @Khang answers at an even everyday pace, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong from the sunny garden, a clock ticking, photographs shuffling, soft footsteps on the stairs. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 4 (`canh-10/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa by day: double-height glass walls onto a sunny garden, a long cream sofa, a walnut coffee table, a large abstract painting, a floating staircase with glass rails, bright soft daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the doctor with the sunlit villa living room softly behind, subtle rack focus.
- Shot 2, 6–9s: 85mm close-up of the husband, slow arc.
- Shot 3, 9–15s: 35mm medium two-shot of the doctor and the husband, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang is standing and slinging his bag over his shoulder and is already speaking at an easy conversational pace (mild).
- 1–2s (Shot 1): @Khang keeps talking, nodding politely.
- 2–3s (Shot 1): @Khang keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Khang keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Khang keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Khang finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Quan starts speaking quickly (suspicious), rising from the armchair, while @Khang listens with the mouth closed.
- 7–8s (Shot 2): @Quan keeps talking, narrowing his eyes.
- 8–9s (Shot 2): @Quan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Khang starts speaking at an easy conversational pace (quiet and level), pausing at the door, while @Quan listens with the mouth closed.
- 10–11s (Shot 3): @Khang keeps talking, glancing back.
- 11–12s (Shot 3): @Khang keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Khang keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Khang finishes the line and closes the mouth.
- 14–15s (Shot 3): @Khang leaves; the door clicks shut. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking at a natural, even conversational pace, mild): "Tốt. Người nhà ở bên cạnh, bệnh nhân hồi phục nhanh hơn. Nhưng phải là người nhà tử tế."
- Turn 2, 5.7–8.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, suspicious): "Anh nói thế là có ý gì? Anh biết chuyện gì về tôi à?"
- Turn 3, 9.2–14.0s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking at a natural, even conversational pace, quiet and level): "Tôi chỉ biết bệnh nhân. Người bị tổn thương thì không cần nhớ, cơ thể vẫn tự biết sợ."
- Pacing: @Khang speaks at an even everyday pace, then @Quan answers quickly, then @Khang answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong from the sunny garden, a clock ticking, photographs shuffling, soft footsteps on the stairs. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 1 (`canh-11/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor by day: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, floor-to-ceiling windows with soft white daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; sage-green long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; lilac long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet.
- Wardrobe: in this shot @Linh and @MaiAnh wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 85mm close-up of the young yoga teacher, slow arc.
- Shot 2, 6–11s: 50mm over-the-shoulder shot from behind the young yoga teacher onto the elegant wife, slow push-in.
- Shot 3, 11–15s: 35mm medium two-shot of the young yoga teacher and the elegant wife, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is walking over with a rolled lilac mat and is already speaking at an easy conversational pace (warm and professional).
- 1–2s (Shot 1): @MaiAnh keeps talking, looking her up and down admiringly.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Linh starts speaking quickly (bubbly), bouncing on her bare toes, while @MaiAnh listens with the mouth closed.
- 7–8s (Shot 2): @Linh keeps talking, flashing a dazzling smile.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Linh finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @MaiAnh starts speaking at an easy conversational pace (puzzled smile), unrolling the mat beside her own, while @Linh listens with the mouth closed.
- 12–13s (Shot 3): @MaiAnh keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh sits cross-legged on the mat and closes her eyes like a model student. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, warm and professional): "Chào chị, chị mới đến lớp lần đầu ạ? Chị dáng đẹp thế này, tập yoga chắc nhanh lên trình lắm."
- Turn 2, 6.2–10.6s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, bubbly): "Gọi em là em thôi, em mới hai mươi hai! Bác sĩ bảo em tập yoga cho đầu óc thư thái."
- Turn 3, 11.1–14.1s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, puzzled smile): "Hai mươi hai ạ? Vâng, vậy em trải thảm ở đây nhé."
- Pacing: @MaiAnh speaks at an even everyday pace, then @Linh answers quickly, then @MaiAnh answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft city noise through the windows, slow breathing, bare feet on wood, the creak of a yoga mat. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 2 (`canh-11/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor by day: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, floor-to-ceiling windows with soft white daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; sage-green long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; lilac long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet.
- Wardrobe: in this shot @Linh and @MaiAnh wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm over-the-shoulder shot from behind the young yoga teacher onto the elegant wife, slow push-in.
- Shot 2, 6–10s: 85mm close-up of the young yoga teacher, locked off.
- Shot 3, 10–15s: 35mm medium two-shot of the elegant wife and the young yoga teacher, gentle handheld drift.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is holding a seated twist and is already speaking at an easy conversational pace (confiding, sly).
- 1–2s (Shot 1): @Linh keeps talking, peeking at the teacher over one shoulder.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @MaiAnh.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Linh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @MaiAnh starts speaking quickly (scandalised), dropping out of her pose, while @Linh listens with the mouth closed.
- 7–8s (Shot 2): @MaiAnh keeps talking, leaning in eagerly.
- 8–9s (Shot 2): @MaiAnh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @MaiAnh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking slowly and softly (innocent), unwinding slowly from the twist, while @MaiAnh listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @MaiAnh.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @MaiAnh's smile stiffens; she blinks twice. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.9s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, confiding, sly): "Chị ơi, em hỏi chuyện riêng tí. Có một anh cứ nhận là chồng em, theo chị em có nên tin không?"
- Turn 2, 6.4–10.0s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, scandalised): "Trời ơi, đàn ông bây giờ ghê thật! Anh ta có tiền không? Có đẹp trai không?"
- Turn 3, 10.5–14.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, innocent): "Có tiền, đẹp trai. Mỗi tội hay đi họp với đối tác Nhật."
- Pacing: @Linh speaks at an even everyday pace, then @MaiAnh answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft city noise through the windows, slow breathing, bare feet on wood, the creak of a yoga mat. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 3 (`canh-11/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor by day: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, floor-to-ceiling windows with soft white daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; sage-green long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; lilac long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet.
- Wardrobe: in this shot @Linh and @MaiAnh wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of the young yoga teacher and the elegant wife, locked off.
- Shot 2, 5–9s: 85mm close-up of the elegant wife, gentle handheld drift.
- Shot 3, 9–15s: 35mm medium two-shot of the young yoga teacher and the elegant wife, slow dolly-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is fiddling with the edge of her mat and is already speaking at an easy conversational pace (careful, uneasy).
- 1–2s (Shot 1): @MaiAnh keeps talking, avoiding the mirror.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking quickly (chirpy), propping her chin on her hand, while @MaiAnh listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, smiling sweetly.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @MaiAnh.
- 8–9s (Shot 2): @Linh finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @MaiAnh starts speaking slowly and softly (unsure), hugging her knees, while @Linh listens with the mouth closed.
- 10–11s (Shot 3): @MaiAnh keeps talking, looking down.
- 11–12s (Shot 3): @MaiAnh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @MaiAnh keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh nods slowly, saying nothing. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, careful, uneasy): "Nghe quen quen nhỉ. Người yêu chị cũng có một đống cuộc họp buổi tối như thế."
- Turn 2, 5.2–8.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, chirpy): "Thế à? Thế anh ấy có vợ chưa hả chị? Chắc là chưa đâu nhỉ?"
- Turn 3, 8.9–14.2s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking slowly and softly, unhurried, with a short natural pause between phrases, unsure): "Có, nhưng hai người ly thân hai năm nay rồi. Ít ra thì anh ấy bảo với chị thế."
- Pacing: @MaiAnh speaks at an even everyday pace, then @Linh answers quickly, then @MaiAnh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft city noise through the windows, slow breathing, bare feet on wood, the creak of a yoga mat. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 4 (`canh-11/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor by day: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, floor-to-ceiling windows with soft white daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; sage-green long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; lilac long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet.
- Wardrobe: in this shot @Linh and @MaiAnh wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the elegant wife with the airy yoga studio softly behind, gentle handheld drift.
- Shot 2, 6–10s: 85mm close-up of the young yoga teacher, slow dolly-in.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the young yoga teacher onto the elegant wife, subtle rack focus.
- Shot 4, 13–15s: 24mm wide shot of the airy yoga studio with the elegant wife and the young yoga teacher, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is rising into a graceful standing stretch and is already speaking at an easy conversational pace (gentle).
- 1–2s (Shot 1): @Linh keeps talking, watching her in the mirror.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @MaiAnh.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Linh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @MaiAnh starts speaking quickly (alarmed), scrambling to her feet, while @Linh listens with the mouth closed.
- 7–8s (Shot 2): @MaiAnh keeps talking, staring at her.
- 8–9s (Shot 2): @MaiAnh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @MaiAnh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking quickly (bright again), laughing lightly, while @MaiAnh listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, rolling her shoulders.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh raises both arms into a perfect tree pose, smiling at the mirror.
- 14–15s (Shot 4): @MaiAnh stands frozen beside her, mouth slightly open. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, gentle): "Ly thân mà tối nào cũng về nhà ăn cơm, sáng nào cũng đưa con đi học thì lạ chị nhỉ?"
- Turn 2, 6.2–9.2s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, alarmed): "Sao em biết? Em nói như thể em biết anh ấy là ai ấy!"
- Turn 3, 9.7–12.9s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, bright again): "Em đoán bừa thôi mà! Phim truyền hình toàn thế. Mình tập tiếp đi chị!"
- Pacing: @Linh speaks at an even everyday pace, then @MaiAnh answers quickly, then @Linh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft city noise through the windows, slow breathing, bare feet on wood, the creak of a yoga mat. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 1 (`canh-12/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A chic quiet café overlooking a green city lake in the afternoon: a marble round table with two cups of tea, rattan chairs, big windows onto the green lake, a glass pastry display, warm golden daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 85mm close-up of the young yoga teacher, slow dolly-in.
- Shot 2, 7–11s: 50mm over-the-shoulder shot from behind the young yoga teacher onto the elegant wife, subtle rack focus.
- Shot 3, 11–15s: 35mm medium two-shot of the young yoga teacher and the elegant wife, slow arc.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is stirring honey into her tea and is already speaking at an easy conversational pace (open-hearted).
- 1–2s (Shot 1): @MaiAnh keeps talking, smiling shyly.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @MaiAnh keeps talking, never looking away from @Linh.
- 6–7s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 7–8s (CUT to Shot 2): @Linh starts speaking slowly and softly (gently probing), setting down her cup, while @MaiAnh listens with the mouth closed.
- 8–9s (Shot 2): @Linh keeps talking, watching her steadily.
- 9–10s (Shot 2): @Linh keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Linh finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @MaiAnh starts speaking quickly (defensive), sitting up straight, while @Linh listens with the mouth closed.
- 12–13s (Shot 3): @MaiAnh keeps talking, waving her teaspoon.
- 13–14s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh nods slowly and looks out at the green lake. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.2s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, open-hearted): "Kể ra cũng lạ, mới quen mà chị thấy em như em gái. Chị chưa kể chuyện anh ấy với ai bao giờ."
- Turn 2, 6.7–10.6s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, gently probing): "Chị yêu anh ấy thật à? Hay yêu cái căn hộ anh ấy hứa?"
- Turn 3, 11.1–14.1s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, defensive): "Yêu thật chứ! Căn hộ là anh ấy tự hứa, chị có đòi đâu!"
- Pacing: @MaiAnh speaks at an even everyday pace, then @Linh answers slowly and calmly, then @MaiAnh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft café chatter far away, cups clinking on saucers, a milk steamer hissing, birds over the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 2 (`canh-12/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A chic quiet café overlooking a green city lake in the afternoon: a marble round table with two cups of tea, rattan chairs, big windows onto the green lake, a glass pastry display, warm golden daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm over-the-shoulder shot from behind the young yoga teacher onto the elegant wife, subtle rack focus.
- Shot 2, 6–10s: 85mm close-up of the young yoga teacher, slow arc.
- Shot 3, 10–13s: 50mm medium shot of the elegant wife with the lakeside café softly behind, slow push-in.
- Shot 4, 13–15s: 24mm wide shot of the lakeside café with the elegant wife and the young yoga teacher, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is turning her phone over on the marble table and is already speaking at an easy conversational pace (calm, laying it out).
- 1–2s (Shot 1): @Linh keeps talking, sliding it gently across.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @MaiAnh.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Linh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @MaiAnh starts speaking quickly (suspicious), leaning back sharply in the rattan chair, while @Linh listens with the mouth closed.
- 7–8s (Shot 2): @MaiAnh keeps talking, eyes flicking to the phone.
- 8–9s (Shot 2): @MaiAnh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @MaiAnh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking slowly and softly (very quiet), meeting her eyes without blinking, while @MaiAnh listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @MaiAnh looks down at the glowing phone wallpaper of a smiling family.
- 14–15s (Shot 4): @MaiAnh's hand drifts up to cover her mouth. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.9s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, calm, laying it out): "Chị biết tiền mua căn hộ ấy ở đâu ra không? Tiền vợ anh ấy bán nhà mẹ đẻ góp vốn đấy."
- Turn 2, 6.4–9.6s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, suspicious): "Sao em biết chuyện ấy? Chuyện ấy cả công ty còn chẳng mấy ai biết!"
- Turn 3, 10.1–13.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, very quiet): "Vì người bán căn nhà đó chính là em, chị ạ."
- Pacing: @Linh speaks at an even everyday pace, then @MaiAnh answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft café chatter far away, cups clinking on saucers, a milk steamer hissing, birds over the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 3 (`canh-12/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A chic quiet café overlooking a green city lake in the afternoon: a marble round table with two cups of tea, rattan chairs, big windows onto the green lake, a glass pastry display, warm golden daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of the young yoga teacher and the elegant wife, slow arc.
- Shot 2, 5–9s: 85mm close-up of the elegant wife, slow push-in.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the elegant wife onto the young yoga teacher, locked off.
- Shot 4, 13–15s: 24mm wide shot of the lakeside café with the young yoga teacher and the elegant wife, gentle handheld drift.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is staring from the phone to her face and is already speaking slowly and softly (frozen whisper).
- 1–2s (Shot 1): @MaiAnh keeps talking, barely breathing.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking at an easy conversational pace (calm smile), taking a slow sip of tea, while @MaiAnh listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, setting the cup down without a sound.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @MaiAnh.
- 8–9s (Shot 2): @Linh finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @MaiAnh starts speaking quickly (tangled in panic), shrinking back in her chair, while @Linh listens with the mouth closed.
- 10–11s (Shot 3): @MaiAnh keeps talking, holding up both palms.
- 11–12s (Shot 3): @MaiAnh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh lets the silence stretch, then smiles kindly.
- 14–15s (Shot 4): @MaiAnh slowly lowers her hands. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.1s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking slowly and softly, unhurried, with a short natural pause between phrases, frozen whisper): "Em là vợ anh Quân? Thế còn chuyện mất trí nhớ thì sao?"
- Turn 2, 4.6–8.9s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, calm smile): "Mất trí nhớ có chọn lọc thôi chị. Cái gì cần nhớ thì em nhớ rất kỹ."
- Turn 3, 9.4–13.2s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, tangled in panic): "Chị à không, em à thôi, chị! Chị định làm gì em? Hắt nước vào mặt em à?"
- Pacing: @MaiAnh speaks slowly and calmly, then @Linh answers at an even everyday pace, then @MaiAnh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft café chatter far away, cups clinking on saucers, a milk steamer hissing, birds over the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 4 (`canh-12/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A chic quiet café overlooking a green city lake in the afternoon: a marble round table with two cups of tea, rattan chairs, big windows onto the green lake, a glass pastry display, warm golden daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the elegant wife with the lakeside café softly behind, slow push-in.
- Shot 2, 5–9s: 85mm close-up of the young yoga teacher, locked off.
- Shot 3, 9–15s: 35mm medium two-shot of the elegant wife and the young yoga teacher, gentle handheld drift.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is refilling the other woman's cup and is already speaking slowly and softly (kind but firm).
- 1–2s (Shot 1): @Linh keeps talking, sliding it back toward her.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @MaiAnh.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @MaiAnh starts speaking at an easy conversational pace (shaky), wrapping both hands around the warm cup, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @MaiAnh keeps talking, eyes glistening.
- 7–8s (Shot 2): @MaiAnh keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @MaiAnh finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Linh starts speaking slowly and softly (plain and gentle), resting her chin on one hand, while @MaiAnh listens with the mouth closed.
- 10–11s (Shot 3): @Linh keeps talking, holding @MaiAnh's gaze.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @MaiAnh.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @MaiAnh lets out a small broken laugh and wipes one eye. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, kind but firm): "Phí trà lắm em. Chị chỉ hỏi một câu: em có muốn biết sự thật không?"
- Turn 2, 5.4–8.9s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, shaky): "Sự thật là anh ấy chưa bao giờ ly thân với chị, đúng không?"
- Turn 3, 9.4–13.9s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, plain and gentle): "Tuần trước anh ấy còn nhờ chị xoa bóp vai, kêu đau lưng vì họp nhiều."
- Pacing: @Linh speaks slowly and calmly, then @MaiAnh answers at an even everyday pace, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft café chatter far away, cups clinking on saucers, a milk steamer hissing, birds over the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 1 (`canh-13/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A chic quiet café overlooking a green city lake in the afternoon: a marble round table with two cups of tea, rattan chairs, big windows onto the green lake, a glass pastry display, warm golden daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young yoga teacher, locked off.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the young yoga teacher onto the elegant wife, gentle handheld drift.
- Shot 3, 10–15s: 35mm medium two-shot of the young yoga teacher and the elegant wife, slow dolly-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is crumpling the napkin in her hand and is already speaking quickly (hurt, rushing).
- 1–2s (Shot 1): @MaiAnh keeps talking, shaking her head.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking slowly and softly (dry), raising her cup in a tiny toast, while @MaiAnh listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, deadpan.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @MaiAnh.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @MaiAnh starts speaking quickly (laughing through tears), burying her face in her hands, then peeking out, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @MaiAnh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @MaiAnh keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh laughs softly despite herself. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, hurt, rushing): "Hai năm! Hai năm anh ấy bảo em chờ, bảo vợ anh ấy lạnh lùng, không hiểu anh ấy!"
- Turn 2, 4.9–9.7s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, dry): "Chị lạnh lùng thật. Mỗi tội là lạnh lùng nấu cơm, lạnh lùng đưa con đi học."
- Turn 3, 10.2–13.4s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, laughing through tears): "Thế mà em cứ tưởng mình là nữ chính. Hóa ra em là vai phụ!"
- Pacing: @MaiAnh speaks quickly, then @Linh answers slowly and calmly, then @MaiAnh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft café chatter far away, cups clinking on saucers, a light breeze rattling the window, birds over the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 2 (`canh-13/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A chic quiet café overlooking a green city lake in the afternoon: a marble round table with two cups of tea, rattan chairs, big windows onto the green lake, a glass pastry display, warm golden daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the young yoga teacher onto the elegant wife, gentle handheld drift.
- Shot 2, 5–10s: 85mm close-up of the young yoga teacher, slow dolly-in.
- Shot 3, 10–15s: 35mm medium two-shot of the elegant wife and the young yoga teacher, subtle rack focus.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is reaching over to tuck a tissue into her hand and is already speaking at an easy conversational pace (warm).
- 1–2s (Shot 1): @Linh keeps talking, smiling gently.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @MaiAnh.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @MaiAnh starts speaking at an easy conversational pace (wiping her eyes), dabbing under her eyes, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @MaiAnh keeps talking, sniffing.
- 7–8s (Shot 2): @MaiAnh keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @MaiAnh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @MaiAnh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking slowly and softly (sly), leaning back with a slow wicked smile, while @MaiAnh listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @MaiAnh.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @MaiAnh stops dabbing and stares at her. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, warm): "Em chẳng thua ai cả. Chị và em đều bị cùng một người diễn cho xem thôi."
- Turn 2, 5.2–9.2s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, wiping her eyes): "Thế bây giờ chị muốn em làm gì? Biến khỏi cuộc đời anh ấy luôn ạ?"
- Turn 3, 9.7–14.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, sly): "Không vội thế. Em cứ yêu anh ấy tiếp đi. Nhưng mà yêu thật đắt vào."
- Pacing: @Linh speaks at an even everyday pace, then @MaiAnh answers at an even everyday pace, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft café chatter far away, cups clinking on saucers, a light breeze rattling the window, birds over the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 3 (`canh-13/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A chic quiet café overlooking a green city lake in the afternoon: a marble round table with two cups of tea, rattan chairs, big windows onto the green lake, a glass pastry display, warm golden daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium two-shot of the young yoga teacher and the elegant wife, slow dolly-in.
- Shot 2, 4–10s: 85mm close-up of the elegant wife, subtle rack focus.
- Shot 3, 10–12s: 50mm over-the-shoulder shot from behind the elegant wife onto the young yoga teacher, slow arc.
- Shot 4, 12–15s: 24mm wide shot of the lakeside café with the young yoga teacher and the elegant wife, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is leaning across the table and is already speaking quickly (catching on, gleeful).
- 1–2s (Shot 1): @MaiAnh keeps talking, ticking items off on her fingers.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 4–5s (CUT to Shot 2): @Linh starts speaking at an easy conversational pace (plotting), tapping her phone calendar, while @MaiAnh listens with the mouth closed.
- 5–6s (Shot 2): @Linh keeps talking, raising one brow.
- 6–7s (Shot 2): @Linh keeps talking, one hand moving lightly with the words.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @MaiAnh.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @MaiAnh starts speaking quickly (delighted), clapping her hands together, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 12–13s (CUT to Shot 4): @Linh lifts her teacup; @MaiAnh clinks hers against it.
- 13–14s (Shot 4): Both women sip at the same moment, eyes locked, grinning.
- 14–15s (Shot 4): @Linh and @MaiAnh stay silent, mouths closed, as the moment settles. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.6s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, catching on, gleeful): "Đắt là đắt thế nào ạ? Túi hiệu, đồng hồ, du lịch châu Âu ạ?"
- Turn 2, 4.1–9.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, plotting): "Đòi gì cũng được, miễn là đòi đúng lúc chị hẹn anh ấy. Để xem anh ấy chia đôi kiểu gì."
- Turn 3, 9.9–12.2s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, delighted): "Chị ác thật đấy. Nhưng mà em thích, em thích lắm!"
- Pacing: @MaiAnh speaks quickly, then @Linh answers at an even everyday pace, then @MaiAnh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft café chatter far away, cups clinking on saucers, a light breeze rattling the window, birds over the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 4 (`canh-13/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A chic quiet café overlooking a green city lake in the afternoon: a marble round table with two cups of tea, rattan chairs, big windows onto the green lake, a glass pastry display, warm golden daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the elegant wife with the lakeside café softly behind, subtle rack focus.
- Shot 2, 6–10s: 85mm close-up of the young yoga teacher, slow arc.
- Shot 3, 10–15s: 35mm medium two-shot of the elegant wife and the young yoga teacher, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is setting down her cup and is already speaking slowly and softly (serious again).
- 1–2s (Shot 1): @Linh keeps talking, holding her gaze.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @MaiAnh.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Linh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @MaiAnh starts speaking at an easy conversational pace (puzzled), tilting her head, while @Linh listens with the mouth closed.
- 7–8s (Shot 2): @MaiAnh keeps talking, hugging her handbag.
- 8–9s (Shot 2): @MaiAnh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @MaiAnh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking at an easy conversational pace (gentle), standing and smoothing her blouse, while @MaiAnh listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @MaiAnh.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh lays a hand lightly on the young woman's shoulder as she passes. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, serious again): "Còn một điều nữa. Tiền anh ấy chuyển cho em, em cứ giữ lại, đừng tiêu đồng nào."
- Turn 2, 5.9–9.7s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, puzzled): "Giữ lại để làm gì hả chị? Chị định lấy lại số tiền ấy à?"
- Turn 3, 10.2–14.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, gentle): "Để cuối truyện em tự chọn nó thuộc về ai. Người tử tế sẽ biết chọn."
- Pacing: @Linh speaks slowly and calmly, then @MaiAnh answers at an even everyday pace, then @Linh answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft café chatter far away, cups clinking on saucers, a light breeze rattling the window, birds over the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 1 (`canh-14/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Quân's glass-walled CEO office high above the city by day: a long walnut desk, a white leather sofa, shelves of interior-design fabric and wood samples, a panoramic city view, two envelopes on the desk, one blue and one pink.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the assistant, slow arc.
- Shot 2, 5–8s: 50mm over-the-shoulder shot from behind the assistant onto the husband, slow push-in.
- Shot 3, 8–15s: 35mm medium two-shot of the assistant and the husband, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tuan is bursting through the glass door waving his tablet and is already speaking quickly (reporting in a rush).
- 1–2s (Shot 1): @Tuan keeps talking, reading off the screen.
- 2–3s (Shot 1): @Tuan keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Tuan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Tuan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking quickly (aghast), dropping his pen, while @Tuan listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, clutching his forehead.
- 7–8s (Shot 2): @Quan finishes the line and closes the mouth.
- 8–9s (CUT to Shot 3): @Tuan starts speaking slowly and softly (deadpan), patting his boss on the shoulder, while @Quan listens with the mouth closed.
- 9–10s (Shot 3): @Tuan keeps talking, never looking away from @Quan.
- 10–11s (Shot 3): @Tuan keeps talking, holding @Quan's gaze.
- 11–12s (Shot 3): @Tuan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Tuan keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Tuan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan groans and lets his head sink onto the walnut desk. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.0s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, reporting in a rush): "Anh ơi, chị Mai Anh vừa nhắn đòi túi hiệu, còn chị Linh thì đòi anh hát dưới cửa sổ tối nay!"
- Turn 2, 5.5–7.8s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, aghast): "Hát? Tôi hát như vịt đực! Cô ấy biết thừa mà!"
- Turn 3, 8.3–13.3s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking slowly and softly, unhurried, with a short natural pause between phrases, deadpan): "Chị ấy mất trí nhớ rồi mà anh. Biết đâu chị ấy quên luôn là anh hát dở."
- Pacing: @Tuan speaks quickly, then @Quan answers quickly, then @Tuan answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet office hum, a pen scratching on paper, the city far below, a phone buzzing on the desk. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 2 (`canh-14/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Quân's glass-walled CEO office high above the city by day: a long walnut desk, a white leather sofa, shelves of interior-design fabric and wood samples, a panoramic city view, two envelopes on the desk, one blue and one pink.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the assistant onto the husband, slow push-in.
- Shot 2, 5–9s: 85mm close-up of the assistant, locked off.
- Shot 3, 9–13s: 50mm medium shot of the husband with the glass CEO office softly behind, gentle handheld drift.
- Shot 4, 13–15s: 24mm wide shot of the glass CEO office with the husband and the assistant, slow dolly-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is lifting his head and sliding two sheets of letter paper across the desk and is already speaking at an easy conversational pace (scheming).
- 1–2s (Shot 1): @Quan keeps talking, pointing at each sheet.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Tuan.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Tuan starts speaking quickly (aghast), pointing at his own face, while @Quan listens with the mouth closed.
- 6–7s (Shot 2): @Tuan keeps talking, backing away a step.
- 7–8s (Shot 2): @Tuan keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Tuan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Quan starts speaking slowly and softly (solemn), handing him the fountain pen, while @Tuan listens with the mouth closed.
- 10–11s (Shot 3): @Quan keeps talking, holding @Tuan's gaze.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Tuan takes the pen, looks at it, and sighs from the bottom of his soul.
- 14–15s (Shot 4): @Quan leans back in his chair, arms folded. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, scheming): "Tuấn, cậu viết hộ tôi hai bức thư tình. Một cho cô ấy, một cho Mai Anh."
- Turn 2, 5.2–8.6s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, aghast): "Em viết á? Em ế ba mươi lăm năm nay, anh nhờ em viết thư tình?"
- Turn 3, 9.1–13.0s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, solemn): "Thì thế mới cần. Văn của người ế lúc nào cũng tha thiết nhất."
- Pacing: @Quan speaks at an even everyday pace, then @Tuan answers quickly, then @Quan answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet office hum, a pen scratching on paper, the city far below, a phone buzzing on the desk. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 3 (`canh-14/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Quân's glass-walled CEO office high above the city by day: a long walnut desk, a white leather sofa, shelves of interior-design fabric and wood samples, a panoramic city view, two envelopes on the desk, one blue and one pink.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of the assistant and the husband, locked off.
- Shot 2, 5–10s: 85mm close-up of the husband, gentle handheld drift.
- Shot 3, 10–15s: 35mm medium two-shot of the assistant and the husband, slow dolly-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tuan is sitting on the white sofa with paper on his tablet and is already speaking at an easy conversational pace (pen hovering).
- 1–2s (Shot 1): @Tuan keeps talking, chewing the pen cap.
- 2–3s (Shot 1): @Tuan keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Tuan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Tuan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking slowly and softly (suddenly serious), taking one sheet back, while @Tuan listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, uncapping a second pen.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Tuan.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Tuan starts speaking quickly (warning), wagging the pen at him, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @Tuan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Tuan keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Tuan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan bends over the desk and begins to write slowly, carefully. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking at a natural, even conversational pace, pen hovering): "Thư cho chị Linh thì em viết gì hả anh? Viết là anh nhớ hồi xưa à?"
- Turn 2, 5.2–9.4s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, suddenly serious): "Không. Bức ấy để tôi tự tay viết. Cậu lo bức gửi Mai Anh thôi."
- Turn 3, 9.9–13.5s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, warning): "Thế nhớ dán phong bì cẩn thận đấy, nhầm một cái là toi cả hai đấy anh!"
- Pacing: @Tuan speaks at an even everyday pace, then @Quan answers slowly and calmly, then @Tuan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet office hum, a pen scratching on paper, the city far below, a phone buzzing on the desk. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 4 (`canh-14/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Quân's glass-walled CEO office high above the city by day: a long walnut desk, a white leather sofa, shelves of interior-design fabric and wood samples, a panoramic city view, two envelopes on the desk, one blue and one pink.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the husband with the glass CEO office softly behind, gentle handheld drift.
- Shot 2, 5–9s: 85mm close-up of the assistant, slow dolly-in.
- Shot 3, 9–12s: 50mm over-the-shoulder shot from behind the assistant onto the husband, subtle rack focus.
- Shot 4, 12–15s: 24mm wide shot of the glass CEO office with the husband and the assistant, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is sealing the blue envelope and handing over both and is already speaking at an easy conversational pace (brisk).
- 1–2s (Shot 1): @Quan keeps talking, straightening his tie-less collar.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Tuan.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Tuan starts speaking quickly (muttering to himself), juggling the two envelopes from hand to hand, while @Quan listens with the mouth closed.
- 6–7s (Shot 2): @Tuan keeps talking, squinting at them.
- 7–8s (Shot 2): @Tuan keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Tuan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Quan starts speaking quickly (mock stern), pointing at the door, while @Tuan listens with the mouth closed.
- 10–11s (Shot 3): @Quan keeps talking, holding @Tuan's gaze.
- 11–12s (Shot 3): @Quan finishes the line and closes the mouth.
- 12–13s (CUT to Shot 4): @Tuan hurries out holding one envelope in each hand, swapping them twice on the way.
- 13–14s (Shot 4): @Quan stares after him, a terrible suspicion dawning.
- 14–15s (Shot 4): @Quan and @Tuan stay silent, mouths closed, as the moment settles. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, brisk): "Xong rồi. Phong bì xanh cho cô ấy, phong bì hồng cho Mai Anh. Cậu đi giao đi."
- Turn 2, 5.4–8.6s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, muttering to himself): "Xanh cho chị Linh, hồng cho Mai Anh. Xanh, hồng, hay là hồng, xanh nhỉ?"
- Turn 3, 9.1–11.9s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, mock stern): "Cậu mà nhầm là tôi cho cậu đi trông kho cả đời đấy!"
- Pacing: @Quan speaks at an even everyday pace, then @Tuan answers quickly, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 11.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet office hum, a pen scratching on paper, the city far below, a phone buzzing on the desk. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 1 (`canh-15/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa in the evening: double-height glass walls onto a garden, a long cream sofa, a walnut coffee table, a large abstract painting, warm amber floor lamps, a floating staircase with glass rails.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; oversized pastel-yellow hoodie, short pleated white tennis skirt over light leggings, chunky white sneakers, a pink scrunchie on the wrist.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the elegant wife, slow dolly-in.
- Shot 2, 5–9s: 50mm over-the-shoulder shot from behind the elegant wife onto the husband, subtle rack focus.
- Shot 3, 9–13s: 50mm medium shot of the elegant wife with the villa living room softly behind, slow arc.
- Shot 4, 13–15s: 24mm wide shot of the villa living room with the elegant wife and the husband, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is waving an open pink envelope from the sofa and is already speaking quickly (gleeful, sing-song).
- 1–2s (Shot 1): @Linh keeps talking, unfolding the letter with a flourish.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking quickly (panicking), rushing across the room with one hand out, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, stopping dead at the coffee table.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Quan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Linh starts speaking at an easy conversational pace (reading aloud, theatrical), holding the letter high out of reach, while @Quan listens with the mouth closed.
- 10–11s (Shot 3): @Linh keeps talking, pressing a hand to her heart.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Quan stands with his hand still out, face burning red.
- 14–15s (Shot 4): @Linh slowly lowers the letter and looks at him. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, gleeful, sing-song): "Anh hàng xóm ơi, có thư gửi tôi này! Để tôi đọc to nhé: Gửi bé yêu của anh."
- Turn 2, 4.9–8.3s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, panicking): "Khoan đã, đừng đọc! Cái phong bì ấy giao nhầm rồi, em đưa đây cho anh!"
- Turn 3, 8.8–13.1s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, reading aloud, theatrical): "Bé yêu, vợ anh mất trí rồi, chúng mình sắp được tự do. Ôi, văn hay quá!"
- Pacing: @Linh speaks quickly, then @Quan answers quickly, then @Linh answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper rustling, the hush of the house at night, wind in the garden trees, a clock ticking softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 2 (`canh-15/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa in the evening: double-height glass walls onto a garden, a long cream sofa, a walnut coffee table, a large abstract painting, warm amber floor lamps, a floating staircase with glass rails.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; oversized pastel-yellow hoodie, short pleated white tennis skirt over light leggings, chunky white sneakers, a pink scrunchie on the wrist.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, subtle rack focus.
- Shot 2, 6–10s: 85mm close-up of the husband, slow arc.
- Shot 3, 10–15s: 35mm medium two-shot of the elegant wife and the husband, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is folding the letter neatly back into the pink envelope and is already speaking slowly and softly (sweetly cutting).
- 1–2s (Shot 1): @Linh keeps talking, laying it on the table.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Linh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Quan starts speaking at an easy conversational pace (ashamed, honest), sitting down slowly on the sofa arm, while @Linh listens with the mouth closed.
- 7–8s (Shot 2): @Quan keeps talking, staring at the envelope.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking at an easy conversational pace (turning away), standing and walking toward the stairs, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh climbs the glass staircase without looking back. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, sweetly cutting): "Tội nghiệp vợ anh nhỉ. Chị ấy mà đọc được mấy dòng này thì chắc đau lắm."
- Turn 2, 5.7–9.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, ashamed, honest): "Cái thư ấy không phải anh viết. Nhưng những lời ấy, đúng là anh từng nói."
- Turn 3, 10.2–13.7s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, turning away): "Thế thì anh nợ chị ấy một lời xin lỗi. Không phải nợ tôi."
- Pacing: @Linh speaks slowly and calmly, then @Quan answers at an even everyday pace, then @Linh answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper rustling, the hush of the house at night, wind in the garden trees, a clock ticking softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 3 (`canh-15/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor in the evening: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, warm low lamps, floor-to-ceiling windows onto the city lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium two-shot of the young yoga teacher and the elegant wife, slow arc.
- Shot 2, 6–9s: 85mm close-up of the elegant wife, slow push-in.
- Shot 3, 9–15s: 35mm medium two-shot of the young yoga teacher and the elegant wife, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is holding out a blue envelope with both hands and is already speaking at an easy conversational pace (subdued).
- 1–2s (Shot 1): @MaiAnh keeps talking, looking down at it.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Linh starts speaking at an easy conversational pace (careful), taking the envelope slowly, while @MaiAnh listens with the mouth closed.
- 7–8s (Shot 2): @Linh keeps talking, turning it over.
- 8–9s (Shot 2): @Linh finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @MaiAnh starts speaking at an easy conversational pace (moved), sitting down on a rolled mat, while @Linh listens with the mouth closed.
- 10–11s (Shot 3): @MaiAnh keeps talking, pressing her lips together.
- 11–12s (Shot 3): @MaiAnh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @MaiAnh keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh draws out the handwritten letter and unfolds it. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, subdued): "Chị ơi, em nhận được cái này. Phong bì xanh, chữ anh ấy viết tay, mà không phải viết cho em."
- Turn 2, 6.2–8.7s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, careful): "Em đọc rồi à? Thế anh ấy viết những gì?"
- Turn 3, 9.2–14.2s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, moved): "Anh ấy kể chuyện chị bán nhà cho anh ấy mở công ty. Bảo đấy là món nợ cả đời."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper rustling, the hush of the house at night, wind in the garden trees, a clock ticking softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 4 (`canh-15/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor in the evening: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, warm low lamps, floor-to-ceiling windows onto the city lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the young yoga teacher with the villa living room softly behind, slow push-in.
- Shot 2, 6–10s: 85mm close-up of the elegant wife, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the elegant wife onto the young yoga teacher, gentle handheld drift.
- Shot 4, 13–15s: 24mm wide shot of the villa living room with the young yoga teacher and the elegant wife, slow dolly-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is wiping her nose with the back of her hand and is already speaking at an easy conversational pace (rueful smile).
- 1–2s (Shot 1): @MaiAnh keeps talking, laughing at herself.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Linh starts speaking slowly and softly (voice thick), holding the letter against her chest, while @MaiAnh listens with the mouth closed.
- 7–8s (Shot 2): @Linh keeps talking, blinking fast.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @MaiAnh starts speaking quickly (gently teasing), jumping up and picking up her bag, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @MaiAnh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @MaiAnh slips out the door with a little wave.
- 14–15s (Shot 4): @Linh sits down on the mat alone and begins to read again, tears sliding down her cheeks. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, rueful smile): "Thư của em thì toàn câu sáo rỗng, đọc như văn mẫu. Còn thư của chị, em đọc mà khóc."
- Turn 2, 5.9–9.3s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, voice thick): "Mười năm rồi anh ấy mới viết cho chị một lá thư."
- Turn 3, 9.8–13.2s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, gently teasing): "Thế thì chị đọc đi! Em ra ngoài cho chị tha hồ khóc một mình nhé!"
- Pacing: @MaiAnh speaks at an even everyday pace, then @Linh answers slowly and calmly, then @MaiAnh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper rustling, the hush of the house at night, wind in the garden trees, a clock ticking softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 1 (`canh-16/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Bống's pastel bedroom in the villa at night: a small white bed with star-patterned sheets, a soft moon-shaped night lamp, plush toys on a shelf, a reading nook by the window.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; soft lavender silk pajama set with long sleeves and long trousers.
- @Bong = Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; pink star-print long pajamas.
- Wardrobe: in this shot @Linh and @Bong wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 85mm close-up of the little girl, locked off.
- Shot 2, 7–10s: 50mm over-the-shoulder shot from behind the little girl onto the elegant wife, gentle handheld drift.
- Shot 3, 10–15s: 35mm medium two-shot of the little girl and the elegant wife, slow dolly-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bong is sitting up on her little bed hugging her plush rabbit and is already speaking at an easy conversational pace (suspicious detective).
- 1–2s (Shot 1): @Bong keeps talking, narrowing her eyes.
- 2–3s (Shot 1): @Bong keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Bong keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Bong keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Bong keeps talking, never looking away from @Linh.
- 6–7s (Shot 1): @Bong finishes the line and closes the mouth.
- 7–8s (CUT to Shot 2): @Linh starts speaking slowly and softly (caught), freezing halfway through tucking the blanket, while @Bong listens with the mouth closed.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Bong starts speaking quickly (bargaining), holding up one finger, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Bong keeps talking, grinning with her gap teeth.
- 12–13s (Shot 3): @Bong keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @Bong finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh bursts out laughing and covers her face with her hands. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.8s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking at a natural, even conversational pace, suspicious detective): "Mẹ ơi, lúc nãy con thấy mẹ gọi điện cho chú bác sĩ, mẹ cười to lắm. Mẹ giả vờ quên bố đúng không?"
- Turn 2, 7.3–9.3s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, caught): "Bống, con nghe thấy hết rồi à?"
- Turn 3, 9.8–13.8s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking quickly in short lively phrases, every word still clear, bargaining): "Con thông minh mà! Mẹ yên tâm, con không mách bố đâu, nếu mẹ cho con ăn kem!"
- Pacing: @Bong speaks at an even everyday pace, then @Linh answers slowly and calmly, then @Bong answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet night house, crickets in the garden, the rustle of soft blankets, a faint ticking clock. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 2 (`canh-16/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Bống's pastel bedroom in the villa at night: a small white bed with star-patterned sheets, a soft moon-shaped night lamp, plush toys on a shelf, a reading nook by the window.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; soft lavender silk pajama set with long sleeves and long trousers.
- @Bong = Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; pink star-print long pajamas.
- Wardrobe: in this shot @Linh and @Bong wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the little girl onto the elegant wife, gentle handheld drift.
- Shot 2, 5–9s: 85mm close-up of the little girl, slow dolly-in.
- Shot 3, 9–12s: 50mm medium shot of the elegant wife with the little girl's bedroom softly behind, subtle rack focus.
- Shot 4, 12–15s: 24mm wide shot of the little girl's bedroom with the elegant wife and the little girl, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is sitting on the edge of the bed and is already speaking at an easy conversational pace (honest and gentle).
- 1–2s (Shot 1): @Linh keeps talking, smoothing her daughter's bangs.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Bong.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Bong starts speaking quickly (inspired), clasping her hands as if praying, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Bong keeps talking, batting her eyelashes.
- 7–8s (Shot 2): @Bong keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Bong finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Linh starts speaking quickly (laughing), tickling her lightly under the chin, while @Bong listens with the mouth closed.
- 10–11s (Shot 3): @Linh keeps talking, holding @Bong's gaze.
- 11–12s (Shot 3): @Linh finishes the line and closes the mouth.
- 12–13s (CUT to Shot 4): @Bong giggles and flops back onto her pillow.
- 13–14s (Shot 4): @Linh tucks the star blanket around her.
- 14–15s (Shot 4): @Linh and @Bong stay silent, mouths closed, as the moment settles. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, honest and gentle): "Mẹ giả vờ vì mẹ muốn biết bố có còn thương nhà mình thật không. Con hiểu không?"
- Turn 2, 5.4–8.7s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking quickly in short lively phrases, every word still clear, inspired): "Con hiểu! Thế con có được giả vờ mất trí nhớ môn toán không mẹ?"
- Turn 3, 9.2–12.0s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, laughing): "Không được! Môn toán thì phải nhớ, nhớ cả bảng cửu chương nữa!"
- Pacing: @Linh speaks at an even everyday pace, then @Bong answers quickly, then @Linh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet night house, crickets in the garden, the rustle of soft blankets, a faint ticking clock. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 3 (`canh-16/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Bống's pastel bedroom in the villa at night: a small white bed with star-patterned sheets, a soft moon-shaped night lamp, plush toys on a shelf, a reading nook by the window.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; soft lavender silk pajama set with long sleeves and long trousers.
- @Bong = Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; pink star-print long pajamas.
- Wardrobe: in this shot @Linh and @Bong wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium two-shot of the little girl and the elegant wife, slow dolly-in.
- Shot 2, 6–10s: 85mm close-up of the elegant wife, subtle rack focus.
- Shot 3, 10–15s: 35mm medium two-shot of the little girl and the elegant wife, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bong is rubbing her eyes with the back of one hand and is already speaking at an easy conversational pace (earnest, sleepy).
- 1–2s (Shot 1): @Bong keeps talking, yawning.
- 2–3s (Shot 1): @Bong keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Bong keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Bong keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Bong finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Linh starts speaking at an easy conversational pace (softly), lying down beside her on top of the blanket, while @Bong listens with the mouth closed.
- 7–8s (Shot 2): @Linh keeps talking, stroking her hair.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Bong starts speaking at an easy conversational pace (wistful), staring up at the moon lamp, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Bong keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Bong keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @Bong finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh goes very still, her hand resting on the little girl's hair. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking at a natural, even conversational pace, earnest, sleepy): "Mẹ ơi, dạo này bố lạ lắm. Bố tự nấu cơm, còn nhớ con thích sữa dâu nữa."
- Turn 2, 5.7–9.5s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, softly): "Thế à? Thế ngày trước bố có nhớ những chuyện nhỏ như thế không con?"
- Turn 3, 10.0–14.0s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking at a natural, even conversational pace, wistful): "Ngày trước bố toàn mua sữa sô cô la, con uống mà không dám nói."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet night house, crickets in the garden, the rustle of soft blankets, a faint ticking clock. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 4 (`canh-16/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Bống's pastel bedroom in the villa at night: a small white bed with star-patterned sheets, a soft moon-shaped night lamp, plush toys on a shelf, a reading nook by the window.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; soft lavender silk pajama set with long sleeves and long trousers.
- @Bong = Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; pink star-print long pajamas.
- Wardrobe: in this shot @Linh and @Bong wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the elegant wife with the little girl's bedroom softly behind, subtle rack focus.
- Shot 2, 5–10s: 85mm close-up of the little girl, slow arc.
- Shot 3, 10–15s: 35mm medium two-shot of the elegant wife and the little girl, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is gazing at the moon lamp and is already speaking slowly and softly (half to herself).
- 1–2s (Shot 1): @Linh keeps talking, breathing slowly.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Bong.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Bong starts speaking quickly (suddenly wide awake), popping up on one elbow, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Bong keeps talking, holding up one finger, then another.
- 7–8s (Shot 2): @Bong keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Bong keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Bong finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking slowly and softly (tender), hugging her close and laying her back down, while @Bong listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @Bong.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh switches off the moon lamp; only the window light remains. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, half to herself): "Có những người phải suýt mất đi một thứ, mới biết mình đang có gì."
- Turn 2, 5.1–9.1s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking quickly in short lively phrases, every word still clear, suddenly wide awake): "Thế mẹ đừng để bố mất mẹ thật nhé. Con chỉ có một bố với một mẹ thôi!"
- Turn 3, 9.6–13.8s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, tender): "Ngủ đi con gái. Chuyện của người lớn, cứ để mẹ tự lo, con nhé."
- Pacing: @Linh speaks slowly and calmly, then @Bong answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet night house, crickets in the garden, the rustle of soft blankets, a faint ticking clock. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 1 (`canh-17/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The modern kitchen of the villa late at night: a white marble island with tall stools, matte sage-green cabinets, only the warm copper pendant lamps lit, a small pot of rice porridge steaming on the stove, rain streaming down the dark garden window.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; soft lavender silk pajama set with long sleeves and long trousers.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; rumpled grey T-shirt and navy pajama trousers, barefoot.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 85mm close-up of the husband, slow arc.
- Shot 2, 6–9s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, slow push-in.
- Shot 3, 9–15s: 35mm medium two-shot of the husband and the elegant wife, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is stirring a small steaming pot at the stove and is already speaking at an easy conversational pace (soft, a little shy).
- 1–2s (Shot 1): @Quan keeps talking, ladling porridge into a bowl.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Linh starts speaking slowly and softly (quiet), pausing in the doorway in her lavender pajamas, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @Linh keeps talking, breathing in the steam.
- 8–9s (Shot 2): @Linh finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Quan starts speaking slowly and softly (rueful), setting the bowl on the marble island, while @Linh listens with the mouth closed.
- 10–11s (Shot 3): @Quan keeps talking, pulling out a stool for her.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @Quan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh sits down slowly and picks up the spoon. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.9s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, soft, a little shy): "Em chưa ngủ à? Anh nấu cháo gà, hồi xưa mỗi lần em ốm anh hay nấu, à, chắc em không nhớ."
- Turn 2, 6.4–8.9s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet): "Không nhớ. Nhưng sao cái mùi này, quen lắm."
- Turn 3, 9.4–14.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, rueful): "Mười năm nay anh không nấu lần nào. Bận quá, bận đến mức quên cả cách nấu."
- Pacing: @Quan speaks at an even everyday pace, then @Linh answers slowly and calmly, then @Quan answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steady rain on the window, porridge bubbling softly, a spoon against a bowl, distant thunder rolling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 2 (`canh-17/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The modern kitchen of the villa late at night: a white marble island with tall stools, matte sage-green cabinets, only the warm copper pendant lamps lit, a small pot of rice porridge steaming on the stove, rain streaming down the dark garden window.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; soft lavender silk pajama set with long sleeves and long trousers.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; rumpled grey T-shirt and navy pajama trousers, barefoot.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm over-the-shoulder shot from behind the elegant wife onto the husband, slow push-in.
- Shot 2, 6–10s: 85mm close-up of the elegant wife, locked off.
- Shot 3, 10–15s: 50mm medium shot of the husband with the dim villa kitchen softly behind, gentle handheld drift.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is folding his hands on the marble and is already speaking at an easy conversational pace (confessing).
- 1–2s (Shot 1): @Quan keeps talking, staring into the rain on the window.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Linh starts speaking slowly and softly (carefully neutral), stirring her porridge very slowly, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @Linh keeps talking, not looking up.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Quan starts speaking slowly and softly (voice low), rubbing his thumb over his wedding ring, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @Quan keeps talking, taking a quick breath between phrases.
- 14–15s (Shot 3): @Quan finishes the line and closes the mouth. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, confessing): "Anh kể em nghe chuyện này nhé, coi như kể với người lạ. Anh từng có một người vợ rất tốt."
- Turn 2, 6.2–9.9s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, carefully neutral): "Từng có à? Thế bây giờ cô ấy đi đâu rồi hả anh?"
- Turn 3, 10.4–14.3s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, voice low): "Anh làm mất cô ấy, từ trước cả hôm cô ấy ngất ở sảnh."
- Pacing: @Quan speaks at an even everyday pace, then @Linh answers slowly and calmly, then @Quan answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steady rain on the window, porridge bubbling softly, a spoon against a bowl, distant thunder rolling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 3 (`canh-17/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The modern kitchen of the villa late at night: a white marble island with tall stools, matte sage-green cabinets, only the warm copper pendant lamps lit, a small pot of rice porridge steaming on the stove, rain streaming down the dark garden window.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; soft lavender silk pajama set with long sleeves and long trousers.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; rumpled grey T-shirt and navy pajama trousers, barefoot.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of the elegant wife and the husband, locked off.
- Shot 2, 5–10s: 85mm close-up of the husband, gentle handheld drift.
- Shot 3, 10–15s: 35mm medium two-shot of the elegant wife and the husband, slow dolly-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is setting down her spoon and is already speaking at an easy conversational pace (testing him).
- 1–2s (Shot 1): @Linh keeps talking, watching his face.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking at an easy conversational pace (honest, heavy), meeting her eyes at last, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, nodding once.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Linh starts speaking slowly and softly (barely above a whisper), looking down into her bowl, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan looks at her for a long moment, puzzled by how she said it. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, testing him): "Thế còn cô gái trẻ hay gọi điện cho anh lúc nửa đêm thì sao?"
- Turn 2, 4.7–9.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, honest, heavy): "Anh đã nói dối cô ấy, nói dối cả vợ anh. Ngày mai anh sẽ nói thật với cô ấy."
- Turn 3, 10.2–14.1s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, barely above a whisper): "Nói thật thì đau đấy. Nhưng nói dối thì còn đau lâu hơn nhiều."
- Pacing: @Linh speaks at an even everyday pace, then @Quan answers at an even everyday pace, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steady rain on the window, porridge bubbling softly, a spoon against a bowl, distant thunder rolling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 4 (`canh-17/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The modern kitchen of the villa late at night: a white marble island with tall stools, matte sage-green cabinets, only the warm copper pendant lamps lit, a small pot of rice porridge steaming on the stove, rain streaming down the dark garden window.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; soft lavender silk pajama set with long sleeves and long trousers.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; rumpled grey T-shirt and navy pajama trousers, barefoot.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the husband with the dim villa kitchen softly behind, gentle handheld drift.
- Shot 2, 6–9s: 85mm close-up of the elegant wife, slow dolly-in.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the elegant wife onto the husband, subtle rack focus.
- Shot 4, 13–15s: 24mm wide shot of the dim villa kitchen with the husband and the elegant wife, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is collecting the empty bowl and is already speaking at an easy conversational pace (gentle).
- 1–2s (Shot 1): @Quan keeps talking, smiling tiredly.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Linh starts speaking slowly and softly (eyes wet), rising from the stool, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @Linh keeps talking, tucking her hair behind one ear.
- 8–9s (Shot 2): @Linh finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Quan starts speaking quickly (jolted, hopeful), half standing up, the bowl still in his hand, while @Linh listens with the mouth closed.
- 10–11s (Shot 3): @Quan keeps talking, holding @Linh's gaze.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh only smiles, and walks out of the kitchen without a word.
- 14–15s (Shot 4): @Quan stands alone under the copper lamps, holding the empty bowl, rain pouring outside. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, gentle): "Cảm ơn em đã ngồi nghe. Lạ thật, nói với người lạ lại dễ hơn nói với chính vợ mình."
- Turn 2, 5.9–9.0s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, eyes wet): "Có khi vợ anh cũng đang ngồi đâu đó nghe đấy."
- Turn 3, 9.5–13.1s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, jolted, hopeful): "Em vừa nói gì cơ? Em nhớ ra rồi à? Em nhớ ra anh rồi phải không?"
- Pacing: @Quan speaks at an even everyday pace, then @Linh answers slowly and calmly, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steady rain on the window, porridge bubbling softly, a spoon against a bowl, distant thunder rolling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 1 (`canh-18/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor by day: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, floor-to-ceiling windows with soft white daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 85mm close-up of the husband, slow dolly-in.
- Shot 2, 6–11s: 50mm over-the-shoulder shot from behind the husband onto the young yoga teacher, subtle rack focus.
- Shot 3, 11–13s: 50mm medium shot of the husband with the airy yoga studio softly behind, slow arc.
- Shot 4, 13–15s: 24mm wide shot of the airy yoga studio with the husband and the young yoga teacher, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is standing just inside the door, hands empty at his sides and is already speaking slowly and softly (plain and honest).
- 1–2s (Shot 1): @Quan keeps talking, breathing out slowly.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @MaiAnh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @MaiAnh starts speaking at an easy conversational pace (calm, surprising him), finishing a stretch and turning to face him, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @MaiAnh keeps talking, folding her arms gently.
- 8–9s (Shot 2): @MaiAnh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @MaiAnh keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @MaiAnh finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Quan starts speaking quickly (caught off guard), blinking rapidly, while @MaiAnh listens with the mouth closed.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth, taking a half step forward.
- 13–14s (CUT to Shot 4): @MaiAnh only smiles a small, private smile.
- 14–15s (Shot 4): @Quan waits, completely lost. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, plain and honest): "Mai Anh, anh đến để nói thật. Anh chưa bao giờ ly thân. Anh đã nói dối em."
- Turn 2, 5.9–10.4s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, calm, surprising him): "Em biết từ lâu rồi. Nhưng đây là câu nói thật đầu tiên anh nói với em đấy."
- Turn 3, 10.9–13.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, caught off guard): "Em biết rồi à? Ai nói cho em biết? Tuấn à?"
- Pacing: @Quan speaks slowly and calmly, then @MaiAnh answers at an even everyday pace, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft city noise through the windows, bare feet on wood, a door opening and closing, a ceiling fan turning. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 2 (`canh-18/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor by day: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, floor-to-ceiling windows with soft white daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm over-the-shoulder shot from behind the husband onto the young yoga teacher, subtle rack focus.
- Shot 2, 6–11s: 85mm close-up of the husband, slow arc.
- Shot 3, 11–15s: 35mm medium two-shot of the young yoga teacher and the husband, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is walking to the window and is already speaking slowly and softly (fond, mysterious).
- 1–2s (Shot 1): @MaiAnh keeps talking, looking out at the city.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Quan starts speaking at an easy conversational pace (ashamed), lowering his head, while @MaiAnh listens with the mouth closed.
- 7–8s (Shot 2): @Quan keeps talking, rubbing the back of his neck.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Quan finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @MaiAnh starts speaking quickly (brisk and proud), taking a thick envelope from her bag and holding it out, while @Quan listens with the mouth closed.
- 12–13s (Shot 3): @MaiAnh keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan takes the envelope, stunned, as if it weighs a ton. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking slowly and softly, unhurried, with a short natural pause between phrases, fond, mysterious): "Một người phụ nữ rất đẹp, rất khôn. Người đó dạy em biết thế nào là tự trọng."
- Turn 2, 5.9–10.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, ashamed): "Còn căn hộ anh hứa, anh không giữ lời được. Tiền đấy là của vợ con anh."
- Turn 3, 10.7–13.7s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, brisk and proud): "Em biết! Số tiền anh chuyển em vẫn giữ nguyên, em trả lại đây!"
- Pacing: @MaiAnh speaks slowly and calmly, then @Quan answers at an even everyday pace, then @MaiAnh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft city noise through the windows, bare feet on wood, a door opening and closing, a ceiling fan turning. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 3 (`canh-18/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor by day: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, floor-to-ceiling windows with soft white daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium two-shot of the husband and the young yoga teacher, slow arc.
- Shot 2, 6–10s: 85mm close-up of the young yoga teacher, slow push-in.
- Shot 3, 10–15s: 35mm medium two-shot of the husband and the young yoga teacher, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is holding the envelope in both hands and is already speaking at an easy conversational pace (sincere).
- 1–2s (Shot 1): @Quan keeps talking, bowing his head slightly.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @MaiAnh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @MaiAnh starts speaking at an easy conversational pace (firm, kind), walking him to the door, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @MaiAnh keeps talking, opening it for him.
- 8–9s (Shot 2): @MaiAnh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @MaiAnh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Quan starts speaking at an easy conversational pace (a small real smile), pausing in the doorway, while @MaiAnh listens with the mouth closed.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan keeps talking, leaning a little toward @MaiAnh.
- 13–14s (Shot 3): @Quan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan gives her a short respectful nod and leaves. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, sincere): "Anh xin lỗi em. Em còn trẻ, em xứng đáng với một người đàn ông không phải nói dối."
- Turn 2, 5.7–9.7s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, firm, kind): "Còn chị ấy thì xứng đáng với một người chồng tử tế. Anh tập làm đi."
- Turn 3, 10.2–14.0s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, a small real smile): "Anh đang tập đây. Ngày nào anh cũng tập, tập từ nấu cháo trở đi."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft city noise through the windows, bare feet on wood, a door opening and closing, a ceiling fan turning. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 4 (`canh-18/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
Mai Anh's airy yoga studio on a high floor by day: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, floor-to-ceiling windows with soft white daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the doctor with the airy yoga studio softly behind, slow push-in.
- Shot 2, 6–10s: 85mm close-up of the young yoga teacher, locked off.
- Shot 3, 10–15s: 35mm medium two-shot of the doctor and the young yoga teacher, gentle handheld drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang is peeking around the door in his white coat, a rolled mat under his arm and is already speaking at an easy conversational pace (awkward and polite).
- 1–2s (Shot 1): @Khang keeps talking, adjusting his rimless glasses.
- 2–3s (Shot 1): @Khang keeps talking, leaning a little toward @MaiAnh.
- 3–4s (Shot 1): @Khang keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Khang keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Khang finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @MaiAnh starts speaking quickly (brightening instantly), springing off the door with a dazzling smile, while @Khang listens with the mouth closed.
- 7–8s (Shot 2): @MaiAnh keeps talking, pointing at his shoes.
- 8–9s (Shot 2): @MaiAnh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @MaiAnh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Khang starts speaking slowly and softly (deadpan, charmed), slipping off his sneakers carefully, while @MaiAnh listens with the mouth closed.
- 11–12s (Shot 3): @Khang keeps talking, looking only at her.
- 12–13s (Shot 3): @Khang keeps talking, leaning a little toward @MaiAnh.
- 13–14s (Shot 3): @Khang finishes the line and closes the mouth.
- 14–15s (Shot 3): @MaiAnh laughs and unrolls a lilac mat at her feet. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking at a natural, even conversational pace, awkward and polite): "Xin lỗi, đây có phải lớp yoga cho người mới không? Bạn tôi bảo tôi cứng như khúc gỗ."
- Turn 2, 5.7–9.5s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, brightening instantly): "Đúng rồi ạ! Anh cởi giày ra đây, khúc gỗ nào sang đây em cũng uốn được hết!"
- Turn 3, 10.0–13.7s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking slowly and softly, unhurried, with a short natural pause between phrases, deadpan, charmed): "Thế thì tôi xin đăng ký học luôn cả năm, cô giáo ạ."
- Pacing: @Khang speaks at an even everyday pace, then @MaiAnh answers quickly, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft city noise through the windows, bare feet on wood, a door opening and closing, a ceiling fan turning. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 1 (`canh-19/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa by day: double-height glass walls onto a sunny garden, a long cream sofa, a walnut coffee table, a large abstract painting, a floating staircase with glass rails, bright soft daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Bong = Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; yellow cotton dress with a white Peter Pan collar, white socks, small red shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 85mm close-up of the husband, locked off.
- Shot 2, 6–11s: 50mm over-the-shoulder shot from behind the husband onto the little girl, gentle handheld drift.
- Shot 3, 11–15s: 35mm medium two-shot of the husband and the little girl, slow dolly-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is kneeling by the coffee table among balloons and coloured paper and is already speaking at an easy conversational pace (conspiratorial whisper).
- 1–2s (Shot 1): @Quan keeps talking, opening a small red velvet ring box.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Bong.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Bong starts speaking quickly (thrilled), gasping at the ring, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @Bong keeps talking, clasping both hands under her chin.
- 8–9s (Shot 2): @Bong keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Bong keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Bong finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Quan starts speaking quickly (finger to lips), snapping the box shut, while @Bong listens with the mouth closed.
- 12–13s (Shot 3): @Quan keeps talking, glancing at the stairs.
- 13–14s (Shot 3): @Quan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Bong mimes zipping her lips shut and throwing away the key. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, conspiratorial whisper): "Bống ơi, thứ bảy này là sinh nhật mẹ. Bố định cầu hôn mẹ lại lần nữa, con giúp bố nhé?"
- Turn 2, 6.2–10.2s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking quickly in short lively phrases, every word still clear, thrilled): "Cầu hôn ạ? Có cả nhẫn, có cả hoa, có cả bố quỳ xuống như trong phim không?"
- Turn 3, 10.7–13.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, finger to lips): "Có hết! Nhưng phải giữ bí mật, không được nói với mẹ đâu đấy!"
- Pacing: @Quan speaks at an even everyday pace, then @Bong answers quickly, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong from the sunny garden, crayons scratching on paper, a balloon squeaking, a clock ticking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 2 (`canh-19/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa by day: double-height glass walls onto a sunny garden, a long cream sofa, a walnut coffee table, a large abstract painting, a floating staircase with glass rails, bright soft daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Bong = Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; yellow cotton dress with a white Peter Pan collar, white socks, small red shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm over-the-shoulder shot from behind the husband onto the little girl, gentle handheld drift.
- Shot 2, 6–10s: 85mm close-up of the husband, slow dolly-in.
- Shot 3, 10–15s: 35mm medium two-shot of the little girl and the husband, subtle rack focus.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bong is puffing out her chest and is already speaking at an easy conversational pace (proud).
- 1–2s (Shot 1): @Bong keeps talking, tapping her own chest with a crayon.
- 2–3s (Shot 1): @Bong keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Bong keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Bong keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Bong finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Quan starts speaking slowly and softly (suddenly alert), going still with a balloon half blown, while @Bong listens with the mouth closed.
- 7–8s (Shot 2): @Quan keeps talking, lowering it slowly.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Bong starts speaking quickly (covering her mouth too late), clapping both hands over her mouth, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @Bong keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Bong keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Bong finishes the line and closes the mouth.
- 14–15s (Shot 3): @Bong stares at him over her hands, eyes huge. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking at a natural, even conversational pace, proud): "Bố yên tâm! Con kín miệng nhất nhà. Chuyện của mẹ con còn giấu được cả tháng nay cơ mà!"
- Turn 2, 6.2–9.6s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, suddenly alert): "Chuyện của mẹ à? Chuyện gì thế, kể bố nghe nào con?"
- Turn 3, 10.1–13.4s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking quickly in short lively phrases, every word still clear, covering her mouth too late): "Chuyện mẹ bảo con không được nói là mẹ bảo! Á, con lỡ mồm rồi!"
- Pacing: @Bong speaks at an even everyday pace, then @Quan answers slowly and calmly, then @Bong answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong from the sunny garden, crayons scratching on paper, a balloon squeaking, a clock ticking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 3 (`canh-19/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa by day: double-height glass walls onto a sunny garden, a long cream sofa, a walnut coffee table, a large abstract painting, a floating staircase with glass rails, bright soft daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Bong = Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; yellow cotton dress with a white Peter Pan collar, white socks, small red shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium two-shot of the husband and the little girl, slow dolly-in.
- Shot 2, 6–11s: 85mm close-up of the little girl, subtle rack focus.
- Shot 3, 11–15s: 35mm medium two-shot of the husband and the little girl, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is sitting down on the floor at her eye level and is already speaking at an easy conversational pace (very gentle).
- 1–2s (Shot 1): @Quan keeps talking, holding her small hands.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Bong.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Bong starts speaking quickly (loyal and stubborn), shaking her head so hard her pigtails fly, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @Bong keeps talking, squeezing her eyes shut.
- 8–9s (Shot 2): @Bong keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Bong keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Bong finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Quan starts speaking slowly and softly (a slow smile), letting out a breath that turns into a quiet laugh, while @Bong listens with the mouth closed.
- 12–13s (Shot 3): @Quan keeps talking, leaning a little toward @Bong.
- 13–14s (Shot 3): @Quan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan pulls her into a hug and rests his chin on her head. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, very gentle): "Bống, nhìn bố này. Mẹ có thật sự quên bố không, hay mẹ đang chơi trò gì với bố?"
- Turn 2, 5.7–10.1s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking quickly in short lively phrases, every word still clear, loyal and stubborn): "Con không nói đâu! Con đã hứa với mẹ, mà hứa thì phải giữ lời, bố dạy con thế mà!"
- Turn 3, 10.6–13.4s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, a slow smile): "Ừ. Bố dạy con thế. Thế mà bố lại quên."
- Pacing: @Quan speaks at an even everyday pace, then @Bong answers quickly, then @Quan answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong from the sunny garden, crayons scratching on paper, a balloon squeaking, a clock ticking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 4 (`canh-19/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The open living room of a modern lakeside villa by day: double-height glass walls onto a sunny garden, a long cream sofa, a walnut coffee table, a large abstract painting, a floating staircase with glass rails, bright soft daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Bong = Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; yellow cotton dress with a white Peter Pan collar, white socks, small red shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the husband with the sunlit villa living room softly behind, subtle rack focus.
- Shot 2, 5–11s: 85mm close-up of the little girl, slow arc.
- Shot 3, 11–15s: 35mm medium two-shot of the husband and the little girl, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is staring at the glass staircase and is already speaking slowly and softly (realising).
- 1–2s (Shot 1): @Quan keeps talking, nodding to himself.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Bong.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Bong starts speaking slowly and softly (worried), tugging his shirt, while @Quan listens with the mouth closed.
- 6–7s (Shot 2): @Bong keeps talking, looking up with shining eyes.
- 7–8s (Shot 2): @Bong keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Bong keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Bong keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Bong finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Quan starts speaking quickly (a sudden grin), tapping her nose, while @Bong listens with the mouth closed.
- 12–13s (Shot 3): @Quan keeps talking, picking up the ring box again.
- 13–14s (Shot 3): @Quan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Bong breaks into a huge gap-toothed grin. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.3s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, realising): "Vậy là mẹ nhớ hết. Nhớ cả những gì bố đã làm với mẹ."
- Turn 2, 4.8–10.1s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking slowly and softly, unhurried, with a short natural pause between phrases, worried): "Bố có giận mẹ không? Bố đừng giận mẹ nhé, mẹ chỉ muốn bố thương nhà mình thôi."
- Turn 3, 10.6–13.8s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, a sudden grin): "Bố không giận. Mẹ muốn diễn thì bố diễn cùng, diễn đến cảnh cuối luôn."
- Pacing: @Quan speaks slowly and calmly, then @Bong answers slowly and calmly, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong from the sunny garden, crayons scratching on paper, a balloon squeaking, a clock ticking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 1 (`canh-20/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A calm doctor's consultation office in the private hospital by day: a white desk with a reading lamp, a model of a human brain, a softly glowing lightbox on the wall, a window with soft daylight, two chairs facing the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 85mm close-up of the husband, slow arc.
- Shot 2, 6–10s: 50mm over-the-shoulder shot from behind the husband onto the doctor, slow push-in.
- Shot 3, 10–13s: 50mm medium shot of the husband with the calm consultation office softly behind, locked off.
- Shot 4, 13–15s: 24mm wide shot of the calm consultation office with the husband and the doctor, gentle handheld drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is sitting down across the desk and crossing his legs and is already speaking at an easy conversational pace (dry and knowing).
- 1–2s (Shot 1): @Quan keeps talking, tapping the model of the brain.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Khang.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Khang starts speaking at an easy conversational pace (unruffled), writing calmly in a blank folder, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @Khang keeps talking, not looking up.
- 8–9s (Shot 2): @Khang keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Khang finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Quan starts speaking quickly (triumphant), leaning forward and pointing at him, while @Khang listens with the mouth closed.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Khang slowly closes the folder and takes off his glasses.
- 14–15s (Shot 4): @Quan sits back, arms folded, waiting. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, dry and knowing): "Bác sĩ, tôi đến tái khám hộ vợ. Bệnh mất trí nhớ có chọn lọc ấy, có thuốc nào chữa không?"
- Turn 2, 6.2–9.7s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking at a natural, even conversational pace, unruffled): "Có. Thuốc đặc trị là một người chồng biết lỗi. Uống đều mỗi ngày."
- Turn 3, 10.2–13.0s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, triumphant): "Anh là đồng phạm của cô ấy, đúng không? Tôi biết hết rồi!"
- Pacing: @Quan speaks at an even everyday pace, then @Khang answers at an even everyday pace, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet clinic hum, a chair creaking, pages turning, soft footsteps in the corridor outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 2 (`canh-20/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A calm doctor's consultation office in the private hospital by day: a white desk with a reading lamp, a model of a human brain, a softly glowing lightbox on the wall, a window with soft daylight, two chairs facing the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the husband onto the doctor, slow push-in.
- Shot 2, 5–11s: 85mm close-up of the husband, locked off.
- Shot 3, 11–15s: 35mm medium two-shot of the doctor and the husband, gentle handheld drift.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang is polishing his glasses on his coat and is already speaking slowly and softly (deadpan).
- 1–2s (Shot 1): @Khang keeps talking, putting them back on.
- 2–3s (Shot 1): @Khang keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Khang keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Khang finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking at an easy conversational pace (half laughing, half aggrieved), counting on his fingers, while @Khang listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, shaking his head.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Khang.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Quan finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Khang starts speaking quickly (a rare grin), leaning back in his chair, while @Quan listens with the mouth closed.
- 12–13s (Shot 3): @Khang keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Khang finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan stares at him, then laughs despite himself. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking slowly and softly, unhurried, with a short natural pause between phrases, deadpan): "Tôi chỉ kê đơn. Thuốc thì cô ấy tự uống. Diễn thì cô ấy tự diễn."
- Turn 2, 5.4–10.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, half laughing, half aggrieved): "Một tháng nay tôi ngủ sofa, hát dưới cửa sổ, viết thư tay. Hóa ra là bị chấm thi."
- Turn 3, 10.7–13.9s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking quickly in short lively phrases, every word still clear, a rare grin): "Thế anh đã qua môn chưa? Nói thật, tôi thấy anh tiến bộ nhanh đấy!"
- Pacing: @Khang speaks slowly and calmly, then @Quan answers at an even everyday pace, then @Khang answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet clinic hum, a chair creaking, pages turning, soft footsteps in the corridor outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 3 (`canh-20/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A calm doctor's consultation office in the private hospital by day: a white desk with a reading lamp, a model of a human brain, a softly glowing lightbox on the wall, a window with soft daylight, two chairs facing the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium two-shot of the husband and the doctor, locked off.
- Shot 2, 6–10s: 85mm close-up of the doctor, gentle handheld drift.
- Shot 3, 10–15s: 35mm medium two-shot of the husband and the doctor, slow dolly-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is looking down at his hands and is already speaking slowly and softly (serious now).
- 1–2s (Shot 1): @Quan keeps talking, turning his wedding ring.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Khang.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Khang starts speaking at an easy conversational pace (curious), leaning forward on the desk, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @Khang keeps talking, steepling his fingers.
- 8–9s (Shot 2): @Khang keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Khang finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Quan starts speaking at an easy conversational pace (a slow grin), looking up with a spark in his eyes, while @Khang listens with the mouth closed.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan keeps talking, leaning a little toward @Khang.
- 13–14s (Shot 3): @Quan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Khang raises his eyebrows, impressed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, serious now): "Tôi không giận cô ấy. Tôi giận mình, vì phải đợi vợ giả mất trí thì tôi mới tỉnh."
- Turn 2, 6.2–10.0s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking at a natural, even conversational pace, curious): "Thế bây giờ anh định làm gì? Vạch mặt cô ấy trước cả nhà à?"
- Turn 3, 10.5–14.0s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, a slow grin): "Không. Cô ấy muốn diễn, tôi diễn theo. Lần này tôi làm đạo diễn."
- Pacing: @Quan speaks slowly and calmly, then @Khang answers at an even everyday pace, then @Quan answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet clinic hum, a chair creaking, pages turning, soft footsteps in the corridor outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 4 (`canh-20/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A calm doctor's consultation office in the private hospital by day: a white desk with a reading lamp, a model of a human brain, a softly glowing lightbox on the wall, a window with soft daylight, two chairs facing the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 50mm medium shot of the husband with the calm consultation office softly behind, gentle handheld drift.
- Shot 2, 7–11s: 85mm close-up of the doctor, slow dolly-in.
- Shot 3, 11–13s: 50mm over-the-shoulder shot from behind the doctor onto the husband, subtle rack focus.
- Shot 4, 13–15s: 24mm wide shot of the calm consultation office with the husband and the doctor, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is lowering his voice and is already speaking at an easy conversational pace (conspiratorial).
- 1–2s (Shot 1): @Quan keeps talking, glancing at the door.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Khang.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan keeps talking, never looking away from @Khang.
- 6–7s (Shot 1): @Quan finishes the line and closes the mouth.
- 7–8s (CUT to Shot 2): @Khang starts speaking quickly (mock outraged), throwing up his hands, while @Quan listens with the mouth closed.
- 8–9s (Shot 2): @Khang keeps talking, shaking his head.
- 9–10s (Shot 2): @Khang keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Khang finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Quan starts speaking slowly and softly (solemn bribe), holding up one finger, while @Khang listens with the mouth closed.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Khang holds up two fingers, bargaining silently.
- 14–15s (Shot 4): @Quan nods; they shake hands across the desk. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, conspiratorial): "Bác sĩ giúp tôi một việc. Thứ bảy này, anh cứ đến tiệc sinh nhật, đứng về phe cô ấy như bình thường."
- Turn 2, 6.7–10.7s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking quickly in short lively phrases, every word still clear, mock outraged): "Anh bắt tôi làm điệp viên hai mang à? Lương bác sĩ không đủ trả cho việc này đâu!"
- Turn 3, 11.2–13.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, solemn bribe): "Tôi trả bằng một bữa bún chả."
- Pacing: @Quan speaks at an even everyday pace, then @Khang answers quickly, then @Quan answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet clinic hum, a chair creaking, pages turning, soft footsteps in the corridor outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 1 (`canh-21/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The villa garden at night dressed for a birthday party: strings of warm fairy lights over the lawn, a white rose arch, a small round table with a cream birthday cake and candles, lanterns along a stone path, a still pool reflecting the lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; flowing white chiffon midi dress with fluttering sleeves, a thin gold belt, white strappy heels.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; elegant lavender satin midi dress with cap sleeves, small pearl earrings, silver heels.
- Wardrobe: in this shot @Linh and @MaiAnh wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young yoga teacher, slow dolly-in.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the young yoga teacher onto the elegant wife, subtle rack focus.
- Shot 3, 10–15s: 35mm medium two-shot of the young yoga teacher and the elegant wife, slow arc.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is hurrying up the lantern path holding a gift bag and is already speaking quickly (excited whisper).
- 1–2s (Shot 1): @MaiAnh keeps talking, looking her up and down in awe.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking at an easy conversational pace (calm, decided), adjusting the thin gold belt of her white dress, while @MaiAnh listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, glancing toward the rose arch.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @MaiAnh.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @MaiAnh starts speaking quickly (playful), craning her neck toward the gate, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @MaiAnh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @MaiAnh keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh follows her gaze and laughs softly. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, excited whisper): "Chị ơi, chị đẹp quá! Hôm nay chị vẫn diễn vai cô gái hai mươi hai tuổi à?"
- Turn 2, 4.7–9.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, calm, decided): "Đêm cuối. Tối nay chị sẽ cho anh ấy biết sự thật, rồi để anh ấy tự chọn."
- Turn 3, 9.7–13.3s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, playful): "Thế thì em đứng đây cổ vũ! Mà anh bác sĩ của chị cũng đến đấy ạ?"
- Pacing: @MaiAnh speaks quickly, then @Linh answers at an even everyday pace, then @MaiAnh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets in the grass, a soft breeze in the fairy lights, glasses clinking, distant laughter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 2 (`canh-21/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The villa garden at night dressed for a birthday party: strings of warm fairy lights over the lawn, a white rose arch, a small round table with a cream birthday cake and candles, lanterns along a stone path, a still pool reflecting the lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; elegant lavender satin midi dress with cap sleeves, small pearl earrings, silver heels.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; light-grey casual blazer over a white T-shirt, dark trousers, white sneakers.
- Wardrobe: in this shot @MaiAnh and @Khang wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the young yoga teacher onto the doctor, subtle rack focus.
- Shot 2, 5–9s: 85mm close-up of the young yoga teacher, slow arc.
- Shot 3, 9–15s: 35mm medium two-shot of the doctor and the young yoga teacher, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang is walking up the lantern path with a small gift box and is already speaking at an easy conversational pace (shy).
- 1–2s (Shot 1): @Khang keeps talking, rubbing his lower back.
- 2–3s (Shot 1): @Khang keeps talking, leaning a little toward @MaiAnh.
- 3–4s (Shot 1): @Khang keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Khang finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @MaiAnh starts speaking quickly (laughing), tilting her head, while @Khang listens with the mouth closed.
- 6–7s (Shot 2): @MaiAnh keeps talking, pointing at his posture.
- 7–8s (Shot 2): @MaiAnh keeps talking, leaning a little toward @Khang.
- 8–9s (Shot 2): @MaiAnh finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Khang starts speaking slowly and softly (smiling), holding out the gift box to her, while @MaiAnh listens with the mouth closed.
- 10–11s (Shot 3): @Khang keeps talking, holding @MaiAnh's gaze.
- 11–12s (Shot 3): @Khang keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Khang keeps talking, leaning a little toward @MaiAnh.
- 13–14s (Shot 3): @Khang finishes the line and closes the mouth.
- 14–15s (Shot 3): @MaiAnh takes the box, cheeks pink. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking at a natural, even conversational pace, shy): "Cô giáo yoga cũng đến à? Hôm nay tôi không mang thảm, chỉ mang cái lưng còn đau."
- Turn 2, 5.4–9.0s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, laughing): "Đau là do anh tập sai tư thế đấy! Lát nữa em chỉnh lại cho, miễn phí!"
- Turn 3, 9.5–13.4s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking slowly and softly, unhurried, with a short natural pause between phrases, smiling): "Miễn phí thì tôi ngại. Hay để tôi mời cô một bữa bún chả."
- Pacing: @Khang speaks at an even everyday pace, then @MaiAnh answers quickly, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets in the grass, a soft breeze in the fairy lights, glasses clinking, distant laughter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 3 (`canh-21/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The villa garden at night dressed for a birthday party: strings of warm fairy lights over the lawn, a white rose arch, a small round table with a cream birthday cake and candles, lanterns along a stone path, a still pool reflecting the lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; cream linen suit over a white shirt, no tie, brown loafers.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
- Wardrobe: in this shot @Quan wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium two-shot of the assistant and the husband, slow arc.
- Shot 2, 6–10s: 85mm close-up of the husband, slow push-in.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the husband onto the assistant, locked off.
- Shot 4, 13–15s: 24mm wide shot of the fairy-lit villa garden with the assistant and the husband, gentle handheld drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tuan is handing over a red ring box and a bouquet of white daisies behind the rose arch and is already speaking quickly (jittery checklist).
- 1–2s (Shot 1): @Tuan keeps talking, patting his pockets.
- 2–3s (Shot 1): @Tuan keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Tuan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Tuan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Tuan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Quan starts speaking slowly and softly (sure), straightening his cream linen jacket, while @Tuan listens with the mouth closed.
- 7–8s (Shot 2): @Quan keeps talking, looking toward the party.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Tuan starts speaking quickly (overwhelmed), fanning his face with his tablet, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @Tuan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Tuan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Quan tucks the ring box into his jacket pocket.
- 14–15s (Shot 4): @Tuan dabs at the corner of one eye. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, jittery checklist): "Anh ơi, nhẫn đây, hoa đây, nhạc đây! Mà anh chắc là chị ấy giả vờ chứ? Nhỡ chị ấy quên thật thì sao?"
- Turn 2, 5.9–9.3s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, sure): "Quên thật thì anh tán lại. Tán bao nhiêu lần cũng được."
- Turn 3, 9.8–12.6s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking quickly in short lively phrases, every word still clear, overwhelmed): "Trời ơi, giám đốc của em lãng mạn từ bao giờ thế này!"
- Pacing: @Tuan speaks quickly, then @Quan answers slowly and calmly, then @Tuan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets in the grass, a soft breeze in the fairy lights, glasses clinking, distant laughter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 4 (`canh-21/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The villa garden at night dressed for a birthday party: strings of warm fairy lights over the lawn, a white rose arch, a small round table with a cream birthday cake and candles, lanterns along a stone path, a still pool reflecting the lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; cream linen suit over a white shirt, no tie, brown loafers.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
- Wardrobe: in this shot @Quan wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 50mm medium shot of the husband with the fairy-lit villa garden softly behind, slow push-in.
- Shot 2, 7–11s: 85mm close-up of the assistant, locked off.
- Shot 3, 11–15s: 35mm medium two-shot of the husband and the assistant, gentle handheld drift.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is looking at the bouquet in his hands and is already speaking at an easy conversational pace (quiet).
- 1–2s (Shot 1): @Quan keeps talking, breathing in.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Tuan.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan keeps talking, never looking away from @Tuan.
- 6–7s (Shot 1): @Quan finishes the line and closes the mouth.
- 7–8s (CUT to Shot 2): @Tuan starts speaking slowly and softly (sniffling), blowing his nose into a handkerchief, while @Quan listens with the mouth closed.
- 8–9s (Shot 2): @Tuan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Tuan keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Tuan finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Quan starts speaking quickly (laughing), clapping him on the back, while @Tuan listens with the mouth closed.
- 12–13s (Shot 3): @Quan keeps talking, leaning a little toward @Tuan.
- 13–14s (Shot 3): @Quan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan steps out from behind the rose arch into the fairy lights. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, quiet): "Từ cái hôm cô ấy nhìn anh như nhìn người lạ. Lúc ấy anh mới biết mình sợ mất cô ấy thế nào."
- Turn 2, 6.7–10.1s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking slowly and softly, unhurried, with a short natural pause between phrases, sniffling): "Anh nói thế làm em tự nhiên muốn đi lấy vợ quá."
- Turn 3, 10.6–13.6s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, laughing): "Lấy vợ thì phải có người yêu trước đã! Đi, ra sân khấu thôi!"
- Pacing: @Quan speaks at an even everyday pace, then @Tuan answers slowly and calmly, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets in the grass, a soft breeze in the fairy lights, glasses clinking, distant laughter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 1 (`canh-22/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The villa garden at night dressed for a birthday party: strings of warm fairy lights over the lawn, a white rose arch, a small round table with a cream birthday cake and candles, lanterns along a stone path, a still pool reflecting the lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; flowing white chiffon midi dress with fluttering sleeves, a thin gold belt, white strappy heels.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; cream linen suit over a white shirt, no tie, brown loafers.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 85mm close-up of the husband, locked off.
- Shot 2, 7–10s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, gentle handheld drift.
- Shot 3, 10–13s: 50mm medium shot of the husband with the fairy-lit villa garden softly behind, slow dolly-in.
- Shot 4, 13–15s: 24mm wide shot of the fairy-lit villa garden with the husband and the elegant wife, subtle rack focus.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is kneeling on one knee under the white rose arch and is already speaking at an easy conversational pace (jittery, sincere).
- 1–2s (Shot 1): @Quan keeps talking, holding up the open red ring box.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan keeps talking, never looking away from @Linh.
- 6–7s (Shot 1): @Quan finishes the line and closes the mouth.
- 7–8s (CUT to Shot 2): @Linh starts speaking slowly and softly (playing along, cool), standing very straight in her white dress, while @Quan listens with the mouth closed.
- 8–9s (Shot 2): @Linh keeps talking, lifting one eyebrow.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Quan starts speaking quickly (grinning), counting on the fingers of his free hand, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh presses her lips together, holding back a laugh.
- 14–15s (Shot 4): @Quan stays kneeling, holding the ring steady. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.4s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, jittery, sincere): "Cô gái hai mươi hai tuổi ơi, anh biết mình mới quen nhau được một tháng. Nhưng em có đồng ý lấy anh không?"
- Turn 2, 6.9–9.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, playing along, cool): "Nhanh thế? Tôi còn chưa biết gì về anh."
- Turn 3, 9.9–12.9s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, grinning): "Thì anh kể! Anh có một vợ, một con, và một tháng ngủ sofa!"
- Pacing: @Quan speaks at an even everyday pace, then @Linh answers slowly and calmly, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets in the grass, a soft breeze in the fairy lights, a hush falling over the garden, the pool lapping gently. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 2 (`canh-22/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The villa garden at night dressed for a birthday party: strings of warm fairy lights over the lawn, a white rose arch, a small round table with a cream birthday cake and candles, lanterns along a stone path, a still pool reflecting the lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; flowing white chiffon midi dress with fluttering sleeves, a thin gold belt, white strappy heels.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; cream linen suit over a white shirt, no tie, brown loafers.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, gentle handheld drift.
- Shot 2, 5–11s: 85mm close-up of the husband, slow dolly-in.
- Shot 3, 11–15s: 35mm medium two-shot of the elegant wife and the husband, subtle rack focus.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is folding her arms and is already speaking slowly and softly (letting the act slip).
- 1–2s (Shot 1): @Linh keeps talking, her voice wavering.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking at an easy conversational pace (tender), looking straight up into her eyes, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, smiling gently.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Quan finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Linh starts speaking at an easy conversational pace (stunned), unfolding her arms slowly, while @Quan listens with the mouth closed.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh's hand drifts to her mouth. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, letting the act slip): "Anh có một vợ rồi, thế mà anh còn dám đứng đây cầu hôn tôi à?"
- Turn 2, 5.4–10.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, tender): "Anh cầu hôn đúng vợ anh. Người vợ mất trí nhớ có chọn lọc, mà chọn đúng mỗi anh để quên."
- Turn 3, 11.2–13.5s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, stunned): "Anh biết từ bao giờ? Ai nói với anh?"
- Pacing: @Linh speaks slowly and calmly, then @Quan answers at an even everyday pace, then @Linh answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets in the grass, a soft breeze in the fairy lights, a hush falling over the garden, the pool lapping gently. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 3 (`canh-22/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The villa garden at night dressed for a birthday party: strings of warm fairy lights over the lawn, a white rose arch, a small round table with a cream birthday cake and candles, lanterns along a stone path, a still pool reflecting the lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; flowing white chiffon midi dress with fluttering sleeves, a thin gold belt, white strappy heels.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; cream linen suit over a white shirt, no tie, brown loafers.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of the husband and the elegant wife, slow dolly-in.
- Shot 2, 5–9s: 85mm close-up of the elegant wife, subtle rack focus.
- Shot 3, 9–15s: 35mm medium two-shot of the husband and the elegant wife, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is tilting his head toward the house and is already speaking at an easy conversational pace (teasing).
- 1–2s (Shot 1): @Quan keeps talking, winking.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking quickly (indignant and laughing), flapping one hand at him, while @Quan listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, laughing with tears in her eyes.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Linh finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Quan starts speaking slowly and softly (soft), his smile fading into something serious, while @Linh listens with the mouth closed.
- 10–11s (Shot 3): @Quan keeps talking, holding @Linh's gaze.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @Quan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh stops laughing; she looks down at him for a long, quiet moment. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, teasing): "Từ hôm con gái mình lỡ mồm. Anh diễn theo em một tuần rồi đấy, đạo diễn ạ."
- Turn 2, 5.4–8.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, indignant and laughing): "Anh lừa em một tuần à? Thế mà em còn thương anh ngủ sofa!"
- Turn 3, 8.9–13.9s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft): "Em lừa anh một tháng. Còn anh đã lừa em cả năm trời. Mình coi như hòa nhé?"
- Pacing: @Quan speaks at an even everyday pace, then @Linh answers quickly, then @Quan answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets in the grass, a soft breeze in the fairy lights, a hush falling over the garden, the pool lapping gently. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 4 (`canh-22/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The villa garden at night dressed for a birthday party: strings of warm fairy lights over the lawn, a white rose arch, a small round table with a cream birthday cake and candles, lanterns along a stone path, a still pool reflecting the lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; flowing white chiffon midi dress with fluttering sleeves, a thin gold belt, white strappy heels.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; cream linen suit over a white shirt, no tie, brown loafers.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the elegant wife with the fairy-lit villa garden softly behind, subtle rack focus.
- Shot 2, 6–11s: 85mm close-up of the husband, slow arc.
- Shot 3, 11–15s: 50mm over-the-shoulder shot from behind the husband onto the elegant wife, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is pressing a hand to her chest and is already speaking slowly and softly (tearful).
- 1–2s (Shot 1): @Linh keeps talking, breathing shakily.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Linh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Quan starts speaking slowly and softly (pleading softly), holding the ring box higher, while @Linh listens with the mouth closed.
- 7–8s (Shot 2): @Quan keeps talking, eyes shining.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Quan finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Linh starts speaking at an easy conversational pace (smiling through tears), wiping her tears with her fingertips, while @Quan listens with the mouth closed.
- 12–13s (Shot 3): @Linh keeps talking, holding out her left hand.
- 13–14s (Shot 3): @Linh keeps talking, taking a quick breath between phrases.
- 14–15s (Shot 3): @Linh finishes the line and closes the mouth. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, tearful): "Em không quên được đâu anh. Những gì anh đã làm với em, em vẫn nhớ hết."
- Turn 2, 5.7–10.5s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking slowly and softly, unhurried, with a short natural pause between phrases, pleading softly): "Anh không xin em quên. Anh chỉ xin em chọn lọc thêm cho anh một lần nữa."
- Turn 3, 11.0–14.3s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, smiling through tears): "Được thôi. Nhưng lần này anh phải ký hợp đồng thử việc đã."
- Pacing: @Linh speaks slowly and calmly, then @Quan answers slowly and calmly, then @Linh answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets in the grass, a soft breeze in the fairy lights, a hush falling over the garden, the pool lapping gently. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 1 (`canh-23/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The villa garden at night dressed for a birthday party: strings of warm fairy lights over the lawn, a white rose arch, a small round table with a cream birthday cake and candles, lanterns along a stone path, a still pool reflecting the lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; flowing white chiffon midi dress with fluttering sleeves, a thin gold belt, white strappy heels.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; cream linen suit over a white shirt, no tie, brown loafers.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 85mm close-up of the elegant wife, slow arc.
- Shot 2, 6–9s: 50mm over-the-shoulder shot from behind the elegant wife onto the husband, slow push-in.
- Shot 3, 9–13s: 50mm medium shot of the elegant wife with the fairy-lit villa garden softly behind, locked off.
- Shot 4, 13–15s: 24mm wide shot of the fairy-lit villa garden with the elegant wife and the husband, gentle handheld drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is unfolding a crisp white sheet beside the birthday cake and is already speaking at an easy conversational pace (business-like, eyes sparkling).
- 1–2s (Shot 1): @Linh keeps talking, smoothing it flat.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Linh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Quan starts speaking quickly (eager), already uncapping a fountain pen, while @Linh listens with the mouth closed.
- 7–8s (Shot 2): @Quan keeps talking, reaching for the sheet.
- 8–9s (Shot 2): @Quan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Linh starts speaking slowly and softly (dry), sliding the sheet just out of his reach, while @Quan listens with the mouth closed.
- 10–11s (Shot 3): @Linh keeps talking, holding @Quan's gaze.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Quan sheepishly picks the sheet up and holds it to the candlelight.
- 14–15s (Shot 4): @Linh folds her arms, smiling. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, business-like, eyes sparkling): "Hợp đồng thử việc làm chồng, thời hạn sáu tháng. Điều một: sáng nào cũng đưa con đi học."
- Turn 2, 5.7–8.9s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, eager): "Đồng ý hết! Điều hai là gì em? Anh ký luôn, khỏi cần đọc nữa!"
- Turn 3, 9.4–12.8s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, dry): "Đọc kỹ vào. Người không đọc kỹ giấy tờ, em không lấy."
- Pacing: @Linh speaks at an even everyday pace, then @Quan answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets in the grass, the candles flickering, a fountain pen scratching, distant laughter by the pool. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 2 (`canh-23/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The villa garden at night dressed for a birthday party: strings of warm fairy lights over the lawn, a white rose arch, a small round table with a cream birthday cake and candles, lanterns along a stone path, a still pool reflecting the lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; flowing white chiffon midi dress with fluttering sleeves, a thin gold belt, white strappy heels.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; cream linen suit over a white shirt, no tie, brown loafers.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm over-the-shoulder shot from behind the elegant wife onto the husband, slow push-in.
- Shot 2, 6–9s: 85mm close-up of the elegant wife, locked off.
- Shot 3, 9–12s: 50mm medium shot of the husband with the fairy-lit villa garden softly behind, gentle handheld drift.
- Shot 4, 12–15s: 24mm wide shot of the fairy-lit villa garden with the husband and the elegant wife, slow dolly-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is squinting at the sheet in the candlelight and is already speaking at an easy conversational pace (reading slowly).
- 1–2s (Shot 1): @Quan keeps talking, tracing a line with his finger.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Linh starts speaking quickly (triumphant), tapping the sheet with one fingernail, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Linh finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Quan starts speaking quickly (grinning), flipping the sheet over, while @Linh listens with the mouth closed.
- 10–11s (Shot 3): @Quan keeps talking, holding @Linh's gaze.
- 11–12s (Shot 3): @Quan finishes the line and closes the mouth.
- 12–13s (CUT to Shot 4): @Linh leans in close to his ear, smiling dangerously.
- 13–14s (Shot 4): @Quan swallows.
- 14–15s (Shot 4): @Linh and @Quan stay silent, mouths closed, as the moment settles. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, reading slowly): "Điều hai: điện thoại không cài mật khẩu. Điều ba: đi họp với đối tác Nhật thì phải mang vợ theo?"
- Turn 2, 6.2–8.5s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, triumphant): "Chuẩn rồi! Đối tác Nhật lai Hàn lại càng phải mang!"
- Turn 3, 9.0–12.0s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, grinning): "Thế điều cuối cùng ghi gì đây? Vi phạm hợp đồng thì sao em?"
- Pacing: @Quan speaks at an even everyday pace, then @Linh answers quickly, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets in the grass, the candles flickering, a fountain pen scratching, distant laughter by the pool. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 3 (`canh-23/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The villa garden at night dressed for a birthday party: strings of warm fairy lights over the lawn, a white rose arch, a small round table with a cream birthday cake and candles, lanterns along a stone path, a still pool reflecting the lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; flowing white chiffon midi dress with fluttering sleeves, a thin gold belt, white strappy heels.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; cream linen suit over a white shirt, no tie, brown loafers.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium two-shot of the elegant wife and the husband, locked off.
- Shot 2, 6–9s: 85mm close-up of the husband, gentle handheld drift.
- Shot 3, 9–15s: 35mm medium two-shot of the elegant wife and the husband, slow dolly-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is whispering beside his ear and is already speaking slowly and softly (sweet menace).
- 1–2s (Shot 1): @Linh keeps talking, straightening up with an innocent smile.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Linh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Quan starts speaking quickly (laughing), signing with a big flourish, while @Linh listens with the mouth closed.
- 7–8s (Shot 2): @Quan keeps talking, laughing.
- 8–9s (Shot 2): @Quan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Linh starts speaking at an easy conversational pace (tender), taking his free hand in hers, while @Quan listens with the mouth closed.
- 10–11s (Shot 3): @Linh keeps talking, holding @Quan's gaze.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan finishes signing with one hand, the other holding hers tight. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.0s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, sweet menace): "Vi phạm thì anh mất trí nhớ thật. Mà lần này là mất vĩnh viễn, không có thuốc chữa đâu."
- Turn 2, 6.5–9.0s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, laughing): "Em đáng sợ thật đấy! Nhưng anh ký! Ký ngay bây giờ!"
- Turn 3, 9.5–13.3s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, tender): "Ký một tay thôi. Tay kia để dành nắm tay vợ con, kẻo lại quên."
- Pacing: @Linh speaks slowly and calmly, then @Quan answers quickly, then @Linh answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets in the grass, the candles flickering, a fountain pen scratching, distant laughter by the pool. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 4 (`canh-23/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The villa garden at night dressed for a birthday party: strings of warm fairy lights over the lawn, a white rose arch, a small round table with a cream birthday cake and candles, lanterns along a stone path, a still pool reflecting the lights.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @MaiAnh = Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; elegant lavender satin midi dress with cap sleeves, small pearl earrings, silver heels.
- @Khang = Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; light-grey casual blazer over a white T-shirt, dark trousers, white sneakers.
- Wardrobe: in this shot @MaiAnh and @Khang wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the young yoga teacher with the fairy-lit villa garden softly behind, gentle handheld drift.
- Shot 2, 6–11s: 85mm close-up of the doctor, slow dolly-in.
- Shot 3, 11–15s: 35mm medium two-shot of the young yoga teacher and the doctor, subtle rack focus.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @MaiAnh is standing by the glowing pool holding a glass of juice and is already speaking at an easy conversational pace (wondering).
- 1–2s (Shot 1): @MaiAnh keeps talking, watching the couple across the lawn.
- 2–3s (Shot 1): @MaiAnh keeps talking, leaning a little toward @Khang.
- 3–4s (Shot 1): @MaiAnh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @MaiAnh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @MaiAnh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Khang starts speaking slowly and softly (gentle), turning to look at her, while @MaiAnh listens with the mouth closed.
- 7–8s (Shot 2): @Khang keeps talking, smiling softly.
- 8–9s (Shot 2): @Khang keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Khang keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Khang finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @MaiAnh starts speaking quickly (shy), twisting the stem of her glass, while @Khang listens with the mouth closed.
- 12–13s (Shot 3): @MaiAnh keeps talking, leaning a little toward @Khang.
- 13–14s (Shot 3): @MaiAnh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Khang offers her his arm; @MaiAnh takes it with a bright smile. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking at a natural, even conversational pace, wondering): "Nhìn họ kìa. Em cứ tưởng mình phá hoại một gia đình, hóa ra lại giúp họ làm lành."
- Turn 2, 5.7–10.7s, spoken on camera by @Khang (man of 34, calm gentle tenor, dry deadpan humour, never in a hurry, speaking slowly and softly, unhurried, with a short natural pause between phrases, gentle): "Cô dũng cảm hơn cô nghĩ đấy. Trả lại tiền, nói lời tử tế, ít ai làm được."
- Turn 3, 11.2–14.2s, spoken on camera by @MaiAnh (young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt, speaking quickly in short lively phrases, every word still clear, shy): "Thế lời mời ăn tối anh hứa hôm trước vẫn còn hiệu lực chứ?"
- Pacing: @MaiAnh speaks at an even everyday pace, then @Khang answers slowly and calmly, then @MaiAnh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets in the grass, the candles flickering, a fountain pen scratching, distant laughter by the pool. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 1 (`canh-24/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The bright modern kitchen of the villa in the morning: a white marble island with tall stools, matte sage-green cabinets, copper pendant lamps, a bowl of lemons, a large window onto the sunny garden.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; grey T-shirt, dark jeans and a frilly pink kitchen apron, house slippers.
- @Bong = Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; yellow cotton dress with a white Peter Pan collar, white socks, small red shoes.
- Wardrobe: in this shot @Quan wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 85mm close-up of the little girl, slow dolly-in.
- Shot 2, 4–10s: 50mm over-the-shoulder shot from behind the little girl onto the husband, subtle rack focus.
- Shot 3, 10–13s: 50mm medium shot of the little girl with the sunny villa kitchen softly behind, slow arc.
- Shot 4, 13–15s: 24mm wide shot of the sunny villa kitchen with the little girl and the husband, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bong is sitting on a tall stool at the marble island and is already speaking quickly (complaining).
- 1–2s (Shot 1): @Bong keeps talking, patting her lopsided pigtails.
- 2–3s (Shot 1): @Bong keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Bong finishes the line and closes the mouth.
- 4–5s (CUT to Shot 2): @Quan starts speaking at an easy conversational pace (concentrating hard), standing behind her with a comb in his teeth, then in his hand, while @Bong listens with the mouth closed.
- 5–6s (Shot 2): @Quan keeps talking, frowning at the pigtails.
- 6–7s (Shot 2): @Quan keeps talking, one hand moving lightly with the words.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Bong.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Bong starts speaking quickly (outraged giggle), turning around on the stool to glare at him, while @Quan listens with the mouth closed.
- 11–12s (Shot 3): @Bong keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Bong finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Quan quickly unties one pigtail and starts again, tongue between his teeth.
- 14–15s (Shot 4): @Bong giggles and swings her legs. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.0s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking quickly in short lively phrases, every word still clear, complaining): "Bố ơi, tóc con bị lệch một bên rồi! Bố tết như cái tổ chim ấy!"
- Turn 2, 4.5–9.3s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, concentrating hard): "Tháng thứ sáu rồi mà bố vẫn chưa tết được tóc đều. Thôi, lệch một tí cho cá tính!"
- Turn 3, 9.8–12.9s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking quickly in short lively phrases, every word still clear, outraged giggle): "Cá tính gì! Các bạn lại bảo con đội tổ chim đi học mất!"
- Pacing: @Bong speaks quickly, then @Quan answers at an even everyday pace, then @Bong answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: eggs sizzling in a pan, birdsong from the garden, a toaster popping, a school bag zipper. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 2 (`canh-24/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The bright modern kitchen of the villa in the morning: a white marble island with tall stools, matte sage-green cabinets, copper pendant lamps, a bowl of lemons, a large window onto the sunny garden.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; grey T-shirt, dark jeans and a frilly pink kitchen apron, house slippers.
- @Bong = Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; yellow cotton dress with a white Peter Pan collar, white socks, small red shoes.
- Wardrobe: in this shot @Quan wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm over-the-shoulder shot from behind the little girl onto the husband, subtle rack focus.
- Shot 2, 6–11s: 85mm close-up of the little girl, slow arc.
- Shot 3, 11–13s: 50mm medium shot of the husband with the sunny villa kitchen softly behind, slow push-in.
- Shot 4, 13–15s: 24mm wide shot of the sunny villa kitchen with the husband and the little girl, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is sliding a plate of fried egg and a carton of strawberry milk across the island and is already speaking at an easy conversational pace (brisk morning dad).
- 1–2s (Shot 1): @Quan keeps talking, zipping up her small school bag.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Bong.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Quan finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Bong starts speaking at an easy conversational pace (proud of him), sipping the strawberry milk through a straw, while @Quan listens with the mouth closed.
- 7–8s (Shot 2): @Bong keeps talking, beaming.
- 8–9s (Shot 2): @Bong keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Bong keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Bong finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Quan starts speaking quickly (chuffed), puffing out his chest in the pink apron, while @Bong listens with the mouth closed.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Bong giggles at the frilly apron.
- 14–15s (Shot 4): @Quan plants one hand on his hip and holds the spatula up like a hero. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, brisk morning dad): "Trứng rán này, sữa dâu này, cặp sách đây. Hôm nay bố đưa con đi học sớm mười phút."
- Turn 2, 5.7–11.0s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking at a natural, even conversational pace, proud of him): "Bố ơi, bố có biết tuần trước cô giáo khen bố là phụ huynh đến đúng giờ nhất lớp không?"
- Turn 3, 11.5–13.2s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, chuffed): "Thật à? Bố phải khoe mẹ mới được!"
- Pacing: @Quan speaks at an even everyday pace, then @Bong answers at an even everyday pace, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: eggs sizzling in a pan, birdsong from the garden, a toaster popping, a school bag zipper. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 3 (`canh-24/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The bright modern kitchen of the villa in the morning: a white marble island with tall stools, matte sage-green cabinets, copper pendant lamps, a bowl of lemons, a large window onto the sunny garden.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; sharp white tailored blazer over a black silk top, slim black trousers, gold earrings, black heels.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; grey T-shirt, dark jeans and a frilly pink kitchen apron, house slippers.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–7s: 35mm medium two-shot of the elegant wife and the husband, slow arc.
- Shot 2, 7–11s: 85mm close-up of the husband, slow push-in.
- Shot 3, 11–15s: 35mm medium two-shot of the elegant wife and the husband, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is sweeping in, radiant in a white blazer, holding up her phone and is already speaking at an easy conversational pace (glowing).
- 1–2s (Shot 1): @Linh keeps talking, spinning on her heel.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Linh keeps talking, never looking away from @Quan.
- 6–7s (Shot 1): @Linh finishes the line and closes the mouth.
- 7–8s (CUT to Shot 2): @Quan starts speaking quickly (proud), lifting her off her feet in a quick hug, while @Linh listens with the mouth closed.
- 8–9s (Shot 2): @Quan keeps talking, setting her down.
- 9–10s (Shot 2): @Quan keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Quan finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Linh starts speaking slowly and softly (teasing), straightening the frills of his pink apron, while @Quan listens with the mouth closed.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan freezes with the spatula in his hand. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, glowing): "Anh ơi, bộ sưu tập đầu tiên của em bán hết sạch rồi! Mười năm rồi em mới được làm lại nghề của mình."
- Turn 2, 6.9–10.3s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, proud): "Anh biết mà! Vợ anh mà, ngày xưa là hoa khôi, bây giờ là bà chủ!"
- Turn 3, 10.8–14.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, teasing): "Còn anh thì sao? Hôm nay hết hạn thử việc rồi đấy."
- Pacing: @Linh speaks at an even everyday pace, then @Quan answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: eggs sizzling in a pan, birdsong from the garden, a toaster popping, a school bag zipper. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 4 (`canh-24/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
The bright modern kitchen of the villa in the morning: a white marble island with tall stools, matte sage-green cabinets, copper pendant lamps, a bowl of lemons, a large window onto the sunny garden.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; sharp white tailored blazer over a black silk top, slim black trousers, gold earrings, black heels.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; grey T-shirt, dark jeans and a frilly pink kitchen apron, house slippers.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the husband with the sunny villa kitchen softly behind, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the elegant wife, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the elegant wife onto the husband, gentle handheld drift.
- Shot 4, 13–15s: 24mm wide shot of the sunny villa kitchen with the husband and the elegant wife, slow dolly-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is following her around the island and is already speaking quickly (fidgety).
- 1–2s (Shot 1): @Quan keeps talking, counting points on his fingers.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking at an easy conversational pace (playful), picking up her handbag, while @Quan listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, waving goodbye with her fingers from the doorway.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Quan starts speaking at an easy conversational pace (a determined nod), saluting with the spatula, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan finishes the line and closes the mouth.
- 13–14s (CUT to Shot 4): @Linh laughs and disappears through the doorway.
- 14–15s (Shot 4): @Quan turns to the stove, grinning, and the egg in the pan has burnt. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, fidgety): "Thế anh có được ký hợp đồng chính thức không? Anh làm đủ hết các điều khoản rồi mà!"
- Turn 2, 4.9–9.7s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, playful): "Để tối nay em công bố. Ở đúng cái nhà hàng mà năm ngoái anh cho em leo cây."
- Turn 3, 10.2–12.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, a determined nod): "Tối nay anh đến trước một tiếng. Không, hai tiếng!"
- Pacing: @Quan speaks quickly, then @Linh answers at an even everyday pace, then @Quan answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: eggs sizzling in a pan, birdsong from the garden, a toaster popping, a school bag zipper. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 1 (`canh-25/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A luxurious rooftop restaurant terrace at night high above a wide city lake, privately booked and empty of other guests: one candlelit table with white linen and red roses, a glass balustrade, the city's golden lights and the dark lake below, potted olive trees, warm string lights overhead, a private brass elevator at the end of the terrace.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; floor-length deep-red silk evening gown with long sleeves, ruby drop earrings.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; classic black tuxedo with a black bow tie, white shirt.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the elegant wife, locked off.
- Shot 2, 5–9s: 50mm over-the-shoulder shot from behind the elegant wife onto the husband, gentle handheld drift.
- Shot 3, 9–15s: 35mm medium two-shot of the elegant wife and the husband, slow dolly-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is stepping out of the brass elevator in a deep-red gown and is already speaking at an easy conversational pace (amused).
- 1–2s (Shot 1): @Linh keeps talking, looking around the candlelit table.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Quan starts speaking quickly (proud), rising from his chair in his tuxedo, while @Linh listens with the mouth closed.
- 6–7s (Shot 2): @Quan keeps talking, holding out a bouquet of white daisies.
- 7–8s (Shot 2): @Quan keeps talking, leaning a little toward @Linh.
- 8–9s (Shot 2): @Quan finishes the line and closes the mouth.
- 9–10s (CUT to Shot 3): @Linh starts speaking slowly and softly (teasing), taking the daisies and smelling them, while @Quan listens with the mouth closed.
- 10–11s (Shot 3): @Linh keeps talking, holding @Quan's gaze.
- 11–12s (Shot 3): @Linh keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): @Quan pulls out her chair with a little bow. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking at a natural, even conversational pace, amused): "Anh đến từ bao giờ thế? Bàn ăn bày xong cả rồi, nến cũng thắp rồi."
- Turn 2, 4.9–8.9s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, proud): "Từ năm giờ chiều! Lần này không có đối tác Nhật nào hết, chỉ có anh với hoa thôi!"
- Turn 3, 9.4–13.3s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, teasing): "Bó hoa này anh tự tay chọn à? Không nhờ Tuấn chọn đấy chứ?"
- Pacing: @Linh speaks at an even everyday pace, then @Quan answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft city hum far below, a gentle night breeze, the faint clink of glassware, distant fireworks popping softly over the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 2 (`canh-25/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A luxurious rooftop restaurant terrace at night high above a wide city lake, privately booked and empty of other guests: one candlelit table with white linen and red roses, a glass balustrade, the city's golden lights and the dark lake below, potted olive trees, warm string lights overhead, a private brass elevator at the end of the terrace.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; floor-length deep-red silk evening gown with long sleeves, ruby drop earrings.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; classic black tuxedo with a black bow tie, white shirt.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the elegant wife onto the husband, gentle handheld drift.
- Shot 2, 5–10s: 85mm close-up of the elegant wife, slow dolly-in.
- Shot 3, 10–15s: 35mm medium two-shot of the husband and the elegant wife, subtle rack focus.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Quan is sitting down across from her and is already speaking at an easy conversational pace (gentle).
- 1–2s (Shot 1): @Quan keeps talking, watching her face.
- 2–3s (Shot 1): @Quan keeps talking, leaning a little toward @Linh.
- 3–4s (Shot 1): @Quan keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Quan finishes the line and closes the mouth.
- 5–6s (CUT to Shot 2): @Linh starts speaking slowly and softly (touched), touching the white petals, while @Quan listens with the mouth closed.
- 6–7s (Shot 2): @Linh keeps talking, blinking quickly.
- 7–8s (Shot 2): @Linh keeps talking, leaning a little toward @Quan.
- 8–9s (Shot 2): @Linh keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Linh finishes the line and closes the mouth.
- 10–11s (CUT to Shot 3): @Quan starts speaking quickly (hopeful grin), leaning in on his elbows, while @Linh listens with the mouth closed.
- 11–12s (Shot 3): @Quan keeps talking, one hand moving lightly with the words.
- 12–13s (Shot 3): @Quan keeps talking, leaning a little toward @Linh.
- 13–14s (Shot 3): @Quan finishes the line and closes the mouth.
- 14–15s (Shot 3): @Linh takes a slow sip of wine, making him wait. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, gentle): "Tự tay anh chọn. Hoa cúc trắng, loại em thích, không phải hoa hồng đỏ anh thích."
- Turn 2, 5.2–9.4s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, touched): "Mười năm anh tặng hoa hồng. Đến năm thứ mười một mới tặng đúng hoa."
- Turn 3, 9.9–13.5s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking quickly in short lively phrases, every word still clear, hopeful grin): "Thì anh học chậm! Nhưng anh học thật! Thế kết quả thử việc thế nào hả sếp?"
- Pacing: @Quan speaks at an even everyday pace, then @Linh answers slowly and calmly, then @Quan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft city hum far below, a gentle night breeze, the faint clink of glassware, distant fireworks popping softly over the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 3 (`canh-25/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A luxurious rooftop restaurant terrace at night high above a wide city lake, privately booked and empty of other guests: one candlelit table with white linen and red roses, a glass balustrade, the city's golden lights and the dark lake below, potted olive trees, warm string lights overhead, a private brass elevator at the end of the terrace.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; floor-length deep-red silk evening gown with long sleeves, ruby drop earrings.
- @Quan = Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; classic black tuxedo with a black bow tie, white shirt.
- Wardrobe: in this shot @Linh and @Quan wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium two-shot of the elegant wife and the husband, slow dolly-in.
- Shot 2, 6–11s: 85mm close-up of the husband, subtle rack focus.
- Shot 3, 11–15s: 35mm medium two-shot of the elegant wife and the husband, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is setting down her glass and is already speaking slowly and softly (official, then soft).
- 1–2s (Shot 1): @Linh keeps talking, reaching across to take his hand.
- 2–3s (Shot 1): @Linh keeps talking, leaning a little toward @Quan.
- 3–4s (Shot 1): @Linh keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Linh keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Linh finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Quan starts speaking at an easy conversational pace (beaming), squeezing her hand, while @Linh listens with the mouth closed.
- 7–8s (Shot 2): @Quan keeps talking, laughing.
- 8–9s (Shot 2): @Quan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Quan keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Quan finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Linh starts speaking quickly (laughing), throwing her head back with laughter, while @Quan listens with the mouth closed.
- 12–13s (Shot 3): @Linh keeps talking, leaning a little toward @Quan.
- 13–14s (Shot 3): @Linh finishes the line and closes the mouth.
- 14–15s (Shot 3): Soft fireworks bloom over the lake behind them. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking slowly and softly, unhurried, with a short natural pause between phrases, official, then soft): "Kết quả là anh được ký hợp đồng dài hạn. Nhưng mỗi năm gia hạn một lần."
- Turn 2, 5.7–10.7s, spoken on camera by @Quan (man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered, speaking at a natural, even conversational pace, beaming): "Mỗi năm một lần thì anh tán em mỗi năm một lần. Tán đến khi nào em già thì thôi."
- Turn 3, 11.2–14.0s, spoken on camera by @Linh (woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young, speaking quickly in short lively phrases, every word still clear, laughing): "Già rồi em lại giả vờ mất trí nhớ cho anh tán tiếp!"
- Pacing: @Linh speaks slowly and calmly, then @Quan answers at an even everyday pace, then @Linh answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft city hum far below, a gentle night breeze, the faint clink of glassware, distant fireworks popping softly over the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 4 (`canh-25/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.

[LOCATION]
A luxurious rooftop restaurant terrace at night high above a wide city lake, privately booked and empty of other guests: one candlelit table with white linen and red roses, a glass balustrade, the city's golden lights and the dark lake below, potted olive trees, warm string lights overhead, a private brass elevator at the end of the terrace.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Tuan = Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, bright lively eyes, thick slightly wavy black hair, a stocky friendly build; light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.
- @Bong = Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; yellow cotton dress with a white Peter Pan collar, white socks, small red shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the little girl with the candlelit rooftop terrace softly behind, subtle rack focus.
- Shot 2, 6–11s: 85mm close-up of the assistant, slow arc.
- Shot 3, 11–15s: 35mm medium two-shot of the little girl and the assistant, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bong is sitting at a little side table with a slice of cake and is already speaking at an easy conversational pace (curious).
- 1–2s (Shot 1): @Bong keeps talking, looking up at him.
- 2–3s (Shot 1): @Bong keeps talking, leaning a little toward @Tuan.
- 3–4s (Shot 1): @Bong keeps talking, taking a quick breath between phrases.
- 4–5s (Shot 1): @Bong keeps talking, eyebrows lifting on the key word.
- 5–6s (Shot 1): @Bong finishes the line and closes the mouth.
- 6–7s (CUT to Shot 2): @Tuan starts speaking slowly and softly (wise for once), watching the fireworks over the lake with a fond smile, while @Bong listens with the mouth closed.
- 7–8s (Shot 2): @Tuan keeps talking, patting her head.
- 8–9s (Shot 2): @Tuan keeps talking, taking a quick breath between phrases.
- 9–10s (Shot 2): @Tuan keeps talking, eyebrows lifting on the key word.
- 10–11s (Shot 2): @Tuan finishes the line and closes the mouth.
- 11–12s (CUT to Shot 3): @Bong starts speaking quickly (cheeky), pointing her cake fork at him, while @Tuan listens with the mouth closed.
- 12–13s (Shot 3): @Bong keeps talking, leaning a little toward @Tuan.
- 13–14s (Shot 3): @Bong finishes the line and closes the mouth.
- 14–15s (Shot 3): @Tuan freezes with cake halfway to his mouth, then bursts out laughing. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking at a natural, even conversational pace, curious): "Chú Tuấn ơi, mất trí nhớ có chọn lọc là bệnh gì hả chú? Bố mẹ con khỏi chưa ạ?"
- Turn 2, 6.2–11.0s, spoken on camera by @Tuan (man of 35, lively nasal comic tenor, gabbling fast whenever he lies, speaking slowly and softly, unhurried, with a short natural pause between phrases, wise for once): "Khỏi rồi. Bệnh ấy lạ lắm, ai khỏi bệnh thì nhà người ấy lại vui hơn trước."
- Turn 3, 11.5–14.0s, spoken on camera by @Bong (girl of 7, high clear child voice, very earnest and bright, speaking quickly in short lively phrases, every word still clear, cheeky): "Thế chú mắc thử đi! Biết đâu chú lấy được vợ!"
- Pacing: @Bong speaks at an even everyday pace, then @Tuan answers slowly and calmly, then @Bong answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft city hum far below, a gentle night breeze, the faint clink of glassware, distant fireworks popping softly over the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```
