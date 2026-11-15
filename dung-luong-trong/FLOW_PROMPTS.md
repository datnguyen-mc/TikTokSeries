# Dung Lượng Trống (Free Space) — Bộ 80 Prompt Google Flow Omni (20 Cảnh × 4 Clips × 15s)

- **Không có người dẫn chuyện:** 100% lời thoại do nhân vật nói trên hình — cả 80 clip là thoại khớp khẩu hình. Giọng gốc của mỗi nhân vật (tuổi, chất giọng, giọng Hà Nội) giữ nguyên văn ở mọi clip để Omni không đổi người nói.
- **Nhịp giọng theo cảnh:** mỗi lượt thoại có nhịp riêng nối sau giọng gốc — **nhanh** (cãi vã, hoảng hốt, rượt đuổi, khoe khoang; tốc độ ×1.2), **vừa** (trò chuyện thường), **chậm** (xúc động, thú nhận, câu chốt lặng người; tốc độ ×0.9). Khung thoại tính theo nhịp nên câu chậm ít chữ hơn. Cả phim: 71 lượt nhanh, 89 lượt vừa, 80 lượt chậm.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 80 clips × 15s, tất cả là clip thoại; lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 41 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 39 clip ảnh nhân vật (Ingredients), 0 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** không có clip VO nên runner không tăng tốc giọng clip nào; tốc độ nói nằm trong prompt (nhịp từng lượt) để khớp khẩu hình.
- **Màu phim & ánh sáng:** Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py dung-luong-trong` sinh lại toàn bộ clip, README, kịch bản.

---

## Cảnh 01 - Clip 1 (`canh-01/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, deep at night, lit only by orange street light through the barred window and a small yellow bedside lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm close-up of the young man's face as he sits up in bed in the dark, slow push-in.
- Shot 2, 5–10s: 28mm wide shot from the foot of the bed of the young man kneeling on the mattress facing the white wall covered in a large slanted black scrawl, locked off.
- Shot 3, 10–15s: 85mm close-up of the young man's face lit by the orange street light as he stares at the wall, handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai jerks upright in bed and is already speaking in a breathless whisper, eyes wide in the dark.
- 1–2s (Shot 1): @Khai keeps whispering as he lifts his right hand and finds an uncapped black marker in his fingers.
- 2–3s (Shot 1): @Khai turns the marker over, still talking softly, his chest rising and falling fast.
- 3–4s (Shot 1): @Khai keeps speaking as a small violet light blinks on the thin patch at the back of his neck.
- 4–5s (Shot 1): @Khai finishes the question, closes his mouth and slowly turns his head toward the wall.
- 5–6s (CUT to Shot 2): @Khai kneels on the mattress facing the white plaster wall, where a large slanted black scrawl, too blurry to read, runs across the plaster, and starts reading it aloud fast.
- 6–7s (Shot 2): @Khai keeps reading quickly, tracing the scrawl in the air with the marker tip.
- 7–8s (Shot 2): @Khai goes on fast, leaning closer to the wall, his breath fogging slightly.
- 8–9s (Shot 2): @Khai keeps talking, glancing from the scrawl to the marker in his hand and back.
- 9–10s (Shot 2): @Khai finishes the question, mouth open, and swallows hard.
- 10–11s (CUT to Shot 3): @Khai starts speaking again slowly and quietly, staring at the slanted strokes on the plaster.
- 11–12s (Shot 3): @Khai keeps talking softly, lowering the marker, his jaw tight.
- 12–13s (Shot 3): @Khai goes on in a hush, shaking his head very slightly.
- 13–14s (Shot 3): @Khai finishes, closes his mouth and lets the marker slip from his fingers onto the blanket.
- 14–15s (Shot 3): @Khai sits frozen on his knees, breathing hard, orange street light striping his face through the window bars. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, spoken on camera by @Khai alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–4.3s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, breathless whisper, half asleep): "Cái gì đây? Sao mình lại cầm cái bút này giữa đêm thế này?"
- Part 2, 4.8–9.4s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, reading aloud in rising panic): "Khu tập thể Kim Liên, nhà C, phòng bảy linh bốn. Đừng ngủ. Ai đã viết cái này lên tường nhà mình?"
- Part 3, 9.9–13.0s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, hushed, chilled to the bone): "Trời ơi, chữ này nghiêng nghiêng, không phải chữ của mình."
- Pacing: @Khai speaks slowly and calmly, then @Khai continues quickly, then @Khai continues slowly and calmly; the change of speed is clearly audible.
- Throughout, @Khai's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the slow whir of an electric fan, a distant scooter in the alley, the squeak of a marker cap, a small electronic tick from the neck patch. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 2 (`canh-01/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, deep at night, lit only by orange street light through the barred window and a small yellow bedside lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Nova = Nova, the NeuroRent app's holographic assistant; a softly glowing translucent violet hologram of a young woman about a hand's height tall, standing on a beam of light above a phone screen, a smooth calm face with a gentle fixed smile, sleek hair in a high knot, faint horizontal scan lines through her body; a simple fitted violet light-dress.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the small violet hologram woman standing on a beam of light above the phone on the pillow, slow push-in.
- Shot 2, 5–10s: 40mm medium two-shot of the young man kneeling on the bed and the hologram on the pillow beside him, locked off.
- Shot 3, 10–15s: 100mm extreme close-up of the hologram's calm smiling face with scan lines drifting through it, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): On the pillow @Nova, a hand-tall violet hologram rising from the phone screen, is already speaking in a bright, cheerful voice.
- 1–2s (Shot 1): @Nova keeps talking, clasping her small glowing hands in front of her, scan lines drifting through her body.
- 2–3s (Shot 1): @Nova goes on, tilting her head with a fixed gentle smile.
- 3–4s (Shot 1): @Nova keeps speaking as a tiny violet coin icon spins in the air beside her.
- 4–5s (Shot 1): @Nova finishes the sentence and closes her mouth, still smiling.
- 5–6s (CUT to Shot 2): @Khai leans toward the pillow and starts speaking fast, pointing back at the scrawled wall.
- 6–7s (Shot 2): @Khai keeps talking quickly, his finger stabbing toward the wall behind him.
- 7–8s (Shot 2): @Khai goes on, looking from the hologram to the wall and back.
- 8–9s (Shot 2): @Khai finishes, closes his mouth and waits, breathing hard.
- 9–10s (Shot 2): @Nova answers slowly in a soothing voice, her smile never changing.
- 10–11s (CUT to Shot 3): @Nova keeps speaking softly, opening her small hands in a calming gesture.
- 11–12s (Shot 3): @Nova goes on gently, her light pulsing softly.
- 12–13s (Shot 3): @Nova finishes and closes her mouth, glowing serenely.
- 13–14s (Shot 3): In extreme close-up @Nova's smooth face holds the same gentle smile while scan lines drift through it.
- 14–15s (Shot 3): @Nova's tiny face keeps smiling without blinking as a faint flicker runs through the hologram. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.5s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking at a natural, even conversational pace, bright, cheerful, like a morning radio host): "Chào buổi sáng anh Khải. Phiên thuê não đêm nay đã hoàn tất. Bốn trăm tám mươi nghìn đã về ví của anh."
- Turn 2, 7.0–10.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, urgent, jabbing a finger at the wall): "Nova, đêm qua tôi có dậy không? Ai vào phòng tôi? Ai viết lên tường?"
- Turn 3, 10.7–14.0s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking slowly and softly, unhurried, with a short natural pause between phrases, soothing, unbothered): "Anh đã ngủ rất ngon. Chúc anh một ngày tốt lành."
- Pacing: @Nova speaks at an even everyday pace, then @Khai answers quickly, then @Nova answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft rising chime as the hologram appears, the low hum of the projected light, the electric fan, a dog barking far away. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 3 (`canh-01/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, deep at night, lit only by orange street light through the barred window and a small yellow bedside lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- @Nova = Nova, the NeuroRent app's holographic assistant; a softly glowing translucent violet hologram of a young woman about a hand's height tall, standing on a beam of light above a phone screen, a smooth calm face with a gentle fixed smile, sleek hair in a high knot, faint horizontal scan lines through her body; a simple fitted violet light-dress.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the hologram onto the young man on the bed, locked off.
- Shot 2, 5–10s: 85mm close-up of the hologram answering from the pillow, slow push-in.
- Shot 3, 10–15s: 40mm medium two-shot of the young man pointing at the wall while the hologram glows on the pillow, handheld.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking, leaning over the pillow, his voice strained but controlled.
- 1–2s (Shot 1): @Khai keeps talking as he holds up the black marker in front of the hologram.
- 2–3s (Shot 1): @Khai goes on, gesturing over his shoulder at the scrawled wall.
- 3–4s (Shot 1): @Khai keeps speaking, pressing his palm flat to his own forehead.
- 4–5s (Shot 1): @Khai finishes, closes his mouth and lowers his hand, waiting.
- 5–6s (CUT to Shot 2): @Nova answers in a smooth, sweet voice, standing perfectly still on her beam of light.
- 6–7s (Shot 2): @Nova keeps talking, giving a small polite nod.
- 7–8s (Shot 2): @Nova goes on, lifting one tiny hand as if reading from an invisible card.
- 8–9s (Shot 2): @Nova keeps speaking in the same pleasant tone, her smile fixed.
- 9–10s (Shot 2): @Nova finishes and closes her mouth, glowing calmly.
- 10–11s (CUT to Shot 3): @Khai snaps back fast, jabbing the marker toward the wall.
- 11–12s (Shot 3): @Khai keeps talking quickly, his eyebrows shooting up in disbelief.
- 12–13s (Shot 3): @Khai finishes, closes his mouth and lets out a short, shaky breath through his nose.
- 13–14s (Shot 3): @Khai stares at the hologram, jaw clenched, while @Nova keeps smiling, mouth closed.
- 14–15s (Shot 3): The marker trembles in @Khai's hand beside the glowing hologram as both stay silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, strained, trying to stay calm): "Không, cô trả lời tôi đi. Tay tôi cầm bút, trên tường có chữ, mà tôi không nhớ gì cả."
- Turn 2, 5.9–10.7s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking at a natural, even conversational pace, sweet and smooth, like a recorded answer): "Hệ thống không ghi nhận bất thường nào. Có thể anh mộng du do làm việc quá sức."
- Turn 3, 11.2–13.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, sharp, disbelieving): "Mộng du mà viết được cả địa chỉ nhà người khác à?"
- Pacing: @Khai speaks at an even everyday pace, then @Nova answers at an even everyday pace, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the electric fan, the hum of the hologram light, a motorbike horn far off in the city, the creak of the bed frame. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 4 (`canh-01/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, deep at night, lit only by orange street light through the barred window and a small yellow bedside lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Nova = Nova, the NeuroRent app's holographic assistant; a softly glowing translucent violet hologram of a young woman about a hand's height tall, standing on a beam of light above a phone screen, a smooth calm face with a gentle fixed smile, sleek hair in a high knot, faint horizontal scan lines through her body; a simple fitted violet light-dress.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 85mm close-up of the hologram speaking softly on the pillow, locked off.
- Shot 2, 4–9s: 50mm medium shot of the young man reaching behind his neck to peel off the thin glowing patch, handheld.
- Shot 3, 9–15s: 35mm wide shot of the dark room as the hologram fades and the young man sits alone on the bed facing the scrawled wall, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Nova is already speaking slowly and softly, swaying gently on her beam of light.
- 1–2s (Shot 1): @Nova keeps talking in a lulling voice, her small hands folded.
- 2–3s (Shot 1): @Nova goes on, her glow dimming to a warmer violet.
- 3–4s (Shot 1): @Nova finishes, closes her mouth and smiles.
- 4–5s (CUT to Shot 2): @Khai snaps back fast, reaching behind his neck to the thin violet patch.
- 5–6s (Shot 2): @Khai keeps talking quickly as he digs a fingernail under the edge of the patch.
- 6–7s (Shot 2): @Khai goes on, wincing as the patch peels away from his skin.
- 7–8s (Shot 2): @Khai finishes, closes his mouth and holds the peeled patch up in front of the hologram.
- 8–9s (Shot 2): @Khai tosses the patch onto the desk, breathing hard, mouth shut.
- 9–10s (CUT to Shot 3): @Nova answers in a pleasant, even voice, unbothered.
- 10–11s (Shot 3): @Nova keeps speaking, giving a small wave of one glowing hand.
- 11–12s (Shot 3): @Nova finishes, closes her mouth, and her figure folds down into the phone screen.
- 12–13s (Shot 3): The violet light shrinks to a dot and goes out; the room falls dark except for the orange street light.
- 13–14s (Shot 3): @Khai sits alone on the bed, rubbing the back of his neck, staring at the slanted scrawl on the wall.
- 14–15s (Shot 3): On the desk the peeled patch blinks once, faintly violet, beside the exam books. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft and lulling): "Anh Khải ơi, anh nên ngủ thêm một chút nữa. Thiết bị sẽ giúp anh thư giãn."
- Turn 2, 5.9–9.3s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, angry, peeling at his neck): "Thôi, tắt đi! Tôi không ngủ nữa. Tối nay tôi không dán cái miếng này nữa."
- Turn 3, 9.8–13.5s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking at a natural, even conversational pace, pleasant, as if nothing happened): "Vâng. Em sẽ nhắc anh lúc mười giờ tối nay. Chúc anh ngủ ngon."
- Pacing: @Nova speaks slowly and calmly, then @Khai answers quickly, then @Nova answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the hologram's low hum, the sticky peel of an adhesive patch, the electric fan, a soft descending chime as the hologram fades. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 1 (`canh-02/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A narrow Hanoi alley at the gate of an old five-storey collective housing block in 2041, daytime: tangled power cables overhead, potted plants, parked silent electric scooters, a peeling yellow wall, laundry hanging from the balconies above.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Hung = Hùng, 35, a loan-shark debt collector; stocky with a thick neck, shaved head, thin moustache, heavy-lidded eyes, tattooed forearms; loud red-and-yellow floral short-sleeved shirt, a thick gold chain, black trousers, leather slip-on shoes.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium shot of the debt collector leaning on the yellow wall by the gate flicking a lighter, locked off.
- Shot 2, 5–10s: 50mm close-up of the delivery rider stopping his scooter and raising both palms, handheld.
- Shot 3, 10–15s: 40mm medium two-shot of the two men face to face at the gate, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung leans on the yellow wall by the gate, flicking a lighter open and shut, and is already speaking in a slow drawl.
- 1–2s (Shot 1): @Hung keeps talking lazily, eyes half-lidded, as @Khai's scooter rolls to a stop in front of him.
- 2–3s (Shot 1): @Hung goes on, rolling his thick neck as if it aches.
- 3–4s (Shot 1): @Hung keeps speaking, snapping the lighter shut with a click.
- 4–5s (Shot 1): @Hung finishes and closes his mouth, staring at @Khai.
- 5–6s (CUT to Shot 2): @Khai swings off the scooter and starts speaking fast, palms raised with an apologetic grin.
- 6–7s (Shot 2): @Khai keeps talking quickly, nodding over and over.
- 7–8s (Shot 2): @Khai goes on, pressing one hand to his chest as he promises.
- 8–9s (Shot 2): @Khai keeps speaking fast, his grin stiff.
- 9–10s (Shot 2): @Khai finishes, closes his mouth and waits, grin fading.
- 10–11s (CUT to Shot 3): @Hung pushes off the wall and answers in a flat voice, stepping closer.
- 11–12s (Shot 3): @Hung keeps talking, holding up one thick tattooed finger.
- 12–13s (Shot 3): @Hung goes on, tilting his shaved head.
- 13–14s (Shot 3): @Hung finishes, closes his mouth and taps @Khai's cheek lightly twice with two fingers.
- 14–15s (Shot 3): @Khai stands rigid, eyes down, as @Hung's gold chain glints in the sun; both mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.5s, spoken on camera by @Hung (man of 35, rough gravelly bass, a slow menacing drawl, speaking slowly and softly, unhurried, with a short natural pause between phrases, lazy and menacing, flicking a lighter): "Khải. Hai ngày rồi đấy em. Anh đứng đợi mỏi cả cổ đây này."
- Turn 2, 5.0–8.4s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, apologetic, forcing a grin): "Anh Hùng, anh cho em đến cuối tuần. Cuối tuần em gom đủ, em thề đấy."
- Turn 3, 8.9–13.2s, spoken on camera by @Hung (man of 35, rough gravelly bass, a slow menacing drawl, speaking at a natural, even conversational pace, flat, unimpressed): "Cuối tuần trước mày cũng thề y như thế. Mày thề nhiều quá rồi đấy Khải."
- Pacing: @Hung speaks slowly and calmly, then @Khai answers quickly, then @Hung answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a lighter clicking open and shut, the soft whine of an electric scooter rolling in, pigeons on the cables, a radio playing faintly from a balcony. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 2 (`canh-02/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A narrow Hanoi alley at the gate of an old five-storey collective housing block in 2041, daytime: tangled power cables overhead, potted plants, parked silent electric scooters, a peeling yellow wall, laundry hanging from the balconies above.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hùng, 35, a loan-shark debt collector; stocky with a thick neck, shaved head, thin moustache, heavy-lidded eyes, tattooed forearms; loud red-and-yellow floral short-sleeved shirt, a thick gold chain, black trousers, leather slip-on shoes.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the debt collector counting on his thick fingers, locked off.
- Shot 2, 5–9s: 50mm medium shot of the delivery rider nodding fast beside his scooter, handheld.
- Shot 3, 9–15s: 35mm low-angle shot past the debt collector's shoulder up to a barred second-floor window, slow tilt up.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung is already speaking, counting slowly on his tattooed fingers.
- 1–2s (Shot 1): @Hung keeps talking, folding down one finger after another.
- 2–3s (Shot 1): @Hung goes on, raising his eyebrows meaningfully.
- 3–4s (Shot 1): @Hung keeps speaking, letting the last words hang in the air.
- 4–5s (Shot 1): @Hung trails off, closes his mouth and smiles thinly.
- 5–6s (CUT to Shot 2): @Khai answers fast, nodding again and again.
- 6–7s (Shot 2): @Khai keeps talking quickly, gesturing at his scooter and its delivery box.
- 7–8s (Shot 2): @Khai goes on, forcing a hopeful smile.
- 8–9s (Shot 2): @Khai finishes and closes his mouth.
- 9–10s (CUT to Shot 3): @Hung turns his head and looks up at a barred window on the second floor, speaking slowly and quietly.
- 10–11s (Shot 3): @Hung keeps talking in a low, cold voice, eyes fixed on the window.
- 11–12s (Shot 3): @Hung goes on, a slow smile spreading under his thin moustache.
- 12–13s (Shot 3): @Hung finishes, closes his mouth and looks back at @Khai.
- 13–14s (Shot 3): @Khai's face goes pale; his hands curl into fists at his sides, mouth shut.
- 14–15s (Shot 3): Above them the empty barred window shows a school bag hanging on a nail inside. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Hung (man of 35, rough gravelly bass, a slow menacing drawl, speaking at a natural, even conversational pace, counting it off slowly on his fingers): "Mười lăm triệu, tính cả lãi là mười tám. Thứ Bảy này anh không thấy tiền thì..."
- Turn 2, 5.4–8.6s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, rushing, desperate to please): "Em biết, em biết rồi. Em chạy thêm ca đêm, em xoay được mà anh."
- Turn 3, 9.1–13.2s, spoken on camera by @Hung (man of 35, rough gravelly bass, a slow menacing drawl, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and cold, eyes on a window): "Con bé em gái mày đi học về đường nào, anh biết hết đấy."
- Pacing: @Hung speaks at an even everyday pace, then @Khai answers quickly, then @Hung answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pigeons fluttering on the cables, the faint radio from the balcony, a neighbour's broom sweeping, a scooter passing at the end of the alley. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 3 (`canh-02/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A narrow Hanoi alley at the gate of an old five-storey collective housing block in 2041, daytime: tangled power cables overhead, potted plants, parked silent electric scooters, a peeling yellow wall, laundry hanging from the balconies above.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Hung = Hùng, 35, a loan-shark debt collector; stocky with a thick neck, shaved head, thin moustache, heavy-lidded eyes, tattooed forearms; loud red-and-yellow floral short-sleeved shirt, a thick gold chain, black trousers, leather slip-on shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm close-up of the delivery rider pleading, handheld.
- Shot 2, 5–10s: 40mm medium two-shot of the debt collector patting the rider's shoulder, locked off.
- Shot 3, 10–15s: 85mm close-up of the delivery rider lowering his eyes, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai steps forward and is already speaking fast, his voice cracking.
- 1–2s (Shot 1): @Khai keeps pleading quickly, both hands pressed together.
- 2–3s (Shot 1): @Khai goes on, shaking his head hard.
- 3–4s (Shot 1): @Khai keeps talking, glancing up at the window and back.
- 4–5s (Shot 1): @Khai finishes and closes his mouth, breathing fast.
- 5–6s (CUT to Shot 2): @Hung answers calmly, resting a heavy hand on @Khai's shoulder.
- 6–7s (Shot 2): @Hung keeps talking, patting the shoulder in a slow rhythm.
- 7–8s (Shot 2): @Hung goes on in an almost friendly tone, smiling.
- 8–9s (Shot 2): @Hung keeps speaking, holding up two fingers.
- 9–10s (Shot 2): @Hung finishes, closes his mouth and lifts his hand away.
- 10–11s (CUT to Shot 3): @Khai lowers his eyes and answers slowly, his voice low.
- 11–12s (Shot 3): @Khai keeps speaking quietly, nodding once.
- 12–13s (Shot 3): @Khai finishes and closes his mouth, jaw tight.
- 13–14s (Shot 3): @Khai stares at the ground while @Hung tucks the lighter into his shirt pocket, both silent.
- 14–15s (Shot 3): The hanging laundry sways above them in the wind as neither man moves. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, pleading, voice cracking): "Anh Hùng, anh đừng động vào con bé. Nó không liên quan gì, nợ là nợ của em mà."
- Turn 2, 4.9–9.7s, spoken on camera by @Hung (man of 35, rough gravelly bass, a slow menacing drawl, speaking at a natural, even conversational pace, calm, almost friendly): "Thế thì lo mà trả đi. Anh không thích phải đến đây nói hai lần đâu em ạ."
- Turn 3, 10.2–13.0s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, swallowing his pride): "Vâng. Thứ Bảy này. Em sẽ có tiền cho anh."
- Pacing: @Khai speaks quickly, then @Hung answers at an even everyday pace, then @Khai answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the radio from the balcony, a pot clattering in a kitchen, a scooter beeping, a gust of wind in the hanging laundry. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 4 (`canh-02/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A narrow Hanoi alley at the gate of an old five-storey collective housing block in 2041, daytime: tangled power cables overhead, potted plants, parked silent electric scooters, a peeling yellow wall, laundry hanging from the balconies above.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Hung = Hùng, 35, a loan-shark debt collector; stocky with a thick neck, shaved head, thin moustache, heavy-lidded eyes, tattooed forearms; loud red-and-yellow floral short-sleeved shirt, a thick gold chain, black trousers, leather slip-on shoes.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium shot of the debt collector patting the scooter seat, handheld.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the debt collector onto the delivery rider, locked off.
- Shot 3, 10–15s: 28mm wide shot down the narrow alley as the debt collector strolls away and the rider stays by his scooter, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Hung is already speaking fast with a mocking grin, patting the seat of @Khai's scooter.
- 1–2s (Shot 1): @Hung keeps talking quickly, running his palm along the delivery box.
- 2–3s (Shot 1): @Hung goes on, tapping the box twice and laughing under his breath.
- 3–4s (Shot 1): @Hung keeps speaking, raising his eyebrows at @Khai.
- 4–5s (Shot 1): @Hung finishes and closes his mouth, still grinning.
- 5–6s (CUT to Shot 2): @Khai steps between @Hung and the scooter and answers in a tense voice.
- 6–7s (Shot 2): @Khai keeps talking, one hand on the handlebar.
- 7–8s (Shot 2): @Khai goes on, opening his other hand in a helpless gesture.
- 8–9s (Shot 2): @Khai finishes and closes his mouth, eyes pleading.
- 9–10s (Shot 2): @Hung turns away and answers slowly over his shoulder, strolling down the alley.
- 10–11s (CUT to Shot 3): @Hung keeps talking as he walks, voice low and chilling.
- 11–12s (Shot 3): @Hung goes on, pointing back at @Khai's chest without turning.
- 12–13s (Shot 3): @Hung finishes, closes his mouth and keeps walking away.
- 13–14s (Shot 3): @Khai stands alone by his scooter, gripping the handlebar, mouth shut.
- 14–15s (Shot 3): @Hung's floral shirt disappears around the corner while @Khai stays still in the narrow alley. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Hung (man of 35, rough gravelly bass, a slow menacing drawl, speaking quickly in short lively phrases, every word still clear, mocking, patting the scooter seat): "Ngoan đấy. Mà này, cái xe giao hàng của mày cũng được giá đấy, thiếu thì anh cắm nó luôn."
- Turn 2, 5.3–9.8s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, tense, stepping between him and the scooter): "Xe là cần câu cơm của em đấy anh. Không có xe thì em lấy gì mà trả?"
- Turn 3, 10.3–14.2s, spoken on camera by @Hung (man of 35, rough gravelly bass, a slow menacing drawl, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow, chilling, walking away): "Thì nghĩ cách đi. Người như mày, chỉ còn mỗi cái thân thôi."
- Pacing: @Hung speaks quickly, then @Khai answers at an even everyday pace, then @Hung answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a palm slapping softly on a scooter seat, slip-on shoes scuffing on concrete, the radio from the balcony, the far rumble of the city. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 1 (`canh-03/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late afternoon, soft grey daylight through the barred window.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; white short-sleeved school shirt, navy pleated skirt, white canvas sneakers.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the schoolgirl turning from her desk holding up her phone, locked off.
- Shot 2, 5–9s: 85mm close-up of the young man on the edge of the bed, handheld.
- Shot 3, 9–15s: 40mm medium two-shot across the small room, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh turns on her chair at the desk and is already speaking fast, holding up her phone.
- 1–2s (Shot 1): @Linh keeps talking quickly, scrolling the glowing screen with her thumb.
- 2–3s (Shot 1): @Linh goes on, biting her lip between phrases.
- 3–4s (Shot 1): @Linh keeps speaking, glancing at the stack of exam books.
- 4–5s (Shot 1): @Linh finishes and closes her mouth, waiting.
- 5–6s (CUT to Shot 2): @Khai, sitting on the edge of the bed in his orange jacket, answers in a relaxed voice.
- 6–7s (Shot 2): @Khai keeps talking, waving his hand casually.
- 7–8s (Shot 2): @Khai finishes and closes his mouth, forcing a smile.
- 8–9s (Shot 2): @Linh lowers the phone and answers slowly, eyes on the floor.
- 9–10s (CUT to Shot 3): @Linh keeps speaking quietly, twisting the end of her ponytail.
- 10–11s (Shot 3): @Linh goes on in a small voice, shrugging one shoulder.
- 11–12s (Shot 3): @Linh keeps talking softly, not looking at her brother.
- 12–13s (Shot 3): @Linh finishes and closes her mouth, eyes still down.
- 13–14s (Shot 3): @Khai's smile falters; he rubs the back of his neck, mouth shut.
- 14–15s (Shot 3): The two siblings sit in silence while the fan turns slowly between them. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.0s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking quickly in short lively phrases, every word still clear, quick, a little nervous): "Anh ơi, cô chủ nhiệm lại nhắn rồi đấy. Tiền ôn thi với tiền hồ sơ, hạn là thứ Hai tuần sau."
- Turn 2, 5.5–7.5s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, trying to sound relaxed): "Bao nhiêu hả em? Cứ nói anh nghe."
- Turn 3, 8.0–12.8s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, eyes down): "Ba triệu hai. Hay là em nghỉ ôn, tự học ở nhà cũng được mà anh ạ."
- Pacing: @Linh speaks quickly, then @Khai answers at an even everyday pace, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the electric fan, pages turning, a pen tapping on a desk, children playing in the courtyard below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 2 (`canh-03/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late afternoon, soft grey daylight through the barred window.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; white short-sleeved school shirt, navy pleated skirt, white canvas sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium shot of the young man getting up and tapping his sister's head with a rolled-up paper, handheld.
- Shot 2, 5–10s: 85mm close-up of the schoolgirl frowning up at him, locked off.
- Shot 3, 10–15s: 50mm over-the-shoulder shot from behind the schoolgirl onto the young man, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai gets up from the bed and is already speaking fast in a mock-stern voice.
- 1–2s (Shot 1): @Khai keeps talking quickly, picking up the fee notice and rolling it into a tube.
- 2–3s (Shot 1): @Khai goes on, tapping @Linh lightly on top of the head with the paper tube.
- 3–4s (Shot 1): @Khai finishes, closes his mouth and grins.
- 4–5s (Shot 1): @Linh ducks away and starts speaking in a worried voice.
- 5–6s (CUT to Shot 2): @Linh keeps talking, frowning up at her brother.
- 6–7s (Shot 2): @Linh goes on, pointing toward the window and the alley below.
- 7–8s (Shot 2): @Linh keeps speaking, her arms folded.
- 8–9s (Shot 2): @Linh finishes and closes her mouth, eyes searching his face.
- 9–10s (Shot 2): @Khai crouches beside her chair and answers slowly and gently.
- 10–11s (CUT to Shot 3): @Khai keeps speaking softly, smoothing the paper tube flat on the desk.
- 11–12s (Shot 3): @Khai goes on, giving her a small firm nod.
- 12–13s (Shot 3): @Khai finishes and closes his mouth.
- 13–14s (Shot 3): @Linh studies him for a long moment, lips pressed together.
- 14–15s (Shot 3): @Khai holds her gaze with a steady smile while the fan turns behind them. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, teasing, mock-stern): "Tự học cái đầu mày ấy. Năm nay thi đại học, nghỉ ôn là anh cốc cho mấy cái đấy."
- Turn 2, 5.1–9.1s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking at a natural, even conversational pace, worried, frowning): "Nhưng anh lấy đâu ra tiền? Em nghe hết rồi, ông Hùng lại đến đòi nợ."
- Turn 3, 9.6–12.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, gentle, firm): "Chuyện người lớn, em không phải lo. Anh lo được hết."
- Pacing: @Khai speaks quickly, then @Linh answers at an even everyday pace, then @Khai answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the electric fan, a page fluttering, a kettle starting to hiss in a neighbour's kitchen. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 3 (`canh-03/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late afternoon, soft grey daylight through the barred window.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; white short-sleeved school shirt, navy pleated skirt, white canvas sneakers.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the schoolgirl pouting, locked off.
- Shot 2, 5–10s: 40mm medium shot of the young man flexing an arm and turning her back to her books, handheld.
- Shot 3, 10–15s: 50mm close-up of the schoolgirl holding out her little finger, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh is already speaking in a frustrated voice, pouting at her brother.
- 1–2s (Shot 1): @Linh keeps talking, counting the late hours on her fingers.
- 2–3s (Shot 1): @Linh goes on, shaking her head.
- 3–4s (Shot 1): @Linh finishes and closes her mouth, glaring.
- 4–5s (Shot 1): @Khai answers fast, flexing one skinny arm like a strongman.
- 5–6s (CUT to Shot 2): @Khai keeps talking quickly, turning her chair back toward the desk.
- 6–7s (Shot 2): @Khai goes on, tapping the maths textbook.
- 7–8s (Shot 2): @Khai finishes and closes his mouth, grinning.
- 8–9s (Shot 2): @Linh sighs and answers slowly, giving in.
- 9–10s (Shot 2): @Linh keeps talking softly, turning back toward him.
- 10–11s (CUT to Shot 3): @Linh goes on, holding out her little finger for a pinky promise.
- 11–12s (Shot 3): @Linh finishes and closes her mouth, finger still held out.
- 12–13s (Shot 3): @Khai hesitates, then hooks his little finger around hers.
- 13–14s (Shot 3): @Linh nods once, satisfied, both mouths closed.
- 14–15s (Shot 3): @Linh turns back to her books while @Khai's smile fades as he looks away. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking at a natural, even conversational pace, frustrated, pouting): "Anh lúc nào cũng nói thế. Rồi tối nào anh cũng chạy xe đến tận ba giờ sáng mới về."
- Turn 2, 5.9–8.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, brushing it off): "Thì anh khỏe mà. Thôi, học đi, mai còn kiểm tra Toán đúng không?"
- Turn 3, 9.4–12.8s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking slowly and softly, unhurried, with a short natural pause between phrases, sighing, giving in): "Vâng. Nhưng anh hứa là không vay thêm ông ấy nữa nhé."
- Pacing: @Linh speaks at an even everyday pace, then @Khai answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the electric fan, a pencil scratching, the kettle whistling next door, children laughing in the courtyard. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 4 (`canh-03/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late afternoon, soft grey daylight through the barred window.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Nova = Nova, the NeuroRent app's holographic assistant; a softly glowing translucent violet hologram of a young woman about a hand's height tall, standing on a beam of light above a phone screen, a smooth calm face with a gentle fixed smile, sleek hair in a high knot, faint horizontal scan lines through her body; a simple fitted violet light-dress.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young man lying on the bed scrolling his translucent phone, locked off.
- Shot 2, 5–10s: 100mm extreme close-up of the small violet hologram woman popping up from the phone screen, slow push-in.
- Shot 3, 10–15s: 50mm close-up of the young man's face lit violet by the hologram, handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): On the phone screen above @Khai's face, @Nova springs up as a hand-tall violet hologram and is already speaking in a bright advertising voice.
- 1–2s (Shot 1): @Nova keeps talking, tapping her own glowing temple with one finger.
- 2–3s (Shot 1): @Nova goes on, spreading her small arms wide.
- 3–4s (Shot 1): @Nova keeps speaking as a little violet outline of a brain spins beside her.
- 4–5s (Shot 1): @Nova finishes the sentence and closes her mouth with a smile.
- 5–6s (CUT to Shot 2): @Nova starts again faster, bouncing on her beam of light like a TV presenter.
- 6–7s (Shot 2): @Nova keeps talking quickly, miming sleep with her palms pressed to one cheek.
- 7–8s (Shot 2): @Nova goes on, pointing straight at @Khai.
- 8–9s (Shot 2): @Nova keeps speaking fast as tiny violet coins rain down around her.
- 9–10s (Shot 2): @Nova finishes and closes her mouth, beaming.
- 10–11s (CUT to Shot 3): @Khai, lying on the bed, answers slowly in a murmur, staring at the hologram.
- 11–12s (Shot 3): @Khai keeps speaking softly, his thumb hovering over the screen.
- 12–13s (Shot 3): @Khai finishes and closes his mouth.
- 13–14s (Shot 3): @Khai lifts his eyes to the ceiling, the violet light playing over his face.
- 14–15s (Shot 3): @Khai looks back down at the glowing hologram, thumb hovering just above the screen. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking at a natural, even conversational pace, bright advertising voice): "Bạn có biết não người chỉ dùng mười phần trăm? Chín mươi phần trăm còn lại đang để trống."
- Turn 2, 5.9–10.6s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking quickly in short lively phrases, every word still clear, excited sales pitch): "Hãy cho NeuroRent thuê khi bạn ngủ. Thức dậy là có tiền. Đăng ký hôm nay, thưởng ngay năm trăm nghìn!"
- Turn 3, 11.1–13.1s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, murmuring, hooked): "Ngủ thôi mà cũng ra tiền à?"
- Pacing: @Nova speaks at an even everyday pace, then @Nova continues quickly, then @Khai answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a bright advertising jingle chime, the hum of the hologram light, the electric fan, a page turning softly in the background. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 1 (`canh-04/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The small shared courtyard of the old collective housing block at dusk: potted bonsai and chili plants, a low plastic table with plastic stools, a water tap, warm tungsten light spilling from open doorways, the blue evening sky between the buildings.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @BaTu = Bà Tư, 68, the gentle landlady of the old collective housing block; small and slightly stooped, a deeply lined kind face, cloudy warm eyes, silver hair in a low bun, a worn thin translucent patch with a faint violet light on the back of her neck; loose brown cotton blouse with cloth buttons, black silky trousers, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot of the young man crouching beside the old woman watering her plants, locked off.
- Shot 2, 5–10s: 85mm close-up of the faded violet patch on the back of the old woman's neck as she turns, slow push-in.
- Shot 3, 10–15s: 40mm medium shot of the young man rubbing the back of his own neck, handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai crouches by the potted plants and is already speaking carefully, pointing at the back of @BaTu's neck.
- 1–2s (Shot 1): @Khai keeps talking as @BaTu tips her plastic watering can over the chili plants.
- 2–3s (Shot 1): @Khai goes on, leaning in to look at the worn translucent patch.
- 3–4s (Shot 1): @Khai finishes and closes his mouth, waiting.
- 4–5s (Shot 1): @BaTu chuckles and answers slowly, touching the faded patch with two fingers.
- 5–6s (CUT to Shot 2): @BaTu keeps talking softly, the patch glowing a faint violet under her fingertips.
- 6–7s (Shot 2): @BaTu goes on, nodding with a gentle smile.
- 7–8s (Shot 2): @BaTu finishes and closes her mouth, setting the watering can down.
- 8–9s (Shot 2): @Khai's eyebrows shoot up and he answers fast.
- 9–10s (Shot 2): @Khai keeps talking quickly, rubbing the back of his own neck.
- 10–11s (CUT to Shot 3): @Khai goes on, glancing nervously at the patch again.
- 11–12s (Shot 3): @Khai finishes and closes his mouth with an awkward laugh.
- 12–13s (Shot 3): @BaTu pats his knee kindly, mouth closed.
- 13–14s (Shot 3): @Khai lets out a breath and smiles back, both silent.
- 14–15s (Shot 3): Warm light from the open doorways falls across the two of them and the chili plants. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, curious, careful): "Bà Tư ơi, cái miếng dán sau gáy bà là cái NeuroRent đúng không hả bà?"
- Turn 2, 4.9–9.3s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking slowly and softly, unhurried, with a short natural pause between phrases, chuckling softly): "Ừ, cái này đấy con. Bà dán nó mười năm nay rồi con ạ."
- Turn 3, 9.8–13.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, surprised, a little nervous): "Mười năm ạ? Thế có đau không bà? Có làm sao không ạ? Cháu hơi sợ."
- Pacing: @Khai speaks at an even everyday pace, then @BaTu answers slowly and calmly, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water trickling from a watering can, crickets starting up, a television murmuring through an open door, a bicycle bell. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 2 (`canh-04/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The small shared courtyard of the old collective housing block at dusk: potted bonsai and chili plants, a low plastic table with plastic stools, a water tap, warm tungsten light spilling from open doorways, the blue evening sky between the buildings.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaTu = Bà Tư, 68, the gentle landlady of the old collective housing block; small and slightly stooped, a deeply lined kind face, cloudy warm eyes, silver hair in a low bun, a worn thin translucent patch with a faint violet light on the back of her neck; loose brown cotton blouse with cloth buttons, black silky trousers, plastic sandals.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the old woman speaking softly, locked off.
- Shot 2, 5–9s: 50mm over-the-shoulder shot from behind the old woman onto the young man listening, handheld.
- Shot 3, 9–15s: 40mm medium two-shot of them at the low plastic table, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaTu is already speaking slowly, waving a hand at the idea of pain.
- 1–2s (Shot 1): @BaTu keeps talking, her eyes drifting toward a doorway.
- 2–3s (Shot 1): @BaTu goes on softly, smoothing her blouse over her knees.
- 3–4s (Shot 1): @BaTu keeps speaking, her voice dropping a little.
- 4–5s (Shot 1): @BaTu finishes and closes her mouth, lips pressed together.
- 5–6s (CUT to Shot 2): @Khai leans forward and asks in an interested voice.
- 6–7s (Shot 2): @Khai keeps talking, resting his forearms on his knees.
- 7–8s (Shot 2): @Khai finishes and closes his mouth.
- 8–9s (Shot 2): @BaTu brightens and answers, counting on her fingers.
- 9–10s (CUT to Shot 3): @BaTu keeps talking, miming sleep with her palms against one cheek.
- 10–11s (Shot 3): @BaTu goes on, laughing softly.
- 11–12s (Shot 3): @BaTu keeps speaking, patting the plastic table proudly.
- 12–13s (Shot 3): @BaTu finishes and closes her mouth with a satisfied smile.
- 13–14s (Shot 3): @Khai nods slowly, thinking, mouth closed.
- 14–15s (Shot 3): @Khai looks down at his own palms while @BaTu sips from a small cup of tea. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking at a natural, even conversational pace, matter-of-fact, a little sad): "Đau gì mà đau. Hồi ông nhà bà mất đi, bà lấy tiền đâu ra mà sống hả con."
- Turn 2, 6.2–8.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, interested): "Thế mỗi đêm bà được bao nhiêu tiền hả bà?"
- Turn 3, 9.2–14.2s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking at a natural, even conversational pace, brightening, almost proud): "Đủ tiền chợ, tiền điện. Ngủ một giấc, sáng ra là có tiền rồi, sướng lắm con ạ."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets, the television through an open door, a neighbour frying garlic, the tap dripping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 3 (`canh-04/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The small shared courtyard of the old collective housing block at dusk: potted bonsai and chili plants, a low plastic table with plastic stools, a water tap, warm tungsten light spilling from open doorways, the blue evening sky between the buildings.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @BaTu = Bà Tư, 68, the gentle landlady of the old collective housing block; small and slightly stooped, a deeply lined kind face, cloudy warm eyes, silver hair in a low bun, a worn thin translucent patch with a faint violet light on the back of her neck; loose brown cotton blouse with cloth buttons, black silky trousers, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the old woman onto the young man, locked off.
- Shot 2, 5–10s: 85mm close-up of the old woman gazing into the distance, slow push-in.
- Shot 3, 10–15s: 40mm medium two-shot at the low plastic table, handheld.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking gently, leaning in toward @BaTu.
- 1–2s (Shot 1): @Khai keeps talking, his brow creased with concern.
- 2–3s (Shot 1): @Khai goes on, tilting his head to catch her eye.
- 3–4s (Shot 1): @Khai finishes and closes his mouth.
- 4–5s (Shot 1): @BaTu answers slowly, her gaze drifting past him into the dusk.
- 5–6s (CUT to Shot 2): @BaTu keeps talking, smiling vaguely.
- 6–7s (Shot 2): @BaTu pauses, her fingers searching the air, then goes on softly.
- 7–8s (Shot 2): @BaTu keeps speaking, touching her temple.
- 8–9s (Shot 2): @BaTu finishes and closes her mouth, blinking slowly.
- 9–10s (Shot 2): @Khai answers fast, worried, sitting up straight.
- 10–11s (CUT to Shot 3): @Khai keeps talking quickly, reaching for her hand.
- 11–12s (Shot 3): @Khai finishes and closes his mouth, holding her thin hand.
- 12–13s (Shot 3): @BaTu looks down at their hands as if seeing them for the first time.
- 13–14s (Shot 3): @BaTu's lips part, but she stays silent, thinking.
- 14–15s (Shot 3): The faint violet patch on @BaTu's neck pulses once as the evening light fades. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, gentle, concerned): "Bà ơi, thế dạo này bà thấy trong người thế nào? Có thấy gì khác lạ không ạ?"
- Turn 2, 5.4–10.7s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking slowly and softly, unhurried, with a short natural pause between phrases, drifting, searching for words): "Khác à... Ngủ ngon hơn con ạ. Chỉ có điều... dạo này bà hay quên lắm cơ."
- Turn 3, 11.2–13.5s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, quickly worried): "Quên gì hả bà? Bà hay quên những chuyện gì ạ?"
- Pacing: @Khai speaks at an even everyday pace, then @BaTu answers slowly and calmly, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets, a gecko clicking on the wall, the television through an open door, a wind chime. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 4 (`canh-04/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The small shared courtyard of the old collective housing block at dusk: potted bonsai and chili plants, a low plastic table with plastic stools, a water tap, warm tungsten light spilling from open doorways, the blue evening sky between the buildings.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaTu = Bà Tư, 68, the gentle landlady of the old collective housing block; small and slightly stooped, a deeply lined kind face, cloudy warm eyes, silver hair in a low bun, a worn thin translucent patch with a faint violet light on the back of her neck; loose brown cotton blouse with cloth buttons, black silky trousers, plastic sandals.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the old woman speaking quietly, locked off.
- Shot 2, 5–10s: 40mm medium shot of the young man reassuring her, handheld.
- Shot 3, 10–15s: 35mm wide shot of the courtyard with the two of them small at the table under the doorway light, slow pull-back.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaTu is already speaking slowly and quietly, frowning at her own hands.
- 1–2s (Shot 1): @BaTu keeps talking, her voice puzzled.
- 2–3s (Shot 1): @BaTu goes on, glancing toward her open kitchen door.
- 3–4s (Shot 1): @BaTu keeps speaking, shaking her head faintly.
- 4–5s (Shot 1): @BaTu finishes and closes her mouth.
- 5–6s (CUT to Shot 2): @Khai answers in a reassuring voice, squeezing her hand.
- 6–7s (Shot 2): @Khai keeps talking, smiling a little too quickly.
- 7–8s (Shot 2): @Khai goes on, nodding.
- 8–9s (Shot 2): @Khai finishes and closes his mouth.
- 9–10s (Shot 2): @BaTu smiles and answers, patting the back of his hand.
- 10–11s (CUT to Shot 3): @BaTu keeps talking warmly, wagging one finger at him.
- 11–12s (Shot 3): @BaTu goes on, chuckling.
- 12–13s (Shot 3): @BaTu finishes and closes her mouth.
- 13–14s (Shot 3): @Khai laughs softly and stands, mouth closed, while @BaTu picks up her watering can.
- 14–15s (Shot 3): The two figures sit small in the courtyard as the doorway lights glow and the sky turns deep blue. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, puzzled): "Quên tên người này người kia. Có hôm bà quên cả mình đang nấu cơm cho ai."
- Turn 2, 6.2–10.0s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, reassuring, a little too quickly): "Chắc tại bà có tuổi thôi bà ạ. Người già ai mà chẳng hay quên."
- Turn 3, 10.5–14.4s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking at a natural, even conversational pace, smiling, patting his hand): "Ừ, chắc là thế. Con mà dán thì nhớ ngủ cho đủ giấc nhé."
- Pacing: @BaTu speaks slowly and calmly, then @Khai answers at an even everyday pace, then @BaTu answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets, a rice cooker clicking off in a kitchen, the gecko clicking, distant traffic. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 1 (`canh-05/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, deep at night, lit only by orange street light through the barred window and a small yellow bedside lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Nova = Nova, the NeuroRent app's holographic assistant; a softly glowing translucent violet hologram of a young woman about a hand's height tall, standing on a beam of light above a phone screen, a smooth calm face with a gentle fixed smile, sleek hair in a high knot, faint horizontal scan lines through her body; a simple fitted violet light-dress.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the violet hologram standing above the phone beside the pillow, locked off.
- Shot 2, 5–9s: 40mm medium shot of the young man sitting cross-legged on the bed, handheld.
- Shot 3, 9–15s: 35mm wide shot of the small dark room with the young man and the glowing hologram on the bed, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Beside the pillow @Nova rises from the phone as a hand-tall violet hologram and is already speaking warmly.
- 1–2s (Shot 1): @Nova keeps talking, opening her small arms in welcome.
- 2–3s (Shot 1): @Nova goes on as a ring of violet light fills up around her like a gauge.
- 3–4s (Shot 1): @Nova keeps speaking, the ring stopping almost full.
- 4–5s (Shot 1): @Nova finishes and closes her mouth, smiling.
- 5–6s (CUT to Shot 2): @Khai sits up cross-legged and answers fast, eyes bright.
- 6–7s (Shot 2): @Khai keeps talking quickly, leaning toward the hologram.
- 7–8s (Shot 2): @Khai finishes and closes his mouth, waiting eagerly.
- 8–9s (Shot 2): @Nova answers sweetly, holding up one tiny finger.
- 9–10s (CUT to Shot 3): @Nova keeps talking, holding up a second finger.
- 10–11s (Shot 3): @Nova goes on as a small stack of violet coins builds up beside her.
- 11–12s (Shot 3): @Nova keeps speaking, the stack growing taller.
- 12–13s (Shot 3): @Nova finishes and closes her mouth, beaming.
- 13–14s (Shot 3): @Khai lets out a low whistle without speaking, staring at the coins.
- 14–15s (Shot 3): @Khai rubs his palms together, grinning, while @Nova glows beside the pillow. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking at a natural, even conversational pace, warm and welcoming): "Chào mừng anh đến với NeuroRent. Dung lượng trống của anh là tám mươi bảy phần trăm."
- Turn 2, 5.4–8.4s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, eager, sitting up): "Tám mươi bảy phần trăm cơ á? Thế một đêm được bao nhiêu tiền?"
- Turn 3, 8.9–12.9s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking at a natural, even conversational pace, sweet and precise): "Sáu mươi nghìn mỗi giờ ngủ. Tám tiếng là bốn trăm tám mươi nghìn ạ."
- Pacing: @Nova speaks at an even everyday pace, then @Khai answers quickly, then @Nova answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft welcome chime, the hum of the hologram, the electric fan, the faint rustle of a curtain upstairs. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 2 (`canh-05/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, deep at night, lit only by orange street light through the barred window and a small yellow bedside lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- @Nova = Nova, the NeuroRent app's holographic assistant; a softly glowing translucent violet hologram of a young woman about a hand's height tall, standing on a beam of light above a phone screen, a smooth calm face with a gentle fixed smile, sleek hair in a high knot, faint horizontal scan lines through her body; a simple fitted violet light-dress.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm close-up of the young man scrolling an endless page of tiny text on his translucent phone, handheld.
- Shot 2, 5–10s: 40mm medium shot of the hologram explaining beside the pillow, locked off.
- Shot 3, 10–15s: 100mm extreme close-up of his thumb pressing a glowing violet button on the screen, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking, scrolling and scrolling through a long page of tiny blurred text.
- 1–2s (Shot 1): @Khai keeps talking with a groan, flicking his thumb faster.
- 2–3s (Shot 1): @Khai goes on, tossing his head back against the wall.
- 3–4s (Shot 1): @Khai finishes and closes his mouth, rolling his eyes at the hologram.
- 4–5s (Shot 1): @Nova answers in a smooth, reassuring voice, hands folded.
- 5–6s (CUT to Shot 2): @Nova keeps talking, tracing a small circle in the air.
- 6–7s (Shot 2): @Nova goes on, tilting her head kindly.
- 7–8s (Shot 2): @Nova keeps speaking, her smile perfectly still.
- 8–9s (Shot 2): @Nova finishes and closes her mouth.
- 9–10s (Shot 2): @Khai answers fast, sitting up straight.
- 10–11s (CUT to Shot 3): @Khai keeps talking quickly as his thumb jumps to the bottom of the page.
- 11–12s (Shot 3): @Khai finishes and closes his mouth.
- 12–13s (Shot 3): His thumb presses a glowing violet button on the translucent screen.
- 13–14s (Shot 3): The button pulses twice and a soft violet light spreads across the screen.
- 14–15s (Shot 3): @Khai lowers the phone, a crooked half-smile on his face, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, scrolling, groaning): "Điều khoản sử dụng... bốn mươi tám trang à? Thôi, tóm tắt cho tôi đi."
- Turn 2, 4.7–10.5s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking at a natural, even conversational pace, smooth and reassuring): "Anh chỉ cần ngủ thôi ạ. Chúng tôi chỉ sử dụng phần dung lượng anh không dùng đến. Hoàn toàn an toàn."
- Turn 3, 11.0–12.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, impatient, decisive): "Được rồi. Đồng ý. Bấm luôn, khỏi đọc nữa."
- Pacing: @Khai speaks at an even everyday pace, then @Nova answers at an even everyday pace, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the swish of a fast scroll on glass, the hologram hum, the electric fan, a confirming double chime. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 3 (`canh-05/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, deep at night, lit only by orange street light through the barred window and a small yellow bedside lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Nova = Nova, the NeuroRent app's holographic assistant; a softly glowing translucent violet hologram of a young woman about a hand's height tall, standing on a beam of light above a phone screen, a smooth calm face with a gentle fixed smile, sleek hair in a high knot, faint horizontal scan lines through her body; a simple fitted violet light-dress.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the young man opening a small white box and peeling the backing off a thin translucent patch, locked off.
- Shot 2, 5–10s: 100mm extreme close-up of the patch settling on the back of his neck and its violet light switching on, slow push-in.
- Shot 3, 10–15s: 35mm overhead shot of the young man lying down on the bed as the hologram dims beside him, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Nova is already speaking slowly and softly while @Khai opens a small plain white box.
- 1–2s (Shot 1): @Nova keeps talking in a lulling voice as he lifts out a thin translucent patch.
- 2–3s (Shot 1): @Nova goes on gently as he peels the backing off the patch.
- 3–4s (Shot 1): @Nova keeps speaking softly, miming a patch at the back of her own glowing neck.
- 4–5s (Shot 1): @Nova finishes and closes her mouth.
- 5–6s (CUT to Shot 2): @Khai presses the patch onto the back of his neck and answers fast with a short shaky laugh.
- 6–7s (Shot 2): @Khai keeps talking quickly, hunching his shoulders at the cold touch.
- 7–8s (Shot 2): @Khai goes on, eyes darting to the hologram as a small violet light switches on at his neck.
- 8–9s (Shot 2): @Khai finishes and closes his mouth, swallowing.
- 9–10s (Shot 2): @Nova answers slowly, her light dimming to a soft glow.
- 10–11s (CUT to Shot 3): @Nova keeps speaking gently as @Khai lies back on the pillow.
- 11–12s (Shot 3): @Nova goes on in a lullaby voice, waving one tiny hand.
- 12–13s (Shot 3): @Nova finishes and closes her mouth.
- 13–14s (Shot 3): @Khai stares at the ceiling, breathing slowly, mouth closed.
- 14–15s (Shot 3): @Khai's eyelids drift shut while the patch at his neck glows a steady violet. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft, almost a lullaby): "Cảm ơn anh Khải. Vui lòng dán thiết bị phía sau gáy, rồi nằm xuống thư giãn."
- Turn 2, 5.9–8.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, nervous laugh): "Ối, lạnh thế. Cái này có chích kim vào đầu tôi không đấy hả?"
- Turn 3, 9.4–13.8s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking slowly and softly, unhurried, with a short natural pause between phrases, lulling, dimming her light): "Không đau đâu ạ. Anh cứ nhắm mắt lại nhé. Chúc anh ngủ thật ngon."
- Pacing: @Nova speaks slowly and calmly, then @Khai answers quickly, then @Nova answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a cardboard box opening, the soft peel of an adhesive backing, a tiny electronic tick, the electric fan slowing. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 4 (`canh-05/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, deep at night, lit only by orange street light through the barred window and a small yellow bedside lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; a loose pale-blue T-shirt and grey cotton shorts, hair down over her shoulders.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Linh and @Khai wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm low-angle shot up at the sleeping loft as the schoolgirl pulls the curtain aside and peers down, locked off.
- Shot 2, 5–10s: 85mm close-up of the young man lying on the bed with his eyes shut, the violet light glowing under his neck, handheld.
- Shot 3, 10–15s: 40mm medium shot from the loft looking down at the young man in bed, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh pulls the loft curtain aside, peers down sleepily and is already speaking.
- 1–2s (Shot 1): @Linh keeps talking, squinting at the violet glow under her brother's neck.
- 2–3s (Shot 1): @Linh goes on, rubbing one eye with her knuckle.
- 3–4s (Shot 1): @Linh finishes and closes her mouth, frowning.
- 4–5s (Shot 1): @Khai answers fast without opening his eyes, lying very still.
- 5–6s (CUT to Shot 2): @Khai keeps talking quickly, waving one hand lazily in the air.
- 6–7s (Shot 2): @Khai goes on, turning his head on the pillow to hide the glow.
- 7–8s (Shot 2): @Khai keeps speaking, his eyes squeezed shut.
- 8–9s (Shot 2): @Khai finishes and closes his mouth.
- 9–10s (Shot 2): @Linh answers slowly and softly, leaning further over the loft edge.
- 10–11s (CUT to Shot 3): @Linh keeps talking, her voice uneasy.
- 11–12s (Shot 3): @Linh goes on, gripping the wooden rail.
- 12–13s (Shot 3): @Linh finishes and closes her mouth.
- 13–14s (Shot 3): @Linh watches him for a moment, then lets the curtain fall closed, mouth shut.
- 14–15s (Shot 3): @Khai opens his eyes in the dark, staring at the ceiling, the violet glow pulsing under his neck. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking at a natural, even conversational pace, sleepy, suspicious): "Anh ơi, cái gì sau gáy anh mà sáng tím thế? Anh dán cái gì đấy?"
- Turn 2, 4.9–8.5s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, too quick, eyes closed): "Không có gì đâu. Cái máy đo giấc ngủ thôi mà, công ty giao hàng phát cho."
- Turn 3, 9.0–12.7s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft, uneasy): "Thật không đấy? Anh đừng có làm gì dại dột đấy nhé anh."
- Pacing: @Linh speaks at an even everyday pace, then @Khai answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a curtain rustling, the wooden loft creaking, the electric fan, the faint electronic hum of the neck patch. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 1 (`canh-06/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, early morning, pale sunlight through the barred window and a small mirror above a basin by the door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Nova = Nova, the NeuroRent app's holographic assistant; a softly glowing translucent violet hologram of a young woman about a hand's height tall, standing on a beam of light above a phone screen, a smooth calm face with a gentle fixed smile, sleek hair in a high knot, faint horizontal scan lines through her body; a simple fitted violet light-dress.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the violet hologram standing above the phone on the pillow in morning light, locked off.
- Shot 2, 5–10s: 40mm medium shot of the young man bouncing up onto his knees on the bed, handheld.
- Shot 3, 10–15s: 100mm extreme close-up of the hologram waving goodbye, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): On the pillow @Nova glows above the phone in the morning light and is already speaking cheerfully.
- 1–2s (Shot 1): @Nova keeps talking, a small violet coin spinning above her open palm.
- 2–3s (Shot 1): @Nova goes on, tossing the coin toward @Khai.
- 3–4s (Shot 1): @Nova finishes and closes her mouth, smiling.
- 4–5s (Shot 1): @Khai springs up onto his knees on the bed and answers fast, eyes wide.
- 5–6s (CUT to Shot 2): @Khai keeps talking quickly, clutching his own hair with both hands in delight.
- 6–7s (Shot 2): @Khai goes on, bouncing on the mattress so the bedsprings creak.
- 7–8s (Shot 2): @Khai keeps speaking fast, laughing.
- 8–9s (Shot 2): @Khai finishes and closes his mouth, beaming at the hologram.
- 9–10s (Shot 2): @Nova answers slowly and sweetly, folding her small hands.
- 10–11s (CUT to Shot 3): @Nova keeps talking, giving a little bow.
- 11–12s (Shot 3): @Nova goes on gently, waving one tiny hand.
- 12–13s (Shot 3): @Nova finishes and closes her mouth.
- 13–14s (Shot 3): @Nova folds down into the phone screen with a soft violet sparkle.
- 14–15s (Shot 3): @Khai flops back onto the pillow, grinning at the ceiling, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking at a natural, even conversational pace, bright morning greeting): "Chào buổi sáng anh Khải. Bốn trăm tám mươi nghìn đã về ví của anh."
- Turn 2, 4.9–8.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, ecstatic, bouncing on the bed): "Thật á? Ngủ một giấc mà có tiền thật à? Trời ơi, sướng thế này cơ à, Nova!"
- Turn 3, 9.2–13.1s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking slowly and softly, unhurried, with a short natural pause between phrases, sweet, unhurried): "Hẹn gặp lại anh tối nay nhé. Chúc anh một ngày tốt lành."
- Pacing: @Nova speaks at an even everyday pace, then @Khai answers quickly, then @Nova answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a bright cash chime, morning birds, a rooster far away, the electric fan, bedsprings creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 2 (`canh-06/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A tiny street-side bánh mì stall at the mouth of the alley in early morning, 2041: a glass cart with bread loaves, plastic stools on the pavement, steam rising, silent scooters passing, soft gold morning sun.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; white short-sleeved school shirt, navy pleated skirt, white canvas sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot of the siblings at the bánh mì cart, handheld.
- Shot 2, 5–10s: 85mm close-up of the schoolgirl holding a fat bánh mì, locked off.
- Shot 3, 10–15s: 50mm medium shot of the young man winking as he takes a big bite, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai stands at the bánh mì cart in his orange jacket and is already speaking fast, holding out a fat paper-wrapped bánh mì.
- 1–2s (Shot 1): @Khai keeps talking quickly, peeling back the paper to show the filling.
- 2–3s (Shot 1): @Khai goes on, pointing at the fried egg tucked inside.
- 3–4s (Shot 1): @Khai finishes and closes his mouth, pressing the bánh mì into @Linh's hands.
- 4–5s (Shot 1): @Linh in her school uniform weighs the heavy bánh mì and answers with narrowed eyes.
- 5–6s (CUT to Shot 2): @Linh keeps talking, a smile tugging at her lips.
- 6–7s (Shot 2): @Linh goes on, sniffing the warm bread.
- 7–8s (Shot 2): @Linh keeps speaking, raising one eyebrow at her brother.
- 8–9s (Shot 2): @Linh finishes and closes her mouth, waiting.
- 9–10s (Shot 2): @Khai answers breezily, unwrapping a second bánh mì for himself.
- 10–11s (CUT to Shot 3): @Khai keeps talking, winking at her.
- 11–12s (Shot 3): @Khai goes on, gesturing grandly at the cart.
- 12–13s (Shot 3): @Khai finishes and closes his mouth, then takes a huge bite.
- 13–14s (Shot 3): @Linh laughs silently and bites into her own bánh mì, mouth full.
- 14–15s (Shot 3): The two siblings chew side by side in the gold morning light as a scooter glides past. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, proud, showing off): "Đây, bánh mì pa tê thịt nguội, đầy đủ hết, thêm cả trứng. Ăn đi rồi đi học."
- Turn 2, 4.7–8.5s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking at a natural, even conversational pace, suspicious but delighted): "Hôm nay anh trúng số à? Mọi hôm anh toàn mua cho em xôi trắng."
- Turn 3, 9.0–12.5s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, breezy, winking): "Anh được thưởng. Từ giờ ngày nào cũng có bánh mì đầy đủ nhé."
- Pacing: @Khai speaks quickly, then @Linh answers at an even everyday pace, then @Khai answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: sizzling egg on a hot plate, paper bags rustling, a scooter passing, the bánh mì seller's knife on a chopping board. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 3 (`canh-06/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A narrow Hanoi alley at the gate of an old five-storey collective housing block in 2041, daytime: tangled power cables overhead, potted plants, parked silent electric scooters, a peeling yellow wall, laundry hanging from the balconies above.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Hung = Hùng, 35, a loan-shark debt collector; stocky with a thick neck, shaved head, thin moustache, heavy-lidded eyes, tattooed forearms; loud red-and-yellow floral short-sleeved shirt, a thick gold chain, black trousers, leather slip-on shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the delivery rider holding up his translucent phone at the alley gate, locked off.
- Shot 2, 5–10s: 85mm close-up of the debt collector squinting at his own phone, slow push-in.
- Shot 3, 10–15s: 40mm medium two-shot of the rider grinning and the debt collector staring, handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai stands at the alley gate and is already speaking confidently, holding up his translucent phone.
- 1–2s (Shot 1): @Khai keeps talking, turning the glowing screen toward @Hung.
- 2–3s (Shot 1): @Khai goes on, chin raised.
- 3–4s (Shot 1): @Khai finishes and closes his mouth, smiling.
- 4–5s (Shot 1): @Hung pulls out his own phone, glances at it and answers slowly, squinting.
- 5–6s (CUT to Shot 2): @Hung keeps talking, looking from the phone to @Khai and back.
- 6–7s (Shot 2): @Hung goes on, rubbing his thin moustache with one thumb.
- 7–8s (Shot 2): @Hung keeps speaking, eyes narrowing.
- 8–9s (Shot 2): @Hung finishes and closes his mouth, studying @Khai's face.
- 9–10s (Shot 2): @Khai answers fast with a cocky grin, spreading his hands.
- 10–11s (CUT to Shot 3): @Khai keeps talking quickly, tapping his chest.
- 11–12s (Shot 3): @Khai goes on, giving a thumbs-up.
- 12–13s (Shot 3): @Khai finishes and closes his mouth, still grinning.
- 13–14s (Shot 3): @Hung slowly puts his phone away, mouth closed, eyes fixed on the faint violet glow at the back of @Khai's neck.
- 14–15s (Shot 3): @Khai turns and walks his scooter into the gate while @Hung watches him go, silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, confident for once): "Anh Hùng ơi, em chuyển trước năm triệu rồi đấy. Anh kiểm tra đi ạ."
- Turn 2, 4.7–9.4s, spoken on camera by @Hung (man of 35, rough gravelly bass, a slow menacing drawl, speaking slowly and softly, unhurried, with a short natural pause between phrases, suspicious, squinting): "Năm triệu à... Mày lấy đâu ra nhanh thế hả? Đi cướp nhà băng đấy à?"
- Turn 3, 9.9–13.1s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, grinning, cocky): "Em làm ăn chân chính. Thứ Bảy tuần sau em trả nốt, anh yên tâm."
- Pacing: @Khai speaks at an even everyday pace, then @Hung answers slowly and calmly, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a payment notification ping, pigeons on the cables, the radio from a balcony, a scooter beeping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 4 (`canh-06/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The gate of a Hanoi high school at noon, 2041: a green iron gate, flame trees casting dappled shade, bicycles and scooters parked along the wall, students in white shirts in soft focus far behind.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; white short-sleeved school shirt, navy pleated skirt, white canvas sneakers.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm wide shot of the schoolgirl running out of the green school gate toward the delivery rider waiting by his scooter, handheld.
- Shot 2, 5–10s: 50mm medium two-shot of the siblings by the scooter, locked off.
- Shot 3, 10–15s: 85mm close-up of the schoolgirl hugging her brother, her chin on his shoulder, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh runs out through the green school gate, backpack bouncing, and is already speaking fast.
- 1–2s (Shot 1): @Linh keeps talking breathlessly as she reaches @Khai at his scooter.
- 2–3s (Shot 1): @Linh goes on, waving a folded receipt in the air.
- 3–4s (Shot 1): @Linh finishes and closes her mouth, panting and grinning.
- 4–5s (Shot 1): @Khai answers warmly, ruffling the top of her head.
- 5–6s (CUT to Shot 2): @Khai keeps talking, pointing at the school building behind her.
- 6–7s (Shot 2): @Khai goes on, giving a proud nod.
- 7–8s (Shot 2): @Khai keeps speaking, smiling.
- 8–9s (Shot 2): @Khai finishes and closes his mouth.
- 9–10s (Shot 2): @Linh throws her arms around him and answers slowly, her voice cracking.
- 10–11s (CUT to Shot 3): @Linh keeps talking softly, her chin resting on his shoulder.
- 11–12s (Shot 3): @Linh goes on, squeezing him tighter.
- 12–13s (Shot 3): @Linh finishes and closes her mouth, eyes shut.
- 13–14s (Shot 3): @Khai hugs her back, his face over her shoulder going still and thoughtful, mouth closed.
- 14–15s (Shot 3): Dappled flame-tree shade moves over the siblings as they hold the hug in front of the gate. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.8s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking quickly in short lively phrases, every word still clear, running up, breathless with joy): "Anh ơi! Cô bảo nhà mình đóng tiền ôn thi rồi! Anh đóng lúc nào thế?"
- Turn 2, 4.3–8.6s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, warm, proud): "Sáng nay. Giờ thì cứ yên tâm mà học đi, đỗ đại học cho anh nhờ nhé."
- Turn 3, 9.1–12.8s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking slowly and softly, unhurried, with a short natural pause between phrases, hugging him, voice cracking): "Em thương anh lắm. Anh đừng làm việc vất vả quá nữa nhé."
- Pacing: @Linh speaks quickly, then @Khai answers at an even everyday pace, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the school bell ringing, students chattering far off, leaves rustling in the flame trees, a bicycle bell. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 1 (`canh-07/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, early morning, pale sunlight through the barred window and a small mirror above a basin by the door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; white short-sleeved school shirt, navy pleated skirt, white canvas sneakers.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the schoolgirl stopping by the door with her backpack, locked off.
- Shot 2, 5–10s: 85mm close-up of the young man at the small mirror with toothpaste foam on his lips, handheld.
- Shot 3, 10–15s: 40mm medium two-shot of the siblings by the basin, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh stops by the door with her backpack on one shoulder and is already speaking, staring at her brother.
- 1–2s (Shot 1): @Linh keeps talking, tilting her head as if listening to an echo.
- 2–3s (Shot 1): @Linh goes on, pointing at him with her house key.
- 3–4s (Shot 1): @Linh finishes and closes her mouth.
- 4–5s (Shot 1): @Khai turns from the little mirror, toothbrush in his mouth, and answers fast through the foam.
- 5–6s (CUT to Shot 2): @Khai keeps talking quickly, waving the toothbrush.
- 6–7s (Shot 2): @Khai goes on, shaking his head and spraying a little foam.
- 7–8s (Shot 2): @Khai keeps speaking, laughing.
- 8–9s (Shot 2): @Khai finishes and closes his mouth, foam on his lips.
- 9–10s (Shot 2): @Linh answers in a teasing voice, rolling her eyes.
- 10–11s (CUT to Shot 3): @Linh keeps talking, humming a few notes in the air with one finger as if conducting.
- 11–12s (Shot 3): @Linh goes on, smirking.
- 12–13s (Shot 3): @Linh finishes and closes her mouth.
- 13–14s (Shot 3): @Khai stops brushing, mouth closed, the toothbrush hanging still.
- 14–15s (Shot 3): @Khai stares at his sister, then slowly turns back toward the mirror. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking at a natural, even conversational pace, curious, stopping mid-step): "Anh hát bài gì thế? Nghe lạ lạ. Hình như là tiếng Nhật đúng không anh?"
- Turn 2, 4.9–8.1s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, mouth full of toothpaste foam): "Hả? Anh hát gì đâu. Anh biết tiếng Nhật bao giờ, em nghe nhầm đấy."
- Turn 3, 8.6–12.6s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking at a natural, even conversational pace, teasing, rolling her eyes): "Thôi đi, anh hát rõ ràng thế cơ mà, lại còn đúng giai điệu nữa cơ."
- Pacing: @Linh speaks at an even everyday pace, then @Khai answers quickly, then @Linh answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a toothbrush scrubbing, water running into a basin, morning birds, a radio news jingle from a neighbour. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 2 (`canh-07/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, early morning, pale sunlight through the barred window and a small mirror above a basin by the door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; white short-sleeved school shirt, navy pleated skirt, white canvas sneakers.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young man's reflection in the small mirror, locked off.
- Shot 2, 5–10s: 35mm wide shot of the schoolgirl opening the door to the stairwell, handheld.
- Shot 3, 10–15s: 50mm medium shot of the young man alone at the basin as the door swings shut, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai stares at his own reflection and is already speaking slowly, foam still on his lips.
- 1–2s (Shot 1): @Khai keeps talking softly, his eyes searching the mirror.
- 2–3s (Shot 1): @Khai goes on, his brow furrowing.
- 3–4s (Shot 1): @Khai keeps speaking, touching the glass with one fingertip.
- 4–5s (Shot 1): @Khai finishes and closes his mouth.
- 5–6s (CUT to Shot 2): @Linh pulls the door open and answers fast over her shoulder, already half outside.
- 6–7s (Shot 2): @Linh keeps talking quickly, waving her bánh mì in its paper bag.
- 7–8s (Shot 2): @Linh goes on, stepping into the stairwell.
- 8–9s (Shot 2): @Linh finishes and closes her mouth, grinning back at him.
- 9–10s (Shot 2): @Khai answers without turning, his eyes still on the mirror.
- 10–11s (CUT to Shot 3): @Khai keeps talking in a distracted voice, lifting one hand in a vague wave.
- 11–12s (Shot 3): @Khai finishes and closes his mouth.
- 12–13s (Shot 3): The door swings shut behind @Linh with a click.
- 13–14s (Shot 3): @Khai stands alone at the basin, the toothbrush forgotten in his hand, mouth closed.
- 14–15s (Shot 3): @Khai leans closer to the mirror, studying his own eyes as if they belonged to a stranger. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, unsettled, staring at the mirror): "Đúng giai điệu... Lạ thật. Anh cứ như đã nghe bài này cả nghìn lần rồi ấy."
- Turn 2, 5.7–9.1s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking quickly in short lively phrases, every word still clear, breezy, already leaving): "Chắc anh xem phim hoạt hình Nhật lúc chạy xe chứ gì. Em đi học đây!"
- Turn 3, 9.6–12.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, distracted, automatic): "Ừ, đi cẩn thận nhé. Nhớ ăn hết cái bánh mì đấy nhé."
- Pacing: @Khai speaks slowly and calmly, then @Linh answers quickly, then @Khai answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water dripping from the tap, the door latch clicking, footsteps clattering down a concrete stairwell, morning birds. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 3 (`canh-07/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, early morning, pale sunlight through the barred window and a small mirror above a basin by the door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 100mm extreme close-up of the young man's eyes in the mirror, locked off.
- Shot 2, 5–10s: 50mm medium shot of the young man pacing between the basin and the bed, handheld.
- Shot 3, 10–15s: 85mm close-up of the young man sitting down hard on the edge of the bed, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking slowly to his own eyes in the mirror, his voice dreamy.
- 1–2s (Shot 1): @Khai keeps talking softly as the reflection flickers for a split second with a faint cyan tint.
- 2–3s (Shot 1): @Khai goes on, his eyelids half closing.
- 3–4s (Shot 1): @Khai keeps speaking in a hush, swaying slightly.
- 4–5s (Shot 1): @Khai finishes and closes his mouth.
- 5–6s (CUT to Shot 2): @Khai jerks away from the mirror and starts speaking fast, shaking his head.
- 6–7s (Shot 2): @Khai keeps talking quickly as he paces toward the bed.
- 7–8s (Shot 2): @Khai goes on, pressing his knuckles to his forehead.
- 8–9s (Shot 2): @Khai keeps speaking, turning sharply at the bed.
- 9–10s (Shot 2): @Khai finishes and closes his mouth, breathing hard.
- 10–11s (CUT to Shot 3): @Khai sits down hard on the edge of the bed and whispers slowly.
- 11–12s (Shot 3): @Khai keeps speaking in a whisper, staring at the floor.
- 12–13s (Shot 3): @Khai goes on, his voice barely audible.
- 13–14s (Shot 3): @Khai finishes and closes his mouth.
- 14–15s (Shot 3): @Khai sits motionless, hands gripping the mattress edge, while the tap drips behind him. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, spoken on camera by @Khai alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–4.9s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, dreamy, half to himself): "Bài này... Ai đã hát cho mình nghe nhỉ? Một người đàn bà... giọng rất nhẹ."
- Part 2, 5.4–9.2s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, shaking it off, agitated): "Không, không phải. Mẹ mình có biết tiếng Nhật đâu. Mình chưa bao giờ nghe bài này cả."
- Part 3, 9.7–13.1s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, whispering, afraid of the answer): "Thế mà sao mình lại thuộc lòng từng chữ một thế này?"
- Pacing: @Khai speaks slowly and calmly, then @Khai continues quickly, then @Khai continues slowly and calmly; the change of speed is clearly audible.
- Throughout, @Khai's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water dripping from the tap, the electric fan, a faint distorted echo of a soft female voice that fades instantly, morning birds. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 4 (`canh-07/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, early morning, pale sunlight through the barred window and a small mirror above a basin by the door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- @Nova = Nova, the NeuroRent app's holographic assistant; a softly glowing translucent violet hologram of a young woman about a hand's height tall, standing on a beam of light above a phone screen, a smooth calm face with a gentle fixed smile, sleek hair in a high knot, faint horizontal scan lines through her body; a simple fitted violet light-dress.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium shot of the young man on the bed holding up his phone, locked off.
- Shot 2, 5–10s: 85mm close-up of the violet hologram answering above the phone, slow push-in.
- Shot 3, 10–15s: 50mm over-the-shoulder shot from behind the hologram onto the young man's suspicious face, handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai holds his phone up in front of him and is already speaking carefully to it.
- 1–2s (Shot 1): @Khai keeps talking as @Nova rises from the screen as a hand-tall violet hologram.
- 2–3s (Shot 1): @Khai goes on, watching her closely.
- 3–4s (Shot 1): @Khai keeps speaking, narrowing his eyes.
- 4–5s (Shot 1): @Khai finishes and closes his mouth.
- 5–6s (CUT to Shot 2): @Nova answers slowly in a pleasant voice, hands folded.
- 6–7s (Shot 2): @Nova keeps talking, her smile never moving.
- 7–8s (Shot 2): @Nova goes on as a small violet padlock icon spins beside her.
- 8–9s (Shot 2): @Nova keeps speaking gently.
- 9–10s (Shot 2): @Nova finishes and closes her mouth.
- 10–11s (CUT to Shot 3): @Khai answers fast, leaning in sharply.
- 11–12s (Shot 3): @Khai keeps talking quickly, jabbing a finger at the hologram.
- 12–13s (Shot 3): @Khai finishes and closes his mouth, waiting.
- 13–14s (Shot 3): @Nova stays silent, smiling, as her figure flickers once.
- 14–15s (Shot 3): @Khai stares at the frozen smiling hologram, jaw tight, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, careful, testing): "Nova, cho tôi hỏi. Thuê não thì có làm người ta biết thêm những thứ lạ không?"
- Turn 2, 5.2–9.9s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking slowly and softly, unhurried, with a short natural pause between phrases, pleasant, evasive): "Dữ liệu của khách hàng được mã hóa tuyệt đối. Anh không thể tiếp cận chúng."
- Turn 3, 10.4–13.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, sharp, catching the slip): "Dữ liệu gì cơ? Cô bảo chỉ thuê phần trống thôi cơ mà?"
- Pacing: @Khai speaks at an even everyday pace, then @Nova answers slowly and calmly, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft hologram chime, the projected light humming, the electric fan, a motorbike starting in the alley. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 1 (`canh-08/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The glass entrance of a modern office tower on a busy Hanoi street in 2041, daytime: a metal door keypad beside the glass door, delivery scooters at the kerb, traffic passing, and across the street a huge slim holographic billboard screen glowing in the daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium shot of the delivery rider at the glass door with a parcel, phone to his ear, handheld.
- Shot 2, 5–10s: 85mm close-up of the delivery rider frowning at the keypad, locked off.
- Shot 3, 10–15s: 100mm extreme close-up of his finger pressing the keypad buttons on its own, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai stands at the glass door holding a parcel, phone to his ear, and is already speaking fast.
- 1–2s (Shot 1): @Khai keeps talking quickly, glancing up at the tower.
- 2–3s (Shot 1): @Khai goes on, pulling the phone away to stare at the unanswered call.
- 3–4s (Shot 1): @Khai finishes and closes his mouth, sighing.
- 4–5s (Shot 1): @Khai turns to the metal keypad and starts muttering in a frustrated voice.
- 5–6s (CUT to Shot 2): @Khai keeps talking, tapping the parcel against his thigh.
- 6–7s (Shot 2): @Khai goes on, frowning at the grid of buttons.
- 7–8s (Shot 2): @Khai keeps speaking, scratching his head.
- 8–9s (Shot 2): @Khai finishes and closes his mouth.
- 9–10s (Shot 2): @Khai's right hand rises by itself and presses four buttons quickly; he speaks slowly, stunned.
- 10–11s (CUT to Shot 3): @Khai keeps talking softly, staring at his own moving finger.
- 11–12s (Shot 3): @Khai goes on in a whisper as his finger presses one last key.
- 12–13s (Shot 3): @Khai finishes and closes his mouth.
- 13–14s (Shot 3): The lock clicks and the glass door swings open a few centimetres.
- 14–15s (Shot 3): @Khai stares at his hand as if it belonged to someone else, the parcel slipping in his grip. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, spoken on camera by @Khai alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–4.0s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, into his phone, hurried): "Alô, chị ơi, em giao hàng đây ạ. Chị không nghe máy à? Cửa khóa mã rồi."
- Part 2, 4.5–8.5s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, muttering, frustrated): "Thôi chết, đơn này mà trễ là bị trừ điểm. Mã cửa là bao nhiêu nhỉ..."
- Part 3, 9.0–12.9s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, stunned, watching his own hand): "Ơ... Sao tay mình lại tự bấm thế này? Mình đâu có biết mã."
- Pacing: @Khai speaks quickly, then @Khai continues at an even everyday pace, then @Khai continues slowly and calmly; the change of speed is clearly audible.
- Throughout, @Khai's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone ringing out unanswered, city traffic, the beep of keypad buttons, a heavy electronic lock clicking open. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 2 (`canh-08/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 11s; it intercuts the two places or times named in the shot list, each shot keeping its own place and light, with sound continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The glass entrance of a modern office tower on a busy Hanoi street in 2041, daytime: a metal door keypad beside the glass door, delivery scooters at the kerb, traffic passing, and across the street a huge slim holographic billboard screen glowing in the daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- Extra: a young woman's slender pale hand with short nails, seen only in the cold cyan memory shots, pressing the same keypad
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the delivery rider backing away from the open glass door in daylight, handheld.
- Shot 2, 4–7s: 100mm extreme close-up memory shot in cold cyan-blue glitching light of a young woman's slender hand pressing the same keypad, locked off.
- Shot 3, 7–11s: 85mm close-up of the delivery rider in daylight, eyes unfocused, slow push-in.
- Shot 4, 11–15s: 40mm medium shot of the delivery rider staring at his own open palm on the busy pavement, handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Each shot keeps the lighting of its own place and time; faces, wardrobe and props stay consistent; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai backs away from the open door and is already speaking fast, shaking his head.
- 1–2s (Shot 1): @Khai keeps talking quickly, the parcel clutched to his chest.
- 2–3s (Shot 1): @Khai goes on, looking up at the tower's glass facade.
- 3–4s (Shot 1): @Khai finishes the burst, closes his mouth, and the picture flickers.
- 4–5s (CUT to Shot 2): In a cold cyan memory, a young woman's slender hand with short nails presses the keypad while @Khai's voice starts again slowly over it.
- 5–6s (Shot 2): The trembling hand presses the last key in the glitching cyan light as @Khai keeps speaking slowly.
- 6–7s (Shot 2): The memory image shudders with digital noise and breaks apart.
- 7–8s (CUT to Shot 3): Back in daylight, @Khai goes on slowly, his eyes unfocused.
- 8–9s (Shot 3): @Khai keeps speaking in a daze, his lips barely moving.
- 9–10s (Shot 3): @Khai finishes and closes his mouth.
- 10–11s (Shot 3): @Khai lifts his open palm and starts speaking again at an even pace, staring at it.
- 11–12s (CUT to Shot 4): @Khai keeps talking, flexing his fingers.
- 12–13s (Shot 4): @Khai goes on, turning his hand over.
- 13–14s (Shot 4): @Khai finishes and closes his mouth.
- 14–15s (Shot 4): @Khai stands frozen on the busy pavement, staring at his palm while scooters stream past behind him. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, spoken on camera by @Khai alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–4.0s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, panicked, backing away): "Mở rồi á? Không đúng. Mình chưa bao giờ đến tòa nhà này. Không thể nào được."
- Part 2, 4.5–9.0s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, dazed, recalling): "Cái tay vừa nãy... là tay một người con gái. Móng tay cắt ngắn, run run."
- Part 3, 9.5–12.8s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, trying to make sense of it): "Mình nhìn thấy nó rõ ràng, như thể chính mình đang bấm vậy."
- Pacing: @Khai speaks quickly, then @Khai continues slowly and calmly, then @Khai continues at an even everyday pace; the change of speed is clearly audible.
- Throughout, @Khai's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: city traffic, a glitchy electronic whine during the memory shots, the keypad beeping in an echo, his quickened breathing. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 3 (`canh-08/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; it intercuts the two places or times named in the shot list, each shot keeping its own place and light, with sound continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The glass entrance of a modern office tower on a busy Hanoi street in 2041, daytime: a metal door keypad beside the glass door, delivery scooters at the kerb, traffic passing, and across the street a huge slim holographic billboard screen glowing in the daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Huy = Trịnh Huy, 45, the polished CEO of NeuroRent; tall and trim, a smooth pale face, slicked-back black hair greying at the temples, a cold confident smile; tailored navy suit, white open-collar shirt, a slim silver watch.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 28mm wide low-angle shot of the giant holographic billboard across the street showing the polished CEO speaking, locked off.
- Shot 2, 5–10s: 85mm close-up of the delivery rider staring up at the billboard, handheld.
- Shot 3, 10–15s: 50mm medium shot of the CEO on the billboard pointing out at the street, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Each shot keeps the lighting of its own place and time; faces, wardrobe and props stay consistent; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Across the street, @Huy, huge on a slim holographic billboard, is already speaking in a polished advertising voice.
- 1–2s (Shot 1): @Huy keeps talking, smiling confidently down at the traffic.
- 2–3s (Shot 1): @Huy goes on, opening one hand as a violet logo of a brain with an empty square glows beside him.
- 3–4s (Shot 1): @Huy keeps speaking, giving a small reassuring nod.
- 4–5s (Shot 1): @Huy finishes and closes his mouth, still smiling.
- 5–6s (CUT to Shot 2): @Khai, standing by his scooter, stares up at the billboard and starts speaking slowly.
- 6–7s (Shot 2): @Khai keeps talking softly, his eyes narrowing.
- 7–8s (Shot 2): @Khai goes on, his face tightening.
- 8–9s (Shot 2): @Khai keeps speaking in a low voice, taking half a step back.
- 9–10s (Shot 2): @Khai finishes and closes his mouth.
- 10–11s (CUT to Shot 3): @Huy on the billboard answers fast and upbeat, pointing straight out at the street.
- 11–12s (Shot 3): @Huy keeps talking quickly, his finger seeming to aim right at @Khai.
- 12–13s (Shot 3): @Huy goes on, flashing a wide smile.
- 13–14s (Shot 3): @Huy finishes and closes his mouth, the smile frozen on the giant screen.
- 14–15s (Shot 3): @Khai stays rooted beside his scooter, staring up at the frozen giant face, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.1s, spoken on camera by @Huy (man of 45, smooth confident baritone, polished and cold, speaking at a natural, even conversational pace, polished advertising tone): "Tôi là Trịnh Huy. NeuroRent trao giá trị cho từng giấc ngủ của bạn. Ngủ ngon, sống khỏe."
- Turn 2, 5.6–9.8s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, staring, uneasy): "Cái mặt này... Mình đã nhìn thấy cái mặt này ở đâu rồi thì phải."
- Turn 3, 10.3–13.1s, spoken on camera by @Huy (man of 45, smooth confident baritone, polished and cold, speaking quickly in short lively phrases, every word still clear, upbeat, pointing at the viewer): "Hơn ba triệu người Việt đã tin dùng. Còn bạn thì sao nào?"
- Pacing: @Huy speaks at an even everyday pace, then @Khai answers slowly and calmly, then @Huy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a huge echoing advertising voice across the street, traffic, a soft corporate chime, a bus braking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 4 (`canh-08/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; it intercuts the two places or times named in the shot list, each shot keeping its own place and light, with sound continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The glass entrance of a modern office tower on a busy Hanoi street in 2041, daytime: a metal door keypad beside the glass door, delivery scooters at the kerb, traffic passing, and across the street a huge slim holographic billboard screen glowing in the daylight. Intercut with cold cyan memory shots: Memory flashback graded cold cyan-blue with faint flickering glitch: a dim abandoned apartment in an old collective housing block at night, a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, dust floating in the light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Huy = Trịnh Huy, 45, the polished CEO of NeuroRent; tall and trim, a smooth pale face, slicked-back black hair greying at the temples, a cold confident smile; tailored navy suit, white open-collar shirt, a slim silver watch.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 85mm close-up memory shot in cold cyan glitching light of the CEO shouting straight into the lens, handheld.
- Shot 2, 4–8s: 50mm medium shot in daylight of the delivery rider doubled over, gripping his scooter, handheld.
- Shot 3, 8–12s: 100mm extreme close-up memory shot in cold cyan light of the CEO's face, suddenly calm, very close to the lens, locked off.
- Shot 4, 12–15s: 35mm wide shot of the busy pavement with the delivery rider small and alone beside his scooter, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Each shot keeps the lighting of its own place and time; faces, wardrobe and props stay consistent; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In a cold cyan memory, @Huy's face fills the frame in his navy suit and he is already shouting straight into the lens.
- 1–2s (Shot 1): @Huy keeps shouting fast, a vein standing out on his temple, the image glitching.
- 2–3s (Shot 1): @Huy goes on, jabbing a finger toward the lens.
- 3–4s (Shot 1): @Huy finishes, closes his mouth and the memory tears apart into static.
- 4–5s (CUT to Shot 2): In daylight @Khai doubles over, gripping his scooter's handlebar, and speaks slowly between gasps.
- 5–6s (Shot 2): @Khai keeps talking, his knuckles white on the handlebar.
- 6–7s (Shot 2): @Khai goes on, shutting his eyes tight.
- 7–8s (Shot 2): @Khai finishes and closes his mouth, panting.
- 8–9s (CUT to Shot 3): In the cyan memory @Huy leans in very close, now perfectly calm, and speaks in a cold, even voice.
- 9–10s (Shot 3): @Huy keeps talking softly, lifting one hand as if to smooth someone's hair.
- 10–11s (Shot 3): @Huy goes on, his smile returning.
- 11–12s (Shot 3): @Huy finishes and closes his mouth, staring into the lens.
- 12–13s (CUT to Shot 4): Back on the bright pavement, @Khai straightens up slowly, breathing hard.
- 13–14s (Shot 4): @Khai looks around at the indifferent crowd, mouth closed, a hand pressed to the back of his neck.
- 14–15s (Shot 4): @Khai stands small and alone beside his scooter as traffic streams past. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.9s, spoken on camera by @Huy (man of 45, smooth confident baritone, polished and cold, speaking quickly in short lively phrases, every word still clear, shouting in the memory, face twisted): "Cô im đi! Cô không được nói với ai hết, nghe chưa? Cô có hiểu không?"
- Turn 2, 4.4–8.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, panting, gripping his scooter): "Không... Hắn đang hét vào mặt ai thế? Sao mình lại thấy sợ đến thế này?"
- Turn 3, 9.4–13.0s, spoken on camera by @Huy (man of 45, smooth confident baritone, polished and cold, speaking at a natural, even conversational pace, suddenly calm and cold in the memory): "Vy, nghe anh nói này. Chuyện tối nay chưa từng xảy ra, rõ chưa?"
- Pacing: @Huy speaks quickly, then @Khai answers slowly and calmly, then @Huy answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a sharp glitch burst, a muffled distorted shout echoing, city traffic swelling and dropping away, a heartbeat thudding. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 1 (`canh-09/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, deep at night, lit only by orange street light through the barred window and a small yellow bedside lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the young man sitting against the white wall holding his phone close to his mouth, locked off.
- Shot 2, 5–10s: 85mm close-up of the young man speaking into the phone, handheld.
- Shot 3, 10–15s: 100mm extreme close-up of the peeled patch on the desk blinking violet beside a cold cup of coffee, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai sits against the white wall holding his phone close to his mouth and is already speaking steadily into it.
- 1–2s (Shot 1): @Khai keeps talking, glancing at the small red recording dot on the screen.
- 2–3s (Shot 1): @Khai goes on, rubbing his tired eyes with his free hand.
- 3–4s (Shot 1): @Khai finishes and closes his mouth, taking a breath.
- 4–5s (Shot 1): @Khai starts again fast, counting things off on his fingers.
- 5–6s (CUT to Shot 2): @Khai keeps talking quickly, his voice rising.
- 6–7s (Shot 2): @Khai goes on, tapping his own temple hard.
- 7–8s (Shot 2): @Khai keeps speaking fast, staring at the scrawled wall beside him.
- 8–9s (Shot 2): @Khai finishes and closes his mouth, breathing hard.
- 9–10s (Shot 2): @Khai lowers the phone and speaks slowly and quietly, eyes on the desk.
- 10–11s (CUT to Shot 3): @Khai keeps talking softly, his jaw set.
- 11–12s (Shot 3): @Khai finishes and closes his mouth.
- 12–13s (Shot 3): On the desk the peeled patch blinks violet beside a cold cup of coffee.
- 13–14s (Shot 3): The patch keeps blinking slowly, like a heartbeat, in the lamplight.
- 14–15s (Shot 3): The blinking light is reflected faintly in the black surface of the coffee. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, spoken on camera by @Khai alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–4.4s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, recording himself, steady): "Ngày thứ sáu. Tôi tên là Khải. Tôi đang ghi âm lại, phòng khi tôi quên."
- Part 2, 4.9–9.3s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, listing it all out, agitated): "Tôi biết những thứ tôi chưa từng học. Một bài hát tiếng Nhật. Một mã cửa. Mặt một người đàn ông."
- Part 3, 9.8–12.3s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, determined): "Tối nay... tôi sẽ không ngủ. Nhất định không."
- Pacing: @Khai speaks at an even everyday pace, then @Khai continues quickly, then @Khai continues slowly and calmly; the change of speed is clearly audible.
- Throughout, @Khai's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft recording beep, the electric fan, a cup set down on wood, a gecko clicking on the ceiling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 2 (`canh-09/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, deep at night, lit only by orange street light through the barred window and a small yellow bedside lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; a loose pale-blue T-shirt and grey cotton shorts, hair down over her shoulders.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Linh and @Khai wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm low-angle shot up at the schoolgirl leaning over the loft rail, locked off.
- Shot 2, 5–10s: 85mm close-up of the young man against the wall, handheld.
- Shot 3, 10–15s: 40mm medium two-shot from the side of the loft and the young man below, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh pulls the loft curtain aside, leans over the rail and is already speaking sleepily.
- 1–2s (Shot 1): @Linh keeps talking, squinting at the bright desk lamp.
- 2–3s (Shot 1): @Linh goes on, pointing at the blinking patch on the desk.
- 3–4s (Shot 1): @Linh finishes and closes her mouth.
- 4–5s (Shot 1): @Khai answers fast without looking up, waving one hand.
- 5–6s (CUT to Shot 2): @Khai keeps talking quickly, forcing a yawn that doesn't come.
- 6–7s (Shot 2): @Khai goes on, pointing up at her pillow.
- 7–8s (Shot 2): @Khai finishes and closes his mouth.
- 8–9s (Shot 2): @Linh answers slowly, hesitating, hugging the rail.
- 9–10s (Shot 2): @Linh keeps talking softly, her eyes wide.
- 10–11s (CUT to Shot 3): @Linh goes on, glancing at the scrawled wall.
- 11–12s (Shot 3): @Linh keeps speaking in a small voice.
- 12–13s (Shot 3): @Linh finishes and closes her mouth.
- 13–14s (Shot 3): @Khai slowly lifts his head to look at her, mouth closed.
- 14–15s (Shot 3): The two siblings stare at each other across the dim room. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking at a natural, even conversational pace, sleepy, worried): "Anh ơi, hai giờ sáng rồi. Sao anh còn ngồi đấy? Anh không dán cái máy à?"
- Turn 2, 5.2–8.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, too quick, waving her off): "Anh không buồn ngủ đâu. Em cứ ngủ đi, mai còn đi học sớm."
- Turn 3, 8.7–13.5s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking slowly and softly, unhurried, with a short natural pause between phrases, hesitant, frightened): "Dạo này anh lạ lắm. Đêm nào anh cũng nói mớ bằng tiếng gì em không hiểu."
- Pacing: @Linh speaks at an even everyday pace, then @Khai answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a curtain sliding on its rail, the wooden loft creaking, the electric fan, a distant night bus. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 3 (`canh-09/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, deep at night, lit only by orange street light through the barred window and a small yellow bedside lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; a loose pale-blue T-shirt and grey cotton shorts, hair down over her shoulders.
- Wardrobe: in this shot @Khai and @Linh wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 85mm close-up of the young man looking up from the wall, locked off.
- Shot 2, 4–10s: 50mm medium shot of the schoolgirl leaning over the loft rail, handheld.
- Shot 3, 10–15s: 35mm wide shot of the dim room as the schoolgirl draws the curtain and the young man stays below, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking slowly and quietly, looking up at the loft.
- 1–2s (Shot 1): @Khai keeps talking, his voice dropping.
- 2–3s (Shot 1): @Khai finishes and closes his mouth, waiting.
- 3–4s (Shot 1): @Khai sits very still, eyes fixed on his sister.
- 4–5s (CUT to Shot 2): @Linh answers in an uneasy voice, gripping the rail.
- 5–6s (Shot 2): @Linh keeps talking, glancing around the dark room.
- 6–7s (Shot 2): @Linh goes on, whispering the name.
- 7–8s (Shot 2): @Linh keeps speaking softly, hugging herself.
- 8–9s (Shot 2): @Linh finishes and closes her mouth.
- 9–10s (Shot 2): @Khai answers fast, shaking his head and waving her off.
- 10–11s (CUT to Shot 3): @Khai keeps talking quickly, forcing a laugh.
- 11–12s (Shot 3): @Khai goes on, pointing at her pillow.
- 12–13s (Shot 3): @Khai keeps speaking, his smile stiff.
- 13–14s (Shot 3): @Khai finishes and closes his mouth as @Linh slowly pulls the curtain shut.
- 14–15s (Shot 3): @Khai sits alone against the wall, his smile gone, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–2.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, dreading): "Anh nói mớ á? Anh nói những gì thế?"
- Turn 2, 3.4–7.9s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking at a natural, even conversational pace, uneasy, whispering the name): "Em không hiểu hết. Chỉ có một cái tên. Anh cứ gọi mãi... Vy, Vy ơi, anh ạ."
- Turn 3, 8.4–12.4s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, brushing it off, rattled): "Vy á? Anh không quen ai tên là Vy cả. Thôi, em ngủ đi, đừng nghĩ linh tinh nữa."
- Pacing: @Khai speaks slowly and calmly, then @Linh answers at an even everyday pace, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the electric fan, a gecko clicking, a faint glitchy whisper that fades instantly, the loft creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 4 (`canh-09/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, deep at night, lit only by orange street light through the barred window and a small yellow bedside lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young man's drooping eyes, locked off.
- Shot 2, 5–10s: 40mm medium shot of the young man shaking himself and rubbing his face, handheld.
- Shot 3, 10–15s: 35mm wide shot of the dim room as the young man slides sideways down the wall into sleep, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking in a slow mumble, his eyelids drooping as he sits against the wall.
- 1–2s (Shot 1): @Khai keeps talking, his head nodding forward.
- 2–3s (Shot 1): @Khai goes on, jerking his head back up.
- 3–4s (Shot 1): @Khai keeps speaking softly, blinking hard.
- 4–5s (Shot 1): @Khai finishes and closes his mouth.
- 5–6s (CUT to Shot 2): @Khai rubs his face with both hands and talks at an even pace, trying to wake himself.
- 6–7s (Shot 2): @Khai keeps talking, patting his own cheeks.
- 7–8s (Shot 2): @Khai goes on, glancing at the phone screen glowing in his lap.
- 8–9s (Shot 2): @Khai keeps speaking, sitting up straighter.
- 9–10s (Shot 2): @Khai finishes and closes his mouth.
- 10–11s (CUT to Shot 3): @Khai's head sinks again and he murmurs slowly, almost asleep.
- 11–12s (Shot 3): @Khai keeps murmuring, his eyes closing.
- 12–13s (Shot 3): @Khai goes on in a barely audible voice, his body tilting sideways.
- 13–14s (Shot 3): @Khai finishes and closes his mouth as his shoulder slides down the wall.
- 14–15s (Shot 3): @Khai lies asleep against the wall while a faint cyan light flickers across his closed eyelids. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, spoken on camera by @Khai alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–4.1s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, mumbling, eyelids drooping): "Không được ngủ. Không được ngủ đâu. Mở mắt ra nào, Khải ơi..."
- Part 2, 4.6–9.6s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, slapping himself awake with words): "Ba giờ rồi đấy. Chỉ còn mấy tiếng nữa là trời sáng thôi. Cố lên, cố thêm một chút nữa."
- Part 3, 10.1–14.0s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, drifting off, barely audible): "Chỉ nhắm mắt một chút thôi... một chút xíu thôi mà, không sao đâu..."
- Pacing: @Khai speaks slowly and calmly, then @Khai continues at an even everyday pace, then @Khai continues slowly and calmly; the change of speed is clearly audible.
- Throughout, @Khai's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the electric fan slowing, a clock ticking, his breathing getting slower and deeper, a faint rising cyan hum. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 1 (`canh-10/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
Memory flashback graded cold cyan-blue with faint flickering glitch: a dim abandoned apartment in an old collective housing block at night, a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, dust floating in the light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Lam = Lâm, 58, NeuroRent's chief engineer; thin and slightly hunched, balding with grey hair at the sides, black-rimmed glasses, a kind tired face; rumpled white shirt with rolled sleeves, grey trousers, brown leather shoes.
- @Huy = Trịnh Huy, 45, the polished CEO of NeuroRent; tall and trim, a smooth pale face, slicked-back black hair greying at the temples, a cold confident smile; tailored navy suit, white open-collar shirt, a slim silver watch.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot in cold cyan light of the engineer by the heavy table clutching a folder, handheld.
- Shot 2, 5–10s: 85mm close-up of the CEO by the door, slow push-in.
- Shot 3, 10–15s: 40mm medium two-shot of the two men across the heavy table, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the cold cyan memory, @Lam stands by the heavy table clutching a folder and is already speaking fast, his glasses flashing.
- 1–2s (Shot 1): @Lam keeps talking quickly, shaking the folder at @Huy.
- 2–3s (Shot 1): @Lam goes on, his voice cracking with emotion.
- 3–4s (Shot 1): @Lam finishes and closes his mouth, breathing hard.
- 4–5s (Shot 1): @Huy, by the door in his navy suit, answers slowly with a cold smile.
- 5–6s (CUT to Shot 2): @Huy keeps talking calmly, gesturing toward a chair.
- 6–7s (Shot 2): @Huy goes on, adjusting his silver watch.
- 7–8s (Shot 2): @Huy keeps speaking, his smile never reaching his eyes.
- 8–9s (Shot 2): @Huy finishes and closes his mouth.
- 9–10s (Shot 2): @Lam answers in a trembling voice, opening the folder to a page of photos.
- 10–11s (CUT to Shot 3): @Lam keeps talking, holding up a photo of an old woman.
- 11–12s (Shot 3): @Lam goes on, his hand shaking.
- 12–13s (Shot 3): @Lam keeps speaking, slamming the folder shut on the table.
- 13–14s (Shot 3): @Lam finishes and closes his mouth, glaring.
- 14–15s (Shot 3): @Huy's smile fades as the cyan picture flickers with a faint glitch. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Lam (man of 58, thin tired tenor, earnest and shaky, speaking quickly in short lively phrases, every word still clear, agitated, clutching a folder): "Anh Huy, tôi không làm nữa. Những người đó không phải máy chủ. Họ là con người!"
- Turn 2, 4.7–9.0s, spoken on camera by @Huy (man of 45, smooth confident baritone, polished and cold, speaking slowly and softly, unhurried, with a short natural pause between phrases, calm, with a cold smile): "Anh Lâm, ngồi xuống đi. Không ai bị hại cả. Họ ngủ, họ có tiền."
- Turn 3, 9.5–14.3s, spoken on camera by @Lam (man of 58, thin tired tenor, earnest and shaky, speaking at a natural, even conversational pace, trembling with anger): "Có bà cụ không còn nhớ nổi tên con gái mình. Thế mà bảo không ai bị hại?"
- Pacing: @Lam speaks quickly, then @Huy answers slowly and calmly, then @Lam answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a low glitchy drone, muffled echoing voices, the curtain flapping in a draught, papers rustling in a folder. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 2 (`canh-10/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
Memory flashback graded cold cyan-blue with faint flickering glitch: a dim abandoned apartment in an old collective housing block at night, a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, dust floating in the light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Huy = Trịnh Huy, 45, the polished CEO of NeuroRent; tall and trim, a smooth pale face, slicked-back black hair greying at the temples, a cold confident smile; tailored navy suit, white open-collar shirt, a slim silver watch.
- @Lam = Lâm, 58, NeuroRent's chief engineer; thin and slightly hunched, balding with grey hair at the sides, black-rimmed glasses, a kind tired face; rumpled white shirt with rolled sleeves, grey trousers, brown leather shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the engineer onto the CEO, locked off.
- Shot 2, 5–10s: 85mm close-up of the engineer, defiant, handheld.
- Shot 3, 10–15s: 40mm medium two-shot as the CEO steps slowly toward the engineer, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Huy is already speaking in a cold, measured voice, hands in his pockets.
- 1–2s (Shot 1): @Huy keeps talking, tilting his head.
- 2–3s (Shot 1): @Huy goes on, his eyes hard.
- 3–4s (Shot 1): @Huy finishes and closes his mouth.
- 4–5s (Shot 1): @Lam answers fast and defiant, hugging the folder to his chest.
- 5–6s (CUT to Shot 2): @Lam keeps talking quickly, pushing his glasses up his nose.
- 6–7s (Shot 2): @Lam goes on, chin raised.
- 7–8s (Shot 2): @Lam finishes and closes his mouth, breathing hard.
- 8–9s (Shot 2): @Huy takes his hands out of his pockets and speaks slowly and quietly.
- 9–10s (Shot 2): @Huy keeps talking softly as he steps closer around the table.
- 10–11s (CUT to Shot 3): @Huy goes on, his voice almost gentle.
- 11–12s (Shot 3): @Huy keeps speaking, stopping an arm's length away.
- 12–13s (Shot 3): @Huy finishes and closes his mouth.
- 13–14s (Shot 3): @Lam swallows, his eyes flicking toward the door, mouth closed.
- 14–15s (Shot 3): The two men stand close in the flickering cyan light. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Huy (man of 45, smooth confident baritone, polished and cold, speaking at a natural, even conversational pace, cold and measured): "Đó là cái giá rất nhỏ cho một công nghệ lớn. Anh đừng làm chuyện ngu ngốc."
- Turn 2, 5.3–8.9s, spoken on camera by @Lam (man of 58, thin tired tenor, earnest and shaky, speaking quickly in short lively phrases, every word still clear, defiant): "Tôi sẽ công bố hết. Toàn bộ dữ liệu, toàn bộ danh sách. Ngay sáng mai."
- Turn 3, 9.4–13.2s, spoken on camera by @Huy (man of 45, smooth confident baritone, polished and cold, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, stepping closer): "Anh Lâm. Anh đã nghĩ thật kỹ chưa? Anh còn vợ con đấy."
- Pacing: @Huy speaks at an even everyday pace, then @Lam answers quickly, then @Huy answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the low glitchy drone, slow footsteps on a dusty floor, the curtain flapping, a distant train horn distorted. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 3 (`canh-10/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
Memory flashback graded cold cyan-blue with faint flickering glitch: a dim abandoned apartment in an old collective housing block at night, a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, dust floating in the light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Lam = Lâm, 58, NeuroRent's chief engineer; thin and slightly hunched, balding with grey hair at the sides, black-rimmed glasses, a kind tired face; rumpled white shirt with rolled sleeves, grey trousers, brown leather shoes.
- @Huy = Trịnh Huy, 45, the polished CEO of NeuroRent; tall and trim, a smooth pale face, slicked-back black hair greying at the temples, a cold confident smile; tailored navy suit, white open-collar shirt, a slim silver watch.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium shot of the engineer heading for the door, handheld.
- Shot 2, 5–10s: 85mm close-up of the CEO shouting as he blocks the doorway, handheld.
- Shot 3, 10–13s: 35mm wide shot of the engineer stumbling backward and falling out of view behind the heavy table, locked off.
- Shot 4, 13–15s: 100mm extreme close-up of black-rimmed glasses sliding to a stop on the dusty floor, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Lam heads for the door and is already speaking fast, the folder under his arm.
- 1–2s (Shot 1): @Lam keeps talking quickly, trying to step around @Huy.
- 2–3s (Shot 1): @Lam goes on, his voice shaking.
- 3–4s (Shot 1): @Lam keeps speaking as @Huy sidesteps into the doorway.
- 4–5s (Shot 1): @Lam finishes and closes his mouth, stopped.
- 5–6s (CUT to Shot 2): @Huy shouts, planting himself in the doorway with his arms spread.
- 6–7s (Shot 2): @Huy keeps shouting, his polished face twisting.
- 7–8s (Shot 2): @Huy goes on, shoving @Lam's shoulder hard with one hand.
- 8–9s (Shot 2): @Huy keeps shouting as @Lam staggers back.
- 9–10s (Shot 2): @Huy finishes and closes his mouth, breathing hard.
- 10–11s (CUT to Shot 3): @Lam stumbles backward toward the heavy table and cries out fast.
- 11–12s (Shot 3): @Lam keeps talking as his heel catches the table leg.
- 12–13s (Shot 3): @Lam finishes, closes his mouth and falls backward out of view behind the heavy table with a dull thud.
- 13–14s (CUT to Shot 4): @Lam's black-rimmed glasses skitter across the dusty floor.
- 14–15s (Shot 4): The glasses spin to a stop under the table and lie still in the flickering cyan light. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Lam (man of 58, thin tired tenor, earnest and shaky, speaking quickly in short lively phrases, every word still clear, frightened but determined): "Tránh ra! Tôi nghĩ kỹ rồi. Tôi sẽ đi thẳng đến công an, anh không cản được tôi đâu!"
- Turn 2, 5.1–9.3s, spoken on camera by @Huy (man of 45, smooth confident baritone, polished and cold, speaking at a natural, even conversational pace, shouting, blocking the door): "Đứng lại! Anh Lâm, anh đứng lại cho tôi! Anh không được ra khỏi cửa này!"
- Turn 3, 9.8–12.3s, spoken on camera by @Lam (man of 58, thin tired tenor, earnest and shaky, speaking quickly in short lively phrases, every word still clear, stumbling backward): "Buông tôi ra! Anh định làm cái gì thế hả anh..."
- Pacing: @Lam speaks quickly, then @Huy answers at an even everyday pace, then @Lam answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: hurried footsteps, a body bumping a door frame, a heavy table scraping, glasses clattering across a dusty floor, the glitch drone cutting to silence. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 4 (`canh-10/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; it intercuts the two places or times named in the shot list, each shot keeping its own place and light, with sound continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
Memory flashback graded cold cyan-blue with faint flickering glitch: a dim abandoned apartment in an old collective housing block at night, a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, dust floating in the light. Intercut with the present: A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, deep at night, lit only by orange street light through the barred window and a small yellow bedside lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Huy = Trịnh Huy, 45, the polished CEO of NeuroRent; tall and trim, a smooth pale face, slicked-back black hair greying at the temples, a cold confident smile; tailored navy suit, white open-collar shirt, a slim silver watch.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up memory shot in cold cyan light of the CEO turning to look straight into the lens, slow push-in.
- Shot 2, 5–10s: 50mm medium shot in the present night room of the young man jolting awake on the floor against the wall with a marker in his hand, handheld.
- Shot 3, 10–15s: 100mm extreme close-up of a small slanted letter signed under the scrawl on the white wall, too blurry to read, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Each shot keeps the lighting of its own place and time; faces, wardrobe and props stay consistent; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the cyan memory, @Huy turns from the table to face the lens and is already speaking slowly, breathing hard.
- 1–2s (Shot 1): @Huy keeps talking in a terrifyingly calm voice, smoothing his jacket.
- 2–3s (Shot 1): @Huy goes on, stepping toward the lens.
- 3–4s (Shot 1): @Huy keeps speaking, his face filling the frame.
- 4–5s (Shot 1): @Huy finishes, closes his mouth and the memory shatters into white static.
- 5–6s (CUT to Shot 2): In the dark room @Khai jolts awake on the floor against the wall, an open marker in his hand, and gasps out fast words.
- 6–7s (Shot 2): @Khai keeps talking quickly, scrambling backward on the floor.
- 7–8s (Shot 2): @Khai goes on, staring at his own hands.
- 8–9s (Shot 2): @Khai keeps speaking, looking wildly around the room.
- 9–10s (Shot 2): @Khai finishes and closes his mouth, panting.
- 10–11s (CUT to Shot 3): @Khai turns to the white wall and reads slowly, his voice chilled.
- 11–12s (Shot 3): @Khai keeps speaking softly, lifting the lamp toward the plaster.
- 12–13s (Shot 3): @Khai goes on, his finger hovering under a small slanted mark beneath the old scrawl.
- 13–14s (Shot 3): @Khai finishes and closes his mouth.
- 14–15s (Shot 3): The small slanted signature, too blurry to read, glistens with fresh ink under the lamp. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.0s, spoken on camera by @Huy (man of 45, smooth confident baritone, polished and cold, speaking slowly and softly, unhurried, with a short natural pause between phrases, breathing hard, terrifyingly calm): "Vy. Nghe anh. Em không thấy gì hết. Em hiểu không? Em chưa từng ở đây."
- Turn 2, 5.5–8.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, waking with a gasp): "Ông ấy ngã rồi! Ông ấy... Không, không phải mình! Mình đang ở đâu thế này?"
- Turn 3, 9.4–13.3s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, reading the wall, chilled): "Đừng ngủ... Và ngay dưới này còn có một chữ ký nhỏ. Chữ V."
- Pacing: @Huy speaks slowly and calmly, then @Khai answers quickly, then @Khai continues slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heavy breathing in the memory, a glitch burst, a sharp gasp, the electric fan in the present, the squeak of a marker cap. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 1 (`canh-11/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm wide shot of the young man in his orange jacket at the foot of a dark stairwell looking up, locked off.
- Shot 2, 5–10s: 50mm medium shot following the young man climbing the broken stairs, handheld.
- Shot 3, 10–15s: 85mm close-up of the young man pushing open a half-closed door in a dark corridor, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai stands at the foot of the dark stairwell and is already speaking, muttering as he looks up.
- 1–2s (Shot 1): @Khai keeps talking softly, his eyes running over the damp stained walls.
- 2–3s (Shot 1): @Khai goes on, stepping over a fallen chunk of plaster.
- 3–4s (Shot 1): @Khai keeps speaking, putting one foot on the first step.
- 4–5s (Shot 1): @Khai finishes and closes his mouth, starting to climb.
- 5–6s (CUT to Shot 2): @Khai climbs fast and starts speaking breathlessly, one hand on the wall.
- 6–7s (Shot 2): @Khai keeps talking quickly as he passes a gap where the railing is broken away.
- 7–8s (Shot 2): @Khai goes on, pressing his back to the wall and edging past the gap.
- 8–9s (Shot 2): @Khai keeps speaking fast, not looking down.
- 9–10s (Shot 2): @Khai finishes and closes his mouth, panting at the top landing.
- 10–11s (CUT to Shot 3): @Khai stops before a half-closed door in the dark corridor and speaks slowly in a hush.
- 11–12s (Shot 3): @Khai keeps talking quietly, reaching out a hand.
- 12–13s (Shot 3): @Khai goes on, his fingertips touching the peeling door.
- 13–14s (Shot 3): @Khai finishes and closes his mouth as the door creaks inward.
- 14–15s (Shot 3): @Khai stands in the doorway, grey daylight from inside falling across his face. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, spoken on camera by @Khai alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–4.7s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, muttering to himself, looking up): "Khu C, Kim Liên. Đúng rồi, chính là khu này. Người ta bảo sắp phá dỡ rồi."
- Part 2, 5.2–8.8s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, breathless, climbing): "Tầng bảy. Cầu thang gãy hết cả lan can rồi. Cẩn thận, cẩn thận, đừng nhìn xuống."
- Part 3, 9.3–13.8s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, hushed, uneasy): "Phòng bảy linh bốn đây rồi... Cửa chỉ khép hờ thôi. Có ai ở trong không?"
- Pacing: @Khai speaks at an even everyday pace, then @Khai continues quickly, then @Khai continues slowly and calmly; the change of speed is clearly audible.
- Throughout, @Khai's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: footsteps echoing on concrete stairs, water dripping, pigeons flapping in an empty corridor, a door creaking on rusty hinges. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 2 (`canh-11/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 28mm wide shot of the empty apartment with the torn yellow curtain and crooked lotus painting as the young man steps in, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the young man crouching by the sharp corner of the heavy table, handheld.
- Shot 3, 10–15s: 40mm medium shot of the young man standing slowly in the middle of the room, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai steps into the empty apartment and is already speaking in an awestruck whisper.
- 1–2s (Shot 1): @Khai keeps whispering, staring at the torn yellow curtain moving in the draught.
- 2–3s (Shot 1): @Khai goes on, turning to the crooked lotus painting on the wall.
- 3–4s (Shot 1): @Khai keeps speaking softly, reaching out but not touching the frame.
- 4–5s (Shot 1): @Khai finishes and closes his mouth.
- 5–6s (CUT to Shot 2): @Khai crouches by the heavy table and starts speaking fast, pointing at its sharp corner.
- 6–7s (Shot 2): @Khai keeps talking quickly, his finger tracing the edge of the table in the air.
- 7–8s (Shot 2): @Khai goes on, looking down at a dark dried stain on the floorboards.
- 8–9s (Shot 2): @Khai keeps speaking fast, his hand trembling.
- 9–10s (Shot 2): @Khai finishes and closes his mouth, pulling his hand back.
- 10–11s (CUT to Shot 3): @Khai stands up slowly and speaks at an even pace, his face drained.
- 11–12s (Shot 3): @Khai keeps talking flatly, looking around the room.
- 12–13s (Shot 3): @Khai goes on, his eyes coming back to the table.
- 13–14s (Shot 3): @Khai finishes and closes his mouth.
- 14–15s (Shot 3): @Khai stands motionless in the middle of the room while the torn curtain flaps behind him. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, spoken on camera by @Khai alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–5.2s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, awestruck whisper): "Rèm vàng rách một góc... Bức tranh hoa sen treo lệch... Y hệt như trong giấc mơ."
- Part 2, 5.7–9.5s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, rising horror): "Cái bàn này. Chính cái góc bàn này. Ông ấy ngã vào đây. Vết này... vẫn còn đây."
- Part 3, 10.0–13.3s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, flat, the truth landing): "Vậy là có thật. Không phải mơ. Có người đã chết ở đây."
- Pacing: @Khai speaks slowly and calmly, then @Khai continues quickly, then @Khai continues at an even everyday pace; the change of speed is clearly audible.
- Throughout, @Khai's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind moving the torn curtain, a fly buzzing, floorboards creaking, his breath catching. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 3 (`canh-11/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the woman in a grey hoodie in the doorway raising a rusty metal pipe, handheld.
- Shot 2, 5–10s: 85mm close-up of the young man turning slowly with both hands raised, locked off.
- Shot 3, 10–15s: 40mm medium two-shot across the room, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy stands in the doorway in her grey hoodie, a rusty metal pipe raised, and is already speaking fast in a low, hard voice.
- 1–2s (Shot 1): @Vy keeps talking quickly, stepping into the room.
- 2–3s (Shot 1): @Vy goes on, the pipe steady in both hands.
- 3–4s (Shot 1): @Vy finishes and closes her mouth, eyes locked on him.
- 4–5s (Shot 1): @Khai turns slowly with both hands raised and answers fast.
- 5–6s (CUT to Shot 2): @Khai keeps talking quickly, shaking his head.
- 6–7s (Shot 2): @Khai goes on, pointing back toward the stairs with one raised hand.
- 7–8s (Shot 2): @Khai keeps speaking fast, his voice cracking.
- 8–9s (Shot 2): @Khai finishes and closes his mouth, hands still up.
- 9–10s (Shot 2): @Vy narrows her eyes and answers slowly, lowering her voice.
- 10–11s (CUT to Shot 3): @Vy keeps speaking softly, the pipe dipping a little.
- 11–12s (Shot 3): @Vy goes on, studying his face.
- 12–13s (Shot 3): @Vy finishes and closes her mouth.
- 13–14s (Shot 3): @Khai stares at her, mouth closed, and gives one small nod.
- 14–15s (Shot 3): @Vy's grip on the pipe loosens slightly as they hold each other's gaze. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.8s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking quickly in short lively phrases, every word still clear, low and hard, holding a rusty pipe): "Đứng im. Quay lại từ từ. Ai cho anh lên đây? Ai gửi anh đến đây?"
- Turn 2, 4.3–8.3s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, hands up, terrified): "Không ai cả! Tôi thề! Có người viết địa chỉ này lên tường nhà tôi lúc ba giờ sáng!"
- Turn 3, 8.8–12.7s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, eyes narrowing, lowering her voice): "Viết lên tường... bằng nét chữ nghiêng nghiêng, ký một chữ V, đúng không?"
- Pacing: @Vy speaks quickly, then @Khai answers quickly, then @Vy answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a floorboard creaking behind him, a rusty pipe scraping the door frame, his sharp intake of breath, wind in the curtain. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 4 (`canh-11/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the woman, pipe still raised, locked off.
- Shot 2, 5–9s: 50mm medium shot of the young man lowering his hands, handheld.
- Shot 3, 9–15s: 35mm wide shot of the empty room as the pipe drops to the floor between them, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy is already speaking urgently, the pipe still raised, her eyes searching his face.
- 1–2s (Shot 1): @Vy keeps talking, taking one step closer.
- 2–3s (Shot 1): @Vy goes on, her jaw tight.
- 3–4s (Shot 1): @Vy keeps speaking, waiting for his answer.
- 4–5s (Shot 1): @Vy finishes and closes her mouth.
- 5–6s (CUT to Shot 2): @Khai lowers his hands and blurts out his answer fast.
- 6–7s (Shot 2): @Khai keeps talking quickly, tapping his temple.
- 7–8s (Shot 2): @Khai goes on, eyes wide.
- 8–9s (Shot 2): @Khai finishes and closes his mouth.
- 9–10s (CUT to Shot 3): @Vy answers slowly, her voice breaking, as the pipe slides from her fingers.
- 10–11s (Shot 3): @Vy keeps speaking softly as the pipe hits the floor with a clang.
- 11–12s (Shot 3): @Vy goes on, pressing one hand over her mouth between words.
- 12–13s (Shot 3): @Vy keeps speaking, her eyes shining.
- 13–14s (Shot 3): @Vy finishes and closes her mouth.
- 14–15s (Shot 3): @Khai and @Vy stand facing each other over the fallen pipe, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, urgent, testing him): "Anh có tự nhiên thuộc một bài hát ru tiếng Nhật không? Trả lời thật đi."
- Turn 2, 4.9–8.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, stunned, blurting it out): "Có! Sao cô biết? Mấy hôm nay tôi ngân nó suốt, mà tôi không hiểu một chữ nào."
- Turn 3, 9.2–13.7s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, voice breaking, lowering the pipe): "Đó là bài mẹ tôi hát ru tôi. Ngoài tôi ra, không ai biết bài đó."
- Pacing: @Vy speaks at an even everyday pace, then @Khai answers quickly, then @Vy answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a rusty pipe dropping with a loud metallic clang on the floor, the clang echoing down the corridor, wind in the curtain. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 1 (`canh-12/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot of the two sitting on the dusty floor by the table, the woman opening a cracked laptop, locked off.
- Shot 2, 5–9s: 85mm close-up of the young man listening, handheld.
- Shot 3, 9–15s: 50mm medium shot of the woman closing the laptop halfway, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy sits cross-legged on the dusty floor opening a cracked laptop and is already speaking in a precise voice.
- 1–2s (Shot 1): @Vy keeps talking, the cracked screen lighting her face.
- 2–3s (Shot 1): @Vy goes on, glancing at @Khai over the screen.
- 3–4s (Shot 1): @Vy keeps speaking, raising one eyebrow.
- 4–5s (Shot 1): @Vy finishes and closes her mouth, waiting.
- 5–6s (CUT to Shot 2): @Khai answers fast, nodding eagerly.
- 6–7s (Shot 2): @Khai keeps talking, gesturing at the phone in his pocket.
- 7–8s (Shot 2): @Khai finishes and closes his mouth.
- 8–9s (Shot 2): @Vy answers slowly and flatly, shaking her head.
- 9–10s (CUT to Shot 3): @Vy keeps speaking, tapping her own temple.
- 10–11s (Shot 3): @Vy goes on, pushing the laptop lid half closed.
- 11–12s (Shot 3): @Vy finishes and closes her mouth.
- 12–13s (Shot 3): @Khai frowns, mouth closed, leaning closer.
- 13–14s (Shot 3): @Vy holds his gaze, silent.
- 14–15s (Shot 3): Grey light falls between them as dust drifts through the air. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, precise, like a lecture): "NeuroRent nói với các anh là não người còn dư dung lượng, họ thuê để chạy máy tính. Đúng không?"
- Turn 2, 5.9–9.3s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, eager to understand): "Đúng thế. Quảng cáo nói thế, cái trợ lý ảo trên điện thoại cũng nói thế."
- Turn 3, 9.8–12.9s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, flat, final): "Sai hết. Não người không phải là ổ cứng đâu anh."
- Pacing: @Vy speaks at an even everyday pace, then @Khai answers quickly, then @Vy answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a laptop fan whirring, keys tapping, wind through a broken pane, pigeons on the window ledge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 2 (`canh-12/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 85mm close-up of the woman explaining, locked off.
- Shot 2, 6–10s: 40mm medium shot of the young man leaning forward on the floor, handheld.
- Shot 3, 10–15s: 100mm extreme close-up of the woman's eyes as she answers, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy is already speaking patiently, holding up one finger.
- 1–2s (Shot 1): @Vy keeps talking, drawing a small circle in the dust on the floor.
- 2–3s (Shot 1): @Vy goes on, rubbing the circle out with her palm.
- 3–4s (Shot 1): @Vy keeps speaking, then draws an arrow pointing away.
- 4–5s (Shot 1): @Vy goes on, tapping the end of the arrow.
- 5–6s (Shot 1): @Vy finishes and closes her mouth.
- 6–7s (CUT to Shot 2): @Khai leans forward and asks fast, alarmed.
- 7–8s (Shot 2): @Khai keeps talking quickly, staring at the arrow in the dust.
- 8–9s (Shot 2): @Khai finishes and closes his mouth.
- 9–10s (Shot 2): @Vy answers slowly in a quiet, grim voice.
- 10–11s (CUT to Shot 3): @Vy keeps speaking, her eyes not leaving his.
- 11–12s (Shot 3): @Vy goes on, her voice dropping lower.
- 12–13s (Shot 3): @Vy finishes and closes her mouth.
- 13–14s (Shot 3): In extreme close-up @Vy's tired eyes stay steady and unblinking.
- 14–15s (Shot 3): @Vy's gaze drops to the arrow in the dust as the silence stretches. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.2s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, explaining patiently): "Thứ duy nhất não người lưu giữ được là ký ức. Và ký ức thì không xóa được, chỉ chuyển đi được thôi."
- Turn 2, 6.7–8.8s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, alarmed): "Chuyển đi đâu? Ý cô là chuyển vào đâu cơ?"
- Turn 3, 9.3–13.0s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and grim): "Vào đầu những người nghèo. Ban đêm. Trong lúc họ đang ngủ say."
- Pacing: @Vy speaks at an even everyday pace, then @Khai answers quickly, then @Vy answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the laptop fan, wind through the broken pane, a distant construction hammer, a pigeon cooing. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 3 (`canh-12/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young man as the realisation hits, locked off.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the young man onto the woman turning the laptop toward him, handheld.
- Shot 3, 10–15s: 40mm medium two-shot of both staring at the glowing cracked screen, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking slowly, his face going pale.
- 1–2s (Shot 1): @Khai keeps talking softly, pressing his fingers to the back of his neck.
- 2–3s (Shot 1): @Khai goes on, staring at nothing.
- 3–4s (Shot 1): @Khai finishes and closes his mouth.
- 4–5s (Shot 1): @Vy answers at an even pace, turning the laptop toward him.
- 5–6s (CUT to Shot 2): @Vy keeps talking as rows of blurred account lines glow on the cracked screen.
- 6–7s (Shot 2): @Vy goes on, scrolling with one finger.
- 7–8s (Shot 2): @Vy keeps speaking, tapping a line.
- 8–9s (Shot 2): @Vy finishes and closes her mouth.
- 9–10s (Shot 2): @Khai answers fast, sickened, leaning back from the screen.
- 10–11s (CUT to Shot 3): @Khai keeps talking quickly, shaking his head.
- 11–12s (Shot 3): @Khai finishes and closes his mouth, swallowing hard.
- 12–13s (Shot 3): @Vy watches him silently, mouth closed.
- 13–14s (Shot 3): @Khai stares at the scrolling blurred lines, his hand still on his neck.
- 14–15s (Shot 3): The cracked screen's glow flickers over both their faces. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.5s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, horrified realisation): "Vậy những gì tôi thấy... là ký ức của người khác?"
- Turn 2, 4.0–9.5s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, turning the laptop toward him): "Người giàu muốn quên một vụ tai nạn, một vụ hối lộ, một tội ác. Họ trả tiền để gửi nó đi."
- Turn 3, 10.0–12.8s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, sickened): "Gửi vào đầu những người như tôi, như bà Tư nhà tôi à?"
- Pacing: @Khai speaks slowly and calmly, then @Vy answers at an even everyday pace, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the laptop fan, a soft click of a trackpad, wind through the broken pane, his breath catching. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 4 (`canh-12/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the woman speaking gently, locked off.
- Shot 2, 5–10s: 40mm medium shot of the young man scrambling to his knees, handheld.
- Shot 3, 10–15s: 50mm over-the-shoulder shot from behind the young man onto the woman, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy is already speaking slowly and gently, her eyes lowered.
- 1–2s (Shot 1): @Vy keeps talking, pressing her palm flat on the laptop lid.
- 2–3s (Shot 1): @Vy goes on, rubbing her thumb in a slow circle as if wearing something away.
- 3–4s (Shot 1): @Vy keeps speaking softly.
- 4–5s (Shot 1): @Vy finishes and closes her mouth.
- 5–6s (CUT to Shot 2): @Khai rises to his knees and answers fast, upset.
- 6–7s (Shot 2): @Khai keeps talking quickly, his hands in fists.
- 7–8s (Shot 2): @Khai goes on, pointing out of the window toward the city.
- 8–9s (Shot 2): @Khai finishes and closes his mouth, breathing hard.
- 9–10s (Shot 2): @Vy answers at an even pace, quiet and sorry.
- 10–11s (CUT to Shot 3): @Vy keeps talking, looking away.
- 11–12s (Shot 3): @Vy goes on, hugging her knees.
- 12–13s (Shot 3): @Vy finishes and closes her mouth.
- 13–14s (Shot 3): @Khai sinks back down onto the floor, silent.
- 14–15s (Shot 3): The two sit without speaking as the torn curtain moves in the draught. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, gentle but blunt): "Bà cụ nào dán chip lâu năm, ký ức của chính bà sẽ bị đè lên, mòn dần đi."
- Turn 2, 6.2–9.4s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, connecting the dots, upset): "Thảo nào bà Tư cứ quên trước quên sau. Bà ấy dán mười năm rồi!"
- Turn 3, 9.9–13.4s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, quiet, sorry): "Mười năm. Chắc bà ấy chẳng còn nhớ nhiều thứ của mình nữa đâu."
- Pacing: @Vy speaks slowly and calmly, then @Khai answers quickly, then @Vy answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the laptop fan, wind through the broken pane, distant children's voices from the street below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 1 (`canh-13/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the young man in the middle of the room, locked off.
- Shot 2, 5–10s: 85mm close-up of the woman by the corner of the heavy table, slow push-in.
- Shot 3, 10–15s: 40mm medium two-shot across the table, handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai stands in the middle of the room and is already speaking quietly.
- 1–2s (Shot 1): @Khai keeps talking, tapping the bridge of his nose as if adjusting glasses.
- 2–3s (Shot 1): @Khai goes on, glancing at the heavy table.
- 3–4s (Shot 1): @Khai finishes and closes his mouth.
- 4–5s (Shot 1): @Vy, standing by the table corner, answers slowly with grief in her voice.
- 5–6s (CUT to Shot 2): @Vy keeps talking softly, resting her fingertips on the table edge.
- 6–7s (Shot 2): @Vy goes on, her eyes shining.
- 7–8s (Shot 2): @Vy keeps speaking, swallowing hard.
- 8–9s (Shot 2): @Vy finishes and closes her mouth.
- 9–10s (Shot 2): @Khai answers fast, piecing it together.
- 10–11s (CUT to Shot 3): @Khai keeps talking quickly, gesturing in the direction of the city.
- 11–12s (Shot 3): @Khai goes on, eyes wide.
- 12–13s (Shot 3): @Khai finishes and closes his mouth.
- 13–14s (Shot 3): @Vy gives a single slow nod, mouth closed.
- 14–15s (Shot 3): @Khai lets out a long breath, staring at the sharp table corner. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, quiet, hesitant): "Còn ông già đeo kính mà tôi nhìn thấy trong mơ... Ông ấy là ai?"
- Turn 2, 4.7–8.6s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, grief in her voice): "Thầy Lâm. Kỹ sư trưởng của NeuroRent. Người đã dạy cho tôi mọi thứ."
- Turn 3, 9.1–12.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, piecing it together): "Và người đàn ông mặc vest đó... là Trịnh Huy, ông chủ trên tấm biển quảng cáo?"
- Pacing: @Khai speaks at an even everyday pace, then @Vy answers slowly and calmly, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: noon traffic far below, wind in the curtain, a fly buzzing at the window, floorboards creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 2 (`canh-13/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 8s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 85mm close-up of the woman speaking, locked off.
- Shot 2, 6–8s: 100mm extreme close-up of the young man's worn sneakers on the dusty floorboards, locked off.
- Shot 3, 8–15s: 40mm medium two-shot as the woman walks slowly around the table toward him, handheld.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy is already speaking in a steady voice, forcing herself to go on.
- 1–2s (Shot 1): @Vy keeps talking, pointing at the sharp table corner.
- 2–3s (Shot 1): @Vy goes on, her finger trembling slightly.
- 3–4s (Shot 1): @Vy keeps speaking, lifting her eyes to @Khai.
- 4–5s (Shot 1): @Vy goes on, pointing at the floor under his feet.
- 5–6s (Shot 1): @Vy finishes and closes her mouth.
- 6–7s (CUT to Shot 2): @Khai looks down at his worn sneakers on the dusty boards and speaks slowly.
- 7–8s (Shot 2): @Khai finishes and closes his mouth, frozen.
- 8–9s (CUT to Shot 3): @Vy starts walking around the table and talks fast and bitterly.
- 9–10s (Shot 3): @Vy keeps talking quickly, touching the back of her own neck.
- 10–11s (Shot 3): @Vy goes on, her voice hardening.
- 11–12s (Shot 3): @Vy keeps speaking fast, stopping in front of him.
- 12–13s (Shot 3): @Vy finishes and closes her mouth, jaw clenched.
- 13–14s (Shot 3): @Khai lifts his eyes to hers, mouth closed.
- 14–15s (Shot 3): The two stand close together beside the table, silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, steady, forcing herself): "Đúng. Thầy định công bố hết. Huy đẩy thầy ngã vào góc bàn đó. Tôi đứng ngay chỗ anh đang đứng."
- Turn 2, 6.2–7.1s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, looking down at his feet): "Ngay chỗ này..."
- Turn 3, 7.6–12.2s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking quickly in short lively phrases, every word still clear, bitter, the words tumbling out): "Đêm đó Huy đưa tôi vào máy, gỡ ký ức đó ra khỏi đầu tôi, để tôi không làm nhân chứng được."
- Pacing: @Vy speaks at an even everyday pace, then @Khai answers slowly and calmly, then @Vy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind in the curtain, a floorboard creaking under his shoe, distant traffic, a fly buzzing. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 3 (`canh-13/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the young man frowning, handheld.
- Shot 2, 3–9s: 85mm close-up of the woman with a faint proud tilt of her head, locked off.
- Shot 3, 9–15s: 100mm extreme close-up of the woman's finger touching the young man's temple, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking fast, frowning in confusion.
- 1–2s (Shot 1): @Khai finishes and closes his mouth.
- 2–3s (Shot 1): @Khai waits, his head tilted.
- 3–4s (CUT to Shot 2): @Vy answers at an even pace, a hint of pride in her face.
- 4–5s (Shot 2): @Vy keeps talking, tapping her own forehead.
- 5–6s (Shot 2): @Vy goes on, glancing at the laptop on the table.
- 6–7s (Shot 2): @Vy keeps speaking, lifting her chin.
- 7–8s (Shot 2): @Vy goes on, her eyes on him.
- 8–9s (Shot 2): @Vy pauses and closes her mouth for a breath.
- 9–10s (CUT to Shot 3): @Vy continues slowly, stepping closer to him.
- 10–11s (Shot 3): @Vy keeps speaking softly, raising one finger.
- 11–12s (Shot 3): @Vy goes on as her fingertip touches his temple.
- 12–13s (Shot 3): @Vy keeps speaking, her finger resting there.
- 13–14s (Shot 3): @Vy finishes and closes her mouth.
- 14–15s (Shot 3): @Khai stares at her, frozen, her fingertip still against his temple. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–1.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, confused): "Nhưng cô vẫn nhớ hết đấy thôi?"
- Turn 2, 2.4–7.9s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, a hint of pride): "Tôi biết là có chuyện đó, nhưng hình ảnh thì mất hết rồi. Mà tôi là người viết ra hệ thống này."
- Turn 3, 8.4–13.4s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, looking straight at him): "Nên tôi đã đổi địa chỉ đích. Ký ức đó không vào kho xóa... mà vào đầu anh."
- Pacing: @Khai speaks quickly, then @Vy answers at an even everyday pace, then @Vy continues slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind in the curtain, a distant scooter horn, the laptop fan starting up on the table. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 4 (`canh-13/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium shot of the young man stepping back furious, handheld.
- Shot 2, 5–11s: 85mm close-up of the woman answering without flinching, locked off.
- Shot 3, 11–15s: 50mm medium shot of the young man sinking down onto the edge of the table, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai steps back from her and is already speaking fast, furious.
- 1–2s (Shot 1): @Khai keeps talking quickly, jabbing a finger at his own head.
- 2–3s (Shot 1): @Khai goes on, his voice rising.
- 3–4s (Shot 1): @Khai finishes and closes his mouth, chest heaving.
- 4–5s (Shot 1): @Vy answers at an even pace, flat and unflinching.
- 5–6s (CUT to Shot 2): @Vy keeps talking, not moving an inch.
- 6–7s (Shot 2): @Vy goes on, pointing at the back of his neck.
- 7–8s (Shot 2): @Vy keeps speaking, her voice level.
- 8–9s (Shot 2): @Vy goes on, folding her arms.
- 9–10s (Shot 2): @Vy keeps speaking calmly.
- 10–11s (Shot 2): @Vy finishes and closes her mouth.
- 11–12s (CUT to Shot 3): @Khai's shoulders drop and he speaks slowly, deflating.
- 12–13s (Shot 3): @Khai finishes and closes his mouth.
- 13–14s (Shot 3): @Khai sinks down onto the edge of the heavy table, rubbing his face with both hands.
- 14–15s (Shot 3): @Vy watches him in silence, arms still folded. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, furious, stepping back): "Cô lấy đầu tôi làm két sắt à? Cô có biết tôi còn một đứa em gái không?"
- Turn 2, 4.7–10.7s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, flat, unflinching): "Đầu anh đã là két sắt của họ từ cái đêm anh bấm đồng ý. Tôi chỉ bỏ vào đó một thứ họ sợ."
- Turn 3, 11.2–12.6s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, deflating): "Tôi... tôi không cãi được."
- Pacing: @Khai speaks quickly, then @Vy answers at an even everyday pace, then @Khai answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: his sneakers scuffing back on the boards, wind in the curtain, a pigeon taking off from the ledge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 1 (`canh-14/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Nova = Nova, the NeuroRent app's holographic assistant; a softly glowing translucent violet hologram of a young woman about a hand's height tall, standing on a beam of light above a phone screen, a smooth calm face with a gentle fixed smile, sleek hair in a high knot, faint horizontal scan lines through her body; a simple fitted violet light-dress.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the violet hologram rising from the phone on the dusty table, a thin red edge to her light, locked off.
- Shot 2, 5–9s: 50mm medium shot of the young man jerking upright on the table edge, handheld.
- Shot 3, 9–15s: 100mm extreme close-up of the hologram's smiling face, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): On the dusty table @Nova rises from @Khai's phone as a hand-tall violet hologram with a thin red edge and is already speaking sweetly.
- 1–2s (Shot 1): @Nova keeps talking, her smile fixed.
- 2–3s (Shot 1): @Nova goes on as a small red warning ring pulses around her feet.
- 3–4s (Shot 1): @Nova keeps speaking, tilting her head.
- 4–5s (Shot 1): @Nova finishes and closes her mouth.
- 5–6s (CUT to Shot 2): @Khai jerks upright on the table edge and answers fast.
- 6–7s (Shot 2): @Khai keeps talking quickly, leaning over the hologram.
- 7–8s (Shot 2): @Khai finishes and closes his mouth.
- 8–9s (Shot 2): @Nova answers slowly, her voice calm and sweet.
- 9–10s (CUT to Shot 3): @Nova keeps talking, lifting one finger like a clock hand.
- 10–11s (Shot 3): @Nova goes on, the red ring around her feet glowing brighter.
- 11–12s (Shot 3): @Nova keeps speaking, smiling wider.
- 12–13s (Shot 3): @Nova finishes and closes her mouth.
- 13–14s (Shot 3): In extreme close-up @Nova's smiling face flickers once with a red glitch.
- 14–15s (Shot 3): @Nova's smile holds perfectly still as the red ring keeps pulsing. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking at a natural, even conversational pace, sweet, with an odd edge): "Anh Khải ơi, hệ thống phát hiện dữ liệu không hợp lệ trong tài khoản của anh."
- Turn 2, 5.4–7.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, alarmed): "Dữ liệu không hợp lệ? Cô nói rõ ra xem nào!"
- Turn 3, 8.2–14.1s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking slowly and softly, unhurried, with a short natural pause between phrases, smiling, sinister in its calm): "Dung lượng của anh sẽ được thu hồi lúc mười hai giờ đêm nay. Anh nhớ ngủ đúng giờ nhé."
- Pacing: @Nova speaks at an even everyday pace, then @Khai answers quickly, then @Nova answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a low warning chime, the hologram humming with a faint crackle, wind in the curtain, his chair-less shuffle on the table edge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 2 (`canh-14/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Nova = Nova, the NeuroRent app's holographic assistant; a softly glowing translucent violet hologram of a young woman about a hand's height tall, standing on a beam of light above a phone screen, a smooth calm face with a gentle fixed smile, sleek hair in a high knot, faint horizontal scan lines through her body; a simple fitted violet light-dress.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the hologram onto the young man, locked off.
- Shot 2, 5–10s: 85mm close-up of the hologram answering, slow push-in.
- Shot 3, 10–15s: 40mm medium shot of the young man standing up from the table edge, handheld.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking defiantly, glaring down at the hologram.
- 1–2s (Shot 1): @Khai keeps talking, folding his arms.
- 2–3s (Shot 1): @Khai goes on, chin raised.
- 3–4s (Shot 1): @Khai finishes and closes his mouth.
- 4–5s (Shot 1): @Nova answers in a sweet voice that has gone a shade colder.
- 5–6s (CUT to Shot 2): @Nova keeps talking, a small padlock icon spinning beside her.
- 6–7s (Shot 2): @Nova goes on, her hands folded.
- 7–8s (Shot 2): @Nova keeps speaking, unblinking.
- 8–9s (Shot 2): @Nova finishes and closes her mouth.
- 9–10s (Shot 2): @Khai stands up from the table edge and answers fast, panicking.
- 10–11s (CUT to Shot 3): @Khai keeps talking quickly, pressing both hands to his head.
- 11–12s (Shot 3): @Khai goes on, pacing a step away and back.
- 12–13s (Shot 3): @Khai finishes and closes his mouth, breathing hard.
- 13–14s (Shot 3): @Nova smiles silently on the table, mouth closed.
- 14–15s (Shot 3): @Khai stares down at the glowing figure, his hands still on his head. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, defiant): "Nếu tôi không đeo thì sao? Nếu tối nay tôi không ngủ thì sao?"
- Turn 2, 4.4–8.9s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking at a natural, even conversational pace, still sweet, slightly colder): "Tài khoản sẽ bị khóa, và toàn bộ thu nhập sẽ được hoàn trả về công ty."
- Turn 3, 9.4–12.6s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, panicking): "Hoàn trả? Tôi tiêu hết rồi! Tiền học của em tôi, tiền trả nợ nữa!"
- Pacing: @Khai speaks at an even everyday pace, then @Nova answers at an even everyday pace, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the hologram's crackling hum, a low warning tone, his hand slapping the table, wind in the curtain. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 3 (`canh-14/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium shot of the woman crossing the room from the window, handheld.
- Shot 2, 5–9s: 85mm close-up of the young man, locked off.
- Shot 3, 9–15s: 50mm medium two-shot of the two standing close by the table, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy crosses the room from the window and is already speaking fast and urgently.
- 1–2s (Shot 1): @Vy keeps talking quickly, glancing at the phone on the table.
- 2–3s (Shot 1): @Vy goes on, stopping in front of @Khai.
- 3–4s (Shot 1): @Vy finishes and closes her mouth.
- 4–5s (Shot 1): @Khai answers at an even pace, trying to stay calm.
- 5–6s (CUT to Shot 2): @Khai keeps talking, his hands open in front of him.
- 6–7s (Shot 2): @Khai goes on, swallowing.
- 7–8s (Shot 2): @Khai finishes and closes his mouth.
- 8–9s (Shot 2): @Vy answers slowly and carefully, her eyes on his.
- 9–10s (CUT to Shot 3): @Vy keeps speaking, making a wiping gesture with her palm.
- 10–11s (Shot 3): @Vy goes on, touching the back of his neck lightly where the patch glows.
- 11–12s (Shot 3): @Vy keeps speaking softly, her voice trailing off.
- 12–13s (Shot 3): @Vy finishes and closes her mouth.
- 13–14s (Shot 3): @Khai stares at her, mouth closed, understanding dawning.
- 14–15s (Shot 3): @Vy lowers her hand from his neck in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.6s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking quickly in short lively phrases, every word still clear, urgent, crossing the room): "Họ biết rồi. Họ dò ra ký ức của thầy Lâm nằm trong đầu anh."
- Turn 2, 4.1–6.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, trying to stay calm): "Thu hồi là sao? Họ lấy lại cái gì của tôi?"
- Turn 3, 7.4–13.3s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, careful, dreading the answer): "Xóa sạch vùng đó. Ký ức của thầy mất. Và vì nó bám vào trí nhớ của anh bảy ngày rồi..."
- Pacing: @Vy speaks quickly, then @Khai answers at an even everyday pace, then @Vy answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: boots crossing the floorboards, wind in the curtain, the faint hologram crackle fading, distant traffic. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 4 (`canh-14/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
An abandoned old collective housing block in Hanoi, daytime: a dark stairwell with broken railings and damp stained walls, sealed doors along the corridor, and inside one empty apartment a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, grey daylight through dusty glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young man whispering, locked off.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the young man onto the woman, handheld.
- Shot 3, 10–15s: 100mm extreme close-up of his fingers touching the violet patch on the back of his neck, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking slowly in a near whisper.
- 1–2s (Shot 1): @Khai keeps talking, his eyes unfocused.
- 2–3s (Shot 1): @Khai goes on, his voice catching.
- 3–4s (Shot 1): @Khai finishes and closes his mouth.
- 4–5s (Shot 1): @Vy answers honestly and gently.
- 5–6s (CUT to Shot 2): @Vy keeps talking, holding up one finger.
- 6–7s (Shot 2): @Vy goes on, spreading her hands wide.
- 7–8s (Shot 2): @Vy keeps speaking, her face sorry.
- 8–9s (Shot 2): @Vy finishes and closes her mouth.
- 9–10s (Shot 2): @Khai answers fast, reaching behind his neck.
- 10–11s (CUT to Shot 3): @Khai keeps talking quickly as his fingers find the thin violet patch.
- 11–12s (Shot 3): @Khai goes on, digging a nail under its edge.
- 12–13s (Shot 3): @Khai finishes and closes his mouth.
- 13–14s (Shot 3): In extreme close-up his fingertips press against the patch, which clings fast to the skin.
- 14–15s (Shot 3): The violet light under his fingers blinks a slow warning red. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.3s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, barely a whisper): "Thì một phần ký ức của tôi cũng đi theo nó, đúng không cô?"
- Turn 2, 4.8–9.1s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, honest, gentle): "Không ai biết là bao nhiêu. Có thể là một ngày, có thể là cả một năm."
- Turn 3, 9.6–12.8s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, grasping at hope): "Còn nếu tôi gỡ cái này ra, không ngủ, giữ lại ký ức thì sao?"
- Pacing: @Khai speaks slowly and calmly, then @Vy answers at an even everyday pace, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind in the curtain, a church bell far away across the city, the patch giving a tiny electronic tick. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 1 (`canh-15/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The small shared courtyard of the old collective housing block at dusk: potted bonsai and chili plants, a low plastic table with plastic stools, a water tap, warm tungsten light spilling from open doorways, the blue evening sky between the buildings.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaTu = Bà Tư, 68, the gentle landlady of the old collective housing block; small and slightly stooped, a deeply lined kind face, cloudy warm eyes, silver hair in a low bun, a worn thin translucent patch with a faint violet light on the back of her neck; loose brown cotton blouse with cloth buttons, black silky trousers, plastic sandals.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot of the old woman on her plastic stool waving the young man over, locked off.
- Shot 2, 5–10s: 100mm extreme close-up of a faded old photo of a young mother holding a little girl beside a lake with a small pagoda, slow push-in.
- Shot 3, 10–15s: 85mm close-up of the old woman puzzling over the photo, handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaTu sits on her plastic stool holding an old photo and is already speaking warmly, waving @Khai over.
- 1–2s (Shot 1): @BaTu keeps talking as @Khai crouches beside her.
- 2–3s (Shot 1): @BaTu goes on, holding the photo out to him.
- 3–4s (Shot 1): @BaTu finishes and closes her mouth.
- 4–5s (Shot 1): @Khai takes the photo and answers slowly and gently.
- 5–6s (CUT to Shot 2): @Khai keeps talking as the faded picture shows a young mother holding a little girl beside a lake with a small pagoda.
- 6–7s (Shot 2): @Khai goes on, smiling faintly.
- 7–8s (Shot 2): @Khai finishes and closes his mouth.
- 8–9s (Shot 2): @BaTu leans in and speaks at an even pace, puzzled but smiling.
- 9–10s (Shot 2): @BaTu keeps talking, tapping the little girl in the photo.
- 10–11s (CUT to Shot 3): @BaTu goes on, frowning gently.
- 11–12s (Shot 3): @BaTu keeps speaking, shaking her head.
- 12–13s (Shot 3): @BaTu finishes and closes her mouth.
- 13–14s (Shot 3): @Khai's smile fades as he looks from the photo to the faded patch on her neck, silent.
- 14–15s (Shot 3): @BaTu keeps gazing at the photo with a soft, empty smile. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking at a natural, even conversational pace, warm, waving him over): "Khải về đấy à con? Lại đây, xem giúp bà cái ảnh này một tí."
- Turn 2, 5.1–8.8s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, tired, gentle): "Vâng, bà. Ảnh cũ quá bà nhỉ. Hồ Gươm ngày xưa đây mà."
- Turn 3, 9.3–14.3s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking at a natural, even conversational pace, puzzled, smiling): "Con bé bà đang bế đây là ai nhỉ? Bà thấy quen quen mà nghĩ mãi không ra."
- Pacing: @BaTu speaks at an even everyday pace, then @Khai answers slowly and calmly, then @BaTu answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets, a television through an open door, a wind chime, the creak of a plastic stool. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 2 (`canh-15/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The small shared courtyard of the old collective housing block at dusk: potted bonsai and chili plants, a low plastic table with plastic stools, a water tap, warm tungsten light spilling from open doorways, the blue evening sky between the buildings.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @BaTu = Bà Tư, 68, the gentle landlady of the old collective housing block; small and slightly stooped, a deeply lined kind face, cloudy warm eyes, silver hair in a low bun, a worn thin translucent patch with a faint violet light on the back of her neck; loose brown cotton blouse with cloth buttons, black silky trousers, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 100mm extreme close-up of faded handwriting on the back of the photo, too blurry to read, locked off.
- Shot 2, 5–10s: 85mm close-up of the old woman laughing it off, handheld.
- Shot 3, 10–15s: 40mm medium two-shot as the young man turns the photo back toward her, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai turns the photo over and is already speaking slowly, reading the faded handwriting on the back, too blurry for us to read.
- 1–2s (Shot 1): @Khai keeps reading carefully, tracing the line with his thumb.
- 2–3s (Shot 1): @Khai goes on, his voice soft.
- 3–4s (Shot 1): @Khai keeps speaking, looking up at her.
- 4–5s (Shot 1): @Khai finishes and closes his mouth.
- 5–6s (CUT to Shot 2): @BaTu laughs and answers, waving her hand.
- 6–7s (Shot 2): @BaTu keeps talking, shaking her head with amusement.
- 7–8s (Shot 2): @BaTu goes on, patting his arm.
- 8–9s (Shot 2): @BaTu finishes and closes her mouth, still smiling.
- 9–10s (Shot 2): @Khai turns the photo back toward her and speaks gently.
- 10–11s (CUT to Shot 3): @Khai keeps talking, holding the picture closer to her eyes.
- 11–12s (Shot 3): @Khai goes on, pointing at the young mother's face.
- 12–13s (Shot 3): @Khai finishes and closes his mouth.
- 13–14s (Shot 3): @BaTu leans in toward the photo, her smile slowly stiffening, mouth closed.
- 14–15s (Shot 3): @BaTu stares at the little girl's face, very still. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, reading carefully): "Đằng sau có ghi đây ạ... Mẹ và bé Hạnh, năm hai nghìn không trăm mười tám."
- Turn 2, 5.7–9.9s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking at a natural, even conversational pace, laughing it off): "Hạnh à? Bà làm gì có con gái nào tên Hạnh. Con đọc nhầm rồi."
- Turn 3, 10.4–14.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, gentle, insistent): "Bà ơi, cháu nghĩ là con gái bà đấy. Bà nhìn kỹ lại xem nào."
- Pacing: @Khai speaks slowly and calmly, then @BaTu answers at an even everyday pace, then @Khai answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets, the wind chime, a rice cooker clicking off in a kitchen, a gecko clicking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 3 (`canh-15/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The small shared courtyard of the old collective housing block at dusk: potted bonsai and chili plants, a low plastic table with plastic stools, a water tap, warm tungsten light spilling from open doorways, the blue evening sky between the buildings.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaTu = Bà Tư, 68, the gentle landlady of the old collective housing block; small and slightly stooped, a deeply lined kind face, cloudy warm eyes, silver hair in a low bun, a worn thin translucent patch with a faint violet light on the back of her neck; loose brown cotton blouse with cloth buttons, black silky trousers, plastic sandals.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the old woman's face crumpling, locked off.
- Shot 2, 5–9s: 40mm medium shot of the young man steadying her on the stool, handheld.
- Shot 3, 9–15s: 100mm extreme close-up of her trembling hands clutching the photo, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaTu is already speaking slowly in a small voice, her smile fading.
- 1–2s (Shot 1): @BaTu keeps talking, pressing the photo to her chest.
- 2–3s (Shot 1): @BaTu goes on, repeating the name with trembling lips.
- 3–4s (Shot 1): @BaTu keeps speaking, one hand going to her heart.
- 4–5s (Shot 1): @BaTu finishes and closes her mouth, eyes wet.
- 5–6s (CUT to Shot 2): @Khai answers at an even pace, worried, steadying her shoulders.
- 6–7s (Shot 2): @Khai keeps talking, guiding her back onto the stool.
- 7–8s (Shot 2): @Khai goes on, kneeling in front of her.
- 8–9s (Shot 2): @Khai finishes and closes his mouth.
- 9–10s (CUT to Shot 3): @BaTu answers slowly, breaking down, her hands trembling on the photo.
- 10–11s (Shot 3): @BaTu keeps speaking, shaking her head.
- 11–12s (Shot 3): @BaTu goes on, tears running down her lined cheeks.
- 12–13s (Shot 3): @BaTu keeps speaking, her voice cracking.
- 13–14s (Shot 3): @BaTu finishes and closes her mouth.
- 14–15s (Shot 3): @BaTu's trembling hands clutch the faded photo as a tear falls onto it. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking at a natural, even conversational pace, smile fading, voice small): "Bà làm gì có con... Hạnh... Hạnh... Sao cái tên này nghe đau thế này hả con?"
- Turn 2, 5.7–9.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, worried, steadying her): "Bà ơi, bà có sao không? Bà ngồi xuống đây đã, bà thở từ từ thôi."
- Turn 3, 10.2–14.3s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking slowly and softly, unhurried, with a short natural pause between phrases, breaking down): "Bà không nhớ. Sao bà lại không nhớ nổi con bé hả con?"
- Pacing: @BaTu speaks at an even everyday pace, then @Khai answers at an even everyday pace, then @BaTu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets, the wind chime, a sharp breath, a plastic stool scraping, the television murmuring. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 4 (`canh-15/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The small shared courtyard of the old collective housing block at dusk: potted bonsai and chili plants, a low plastic table with plastic stools, a water tap, warm tungsten light spilling from open doorways, the blue evening sky between the buildings.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @BaTu = Bà Tư, 68, the gentle landlady of the old collective housing block; small and slightly stooped, a deeply lined kind face, cloudy warm eyes, silver hair in a low bun, a worn thin translucent patch with a faint violet light on the back of her neck; loose brown cotton blouse with cloth buttons, black silky trousers, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm close-up of the young man holding the old woman's hands, locked off.
- Shot 2, 5–10s: 40mm medium shot of the old woman touching the faded patch on her neck, handheld.
- Shot 3, 10–15s: 35mm wide shot of the courtyard at dusk with the two small figures by the plants, slow pull-back.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai kneels holding both her hands and is already speaking slowly and steadily.
- 1–2s (Shot 1): @Khai keeps talking, squeezing her fingers.
- 2–3s (Shot 1): @Khai goes on, nodding firmly.
- 3–4s (Shot 1): @Khai finishes and closes his mouth.
- 4–5s (Shot 1): @BaTu wipes her eyes and answers, touching the faded patch on her neck.
- 5–6s (CUT to Shot 2): @BaTu keeps talking, rubbing the patch with her fingertips.
- 6–7s (Shot 2): @BaTu goes on, a faint smile through the tears.
- 7–8s (Shot 2): @BaTu keeps speaking, looking down at the photo.
- 8–9s (Shot 2): @BaTu finishes and closes her mouth.
- 9–10s (Shot 2): @Khai answers fast with quiet resolve.
- 10–11s (CUT to Shot 3): @Khai keeps talking quickly, his hand covering hers over the patch.
- 11–12s (Shot 3): @Khai goes on, looking into her eyes.
- 12–13s (Shot 3): @Khai finishes and closes his mouth.
- 13–14s (Shot 3): @BaTu nods slowly, mouth closed, holding the photo to her chest.
- 14–15s (Shot 3): The two small figures stay close together in the dusk courtyard under the warm doorway light. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.1s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, holding her hands, steady): "Không sao đâu bà. Cháu sẽ giúp bà nhớ lại. Cháu hứa đấy."
- Turn 2, 4.6–10.2s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking at a natural, even conversational pace, wiping her eyes): "Cái miếng dán này... từ hôm dán nó, bà ngủ ngon lắm. Mà hình như bà mất nhiều thứ quá."
- Turn 3, 10.7–13.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, quiet resolve): "Bà Tư, tối nay bà đừng dán nó nữa nhé. Cháu xin bà đấy."
- Pacing: @Khai speaks slowly and calmly, then @BaTu answers at an even everyday pace, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets, the wind chime, distant traffic, the faint electronic hum of the old patch. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 1 (`canh-16/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late at night, lit by the yellow desk lamp, the orange street light through the barred window and the glow of a phone on a small tripod on the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 40mm medium two-shot of the two sitting across the lamp-lit desk, locked off.
- Shot 2, 6–10s: 85mm close-up of the young man counting on his fingers, handheld.
- Shot 3, 10–15s: 40mm over-the-shoulder shot from behind the young man onto the woman in the lamplight, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy sits across the lamp-lit desk from @Khai and is already speaking in a low voice.
- 1–2s (Shot 1): @Vy keeps talking, tapping the closed laptop with one finger.
- 2–3s (Shot 1): @Vy goes on, glancing toward the window and the alley.
- 3–4s (Shot 1): @Vy keeps speaking, holding his gaze.
- 4–5s (Shot 1): @Vy goes on, her voice steady.
- 5–6s (Shot 1): @Vy finishes and closes her mouth.
- 6–7s (CUT to Shot 2): @Khai answers fast and bitterly, counting on his fingers.
- 7–8s (Shot 2): @Khai keeps talking quickly, folding down one finger after another.
- 8–9s (Shot 2): @Khai goes on, spreading his hands.
- 9–10s (Shot 2): @Khai finishes and closes his mouth.
- 10–11s (CUT to Shot 3): @Vy answers slowly and quietly, not looking away.
- 11–12s (Shot 3): @Vy keeps speaking, her voice barely above a whisper.
- 12–13s (Shot 3): @Vy finishes and closes her mouth.
- 13–14s (Shot 3): @Khai lowers his hands slowly, mouth closed.
- 14–15s (Shot 3): The lamp hums between them as neither speaks. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.2s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, laying out the facts, low): "Nếu anh gỡ chip ra, anh giữ được ký ức. Nhưng họ sẽ đòi lại tiền, và họ biết nhà anh ở đâu."
- Turn 2, 6.7–9.5s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, bitter, counting on his fingers): "Còn nếu tôi ngủ, tôi quên hết, lấy tiền, trả nợ, yên ổn."
- Turn 3, 10.0–13.4s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, final): "Ừ. Và thầy Lâm sẽ chết như chưa từng chết bao giờ."
- Pacing: @Vy speaks at an even everyday pace, then @Khai answers quickly, then @Vy answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the electric fan, a soft snore from behind the loft curtain, a night bus passing, the laptop fan. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 2 (`canh-16/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late at night, lit by the yellow desk lamp, the orange street light through the barred window and the glow of a phone on a small tripod on the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 85mm close-up of the young man, handheld.
- Shot 2, 6–11s: 50mm over-the-shoulder shot from behind the young man onto the woman, locked off.
- Shot 3, 11–15s: 35mm low-angle wide shot from the desk up to the closed loft curtain, slow tilt up.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking in a frustrated voice, rubbing his forehead.
- 1–2s (Shot 1): @Khai keeps talking, gesturing at himself in his orange jacket.
- 2–3s (Shot 1): @Khai goes on, shaking his head.
- 3–4s (Shot 1): @Khai keeps speaking, throwing up one hand.
- 4–5s (Shot 1): @Khai goes on, his voice cracking at the end.
- 5–6s (Shot 1): @Khai finishes and closes his mouth.
- 6–7s (CUT to Shot 2): @Vy answers slowly and flatly, staring at the desk.
- 7–8s (Shot 2): @Vy keeps talking, counting losses on her fingers without looking up.
- 8–9s (Shot 2): @Vy goes on, her voice worn out.
- 9–10s (Shot 2): @Vy keeps speaking, pulling her hoodie sleeves over her hands.
- 10–11s (Shot 2): @Vy finishes and closes her mouth.
- 11–12s (CUT to Shot 3): @Khai lifts his eyes to the closed loft curtain and speaks slowly.
- 12–13s (Shot 3): @Khai keeps speaking softly, his face tender.
- 13–14s (Shot 3): @Khai finishes and closes his mouth.
- 14–15s (Shot 3): The loft curtain stirs faintly as the sleeping girl behind it turns over. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, frustrated, hopeless): "Mà kể cả tôi giữ được, một thằng giao hàng đi tố cáo ông chủ tập đoàn bằng một giấc mơ. Ai tin?"
- Turn 2, 6.7–11.2s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, flat, worn out): "Không ai tin đâu. Tôi đã thử. Tôi mất việc, mất nhà, mất luôn bạn bè."
- Turn 3, 11.7–14.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, looking up at the loft): "Em gái tôi đang ngủ ngay trên kia kìa..."
- Pacing: @Khai speaks at an even everyday pace, then @Vy answers slowly and calmly, then @Khai answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the electric fan, a soft breath from behind the curtain, the laptop fan, a dog barking far away. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 3 (`canh-16/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late at night, lit by the yellow desk lamp, the orange street light through the barred window and the glow of a phone on a small tripod on the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young man remembering, locked off.
- Shot 2, 5–9s: 50mm medium shot of the woman, handheld.
- Shot 3, 9–15s: 35mm wide shot of the lamp-lit room as the young man sits up straight with a new idea, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking slowly, staring at his own reflection in the dark window.
- 1–2s (Shot 1): @Khai keeps talking, his face pained.
- 2–3s (Shot 1): @Khai goes on, touching the back of his neck.
- 3–4s (Shot 1): @Khai keeps speaking softly.
- 4–5s (Shot 1): @Khai finishes and closes his mouth.
- 5–6s (CUT to Shot 2): @Vy answers quietly and sadly.
- 6–7s (Shot 2): @Vy keeps talking, nodding toward the city beyond the window.
- 7–8s (Shot 2): @Vy goes on, her eyes lowered.
- 8–9s (Shot 2): @Vy finishes and closes her mouth.
- 9–10s (CUT to Shot 3): @Khai sits up straight and starts speaking fast, an idea forming.
- 10–11s (Shot 3): @Khai keeps talking quickly, picking up his phone from the desk.
- 11–12s (Shot 3): @Khai goes on, turning the phone's camera lens toward himself.
- 12–13s (Shot 3): @Khai keeps speaking, his eyes bright.
- 13–14s (Shot 3): @Khai finishes and closes his mouth.
- 14–15s (Shot 3): @Vy looks from the phone to his face, mouth closed, slowly understanding. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, remembering, pained): "Bà Tư không còn nhớ con gái mình nữa. Bà ấy dán cái này mười năm."
- Turn 2, 5.4–8.9s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, quiet, sad): "Có hàng triệu người như bà ấy. Họ không biết mình đang mất gì."
- Turn 3, 9.4–13.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, rising, an idea forming): "Không ai tin một giấc mơ. Nhưng người ta sẽ tin cái người ta tận mắt nhìn thấy."
- Pacing: @Khai speaks slowly and calmly, then @Vy answers at an even everyday pace, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the electric fan, the laptop fan, a motorbike passing in the alley, his chair scraping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 4 (`canh-16/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late at night, lit by the yellow desk lamp, the orange street light through the barred window and the glow of a phone on a small tripod on the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 85mm close-up of the woman asking, locked off.
- Shot 2, 4–9s: 40mm medium shot of the young man setting his phone on a small tripod on the desk, handheld.
- Shot 3, 9–15s: 50mm close-up of the woman opening her cracked laptop with a faint smile, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy is already speaking cautiously, watching him.
- 1–2s (Shot 1): @Vy keeps talking, her head tilted.
- 2–3s (Shot 1): @Vy finishes and closes her mouth.
- 3–4s (Shot 1): @Vy waits, her hands resting on the laptop.
- 4–5s (CUT to Shot 2): @Khai answers fast, clipping his phone onto a small tripod on the desk.
- 5–6s (Shot 2): @Khai keeps talking quickly, angling the tripod toward his chair.
- 6–7s (Shot 2): @Khai goes on, checking the framing on the screen.
- 7–8s (Shot 2): @Khai keeps speaking, turning to @Vy.
- 8–9s (Shot 2): @Khai finishes and closes his mouth, waiting.
- 9–10s (CUT to Shot 3): @Vy answers slowly, opening her cracked laptop with a small smile.
- 10–11s (Shot 3): @Vy keeps speaking, the screen lighting her face.
- 11–12s (Shot 3): @Vy goes on, cracking her knuckles.
- 12–13s (Shot 3): @Vy finishes and closes her mouth.
- 13–14s (Shot 3): @Khai sits down in front of the tripod, mouth closed, taking a deep breath.
- 14–15s (Shot 3): @Vy pulls her chair beside him, both facing the little phone lens. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–2.2s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, cautious): "Thế anh định làm gì bây giờ?"
- Turn 2, 2.7–7.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, decided, urgent): "Phát trực tiếp. Kể hết những gì tôi còn nhớ, trước khi họ xóa nó đi. Cô có danh sách tài khoản đúng không?"
- Turn 3, 8.2–12.4s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, opening her laptop, a small smile): "Có. Tôi mang theo đủ cả. Mười một giờ bốn mươi bảy, ta bắt đầu."
- Pacing: @Vy speaks at an even everyday pace, then @Khai answers quickly, then @Vy answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone clicking into a small tripod, the laptop lid opening, the laptop fan speeding up, the electric fan. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 1 (`canh-17/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late at night, lit by the yellow desk lamp, the orange street light through the barred window and the glow of a phone on a small tripod on the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot from behind the tripod of the young man facing the phone lens, locked off.
- Shot 2, 5–10s: 85mm close-up of the young man speaking into the lens, slow push-in.
- Shot 3, 10–15s: 40mm medium two-shot of the young man and the woman side by side, the laptop glowing, handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai sits facing the phone on its tripod and is already speaking steadily into the lens.
- 1–2s (Shot 1): @Khai keeps talking, his hands gripping his knees.
- 2–3s (Shot 1): @Khai goes on, swallowing once.
- 3–4s (Shot 1): @Khai keeps speaking, touching the violet patch on his neck.
- 4–5s (Shot 1): @Khai finishes and closes his mouth for a breath.
- 5–6s (CUT to Shot 2): @Khai leans closer to the lens and speaks fast and urgently.
- 6–7s (Shot 2): @Khai keeps talking quickly, tapping his temple.
- 7–8s (Shot 2): @Khai goes on, eyes locked on the lens.
- 8–9s (Shot 2): @Khai keeps speaking fast.
- 9–10s (Shot 2): @Khai finishes and closes his mouth.
- 10–11s (CUT to Shot 3): @Vy, beside him with the laptop, speaks slowly in a hushed aside.
- 11–12s (Shot 3): @Vy keeps speaking softly, turning the laptop slightly toward him.
- 12–13s (Shot 3): @Vy finishes and closes her mouth.
- 13–14s (Shot 3): @Khai glances at the laptop and back at the lens, mouth closed.
- 14–15s (Shot 3): The small red live light on the phone glows steadily. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, straight into the lens, steady): "Tôi tên là Khải. Tôi là người giao hàng. Bảy ngày trước, tôi cho NeuroRent thuê não."
- Turn 2, 5.2–9.4s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, urgent): "Mười ba phút nữa, họ sẽ xóa thứ trong đầu tôi. Nên tôi kể ra đây, trước khi tôi quên."
- Turn 3, 9.9–12.4s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, a hushed aside, eyes on the laptop): "Có người vào xem rồi đấy. Bốn mươi người."
- Pacing: @Khai speaks at an even everyday pace, then @Khai continues quickly, then @Vy answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft live-start beep, the electric fan, the laptop fan, a faint stream of notification ticks. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 2 (`canh-17/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late at night, lit by the yellow desk lamp, the orange street light through the barred window and the glow of a phone on a small tripod on the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young man rattling off details, handheld.
- Shot 2, 5–10s: 50mm medium shot of the young man drawing glasses in the air, locked off.
- Shot 3, 10–15s: 50mm over-the-shoulder shot from behind the tripod as the woman leans in and turns the laptop screen toward the phone lens, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking fast, rattling off details to the lens.
- 1–2s (Shot 1): @Khai keeps talking quickly, counting on his fingers.
- 2–3s (Shot 1): @Khai goes on, gesturing a torn corner in the air.
- 3–4s (Shot 1): @Khai keeps speaking fast, tilting his hand like a crooked frame.
- 4–5s (Shot 1): @Khai finishes and closes his mouth for a breath.
- 5–6s (CUT to Shot 2): @Khai continues at an even pace, drawing a pair of glasses in the air.
- 6–7s (Shot 2): @Khai keeps talking carefully.
- 7–8s (Shot 2): @Khai goes on, his voice dropping.
- 8–9s (Shot 2): @Khai finishes and closes his mouth.
- 9–10s (Shot 2): @Vy leans into frame and speaks firmly to the lens.
- 10–11s (CUT to Shot 3): @Vy keeps talking, turning the laptop screen toward the phone.
- 11–12s (Shot 3): @Vy goes on as rows of blurred lines glow on the cracked screen.
- 12–13s (Shot 3): @Vy finishes and closes her mouth.
- 13–14s (Shot 3): @Khai nods at the lens, mouth closed.
- 14–15s (Shot 3): The phone's small red light glows as the laptop screen shines toward it. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, rattling off details): "Khu tập thể Kim Liên, nhà C, phòng bảy linh bốn. Rèm vàng rách góc trái. Tranh hoa sen treo lệch."
- Turn 2, 5.3–8.8s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, slower, careful): "Một người đàn ông đeo kính gọng đen, kỹ sư trưởng, tên là Lâm."
- Turn 3, 9.3–12.8s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, stepping into frame, firm): "Tôi là Vy, kỹ sư hệ thống cũ của NeuroRent. Đây là danh sách."
- Pacing: @Khai speaks quickly, then @Khai continues at an even everyday pace, then @Vy answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the electric fan, rapid notification ticks, the laptop fan, keys tapping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 3 (`canh-17/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late at night, lit by the yellow desk lamp, the orange street light through the barred window and the glow of a phone on a small tripod on the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 100mm extreme close-up of the cracked laptop screen scrolling rows of blurred lines, locked off.
- Shot 2, 5–10s: 85mm close-up of the young man reading the phone screen, handheld.
- Shot 3, 10–15s: 40mm medium two-shot of the two staring at the phone, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy is already speaking fast as her finger scrolls endless blurred rows on the cracked laptop screen.
- 1–2s (Shot 1): @Vy keeps talking quickly, the rows racing past.
- 2–3s (Shot 1): @Vy goes on, stopping the scroll with one tap.
- 3–4s (Shot 1): @Vy keeps speaking, looking at the lens.
- 4–5s (Shot 1): @Vy finishes and closes her mouth.
- 5–6s (CUT to Shot 2): @Khai leans toward the phone and speaks at an even pace, reading.
- 6–7s (Shot 2): @Khai keeps talking, his voice moved.
- 7–8s (Shot 2): @Khai goes on, blinking hard.
- 8–9s (Shot 2): @Khai finishes and closes his mouth.
- 9–10s (Shot 2): @Vy speaks slowly and quietly, awed.
- 10–11s (CUT to Shot 3): @Vy keeps speaking, pressing her fingers to her lips.
- 11–12s (Shot 3): @Vy finishes and closes her mouth.
- 12–13s (Shot 3): @Khai and @Vy look at each other, both silent.
- 13–14s (Shot 3): The phone screen's glow flickers faster on their faces.
- 14–15s (Shot 3): Behind them the scrawled wall is lit by the shifting light. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking quickly in short lively phrases, every word still clear, scrolling quickly): "Mỗi dòng là một người đang bị cất ký ức của người khác vào đầu. Hơn ba triệu tài khoản."
- Turn 2, 5.1–8.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, reading comments, moved): "Mọi người bình luận... Bà ngoại tôi cũng dán cái này. Mẹ tôi cũng dán."
- Turn 3, 9.4–12.8s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, awed, quiet): "Tám nghìn người đang xem rồi. Họ đang chia sẻ khắp nơi."
- Pacing: @Vy speaks quickly, then @Khai answers at an even everyday pace, then @Vy answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a flood of notification ticks, the laptop fan, the electric fan, a neighbour's phone buzzing through the wall. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 4 (`canh-17/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late at night, lit by the yellow desk lamp, the orange street light through the barred window and the glow of a phone on a small tripod on the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young man naming the CEO into the lens, locked off.
- Shot 2, 5–9s: 100mm extreme close-up of the patch on the back of his neck blinking red, handheld.
- Shot 3, 9–15s: 40mm medium two-shot as the woman grips his arm and he forces himself upright, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking slowly and clearly into the lens, naming the man.
- 1–2s (Shot 1): @Khai keeps talking, his jaw set.
- 2–3s (Shot 1): @Khai goes on, not blinking.
- 3–4s (Shot 1): @Khai keeps speaking, his voice hard.
- 4–5s (Shot 1): @Khai finishes and closes his mouth.
- 5–6s (CUT to Shot 2): @Vy speaks fast, alarmed, as the patch on @Khai's neck starts blinking red.
- 6–7s (Shot 2): @Vy keeps talking quickly, pointing at his neck.
- 7–8s (Shot 2): @Vy goes on, gripping his arm.
- 8–9s (Shot 2): @Vy finishes and closes her mouth.
- 9–10s (CUT to Shot 3): @Khai answers slowly, straining, sweat beading on his forehead.
- 10–11s (Shot 3): @Khai keeps speaking, gritting his teeth.
- 11–12s (Shot 3): @Khai goes on, pressing his palm flat on the desk.
- 12–13s (Shot 3): @Khai finishes and closes his mouth.
- 13–14s (Shot 3): @Khai forces himself upright in the chair, the red light pulsing at his neck.
- 14–15s (Shot 3): @Vy keeps hold of his arm, both staring at the phone lens. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, slow and clear, naming him): "Người đẩy ông Lâm ngã vào góc bàn là Trịnh Huy. Chính là ông chủ của NeuroRent."
- Turn 2, 5.2–8.4s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking quickly in short lively phrases, every word still clear, alarmed): "Anh Khải, chip của anh đang nháy đỏ kìa. Họ bắt đầu sớm hơn rồi!"
- Turn 3, 8.9–12.8s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, strained, gritting his teeth): "Không sao. Tôi vẫn còn nhớ. Tôi còn nhớ được... Cố lên nào, Khải."
- Pacing: @Khai speaks at an even everyday pace, then @Vy answers quickly, then @Khai answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a sharp electronic warning beep, a rising glitch whine, the electric fan, his breathing quickening. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 1 (`canh-18/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late at night, lit by the yellow desk lamp, the orange street light through the barred window and the glow of a phone on a small tripod on the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Nova = Nova, the NeuroRent app's holographic assistant; a softly glowing translucent violet hologram of a young woman about a hand's height tall, standing on a beam of light above a phone screen, a smooth calm face with a gentle fixed smile, sleek hair in a high knot, faint horizontal scan lines through her body; a simple fitted violet light-dress.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the hologram on the desk now glowing red-violet, locked off.
- Shot 2, 5–10s: 50mm medium shot of the young man defiant in front of the tripod, the picture glitching, handheld.
- Shot 3, 10–15s: 100mm extreme close-up of the hologram's smile breaking into static, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): On the desk @Nova rises from the phone glowing red-violet and is already speaking slowly in a cold voice.
- 1–2s (Shot 1): @Nova keeps talking, her smile gone for the first time.
- 2–3s (Shot 1): @Nova goes on, raising one hand like a stop sign.
- 3–4s (Shot 1): @Nova keeps speaking, static crawling through her body.
- 4–5s (Shot 1): @Nova finishes and closes her mouth.
- 5–6s (CUT to Shot 2): @Khai leans past her toward the tripod lens and speaks fast, gritting his teeth.
- 6–7s (Shot 2): @Khai keeps talking quickly as the picture glitches around him.
- 7–8s (Shot 2): @Khai goes on, gripping the edge of the desk.
- 8–9s (Shot 2): @Khai keeps speaking fast, sweat running down his temple.
- 9–10s (Shot 2): @Khai finishes and closes his mouth, panting.
- 10–11s (CUT to Shot 3): @Nova answers in a voice gone eerily sweet again.
- 11–12s (Shot 3): @Nova keeps talking, her smile returning.
- 12–13s (Shot 3): @Nova goes on, tilting her head.
- 13–14s (Shot 3): @Nova finishes and closes her mouth.
- 14–15s (Shot 3): @Nova's smiling face breaks apart into red static for a moment, then re-forms. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking slowly and softly, unhurried, with a short natural pause between phrases, for the first time cold): "Anh Khải. Vui lòng kết thúc phát sóng ngay. Đây là cảnh báo cuối cùng."
- Turn 2, 5.3–8.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, gritting his teeth, defiant): "Không! Mọi người nghe tôi. Ngày sáu tháng mười một, lúc ba giờ mười bảy phút sáng."
- Turn 3, 9.4–13.1s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking at a natural, even conversational pace, sweetness returning, eerie): "Phiên thu hồi bắt đầu sớm hơn. Anh sẽ không cảm thấy đau đâu."
- Pacing: @Nova speaks slowly and calmly, then @Khai answers quickly, then @Nova answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a harsh warning tone, the hologram crackling with static, a rising digital whine, the electric fan stuttering. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 2 (`canh-18/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 11s; it intercuts the two places or times named in the shot list, each shot keeping its own place and light, with sound continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late at night, lit by the yellow desk lamp, the orange street light through the barred window and the glow of a phone on a small tripod on the desk. Intercut with cold cyan memory flashes: Memory flashback graded cold cyan-blue with faint flickering glitch: a dim abandoned apartment in an old collective housing block at night, a torn yellow curtain on the window, a crooked lotus painting on the wall, a heavy dark wooden table with a sharp corner, dust floating in the light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young man forcing out words, the room flickering, handheld.
- Shot 2, 5–8s: 50mm medium shot of the woman gripping his shoulder, locked off.
- Shot 3, 8–11s: 100mm extreme close-up memory shot in cold cyan light of black-rimmed glasses lying under a heavy wooden table, locked off.
- Shot 4, 11–15s: 85mm close-up of the young man straining to stay awake, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Each shot keeps the lighting of its own place and time; faces, wardrobe and props stay consistent; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking fast, forcing the words out, the room flickering around him.
- 1–2s (Shot 1): @Khai keeps talking quickly, his eyes squeezing shut.
- 2–3s (Shot 1): @Khai goes on, one hand pressed to his temple.
- 3–4s (Shot 1): @Khai keeps speaking fast, sweat dripping from his chin.
- 4–5s (Shot 1): @Khai finishes and closes his mouth, gasping.
- 5–6s (CUT to Shot 2): @Vy grips his shoulder and speaks, begging.
- 6–7s (Shot 2): @Vy keeps talking, shaking him gently.
- 7–8s (Shot 2): @Vy finishes and closes her mouth, her eyes wet.
- 8–9s (CUT to Shot 3): @Khai's voice comes slowly over a cold cyan memory of black-rimmed glasses lying under a heavy wooden table.
- 9–10s (Shot 3): @Khai keeps speaking slowly as the memory image holds on the glasses in the dust.
- 10–11s (Shot 3): The cyan image shudders with static and tears away.
- 11–12s (CUT to Shot 4): Back in the room @Khai goes on slowly, struggling to stay upright.
- 12–13s (Shot 4): @Khai keeps speaking, his eyes half closing.
- 13–14s (Shot 4): @Khai finishes and closes his mouth.
- 14–15s (Shot 4): @Khai sways in the chair, mouth closed, the red light at his neck blinking frantically. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, forcing the words out): "Ông Lâm định đi báo công an. Huy chặn cửa. Huy đẩy ông ấy. Ông ấy đập đầu vào góc bàn."
- Turn 2, 5.3–8.3s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, begging, gripping his shoulder): "Đủ rồi, anh Khải! Từng ấy là đủ rồi! Gỡ ra đi!"
- Turn 3, 8.8–13.6s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, fighting to hold on): "Chưa đủ. Còn chiếc kính... chiếc kính văng vào gầm bàn. Cảnh sát sẽ tìm thấy nó."
- Pacing: @Khai speaks quickly, then @Vy answers at an even everyday pace, then @Khai answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a glitch whine rising and falling, the patch beeping faster, a muffled echo of a dull thud from the memory, his ragged breathing. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 3 (`canh-18/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late at night, lit by the yellow desk lamp, the orange street light through the barred window and the glow of a phone on a small tripod on the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; a loose pale-blue T-shirt and grey cotton shorts, hair down over her shoulders.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
- Wardrobe: in this shot @Linh wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium shot of the schoolgirl scrambling down the loft ladder, handheld.
- Shot 2, 5–10s: 85mm close-up of the young man smiling weakly at her, locked off.
- Shot 3, 10–15s: 50mm medium two-shot of the schoolgirl holding her brother's face in both hands, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh scrambles down the loft ladder in her home clothes and is already speaking fast, her eyes wide.
- 1–2s (Shot 1): @Linh keeps talking quickly as she drops to the floor.
- 2–3s (Shot 1): @Linh goes on, pointing at the red light blinking on his neck.
- 3–4s (Shot 1): @Linh keeps speaking fast, rushing to his chair.
- 4–5s (Shot 1): @Linh finishes and closes her mouth, kneeling in front of him.
- 5–6s (CUT to Shot 2): @Khai turns his head to her and answers slowly with a weak smile.
- 6–7s (Shot 2): @Khai keeps talking softly, lifting one heavy hand to her hair.
- 7–8s (Shot 2): @Khai goes on, his eyelids drooping.
- 8–9s (Shot 2): @Khai keeps speaking gently.
- 9–10s (Shot 2): @Khai finishes and closes his mouth.
- 10–11s (CUT to Shot 3): @Linh takes his face in both hands and speaks, crying.
- 11–12s (Shot 3): @Linh keeps talking, shaking his face gently.
- 12–13s (Shot 3): @Linh goes on, tears running down her cheeks.
- 13–14s (Shot 3): @Linh finishes and closes her mouth, sobbing.
- 14–15s (Shot 3): @Khai looks at her with a tired smile, mouth closed, her hands still on his cheeks. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking quickly in short lively phrases, every word still clear, scrambling down the loft ladder, frightened): "Anh ơi! Anh làm sao thế? Sao cổ anh sáng đỏ thế kia? Anh nói chuyện với ai thế?"
- Turn 2, 4.9–9.1s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, smiling weakly): "Linh à. Không sao đâu em. Anh chỉ đi ngủ một chút thôi mà em."
- Turn 3, 9.6–12.6s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking at a natural, even conversational pace, holding his face, crying): "Anh đừng ngủ! Anh nhìn em đi này, anh không được ngủ!"
- Pacing: @Linh speaks quickly, then @Khai answers slowly and calmly, then @Linh answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a wooden ladder creaking under quick feet, the patch beeping, the glitch whine, a sob. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 4 (`canh-18/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, late at night, lit by the yellow desk lamp, the orange street light through the barred window and the glow of a phone on a small tripod on the desk.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Nova = Nova, the NeuroRent app's holographic assistant; a softly glowing translucent violet hologram of a young woman about a hand's height tall, standing on a beam of light above a phone screen, a smooth calm face with a gentle fixed smile, sleek hair in a high knot, faint horizontal scan lines through her body; a simple fitted violet light-dress.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; faded orange delivery jacket with a plain patch without letters over a grey T-shirt, dark jeans, worn black sneakers.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 85mm close-up of the red-violet hologram on the desk, locked off.
- Shot 2, 4–10s: 50mm medium shot of the young man looking off toward his sister with a tender smile, slow push-in.
- Shot 3, 10–15s: 35mm wide shot of the room flickering harder and harder until it washes out to pure white, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): On the desk @Nova glows red-violet above the phone and is already speaking slowly in a cold, final voice.
- 1–2s (Shot 1): @Nova keeps talking, raising ten small glowing fingers.
- 2–3s (Shot 1): @Nova goes on, her face blank.
- 3–4s (Shot 1): @Nova finishes and closes her mouth.
- 4–5s (CUT to Shot 2): @Khai turns his face toward his sister just out of frame and speaks tenderly.
- 5–6s (Shot 2): @Khai keeps talking, a soft smile on his lips.
- 6–7s (Shot 2): @Khai goes on, his eyes shining.
- 7–8s (Shot 2): @Khai keeps speaking, nodding gently.
- 8–9s (Shot 2): @Khai goes on, his voice thick.
- 9–10s (Shot 2): @Khai finishes and closes his mouth, still smiling.
- 10–11s (CUT to Shot 3): @Nova counts down slowly, folding one glowing finger at a time, as the whole room flickers.
- 11–12s (Shot 3): @Nova keeps counting while the cyan memory and the room flash over each other faster.
- 12–13s (Shot 3): @Nova goes on counting as the red light on @Khai's neck becomes a solid glare.
- 13–14s (Shot 3): @Nova finishes the count and closes her mouth.
- 14–15s (Shot 3): The entire room washes out to pure white light. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.0s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking slowly and softly, unhurried, with a short natural pause between phrases, cold, final): "Anh Khải. Thu hồi sẽ bắt đầu sau mười giây nữa thôi."
- Turn 2, 4.5–10.5s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, tender, saying goodbye): "Linh này. Ở nhà học cho tử tế nghe chưa. Thi đỗ đại học cho anh nhé. Anh thương em nhiều lắm, Linh ạ."
- Turn 3, 11.0–14.0s, spoken on camera by @Nova (sweet smooth synthetic young woman's voice, perfectly calm and polite, speaking slowly and softly, unhurried, with a short natural pause between phrases, counting down evenly): "Mười, chín, tám, bảy, sáu, năm, bốn, ba, hai, một."
- Pacing: @Nova speaks slowly and calmly, then @Khai answers at an even everyday pace, then @Nova answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a slow ticking, the patch beeping faster and faster, the glitch whine climbing, then total silence on a white flash. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 1 (`canh-19/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, early morning, pale sunlight through the barred window and a small mirror above a basin by the door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; a loose pale-blue T-shirt and grey cotton shorts, hair down over her shoulders.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Linh and @Khai wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the schoolgirl with red eyes leaning over the bed, locked off.
- Shot 2, 5–10s: 40mm medium shot of the young man sitting up in bed, handheld.
- Shot 3, 10–15s: 85mm close-up of the schoolgirl hugging him, her face on his shoulder, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh leans over the bed with red, sleepless eyes and is already speaking slowly.
- 1–2s (Shot 1): @Linh keeps talking, her voice trembling.
- 2–3s (Shot 1): @Linh goes on, gripping the edge of the blanket.
- 3–4s (Shot 1): @Linh keeps speaking, holding her breath between words.
- 4–5s (Shot 1): @Linh finishes and closes her mouth.
- 5–6s (CUT to Shot 2): @Khai sits up and answers fast with a puzzled laugh.
- 6–7s (Shot 2): @Khai keeps talking quickly, rubbing his eyes.
- 7–8s (Shot 2): @Khai goes on, glancing at the sunlight in the window.
- 8–9s (Shot 2): @Khai finishes and closes his mouth, frowning at her.
- 9–10s (Shot 2): @Linh answers, laughing and crying at once.
- 10–11s (CUT to Shot 3): @Linh keeps talking, throwing her arms around his neck.
- 11–12s (Shot 3): @Linh goes on, squeezing him tight.
- 12–13s (Shot 3): @Linh finishes and closes her mouth, sobbing into his shoulder.
- 13–14s (Shot 3): @Khai pats her back awkwardly, confused, mouth closed.
- 14–15s (Shot 3): Morning sun falls through the bars across the two of them. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking slowly and softly, unhurried, with a short natural pause between phrases, eyes red, terrified of the answer): "Anh tỉnh rồi à? Anh có nhận ra em không? Em là ai, anh nói đi?"
- Turn 2, 5.4–9.0s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, puzzled laugh, sitting up): "Hỏi gì lạ thế? Em là Linh chứ ai. Mấy giờ rồi, sao em không đi học?"
- Turn 3, 9.5–13.0s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking at a natural, even conversational pace, laughing and crying at once): "Anh vẫn nhớ em. Anh vẫn nhớ em thật này. Thế là tốt rồi."
- Pacing: @Linh speaks slowly and calmly, then @Khai answers quickly, then @Linh answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning birds, a rooster far away, the electric fan, a sniffle, bedsprings creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 2 (`canh-19/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, early morning, pale sunlight through the barred window and a small mirror above a basin by the door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; a loose pale-blue T-shirt and grey cotton shorts, hair down over her shoulders.
- Wardrobe: in this shot @Khai and @Linh wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the young man holding his sister at arm's length, handheld.
- Shot 2, 5–10s: 85mm close-up of the schoolgirl pushing her glowing phone into his hands, locked off.
- Shot 3, 10–15s: 100mm extreme close-up of the young man's eyes reflecting the glowing phone screen, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai holds his sister at arm's length and is already speaking in a confused voice.
- 1–2s (Shot 1): @Khai keeps talking, touching her swollen eyes with his thumb.
- 2–3s (Shot 1): @Khai goes on, looking around the room.
- 3–4s (Shot 1): @Khai keeps speaking, shaking his head.
- 4–5s (Shot 1): @Khai finishes and closes his mouth.
- 5–6s (CUT to Shot 2): @Linh answers fast, excited, pushing her glowing phone into his hands.
- 6–7s (Shot 2): @Linh keeps talking quickly, pointing at the screen.
- 7–8s (Shot 2): @Linh goes on, bouncing on the edge of the bed.
- 8–9s (Shot 2): @Linh finishes and closes her mouth, watching his face.
- 9–10s (Shot 2): @Khai stares at the screen and speaks slowly.
- 10–11s (CUT to Shot 3): @Khai keeps speaking softly, the screen's light on his face.
- 11–12s (Shot 3): @Khai goes on, his brow furrowed.
- 12–13s (Shot 3): @Khai finishes and closes his mouth.
- 13–14s (Shot 3): In extreme close-up the glowing screen is reflected in @Khai's eyes.
- 14–15s (Shot 3): @Khai keeps staring, blank and wondering, as the light flickers in his eyes. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, confused, concerned): "Sao mắt em sưng thế? Đêm qua có chuyện gì à? Anh chẳng nhớ gì cả đấy."
- Turn 2, 5.2–8.8s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking quickly in short lively phrases, every word still clear, handing him her phone, excited): "Anh xem đi này. Bốn triệu lượt xem. Sáng nay người ta bắt ông chủ NeuroRent rồi."
- Turn 3, 9.3–12.7s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, staring at a stranger who is himself): "Người đang nói trong cái video này... là anh thật đấy à?"
- Pacing: @Khai speaks at an even everyday pace, then @Linh answers quickly, then @Khai answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning birds, a faint muffled voice from a phone speaker, the electric fan, a scooter in the alley. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 3 (`canh-19/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, early morning, pale sunlight through the barred window and a small mirror above a basin by the door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium shot of the woman in the grey hoodie standing in the open doorway holding a small old phone, locked off.
- Shot 2, 5–10s: 85mm close-up of the young man looking at her politely, handheld.
- Shot 3, 10–15s: 100mm extreme close-up of the woman's face, a small smile and wet eyes, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy stands in the open doorway in her grey hoodie and is already speaking slowly and quietly.
- 1–2s (Shot 1): @Vy keeps talking, holding out a small old phone in both hands.
- 2–3s (Shot 1): @Vy goes on, her eyes searching his face.
- 3–4s (Shot 1): @Vy keeps speaking softly.
- 4–5s (Shot 1): @Vy finishes and closes her mouth.
- 5–6s (CUT to Shot 2): @Khai stands by the bed and answers politely, his face blank.
- 6–7s (Shot 2): @Khai keeps talking, scratching the back of his neck where the patch used to be.
- 7–8s (Shot 2): @Khai goes on with a friendly, apologetic smile.
- 8–9s (Shot 2): @Khai keeps speaking, tilting his head.
- 9–10s (Shot 2): @Khai finishes and closes his mouth.
- 10–11s (CUT to Shot 3): @Vy answers slowly with a small wistful smile.
- 11–12s (Shot 3): @Vy keeps speaking, swallowing hard.
- 12–13s (Shot 3): @Vy goes on, her voice steady with effort.
- 13–14s (Shot 3): @Vy finishes and closes her mouth.
- 14–15s (Shot 3): @Vy holds the wistful smile, her eyes glistening, still holding out the little phone. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, emotional): "Chào anh. Tôi đến để cảm ơn anh. Và để trả lại cho anh cái này."
- Turn 2, 5.4–9.9s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, polite, blank): "Chào chị ạ. Xin lỗi chị... chị là ai nhỉ? Mình đã gặp nhau bao giờ chưa ạ?"
- Turn 3, 10.4–13.8s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking slowly and softly, unhurried, with a short natural pause between phrases, a small sad smile): "Chưa đâu. Coi như là chưa bao giờ. Tôi tên là Vy."
- Pacing: @Vy speaks slowly and calmly, then @Khai answers at an even everyday pace, then @Vy answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft knock on a wooden door, the door creaking open, morning birds, distant street sounds. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 4 (`canh-19/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, early morning, pale sunlight through the barred window and a small mirror above a basin by the door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- @Vy = Vy, 30, a former NeuroRent systems engineer in hiding; slim, pale skin, a chin-length black bob, dark circles under sharp guarded eyes, a small scar through her left eyebrow; oversized charcoal-grey hoodie, black cargo trousers, black boots, a battered laptop bag across her chest.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the young man thinking, locked off.
- Shot 2, 5–10s: 100mm extreme close-up of the woman pressing the small old phone into his palm, handheld.
- Shot 3, 10–15s: 40mm medium shot of the young man alone in the doorway holding the phone as footsteps fade, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai is already speaking, puzzled, repeating the name to himself.
- 1–2s (Shot 1): @Khai keeps talking thoughtfully, frowning.
- 2–3s (Shot 1): @Khai goes on, tapping his temple.
- 3–4s (Shot 1): @Khai finishes and closes his mouth.
- 4–5s (Shot 1): @Vy steps forward and speaks, pressing the small old phone into his palm.
- 5–6s (CUT to Shot 2): @Vy keeps talking, closing his fingers over it.
- 6–7s (Shot 2): @Vy goes on, her hand lingering on his.
- 7–8s (Shot 2): @Vy keeps speaking softly.
- 8–9s (Shot 2): @Vy finishes and closes her mouth, letting go.
- 9–10s (Shot 2): @Khai looks up and speaks slowly, worried.
- 10–11s (CUT to Shot 3): @Khai keeps speaking gently.
- 11–12s (Shot 3): @Khai finishes and closes his mouth.
- 12–13s (Shot 3): @Vy only shakes her head with a small smile and turns away down the stairwell.
- 13–14s (Shot 3): @Khai stands in the doorway holding the little phone, mouth closed, as her footsteps fade.
- 14–15s (Shot 3): @Khai looks down at the phone in his hand, then back at the empty stairwell. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, puzzled, thoughtful): "Vy... Cái tên nghe quen lắm. Hình như đã có ai đó hay gọi tên này."
- Turn 2, 4.9–9.9s, spoken on camera by @Vy (woman of 30, low clipped quiet alto, guarded and precise, speaking at a natural, even conversational pace, pressing the phone into his hand): "Anh giữ lấy nhé. Trong này là đoạn ghi âm của chính anh. Anh đã tự kể lại mọi thứ."
- Turn 3, 10.4–13.5s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, worried, gentle): "Tôi đã kể những gì? Tôi có làm gì sai không?"
- Pacing: @Khai speaks at an even everyday pace, then @Vy answers at an even everyday pace, then @Khai answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning birds, a small phone pressed into a palm, distant street sounds, footsteps fading down the stairwell. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 1 (`canh-20/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The small shared courtyard of the old collective housing block in bright morning sun: potted bonsai and chili plants, a low plastic table with plastic stools, a water tap, morning sun on the potted plants, laundry drying on a line.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaTu = Bà Tư, 68, the gentle landlady of the old collective housing block; small and slightly stooped, a deeply lined kind face, cloudy warm eyes, silver hair in a low bun, a worn thin translucent patch with a faint violet light on the back of her neck; loose brown cotton blouse with cloth buttons, black silky trousers, plastic sandals.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm wide shot of the old woman hurrying across the sunny courtyard waving the old photo, handheld.
- Shot 2, 5–9s: 50mm medium shot of the young man stepping out of his doorway, locked off.
- Shot 3, 9–15s: 85mm close-up of the old woman's joyful tearful face, the back of her neck now bare, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaTu hurries across the sunny courtyard waving her old photo and is already speaking fast and breathlessly.
- 1–2s (Shot 1): @BaTu keeps talking quickly, her face lit up.
- 2–3s (Shot 1): @BaTu goes on, pressing the photo to her heart.
- 3–4s (Shot 1): @BaTu keeps speaking fast, almost laughing.
- 4–5s (Shot 1): @BaTu finishes and closes her mouth, panting.
- 5–6s (CUT to Shot 2): @Khai steps out of his doorway and answers, amazed, breaking into a smile.
- 6–7s (Shot 2): @Khai keeps talking, reaching out to steady her.
- 7–8s (Shot 2): @Khai finishes and closes his mouth.
- 8–9s (Shot 2): @BaTu answers slowly, crying with joy, touching the bare skin at the back of her neck.
- 9–10s (CUT to Shot 3): @BaTu keeps speaking, tears on her cheeks.
- 10–11s (Shot 3): @BaTu goes on, smiling through them.
- 11–12s (Shot 3): @BaTu keeps speaking, her voice soft.
- 12–13s (Shot 3): @BaTu finishes and closes her mouth.
- 13–14s (Shot 3): @Khai laughs silently and takes both her hands.
- 14–15s (Shot 3): The two stand in the bright courtyard holding hands, the photo between them. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.3s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking quickly in short lively phrases, every word still clear, breathless, overjoyed): "Khải ơi! Bà nhớ ra rồi! Hạnh là con gái bà! Nó đi làm ở Đà Nẵng, sáu năm nay rồi!"
- Turn 2, 5.8–8.1s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, amazed, breaking into a smile): "Bà nhớ ra thật rồi ạ? Thật không bà?"
- Turn 3, 8.6–13.6s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking slowly and softly, unhurried, with a short natural pause between phrases, crying with joy): "Bà bỏ cái miếng dán đi rồi. Sáng nay tỉnh dậy, bà nhớ ra giọng nó."
- Pacing: @BaTu speaks quickly, then @Khai answers at an even everyday pace, then @BaTu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: plastic sandals slapping quickly on concrete, morning birds, a radio from a balcony, laundry flapping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 2 (`canh-20/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
The small shared courtyard of the old collective housing block in bright morning sun: potted bonsai and chili plants, a low plastic table with plastic stools, a water tap, morning sun on the potted plants, laundry drying on a line.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaTu = Bà Tư, 68, the gentle landlady of the old collective housing block; small and slightly stooped, a deeply lined kind face, cloudy warm eyes, silver hair in a low bun, a worn thin translucent patch with a faint violet light on the back of her neck; loose brown cotton blouse with cloth buttons, black silky trousers, plastic sandals.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 85mm close-up of the old woman asking, locked off.
- Shot 2, 6–10s: 40mm medium shot of the young man handing over his translucent phone, handheld.
- Shot 3, 10–15s: 100mm extreme close-up of the old woman's wrinkled finger pressing the glowing number keys one by one, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaTu is already speaking urgently and happily, holding out her hand.
- 1–2s (Shot 1): @BaTu keeps talking, wiggling her fingers for the phone.
- 2–3s (Shot 1): @BaTu goes on, laughing at herself.
- 3–4s (Shot 1): @BaTu keeps speaking, holding up six fingers.
- 4–5s (Shot 1): @BaTu goes on, her eyes bright.
- 5–6s (Shot 1): @BaTu finishes and closes her mouth.
- 6–7s (CUT to Shot 2): @Khai answers fast, pulling his translucent phone from his pocket.
- 7–8s (Shot 2): @Khai keeps talking quickly, unlocking it and handing it over.
- 8–9s (Shot 2): @Khai finishes and closes his mouth.
- 9–10s (Shot 2): @BaTu answers slowly and proudly, pressing the number keys one at a time.
- 10–11s (CUT to Shot 3): @BaTu keeps speaking, her wrinkled finger finding each key without hesitation.
- 11–12s (Shot 3): @BaTu goes on, nodding with each press.
- 12–13s (Shot 3): @BaTu finishes and closes her mouth, lifting the phone to her ear.
- 13–14s (Shot 3): @BaTu waits, holding her breath, as a ringing tone begins.
- 14–15s (Shot 3): @Khai watches her with a wide smile, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.3s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking at a natural, even conversational pace, urgent, happy): "Con cho bà mượn điện thoại. Bà phải gọi cho con bé ngay. Sáu năm bà chưa gọi nó lần nào."
- Turn 2, 6.8–10.0s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, pulling out his phone): "Đây ạ, bà cứ gọi đi. Số của chị Hạnh bà có còn nhớ không?"
- Turn 3, 10.5–13.6s, spoken on camera by @BaTu (old woman of 68, soft creaky gentle voice, a little breathless, speaking slowly and softly, unhurried, with a short natural pause between phrases, dialling slowly, proud): "Nhớ chứ. Bà nhớ hết. Không sót một số nào."
- Pacing: @BaTu speaks at an even everyday pace, then @Khai answers quickly, then @BaTu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone unlocking, the soft beeps of a number being dialled one digit at a time, morning birds, a ringing tone starting. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 3 (`canh-20/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, early morning, pale sunlight through the barred window and a small mirror above a basin by the door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Linh = Linh, 17, Khải's younger sister in her final year of high school; small and slim, a round bright face, long black hair in a high ponytail, sharp lively eyes; white short-sleeved school shirt, navy pleated skirt, white canvas sneakers.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium shot of the schoolgirl at the door with her backpack, locked off.
- Shot 2, 5–10s: 85mm close-up of the young man by the sunny barred window, handheld.
- Shot 3, 10–15s: 50mm medium two-shot across the room as the schoolgirl taps her head and leaves, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Linh stands at the door in her school uniform with her backpack and is already speaking brightly.
- 1–2s (Shot 1): @Linh keeps talking, giving a determined fist pump.
- 2–3s (Shot 1): @Linh goes on, pointing at him.
- 3–4s (Shot 1): @Linh finishes and closes her mouth, grinning.
- 4–5s (Shot 1): @Khai, standing by the sunny barred window, answers fast and teasingly.
- 5–6s (CUT to Shot 2): @Khai keeps talking quickly, waving her off.
- 6–7s (Shot 2): @Khai goes on, tapping his own head.
- 7–8s (Shot 2): @Khai keeps speaking, a warm smile spreading.
- 8–9s (Shot 2): @Khai finishes and closes his mouth.
- 9–10s (Shot 2): @Linh answers slowly with a grin, tapping her own head twice.
- 10–11s (CUT to Shot 3): @Linh keeps speaking, opening the door.
- 11–12s (Shot 3): @Linh finishes and closes her mouth.
- 12–13s (Shot 3): @Linh waves and slips out; the door clicks shut behind her.
- 13–14s (Shot 3): @Khai stays by the window, smiling at the closed door, mouth closed.
- 14–15s (Shot 3): Sunlight streams through the bars onto the freshly whitewashed wall. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking at a natural, even conversational pace, bright, determined): "Anh, em đi học đây. Hôm nay em sẽ làm bài thật tốt, anh cứ chờ mà xem."
- Turn 2, 5.4–9.2s, spoken on camera by @Khai (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking quickly in short lively phrases, every word still clear, teasing, warm): "Ừ, đi đi. Học giỏi vào, sau này đừng có để ai thuê cái đầu của mình nhé."
- Turn 3, 9.7–12.5s, spoken on camera by @Linh (girl of 17, bright quick clear voice, sharp and teasing, speaking slowly and softly, unhurried, with a short natural pause between phrases, grinning, tapping her head): "Vâng ạ. Cái đầu của em, em tự dùng hết."
- Pacing: @Linh speaks at an even everyday pace, then @Khai answers quickly, then @Linh answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning birds, a school bag zipper, the door latch, footsteps on the stairwell, the electric fan. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 4 (`canh-20/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action near-future science-fiction drama set in Hanoi in 2041, where the city looks almost like today — narrow alleys, tangled power cables, peeling yellow collective housing blocks, street food stalls — with quiet touches of the future: slim translucent phones, small violet holograms, silent electric scooters; natural skin texture, subtle 35mm film grain, shallow depth of field, intimate handheld camera.

[LIGHTING]
Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.

[LOCATION]
A cramped rented room in an old Hanoi collective housing block in 2041: peeling pale-green walls, a narrow bed pushed against a plain white plaster wall, a small wooden sleeping loft with a curtain above the desk, a study desk piled with exam books under a window with iron bars, a standing electric fan, a bare hanging bulb, early morning, pale sunlight through the barred window and a small mirror above a basin by the door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 27, a broke delivery rider in Hanoi in 2041; lean wiry build, sun-browned skin, slightly long messy black hair falling over his forehead, a thin face with tired but warm dark eyes and a quick apologetic grin; a faded grey T-shirt and dark blue cotton shorts, barefoot.
- Wardrobe: in this shot @Khai wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the young man at the sunny barred window looking out over the rooftops, locked off.
- Shot 2, 5–10s: 85mm close-up of the young man's face in the sunlight, slow push-in.
- Shot 3, 10–15s: 35mm wide shot from behind him of the window and the morning rooftops of Hanoi, slow pull-back.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai stands at the sunny barred window looking out over the rooftops and is already speaking slowly and quietly to himself.
- 1–2s (Shot 1): @Khai keeps talking softly, resting his forehead against the bars.
- 2–3s (Shot 1): @Khai goes on, his eyes on the city.
- 3–4s (Shot 1): @Khai keeps speaking in a hush.
- 4–5s (Shot 1): @Khai finishes and closes his mouth.
- 5–6s (CUT to Shot 2): @Khai lifts his head and speaks at an even pace, wondering.
- 6–7s (Shot 2): @Khai keeps talking, a faint frown between his brows.
- 7–8s (Shot 2): @Khai goes on, tapping one finger gently against the window bar like a slow beat.
- 8–9s (Shot 2): @Khai keeps speaking softly.
- 9–10s (Shot 2): @Khai finishes and closes his mouth.
- 10–11s (CUT to Shot 3): @Khai speaks slowly with a soft, peaceful smile.
- 11–12s (Shot 3): @Khai keeps speaking, his eyes half closed in the sun.
- 12–13s (Shot 3): @Khai finishes and closes his mouth.
- 13–14s (Shot 3): @Khai reaches up and touches the bare skin at the back of his neck where the patch used to be.
- 14–15s (Shot 3): @Khai stands smiling at the window as the morning light spills over the rooftops of Hanoi. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, spoken on camera by @Khai alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–4.3s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, to himself): "Lạ thật. Mình không nhớ gì về bảy ngày qua. Không nhớ gì cả."
- Part 2, 4.8–10.1s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking at a natural, even conversational pace, wondering): "Nhưng có một bài hát cứ ở lại trong đầu mình. Một bài hát ru, bằng thứ tiếng mình không hiểu."
- Part 3, 10.6–14.3s (man of 27, warm slightly husky baritone, an easygoing Hanoi street voice that turns tight and quiet when scared, speaking slowly and softly, unhurried, with a short natural pause between phrases, a soft, peaceful smile): "Chắc là của một người nào đó... gửi lại cho mình giữ hộ."
- Pacing: @Khai speaks slowly and calmly, then @Khai continues at an even everyday pace, then @Khai continues slowly and calmly; the change of speed is clearly audible.
- Throughout, @Khai's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning birds, the city waking up below, a soft breeze through the window bars, the electric fan slowing to a stop. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```
