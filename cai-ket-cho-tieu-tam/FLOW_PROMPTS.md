# Cái Kết Cho Tiểu Tam — Bộ 100 Prompt Google Flow Omni (25 Cảnh × 4 Clips × 15s)

- **Giọng Người Dẫn Chuyện (cố định cả 100 clip):** Vietnamese woman about 50, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm low alto with a slight husk, fast fluent heartfelt family-drama storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; đọc nhanh liên thanh như oan-thai-doi-me, ~4.0 âm tiết/giây, liền một hơi, không ngắt giữa câu.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 100 clips × 15s — 0 clip VO + 100 clip thoại (65 clip có hai lượt thoại); lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 24 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 76 clip ảnh nhân vật (Ingredients), 0 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** clip VO được tăng tốc giọng thêm 1.18x khi tải về (`FLOWKIT_VOICE_TEMPO` mặc định 1.18, đặt 1.0 để tắt), giữ nguyên khung hình 15s; clip lip-sync không bao giờ bị tăng tốc để khớp khẩu hình.
- **Màu phim & ánh sáng:** Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py cai-ket-cho-tieu-tam` sinh lại toàn bộ clip, README, kịch bản.

---

## Cảnh 01 - Clip 1 (`canh-01/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Pre-dawn aerial over the tiled roofs of Hà Nội's old quarter: mist, yellow streetlamps, a few lit kitchen windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm aerial descending glide from the misty rooftops down to an upper-floor window; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: High aerial view over the dark tiled roofs of the old quarter before dawn, thin mist drifting between the rooftops and yellow streetlamps glowing in the narrow alleys below.
- 3.0–7.0s: The camera glides down past tangled overhead wires to a small upper-floor window, where @BaNhan swings open the wooden shutters and starts speaking, her wrinkled face lit by a lamp behind her.
- 7.0–11.0s: @BaNhan keeps speaking as she leans on the sill with one hand on her bamboo walking stick, peering down into the dark empty alley with narrowed eyes.
- 11.0–15.0s: @BaNhan says her last words, closes her mouth and lifts one eyebrow at the alley below, while steam glows gold from the lit kitchen window under her in the mist. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–13.0s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bốn giờ sáng, cả phố còn ngủ, con dâu tôi đã dậy đồ xôi. Còn thằng con giám đốc của tôi thì dạo này toàn về lúc gà gáy. Tôi nói trước nhé, nhà này sắp có biến." (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a distant rooster crowing, a cold breeze, wooden shutters creaking, a soft hiss of steam below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 2 (`canh-01/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot from the dining table toward the stove and the staircase, slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The narrow kitchen before dawn, a big aluminum sticky-rice steamer puffing thick steam on the gas stove, banana leaves stacked on the wooden table, the steep tiled staircase dim beside it.
- 3.0–7.0s: @Thu lifts the steamer lid in a cloud of steam and speaks over her shoulder to @BaNhan, who comes slowly down the last stairs on her bamboo walking stick with her mouth closed.
- 7.0–11.0s: @BaNhan reaches the bottom step and answers @Thu with a dry crooked smile, raising the tip of her bamboo stick to point up at the ceiling, while @Thu listens with her mouth closed.
- 11.0–15.0s: @BaNhan finishes, closes her mouth and sets the stick back down on the tiles, while @Thu presses her lips together to hold back a smile and turns back to the steam. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–6.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Mẹ đau lưng thì cứ nằm, xuống bếp sớm thế làm gì hả mẹ?"
- Turn 2, 7.0–13.4s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Lưng mẹ đau mà còn dậy được, chứ anh chồng khoẻ như vâm của con thì vẫn ngáy khò khò trên gác kia kìa."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, the steamer lid rattling, slow footsteps on tiles, the tap of a bamboo stick, faint snoring from upstairs. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 3 (`canh-01/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot across the wooden table, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @BaNhan lowers herself onto a low stool at the wooden table while @Thu sets a small bowl of warm sticky rice in front of her, both of them silent in the drifting steam.
- 3.0–7.0s: @BaNhan speaks to @Thu with a loud sniff, pointing her chopsticks up the staircase, while @Thu folds a banana-leaf parcel across the table and listens with her mouth closed.
- 7.0–11.0s: @BaNhan finishes with a scornful little snort, and @Thu tilts her head toward the staircase and begins answering in a low hush, while @BaNhan listens with her mouth closed.
- 11.0–15.0s: @Thu finishes her hushed reply with a calm half-smile and closes her mouth, while @BaNhan rolls her eyes toward the ceiling and pops a ball of sticky rice into her mouth. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–9.6s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Hồi nó trắng tay, xôi của con là cao lương mỹ vị, giờ làm giám đốc rồi thì lại chê xôi là đồ nhà quê."
- Turn 2, 10.1–13.4s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Mẹ nói khẽ thôi, giám đốc nghe thấy lại dỗi cả tuần đấy."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, chopsticks against a bowl, banana leaves rustling, faint snoring from upstairs. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 4 (`canh-01/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm medium close-up two-shot beside the chair back, slow rack focus; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @BaNhan leans over to a charcoal-grey suit jacket draped on the back of a chair and sniffs its collar twice, her nose wrinkling, while @Thu watches from the table, both of them silent.
- 3.0–7.0s: @BaNhan holds the jacket collar out between two fingers like a dead fish and speaks to @Thu with a deadpan stare, while @Thu listens with her mouth closed, folding a banana leaf.
- 7.0–11.0s: @BaNhan finishes and lets the collar drop, and @Thu answers her without looking up, smoothing the banana leaf with calm fingers and a faint dry half-smile, while @BaNhan listens.
- 11.0–15.0s: @Thu says her last words and closes her mouth, and @BaNhan narrows her eyes and glances up at the small white home camera on the high kitchen shelf, her lips pressed tight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.6s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Mẹ sống bảy mươi năm, chưa thấy ai đi họp mà về thơm nức mùi nước hoa đàn bà thế này."
- Turn 2, 9.1–13.1s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Mẹ lại đùa. Khách của anh ấy chắc dùng nước hoa thay nước lã đấy mẹ."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: two loud sniffs, steam hissing, a banana leaf crackling, a rooster outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 1 (`canh-02/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Dawn on a Hà Nội old-quarter pavement corner: a small sticky-rice stall with a bamboo basket, a steaming pot and banana leaves under a big faded umbrella, low plastic stools, mopeds passing, blue-grey dawn light and yellow streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- Extra: an elderly woman street sweeper in an orange vest with a bamboo broom
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide establishing shot, slow lateral track along the pavement; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A quiet old-quarter street corner at dawn, yellow streetlamps still glowing over the mist, a small sticky-rice stall steaming under a big faded umbrella beside empty low plastic stools.
- 3.0–7.0s: @Thu lifts the lid of the steaming pot as an elderly woman street sweeper in an orange vest pauses by the stall with her bamboo broom, and @Thu starts speaking to her warmly.
- 7.0–11.0s: @Thu keeps speaking with a bright wry smile as she wraps a warm banana-leaf parcel, tipping her head once toward the glass towers far down the street.
- 11.0–15.0s: @Thu finishes, closes her mouth and pats the low plastic stool beside her with a little shrug, while the sweeper's shoulders shake with a silent chuckle as she takes the warm parcel in both hands. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cô ơi, sương lạnh thế này, cháu biếu cô gói xôi nóng. Chồng cháu á? Giám đốc đấy cô ạ. Giám đốc thì ngồi ô tô, còn vợ giám đốc ngồi ghế nhựa bán xôi." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a moped passing, steam hissing, a bamboo broom sweeping the pavement. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 2 (`canh-02/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, slow push-in toward the high kitchen shelf; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Early morning light in the narrow kitchen, the small white home camera on the high kitchen shelf blinking its tiny light above the empty dining table and a covered plate of banana-leaf parcels.
- 3.0–7.0s: @BaNhan shuffles in on her bamboo walking stick, rises on tiptoe, taps the little white camera twice with the tip of her stick like knocking on a door, and starts speaking up to it.
- 7.0–11.0s: @BaNhan keeps reporting up to the little camera in a conspiratorial murmur, counting the points off on her thin fingers and nodding to it as if it were answering her.
- 11.0–15.0s: @BaNhan says her last words, closes her mouth and wags one bony finger at the little camera, then gives it a satisfied nod and lowers herself onto a stool. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.8s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Camera ơi, bà báo cáo nhé: đêm qua thằng Tùng hai giờ mới về, giày để ngược, nằm cười một mình với cái điện thoại. Mày ghi hết vào cho bà, có ngày bà cần đến mày." (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a bamboo stick tapping plastic twice, slippers shuffling on tiles, a stool creaking, a rooster outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 3 (`canh-02/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Dawn on a Hà Nội old-quarter pavement corner: a small sticky-rice stall with a bamboo basket, a steaming pot and banana leaves under a big faded umbrella, low plastic stools, mopeds passing, blue-grey dawn light and yellow streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The edge of the stall in grey dawn light, an old cracked smartphone lying face-down beside the bamboo basket with a faint glow leaking from its edges, steam drifting past the faded umbrella.
- 3.0–7.0s: @Thu sits on the low stool, holds the old phone flat near her mouth with its glowing screen turned toward her and away from the camera, and starts speaking into it with a calm face.
- 7.0–11.0s: @Thu keeps speaking as she draws a small empty red velvet earring box from her apron pocket with her free hand and thumbs it open, gazing at the bare velvet.
- 11.0–15.0s: @Thu says her last words with a dry half-smile, closes her mouth and clicks the empty velvet box shut, her eyes bright but steady as steam curls past her face. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.0s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh nhắn em đừng mang xôi lên công ty kẻo đối tác cười à? Vâng, em nhớ rồi. Ngày xưa em bán đôi bông tai cưới cho anh làm vốn, lúc ấy anh có cười đâu." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, the soft click of a box lid, a distant moped, dawn birdsong. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 4 (`canh-02/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Dawn on a Hà Nội old-quarter pavement corner: a small sticky-rice stall with a bamboo basket, a steaming pot and banana leaves under a big faded umbrella, low plastic stools, mopeds passing, blue-grey dawn light and yellow streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- Extra: a woman customer in a pink raincoat
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm over-the-shoulder shot from behind the customer, slow crane up above the umbrella; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The steaming pot under the faded umbrella, banana-leaf parcels lined up in the bamboo basket, a parked moped at the curb in the brightening dawn.
- 3.0–7.0s: @Thu stands behind the pot facing a woman customer in a pink raincoat, tucks an extra spoonful of fried shallots into a warm parcel and starts calling out with a bright grin.
- 7.0–11.0s: @Thu hands the parcel across the basket and keeps speaking, tipping her chin toward the distant skyline as the camera begins to rise above the umbrella.
- 11.0–15.0s: The camera rises above the faded umbrella to reveal glass towers catching the sunrise far away, while @Thu finishes, closes her mouth and pats the side of her steaming pot below. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Xôi xéo nóng đây chị ơi! Chị thấy tòa nhà kính kia không? Chồng em ngồi tít trên đấy. Em cứ giữ cái gánh xôi này, lỡ mai anh ấy ngã xuống thì còn có chỗ mà đỡ." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, rustling banana leaves, mopeds passing, morning street noise rising. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 1 (`canh-03/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, slow push-in toward the mirror; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Morning light through the open front door of the narrow house, a small mirror hanging beside the steep tiled staircase, a leather briefcase resting on a stool.
- 3.0–7.0s: @Tung steps in front of the mirror in his charcoal-grey suit, raises one palm to an imaginary audience and starts speaking in a grand booming tone to his own reflection.
- 7.0–11.0s: @Tung keeps speaking as he leans close to the glass, smooths his gelled hair with both palms and turns his chin left and right to admire his profile.
- 11.0–15.0s: @Tung finishes, closes his mouth, points a finger at his reflection and winks at it, then straightens his open white collar with a pleased little nod. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Kính thưa quý vị, thay mặt ban giám đốc, tôi xin phát biểu. Chà, khuôn mặt sáng sủa thế này, ngày xưa đi giao xôi với vợ đúng là phí cả một thời trai trẻ." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a moped outside, morning birds, the mirror creaking on its nail. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 2 (`canh-03/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 40mm over-the-shoulder shot from behind the girl at child height, slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The foot of the steep staircase seen from child height, a small red toy drum with two wooden sticks resting on the bottom step in the morning light.
- 3.0–7.0s: @Na hurries down the last steps in her school uniform, scoops up the little red drum and speaks up at @Tung, who keeps preening at the mirror with his mouth closed.
- 7.0–11.0s: @Na finishes her question and hugs the drum, and @Tung answers her without turning from the mirror, flicking a speck off his lapel, while @Na listens with her mouth closed.
- 11.0–15.0s: @Tung finishes, closes his mouth and picks up his briefcase, while @Na lowers the little red drum to her side and stares at his back, her lower lip tucked in. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.3s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter): "Bố ơi, sao bố soi gương lâu hơn cả mẹ thế? Chiều nay bố đi xem con đánh trống nhé."
- Turn 2, 8.8–13.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Bộ mặt giám đốc là bộ mặt công ty đấy con. Chiều bố họp, con bảo mẹ đi."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: light footsteps on tiles, a soft drum tap, a briefcase clasp clicking, a moped outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 3 (`canh-03/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide two-shot from the kitchen, slow lateral dolly; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The kitchen near the open front door, a bowl of steaming sticky rice heaped with golden fried shallots on the wooden dining table in a patch of morning sun.
- 3.0–7.0s: @Thu holds the steaming bowl out toward @Tung at the doorway, and he waves one hand at it and speaks with a curl of his lip, while @Thu listens with her mouth closed.
- 7.0–11.0s: @Thu draws the bowl back to her chest and answers @Tung evenly with a calm half-smile, looking him straight in the eye, while he listens with his mouth closed.
- 11.0–15.0s: @Thu finishes, closes her mouth, sets the bowl on the table and sits down to it herself, while @Tung blinks twice, tugs his collar and walks out into the bright alley. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Thôi, xôi với chả xôi, ăn vào hôi mồm, lát gặp đối tác người ta cười cho."
- Turn 2, 7.8–12.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Hồi chưa làm giám đốc, anh ăn một lúc ba bát, đối tác duy nhất của anh là em đấy."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, a moped idling outside, footsteps leaving, a car door shutting outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 4 (`canh-03/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot in the doorway, slow pull-back; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The open front door of the narrow house and the empty bright alley outside, a thin trail of steam curling from a bowl of sticky rice on the wooden table.
- 3.0–7.0s: @Na walks up beside @Thu at the doorway hugging the little red drum, sniffs the air twice with her nose wrinkled and asks her a question, while @Thu listens with her mouth closed.
- 7.0–11.0s: @Thu crouches to @Na's height, smooths her red scarf and answers her with a dry, slightly crooked smile, while @Na listens with her eyes on her mother's face.
- 11.0–15.0s: @Thu finishes and closes her mouth, and @Na giggles silently behind her hand and gives the little red drum one soft tap, the two of them framed in the bright doorway. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter): "Mẹ ơi, bố bảo đi họp, sao bố xịt nước hoa thơm như cô nào ấy?"
- Turn 2, 7.8–13.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Trẻ con biết gì. Chiều nay mẹ ngồi hàng đầu xem con đánh trống, còn bố chắc họp ở tiệm nước hoa."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning birds, a moped passing in the alley, a soft drum tap. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 1 (`canh-04/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, slow dolly-in on the white desk; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A bright glass-walled office high above the city, the large white desk gleaming in cold morning light, with a glossy black lacquered lunch box sitting open beside a framed family photo of Thu, Tùng and Na.
- 3.0–7.0s: @Vy stands at the desk in her crimson dress, tears open a plain paper takeaway bag with no logo and starts murmuring to herself with a wicked little grin.
- 7.0–11.0s: @Vy keeps murmuring as she tips the takeaway rice and braised pork from the bag into the lacquered box, then sprinkles a pinch of chopped green onion on top with a flourish.
- 11.0–15.0s: @Vy finishes, closes her red lips and presses the lacquered lid shut, then drops the crumpled paper bag into the waste bin under the desk without looking. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.8s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cơm quán dưới sảnh, bóc túi, đổ sang hộp sơn mài, rắc thêm tí hành là thành cơm em tự tay nấu. Đàn ông ấy mà, cứ thấy cái hộp đẹp là tin sái cổ." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper tearing, rice sliding into a box, a lid clicking shut, air conditioning hum. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 2 (`canh-04/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide two-shot of the office, slow lateral dolly; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The white desk with a glossy black lacquered lunch box resting beside a framed family photo of Thu, Tùng and Na, the city skyline blurred in the glass behind.
- 3.0–7.0s: @Tung sits in the black leather chair with chopsticks over the lunch box, swallows a bite and speaks to @Vy with his eyes narrowed at the food, while she stands by the desk with her mouth closed.
- 7.0–11.0s: @Vy freezes for a heartbeat with her smile stuck in place, then answers @Tung in a honey-sweet voice, fluttering her lashes, while he listens with his mouth closed.
- 11.0–15.0s: @Vy finishes and closes her red lips, and @Tung shrugs, nods and digs back into the lunch box, while @Vy lets out a slow silent breath behind her smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Em nấu đấy à? Ngon thật, mà sao vị giống hệt cơm quán dưới sảnh thế nhỉ?"
- Turn 2, 7.8–12.6s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Thì em học lỏm công thức của quán ấy đấy anh, ai bảo anh mê cơm ở đấy cơ."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: chopsticks clicking on lacquer, chair leather creaking, air conditioning hum. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 3 (`canh-04/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow rack focus between them; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy perches on the corner of the white desk and leans toward @Tung as he sets the chopsticks down, straightening his open white collar with one fingertip, both of them silent.
- 3.0–7.0s: @Vy speaks to @Tung in a soft coaxing voice, tilting her head so her wavy hair falls over one shoulder, while @Tung listens with his mouth closed.
- 7.0–11.0s: @Vy finishes, and @Tung gives his own sleeve one quick sniff, lowers it with a sour grimace and answers her, while @Vy listens with a sympathetic pout.
- 11.0–15.0s: @Tung finishes and closes his mouth, frowning at his sleeve, while @Vy hides a small cold smirk behind her hand, the skyline glittering behind them. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.5s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Anh tài giỏi thế này, sao tối nào cũng phải về ngồi ngửi mùi khói bếp hả anh?"
- Turn 2, 8.0–11.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Em nói đúng, giám đốc gì mà người lúc nào cũng ám mùi lá chuối."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: chair leather creaking, a long sniff, faint traffic far below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 4 (`canh-04/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, slow lateral dolly from the glass wall to the desk corner; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The empty office in cold city light, the white desk bare except for a framed family photo of Thu, Tùng and Na and a glossy black lacquered lunch box scraped clean.
- 3.0–7.0s: @Vy strolls back in through the glass door, stops at the corner of the desk, picks up the family photo and starts speaking to it in a sugary baby voice.
- 7.0–11.0s: @Vy keeps whispering to the photo, tapping the glass over the wife's face with one red fingernail and tilting her head in mock sympathy.
- 11.0–15.0s: @Vy says her last words, closes her mouth and lays the frame face down on the desk with one manicured finger, her smile reflected cold in the glossy white surface. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.5s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ảnh gia đình ba người, đẹp nhỉ. Chị Thu ơi, chị cứ ở nhà đồ xôi cho mỏi tay đi, còn ông chồng giám đốc của chị, em xin phép nhận nuôi hộ nhé." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: high heels on a polished floor, a fingernail tapping glass, a soft tap of a frame on the desk. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 1 (`canh-05/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
An upscale café at noon: velvet armchairs, brass lamps, marble tables, tall windows facing a leafy street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide establishing shot, slow pan across the room; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A hushed upscale café at noon, sunlight through tall windows onto velvet armchairs and marble tables, a tall potted areca palm half-hiding a corner table under a brass lamp.
- 3.0–7.0s: @Vy walks in sliding her dark sunglasses down her nose, spots @Khai crouched low behind the potted palm and speaks to him with one eyebrow raised, while he stays silent.
- 7.0–11.0s: @Khai pokes his head out between the palm fronds with a sly grin and answers @Vy in a lazy whisper, while she listens with her red lips pressed together.
- 11.0–15.0s: @Khai finishes, closes his mouth and slides up into the velvet armchair behind the palm, smoothing his black shirt, while @Vy shakes her head and sits down opposite him. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.0s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Anh Khải, anh ngồi thụp sau chậu cau làm gì, trông như đi ăn trộm thế?"
- Turn 2, 7.5–11.8s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Thì mình đi ăn trộm thật còn gì, mà trộm hẳn một cái công ty cơ em."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a café door chime, soft clinking of cups, palm fronds rustling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 2 (`canh-05/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
An upscale café at noon: velvet armchairs, brass lamps, marble tables, tall windows facing a leafy street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm over-the-shoulder shot through the palm fronds, gentle dolly; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Khai parts the palm fronds with two fingers to peek out at the room, then lets them fall back and leans toward @Vy across the marble table, both of them silent.
- 3.0–7.0s: @Khai speaks to @Vy in a low lazy voice with a sly half-smile, tapping one finger on the marble, while @Vy slips off her sunglasses and listens with her mouth closed.
- 7.0–11.0s: @Vy answers @Khai with a cool crooked smile, stirring her coffee slowly, the sweetness gone from her face, while he listens with his mouth closed.
- 11.0–15.0s: @Vy finishes and sets the spoon on the saucer with a precise click, while @Khai raises both eyebrows and sits back slowly, his silver chain bracelet catching the lamplight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Ngồi xuống đi em, kẻo có người nhìn thấy. Thế nào, lão giám đốc cắn câu chưa?"
- Turn 2, 7.8–13.3s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Cắn câu à? Lão nuốt luôn cả cần câu rồi anh. Nửa năm nữa lão bỏ vợ, sang tên nhà cho em."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: cups clinking, a low café murmur, a spoon circling porcelain. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 3 (`canh-05/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
An upscale café at noon: velvet armchairs, brass lamps, marble tables, tall windows facing a leafy street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Two coffee cups steaming on the marble table behind the potted areca palm, a pair of dark sunglasses and a phone lying face-down beside them in the brass lamplight.
- 3.0–7.0s: @Khai leans in over the cups and speaks to @Vy in a hushed voice, glancing twice over the palm fronds toward the windows, while @Vy listens with her mouth closed.
- 7.0–11.0s: @Khai finishes his worry, and @Vy answers him with a slow curl of her red lips, her winged eyes cold above the rim of her coffee cup, while he listens with his mouth closed.
- 11.0–15.0s: @Vy finishes and closes her mouth, taking a sip of coffee, while @Khai lets out a long breath and tugs at his collar, glancing at the palm fronds once more. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.3s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Nhưng nhỡ lão phát hiện ra có anh thì sao? Đàn ông ngu đến mấy cũng có lúc tỉnh đấy em."
- Turn 2, 8.8–12.6s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Lão ký hợp đồng còn chẳng thèm đọc, thì làm sao mà đọc nổi em."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a low café murmur, a cup set on a saucer, a car passing outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 4 (`canh-05/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
An upscale café at noon: velvet armchairs, brass lamps, marble tables, tall windows facing a leafy street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, slow lateral dolly; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy sets her coffee cup down and leans forward toward @Khai, her red nails tapping the rim, both of them silent in the warm lamplight behind the palm.
- 3.0–7.0s: @Vy speaks to @Khai in a low cold voice, her winged eyes narrowing above a thin smile, while @Khai listens with his mouth closed.
- 7.0–11.0s: @Khai lifts his coffee cup toward her in a small toast and answers with a lazy grin, then pats his empty trouser pockets with a sheepish shrug, while @Vy listens.
- 11.0–15.0s: @Khai finishes and closes his mouth, and @Vy rolls her eyes at the ceiling, takes a folded banknote from her small white handbag and sets it on the marble with a sigh. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.0s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Đến lúc lão tỉnh ra thì chỉ còn cái bụng phệ với hai bàn tay trắng."
- Turn 2, 7.5–12.5s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Thế thì cụng ly, chúc mừng bà chủ tương lai. À mà em trả tiền nhé, anh lại quên ví."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: porcelain cups clinking, a low café murmur, a handbag clasp clicking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 1 (`canh-06/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot, slow dolly-in across the kitchen; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The dim kitchen at night lit by one warm bulb, the charcoal stove glowing low, a white dress shirt and a loosened silk tie draped over a dining chair, black shoes askew beneath it.
- 3.0–7.0s: @BaNhan lifts the white shirt off the chair on the tip of her bamboo walking stick, sniffs it and speaks with a sour pucker, while @Thu comes down the last stairs listening with her mouth closed.
- 7.0–11.0s: @BaNhan finishes, and @Thu lifts the shirt off the stick and answers her calmly, folding it over her arm, while @BaNhan listens with her mouth closed and one eyebrow raised.
- 11.0–15.0s: @Thu finishes and closes her mouth, then lifts the collar toward the bulb and stops, her brows drawing together, while @BaNhan's hand tightens on her bamboo stick. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.0s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Lại nước hoa. Loại này đắt tiền đấy, thằng Tùng có bao giờ mua cho con lọ nào đâu."
- Turn 2, 8.5–13.0s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Mẹ đưa con giặt, mai anh ấy còn mặc đi họp. Họp với ai thì con chưa biết."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the charcoal stove crackling, soft footsteps on the stairs, fabric rustling, a dog barking far away. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 2 (`canh-06/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on the collar and their faces, slow rack focus; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu turns the white collar toward the bulb, revealing a smudge of bright red lipstick on the fabric, while @BaNhan leans in to look, both of them silent.
- 3.0–7.0s: @Thu lifts a single long wavy brown hair from the shoulder of the shirt, holds it up in the warm light and speaks to @BaNhan in an even voice, while @BaNhan listens.
- 7.0–11.0s: @Thu finishes, and @BaNhan squints at the brown hair, then answers @Thu in a flat deadpan voice without blinking, while @Thu listens with her mouth closed.
- 11.0–15.0s: @BaNhan finishes and closes her mouth, and @Thu lets the hair drift to the floor and folds the shirt into a neat square, her jaw set and her eyes dry. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Mẹ ơi, son đỏ trên cổ áo, sợi tóc xoăn màu nâu, mà tóc con thì thẳng và đen."
- Turn 2, 8.3–11.8s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Tóc xoăn, son đỏ, chắc không phải ông khách hàng nào đâu nhỉ."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the stove crackling, a slow breath, a moth tapping the bulb. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 3 (`canh-06/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide two-shot from the kitchen doorway, slow dolly; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The foot of the steep staircase in the dim warm light, the wooden dining table between the stairs and the glowing charcoal stove, the kitchen empty and still.
- 3.0–7.0s: @Tung appears on the lower stairs in his suit, and @Thu holds up the folded white shirt toward him from across the table and speaks in a steady voice, while he listens.
- 7.0–11.0s: @Tung rolls his eyes, steps down onto the tiles and answers @Thu flatly with a lazy wave of his hand, not looking at the shirt, while she listens with her mouth closed.
- 11.0–15.0s: @Tung finishes, closes his mouth, turns his back and climbs the stairs again, while @Thu stays across the table with the shirt still raised and one eyebrow lifted. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.0s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Anh Tùng, vệt son đỏ trên cổ áo anh là của ai? Anh nói thật đi."
- Turn 2, 7.5–12.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Thang máy công ty đông người, ai va vào chả dính, cô đừng có làm ầm lên giữa đêm."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the stove crackling, a creaking stair, heavy footsteps on the stairs. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 4 (`canh-06/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot from the kitchen, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The bottom of the steep tiled staircase in the dim kitchen, the warm bulb swaying slightly on its cord and the charcoal stove reduced to faint embers.
- 3.0–7.0s: @Thu sits down on the lowest stair with the white shirt in her lap and starts speaking quietly toward the dark top of the stairs, her face calm.
- 7.0–11.0s: @Thu keeps speaking as she rubs the red smudge on the collar with her thumb, then folds the shirt into a perfect square on her knees.
- 11.0–15.0s: @Thu says her last words with a calm half-smile, closes her mouth and sets the folded shirt on the step beside her, her eyes on the dark landing above. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–13.0s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thang máy công ty anh chắc đông lắm, đông đến mức son người ta dính đúng cổ áo, tóc người ta vắt đúng vai anh. Được, em không làm ầm. Em cứ im lặng mà xem anh diễn đến đâu." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: embers ticking, the bulb cord creaking, a distant dog bark. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 1 (`canh-07/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Sunset at a luxury seaside resort: an infinity pool terrace with white loungers, palm trees, the sea glowing orange.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm aerial slow descending orbit down to the pool terrace; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: High aerial view of a luxury seaside resort at sunset, palm trees swaying above a long curve of golden beach and a calm orange sea.
- 3.0–7.0s: The camera sweeps down to the infinity pool terrace, where @Tung stands in his full charcoal-grey suit beside a white lounger, a phone pressed to his ear, speaking in a solemn businesslike voice.
- 7.0–11.0s: @Tung keeps speaking into the phone as a big wave rolls loudly onto the beach below, and he quickly cups his free hand over the phone and turns his back to the sea.
- 11.0–15.0s: @Tung finishes, closes his mouth, lowers the phone and tosses it onto the lounger with a smug grin, the pool edge melting into the shining sea behind him. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thu à, anh đang họp căng lắm, phải ba ngày nữa mới về, sinh nhật em anh không kịp rồi. Tiếng gì à? À, máy lạnh phòng họp kêu đấy em, công ty to thì máy lạnh cũng to." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: gentle waves, one loud wave rolling onto the sand, palm fronds rustling, distant seabirds. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 2 (`canh-07/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Sunset at a luxury seaside resort: an infinity pool terrace with white loungers, palm trees, the sea glowing orange.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, slow lateral dolly along the pool; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Two white loungers at the edge of the infinity pool, a small table between them holding two glasses of orange juice, the sea glowing orange beyond.
- 3.0–7.0s: @Vy reclines on one lounger in her crimson dress, lifts her glass of orange juice in a mock toast and teases @Tung with a smirk as he sits beside her, while he listens with his mouth closed.
- 7.0–11.0s: @Tung answers @Vy with a lazy grin, jerking a thumb toward the sea behind him, while @Vy listens with a closed-mouth smile.
- 11.0–15.0s: @Tung finishes and closes his mouth, and @Vy clinks her glass against his, the two of them grinning and gazing out at the orange sea. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–6.5s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Máy lạnh phòng họp mà có cả sóng biển với nước cam hả anh?"
- Turn 2, 7.0–11.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Vợ anh chỉ biết xôi với chợ, anh bảo sóng biển là máy lạnh thì cô ấy cũng tin."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: gentle waves, glasses clinking, a soft breeze. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 3 (`canh-07/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Sunset at a luxury seaside resort: an infinity pool terrace with white loungers, palm trees, the sea glowing orange.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy turns toward @Tung on the lounger, resting her chin on her hand, the sunset gilding her wavy hair, both of them silent.
- 3.0–7.0s: @Vy speaks to @Tung in a sweet coaxing voice, her winged eyes half-lowered, tracing a small square frame in the air with one finger, while @Tung listens with his mouth closed.
- 7.0–11.0s: @Vy finishes, and @Tung waves a careless hand and answers her with a shrug, his eyes on the darkening sea, while she listens with her mouth closed.
- 11.0–15.0s: @Tung finishes and closes his mouth, and @Vy rests her head lightly on his shoulder, her sweet smile turning cold where he cannot see it as the last sunlight fades. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Anh ơi, thế bao giờ em mới được đứng cạnh anh trong tấm ảnh gia đình trên bàn ấy?"
- Turn 2, 8.3–12.6s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Về Hà Nội anh tính. Ảnh thì dễ thôi em, ra hiệu ảnh chụp lại là xong."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: waves lapping, a soft breeze through the palms. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 4 (`canh-07/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 40mm over-the-shoulder shot across the birthday cake, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The wooden dining table in the dim kitchen at night, a small round birthday cake with one lit candle, three bowls and one empty chair pulled out at the far end.
- 3.0–7.0s: @Na kneels on her stool across the cake from @Thu and speaks to her with a puzzled frown, cupping one hand behind her ear, while @Thu listens with her mouth closed.
- 7.0–11.0s: @Thu answers @Na with a dry little smile, her eyes glistening in the candlelight as she slides the cake toward her daughter, while @Na listens with her mouth closed.
- 11.0–15.0s: @Thu finishes and closes her mouth, and @Na shuts her eyes and clasps her small hands over the candle, while @Thu glances at the empty chair across the table. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.0s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter): "Mẹ ơi, bố bảo máy lạnh kêu, nhưng con nghe rõ tiếng sóng biển mà."
- Turn 2, 7.5–13.0s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Ừ, máy lạnh nhà giàu kêu như sóng biển đấy con. Thôi, thổi nến đi, điều ước năm nay mẹ nhường con."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint candle hiss, soft rain on the roof, a moth tapping the bulb. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 1 (`canh-08/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, slow push-in on the table; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The dining table in the dim kitchen at night, a sleek black smartphone lying face-down beside a car key, buzzing on the wood as a cold glow leaks from under its edges.
- 3.0–7.0s: @Thu steps over from the stove, picks up the buzzing phone with its glowing screen turned toward her and away from the camera, and starts reading aloud in a flat dry voice.
- 7.0–11.0s: @Thu keeps speaking as she tilts the phone in the cold light, one eyebrow climbing higher with each word, her other hand settling on her hip.
- 11.0–15.0s: @Thu says her last words, closes her mouth and looks up from the glowing phone toward the staircase with a calm, icy half-smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.0s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh Tuấn kế toán nhắn lúc nửa đêm: nhớ anh quá. Còn gửi cả ảnh. Kế toán gì mà tóc xoăn, váy đỏ, lại tựa đầu vào vai chồng người ta thế này hả anh Tuấn?" (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone buzzing on wood, a dripping tap, a heavy silence. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 2 (`canh-08/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide two-shot from the stove, slow dolly; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The steep staircase and the dining table in the dim kitchen, a phone's cold glow the brightest light in the room, the charcoal stove ticking low.
- 3.0–7.0s: @Tung strides down the last stairs and stops on the far side of the table, pointing at the phone in @Thu's hand as he speaks sharply, while she listens with her mouth closed.
- 7.0–11.0s: @Thu sets the glowing phone face-down on the table between them and answers @Tung evenly with her chin lifted, while he listens with his jaw working.
- 11.0–15.0s: @Thu finishes, closes her mouth and folds her arms, while @Tung opens and shuts his empty hands at his sides, the wooden table still between them. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–6.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Cô lục điện thoại của tôi à? Thế là xâm phạm đời tư đấy!"
- Turn 2, 7.0–12.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Đời tư à? Thế anh xâm phạm cả cái nhà này, cả mẹ con em, thì gọi là gì hả anh?"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heavy footsteps on tiles, a phone set down on wood, the tap dripping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 3 (`canh-08/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot across the table, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung picks his phone up off the table and slips it into his trouser pocket without looking at @Thu, both of them silent under the swaying bulb.
- 3.0–7.0s: @Tung speaks coldly to @Thu with a flick of his hand toward the steamer by the stove, his nose wrinkled, and then @Thu begins answering in a low steady voice while he listens.
- 7.0–11.0s: @Thu keeps answering @Tung with her eyes level and dry, tapping one finger on the wooden table with each phrase, while @Tung listens with his jaw set.
- 11.0–15.0s: @Thu finishes and closes her mouth, and @Tung turns away without a word and climbs the stairs two at a time, leaving @Thu alone at the table under the swaying bulb. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–6.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Tôi chán cái nhà này rồi, chán mùi xôi, chán cả cô."
- Turn 2, 6.5–13.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Anh chán mùi xôi, nhưng hồi anh trắng tay, chính gánh xôi với đôi bông tai cưới em bán đi đã nuôi anh thành giám đốc đấy."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: footsteps on the stairs, a door shutting hard upstairs, the tap dripping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 4 (`canh-08/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night on the dim tiled stair landing of the tube house, a faint light from the kitchen below.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium low-angle shot up the stairwell, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A dim tiled stair landing in darkness, a faint warm glow rising from the kitchen below and a closed door above.
- 3.0–7.0s: @BaNhan stands on the landing in her brown cardigan gripping her bamboo walking stick, shakes her head at the closed door above and starts speaking in a sharp whisper.
- 7.0–11.0s: @BaNhan leans over the railing and keeps whispering down toward a tiny green light glowing far below in the kitchen, wagging one bony finger at it.
- 11.0–15.0s: @BaNhan says her last words, closes her mouth and taps her own temple twice with one finger, giving a firm little nod in the faint light. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.3s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thằng này hết thuốc chữa thật rồi. Camera ơi, ở dưới ấy mày có ghi được không? Không ghi được thì bà nhớ hộ. Bà già thật, nhưng trí nhớ còn tốt hơn mày đấy." (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a door closing upstairs, the faint drip of a tap below, the railing creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 1 (`canh-09/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Dawn on a Hà Nội old-quarter pavement corner: a small sticky-rice stall with a bamboo basket, a steaming pot and banana leaves under a big faded umbrella, low plastic stools, mopeds passing, blue-grey dawn light and yellow streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow tilt up from the wet curb to her face; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A black luxury sedan with no badge glides to a stop at the curb of the misty old-quarter corner, its glossy rear door swinging open onto the wet pavement under a yellow streetlamp.
- 3.0–7.0s: A beige high heel steps down onto the pavement and the camera tilts up to @Vy in her crimson dress and dark sunglasses as she starts murmuring to herself, her red lips clearly visible.
- 7.0–11.0s: @Vy lowers the sunglasses to the tip of her nose with one finger and keeps murmuring, eyeing the small sticky-rice stall across the pavement from top to bottom with one eyebrow raised.
- 11.0–15.0s: @Vy finishes speaking and closes her red lips in a smirk, slides the sunglasses back up with one fingertip and starts walking toward the steaming stall, the car door left open behind her. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.3s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thì ra bà vợ bán xôi của anh Tùng ngồi ở cái góc này. Mặt mộc, tạp dề, tay thì chai sạn. Mình còn đeo kính râm cho đỡ chói mắt, hóa ra phí cả cái kính." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a car engine idling, a car door opening, high heels clicking on wet pavement, mopeds passing. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 2 (`canh-09/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Dawn on a Hà Nội old-quarter pavement corner: a small sticky-rice stall with a bamboo basket, a steaming pot and banana leaves under a big faded umbrella, low plastic stools, mopeds passing, blue-grey dawn light and yellow streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot in profile across the stall, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Banana leaves and a round bamboo tray of steaming sticky rice on the stall table under the big faded umbrella, wisps of steam drifting through the blue dawn light.
- 3.0–7.0s: @Vy walks up to the stall in her crimson dress and dark sunglasses and speaks sweetly across the steam with a tilted head, while @Thu keeps folding a banana-leaf parcel with her mouth closed.
- 7.0–11.0s: @Vy finishes and closes her red lips, and @Thu slowly looks up from the parcel, lets her eyes travel over the crimson dress and the wavy hair, and answers calmly with a faint dry half-smile.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, going back to tying the parcel, while @Vy's sweet smile stays frozen in place and her sunglasses slide halfway down her nose. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.0s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Chị ơi, cho em một gói xôi xéo, nghe nói ngày xưa anh Tùng mê xôi của chị lắm cơ."
- Turn 2, 8.5–12.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Váy đỏ, tóc xoăn, giọng ngọt như rót mật. Cô là kế toán Tuấn đấy à?"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing from the pot, high heels stopping on wet pavement, a moped passing, banana leaves rustling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 3 (`canh-09/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Dawn on a Hà Nội old-quarter pavement corner: a small sticky-rice stall with a bamboo basket, a steaming pot and banana leaves under a big faded umbrella, low plastic stools, mopeds passing, blue-grey dawn light and yellow streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot across the steaming pot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy takes off her sunglasses and rests one hand on the edge of the stall table, looking @Thu up and down, while @Thu ladles sticky rice onto a banana leaf, both with their mouths closed.
- 3.0–7.0s: @Vy speaks to @Thu in a sweet cold voice with a thin smile, her winged eyes narrowing, while @Thu keeps ladling the rice with steady hands and her mouth closed.
- 7.0–11.0s: @Vy finishes and closes her lips, and @Thu wraps the parcel without looking up and answers in an easy, kindly tone with a calm half-smile, her face and lips clearly visible.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, setting the neat parcel down right in front of @Vy, who blinks twice with her lips pressed shut and her smile sagging at one corner. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–6.5s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Chị giữ được cái bếp, nhưng giữ không nổi ông chồng đâu chị ạ."
- Turn 2, 7.0–12.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Em thích thì cứ lấy, chị không giữ đâu. Nhưng anh ấy ngáy to lắm, nhớ mua bông nhét tai nhé."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, a ladle tapping the pot rim, a moped horn far away. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 4 (`canh-09/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Dawn on a Hà Nội old-quarter pavement corner: a small sticky-rice stall with a bamboo basket, a steaming pot and banana leaves under a big faded umbrella, low plastic stools, mopeds passing, blue-grey dawn light and yellow streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot across the stall, slow dolly back; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy takes a folded banknote from her small white handbag and drops it onto the bamboo tray of sticky rice, while @Thu stands behind the pot watching, both with their mouths closed.
- 3.0–7.0s: @Vy slips her dark sunglasses back on and speaks to @Thu with a sugary smile, flicking her eyes at @Thu's work-roughened hands, while @Thu listens with her mouth closed.
- 7.0–11.0s: @Vy finishes and closes her lips, and @Thu picks up the banknote, smooths it flat and tucks it into her green apron pocket, answering evenly with a calm half-smile.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth and calmly wraps the next parcel, while @Vy's red lips press into a thin line and she turns on her heel toward the parked black car. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.0s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Tiền xôi đây, khỏi trả lại. Chị giữ lấy mà mua kem dưỡng da tay nhé."
- Turn 2, 7.5–12.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Cảm ơn em, chị mua thêm gạo nếp. Tay chị thô thật, nhưng chưa lấy của ai cái gì bao giờ."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a banknote rustling, steam hissing, high heels clicking away, a car door shutting. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 1 (`canh-10/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot along the dinner table, slow glide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A wooden dining table under one warm bulb set with braised fish, stir-fried morning glory, crab soup and a pot of rice, steam curling up beside neat bowls and chopsticks.
- 3.0–7.0s: @Thu sets a steaming bowl of crab soup in front of @Tung as he sits down in his charcoal suit, and speaks warmly to him, while he keeps his mouth closed.
- 7.0–11.0s: @Tung lifts his own suit sleeve to his nose, sniffs it with a grimace and answers @Thu flatly, laying his chopsticks across the untouched bowl, his face and lips clearly visible.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, leaning back with his arms folded, while @Thu stands motionless beside the table, the soup ladle frozen in her hand above the pot. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–6.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Anh ngồi xuống ăn đi, cá kho với canh cua anh thích đây."
- Turn 2, 6.8–12.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Bộ vest mấy chục triệu của tôi giờ ám toàn mùi cá kho. Tôi chịu hết nổi rồi, mình ly hôn đi."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a charcoal stove crackling, porcelain bowls clinking, chopsticks laid across a bowl. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 2 (`canh-10/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot across the corner of the table, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu slowly lowers the ladle into the soup pot and sits down at the corner of the table, her eyes level on @Tung, who stays leaning back, both of them with their mouths closed.
- 3.0–7.0s: @Thu speaks to @Tung in a quiet even voice with one eyebrow lifting, her hands folded on the table, while he listens with his mouth closed and his jaw tight.
- 7.0–11.0s: @Thu finishes and closes her mouth, and @Tung points one finger hard at the tabletop and answers loudly, his face and lips clearly visible, while she watches him with her mouth closed.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, his raised finger slowly curling back as his eyes widen at what he just blurted out, while @Thu tilts her head with a calm closed half-smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Anh định bỏ cả mẹ con em lẫn mâm cơm này để đi theo kế toán Tuấn đấy à?"
- Turn 2, 8.3–12.6s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Cô ấy hiểu tôi hơn cô nhiều. Mà Tuấn gì mà Tuấn, người ta tên là Vy!"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soup bowl clinking, rain beginning on the roof, the charcoal stove ticking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 3 (`canh-10/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot from the foot of the staircase along the table, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A carved bamboo walking stick leaning against a low stool at the corner of the dinner table, a pot of crab soup with an aluminum ladle resting in it under the warm bulb.
- 3.0–7.0s: @Tung stands up from the head of the table, buttons his suit jacket and speaks down to @BaNhan in a lofty tone, while she sits glaring at him with her mouth closed.
- 7.0–11.0s: @Tung finishes and closes his mouth, and @BaNhan rises on her bamboo stick, lifts the soup ladle out of the pot like a judge's gavel and answers him in a flat deadpan voice.
- 11.0–15.0s: @BaNhan finishes speaking and closes her mouth, the dripping ladle still raised from across the table, while @Tung stands stiff with his lips pressed shut and one hand frozen on his jacket button. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Mẹ đừng nhìn con như thế. Con lớn rồi, lại còn là giám đốc, chuyện nhà con tự lo."
- Turn 2, 8.3–13.3s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Giám đốc à? Giám đốc mà ăn cơm vợ nấu bao nhiêu năm, chưa rửa nổi một cái bát."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a stool scraping on tiles, broth dripping from a ladle, rain on the roof. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 4 (`canh-10/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot across the table, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @BaNhan lowers the ladle back into the crab soup and rests one hand on the pot handle, while @Tung stands across the table straightening his cuffs, both of them with their mouths closed.
- 3.0–7.0s: @BaNhan speaks to @Tung in a dry raspy deadpan, tapping the rim of the soup pot once with her finger, while he listens with his mouth closed and his chin raised.
- 7.0–11.0s: @BaNhan finishes and closes her mouth, and @Tung picks up his car keys from the table and answers her stiffly without meeting her eyes, his face and lips clearly visible.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, turning his shoulder toward the front door, while @BaNhan calmly slides the whole pot of crab soup to her own end of the table, her lips shut. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Nói thêm một câu nữa là mẹ cất nồi canh cua, cho giám đốc nhịn đói."
- Turn 2, 7.8–12.1s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Thì con nhịn, ra ngoài thiếu gì nhà hàng. Con quyết rồi, tuần này con dọn đi."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain on the roof, a walking stick tapping the tiled floor, a heavy pot sliding across wood, car keys jingling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 1 (`canh-11/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow tilt up from the basin of soaking rice to her face; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A glowing clay charcoal stove in the dark kitchen beside an aluminum basin of soaking sticky rice and a low plastic stool, a single warm bulb swaying slightly overhead.
- 3.0–7.0s: @Thu sits on the low stool rinsing the soaked rice with both hands and whispers to herself in a thin voice, a tear dropping into the basin, her face and lips lit orange.
- 7.0–11.0s: @Thu glances up toward the dark staircase and keeps whispering, then wipes her cheek with the back of her wet wrist, a small wry smile tugging at her lips.
- 11.0–15.0s: @Thu finishes whispering and closes her mouth, pours fresh water over the rice and stirs it with steady hands, her chin set in the orange glow of the stove. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thôi, không được khóc to. Mẹ mà thức thì lại lo, con bé mà thấy thì nó sợ. Khóc thì cứ khóc, nhưng nước mắt có làm chín được nồi xôi nào đâu." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal crackling, water swishing in a basin, crickets outside, a faint snore from upstairs. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 2 (`canh-11/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot from the side of the stove, slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The bottom of the steep tiled staircase in the dim kitchen, the clay stove glowing orange beside the basin of soaking rice and an empty low plastic stool.
- 3.0–7.0s: @Na pads down in her school clothes, sits on the stool beside @Thu and asks her a question with wide earnest eyes, while @Thu turns her wet face to her, mouth closed.
- 7.0–11.0s: @Na keeps asking with a small frown of concentration, and when she finishes and closes her mouth, @Thu bursts into a laugh through her tears and answers, tapping the tip of @Na's nose.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, wiping her eyes with her wrist and pulling @Na against her side, while @Na grins up at her with a closed mouth in the orange glow. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–9.4s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter): "Mẹ ơi, người ta bảo bố có bé ba, bé ba là gì hả mẹ? Có phải em bé thứ ba nhà mình không?"
- Turn 2, 9.9–13.7s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Không phải đâu con. Nhà mình chỉ có một em bé thôi, là con đấy."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: small footsteps on tiles, charcoal crackling, a soft laugh through a sniffle. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 3 (`canh-11/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot of mother and daughter, slow arc around the stove; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Na reaches up and wipes the tears off @Thu's cheeks with her small thumbs, then sits up very straight on the stool, both of them with their mouths closed.
- 3.0–7.0s: @Na holds up one stern little finger like a tiny boss and speaks earnestly to @Thu, her face and lips clearly visible, while @Thu listens with glistening eyes and her mouth closed.
- 7.0–11.0s: @Na finishes and closes her mouth, and @Thu gives her a small two-finger salute at her brow and answers with a trembling smile, her face and lips clearly visible.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, hooking her little finger around @Na's, both of them smiling with closed mouths in the orange glow of the stove. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.8s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter): "Thế con là bé nhất, bé nhất được ra lệnh: mẹ không được khóc nữa, mai con dậy gói xôi với mẹ."
- Turn 2, 9.3–13.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Vâng, mẹ tuân lệnh sếp nhỏ. Mẹ còn con, còn bà, mẹ không gục được đâu."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal crackling, rain easing outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 4 (`canh-11/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, low angle from beside the clay stove, slow tilt up to her face; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Grey charcoal embers inside a clay stove in the dark kitchen, a faint orange glow pulsing between them beside a woven bamboo hand fan lying on the tiles.
- 3.0–7.0s: @Thu kneels beside the stove, picks up the woven bamboo hand fan and fans the coals, speaking firmly to herself as the embers start to redden, her face and lips lit by the glow.
- 7.0–11.0s: @Thu keeps fanning in steady strokes as she speaks, a dry little smile aimed at the stubborn coals, her eyes fixed on the flames as they flare bright orange.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, fanning steadily with her chin raised, the fierce orange flames filling the bottom of the frame and lighting her dry eyes. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cháy lên nào. Than sắp tàn mà quạt mãi còn đỏ lại, chẳng lẽ người lại thua cục than. Từ mai mẹ con mình không chờ ai thương nữa, mình tự thương lấy mình." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal crackling and flaring, a bamboo fan swishing, a soft whoosh of air. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 1 (`canh-12/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A luxury high-rise apartment in the morning: a white marble kitchen island, a pale sofa, floor-to-ceiling windows over the city, glossy cold light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow rack focus from the test stick to her face; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Glossy cold morning light on a white marble kitchen island, a plastic pregnancy test stick showing two faint pink lines lying beside a cup of coffee and a vase of white orchids.
- 3.0–7.0s: @Vy leans into frame at the island in her crimson dress with a glowing phone pressed to her ear, chatting into it with a lazy smile, her face and red lips clearly visible.
- 7.0–11.0s: @Vy picks up the plastic pregnancy test stick showing two faint pink lines and twirls it between her manicured fingers like a tiny baton, still talking into the phone with a sly grin.
- 11.0–15.0s: @Vy finishes speaking and closes her lips, tucking the test stick into her small white handbag with a wink and lowering the glowing phone, the city skyline soft behind her. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.3s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "A lô, mày ơi, que này tao mượn của con bạn đang bầu đấy, hai vạch hồng hẳn hoi. Nó hỏi mượn làm gì, tao bảo mượn để mua nhà, mua cả chồng." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint city hum far below, an air conditioner whispering, a coffee cup set down on marble. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 2 (`canh-12/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A luxury high-rise apartment in the morning: a white marble kitchen island, a pale sofa, floor-to-ceiling windows over the city, glossy cold light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot by the kitchen island, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The marble kitchen island in cold morning light, a set of car keys and a leather wallet lying beside a coffee cup, the floor-to-ceiling windows glowing over the city.
- 3.0–7.0s: @Vy holds out the plastic pregnancy test stick showing two faint pink lines to @Tung with one hand on her flat stomach and speaks sweetly with shining eyes, while he keeps his mouth closed.
- 7.0–11.0s: @Vy finishes and closes her lips, and @Tung takes the stick, puffs out his chest and answers grandly, sweeping one open hand through the air as if unveiling a giant sign.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, smoothing his gelled hair in the window reflection with his chin up, while @Vy holds a sweet closed smile that tightens at one corner. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–6.8s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Anh ơi, mình có con rồi! Bác sĩ bảo chắc là con trai đấy anh."
- Turn 2, 7.3–12.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Con trai à? Giỏi! Anh đặt tên luôn là Đại Phát, lớn lên làm giám đốc, đẹp trai giống bố."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the refrigerator humming, a soft gasp, a short proud laugh. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 3 (`canh-12/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A luxury high-rise apartment in the morning: a white marble kitchen island, a pale sofa, floor-to-ceiling windows over the city, glossy cold light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy sets the test stick down on the marble and lets her smile fade, laying her hand flat on the island, while @Tung still beams at her, both of them with their mouths closed.
- 3.0–7.0s: @Vy speaks firmly to @Tung in a soft voice with a hard gaze, one red fingertip tapping the marble island in a steady rhythm, while he listens with his mouth closed.
- 7.0–11.0s: @Vy finishes and closes her lips, and @Tung pats his own chest with an open palm and answers at once without a pause, his face and lips clearly visible.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, chin lifted like a statue of himself, while @Vy lets a slow sweet closed smile spread back across her red lips. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.3s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Đại Phát nhà mình không thể không có danh phận. Anh ly hôn đi, rồi sang tên căn nhà cho con."
- Turn 2, 8.8–13.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Được, tuần này anh ly hôn. Nhà phố cổ anh sang tên cho em luôn, giám đốc nói là làm."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a fingernail tapping marble, the air conditioner humming. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 4 (`canh-12/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A luxury high-rise apartment in the morning: a white marble kitchen island, a pale sofa, floor-to-ceiling windows over the city, glossy cold light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot by the window, slow push-in onto her face; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy steps around the marble island and leans her head on @Tung's shoulder, her face turned toward the camera, both of them with their mouths closed in the glossy cold light.
- 3.0–7.0s: @Tung speaks tenderly to @Vy with his hand over hers, gazing out at the city skyline, while she listens on his shoulder with a sweet closed smile.
- 7.0–11.0s: @Tung finishes and closes his mouth, and @Vy answers sweetly, then turns her face away from him toward the camera and mutters the rest under her breath, her red lips clearly visible.
- 11.0–15.0s: @Vy finishes muttering and closes her lips into a cold little smirk, rolling her winged eyes, while @Tung keeps gazing out of the window with a proud closed smile, noticing nothing. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Từ giờ em cứ nghỉ ngơi, đừng tự tay nấu cơm nữa kẻo mệt con anh."
- Turn 2, 7.5–12.0s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Vâng, em nghe anh. Mà trước giờ toàn cơm quán dưới sảnh, em có nấu bữa nào đâu."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint city hum, a slow exhale, the air conditioner whispering. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 1 (`canh-13/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot from the kitchen toward the front door, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The ground-floor kitchen of the tube house in soft afternoon light, the big aluminum sticky-rice steamer on the gas stove, the steep tiled staircase on the right and the front door open.
- 3.0–7.0s: @Vy steps in through the front door in her crimson dress with a wicker basket of fruit and calls out sweetly, while @Thu turns from the stove holding a dish towel, mouth closed.
- 7.0–11.0s: @Vy finishes and closes her lips, and @Thu stays by the stove drying a bowl with the dish towel and answers her evenly with a calm half-smile, her face and lips clearly visible.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, setting the dry bowl down neatly, while @Vy's smile stiffens and she lowers the fruit basket onto the wooden dining table. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Chị Thu ơi, em mang ít hoa quả sang chào chị cả đây, toàn quả nhập khẩu đấy chị."
- Turn 2, 8.3–13.1s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Cảm ơn cô. Nhưng nhà này không có chị cả, chỉ có chủ nhà với khách không mời thôi."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the alley outside, high heels on tiles, a wicker basket set down on wood. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 2 (`canh-13/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot across the kitchen, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy turns slowly in the middle of the kitchen, eyeing the walls and the staircase like a buyer at a viewing, while @Thu stands by the stove with the dish towel, both mouths closed.
- 3.0–7.0s: @Vy sweeps one manicured hand across the stove and the steamer as if erasing them and speaks with a sweet smirk, while @Thu listens several steps away with her mouth closed.
- 7.0–11.0s: @Vy finishes and closes her lips, and @Thu folds the dish towel in her hands and answers in a light, pleasant tone with a calm half-smile, her face and lips clearly visible.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth and turns back to the stove, while @Vy's sweeping hand slowly drops to her side and her red lips press into a thin line. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.5s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Căn bếp này em sẽ cho dỡ đi làm quầy rượu, mùi xôi ám hết cả tường rồi."
- Turn 2, 8.0–12.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Cô cứ vẽ tiếp đi, đẹp lắm. Chỉ thiếu mỗi cái sổ đỏ đứng tên cô thôi."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a dripping tap, a car engine pulling into the alley outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 3 (`canh-13/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot from the kitchen corner, slow pull-back from the fruit basket to reveal the staircase and the stove; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A close view of the wicker fruit basket on the wooden dining table in the quiet afternoon kitchen, sunlight from the open front door lying across the tiles beyond it.
- 3.0–7.0s: As the camera pulls back, @Vy is revealed already seated on the bottom stair, one hand holding her ankle and one on her flat stomach, wailing toward the front door, nobody near her.
- 7.0–11.0s: @Vy finishes and closes her lips, and far across the kitchen by the stove, @Thu stands holding a dish towel in both hands and answers in a dry steady voice, lips clearly visible.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, holding up the dish towel at arm's length as proof, while @Vy peeks toward the front door from under her lashes with her lips shut. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.0s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Ối đau quá, chị Thu ơi sao chị nỡ làm thế với em, anh Tùng ơi cứu con em với!"
- Turn 2, 8.5–13.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Cô diễn thì diễn cho khéo. Tôi đứng cách cô ba mét, tay còn cầm cái khăn lau bát đây này."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a car door closing outside, the front gate creaking open, a dripping tap. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 4 (`canh-13/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot from beside the stove, slow tilt up toward the high kitchen shelf; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The bright front doorway of the tube house with the alley beyond, dust floating in the afternoon light and the steel gate standing half open.
- 3.0–7.0s: @Tung strides in through the doorway in his charcoal suit, stops several steps away and points across the kitchen at @Thu, shouting, while she stands by the stove, mouth closed.
- 7.0–11.0s: @Tung finishes and closes his mouth, and @Thu keeps her hands still on the towel and answers in a low steady voice, glancing up once toward the high kitchen shelf, lips clearly visible.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, and the camera tilts up past her to the small white home camera on the high kitchen shelf, its tiny green light blinking steadily. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Cô làm gì cô ấy thế hả? Cô ấy đang mang thai Đại Phát của tôi đấy!"
- Turn 2, 7.8–12.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Tôi không hề chạm vào cô ta. Anh không tin thì có trời biết, đất biết, và có người biết."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the front gate clanging open, quick footsteps on tiles, a faint electronic beep. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 1 (`canh-14/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot across the dining table, slow dolly across; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Morning light lies across the bare wooden dining table where a few pages with only faint unreadable lines of ink rest beside a cheap ballpoint pen, empty cardboard boxes stacked by the wall.
- 3.0–7.0s: @Tung steps up to the table in his charcoal suit, taps the pages with one finger and speaks in a lofty businesslike tone, while @Thu sits on a low stool with her mouth closed.
- 7.0–11.0s: @Tung finishes and closes his mouth, and @Thu picks up the pen, signs in one quick stroke without reading and answers him calmly with a dry half-smile, her face and lips clearly visible.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, sliding the signed pages back across the table, while @Tung blinks down at them with his lips pressed shut and his finger still hovering in the air. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Đơn tôi soạn sẵn rồi, luật sư giỏi nhất Hà Nội đấy. Cô ký vào đây cho xong."
- Turn 2, 8.0–13.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Em ký đây. Nhà cửa em không lấy, chỉ xin nuôi con Na. Anh thuê luật sư giỏi thế, phí tiền quá."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a moped passing outside, paper rustling, a pen scratching on paper. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 2 (`canh-14/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot, slow rack focus from his face to hers; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung folds the signed pages into his inside jacket pocket and checks his gold wristwatch, while @Thu rises from the stool and smooths her apron, both of them with their mouths closed.
- 3.0–7.0s: @Tung speaks curtly to @Thu with his chin up, tugging his cuffs straight, while she listens with her lips pressed shut and her hands folded in front of her apron.
- 7.0–11.0s: @Tung finishes and closes his mouth, and @Thu answers him in a helpful matter-of-fact tone as if passing on a recipe, counting each item on her fingers, her face and lips clearly visible.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth with a calm half-smile and turns away, while @Tung stands frozen with his eyebrows jumping up and his lips pressed shut. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–6.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Cô còn gì muốn nói thì nói nốt đi, tôi còn đi họp."
- Turn 2, 6.8–12.6s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "À, em để lại tờ giấy dặn cô ấy trên kệ bếp rồi: anh ngáy to, dị ứng tôm, tất vứt khắp nhà."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper rustling, a car horn in the alley, a stool scraping on tiles. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 3 (`canh-14/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot toward the front door, slow pan from the stairs to the doorway; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The front doorway of the tube house in morning light, two packed cloth bags and a rolled straw mat waiting on the threshold beside the steep tiled staircase.
- 3.0–7.0s: @Na stands by the packed bags in her school clothes and looks up at @BaNhan coming down the last stairs with an old rattan basket on her arm, asking her, lips clearly visible.
- 7.0–11.0s: @Na finishes and closes her mouth, and @BaNhan stops on the bottom step, leans on her bamboo walking stick and answers in a dry deadpan, her wrinkled face and lips clearly visible.
- 11.0–15.0s: @BaNhan finishes speaking and closes her mouth, hooks the rattan basket higher on her arm and takes @Na's small hand, the two of them marching toward the bright alley with their chins raised. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter): "Bà ơi, bà xách làn đi đâu thế ạ? Sáng nay bà đi chợ sớm à?"
- Turn 2, 7.8–13.1s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Chợ gì. Bà đi theo mẹ cháu chứ đi đâu. Ở lại đây làm mẹ chồng kế toán Tuấn à?"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: slow footsteps on the stairs, a walking stick tapping on tiles, the alley waking up. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 4 (`canh-14/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide shot from the foot of the stairs toward the front door, slow push-in on him; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The bright front doorway seen from inside the house, a strip of morning sun across the tiled floor, the cold stove and the sticky-rice steamer with no steam in the foreground.
- 3.0–7.0s: @BaNhan stands in the doorway with her rattan basket and bamboo stick and speaks in profile without looking at @Tung, chin high, while he stands a few steps away, mouth closed.
- 7.0–11.0s: @BaNhan finishes, closes her mouth and steps out into the alley, and @Tung, left alone, looks slowly around the bare kitchen and mutters to himself, his face and lips clearly visible.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, lifts the lid of the cold empty rice pot on the stove and stares down into it, the open front door bright and empty behind him. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Nhà to này mày cứ giữ. Mẹ chỉ mang theo cái gậy, cái làn, với đứa con dâu."
- Turn 2, 8.3–12.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Đi hết càng tốt, nhà cửa yên tĩnh, mà sao vắng thế nhỉ? Tối nay ai nấu cơm?"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a walking stick tapping away down the alley, a rooster far away, a pot lid clinking in the silence. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 1 (`canh-15/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A tiny rented room in a crowded Hà Nội boarding alley at night: a single wooden bed, a folding table, a small barred window, a hot plate, an aluminum basin catching drips from the leaking ceiling, a bare yellow bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide shot from the doorway, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A tiny rented room at night under a bare yellow bulb, a single wooden bed against the wall and rain dripping from a dark ceiling stain into an aluminum basin.
- 3.0–7.0s: @Na steps in hugging a small cloth bag, stretches both arms out between the bed and the wall and speaks to @Thu, while @Thu sets down the sticky-rice steamer with her mouth closed.
- 7.0–11.0s: @Na finishes and closes her mouth, and @Thu nudges the aluminum basin under the drip with her foot, cocks her head at the dripping sound and answers warmly with a playful half-smile.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, tapping a spoon on the basin rim in time with the drops, while @Na grins at her with a closed mouth and sways along to the rhythm. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter): "Mẹ ơi, phòng mình bé thế, con nằm xoay người một cái là chạm tường rồi."
- Turn 2, 7.8–12.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Bé thì ấm con ạ. Mưa dột thì có cái chậu, coi như nhà mình có nhạc sống miễn phí."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain on a tin roof, water dripping into a metal basin, a spoon tinkling on a metal rim. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 2 (`canh-15/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A tiny rented room in a crowded Hà Nội boarding alley at night: a single wooden bed, a folding table, a small barred window, a hot plate, an aluminum basin catching drips from the leaking ceiling, a bare yellow bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot beside the bed, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The edge of the wooden bed under the bare yellow bulb, a small knotted handkerchief bundle resting on the thin blanket, rain dripping into the basin beyond.
- 3.0–7.0s: @BaNhan sits on the bed, unknots the handkerchief to show a few small gold rings and speaks to @Thu with a sly deadpan look, while @Thu kneels beside the bed, mouth closed.
- 7.0–11.0s: @BaNhan finishes and closes her mouth, and @Thu takes the bundle in both rough palms, bows her head slightly and answers with a warm smile, her face and lips clearly visible.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, while @BaNhan gives one brisk businesslike nod as if sealing a deal and pats the back of @Thu's hands, both smiling with closed lips. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–9.1s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Mẹ giấu ít vàng kỹ đến mức thằng Tùng chưa tìm thấy bao giờ. Cầm lấy mở quán, coi như mẹ đầu tư."
- Turn 2, 9.6–13.9s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Mẹ đầu tư vào con thì con không để mẹ lỗ đâu, lãi con trả bằng xôi."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain on the roof, the basin dripping, a cloth bundle rustling, gold rings clinking softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 3 (`canh-15/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A tiny rented room in a crowded Hà Nội boarding alley at night: a single wooden bed, a folding table, a small barred window, a hot plate, an aluminum basin catching drips from the leaking ceiling, a bare yellow bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow tilt up from the crayon drawing to her face; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The folding table under the bare yellow bulb, a crayon drawing of three figures holding hands and one tiny figure in the far corner, with no words anywhere on the page.
- 3.0–7.0s: @Na sits at the folding table in her school clothes, touching each of the three figures with a red crayon and whispering to herself, her face and lips clearly visible under the yellow bulb.
- 7.0–11.0s: @Na moves the crayon to the tiny figure in the corner and keeps whispering, her lips clearly visible and her brow furrowed as she studies how small it is.
- 11.0–15.0s: @Na finishes whispering and closes her mouth, then slowly adds a little red heart beside the tiny figure in the corner and looks at it with a small closed-mouth pout. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.0s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Đây là bà, đây là mẹ, đây là con, ba người nắm tay nhau thật chặt. Còn bố thì con vẽ bé tí tẹo ở góc giấy, vì dạo này bố ở xa lắm." (no subtitles)
- From 3.0s onward, @Na's face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a crayon scratching on paper, rain on the roof, the basin dripping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 4 (`canh-15/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A tiny rented room in a crowded Hà Nội boarding alley at night: a single wooden bed, a folding table, a small barred window, a hot plate, an aluminum basin catching drips from the leaking ceiling, a bare yellow bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot from above the straw mat, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Faint streetlight from the small barred window lies across a straw mat and a thin blanket on the floor of the dark room, the bare bulb switched off and rain softening outside.
- 3.0–7.0s: @Na lies on the straw mat beside @Thu under the thin blanket, both fully clothed, and whispers up to her mother sleepily, her lips visible in the streetlight, while @Thu keeps her mouth closed.
- 7.0–11.0s: @Na finishes and closes her mouth, and @Thu strokes her hair and whispers back with a faint smile, her face and lips visible in the streetlight, while @Na's sleepy eyes crinkle.
- 11.0–15.0s: @Thu finishes whispering and closes her mouth and eyes, and mother and daughter sink into a deep sleep with slow even breathing, @Thu's hand resting open on the blanket. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–6.7s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter): "Mẹ ơi, thế từ nay mẹ không phải thức chờ bố về nữa ạ?"
- Turn 2, 7.2–12.7s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Ừ, không chờ ai nữa. Mẹ con mình ngủ sớm, sáng mai còn khai trương gánh xôi mới, bà làm cổ đông."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: light rain, slow steady breathing, a distant moped. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 1 (`canh-16/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot of the remodelled kitchen, slow push-in toward her; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The ground-floor kitchen remodelled, a new dark-wood bar counter where the steamer used to stand, deep red velvet curtains over the window, a small folded note propped against a wine bottle.
- 3.0–7.0s: @Vy in her crimson dress unfolds the small note, the paper showing only faint unreadable lines, and reads it aloud in a mocking sing-song voice, her face and red lips clearly visible.
- 7.0–11.0s: @Vy scoffs, crumples the note in one hand and keeps talking, then stops short as her eyes drop to a bar stool where a crumpled grey man's sock lies draped over the velvet seat.
- 11.0–15.0s: @Vy finishes speaking and closes her red lips, holding the grey sock up between two fingertips at arm's length, her nose wrinkled and her winged eyes narrowed. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.3s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Gửi người đến sau: anh ấy ngáy to, dị ứng tôm, tất vứt khắp nhà. Chúc em may mắn nhé. Hừ, bà bán xôi này chọc mình đấy à, ơ, tất thật này!" (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper rustling, a scoff, high heels shifting on tiles, a loud snore rumbling down the staircase from upstairs. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 2 (`canh-16/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot across the white desk, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The large white desk in the glass office, a thin stack of documents with only faint unreadable lines and a gold pen laid neatly on top, the city skyline beyond the windows.
- 3.0–7.0s: @Vy leans over the desk beside @Tung's black leather chair, slides the documents toward him and speaks sweetly, tapping the page with a red fingernail, while he keeps his mouth closed.
- 7.0–11.0s: @Vy finishes and closes her lips, and @Tung uncaps the gold pen with a grand flourish and answers her airily as he signs page after page without looking down, his face and lips clearly visible.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, leaning back in the black leather chair with both hands behind his head, while @Vy gathers the signed stack with a sweet closed smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–6.8s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Anh ký vào giấy ủy quyền này, để em lo hết giấy tờ cho con."
- Turn 2, 7.3–12.1s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Em lo thì anh yên tâm. Giám đốc ký thì cần gì đọc, đọc là việc của thư ký."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: papers sliding on a desk, a pen scratching quickly, the air conditioner humming. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 3 (`canh-16/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 100mm extreme close-up, slow tilt up from the folder to her lips and eyes; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The signed documents lying on the white desk, faint unreadable lines of ink and a fresh dark scrawl at the bottom of the page, the capped gold pen beside them.
- 3.0–7.0s: @Vy's red-nailed fingers close a slim white folder over the documents and lift it to her chest as she whispers to herself, her red lips moving clearly in the frame.
- 7.0–11.0s: The camera rises to @Vy's face as she keeps whispering above the white folder, her red lips clearly visible and her sharp winged eyes flicking toward the office door.
- 11.0–15.0s: @Vy finishes whispering and her red lips close and curl into a cold smile, and she gives the white folder two little pats like a pet, her winged eyes narrowing. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.0s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Một chữ ký thôi mà cả công ty lẫn căn nhà phố cổ. Đàn ông mê gái có bao giờ đọc chữ nhỏ. Lão bảo đọc là việc của thư ký, thì thư ký lấy luôn." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a folder snapping shut, the air conditioner humming, distant city traffic. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 4 (`canh-16/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a black luxury sedan with no badge parked in a dim underground car park, the elevator doors glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot through the windshield, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Through the windshield of a black luxury sedan with no badge parked in a dim underground car park, the dark leather front seats, concrete pillars and the elevator doors glowing in the distance.
- 3.0–7.0s: @Khai sits behind the wheel drumming his fingers, and as @Vy slides into the passenger seat with a slim white folder, he turns to her with a sly grin and speaks, her lips closed.
- 7.0–11.0s: @Khai finishes and closes his mouth, and @Vy answers him in a cool dry voice without looking at him, tapping the folder on her knee, her face and red lips clearly visible.
- 11.0–15.0s: @Vy finishes speaking and closes her lips, and @Khai pats his shirt pocket, then both trouser pockets, his sly grin turning sheepish, while @Vy rolls her eyes toward the car roof. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Xong chưa em? Ba tháng nữa mình rút sạch tiền, bay sang nước ngoài sống như vua."
- Turn 2, 7.8–12.8s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Xong rồi. Vua thì vua, nhưng lần này anh tự trả tiền gửi xe nhé, đừng có lại quên ví."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: fingers drumming on leather, a car door shutting, hands patting empty pockets, an echoing car park. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 1 (`canh-17/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot from the pavement, slow crane down to the shop doorway; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A dark old-quarter street before dawn, yellow streetlamps on mossy walls as warm light and thick steam spill from the small sticky-rice shop across the empty wet pavement.
- 3.0–7.0s: @Thu lifts a big steamer lid behind the counter and speaks over her shoulder to @BaNhan, who comes in from the back with her carved bamboo walking stick and listens with her mouth closed.
- 7.0–11.0s: @Thu finishes and closes her mouth, and @BaNhan answers her with a flat deadpan face, slowly lifting her walking stick to point at the open doorway, her lips clearly visible.
- 11.0–15.0s: @BaNhan finishes speaking and closes her mouth, still pointing her stick at the doorway, as @Thu leans over the counter to peek outside and breaks into a calm half-smile in the golden steam. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Mẹ ơi, trời còn tối om, mẹ ra đây làm gì, giờ này đã có ai mua đâu."
- Turn 2, 8.0–13.6s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Chưa có ai à? Con ngó ra cửa mà xem, hàng còn dài hơn mua vé tàu về quê ăn Tết."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing from big pots, a walking stick tapping the tiled floor, a rooster crowing far down the alley. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 2 (`canh-17/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- Extra: a long queue of office workers and students waiting under the streetlamps, with a plump man in a business suit trying to step in at its front
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot down the queue, slow tracking alongside Na in the foreground; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The old-quarter pavement in front of the glowing shop, parked mopeds lining the curb under yellow streetlamps and the first pale blue light rising above the tiled rooftops.
- 3.0–7.0s: @Na steps out in front of the plump man in a business suit as he edges toward the counter, raises one small palm like a traffic warden and speaks up at him, her lips visible.
- 7.0–11.0s: @Na keeps speaking with a serious little frown, pointing her other hand all the way down the long queue toward the corner, while the plump man blinks down at her with his mouth closed.
- 11.0–15.0s: @Na finishes speaking and closes her mouth, folding her arms over her red scarf, as the plump man turns around and trudges off toward the far end of the queue. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.0s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chú ơi, chú ra cuối hàng xếp giúp cháu với ạ. Chú là giám đốc ạ? Không sao đâu chú, mẹ cháu bảo rồi, ai cũng như ai, giám đốc cũng phải xếp hàng." (no subtitles)
- From 3.0s onward, @Na's face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: shuffling footsteps, a few chuckles along the queue, mopeds puttering far down the street, steam hissing from the shop. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 3 (`canh-17/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot from table height, slow lateral slide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A low wooden table at the back of the shop piled with fresh green banana leaves, a bundle of bamboo strings and two small stools in warm lamplight.
- 3.0–7.0s: The camera slides to @Na kneeling on a stool and holding up a glowing phone, screen turned away from the camera, as she speaks to @BaNhan, who folds a banana leaf with her mouth closed.
- 7.0–11.0s: @Na finishes and closes her mouth, and @BaNhan answers her with a dry deadpan face while knotting a bamboo string tight around a parcel, her wrinkled face and lips clearly visible.
- 11.0–15.0s: @BaNhan finishes speaking and closes her mouth with a sly little smile, tapping one finger on the table, as @Na slowly lowers the glowing phone and stares up at her with round eyes. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.0s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter): "Bà ơi, cái camera nhà cũ vẫn lưu hết video trong máy mẹ đấy ạ."
- Turn 2, 7.5–12.5s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Cứ giữ đấy. Bố cháu đang mê, gửi cũng chẳng xem. Đợi nó ngã đau, bà gửi làm quà."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: banana leaves crinkling, a bamboo string tightening, steam hissing in the background. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 4 (`canh-17/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- Extra: a few customers holding banana-leaf parcels
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot from the pavement facing the counter, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The worn wooden counter with an empty steaming pot and a few last banana-leaf parcels, warm yellow light falling across the wet pavement as the sky turns pale blue.
- 3.0–7.0s: @Thu leans over the counter and calls out warmly to the few customers holding banana-leaf parcels, tilting the empty pot toward them to show its bare shiny bottom, her lips clearly visible.
- 7.0–11.0s: @Thu keeps speaking with a bright smile and presses her palms together in a small apologetic bow, as the customers laugh and nod on the pavement.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, raising one eyebrow with a calm dry half-smile, then sets the empty pot down on the counter in the first light of dawn. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Hết xôi rồi cả nhà ơi! Mai mọi người đến sớm nhé, em để phần cho. Ai ở xa cứ gọi, em giao tận nơi, cả phố cổ em giao hết, chỉ trừ đúng một nhà: nhà chồng cũ." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a ladle tapping the empty pot, customers laughing, distant mopeds passing, birds waking in the alley. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 1 (`canh-18/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot of the office, slow dolly in toward the desk; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The glass-walled director's office in cold morning light, loose papers covered in faint unreadable lines scattered across the large white desk beside the architectural model of a residential tower.
- 3.0–7.0s: @Tung strides in from the door with his phone pressed to his ear, its screen turned away, and speaks sharply into it, his face and lips clearly visible.
- 7.0–11.0s: @Tung keeps speaking as he paces behind the desk, then lowers the phone and stares at it, his eyebrows climbing high, as the call goes dead in his hand.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, then turns to the window, straightens his tie in his own reflection on the glass and smooths his gelled hair with one palm. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Sao lại hủy hợp đồng? Tuần này ba bên hủy rồi đấy! Anh nói rõ lý do cho tôi... Alo? Alo? Lại dập máy. Giám đốc gì mà bị dập máy như nhân viên bán bảo hiểm thế này?" (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: air conditioning hum, a call clicking dead, a flat dial tone, a distant phone ringing unanswered. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 2 (`canh-18/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- Extra: a middle-aged woman accountant in a grey cardigan holding a folder
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder shot from behind the accountant onto Tùng, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The large white desk with a black leather chair, a closed laptop and a framed family photo of Thu, Tùng and Na lying face down beside a thick folder.
- 3.0–7.0s: @Tung sits in the black leather chair, flips open the thick folder the accountant has set before him and speaks up at her sharply, his face and lips clearly visible.
- 7.0–11.0s: @Tung keeps speaking as he leans in over the pages of faint unreadable figures, while the accountant silently holds up four fingers with a flat face.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, sinking back into the black leather chair as it rolls slowly away from the desk, his arms hanging limp over the armrests. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chị nói gì? Tài khoản công ty còn đúng bốn trăm nghìn? Bốn trăm nghìn đồng á? Chị kiểm tra lại xem, tiền đâu hết cả rồi? Từng ấy còn chưa đủ mua hai suất cơm quán dưới sảnh!" (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a folder flipping open, paper rustling, a leather chair creaking, chair wheels rolling across the floor. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 3 (`canh-18/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow rack focus from the transfer slips to his face; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A stack of transfer slips on the white desk in sharp focus, each covered in faint unreadable lines with the same blue ink scrawl at the bottom.
- 3.0–7.0s: Focus racks to @Tung leaning over the desk behind the slips, sliding a finger from one blue scrawl to the next as he mutters to himself, his face and lips clearly visible.
- 7.0–11.0s: @Tung keeps speaking as he presses his phone to his ear, its softly glowing screen turned away from the camera, and flatly repeats the recorded message word by word.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, lowers the phone and lays his forehead down on the stack of slips with a long sigh in the cold office light. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Lệnh chuyển tiền nào cũng có chữ ký ủy quyền của Vy. Vy ơi, nghe máy đi em... Thuê bao quý khách vừa gọi tạm thời không liên lạc được. Đến cái tổng đài cũng chán mình." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper rustling, a phone ringing out, a flat automated tone, a long sigh. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 4 (`canh-18/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Dusk on a busy Hà Nội street, rush-hour mopeds, neon shop lights flickering on.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium tracking shot along the pavement; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A busy Hà Nội street at dusk, rush-hour mopeds streaming past far beyond a row of parked bikes, neon shop lights with no letters flickering on above the empty pavement.
- 3.0–7.0s: @Tung walks slowly into frame along the pavement in his charcoal-grey suit, his collar askew, muttering to himself with his face and lips clearly visible.
- 7.0–11.0s: @Tung keeps speaking as he stops at a dark shop window, squares his shoulders and straightens his collar in his own reflection, lifting his chin.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth with a firm little nod, turning into a narrow side alley as thunder rumbles and the first fat raindrops darken his shoulders. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mất công ty, mất tiền, mất cả Vy. Không sao, giám đốc thì phải bản lĩnh. Thôi về nhà ngủ một giấc, ít ra mình vẫn còn căn nhà trong ngõ cũ. Nhà thì ai lấy được." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rush-hour traffic roaring in the distance, horns, a buzzing neon tube, thunder rumbling, the first drops of rain. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 1 (`canh-19/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Rainy night on the pavement outside an upscale café, warm light glowing through tall rain-streaked windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot along the wet pavement, slow push-in toward the glowing window; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Rain falls through the yellow glow of a streetlamp onto the empty wet pavement outside an upscale café, warm light glowing through its tall rain-streaked windows.
- 3.0–7.0s: @Tung walks into frame in his soaked charcoal-grey suit, stops in front of the glowing window and murmurs to himself, rain running down his face and his lips clearly visible.
- 7.0–11.0s: @Tung keeps speaking as he cups both hands around his eyes against the streaming glass and peers inside, his breath fogging the pane.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, glances down at his own round belly and then back at the glass, blinking hard in the pouring rain. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–11.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cả ngày gọi không nghe máy, hóa ra ngồi đây. Kia rồi, Vy với thằng nào mà ngồi sát rạt thế? Mà khoan, bầu mấy tháng rồi, sao bụng vẫn phẳng lì như cái thớt?" (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steady rain on the pavement, water gurgling in a gutter, distant thunder. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 2 (`canh-19/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
An upscale café at night: velvet armchairs, brass lamps, marble tables, rain-streaked floor-to-ceiling windows facing the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot past the brass lamps, slow lateral slide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A corner table of the upscale café, a marble top with two tall glasses of fruit juice, brass lamps glowing and rain streaking the window behind.
- 3.0–7.0s: @Khai lounges in a velvet armchair beside @Vy, swirls his glass and speaks with a lazy sly grin, while @Vy rests her head on his shoulder and listens with her mouth closed.
- 7.0–11.0s: @Khai finishes and closes his mouth, and @Vy lifts her head and answers him with a sweet smile that curls into a cold smirk, her red lips clearly visible, one hand patting her flat stomach.
- 11.0–15.0s: @Vy finishes speaking and closes her mouth as they clink glasses, both grinning widely, her small white handbag resting on the marble table beside them. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Tội lão Tùng, mất sạch cơ nghiệp mà vẫn đinh ninh sắp có thằng con trai tên Đại Phát."
- Turn 2, 8.3–12.3s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Sáng mai mình bay rồi. Còn thằng Đại Phát của lão á? Đại bại thì có."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: glasses clinking, soft rain on the window, a coffee machine hissing, a low chuckle. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 3 (`canh-19/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
An upscale café at night: velvet armchairs, brass lamps, marble tables, rain-streaked floor-to-ceiling windows facing the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide two-shot of the corner table, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Rain streaks down the café window beside a marble table where an empty velvet armchair stands pulled back and a half-finished glass of juice waits under a glowing brass lamp.
- 3.0–7.0s: The camera reveals @Vy seated alone in her velvet armchair as @Tung walks up dripping wet and speaks hoarsely down at her, while she listens with her mouth closed and a bored look.
- 7.0–11.0s: @Tung finishes and closes his mouth, and @Vy leans back, crosses her legs and answers him lightly and sharply, tapping her flat stomach with red-nailed fingertips, her lips clearly visible.
- 11.0–15.0s: @Vy finishes speaking and closes her mouth with a slow mocking half-smile, while @Tung stands frozen and dripping an arm's length from the table, his mouth hanging open. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–6.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Vy, thằng vừa ngồi đây là ai? Còn con trai của anh đâu?"
- Turn 2, 6.8–12.8s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Con nào hả anh? Que thử thai em mượn của con bạn đang bầu đấy. Anh ngây thơ thật, đến cái que cũng tin."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain dripping from his clothes onto the floor, a hushed café, ice clinking in a glass. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 4 (`canh-19/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
An upscale café at night: velvet armchairs, brass lamps, marble tables, rain-streaked floor-to-ceiling windows facing the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, slow pan following her to the door; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung stands dripping an arm's length from the table with his mouth closed, while @Vy sits back in the velvet armchair with her mouth closed, examining her red fingernails.
- 3.0–7.0s: @Tung speaks hoarsely to @Vy with rain dripping from his chin, while @Vy listens with her mouth closed and a bored look, then rises and slings her small white handbag over her shoulder.
- 7.0–11.0s: @Tung finishes and closes his mouth, and @Vy answers him sweetly and coldly from an arm's length away, nodding down at the two glasses on the table, her red lips clearly visible.
- 11.0–15.0s: @Vy finishes speaking and closes her mouth, gives a tiny wave of her fingers and walks out through the glass door, leaving @Tung alone and dripping beside the table, staring at the two glasses. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–5.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Thế từ đầu đến cuối em chỉ lừa anh thôi à?"
- Turn 2, 6.3–13.1s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Anh tưởng em yêu cái bụng phệ à? Em yêu tiền thôi. À, hai ly nước của em với anh ấy, anh trả nhé, em quên ví."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heels clicking, the café door swinging shut, rain rushing in for a moment. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 1 (`canh-20/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Rainy night in a narrow Hà Nội alley outside a closed steel gate of a tube house, a paper seal stuck across the gate, a single streetlamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot down the alley, slow push-in toward the gate; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A narrow rain-soaked alley at night, a single streetlamp lighting puddles and a closed steel gate with a long paper seal of faint unreadable lines pasted across it.
- 3.0–7.0s: @Tung walks up to the sealed gate in his soaked charcoal-grey suit, stares at the paper seal and speaks hoarsely to himself, his face and lips clearly visible under the streetlamp.
- 7.0–11.0s: @Tung keeps speaking as he lays one palm flat on the wet iron bars beside the seal, then sinks down onto the worn stone doorstep below it.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, sitting hunched on the doorstep with his forearms on his knees and the dark phone in his hand as rain drips from the gate. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Niêm phong? Vy đem nhà đi thế chấp từ bao giờ thế này? Vừa nói nhà thì ai lấy được, thế mà lấy thật. Vợ con, mẹ già, mình tự tay đuổi đi cả rồi, giờ biết gọi ai?" (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heavy rain, water rushing in a gutter, a dog barking far away. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 2 (`canh-20/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Rainy night in a narrow Hà Nội alley outside a closed steel gate of a tube house, a paper seal stuck across the gate, a single streetlamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up from step level, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung sits hunched on the doorstep with his lips pressed shut as the phone in his hand buzzes and lights up, its screen turned away from the camera.
- 3.0–7.0s: @Tung lifts the glowing phone close to his wet face, the screen still turned away from the camera, and speaks quietly to himself with a faint tired smile, his lips clearly visible.
- 7.0–11.0s: @Tung keeps speaking as the smile drops off his face and his eyes narrow, leaning in closer toward the hidden screen with rain running off his nose.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, his eyes wide and unblinking in the cold glow, rain dripping from his hair onto the phone. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mẹ gửi gì đây? Video từ camera bếp nhà mình. Mẹ lại ngồi báo cáo với cái camera như với người ấy... Khoan đã. Vy tự ngồi xuống bậc cầu thang, rồi tự kêu lên à?" (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone buzzing, rain pattering on the phone, thunder rolling far away. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 3 (`canh-20/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Rainy night in a narrow Hà Nội alley outside a closed steel gate of a tube house, a paper seal stuck across the gate, a single streetlamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 100mm extreme close-up on his face, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung lowers the glowing phone onto his knee and stares into the rain-soaked alley, his mouth shut tight and rain running down his cheeks.
- 3.0–7.0s: @Tung speaks hoarsely to himself, his face filling the frame in the cold glow from below, his lips clearly visible and trembling.
- 7.0–11.0s: @Tung keeps speaking as his eyes squeeze shut and his voice breaks, his shoulders starting to shake under the soaked suit.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, pressing the back of his hand against it and bowing his head as the phone's glow fades out below the frame. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thu đứng cách những ba mét, tay còn cầm cái khăn lau bát, đúng như cô ấy nói. Thế mà mình quát vợ ngay giữa bếp, vì một cái que thử thai đi mượn. Thu ơi, anh sai rồi." (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain intensifying, a ragged breath, water dripping from the gate. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 4 (`canh-20/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Grey dawn in the same narrow Hà Nội alley outside the sealed steel gate, the rain easing to a drizzle, the streetlamp still on.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot facing him in the alley, slow crane up; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Grey dawn light creeps into the narrow alley as the rain eases to a fine drizzle, the streetlamp still glowing beside the sealed steel gate.
- 3.0–7.0s: @Tung rises into frame from the doorstep, wipes his face with his sleeve and speaks quietly to himself with a set jaw, his face and lips clearly visible.
- 7.0–11.0s: @Tung keeps speaking as he bends over a puddle, smooths his wet hair in its reflection out of pure habit and buttons his soaked charcoal-grey jacket.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, slips the phone into his pocket and walks away down the wet alley toward the brightening street as the camera rises over the tiled roofs. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Trời sáng rồi. Mất hết rồi thì thôi, nhưng không thể để chúng nó ôm tiền bỏ trốn được. Ra đồn công an thôi. Làm giám đốc thì chưa ra hồn, giờ làm nhân chứng cho ra hồn vậy." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: light drizzle, footsteps on wet concrete, the first moped starting in the distance. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 1 (`canh-21/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A bright modern airport departure hall: polished stone floor, check-in counters, tall glass walls, travelers with suitcases in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot of the hall, slow crane down to the pair; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A bright modern airport departure hall, morning sun pouring through the tall glass walls onto the polished stone floor beside a tall potted areca palm, a white airliner beyond the glass.
- 3.0–7.0s: @Khai in huge dark sunglasses peeks out from behind the potted areca palm and whispers to @Vy, who stands beside the palm with her suitcase and listens with her mouth closed.
- 7.0–11.0s: @Khai finishes and closes his mouth, and @Vy looks him up and down and answers him flatly, pointing one red-nailed finger at his sunglasses, her lips clearly visible.
- 11.0–15.0s: @Vy finishes speaking and closes her mouth, and @Khai slowly lowers the sunglasses down his nose, glances left and right, and steps out from behind the palm with a stiff smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–6.5s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Em đeo kính đen vào đi, cẩn thận kẻo có người nhận ra mình."
- Turn 2, 7.0–12.5s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Đeo kính đen trong nhà lúc tám giờ sáng, anh tưởng không ai nhìn à? Cả sân bay đang nhìn anh đấy."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: airport hall echo, a distant jet engine, suitcase wheels rolling on stone, a soft chime. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 2 (`canh-21/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A bright modern airport departure hall: polished stone floor, check-in counters, tall glass walls, travelers with suitcases in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot tracking alongside them; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Khai and @Vy walk side by side with their suitcases rolling behind them, both mouths closed, the dark sunglasses back on @Khai's nose and a boarding pass trembling in his fingers.
- 3.0–7.0s: @Khai leans toward @Vy and speaks low with a shaky grin, holding the trembling boarding pass out to her, while @Vy listens with her mouth closed and rolls her eyes.
- 7.0–11.0s: @Khai finishes and closes his mouth, and @Vy takes the boarding pass from his fingers and answers him with a cold smirk, her red lips clearly visible.
- 11.0–15.0s: @Vy finishes speaking and closes her mouth, stopping mid-step and staring ahead toward the check-in counters, while @Khai freezes beside her with his mouth falling open below the sunglasses. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.0s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Qua được cửa này là mình giàu cả đời. Mà em cầm hộ anh tấm vé, tay anh run quá."
- Turn 2, 8.5–13.5s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Run gì, lão Tùng giờ đang ngồi khóc ở nhà rồi. Ơ khoan, sao công an đứng ngay quầy kia?"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: suitcase wheels rolling on stone, heels clicking, the wheels stopping, a soft chime echoing in the hall. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 3 (`canh-21/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A bright modern airport departure hall: polished stone floor, check-in counters, tall glass walls, travelers with suitcases in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- Extra: a calm police officer in a dark-green uniform holding a paper with faint unreadable lines
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder shot onto Vy from behind the officer, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The check-in counters in bright morning light, the polished stone floor stretching empty in front of them under the tall glass walls.
- 3.0–7.0s: @Vy stops short with her suitcase as the calm police officer walks up and holds out a paper with faint unreadable lines, and she lifts her chin and speaks sharply, her lips clearly visible.
- 7.0–11.0s: @Vy keeps speaking as her chin sinks a little lower with every sentence and her fingers loosen on the small white handbag, while the officer waits a calm step away.
- 11.0–15.0s: @Vy finishes speaking and closes her mouth, lets out a long breath and holds out both wrists toward the officer of her own accord, the small white handbag sliding down to her elbow. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.3s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Các anh nhầm người rồi, tôi là vợ giám đốc đấy... à, sắp là vợ giám đốc... à mà giám đốc phá sản rồi. Thôi, tôi là ai thì chắc các anh còn biết rõ hơn tôi." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: suitcase wheels stopping, measured footsteps on stone, the hall falling quiet. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 4 (`canh-21/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A bright modern airport departure hall: polished stone floor, check-in counters, tall glass walls, travelers with suitcases in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- Extra: a calm police officer in a dark-green uniform standing a step away from him
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A stretch of polished stone floor near the counters, a hard-shell suitcase standing upright beside a tall potted areca palm in a pool of morning sunlight.
- 3.0–7.0s: @Khai steps out from behind the potted palm the moment the calm police officer walks up, pulls off his dark sunglasses and holds out both wrists at once, speaking fast, his lips clearly visible.
- 7.0–11.0s: @Khai keeps speaking eagerly, counting points off on his fingers one by one, while the police officer stands perfectly still a step away and simply listens.
- 11.0–15.0s: @Khai finishes speaking and closes his mouth, holding out both wrists again with a stiff hopeful smile as a boarding pass with faint unreadable print slips from his shirt pocket onto the stone floor. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.0s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Các anh cứ làm việc, em không chạy đâu, em khai hết: tiền ở tài khoản nào, mật khẩu là gì, ý tưởng là của cô ấy hết, em chỉ là thằng xách vali thôi ạ." (no subtitles)
- From 3.0s onward, @Khai's face and lips stay clearly visible while speaking; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: measured footsteps on stone, a hushed hall, paper landing on stone, a distant jet engine fading. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 1 (`canh-22/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- Extra: a long queue of customers waiting under the streetlamps ahead of him, their backs to the camera
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot down the pavement, slow push-in to the back of the queue; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The old-quarter street before dawn, the sticky-rice shop glowing warm at the far end of a dark wet pavement, steam rising into the lamplight through a light drizzle.
- 3.0–7.0s: @Tung steps into the foreground at the very back of the long queue in his creased charcoal-grey suit and murmurs to himself, rising on tiptoe to see the shop, his lips clearly visible.
- 7.0–11.0s: @Tung keeps speaking under his breath as he straightens his collar and smooths his hair, glancing around at the customers' backs as if waiting to be recognised.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, his shoulders dropping with a small sigh, and shuffles one step forward as the queue inches toward the warm glow of the shop. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Trời ơi, quán Thu đông thật đấy, người xếp hàng kín cả vỉa hè. Ngày xưa vợ bưng xôi tận miệng mình còn chê, giờ đứng cuối hàng, chẳng ai biết mình từng là giám đốc." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: light drizzle, shuffling footsteps, steam hissing far away, a moped passing in the distance. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 2 (`canh-22/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot across the counter, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The worn wooden counter of the shop, banana-leaf parcels stacked beside a steaming pot under a warm bulb, drizzle glittering on the pavement beyond.
- 3.0–7.0s: @Thu looks up from wrapping a parcel as @Tung steps up to the counter in his creased charcoal-grey suit, and she speaks to him evenly while he listens with his mouth closed.
- 7.0–11.0s: @Thu finishes and closes her mouth, and @Tung rests both hands on the edge of the counter and answers her in a cracked, pleading voice, his eyes red-rimmed and his lips clearly visible.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, lowering his gaze to the steaming pot, while @Thu stands still across the counter with one eyebrow raised and the steam drifting between them. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–5.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Anh Tùng? Anh đứng xếp hàng từ bao giờ thế?"
- Turn 2, 6.0–13.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Từ ba giờ sáng em ạ, cả đời anh chưa xếp hàng lâu thế. Thu ơi, anh sai rồi, cho anh về với mẹ con em được không?"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, drizzle on the awning, his unsteady breathing. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 3 (`canh-22/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot across the counter, slow lateral slide; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu silently wraps a fresh scoop of hot sticky rice in a banana leaf and knots a bamboo string around it, her lips pressed together, while @Tung waits across the counter with his mouth closed.
- 3.0–7.0s: @Thu sets the warm parcel on the counter in front of @Tung and speaks to him calmly and evenly, while he listens with his mouth closed.
- 7.0–11.0s: @Thu finishes and closes her mouth, and @Tung lifts the warm parcel, breathes in its steam and answers hoarsely, his lips clearly visible and trembling.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, a tear dropping onto the green banana leaf, while @Thu straightens behind the counter with her hands folded on her dark-green apron. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Gói xôi này em mời anh, còn cơm nhà, chính anh đã tự tay bỏ đi rồi."
- Turn 2, 7.8–12.1s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Vẫn nóng hổi như ngày xưa. Thế mà có thời anh dám chê xôi với chả xôi."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: banana leaf crinkling, steam hissing, drizzle on the awning. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 4 (`canh-22/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot from the pavement, slow crane down; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung stands at the counter hugging the warm parcel to his chest with his mouth closed, while @Thu wipes the worn wooden counter with a cloth, her lips pressed together.
- 3.0–7.0s: @Tung lifts his red-rimmed eyes and speaks softly to @Thu, while she stops wiping and listens with her mouth closed.
- 7.0–11.0s: @Tung finishes and closes his mouth, and @Thu answers him evenly with a calm half-smile, lifting her ladle to point down the pavement toward the far end of the street, her lips clearly visible.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, lifting the lid of a big pot in a cloud of golden steam, while @Tung clutches his parcel and shuffles out of frame down the street. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–5.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Thu ơi, em còn thương anh chút nào không?"
- Turn 2, 5.8–12.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Thương thì còn, nhưng giờ em biết thương mình trước. Muốn ăn nữa thì anh ra cuối hàng, ai cũng như ai, giám đốc cũng phải xếp hàng."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: drizzle, steam rushing from a lifted pot lid, slow shuffling footsteps. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 1 (`canh-23/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Evening on a narrow wooden staircase leading up to a closed door above the sticky-rice shop, warm light under the door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium profile shot across the top landing, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A narrow wooden staircase climbing to a closed door above the sticky-rice shop, a thin strip of warm light glowing underneath it.
- 3.0–7.0s: The door creaks open on @BaNhan, as @Tung on the top step holds up his glowing phone, screen turned away from the camera, and speaks while she listens with her mouth closed.
- 7.0–11.0s: @Tung finishes and closes his mouth, and @BaNhan answers him with a flat deadpan face and her chin lifted, her wrinkled face and lips clearly visible in the warm light.
- 11.0–15.0s: @BaNhan finishes speaking and closes her mouth, pulls a dark phone of her own from her cardigan pocket and waggles it at him, while @Tung stands on the threshold with his mouth hanging open. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Mẹ ơi, video ấy là mẹ gửi ạ? Mẹ biết dùng điện thoại từ bao giờ thế?"
- Turn 2, 7.8–13.1s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Từ hôm mày bỏ vợ. Con dại thì mẹ phải khôn, già cũng phải học cho kịp với cái ác."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: creaking wooden steps, the door creaking open, a walking stick tapping the floor. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 2 (`canh-23/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Evening in a small cozy room above the sticky-rice shop: a low wooden bed, a family altar with incense, a window over the old-quarter street, a warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot across the threshold, slow lateral slide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the cozy room above the shop, a warm lamp glowing and incense smoke curling from the small family altar beside the window over the lit street.
- 3.0–7.0s: The camera slides to @Tung standing just inside the door as he lifts his red-rimmed eyes and speaks to @BaNhan in a low, breaking voice, while she listens with her mouth closed.
- 7.0–11.0s: @Tung finishes and closes his mouth, and @BaNhan folds both hands on top of her bamboo walking stick and answers him firmly and dryly, her lips clearly visible.
- 11.0–15.0s: @BaNhan finishes speaking, closes her mouth and holds up one bony finger for one bowl, while @Tung blinks at the finger and slowly nods in the warm lamplight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Mẹ ơi, con mất hết rồi. Con xin mẹ cho con được làm lại người tử tế."
- Turn 2, 7.8–12.8s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Tử tế thì phải làm cả đời. Mai ra quán rửa bát cho con Thu, lương một bát xôi."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the lamp humming softly, the stick tapping on wood, a moped passing in the street below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 3 (`canh-23/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Evening in a small cozy room above the sticky-rice shop: a low wooden bed, a family altar with incense, a window over the old-quarter street, a warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot at the doorway, slow pull back; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung stands bowed just inside the door with his mouth closed, while @BaNhan studies him for a long moment with her lips pressed into a thin line.
- 3.0–7.0s: @Tung straightens his collar out of habit and asks @BaNhan in a small voice, while she listens with her mouth closed and one eyebrow slowly climbing.
- 7.0–11.0s: @Tung finishes and closes his mouth, and @BaNhan answers him gruffly and deadpan, pointing her walking stick at the door, her wrinkled face and lips clearly visible in the lamplight.
- 11.0–15.0s: @BaNhan finishes speaking and closes her mouth, and @Tung bows very low and backs out through the doorway, leaving @BaNhan alone with her stick in the warm lamplight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Vâng ạ, con đi. Mà mẹ ơi, giám đốc đi rửa bát thì có ai cười không mẹ?"
- Turn 2, 8.0–13.6s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Giám đốc gì nữa con. Từ mai mày là nhân viên rửa bát, năm giờ có mặt, đến muộn trừ xôi."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a deep unsteady breath, the lamp hum, slow footsteps going down wooden stairs. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 4 (`canh-23/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Evening in a small cozy room above the sticky-rice shop: a low wooden bed, a family altar with incense, a window over the old-quarter street, a warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on Bà Nhàn at the altar, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the cozy room, the small family altar glows with incense smoke beside the window over the lit old-quarter street, the wooden door shut.
- 3.0–7.0s: @BaNhan shuffles up to the altar with her bamboo walking stick, lights a fresh stick of incense and speaks to the altar in a brisk reporting tone, her lips clearly visible.
- 7.0–11.0s: @BaNhan keeps speaking as she plants the incense in the bowl and gives a crisp little nod, as if handing in a report, her chin trembling.
- 11.0–15.0s: @BaNhan finishes speaking and closes her mouth, dabs her eyes with the cuff of her brown knitted cardigan, and her wrinkled face softens into a small smile in the warm light. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–13.0s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông nó ơi, cái camera nghỉ hưu rồi, giờ tôi báo cáo với ông: thằng con ông đã chịu cầm giẻ rửa bát. Ông phù hộ cho nó rửa sạch cái bát, rồi rửa sạch cả cái lòng." (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a match flaring, incense crackling softly, a soft sniff. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 1 (`canh-24/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Afternoon in a primary school hall: a small stage with paper flower decorations and colorful bunting, rows of plastic chairs filled with parents.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- Extra: rows of parents seated in plastic chairs below the stage
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot from above the parents' heads, slow crane down to the front edge of the stage; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Colorful bunting and paper flowers strung high across a bright primary school hall in the afternoon, the small decorated stage glowing warm at the far end.
- 3.0–7.0s: @Na marches to the front edge of the stage beating a small red drum, pauses and speaks to herself while scanning the rows of parents below, her lips clearly visible.
- 7.0–11.0s: @Na keeps speaking as she rises on tiptoe and peers toward the back of the hall, her drumsticks frozen in mid-air above the red drum.
- 11.0–15.0s: @Na finishes speaking and closes her mouth, then drums harder and faster than ever with her cheeks puffed out, her bright eyes still searching the rows of parents. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–12.3s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bố có đến không nhỉ? Mẹ bảo bố rửa xong bát sẽ đến mà. Hàng đầu chưa thấy. Bố ơi, con đánh trống to thế này, ngồi hàng nào bố cũng phải nghe thấy chứ!" (no subtitles)
- From 3.0s onward, @Na's face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a small drum tapping a steady march, scattered applause, chairs creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 2 (`canh-24/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Afternoon in a primary school hall: a small stage with paper flower decorations and colorful bunting, rows of plastic chairs filled with parents.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot from the side, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The last row of plastic chairs at the back of the hall, warm light from the high windows falling across one empty seat and a strand of paper flowers.
- 3.0–7.0s: @Tung slips breathless into the empty seat beside @Thu, his suit sleeves rolled up and his hands still wet, and whispers to her, while @Thu listens with her hands folded and her mouth closed.
- 7.0–11.0s: @Tung finishes and closes his mouth, and @Thu answers him dryly without turning her head, her eyes on the stage and a faint half-smile on her lips, clearly visible.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth, and @Tung springs up and waves both damp hands high above his head toward the stage, grinning with his chin trembling. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Anh chạy từ quán sang, tay còn chưa kịp lau. Con có nhìn thấy anh không em?"
- Turn 2, 7.8–12.6s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Con bé tìm anh từ nãy đấy. Anh giơ tay vẫy đi, hôm nay anh không phải họp đâu."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the little drum from the stage, applause swelling, a plastic chair creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 3 (`canh-24/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Backstage corner of the school hall after the show, paper decorations, soft afternoon light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot from child height, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A quiet backstage corner of the school hall, paper flowers and folded bunting piled on a chair in soft afternoon light.
- 3.0–7.0s: @Na runs into frame with her small red drum, sniffs the air near @Tung's rolled-up sleeve with a wrinkled nose and speaks up at him, while he listens with his mouth closed.
- 7.0–11.0s: @Na finishes and closes her mouth, and @Tung kneels down to her eye level in his charcoal-grey suit and answers her with a sheepish grin, holding up his little finger toward her.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth as @Na hooks her little finger around his, the two of them holding the pinky promise between them, both beaming. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.3s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter): "Bố đến thật rồi! Ơ, ngày xưa bố thơm mùi nước hoa, sao giờ bố thơm mùi nước rửa bát?"
- Turn 2, 8.8–13.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Bố hứa, từ nay bố ngồi hàng đầu. Còn mùi ấy là vì bố đang làm thuê cho mẹ con."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: distant applause from the hall, quick small footsteps, paper decorations rustling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 4 (`canh-24/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Backstage corner of the school hall after the show, paper decorations, soft afternoon light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot in the doorway, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A doorway at the edge of the backstage corner, soft afternoon light and a string of paper flowers hanging across it.
- 3.0–7.0s: @Thu stands in the doorway with her hands folded as @Tung stops an arm's length away and speaks to her quietly with his eyebrows lifted, while she listens with her mouth closed.
- 7.0–11.0s: @Tung finishes and closes his mouth, and @Thu answers him evenly and gently, her eyes steady on his face and her lips clearly visible.
- 11.0–15.0s: @Thu finishes speaking and closes her mouth with a calm dry half-smile and turns toward the sound of a small drum, while @Tung glances down at his wrinkled wet fingertips and nods slowly. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–7.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Cảm ơn em đã cho anh đến xem con. Thế là em tha thứ cho anh rồi hả em?"
- Turn 2, 8.3–13.6s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Em tha thứ để con còn có bố, chứ không phải để anh quay lại. Bát thì mai anh vẫn rửa."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft applause fading, a small drum tapping nearby, a breeze through the paper flowers. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 1 (`canh-25/clip-1.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot from the street, slow push-in to the doorway; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The old-quarter street at first light, the sticky-rice shop's warm glow spilling across the pavement and thick steam billowing from a row of big pots behind the worn wooden counter.
- 3.0–7.0s: @BaNhan reaches her walking stick toward a steamer lid to help, and @Thu waves her gently toward a stool and speaks fondly to her, while @BaNhan listens with her mouth closed.
- 7.0–11.0s: @Thu finishes and closes her mouth, turning the glossy rice with a wooden paddle, and @BaNhan sits on the stool and answers her with a lifted chin and a deadpan face, her lips clearly visible.
- 11.0–15.0s: @BaNhan finishes speaking and closes her mouth, giving a firm nod at her own words, as @Thu laughs softly through the rising steam and the first gold sunlight touches the rooftops. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–8.0s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Mẹ ngồi đi, mẻ đầu là mẻ của nhà mình. Tay con vẫn chai, nhưng lòng nhẹ lắm mẹ ạ."
- Turn 2, 8.5–13.3s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Một năm ba cửa hàng mà vẫn tự đồ xôi. Nhà này giờ mới có giám đốc thật."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam roaring, a walking stick tapping the floor, sparrows chirping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 2 (`canh-25/clip-2.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot in the back corner, slow lateral slide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A corner at the back of the shop, a big plastic basin of soapy water and a tall stack of clean bowls on a low stool, steam drifting in from the front.
- 3.0–7.0s: @Tung sits on a low stool in his charcoal-grey suit, sleeves rolled to the elbows and hands in the soapy basin, as @BaNhan stops beside him on her stick and asks him dryly.
- 7.0–11.0s: @BaNhan finishes and closes her mouth, and @Tung looks up at her and answers with a humble grin, lifting a big dripping pot out of the basin, his lips clearly visible.
- 11.0–15.0s: @Tung finishes speaking and closes his mouth, holding the shining pot up like a trophy, as @BaNhan rolls her eyes, then gives a small approving nod and taps her stick once on the floor. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–6.2s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Một năm rửa bát rồi đấy, còn thấy nhục không, giám đốc?"
- Turn 2, 6.7–13.2s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter): "Không mẹ ạ, mỗi cái bát sạch là con trả bớt chút nợ ân tình. Mà con lên chức rồi, giờ con được rửa cả nồi."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water sloshing, bowls clinking, a big pot clanging gently, steam hissing in the background. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 3 (`canh-25/clip-3.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot at a low table, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A low wooden table by the shop counter in golden morning light, a stack of banana leaves and a softly glowing phone lying face down.
- 3.0–7.0s: @BaNhan squints and holds the glowing phone at arm's length, screen turned away from the camera, and speaks to @Na, who listens with her mouth closed.
- 7.0–11.0s: @BaNhan finishes and closes her mouth, and @Na, folding a banana leaf beside her, tilts her head and asks her grandmother innocently, her lips clearly visible.
- 11.0–15.0s: @Na finishes speaking and closes her mouth, blinking up at her grandmother, as @BaNhan freezes, lowers the phone and points her walking stick toward the front counter with a deadpan face. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–9.9s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter): "Báo vừa đưa tin, con Vy với thằng Khải lĩnh án rồi. Đòi bay sang Tây, giờ ngồi bóc lịch. Đấy, cái kết cho tiểu tam."
- Turn 2, 10.4–13.6s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter): "Bà ơi, tiểu tam là gì, có phải bé ba không ạ?"
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning street sounds, steam hissing, a banana leaf crinkling, a stool creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 4 (`canh-25/clip-4.md`)

```markdown
One continuous 15-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Sunrise over the tiled roofs of Hà Nội's old quarter seen from a low drone: golden light, steam rising from the open doorway of a small sticky-rice shop on a corner street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm low drone medium shot at head height facing the doorway, then one slow crane up into a wide aerial over the rooftops; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A low drone hovers at head height before the open golden doorway of the small sticky-rice shop at sunrise, white steam curling out into the morning air beneath the mossy tiled roofs.
- 3.0–7.0s: @Thu steps into the doorway holding @Na's hand, and @Na looks up and asks her mother, while @Thu listens with her mouth closed and the camera holds still at head height.
- 7.0–11.0s: @Na finishes and closes her mouth, and @Thu looks down at her daughter and answers her softly with a calm half-smile, her face and lips clearly visible in the golden light, the camera still holding.
- 11.0–15.0s: @Thu finishes the last words and closes her mouth, and only then the camera cranes slowly up over a sea of mossy tiled roofs, mother and daughter small in the glowing doorway below. The shot settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 3.0–5.9s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter): "Mẹ ơi, sao bố lại bỏ mẹ đi theo cô ấy?"
- Turn 2, 6.4–11.7s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter): "Người ta có thể đi tìm hương lạ, nhưng vợ tào khang thì cả đời chỉ có một thôi con ạ."
- Both keep their mouths closed until 3.0s; then each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft morning wind, distant temple bells, sparrows, the old quarter waking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```
