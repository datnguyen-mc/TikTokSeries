# Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít — Bộ 90 Prompt Google Flow Omni (15 Cảnh × 6 Clips × 10s)

- **Giọng Người Dẫn Chuyện (cố định cả 90 clip):** Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; đọc nhanh liên thanh như oan-thai-doi-me, ~4.0 âm tiết/giây, liền một hơi, không ngắt giữa câu.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 90 clips × 10s — 67 clip VO + 23 clip thoại; lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 33 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 56 clip ảnh nhân vật (Ingredients), 1 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** clip VO được tăng tốc giọng thêm 1.18x khi tải về (`FLOWKIT_VOICE_TEMPO` mặc định 1.18, đặt 1.0 để tắt), giữ nguyên khung hình 10s; clip lip-sync không bao giờ bị tăng tốc để khớp khẩu hình.
- **Màu phim & ánh sáng:** Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py can-nha-am-duong` sinh lại toàn bộ clip, README, kịch bản.

---

## Cảnh 01 - Clip 1 (`canh-01/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Night, heavy rain: dark fog-shrouded rice paddies and a lonely rural highway; a sleeper coach crawls along it, its rain-streaked windows dimly lit.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm stabilized aerial drone slow descending push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Wide aerial view above dark misty Northern Vietnamese rice fields as a lone coach bus rolls along the highway.
- 3.0–7.0s: High-angle aerial camera gliding over dark, fog-shrouded Northern Vietnamese rice paddies at midnight and descending toward the rain-streaked window of a lone sleeper coach bus where @Binh sits huddled.
- 7.0–10.0s: Camera pushes in close to the rain-streaked sleeper bus window revealing @Binh huddled inside. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Ôm món nợ hơn bốn trăm triệu đồng không lối thoát, Bình đành bỏ trốn trong đêm về căn nhà hoang của ông nội." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: coach engine droning low through the night rain, wind whistling across the open fields. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 2 (`canh-01/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Night, heavy rain. Inside a dim sleeper coach crawling along a misty Northern Vietnamese rural highway; amber highway lights sweep across the rain-streaked window seat.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal slow creeping push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Interior view by the rain-streaked bus window where @Binh hugs his black backpack.
- 3.0–7.0s: Inside the dimly lit sleeper bus cabin, @Binh clutches his black backpack tightly against his chest as passing amber highway streetlights sweep across his pale, hollow-eyed face.
- 7.0–10.0s: @Binh stares blankly at his pale reflection in the wet glass as his jacket pocket begins to vibrate. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Nhưng Bình đâu hề biết sau vụ tai nạn cướp đi sáu mạng người, căn nhà ấy đã thành nơi trú ngụ của ma quỷ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steady swish of the coach's wipers, heavy uneasy breathing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 3 (`canh-01/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Night, heavy rain. Inside a dim sleeper coach crawling along a misty Northern Vietnamese rural highway; amber highway lights sweep across the rain-streaked window seat.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized medium close-up shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh pulls his buzzing smartphone from his hoodie pocket by the dark bus window.
- 3.0–7.0s: @Binh flinches, answers the call and speaks in a low, shaking voice, his breath shallow, the phone at his ear and his face turned toward the camera so his lips stay clearly visible.
- 7.0–10.0s: @Binh keeps the phone pressed to his ear, eyes darting nervously toward the dark aisle. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.4s, spoken on camera by @Binh (young man of 21, standard Hà Nội accent, light tenor, shaky and breathless with fear, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Con nghe đây mẹ ơi, con đang ngồi trên xe khách về quê nội rồi, mẹ đừng gọi nhiều nhỡ người ta nghe thấy." (no subtitles)
- @Binh's face and lips stay clearly visible while speaking; after the last word @Binh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: phone buzzing against the seat cushion, low rumble of the coach in the dark cabin. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 4 (`canh-01/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Night. A small, dim city apartment kitchen: worn wooden table, weak yellow bulb, old electric fan.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaPhuong = Bà Phượng, Bình's mother, 50; gentle worried oval face, black hair with grey streaks in a low bun; plain blue blouse, dark trousers.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized medium close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Medium close-up of @BaPhuong standing at a worn wooden kitchen table under a weak yellow bulb, phone pressed to her ear.
- 3.0–7.0s: @BaPhuong grips the edge of the table, tears brimming, and warns her son in an urgent voice, her face toward the camera.
- 7.0–10.0s: Tears roll down @BaPhuong's cheeks as she clutches the table edge, the phone still at her ear. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.7s, spoken on camera by @BaPhuong (woman of 50, standard Hà Nội accent, warm mezzo voice, tearful and worried, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Bố mày vẫn chưa biết chuyện đâu, nhưng đám chủ nợ sắp tìm tới nhà rồi, mày về quê nội phải thật cẩn thận nhé!" (no subtitles)
- @BaPhuong's face and lips stay clearly visible while speaking; after the last word @BaPhuong closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: an old electric fan rattling as it turns, the mother's choked breathing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 5 (`canh-01/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Night, heavy rain. Inside a dim sleeper coach crawling along a misty Northern Vietnamese rural highway; amber highway lights sweep across the rain-streaked window seat.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized over-the-shoulder tilt-down push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Back inside the dark bus cabin as @Binh lowers his glowing smartphone screen.
- 3.0–7.0s: Back in his dark sleeper bus seat, @Binh lowers the smartphone and stares at a screenshot of his liquidated online trading account glowing red, burying his face in his shaking hands.
- 7.0–10.0s: @Binh buries his forehead in both trembling hands beside the rain-streaked window. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Tất cả bi kịch bắt nguồn từ cái bẫy tiền ảo trên mạng, chỉ sau một đêm mất trắng mà nợ lãi chồng chất." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: flat beep of the call ending, bitter remorseful breathing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 6 (`canh-01/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Night, heavy rain. Inside a dim sleeper coach crawling along a misty Northern Vietnamese rural highway; amber highway lights sweep across the rain-streaked window seat.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow dolly pull-back; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh locks his phone screen and rests his forehead against the cold bus window.
- 3.0–7.0s: @Binh switches off his phone screen and leans his forehead against the freezing wet bus glass, watching his hollow reflection as the coach plunges deeper into rural night fog.
- 7.0–10.0s: The sleeper coach bus disappears into dense white rural highway fog in the night. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Không còn mặt mũi nào nhìn bố, Bình đánh liều trốn về quê mà chẳng ngờ mình đang tự bước chân vào cõi âm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: coach tyres hissing through rain puddles, hollow night wind. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 1 (`canh-02/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Afternoon in a small Northern Vietnamese provincial town and its village: a dusty bus stop, a roadside rice stall, a narrow concrete lane between rice paddies and old bamboo groves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm stabilized gimbal tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh steps off the coach bus onto the dusty provincial roadside wearing his black backpack.
- 3.0–7.0s: Under pale late-afternoon sun at a dusty provincial bus stop, the coach pulls away and @Binh steps onto the gravel shoulder with his black backpack, letting out a long, exhausted breath.
- 7.0–10.0s: @Binh adjusts his backpack straps and looks toward a humble roadside rice stall. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Hơn hai giờ chiều chiếc xe khách thả Bình xuống bến thị xã nhỏ, giữa nơi đất khách cậu mới dám thở phào." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: coach horn fading away down the highway, afternoon wind blowing grit underfoot. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 2 (`canh-02/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Afternoon in a small Northern Vietnamese provincial town and its village: a dusty bus stop, a roadside rice stall, a narrow concrete lane between rice paddies and old bamboo groves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized medium close-up push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh sits hunched at a low plastic table looking down at his smartphone beside a rice plate.
- 3.0–7.0s: @Binh sits alone at a low plastic table in a roadside eatery, staring down at a text message showing his mother just transferred her last five hundred thousand dong beside a plate of cold rice.
- 7.0–10.0s: @Binh swallows hard with reddened eyes, unable to touch the cold rice before him. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Ngồi bên quán cơm bụi nhìn tin nhắn mẹ chuyển năm trăm nghìn cuối cùng, sống mũi Bình bỗng nhiên cay xè." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft message chime on the phone, a spoon clinking on a china plate. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 3 (`canh-02/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Afternoon in a small Northern Vietnamese provincial town and its village: a dusty bus stop, a roadside rice stall, a narrow concrete lane between rice paddies and old bamboo groves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal slow tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh puts his phone away and stands up from the roadside plastic table.
- 3.0–7.0s: @Binh slips the phone into his hoodie pocket, stares briefly at his trembling thin hands, then rises with his backpack to walk down the narrow concrete road leading into his grandfather's village.
- 7.0–10.0s: @Binh walks onto the narrow concrete village road bordered by quiet fields. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Cậu tự nhủ sẽ ẩn náu ở quê nội ít ngày, nhưng khi hỏi thăm đường về nhà cụ Xá thì ai cũng biến sắc." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a plastic stool scraping on concrete, lone footsteps. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 4 (`canh-02/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Afternoon in a small Northern Vietnamese provincial town and its village: a dusty bus stop, a roadside rice stall, a narrow concrete lane between rice paddies and old bamboo groves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm stabilized gimbal following shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh walks down the narrow concrete path beneath overhanging dark bamboo stalks.
- 3.0–7.0s: @Binh walks alone along the narrow concrete lane between two darkening afternoon rice paddies as cold wind bends the overarching old bamboo groves with a hollow, eerie creak.
- 7.0–10.0s: @Binh slows his pace as he spots an elderly farmer ahead near the village entrance. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Con đường bê tông dẫn về thôn cứ hẹp dần giữa cánh đồng chiều vắng lặng, rợp bóng tre già âm u lạnh lẽo." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: old bamboo stalks creaking against each other in the cold evening wind. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 5 (`canh-02/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Afternoon in a small Northern Vietnamese provincial town and its village: a dusty bus stop, a roadside rice stall, a narrow concrete lane between rice paddies and old bamboo groves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized two-shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh stops on the concrete lane as @OngBay walks toward him, pushing an old black bicycle.
- 3.0–7.0s: @OngBay stops beside @Binh, looks him over warily, then speaks and points down the lane toward a towering jackfruit tree at the far edge of the village, his face toward the camera.
- 7.0–10.0s: @OngBay points his calloused hand down the lane toward the dark canopy at the village edge. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–7.2s, spoken on camera by @OngBay (village man of 60, Northern accent, warm rustic baritone, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Căn nhà cuối xóm có gốc mít cổ thụ ấy bỏ hoang hai mươi năm nay rồi cậu ơi, nhà ấy nặng âm khí có ma đấy!" (no subtitles)
- @OngBay's face and lips stay clearly visible while speaking; after the last word @OngBay closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind rustling the rice paddies, a bicycle chain ticking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 6 (`canh-02/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Dusk: the rusted black iron gate under an ancient twisted jackfruit tree at the end of the village lane; an overgrown yard and a dark three-bay tiled house behind it.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal slow creeping push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh approaches the rusted black iron gate beneath the massive ancient jackfruit tree.
- 3.0–7.0s: Following the pointed path, @Binh halts before a peeling, rusted black iron gate; inside the weed-choked yard, a gnarled ancient jackfruit tree looms over the dark three-bay tiled house.
- 7.0–10.0s: @Binh grips the cold rusted iron bars looking into the overgrown, shadowed courtyard. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Đứng trước cánh cổng sắt rỉ sét và gốc mít cổ thụ vặn vẹo, một luồng khí lạnh thổi ra làm Bình rùng mình." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: dry jackfruit leaves rustling at dusk, rusted gate hinges groaning softly. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 1 (`canh-03/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Dusk: the rusted iron gate under the ancient jackfruit tree and the quiet village lane.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh holds the rusted iron gate bars as @OngBay brakes his old black bicycle right behind him.
- 3.0–7.0s: @OngBay recognizes the young man from the afternoon and calls out to him with suspicion from his bicycle, his face toward the camera, while @Binh still grips the gate bars.
- 7.0–10.0s: @Binh spins around, breath catching and shoulders jerking up, to face @OngBay's stern gaze. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.9s, spoken on camera by @OngBay (village man of 60, Northern accent, warm rustic baritone, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Ơ cậu hỏi đường lúc chiều đây mà, trời tối rồi sao còn đứng lấp ló trước cổng nhà ấy thế hả?!" (no subtitles)
- @OngBay's face and lips stay clearly visible while speaking; after the last word @OngBay closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: bicycle brakes squealing on concrete, crickets starting up. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 2 (`canh-03/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Dusk: the rusted iron gate under the ancient jackfruit tree and the quiet village lane.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized two-shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh steps back from the gate and bows his head respectfully toward @OngBay.
- 3.0–7.0s: @Binh explains who he is, his face toward the camera; hearing the name of his late neighbour's grandson, @OngBay's stern face softens.
- 7.0–10.0s: @OngBay smiles warmly and pats @Binh's shoulder. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.9s, spoken on camera by @Binh (young man of 21, standard Hà Nội accent, light tenor, shaky and breathless with fear, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Dạ cháu không phải kẻ gian đâu bác ơi, cháu là Bình cháu nội cụ Xá, con trai bố Quân trên phố về thăm nhà ạ!" (no subtitles)
- @Binh's face and lips stay clearly visible while speaking; after the last word @Binh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a relieved exhale, a warm pat on the hoodie shoulder. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 3 (`canh-03/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Dusk: the rusted iron gate under the ancient jackfruit tree and the quiet village lane.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm stabilized gimbal side-tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngBay wheels his bicycle alongside @Binh away from the dark jackfruit gate.
- 3.0–7.0s: @OngBay walks his bicycle side by side with @Binh away from the rusted iron gate toward his own modest three-bay tiled house at the head of the lane as dusk settles.
- 7.0–10.0s: Both walk toward the warm yellow porch light of @OngBay's house down the lane. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Nhận ra đứa cháu nội của ông cụ hàng xóm quá cố, ông Bảy mừng rỡ dẫn Bình về nhà mình nghỉ tạm qua đêm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: bicycle freewheel ticking steadily, evening insects chirring. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 4 (`canh-03/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Night: Ông Bảy's warm-lit tiled porch with a wooden tea table, looking out through fog toward the dark road bend and the black jackfruit tree by Cụ Xá's gate.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
- Extra: @OngBay's wife: a thin village woman about 58 in a faded floral blouse, hair in a bun (unnamed, no reference image).
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh sits drinking hot tea at a wooden table on @OngBay's warm-lit porch.
- 3.0–7.0s: While @Binh sips his tea, @OngBay's wife beckons her husband to the corner pillar and whispers urgently; @OngBay listens with a troubled frown.
- 7.0–10.0s: @OngBay's expression darkens with worry as he glances out toward the dark village road. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Thế nhưng vừa nghe chồng bảo ngày mai cho Bình sang nhà hoang ở, vợ ông Bảy đã tái mặt kéo chồng ra góc hiên." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a china cup set down on a wooden tray, an anxious wordless whisper from the porch corner. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 5 (`canh-03/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Night: Ông Bảy's warm-lit tiled porch with a wooden tea table, looking out through fog toward the dark road bend and the black jackfruit tree by Cụ Xá's gate.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized over-the-shoulder push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Over @OngBay's shoulder looking out from the porch into the fog-shrouded highway curve.
- 3.0–7.0s: From his porch, @OngBay stares out through the thickening night fog toward the sharp highway curve right in front of Cụ Xá's rusted gate and the looming black jackfruit tree.
- 7.0–10.0s: In the distance, the dark silhouette of the ancient jackfruit tree looms over the empty curve. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Bà nhắc rằng mười ba năm trước đúng ba giờ sáng, chiếc xe rước dâu lật nhào trước cổng làm sáu người chết thảm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: cold night wind hissing through bamboo, a faint distant echo like tyres screeching. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 6 (`canh-03/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Night, ground fog: the gnarled roots of the ancient jackfruit tree outside Cụ Xá's rusted gate.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @VongLa = the wandering ghost of the jackfruit tree: tall gaunt figure, ash-grey damp skin, tangled wet black hair over half the face, long thin fingers, tattered dark wet clothes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow creeping push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Creeping view through white night mist toward the gnarled roots of the ancient jackfruit tree.
- 3.0–7.0s: The camera pushes slowly through the ground fog beneath the gnarled ancient jackfruit tree outside the rusted iron gate, where the tall, skeletal silhouette of @VongLa stands staring into the abandoned house.
- 7.0–10.0s: @VongLa's tall, ash-grey figure stands half-hidden behind the weeds staring through the iron gate. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Những oan hồn chết oan khuất không tìm được đường về đã kéo cả vào căn nhà bỏ không ấy trú ngụ suốt bao năm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: jackfruit leaves falling on wet grass, a deep hollow sigh from the old tree. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 1 (`canh-04/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Bright morning: the overgrown mossy brick courtyard under the ancient jackfruit tree and the rusted iron gate.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm stabilized gimbal tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh walks along the sunlit morning lane carrying a bamboo broom toward the iron gate.
- 3.0–7.0s: Morning sunlight burns away the night mist under the jackfruit tree as @Binh walks up to the rusted iron gate carrying a bamboo broom while roosters crow across the village.
- 7.0–10.0s: @Binh stops before the rusted padlock on the black iron gate under the jackfruit tree. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Ánh nắng ban mai trong trẻo xua tan màn sương đêm, làm những lời đồn thổi ma quỷ tối hôm qua tạm thời lắng xuống." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: roosters crowing across the village, sparrows chirping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 2 (`canh-04/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Bright morning: the overgrown mossy brick courtyard under the ancient jackfruit tree and the rusted iron gate.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium close-up shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngBay inserts his hoe handle into the rusted padlock while @Binh holds the gate bar.
- 3.0–7.0s: At the iron gate, @OngBay wedges the wooden handle of his iron hoe into the rusted padlock beside @Binh and wrenches downward, snapping the 20-year-old lock open with a sharp metallic crack.
- 7.0–10.0s: The broken padlock drops onto the mossy bricks and the iron gate swings open. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Sáng hôm ấy ông Bảy dùng cán cuốc bẩy gãy tung chiếc ổ khóa sắt rỉ, mở toang cánh cổng khóa suốt hai mươi năm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the rusted padlock snapping with a sharp crack, the heavy iron gate creaking open. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 3 (`canh-04/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Bright morning: the overgrown mossy brick courtyard under the ancient jackfruit tree and the rusted iron gate.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm stabilized gimbal panning shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh sweeps piles of dry jackfruit leaves across the mossy brick courtyard.
- 3.0–7.0s: Inside the open gate, @Binh sweeps away thick layers of rotting brown jackfruit leaves, weeds, and cobwebs across the mossy brick courtyard beneath the sprawling tree canopy.
- 7.0–10.0s: @Binh wipes sweat from his forehead and looks toward the dark open doorway of the main house. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Suốt ba tiếng đồng hồ phát cỏ dại và quét mạng nhện, khoảng sân gạch rêu phong dưới gốc mít cổ thụ mới lộ ra." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a bamboo broom sweeping dry leaves across old bricks. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 4 (`canh-04/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Late morning: the dusty, empty three-bay main room with peeling plaster and no ancestral altar; sunbeams through gaps in the roof tiles.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh steps over the wooden threshold into the dusty, empty three-bay main room.
- 3.0–7.0s: @Binh steps across the wooden threshold into the bare, peeling-plaster main room; slanted afternoon sunbeams cut through roof tile gaps illuminating thick dust motes where no ancestral altar stands.
- 7.0–10.0s: @Binh stands alone in the center of the bare room looking at the empty altar wall. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Bước qua ngưỡng cửa vào gian nhà chính trống huơ không một nén hương sưởi ấm, lòng Bình chợt chùng xuống lạnh lẽo." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: footsteps echoing in the empty room, wind through gaps in the old roof tiles. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 5 (`canh-04/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Bright morning: the overgrown mossy brick courtyard under the ancient jackfruit tree and the rusted iron gate.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaPhuong = Bà Phượng, Bình's mother, 50; gentle worried oval face, black hair with grey streaks in a low bun; plain blue blouse, dark trousers.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized tight close-up push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Tight close-up of @BaPhuong in a dim city room pressing her phone to her tear-stained cheek.
- 3.0–7.0s: A shrill ringtone shatters the silence; on the other end in the city, @BaPhuong cowers in a dark room corner clutching her phone with both hands, sobbing in sheer panic.
- 7.0–10.0s: @BaPhuong's voice cuts off abruptly as she lowers the phone in terror. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.4s, spoken on camera by @BaPhuong (woman of 50, standard Hà Nội accent, warm mezzo voice, tearful and worried, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Bình ơi! Bố mày đã biết hết chuyện nợ nần rồi con ơi, ông ấy đang điên tiết lùng tìm mày khắp nơi đấy!" (no subtitles)
- @BaPhuong's face and lips stay clearly visible while speaking; after the last word @BaPhuong closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: panicked breathing, a faint crash of things breaking in another room. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 6 (`canh-04/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Late morning: the dusty, empty three-bay main room with peeling plaster and no ancestral altar; sunbeams through gaps in the roof tiles.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow crane-down pull-back; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh stands frozen in the bare main room as the phone call disconnects.
- 3.0–7.0s: Hearing the line go dead, @Binh lowers his phone with a lifeless arm, slides his back down the peeling damp lime wall onto the cold brick floor, and buries his head in his knees.
- 7.0–10.0s: @Binh slumps onto the cold brick floor against the peeling wall holding his head. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Cuộc gọi tắt phụt cắt đứt tia hy vọng cuối cùng, Bình ngồi gục xuống nền gạch lạnh ngắt giữa căn nhà ma." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone knocking on the brick floor, a despairing sigh in the empty house. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 1 (`canh-05/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
First night: the dim main room of the abandoned house, a creaking folding cot inside a thin white mosquito net under a weak yellow filament bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh lies curled on the folding cot inside the thin white mosquito net under dim yellow light.
- 3.0–7.0s: On his first night alone under the dim, sickly yellow glow of a 15W filament bulb, @Binh lies curled on a creaking folding cot inside a thin white mosquito net, pulling his blanket tight.
- 7.0–10.0s: @Binh closes his tired eyes beneath the mosquito net as the room shadows deepen. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Đêm đầu tiên ngủ lại một mình dưới ánh đèn dây tóc vàng vọt, Bình kéo chăn ngang ngực cố tự trấn an mình." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: frogs croaking in the night paddies, the folding cot creaking softly. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 2 (`canh-05/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
First night: the dim main room of the abandoned house, a creaking folding cot inside a thin white mosquito net under a weak yellow filament bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongLa = the wandering ghost of the jackfruit tree: tall gaunt figure, ash-grey damp skin, tangled wet black hair over half the face, long thin fingers, tattered dark wet clothes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized high-angle slow crane-down shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: High angle descending toward the white mosquito net in the dimly lit room.
- 3.0–7.0s: The camera lowers slowly from the dark ceiling beams toward the white mosquito net where @Binh dozes; the shadows thicken, and the tall gaunt figure of @VongLa circles silently right outside the net.
- 7.0–10.0s: @VongLa's tall dark silhouette pauses right beside the thin mosquito net above @Binh. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Khi cơn mê man vừa kéo đến, ngay sát bên ngoài lớp màn mỏng bỗng có bóng người cao gầy lặng lẽ đi quanh giường!" (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wet bare footsteps gliding on the brick floor, the mosquito net trembling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 3 (`canh-05/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
First night: the dim main room of the abandoned house, a creaking folding cot inside a thin white mosquito net under a weak yellow filament bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongLa = the wandering ghost of the jackfruit tree: tall gaunt figure, ash-grey damp skin, tangled wet black hair over half the face, long thin fingers, tattered dark wet clothes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized close-up shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close framing inside the mosquito net: @Binh lies rigid as a long ash-grey hand hovers just above his left wrist.
- 3.0–7.0s: Frost creeps across @Binh's skin under @VongLa's hovering grey hand; his eyes fly open, his body frozen in sleep paralysis, and he cries out in terror, his face toward the camera.
- 7.0–10.0s: @Binh strains his neck, gasping, unable to move, as the grey hand slowly withdraws into the dark. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.4s, spoken on camera by @Binh (young man of 21, standard Hà Nội accent, light tenor, shaky and breathless with fear, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Ai đó?! Bỏ ngay cái bàn tay lạnh buốt ấy ra khỏi người tôi, cứu tôi với, có ai ngoài đó bỏ tôi ra!!" (no subtitles)
- @Binh's face and lips stay clearly visible while speaking; after the last word @Binh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the folding cot rattling, an icy hiss of frost, faint ghostly breathing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 4 (`canh-05/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Early morning: the same main room, sunbeams slanting through the wooden window bars onto the folding cot.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium close-up push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Morning sunlight hits the mosquito net as @Binh bolts upright on the folding cot.
- 3.0–7.0s: Morning sunbeams slant through the wooden window bars across the folding cot; @Binh bolts upright drenched in cold sweat and freezes as he looks down at a dark purple five-finger bruise on his left wrist.
- 7.0–10.0s: @Binh stares in horror at the dark five-finger bruise encircling his pale left wrist. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Giật mình choàng tỉnh khi trời vừa hửng sáng, Bình chết lặng nhìn vết bầm tím đen năm ngón tay hằn sâu trên cổ tay!" (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ragged waking gasps, early-morning birds outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 5 (`canh-05/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Early morning: the main room doorway and the sunlit front porch, the iron gate under the jackfruit tree beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngBay stands at the open iron gate in the morning sun and calls toward the house.
- 3.0–7.0s: @OngBay calls out warmly, his face toward the camera, as @Binh hurries out of the wooden doorway onto the sunlit porch, lifting his left wrist to look at it.
- 7.0–10.0s: @Binh stops on the porch steps staring at his now-unmarked wrist while @OngBay waves from the gate. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.4s, spoken on camera by @OngBay (village man of 60, Northern accent, warm rustic baritone, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Bình ơi dậy chưa cháu? Mau ra rửa mặt mũi đi rồi sang bên nhà bác ăn bát cháo nóng cho ấm bụng nào!" (no subtitles)
- @OngBay's face and lips stay clearly visible while speaking; after the last word @OngBay closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the wooden door opening onto the morning sun, birdsong. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 6 (`canh-05/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Early morning: the main room doorway and the sunlit front porch, the iron gate under the jackfruit tree beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongLa = the wandering ghost of the jackfruit tree: tall gaunt figure, ash-grey damp skin, tangled wet black hair over half the face, long thin fingers, tattered dark wet clothes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow dolly pull-back into interior; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh stands on the sunlit porch turning his clean left wrist over in disbelief.
- 3.0–7.0s: @Binh stands on the bright porch rubbing his now-clean left wrist in confusion, while the camera pulls slowly backward into the dark room corner behind him where @VongLa watches before fading away.
- 7.0–10.0s: Inside the shadowed doorway behind @Binh, @VongLa's dark silhouette lingers then dissolves. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Bước ra nắng sớm vết bầm bỗng biến mất sạch trơn, nhưng trong góc tối sau lưng cậu cái bóng đen vẫn lặng lẽ dõi theo." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a cold draft in the dark corner against bright morning birdsong outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 1 (`canh-06/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Late afternoon: a lush green rice-paddy embankment in the village.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm stabilized gimbal side-tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh and @OngBay walk side by side along a sunlit green rice field embankment.
- 3.0–7.0s: Under peaceful late-afternoon sunshine, @Binh walks alongside @OngBay down a lush green rice paddy embankment, his pale face relaxing slightly in the quiet rural breeze.
- 7.0–10.0s: Both pause to look across the peaceful golden-green rice paddies toward the village. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Hai ngày tiếp theo trôi qua êm ả, ban ngày Bình đi theo ông Bảy ra thăm đồng cho vơi bớt nỗi ám ảnh." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: green rice rustling in the afternoon breeze, soft footsteps on the earthen path. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 2 (`canh-06/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Dusk: Ông Bảy's tiled porch with a wooden table and tea cups.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium two-shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh and @OngBay sit at the wooden porch table sharing steaming cups of green tea.
- 3.0–7.0s: Back on @OngBay's tiled porch at dusk, @Binh sits at the wooden table lifting a steaming cup of green tea with @OngBay, a faint relieved smile touching his lips.
- 7.0–10.0s: @Binh takes a quiet sip of tea as evening twilight begins to settle over the yard. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Ngồi uống chén nước chè xanh nóng hổi nơi hiên nhà hàng xóm, Bình thoáng nghĩ hay là cứ ở lại quê nghèo mãi mãi." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: hot tea poured into china cups, birds returning to roost. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 3 (`canh-06/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Night: Ông Bảy's porch table under a yellow bulb, looking down the dark lane toward the jackfruit tree.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Under the yellow porch light at night, @OngBay leans across the table toward @Binh.
- 3.0–7.0s: Over small cups of rice wine, @OngBay leans in close to @Binh and points with a trembling finger toward the dark jackfruit tree down the lane.
- 7.0–10.0s: @OngBay points out into the dark lane toward the ancient jackfruit tree silhouette. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Nhưng rồi tối hôm ấy bên bàn rượu quê, ông Bảy hạ giọng ghé sát tai kể chuyện ông Tư gặp ma dưới gốc mít." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: small wine cups set on the table, crickets in the village night. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 4 (`canh-06/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Flashback, foggy night: the gnarled roots of the ancient jackfruit tree outside the rusted gate.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @VongLa = the wandering ghost of the jackfruit tree: tall gaunt figure, ash-grey damp skin, tangled wet black hair over half the face, long thin fingers, tattered dark wet clothes.
- Extra: Ông Tư: an old villager seen only as a hand holding a lit lighter in the foreground (unnamed, face never shown).
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Foggy night at the gnarled base of the ancient jackfruit tree; an old man's hand flicks a lighter in the foreground.
- 3.0–7.0s: In the small orange flame, @VongLa, crouched among the roots, slowly lifts an ash-grey face with two pitch-black, eyeless sockets.
- 7.0–10.0s: @VongLa's ash-grey face with hollow black eye sockets hangs in the flickering lighter glow. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Đêm đó ông Tư đi về khuya bật lửa mời thuốc, hiện ra trước mặt ông là khuôn mặt trắng bệch không có con ngươi!" (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a lighter flicking in the night fog, icy wind through the jackfruit canopy. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 5 (`canh-06/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Flashback, foggy night: the gnarled roots of the ancient jackfruit tree outside the rusted gate.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @VongLa = the wandering ghost of the jackfruit tree: tall gaunt figure, ash-grey damp skin, tangled wet black hair over half the face, long thin fingers, tattered dark wet clothes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow dolly pull-back; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @VongLa crouches against the gnarled jackfruit trunk grinning in the cold mist.
- 3.0–7.0s: @VongLa stretches a wide, silent grin and melts backward into the rough bark of the ancient jackfruit trunk, leaving a crumpled cigarette pack resting alone on the wet mossy roots.
- 7.0–10.0s: @VongLa dissolves into the dark tree bark, leaving only the cigarette pack on the wet roots. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Thứ tà ma đó nhoẻn miệng cười lạnh lẽo rồi tan biến vào thân cây, để lại bao thuốc lá trên đám rễ mít lạnh." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a cold echoing giggle that dies away, jackfruit leaves falling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 6 (`canh-06/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Late night: the dark village lane, the rusted iron gate and the ancient jackfruit tree.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal following shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh walks alone down the dark lane and steps through the rusted iron gate.
- 3.0–7.0s: Late that night, @Binh walks alone through the rusted iron gate right past that very jackfruit tree, his eyes darting anxiously up at the pitch-black canopy rustling overhead.
- 7.0–10.0s: @Binh hurries across the dark courtyard glancing fearfully back at the looming jackfruit tree. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Đêm khuya một mình bước qua đúng gốc mít cổ thụ ấy để về nhà, sống lưng Bình lạnh toát như ai chà nước đá." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: hurried footsteps through the iron gate, jackfruit branches creaking overhead. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 1 (`canh-07/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Third night, deep night: the dark kitchen and main room of the abandoned house, folding cot with mosquito net, a barred wooden window facing the jackfruit yard, a single filament bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium close-up push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh lies asleep under the mosquito net in the dark room.
- 3.0–7.0s: On the third night inside the dark house, @Binh is half-asleep on his folding cot when an ear-splitting metallic crash echoes from the adjoining kitchen, jolting him wide awake.
- 7.0–10.0s: @Binh jerks upright on the cot staring toward the pitch-black kitchen doorway. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Đêm thứ ba khi Bình vừa mới chợp mắt trên giường xếp, từ dưới gian bếp tối bỗng vang lên tiếng xoong rơi chói tai!" (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: an aluminium pot crashing on the brick floor and echoing through the dead-quiet night. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 2 (`canh-07/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Third night, deep night: the dark kitchen and main room of the abandoned house, folding cot with mosquito net, a barred wooden window facing the jackfruit yard, a single filament bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized tracking tilt-down shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh enters the dark kitchen aiming his smartphone flashlight beam at the floor.
- 3.0–7.0s: @Binh steps cautiously into the dark kitchen shining his smartphone flashlight onto the brick floor: an aluminum saucepan that hung on a high wall nail now lies spinning on the tiles as he crouches.
- 7.0–10.0s: @Binh crouches with trembling fingers to pick up the fallen aluminum saucepan. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.4s, spoken on camera by @Binh (young man of 21, standard Hà Nội accent, light tenor, shaky and breathless with fear, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Chắc chỉ là con chuột thôi mà, chỉ là con chuột chạy qua làm rơi cái xoong nhôm từ trên đinh xuống đất thôi." (no subtitles)
- @Binh's face and lips stay clearly visible while speaking; after the last word @Binh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the aluminium pot spinning on the bricks before it settles. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 3 (`canh-07/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Third night, deep night: the dark kitchen and main room of the abandoned house, folding cot with mosquito net, a barred wooden window facing the jackfruit yard, a single filament bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongLa = the wandering ghost of the jackfruit tree: tall gaunt figure, ash-grey damp skin, tangled wet black hair over half the face, long thin fingers, tattered dark wet clothes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh reaches up to hang the aluminium pot back on the kitchen wall nail.
- 3.0–7.0s: As @Binh hangs the pot, the overhead filament bulb sparks and goes pitch black; in the cold blue darkness the pale figure of @VongLa stands right behind him.
- 7.0–10.0s: In the cold blue darkness @VongLa stands inches behind @Binh's back. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Nhưng ngay khi tay cậu vừa chạm vào chiếc đinh trên tường, bóng đèn dây tóc bỗng nổ lách tách rồi tắt phụt tối đen!" (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the filament bulb popping with a sharp crackle, then dead silence. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 4 (`canh-07/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Third night, deep night: the dark kitchen and main room of the abandoned house, folding cot with mosquito net, a barred wooden window facing the jackfruit yard, a single filament bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongLa = the wandering ghost of the jackfruit tree: tall gaunt figure, ash-grey damp skin, tangled wet black hair over half the face, long thin fingers, tattered dark wet clothes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized tight over-the-shoulder close-up; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Tight close-up on the back of @Binh's neck as icy white breath mist touches his skin.
- 3.0–7.0s: In the freezing blue-black darkness, a plume of icy white breath from @VongLa drifts against the back of @Binh's neck and his hair stands on end, then the bulb flickers back on.
- 7.0–10.0s: The yellow bulb flickers on and @Binh gasps, alone again in the kitchen. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Giữa bóng tối đặc quánh như mực, một luồng hơi thở lạnh buốt như băng phả thẳng vào sau gáy khiến Bình cứng đờ!" (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a raspy icy breath right at the neck, the bulb buzzing back on. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 5 (`canh-07/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Third night, deep night: the dark kitchen and main room of the abandoned house, folding cot with mosquito net, a barred wooden window facing the jackfruit yard, a single filament bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongLa = the wandering ghost of the jackfruit tree: tall gaunt figure, ash-grey damp skin, tangled wet black hair over half the face, long thin fingers, tattered dark wet clothes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized quick panning push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh slams the saucepan onto the wooden shelf and glances toward the barred window.
- 3.0–7.0s: With the light back on, @Binh sets the pan hastily on the wooden shelf, but as he glances toward the barred wooden window beside him, @VongLa's legless white figure glides right past the bars.
- 7.0–10.0s: Outside the wooden window bars, @VongLa's pale white silhouette glides past into the dark. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Ánh đèn vừa nhấp nháy sáng lại, Bình liếc nhanh qua khung cửa sổ gỗ thì thấy một bóng trắng lướt vụt qua chấn song!" (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a pot set hastily on a wooden shelf, a cold whoosh past the window bars. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 6 (`canh-07/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Third night, deep night: the dark kitchen and main room of the abandoned house, folding cot with mosquito net, a barred wooden window facing the jackfruit yard, a single filament bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongLa = the wandering ghost of the jackfruit tree: tall gaunt figure, ash-grey damp skin, tangled wet black hair over half the face, long thin fingers, tattered dark wet clothes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow dolly pull-back toward window; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh dives onto the folding cot pulling the blanket over his head.
- 3.0–7.0s: @Binh scrambles back onto his folding cot and pulls the blanket completely over his head, while the camera pulls back toward the barred wooden window where @VongLa's five black-nailed fingers grip the sill.
- 7.0–10.0s: At the wooden window sill in the foreground, five ash-grey black-nailed fingers grip the wood. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Bình phóng vội lên giường trùm kín chăn, không hề biết ngoài cửa sổ năm móng tay đen dài đang bấu chặt mép gỗ!" (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a blanket thrown over, fingernails scraping softly on the wooden sill, a faint giggle. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 1 (`canh-08/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Fourth night, deep night: the moonlit main room, twisted jackfruit-branch shadows on the walls, folding cot with a thin white mosquito net.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm stabilized gimbal slow creeping push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Wide view of the moonlit room: twisted jackfruit-branch shadows crawl across the walls.
- 3.0–7.0s: Deep in the fourth night, cold blue moonlight pierces the ancient jackfruit tree outside and casts claw-like branch shadows through the barred window onto @Binh's mosquito-netted cot.
- 7.0–10.0s: The camera creeps closer to the thin white mosquito net where @Binh sleeps. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Đêm thứ tư kinh hoàng nhất đã tới, ánh trăng lạnh xuyên qua tán mít hắt bóng cành cây vặn vẹo như quỷ dữ lên vách." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: night wind hissing through the jackfruit canopy, branches scraping the roof tiles. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 2 (`canh-08/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Fourth night, deep night: the moonlit main room, twisted jackfruit-branch shadows on the walls, folding cot with a thin white mosquito net.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close view through the white mosquito net onto @Binh's sleeping face.
- 3.0–7.0s: Pushing close to the thin white mosquito net in the dim light, @Binh suddenly snaps his dark-circled eyes open, paralyzed by the sensation of unseen eyes staring down at him from inches away.
- 7.0–10.0s: @Binh's eyes snap wide open staring straight up through the top of the net. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Đúng hai giờ bốn mươi lăm phút sáng, Bình bỗng mở choàng mắt tỉnh giấc vì cảm giác có kẻ đang nhìn sát mặt mình." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a pounding heartbeat, a breath caught in the throat. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 3 (`canh-08/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Fourth night, deep night: the moonlit main room, twisted jackfruit-branch shadows on the walls, folding cot with a thin white mosquito net.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongLa = the wandering ghost of the jackfruit tree: tall gaunt figure, ash-grey damp skin, tangled wet black hair over half the face, long thin fingers, tattered dark wet clothes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized low-angle shot from beside @Binh's pillow, looking up through the net; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Low angle from beside @Binh's face on the pillow, looking up through the white net mesh at a tall dark figure beside the cot.
- 3.0–7.0s: @Binh, lying on his back with his face in the foreground toward the camera, stammers in terror, while beyond the translucent net the tall contorted silhouette of @VongLa looms at the cot edge, bowing its head to stare at him.
- 7.0–10.0s: @VongLa leans its shadowed head closer against the outside of the thin white net above @Binh. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.2s, spoken on camera by @Binh (young man of 21, standard Hà Nội accent, light tenor, shaky and breathless with fear, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Ai đó?! Kẻ nào đang đứng lù lù ngay sát bên ngoài tấm màn tuyn trắng của tôi lúc nửa đêm thế kia?!" (no subtitles)
- @Binh's face and lips stay clearly visible while speaking; after the last word @Binh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: dead-still cold room tone, a faint creak of the cot. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 4 (`canh-08/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Fourth night, deep night: the moonlit main room, twisted jackfruit-branch shadows on the walls, folding cot with a thin white mosquito net.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongLa = the wandering ghost of the jackfruit tree: tall gaunt figure, ash-grey damp skin, tangled wet black hair over half the face, long thin fingers, tattered dark wet clothes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized macro close-up push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close framing on the taut white mosquito net beside @Binh's chest.
- 3.0–7.0s: @VongLa stands silent outside the net; slowly, a shrivelled ash-grey hand with five long black fingernails slides through a gap in the mesh toward @Binh.
- 7.0–10.0s: @VongLa's ash-grey hand with long black nails hovers inside the net just above @Binh. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Đáp lại cậu chỉ là sự im lặng chết chóc, rồi một bàn tay xác chết xám ngoét với năm móng đen thò xuyên qua màn!" (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a very soft rustle of the mosquito net as the hand slides through. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 5 (`canh-08/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Fourth night, deep night: the moonlit main room, twisted jackfruit-branch shadows on the walls, folding cot with a thin white mosquito net.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongLa = the wandering ghost of the jackfruit tree: tall gaunt figure, ash-grey damp skin, tangled wet black hair over half the face, long thin fingers, tattered dark wet clothes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized tight close-up shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @VongLa's grey hand hovers just above @Binh's left wrist on the mattress.
- 3.0–7.0s: @VongLa's hollow-eyed pale face presses close to the outside of the net, lips visible through the mesh, and speaks in a cold whisper while @Binh lies frozen with wide eyes.
- 7.0–10.0s: @VongLa's pale hollow-eyed face stays pressed against the net, inches from @Binh's wide, unblinking eyes. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.8s, spoken on camera by @VongLa (cold breathy whisper, Northern accent, echoing as if from every direction, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Đi đi, mày hãy cút khỏi căn nhà này ngay lập tức, nơi đây không phải chỗ cho người sống chúng mày ở đâu!" (no subtitles)
- @VongLa's face and lips stay clearly visible while speaking; after the last word @VongLa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the net fabric shivering, a cold draft. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 6 (`canh-08/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Fourth night, deep night: the moonlit main room, twisted jackfruit-branch shadows on the walls, folding cot with a thin white mosquito net.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium close-up push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh bolts upright inside the mosquito net, gasping and clutching his left arm.
- 3.0–7.0s: The grey hand is gone; @Binh lifts his trembling left arm and sees the dark purple five-finger bruise now deep in his skin, not fading.
- 7.0–10.0s: Close view of @Binh's left wrist marked with a deep black-purple five-finger bruise. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Bình choàng tỉnh dậy đẫm mồ hôi lạnh, vết bầm năm ngón tay trên cổ tay nay đã tím đen như máu tụ không tan nữa!" (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a horrified gasp, the cot creaking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 1 (`canh-09/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Grey early morning: the mossy brick courtyard, stone porch steps and the old house under the overcast jackfruit canopy.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh runs out of the house into the morning courtyard toward @OngBay.
- 3.0–7.0s: At dawn the next morning, @Binh rushes out into the brick courtyard pale as a sheet, rolls up his grey hoodie sleeve, and thrusts the dark five-finger bruise right in front of @OngBay.
- 7.0–10.0s: @Binh holds out his bruised left wrist with trembling hands before @OngBay's face. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.9s, spoken on camera by @Binh (young man of 21, standard Hà Nội accent, light tenor, shaky and breathless with fear, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Bác Bảy ơi cứu cháu với! Đêm hôm qua có bàn tay người chết thò xuyên qua màn bóp chặt lấy cổ tay cháu đây này!" (no subtitles)
- @Binh's face and lips stay clearly visible while speaking; after the last word @Binh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: panicked running footsteps on the brick courtyard. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 2 (`canh-09/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Grey early morning: the mossy brick courtyard, stone porch steps and the old house under the overcast jackfruit canopy.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized two-shot push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngBay holds @Binh's forearm gently, examining the dark purple finger marks.
- 3.0–7.0s: @OngBay knits his silver brows and inspects the unmistakable five-finger bruise in the morning light, then speaks low and grave, his face toward the camera.
- 7.0–10.0s: @OngBay picks up his wooden stick and turns gravely toward the house porch. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.9s, spoken on camera by @OngBay (village man of 60, Northern accent, warm rustic baritone, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Lạy hồn, vết bầm năm ngón tay rõ mồn một thế này thì không phải chuyện đùa rồi, để bác vào kiểm tra quanh nhà xem!" (no subtitles)
- @OngBay's face and lips stay clearly visible while speaking; after the last word @OngBay closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a startled sigh, morning wind rustling the jackfruit canopy. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 3 (`canh-09/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Grey early morning: the mossy brick courtyard, stone porch steps and the old house under the overcast jackfruit canopy.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm stabilized gimbal following shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngBay walks along the house windows with @Binh, testing the wooden bars with his stick.
- 3.0–7.0s: @OngBay walks along the veranda and interior of the three-bay house with @Binh, checking every wooden window bar and door bolt — all remain tightly latched and covered in undisturbed thick dust.
- 7.0–10.0s: Inside, the wooden window bolts remain locked tight beneath undisturbed grey dust. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Ông Bảy cầm gậy đi kiểm tra khắp các chốt cửa gỗ và chấn song cửa sổ, tuyệt nhiên không có dấu vết người lạ cạy cửa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a wooden stick tapping window bars and ironwood door bolts. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 4 (`canh-09/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Grey early morning: the mossy brick courtyard, stone porch steps and the old house under the overcast jackfruit canopy.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium two-shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngBay steps back into the courtyard with @Binh and glances up at the jackfruit canopy.
- 3.0–7.0s: @OngBay stops in the brick courtyard, glances warily up at the dark jackfruit tree canopy, then pats @Binh's shoulder with an evasive, sympathetic look to keep the boy from panicking further.
- 7.0–10.0s: @OngBay pats @Binh's shoulder with a troubled, pitying gaze before turning toward the gate. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Sợ thằng nhỏ thêm hoảng loạn, ông Bảy đành gượng bảo do cậu nằm mê nhưng ánh mắt trốn tránh của ông không giấu nổi." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: jackfruit leaves dropping on the bricks, an old neighbour's uneasy sigh. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 5 (`canh-09/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Grey early morning: the mossy brick courtyard, stone porch steps and the old house under the overcast jackfruit canopy.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized medium close-up push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh sits hunched on the mossy porch steps holding his smartphone to his ear.
- 3.0–7.0s: Once the old neighbour has gone, @Binh sits alone on the mossy stone porch step pressing his phone to his ear to call his mother, his voice cracking with fear and utter helplessness.
- 7.0–10.0s: A tear slips down @Binh's pale cheek as he listens to the quiet phone line. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–7.2s, spoken on camera by @Binh (young man of 21, standard Hà Nội accent, light tenor, shaky and breathless with fear, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Mẹ ơi căn nhà của ông nội ở dưới quê thật sự có thứ gì đáng sợ lắm, nhưng giờ con biết trốn đi đâu hả mẹ!" (no subtitles)
- @Binh's face and lips stay clearly visible while speaking; after the last word @Binh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a quiet empty porch, a distant rooster. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 6 (`canh-09/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Grey early morning: the mossy brick courtyard, stone porch steps and the old house under the overcast jackfruit canopy.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow dolly push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh lowers the smartphone onto his lap on the mossy stone porch step.
- 3.0–7.0s: @Binh lowers his phone, hugs his knees on the cold stone step, and turns his head to stare deep into the shadowed interior of the main hall, his fear hardening into desperate resolve.
- 7.0–10.0s: @Binh turns his head to stare straight into the dark open doorway of the main room. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Quay về phố thì chủ nợ chờ sẵn mà ở lại thì ma quỷ vây quanh, bước đường cùng biến nỗi sợ thành sự liều lĩnh." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: cold wind breathing out of the dark house onto the porch. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 1 (`canh-10/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Fifth night, deep night: the freezing moonlit main room where the old family altar once stood; bare lime-plaster walls.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh sits awake on the floor against the peeling lime wall hugging his knees in the dark.
- 3.0–7.0s: As the fifth night falls over the main hall, @Binh leaves the mosquito net untied and sits with his back braced against the cold lime wall, hugging his knees and staring wide-eyed into the dark.
- 7.0–10.0s: @Binh's dark-circled eyes remain fixed unblinkingly on the empty shadowed altar corner. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Đêm thứ năm Bình quyết định không ngủ, cậu ngồi tựa lưng vào bức tường vôi lạnh nhìn thẳng bóng tối chờ gặp người âm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a clock ticking very softly, night wind whistling through the door gaps. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 2 (`canh-10/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Fifth night, deep night: the freezing moonlit main room where the old family altar once stood; bare lime-plaster walls.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongCuXa = the ghost of Cụ Xá, Bình's late grandfather, about 80; gaunt, wispy white hair and beard, sad hollow eyes; faded brown traditional áo bà ba, barefoot; semi-transparent with a faint cold glow.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow creeping push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh shivers against the wall as his breath turns into visible white vapour.
- 3.0–7.0s: The room turns freezing; @Binh's breath plumes white as, in the dark corner where the ancestral altar once stood, the translucent figure of @VongCuXa slowly takes form.
- 7.0–10.0s: In the dark corner opposite him, the semi-transparent figure of @VongCuXa stands fully formed. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Đúng một giờ sáng nhiệt độ tụt xuống lạnh cóng, hơi thở Bình phả ra khói trắng khi từ góc gian thờ cũ bóng già hiện lên." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: air freezing with a faint crackle, a hoarse old man's cough from the dark corner. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 3 (`canh-10/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Fifth night, deep night: the freezing moonlit main room where the old family altar once stood; bare lime-plaster walls.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongCuXa = the ghost of Cụ Xá, Bình's late grandfather, about 80; gaunt, wispy white hair and beard, sad hollow eyes; faded brown traditional áo bà ba, barefoot; semi-transparent with a faint cold glow.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized medium close-up push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @VongCuXa turns his translucent, white-bearded face into the slant of silver moonlight.
- 3.0–7.0s: Dressed in a faded brown áo bà ba tunic, @VongCuXa turns slowly under the cold moonlight slanting through the window; @Binh gasps in shock as he recognizes the gentle, gaunt face of his late grandfather.
- 7.0–10.0s: @Binh's eyes widen with emotion as @VongCuXa extends a frail, glowing hand toward him. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–7.0s, spoken on camera by @VongCuXa (very old man, Northern accent, soft hoarse voice with a faint echo, low and steady, without long pauses), in Vietnamese with exact lip-sync, said exactly once: "Bình đấy ư, đứa cháu nội đích tôn của ông đấy ư, con đừng sợ ông, hãy lại đây ngồi gần với ông nào con." (no subtitles)
- @VongCuXa's face and lips stay clearly visible while speaking; after the last word @VongCuXa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: deep cold room tone with a faint echo. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 4 (`canh-10/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Fifth night, deep night: the freezing moonlit main room where the old family altar once stood; bare lime-plaster walls.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongCuXa = the ghost of Cụ Xá, Bình's late grandfather, about 80; gaunt, wispy white hair and beard, sad hollow eyes; faded brown traditional áo bà ba, barefoot; semi-transparent with a faint cold glow.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized close-up shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close framing on @VongCuXa looking at the bare wall where his altar once stood.
- 3.0–7.0s: @VongCuXa gazes sadly at the bare, incense-less plaster wall with hollow eyes, his hoarse Northern voice echoing softly through the empty ancestral room.
- 7.0–10.0s: @VongCuXa looks back down at @Binh with sorrowful, loving eyes. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–7.6s, spoken on camera by @VongCuXa (very old man, Northern accent, soft hoarse voice with a faint echo, low and steady, without long pauses), in Vietnamese with exact lip-sync, said exactly once: "Ngày ông mất đi, bố mày làm đám xong liền rước bát hương lên phố nhưng quên lễ rước vong, để hồn ông bơ vơ lạnh lẽo." (no subtitles)
- @VongCuXa's face and lips stay clearly visible while speaking; after the last word @VongCuXa closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: bare-room hush, faint wind under the door. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 5 (`canh-10/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Fifth night, deep night: the freezing moonlit main room where the old family altar once stood; bare lime-plaster walls.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongCuXa = the ghost of Cụ Xá, Bình's late grandfather, about 80; gaunt, wispy white hair and beard, sad hollow eyes; faded brown traditional áo bà ba, barefoot; semi-transparent with a faint cold glow.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh crawls forward on the brick floor and kneels at @VongCuXa's feet.
- 3.0–7.0s: @Binh crawls across the cold brick tiles and falls to his knees before @VongCuXa's translucent form, tears streaming down his face in overwhelming grief and remorse.
- 7.0–10.0s: @Binh bows his head weeping as @VongCuXa gazes down at him with gentle compassion. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–7.2s, spoken on camera by @Binh (young man of 21, standard Hà Nội accent, light tenor, shaky and breathless with fear, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Ông nội ơi cháu có lỗi với ông nhiều lắm, cháu và bố ở trên thành phố thật sự không biết ông phải lạnh lẽo thế này!" (no subtitles)
- @Binh's face and lips stay clearly visible while speaking; after the last word @Binh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: knees knocking on the brick floor, cold room tone. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 6 (`canh-10/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Fifth night, deep night: the freezing moonlit main room where the old family altar once stood; bare lime-plaster walls.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @VongCuXa = the ghost of Cụ Xá, Bình's late grandfather, about 80; gaunt, wispy white hair and beard, sad hollow eyes; faded brown traditional áo bà ba, barefoot; semi-transparent with a faint cold glow.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow dolly pull-back; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @VongCuXa rests a translucent hand above @Binh's bowed head in the moonlit room.
- 3.0–7.0s: @VongCuXa explains he had sent the spirit under the jackfruit tree only because he feared @Binh came to sell the ancestral land, then fades into the blue moonlight leaving @Binh kneeling in vow.
- 7.0–10.0s: @VongCuXa dissolves into soft silver moonlight, leaving @Binh kneeling resolutely on the floor. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Vong hồn cụ Xá bảo chính cụ đã sai vong gốc mít vào dọa cháu, rồi dặn Bình phải gọi bố về quê chuộc lỗi tổ tiên." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: night wind calming, a soft shimmering tone as the grandfather fades into moonlight. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 1 (`canh-11/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Dawn, pale early light: the mossy stone porch steps of the ancestral house.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh sits on the stone porch steps at dawn holding his smartphone.
- 3.0–7.0s: At dawn after his tearful encounter with his grandfather's spirit, @Binh steps out onto the pale sunlit porch steps, takes a deep steadying breath, and dials his father's phone number.
- 7.0–10.0s: @Binh raises the phone to his ear with a calm, determined expression. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Trắng đêm suy nghĩ sau cuộc gặp gỡ đẫm nước mắt với ông nội, vừa rạng sáng Bình đã lấy hết can đảm bấm gọi cho bố." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: early birds singing in the garden, phone keypad taps. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 2 (`canh-11/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Early morning. A bright city apartment room by a window.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized medium close-up shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Medium close-up of @OngQuan by a city window gripping his phone in blazing anger.
- 3.0–7.0s: In a bright city room by a window, @OngQuan stands flushed with fury, clenching his fist as he roars into the smartphone pressed against his ear.
- 7.0–10.0s: @OngQuan glares out the window breathing heavily as he listens to his son's reply. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.7s, spoken on camera by @OngQuan (man of 55, standard Hà Nội accent, deep stern gravelly baritone, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Thằng nghịch tử kia! Mày phá gia chi tử nợ bốn trăm triệu rồi còn dám lôi vong hồn ông nội ra lừa bố hả?!" (no subtitles)
- @OngQuan's face and lips stay clearly visible while speaking; after the last word @OngQuan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: city apartment room tone, distant traffic. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 3 (`canh-11/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Morning: the mossy stone porch steps and brick courtyard of the ancestral house.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized close-up push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh kneels upright on the stone porch steps clutching the phone to his ear.
- 3.0–7.0s: Out on the rural porch steps, @Binh drops straight to his knees on the brick tiles with tears rolling down his cheeks, speaking into the phone with unwavering sincerity.
- 7.0–10.0s: Tears stream down @Binh's face as the phone line clicks dead. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–7.2s, spoken on camera by @Binh (young man of 21, standard Hà Nội accent, light tenor, shaky and breathless with fear, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Bố về đánh gãy chân con cũng được, nhưng con van xin bố hãy về quê thắp hương xin lỗi ông nội một lần đi bố ơi!" (no subtitles)
- @Binh's face and lips stay clearly visible while speaking; after the last word @Binh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: knees on the porch bricks, morning birds. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 4 (`canh-11/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Morning: the mossy stone porch steps and brick courtyard of the ancestral house.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow pull-back; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh lowers the disconnected smartphone into his lap on the porch steps.
- 3.0–7.0s: The phone line disconnects abruptly; @Binh lowers the handset into his lap and remains seated quietly on the mossy stone porch steps, keeping his eyes fixed on the rusted iron gate under the jackfruit tree.
- 7.0–10.0s: @Binh sits motionless on the porch looking straight out toward the rusted iron gate. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Tiếng điện thoại cúp máy cái rập, Bình vẫn ngồi bất động nơi bậc thềm hiên nhà, sẵn sàng chịu đòn chờ người cha trở về." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: afternoon wind rustling jackfruit leaves across the quiet courtyard. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 5 (`canh-11/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Late afternoon, low golden sun: the brick courtyard, the porch steps and the rusted iron gate under the jackfruit tree.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @BaPhuong = Bà Phượng, Bình's mother, 50; gentle worried oval face, black hair with grey streaks in a low bun; plain blue blouse, dark trousers.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm stabilized gimbal tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngQuan pushes open the rusted iron gate and strides into the courtyard with @BaPhuong behind him.
- 3.0–7.0s: As late afternoon sun slants through the jackfruit tree, the iron gate swings wide open: @OngQuan strides furiously across the brick courtyard toward @Binh, followed closely by @BaPhuong, hands clasped tight at her chest.
- 7.0–10.0s: @OngQuan marches straight up to @Binh standing before the porch steps. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Quả nhiên ngay chiều hôm ấy ông Quân cùng bà Phượng đã về tới cổng, đôi mắt người cha long lên giận dữ khi thấy con trai." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the iron gate thrown open with a clang, hurried footsteps on the bricks. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 6 (`canh-11/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Late afternoon, low golden sun: the brick courtyard, the porch steps and the rusted iron gate under the jackfruit tree.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @BaPhuong = Bà Phượng, Bình's mother, 50; gentle worried oval face, black hair with grey streaks in a low bun; plain blue blouse, dark trousers.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium three-shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngQuan stands over @Binh in the courtyard with his right hand raised high in fury as @BaPhuong rushes in.
- 3.0–7.0s: @OngQuan's raised hand trembles in the air and stops; @BaPhuong steps between father and son, weeping; @Binh kneels on the bricks and pleads up at his father, his face toward the camera.
- 7.0–10.0s: @Binh bows his forehead to the bricks before @OngQuan, who slowly lowers his hand, jaw clenched. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.9s, spoken on camera by @Binh (young man of 21, standard Hà Nội accent, light tenor, shaky and breathless with fear, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Con xin chịu hết mọi hình phạt của bố mẹ, nhưng con cầu xin bố tối nay hãy ngủ lại căn nhà này một đêm thôi!" (no subtitles)
- @Binh's face and lips stay clearly visible while speaking; after the last word @Binh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the father's heavy furious breathing, the mother's sobs, wind in the jackfruit leaves. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 1 (`canh-12/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Night: the dark main room of the ancestral house with a wooden bed in the centre and a small side table; moonlight through wooden shutters.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @BaPhuong = Bà Phượng, Bình's mother, 50; gentle worried oval face, black hair with grey streaks in a low bun; plain blue blouse, dark trousers.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngQuan lies on the wooden bed in the dim main room while @BaPhuong and @Binh sit nearby.
- 3.0–7.0s: Night falls over the ancestral house: @OngQuan lies stern-faced on a wooden bed placed in the center of the dark main room, while @BaPhuong and @Binh sit quietly awake at a side table.
- 7.0–10.0s: @OngQuan closes his stern eyes as cold moonlight filters through the wooden shutters. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Đêm hôm ấy ông Quân nhất quyết nằm ngay tại gian phòng khách cũ, tuyên bố đanh thép sáng mai sẽ áp giải con về phố." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: night insects in the garden, heavy breathing in the dark house. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 2 (`canh-12/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Night: the dark main room of the ancestral house with a wooden bed in the centre and a small side table; moonlight through wooden shutters.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @VongCuXa = the ghost of Cụ Xá, Bình's late grandfather, about 80; gaunt, wispy white hair and beard, sad hollow eyes; faded brown traditional áo bà ba, barefoot; semi-transparent with a faint cold glow.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close framing on @OngQuan's sleeping face as @VongCuXa's translucent form stands by the headboard.
- 3.0–7.0s: Under cold silver moonlight, the camera pushes close to @OngQuan's sleeping face: his brows knit in deep anguish and hot tears stream from his closed eyes as @VongCuXa stands silently beside the bed.
- 7.0–10.0s: Tears roll down @OngQuan's weathered cheeks in the moonlight as @VongCuXa gazes down at him. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Giữa đêm khuya không ai biết ông Quân mơ thấy điều gì, chỉ thấy người đàn ông sắt đá ấy bật khóc trong giấc ngủ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the father's muffled sobs in his sleep, soft night wind. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 3 (`canh-12/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Dawn: white mist over a village rice-field cemetery; Cụ Xá's mossy stone grave in the wet grass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow push-in in morning mist; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngQuan kneels alone in the misty field cemetery before his father's mossy stone grave.
- 3.0–7.0s: At dawn in the white mist of the village rice-field cemetery, a red-eyed @OngQuan kneels alone in the wet grass before Cụ Xá's mossy stone grave, bowing deeply as he plants burning incense.
- 7.0–10.0s: @OngQuan plants burning incense sticks into the censer and bows his forehead to the damp earth. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Khi trời vừa tờ mờ sáng, ông Quân lặng lẽ mua hương hoa ra nghĩa trang đồng làng, một mình quỳ gục hàng giờ trước mộ cha." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: dawn wind over the fields carrying incense smoke, remorseful sobs. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 4 (`canh-12/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Daytime: the main room of the ancestral house as a new carved mahogany altar cabinet is carried in.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm stabilized gimbal tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngQuan and @Binh carry a carved mahogany altar cabinet through the doorway into the main hall.
- 3.0–7.0s: Returning to the ancestral house, @OngQuan rolls up his shirt sleeves and works side by side with @Binh to carry a newly carved mahogany ancestral altar cabinet into the center of the main room.
- 7.0–10.0s: Father and son set the mahogany altar cabinet squarely against the central wall. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Trở về từ nghĩa trang, ông Quân lập tức cùng Bình tự tay khiêng chiếc tủ thờ gỗ gụ mới tinh đặt vào chính giữa gian nhà." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: mahogany cabinet legs set down firmly on the brick floor. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 5 (`canh-12/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Daytime: the main room with the new mahogany altar, Cụ Xá's framed portrait, a bronze incense burner and sandalwood incense.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @BaPhuong = Bà Phượng, Bình's mother, 50; gentle worried oval face, black hair with grey streaks in a low bun; plain blue blouse, dark trousers.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngQuan places the bronze incense burner on the mahogany altar and lights three incense sticks.
- 3.0–7.0s: @OngQuan sets Cụ Xá's portrait on the new altar and kneels before it, @BaPhuong and @Binh kneeling behind him; he turns his tear-streaked face slightly toward the camera as he prays aloud.
- 7.0–10.0s: @OngQuan kneels with clasped hands before the glowing altar, @BaPhuong and @Binh behind him. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.9s, spoken on camera by @OngQuan (man of 55, standard Hà Nội accent, deep stern gravelly baritone, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Bố ơi con bất hiếu quá, bao năm để hồn bố lạnh lẽo nơi quê nhà, hôm nay con xin rước bố về gian thờ tổ!" (no subtitles)
- @OngQuan's face and lips stay clearly visible while speaking; after the last word @OngQuan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a match striking, incense catching. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 6 (`canh-12/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Daytime: under the ancient jackfruit tree by the front gate, a small newly built brick shrine.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal slow pull-back; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngQuan and @Binh stand before the newly built brick shrine beneath the ancient jackfruit tree.
- 3.0–7.0s: Out beneath the ancient jackfruit tree by the front gate, @OngQuan and @Binh finish building a small, solemn brick shrine where fragrant incense smoke curls upward to soothe the wandering spirits.
- 7.0–10.0s: Fragrant incense smoke rises from the small brick shrine up into the green jackfruit leaves. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Ngay dưới gốc mít cổ thụ trước cổng, ông Quân còn cho dựng một ngôi miếu gạch nhỏ và lập đàn cầu siêu cho sáu vong hồn." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a temple bell ringing warmly, incense smoke drifting under the jackfruit tree. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 1 (`canh-13/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
During the forty-nine days of mourning: the warm, incense-filled main hall with the new mahogany altar and the sunlit brick courtyard.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @BaPhuong = Bà Phượng, Bình's mother, 50; gentle worried oval face, black hair with grey streaks in a low bun; plain blue blouse, dark trousers.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm stabilized gimbal panning shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngQuan bows with glowing incense at the mahogany altar while sunlight fills the open doorway.
- 3.0–7.0s: In the peaceful morning light, @OngQuan in a simple white shirt lights fresh incense at the mahogany altar inside, while out on the sunny porch @BaPhuong and @Binh sweep the clean courtyard.
- 7.0–10.0s: Camera pans toward the sunny courtyard where @BaPhuong and @Binh sweep fallen leaves together. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Suốt bốn mươi chín ngày ròng rã, ông Quân xin nghỉ ở lại quê ăn chay hương khói, sưởi ấm ngôi nhà lạnh lẽo hai thập kỷ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a broom sweeping softly in the morning sun. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 2 (`canh-13/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Golden afternoon: the small brick shrine under the ancient jackfruit tree by the gate.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngQuan walks out to the small brick shrine beneath the sunlit jackfruit tree with fresh fruit.
- 3.0–7.0s: In the golden afternoon sunlight beneath the ancient jackfruit tree, @OngQuan reverently places a plate of fresh fruit and lights incense at the small brick shrine, the air now peaceful and warm.
- 7.0–10.0s: @OngQuan clasps his hands respectfully as three incense sticks glow warmly in the shrine. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Ngôi miếu nhỏ dưới gốc mít luôn đỏ đèn nhang mỗi tối, để những vong hồn lỡ bước trên khúc cua năm nào có chốn nương tựa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: green jackfruit leaves rustling in the afternoon sun. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 3 (`canh-13/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
The forty-ninth night: the main worship hall glowing with warm oil-lamp light before the mahogany altar.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium two-shot push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngQuan and @Binh kneel side by side on a woven mat before the warm-lit mahogany altar.
- 3.0–7.0s: On the forty-ninth night inside the main worship hall, @OngQuan and @Binh sit side by side with clasped hands before Cụ Xá's warm oil-lamp altar as fragrant incense smoke curls peacefully upward.
- 7.0–10.0s: Warm amber lantern light bathes their calm faces as incense smoke rises toward the rafters. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Đêm thứ bốn mươi chín, cả căn nhà ngói ba gian tỏa ra luồng sinh khí ấm áp lạ thường, không còn bóng đen lạnh lẽo nữa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the oil lamp burning softly on the altar, calm breathing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 4 (`canh-13/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Night: the view from the jackfruit tree across the brick courtyard to the glowing three-bay house.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm stabilized dolly slow pull-back through gate; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: View from the courtyard looking into the warm golden-lit doorway where @OngQuan and @Binh sit.
- 3.0–7.0s: Seen from outside the jackfruit tree looking across the brick courtyard at night, warm golden light glows through all the wooden windows of the three-bay house where @OngQuan and @Binh talk.
- 7.0–10.0s: Camera pulls back past the jackfruit shrine, framing the glowing three-bay house in the night. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Nhìn từ ngoài cổng vào trong đêm, lần đầu tiên sau hai mươi năm dân làng thấy căn nhà cụ Xá sáng bừng ánh đèn ấm áp." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a village temple bell ringing far away in the peaceful night. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 5 (`canh-13/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
The next morning: the sunlit wooden porch of the ancestral house.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @BaPhuong = Bà Phượng, Bình's mother, 50; gentle worried oval face, black hair with grey streaks in a low bun; plain blue blouse, dark trousers.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium three-shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: On the sunlit wooden porch, @OngQuan places a steady hand on @Binh's shoulder beside @BaPhuong.
- 3.0–7.0s: The next morning on the sunlit porch, @OngQuan rests a forgiving hand on @Binh's shoulder and turns to @BaPhuong with a calm, compassionate expression.
- 7.0–10.0s: @Binh and @BaPhuong nod gratefully as @OngQuan looks warmly at his son. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.4s, spoken on camera by @OngQuan (man of 55, standard Hà Nội accent, deep stern gravelly baritone, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Bà đưa thằng Bình về phố lo trả dần nợ nần trước đi, tôi ở lại sửa sang lại mộ phần cho ông cụ." (no subtitles)
- @OngQuan's face and lips stay clearly visible while speaking; after the last word @OngQuan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning birdsong on the sunlit porch. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 6 (`canh-13/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Morning: Cụ Xá's newly restored stone grave among green rice paddies.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow crane-up shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngQuan stands with clasped hands before his father's clean stone grave in the green field.
- 3.0–7.0s: @OngQuan stands with clasped hands bowing solemnly before Cụ Xá's newly refurbished stone grave surrounded by lush green rice paddies swaying in the morning breeze.
- 7.0–10.0s: Camera cranes gently upward over the sunlit rice paddies surrounding the peaceful grave. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Biến cố tưởng chừng đẩy gia đình xuống vực thẳm ấy lại kéo người cha lầm lỗi trở về cội nguồn, giữ trọn đạo hiếu làm con." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind through green rice fields, peaceful birdsong. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 1 (`canh-14/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Late in the year, cool bright days: the sunlit porch with a wooden table, the clean brick courtyard and the small brick shrine under the jackfruit tree.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh sits at the wooden porch table with an open laptop.
- 3.0–7.0s: On a bright year-end morning, @Binh reads an official notice on his laptop (screen text not readable) that the online scam ring has been caught and his money recovered.
- 7.0–10.0s: @Binh's eyes light up with relief as he looks up from the laptop. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Ở hiền gặp lành, cuối năm ấy công an triệt phá thành công ổ lừa đảo trên mạng và thu hồi phần lớn tiền cho Bình." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: cool year-end wind on the porch, a relieved exhale. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 2 (`canh-14/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Late in the year, cool bright days: the sunlit porch with a wooden table, the clean brick courtyard and the small brick shrine under the jackfruit tree.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized close-up push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh picks up a stamped university readmission letter beside his laptop.
- 3.0–7.0s: @Binh lifts the letter in both hands (text not readable), smiling brightly with gratitude after months of darkness.
- 7.0–10.0s: @Binh holds the letter close with a grateful, radiant smile. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Trả dứt được món nợ đè nặng trên vai, Bình được nhà trường nhận quay lại học năm cuối, mở ra cánh cửa cuộc đời mới." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper rustling in his hands, warm sunny courtyard ambience. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 3 (`canh-14/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Late in the year, cool bright days: the sunlit porch with a wooden table, the clean brick courtyard and the small brick shrine under the jackfruit tree.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @BaPhuong = Bà Phượng, Bình's mother, 50; gentle worried oval face, black hair with grey streaks in a low bun; plain blue blouse, dark trousers.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm stabilized gimbal tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh closes his laptop as @BaPhuong brings a steaming wooden meal tray to the porch table.
- 3.0–7.0s: @Binh closes his laptop as @BaPhuong carries a steaming wooden tray of traditional dishes out onto the porch; @OngQuan, @BaPhuong, and @Binh gather warmly around the family meal.
- 7.0–10.0s: @OngQuan, @BaPhuong, and @Binh sit together around the steaming family meal. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Những ngày cuối năm tiết trời se lạnh, cả gia đình lại quây quần ấm cúng bên mâm cơm đoàn viên nơi hiên nhà ngói quê nội." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: bowls and chopsticks clinking, warm wordless family murmurs. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 4 (`canh-14/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Late in the year, cool bright days: the sunlit porch with a wooden table, the clean brick courtyard and the small brick shrine under the jackfruit tree.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @BaPhuong = Bà Phượng, Bình's mother, 50; gentle worried oval face, black hair with grey streaks in a low bun; plain blue blouse, dark trousers.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized medium close-up shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngQuan pours a small porcelain cup of rice wine at the porch table opposite @Binh.
- 3.0–7.0s: At the family meal table, @OngQuan pours a small cup of clear rice wine and sets it before @Binh, looking at his son with stern yet deeply loving eyes.
- 7.0–10.0s: @Binh bows his head respectfully receiving his father's words while @BaPhuong smiles warmly. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–7.2s, spoken on camera by @OngQuan (man of 55, standard Hà Nội accent, deep stern gravelly baritone, speaking at a brisk, urgent, fast-clipped pace), in Vietnamese with exact lip-sync, said exactly once: "Đời người ai chẳng có lúc lầm đường lạc lối hả con, quan trọng nhất là biết quay đầu và sống trọn chữ hiếu với tổ tiên." (no subtitles)
- @OngQuan's face and lips stay clearly visible while speaking; after the last word @OngQuan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rice wine poured into a small china cup. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 5 (`canh-14/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Late in the year, cool bright days: the sunlit porch with a wooden table, the clean brick courtyard and the small brick shrine under the jackfruit tree.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal following shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh walks across the swept brick courtyard toward the ancient jackfruit tree at the gate.
- 3.0–7.0s: After the afternoon meal, @Binh walks across the clean brick courtyard to the ancient jackfruit tree by the gate and respectfully plants three fragrant burning incense sticks into the small brick shrine.
- 7.0–10.0s: @Binh bows with clasped hands before the small brick shrine as three incense sticks glow. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Buổi chiều muộn, Bình bước ra thắp ba nén nhang thơm nơi miếu gốc mít, thầm cảm ơn biến cố đã giúp gia đình mình tỉnh ngộ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: unhurried footsteps on swept bricks, incense crackling softly. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 6 (`canh-14/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Twilight at year's end: the clean brick courtyard, the small shrine under the jackfruit tree and the warm-lit porch.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @BaPhuong = Bà Phượng, Bình's mother, 50; gentle worried oval face, black hair with grey streaks in a low bun; plain blue blouse, dark trousers.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm stabilized crane-up pull-back; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Binh turns from the jackfruit shrine and walks back across the courtyard toward the porch.
- 3.0–7.0s: From the small shrine beneath the jackfruit tree, the camera cranes slowly upward revealing the clean three-bay tiled house and courtyard where @Binh joins @OngQuan and @BaPhuong on the warm-lit porch.
- 7.0–10.0s: High crane view of @Binh joining @OngQuan and @BaPhuong on the glowing porch under twilight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Ngôi nhà từng bị cả làng gọi là nhà ma đầy khiếp đảm, nay đã thực sự trở thành chốn dương thịnh âm an bình yên." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: calm evening wind through the green jackfruit tree, warm porch ambience. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 1 (`canh-15/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Full-moon night, calm and peaceful: the moonlit courtyard, the glowing brick shrine under the ancient jackfruit tree and the warm-lit ancestral hall.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Moonlit view of the ancient jackfruit tree and the small brick shrine by the gate.
- 3.0–7.0s: Under a tranquil full moon, the camera glides slowly toward the shrine where three freshly lit incense sticks glow bright red in the night.
- 7.0–10.0s: Close view of the three glowing red incense tips curling white smoke into the moonlight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Quý vị thân mến, trên đời này có những nỗi tủi phận của người đã khuất mà đôi khi người đang sống vô tình lãng quên mất." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets on a moonlit night, a soft breeze over the glowing incense. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 2 (`canh-15/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Full-moon night, calm and peaceful: the moonlit courtyard, the glowing brick shrine under the ancient jackfruit tree and the warm-lit ancestral hall.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @VongCuXa = the ghost of Cụ Xá, Bình's late grandfather, about 80; gaunt, wispy white hair and beard, sad hollow eyes; faded brown traditional áo bà ba, barefoot; semi-transparent with a faint cold glow.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: In the moonlit courtyard beside the porch, @VongCuXa's serene translucent figure stands watching.
- 3.0–7.0s: Silver moonlight filters through the jackfruit leaves onto the clean brick courtyard; beside the porch pillar, the gentle translucent figure of @VongCuXa smiles at peace and dissolves into ascending light motes.
- 7.0–10.0s: @VongCuXa smiles peacefully and dissolves into soft silver light motes rising into the night. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Sợi dây duy nhất có thể hóa giải mọi oán hờn giữa hai cõi âm dương, chính là chữ Hiếu và lòng thành kính từ tâm can." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind chimes chiming softly as the grandfather turns into rising specks of light. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 3 (`canh-15/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Full-moon night, calm and peaceful: the moonlit courtyard, the glowing brick shrine under the ancient jackfruit tree and the warm-lit ancestral hall.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @BaPhuong = Bà Phượng, Bình's mother, 50; gentle worried oval face, black hair with grey streaks in a low bun; plain blue blouse, dark trousers.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal glide into hall; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Camera glides through the open wooden doorway into the warm-lit ancestral main hall.
- 3.0–7.0s: The camera glides from the moonlit porch into the warm main worship hall where @Binh, @OngQuan, and @BaPhuong stand with clasped hands bowing reverently before the fragrant mahogany ancestral altar.
- 7.0–10.0s: @OngQuan, @BaPhuong, and @Binh bow together before the glowing mahogany altar. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Dù đi đâu về đâu, giàu sang hay nghèo khó, mỗi người con đất Việt xin đừng bao giờ để lạnh khói hương nơi bàn thờ tổ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft hush of the warm altar room, faint incense crackle. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 4 (`canh-15/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Full-moon night, calm and peaceful: the moonlit courtyard, the glowing brick shrine under the ancient jackfruit tree and the warm-lit ancestral hall.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngBay = Ông Bảy, 60, the neighbouring village farmer; lean and sun-tanned, silver-streaked hair, kind wrinkled face; faded plaid shirt with a plain pocket (no name tag, badge, label or embroidery), brown work trousers, rubber sandals; often with his old black bicycle.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized medium tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @OngBay walks along the moonlit village lane past the open iron gate under the jackfruit tree.
- 3.0–7.0s: Outside the open iron gate under the silver full moon, @OngBay walks leisurely along the village lane, smiling and nodding toward the warm-lit ancestral house before continuing on his way.
- 7.0–10.0s: @OngBay smiles warmly looking into the bright courtyard, then walks on down the quiet lane. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Bởi thứ mà ông bà tổ tiên đã khuất mong mỏi nhất, chỉ là tấm lòng tưởng nhớ hướng về cội nguồn của con cháu." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: unhurried footsteps on the moonlit village lane, bamboo leaves rustling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 5 (`canh-15/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Full-moon night, calm and peaceful: the moonlit courtyard, the glowing brick shrine under the ancient jackfruit tree and the warm-lit ancestral hall.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
- @OngQuan = Ông Quân, Bình's father, 55; stocky, crew-cut greying hair, stern face with deep frown lines; white collared shirt with rolled sleeves, dark trousers.
- @BaPhuong = Bà Phượng, Bình's mother, 50; gentle worried oval face, black hair with grey streaks in a low bun; plain blue blouse, dark trousers.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm stabilized aerial drone slow ascending pull-back; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Wide view of the glowing three-bay ancestral house and courtyard under the full moon.
- 3.0–7.0s: Wide aerial drone shot ascending slowly under the full moon: the three-bay tiled house where @Binh, @OngQuan, and @BaPhuong stand on the porch glows like a warm lantern amid vast Northern rice fields.
- 7.0–10.0s: High aerial pull-back revealing the warm-lit house nestled peacefully among moonlit rice paddies. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Khép lại câu chuyện Căn Nhà Âm Dương đêm nay, cầu mong mỗi mái nhà Việt Nam luôn giữ trọn được hơi ấm nghĩa tình muôn đời." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a gentle bamboo-flute melody blending with wind over the moonlit rice fields. Ambience continues to 10.0s.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 6 (`canh-15/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese folk-horror film set in the Northern Vietnamese countryside; gritty grade with deep charcoal-black shadows, damp moss greens and dark rust-terracotta tones, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key horror lighting: flickering amber oil-lamp and incense light against cold cyan-green moonlight and midnight-blue shade; daylight stays muted and desaturated.

[LOCATION]
Full-moon night, calm and peaceful: the moonlit courtyard, the glowing brick shrine under the ancient jackfruit tree and the warm-lit ancestral hall.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Binh = Bình, 21, thin pale Vietnamese university student; messy short black hair, dark circles under tired eyes; dark charcoal-grey hoodie over a white T-shirt, dark jeans, worn sneakers, black backpack.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm stabilized close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close framing on the three glowing red incense tips in the brick shrine under the jackfruit tree.
- 3.0–7.0s: The incense tips brighten gently in the night breeze while, in the soft-focus background, @Binh quietly closes the wooden doors of the house.
- 7.0–10.0s: The red incense tips glow softly in the moonlight as the wooden door clicks shut. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–7.2s by an off-screen male narrator (Vietnamese man about 45, standard Hà Nội Northern accent with clear six tones, sharp resonant mid-baritone with crisp consonants, fast and fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no pauses mid-sentence, never slow or sleepy), in Vietnamese, said exactly once: "Đồng hồ đã điểm sang canh ba, chúc quý vị ngủ ngon và hãy thử lắng nghe tiếng gió đêm đang thì thầm ngoài hiên nhà mình." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a wooden door closing softly with a click, night wind through the jackfruit leaves. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```
