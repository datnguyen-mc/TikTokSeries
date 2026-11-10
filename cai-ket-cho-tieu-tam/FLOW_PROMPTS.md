# Chính Thất Cao Tay, Tiểu Tam Trắng Tay — Bộ 100 Prompt Google Flow Omni (25 Cảnh × 4 Clips × 15s)

- **Không có người dẫn chuyện:** 100% lời thoại do nhân vật nói trên hình — cả 100 clip là thoại khớp khẩu hình. Giọng gốc của mỗi nhân vật (tuổi, chất giọng, giọng Hà Nội) giữ nguyên văn ở mọi clip để Omni không đổi người nói.
- **Nhịp giọng theo cảnh:** mỗi lượt thoại có nhịp riêng nối sau giọng gốc — **nhanh** (cãi vã, hoảng hốt, rượt đuổi, khoe khoang; tốc độ ×1.2), **vừa** (trò chuyện thường), **chậm** (xúc động, thú nhận, câu chốt lặng người; tốc độ ×0.9). Khung thoại tính theo nhịp nên câu chậm ít chữ hơn. Cả phim: 95 lượt nhanh, 105 lượt vừa, 89 lượt chậm.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 100 clips × 15s, tất cả là clip thoại (5 clip có hai lượt thoại); lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 36 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 64 clip ảnh nhân vật (Ingredients), 0 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** không có clip VO nên runner không tăng tốc giọng clip nào; tốc độ nói nằm trong prompt (nhịp từng lượt) để khớp khẩu hình.
- **Màu phim & ánh sáng:** Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py cai-ket-cho-tieu-tam` sinh lại toàn bộ clip, README, kịch bản.

---

## Cảnh 01 - Clip 1 (`canh-01/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Thu's narrow áo dài tailor shop on an old-quarter silk street by day: bolts of jewel-toned silk stacked on wooden shelves to the ceiling, two headless dress forms in half-finished áo dài, an old black sewing machine on a worn wooden table, a tall standing fitting mirror, a long cutting table with tailor's chalk and paper patterns, a small brass bell above the glass door, soft daylight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the old woman at the cutting table, gentle push-in.
- Shot 2, 5–10s: 85mm close-up of the tailor bent over the sewing machine, locked off.
- Shot 3, 10–13s: 35mm medium two-shot across the shop, slow drift.
- Shot 4, 13–15s: 24mm wide shot of the shop toward the inner staircase, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan stands at the cutting table folding a length of pale silk and is already speaking, dry and half to herself, without looking up.
- 1–2s (Shot 1): @BaNhan keeps talking as she smooths the fold flat with her thin old hands.
- 2–3s (Shot 1): @BaNhan raises one eyebrow toward the sewing machine as she goes on.
- 3–4s (Shot 1): @BaNhan finishes the sentence and lays the folded silk on the pile.
- 4–5s (Shot 1): @BaNhan closes her mouth and waits, holding her bamboo stick.
- 5–6s (CUT to Shot 2): @Thu sits at the sewing machine guiding red silk under the needle and starts answering slowly in a low calm voice, eyes on the needle.
- 6–7s (Shot 2): @Thu keeps speaking evenly, a faint smile at the corner of her mouth.
- 7–8s (Shot 2): @Thu rocks the treadle once as she adds a short last remark.
- 8–9s (Shot 2): @Thu finishes, closes her mouth and keeps sewing.
- 9–10s (Shot 2): The needle stops; @Thu breathes out softly, mouth closed.
- 10–11s (CUT to Shot 3): @BaNhan wags one finger toward @Thu and fires back a quick dry remark with a chuckle.
- 11–12s (Shot 3): @BaNhan keeps talking briskly, eyes twinkling, while @Thu looks up at her, mouth closed.
- 12–13s (Shot 3): @BaNhan finishes her last words and closes her mouth.
- 13–14s (CUT to Shot 4): @BaNhan shuffles toward the narrow inner staircase with her carved bamboo stick, mouth closed.
- 14–15s (Shot 4): @Thu snips the red thread with small shears and smooths the silk, alone at the machine, thoughtful and silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, dry, half to herself): "Thu này, chồng con dạo này đi họp về toàn thơm nước hoa đàn bà đấy nhé."
- Turn 2, 5.4–9.9s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, calm, eyes on the needle): "Đàn ông có tiền thì mũi đàn bà phải thính hơn, mẹ ạ. Mẹ lo gì."
- Turn 3, 10.4–13.7s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking quickly in short lively phrases, every word still clear, a dry chuckle): "Thính thôi chưa đủ đâu, con phải tinh nữa cơ. Mẹ nói thế thôi đấy."
- Pacing: @BaNhan speaks at an even everyday pace, then @Thu answers slowly and calmly, then @BaNhan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the rhythmic clatter of an old treadle sewing machine, rustling silk, motorbikes passing on the street outside, a soft snip of thread. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 2 (`canh-01/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Thu's narrow áo dài tailor shop on an old-quarter silk street by day: bolts of jewel-toned silk stacked on wooden shelves to the ceiling, two headless dress forms in half-finished áo dài, an old black sewing machine on a worn wooden table, a tall standing fitting mirror, a long cutting table with tailor's chalk and paper patterns, a small brass bell above the glass door, soft daylight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium tracking shot following the customer in from the glass door.
- Shot 2, 3–6s: 85mm close-up of the customer by the silk shelves, slow push-in.
- Shot 3, 6–9s: 50mm over-the-shoulder shot from behind the customer onto the tailor.
- Shot 4, 9–15s: 40mm medium two-shot at the cutting table, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): The brass bell jingles as @Vy steps in through the glass door and is already speaking, sweet and a little haughty, looking around.
- 1–2s (Shot 1): @Vy keeps talking as she walks along the bolts of jewel-toned silk, heels clicking on the tiles.
- 2–3s (Shot 1): @Vy runs one hand along a bolt of red silk as she goes on.
- 3–4s (CUT to Shot 2): @Vy stops at the cutting table, finishing her request with a bright smile.
- 4–5s (Shot 2): @Vy closes her mouth and tilts her head, waiting.
- 5–6s (Shot 2): @Thu rises from the sewing machine, watching her, mouth closed.
- 6–7s (CUT to Shot 3): @Thu sets down her chalk and answers politely and evenly.
- 7–8s (Shot 3): @Thu pulls out a wooden stool beside the cutting table as she finishes.
- 8–9s (Shot 3): @Thu closes her mouth and gestures to the stool.
- 9–10s (CUT to Shot 4): @Vy sits down and starts to reply with a small private smile, as if enjoying a joke.
- 10–11s (Shot 4): @Vy keeps talking while she crosses her legs.
- 11–12s (Shot 4): @Vy sets her small white handbag on the cutting table, still talking.
- 12–13s (Shot 4): @Vy finishes and closes her mouth, looking @Thu up and down.
- 13–14s (Shot 4): @Thu picks up a pencil and an order pad, mouth closed.
- 14–15s (Shot 4): @Thu holds the pencil over the pad, waiting, while @Vy smiles without a word. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, sweet and a little haughty): "Chị là chủ tiệm ạ? Em cần may một bộ áo dài cưới, thật đẹp vào, tiền không thành vấn đề."
- Turn 2, 6.2–8.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, polite and even): "Em ngồi đi. Cưới ngày nào để chị xếp lịch?"
- Turn 3, 9.2–13.0s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, coy, enjoying a private joke): "Tháng sau ạ. Chị đo kỹ cho em nhé, em kén lắm, khó chiều lắm."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a brass door bell jingling, street traffic swelling then muffled as the door closes, high heels clicking on tiles, a stool scraping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 3 (`canh-01/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Thu's narrow áo dài tailor shop on an old-quarter silk street by day: bolts of jewel-toned silk stacked on wooden shelves to the ceiling, two headless dress forms in half-finished áo dài, an old black sewing machine on a worn wooden table, a tall standing fitting mirror, a long cutting table with tailor's chalk and paper patterns, a small brass bell above the glass door, soft daylight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot at the cutting table, holding the previous framing.
- Shot 2, 5–10s: 85mm close-up of the tailor, very slow push-in.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the tailor onto the customer.
- Shot 4, 13–15s: 35mm medium two-shot across the cutting table, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy slides a thick red envelope across the cutting table with two fingers and is already speaking slowly and sweetly.
- 1–2s (Shot 1): @Vy keeps speaking, savoring each word, red lips curling, while @Thu's pencil stops on the pad.
- 2–3s (Shot 1): @Vy leans a little closer as she goes on.
- 3–4s (Shot 1): @Vy lands the last words with a satisfied smile.
- 4–5s (Shot 1): @Vy closes her mouth and waits for the reaction, while @Thu stays perfectly still.
- 5–6s (CUT to Shot 2): @Thu lifts her eyes to @Vy and answers in a very quiet, level voice.
- 6–7s (Shot 2): @Thu keeps speaking calmly and taps the pencil on the pad as if taking an ordinary order.
- 7–8s (Shot 2): @Thu asks her last question without any change in her face.
- 8–9s (Shot 2): @Thu closes her mouth and holds @Vy's gaze.
- 9–10s (Shot 2): @Thu waits, breathing slowly, mouth closed.
- 10–11s (CUT to Shot 3): @Vy blinks, her smile frozen, then snaps a quick question.
- 11–12s (Shot 3): @Vy keeps talking fast, leaning in over the table.
- 12–13s (Shot 3): @Vy finishes and closes her mouth, staring.
- 13–14s (CUT to Shot 4): @Thu writes calmly on the order pad without looking up, mouth closed.
- 14–15s (Shot 4): @Vy's fingers tighten on her handbag strap while @Thu reaches for the yellow measuring tape around her neck, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking slowly and softly, unhurried, with a short natural pause between phrases, savoring every word, sweetly cruel): "Chú rể là anh Tùng, giám đốc công ty xây dựng. Chồng của chị đấy, chắc chị biết."
- Turn 2, 5.9–9.8s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, very quiet, perfectly level): "Thế à. Em muốn cổ cao hay cổ thuyền? Lụa tơ tằm hay gấm?"
- Turn 3, 10.3–13.3s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, thrown off, needled): "Chị có nghe rõ em vừa nói gì không đấy? Hay chị điếc thật?"
- Pacing: @Vy speaks slowly and calmly, then @Thu answers slowly and calmly, then @Vy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper sliding across wood, the street muffled behind glass, a clock ticking on the shelf, one slow breath. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 4 (`canh-01/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Thu's narrow áo dài tailor shop on an old-quarter silk street by day: bolts of jewel-toned silk stacked on wooden shelves to the ceiling, two headless dress forms in half-finished áo dài, an old black sewing machine on a worn wooden table, a tall standing fitting mirror, a long cutting table with tailor's chalk and paper patterns, a small brass bell above the glass door, soft daylight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot across the cutting table, holding the previous framing.
- Shot 2, 5–9s: 85mm close-up of the customer, locked off.
- Shot 3, 9–13s: 50mm medium shot beside the tall fitting mirror, slow arc.
- Shot 4, 13–15s: 28mm wide shot of the fitting corner with both women reflected in the mirror.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu stands, unwinds the yellow tailor's measuring tape from her neck and is already speaking slowly and evenly.
- 1–2s (Shot 1): @Thu keeps speaking calmly and points toward the low fitting stand by the mirror.
- 2–3s (Shot 1): @Thu goes on, unhurried, the tape hanging from her fingers.
- 3–4s (Shot 1): @Thu finishes the sentence, while @Vy rises from the stool, mouth closed.
- 4–5s (Shot 1): @Vy steps onto the low fitting stand, mouth closed, as the yellow tape unrolls in @Thu's hand.
- 5–6s (CUT to Shot 2): @Vy blurts a quick reply with a forced laugh, swallowing hard.
- 6–7s (Shot 2): @Vy keeps talking fast, eyes darting to the tape.
- 7–8s (Shot 2): @Vy finishes her question and closes her mouth.
- 8–9s (Shot 2): @Vy glances down at the yellow tape, mouth closed.
- 9–10s (CUT to Shot 3): @Thu holds the yellow measuring tape across the back of @Vy's shoulders and starts reading the numbers aloud in a flat calm voice.
- 10–11s (Shot 3): @Thu keeps talking as she slides the tape down around @Vy's waist.
- 11–12s (Shot 3): @Thu adds a short last word and closes her mouth.
- 12–13s (Shot 3): @Thu lets the tape fall loose and jots on the order pad, mouth closed.
- 13–14s (CUT to Shot 4): @Vy looks at her own reflection in the tall mirror, her smile slipping, mouth closed.
- 14–15s (Shot 4): Both women stand silent in the mirror, the tailor calm, the customer stiff. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, cool and unhurried): "Rõ cả rồi. Giận thì tốn vải lắm em ạ. Đứng thẳng lên, chị đo cho chuẩn."
- Turn 2, 5.7–8.9s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, forcing a laugh, rattled): "Chị bình tĩnh thế, làm em thấy sờ sợ đấy. Chị định làm gì em?"
- Turn 3, 9.4–13.3s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, matter-of-fact, reading the tape): "Vai ba sáu, eo năm tám. Em gầy hơn chị nghĩ. Đứng yên nào."
- Pacing: @Thu speaks slowly and calmly, then @Vy answers quickly, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a stool scraping on tiles, the soft zip of a measuring tape unrolling, silk rustling, the street faint behind the glass. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 1 (`canh-02/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot from the altar side across the round dining table, slow dolly-in.
- Shot 2, 5–10s: 85mm close-up of the mother ladling soup at the table, locked off.
- Shot 3, 10–13s: 50mm medium shot of the girl laying an extra place, slow pan.
- Shot 4, 13–15s: 85mm close-up of the girl turning toward the alley door, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Na stands by the round dining table holding up a school test paper with no readable writing and is already speaking fast, bouncing on her toes, while @Thu comes out of the small kitchen with a steaming pot of soup, mouth closed.
- 1–2s (Shot 1): @Na keeps talking excitedly, waving the paper toward her mother, her pigtails bouncing.
- 2–3s (Shot 1): @Na keeps speaking fast and hugs the test paper to her chest with a wide grin.
- 3–4s (Shot 1): @Na keeps talking, eyes shining, as @Thu sets the pot down in the middle of the table.
- 4–5s (Shot 1): @Na finishes and closes her mouth, and @Thu picks up the ladle and starts answering warmly, a touch too brightly.
- 5–6s (CUT to Shot 2): @Thu keeps speaking as she ladles soup into a bowl, steam rising past her face.
- 6–7s (Shot 2): @Thu keeps talking with a smile a little too wide.
- 7–8s (Shot 2): @Thu keeps speaking evenly, setting the bowl at her daughter's place.
- 8–9s (Shot 2): @Thu keeps talking, her eyes flicking once toward the door to the alley.
- 9–10s (Shot 2): @Thu finishes, closes her mouth and rests the ladle back in the pot.
- 10–11s (CUT to Shot 3): @Na picks up an extra bowl and a pair of chopsticks and chirps a quick eager reply, while @Thu listens with her mouth closed.
- 11–12s (Shot 3): @Na keeps talking fast as she lays the bowl and chopsticks at the empty place beside her own stool.
- 12–13s (Shot 3): @Na keeps speaking eagerly, patting the empty stool beside her.
- 13–14s (CUT to Shot 4): @Na finishes her last words and closes her mouth, turning toward the door to the alley.
- 14–15s (Shot 4): @Na watches the door to the alley with bright, waiting eyes, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, bouncing with excitement): "Mẹ ơi, tối nay bố có về ăn cơm không ạ? Con được điểm mười môn toán đấy!"
- Turn 2, 4.9–9.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, warm, a touch too bright): "Thật à? Giỏi thế. Mẹ nấu toàn món bố thích, có cả canh cua, kiểu gì bố cũng về."
- Turn 3, 10.2–14.0s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, eager, already planning): "Thế con bày thêm bát cho bố nhé, để bố ngồi cạnh con, nghe con kể chuyện!"
- Pacing: @Na speaks quickly, then @Thu answers at an even everyday pace, then @Na answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a pot lid rattling, chopsticks clinking on china bowls, soup bubbling, a moped passing in the alley outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 2 (`canh-02/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium two-shot at the alley doorway as the girl runs to her father, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the father's face lit by his phone, slow pan as he moves.
- Shot 3, 10–13s: 40mm over-the-shoulder shot from behind the father on the staircase down onto the girl.
- Shot 4, 13–15s: 85mm close-up of the girl at the foot of the stairs, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tung steps in from the dark alley loosening his tie, eyes on a phone with a glowing blank screen, as @Na hurries into his path holding up her test paper and is already speaking fast.
- 1–2s (Shot 1): @Na keeps talking fast and beaming, the test paper with no readable writing held high in both hands, while @Tung keeps his mouth closed.
- 2–3s (Shot 1): @Na bounces on her toes and keeps speaking proudly, eyes shining.
- 3–4s (Shot 1): @Na keeps talking and claps the paper between her palms to show the class applauding.
- 4–5s (Shot 1): @Na finishes her last words and closes her mouth, holding the paper up toward @Tung's face, while his eyes stay on the glowing phone.
- 5–6s (CUT to Shot 2): @Tung answers fast without lifting his eyes from the glowing blank screen, his thumb scrolling.
- 6–7s (Shot 2): @Tung keeps talking flatly, the blue-white glow on his face.
- 7–8s (Shot 2): @Tung waves the phone vaguely toward the dining table and keeps speaking, still not looking down.
- 8–9s (Shot 2): @Tung keeps talking as he steps around @Na toward the staircase.
- 9–10s (Shot 2): @Tung keeps speaking over his shoulder, one foot on the bottom stair.
- 10–11s (CUT to Shot 3): @Tung finishes, closes his mouth and starts up the steep tiled stairs, while @Na turns after him and speaks slowly in a small voice.
- 11–12s (Shot 3): @Na keeps speaking softly, the test paper still lifted toward his back, her smile fading.
- 12–13s (Shot 3): @Na keeps talking in a small voice, her arm sinking.
- 13–14s (CUT to Shot 4): @Na finishes, closes her mouth and lowers the test paper to her side.
- 14–15s (Shot 4): @Na's eyes drop to the floor, her lips pressed together, as footsteps fade up the stairs. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, proud, waving the paper): "Bố ơi, xem bài con này! Cô giáo khen con trước cả lớp, các bạn còn vỗ tay nữa cơ!"
- Turn 2, 5.3–10.1s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, distracted, eyes on the phone): "Ừ, con gái bố giỏi lắm. Bố ăn với khách rồi, hai mẹ con cứ ăn trước đi, bố lên tắm cái đã."
- Turn 3, 10.6–13.6s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking slowly and softly, unhurried, with a short natural pause between phrases, small voice, smile fading): "Nhưng bố còn chưa nhìn con lấy một cái mà..."
- Pacing: @Na speaks quickly, then @Tung answers quickly, then @Na answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a motorbike engine cutting off in the alley, a door creaking, a phone buzzing, heavy footsteps on tiled stairs. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 3 (`canh-02/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium two-shot across the round table, slow push-in.
- Shot 2, 3–6s: 85mm close-up of the wife over her rice bowl, locked off.
- Shot 3, 6–9s: 50mm medium shot of the husband at the table, slight handheld sway.
- Shot 4, 9–15s: 50mm over-the-shoulder shot from behind the husband onto the wife, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu, seated at the round dinner table, lifts her eyes from her rice bowl and is already speaking lightly, while @Tung, his tie hanging loose, drops onto the stool across from her and pours a glass of water.
- 1–2s (Shot 1): @Thu keeps talking in an offhand voice, picking up a piece of braised fish with her chopsticks, while @Tung raises the glass to his mouth.
- 2–3s (Shot 1): @Thu keeps speaking casually as @Tung gulps the water.
- 3–4s (CUT to Shot 2): @Thu keeps talking evenly, her eyes resting on his face.
- 4–5s (Shot 2): @Thu keeps speaking lightly, laying the piece of fish in her bowl.
- 5–6s (Shot 2): @Thu says the last word gently, lays her chopsticks down and closes her mouth.
- 6–7s (CUT to Shot 3): @Tung splutters into the glass, water dribbling down his chin, and answers fast between coughs.
- 7–8s (Shot 3): @Tung keeps talking loudly, patting his own chest with his palm.
- 8–9s (Shot 3): @Tung keeps speaking fast, his eyes darting away, then closes his mouth.
- 9–10s (CUT to Shot 4): @Thu answers slowly and mildly, her eyes fixed on him, while @Tung wipes his chin with the back of his hand.
- 10–11s (Shot 4): @Thu keeps speaking softly, with a faint shrug of her shoulders.
- 11–12s (Shot 4): @Thu keeps talking in a mild voice, picking up her chopsticks again.
- 12–13s (Shot 4): @Thu keeps speaking calmly, her eyes never leaving him.
- 13–14s (Shot 4): @Thu finishes and closes her mouth.
- 14–15s (Shot 4): @Thu watches him without blinking, mouth closed, while @Tung's shoulders stiffen in the foreground. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, light, almost offhand): "Chiều nay có cô khách xinh lắm đến đặt may đồ cưới. Chú rể làm giám đốc xây dựng, tên Tùng."
- Turn 2, 6.2–9.0s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, spluttering, defensive): "Thì sao? Cả Hà Nội thiếu gì người trùng tên, kể làm gì!"
- Turn 3, 9.5–13.4s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, mild, eyes fixed on him): "Ừ, thiếu gì. Em kể cho vui thôi, em có bảo là anh đâu."
- Pacing: @Thu speaks at an even everyday pace, then @Tung answers quickly, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water pouring into a glass, a sudden splutter and cough, chopsticks set down on a bowl, an old fridge humming. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 4 (`canh-02/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the husband onto the wife, holding the previous framing.
- Shot 2, 5–8s: 35mm medium shot of the husband rising from the stool, slow tilt up.
- Shot 3, 8–10s: 85mm close-up of the husband's flushed face, locked off.
- Shot 4, 10–15s: 50mm medium shot of the wife at the table with the staircase behind her, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu is already speaking slowly and coldly, her eyes resting on the collar of @Tung's white shirt, while @Tung listens with his mouth closed, the glass frozen halfway to the table.
- 1–2s (Shot 1): @Thu keeps speaking in a low, precise voice, her chopsticks laid neatly beside her bowl.
- 2–3s (Shot 1): @Thu tilts her head slightly toward his collar and keeps talking, her face perfectly still.
- 3–4s (Shot 1): @Thu keeps talking quietly, her eyes never leaving him, while @Tung's knuckles whiten on the glass.
- 4–5s (Shot 1): @Thu finishes in the same even voice and closes her mouth.
- 5–6s (CUT to Shot 2): @Tung springs up from the stool, the stool scraping back, and answers fast and loud.
- 6–7s (Shot 2): @Tung keeps shouting, flinging one hand up in the air.
- 7–8s (Shot 2): @Tung points toward the door to the alley and keeps talking loudly, his chest heaving.
- 8–9s (CUT to Shot 3): @Tung keeps speaking loudly, red in the face, a vein standing out at his temple.
- 9–10s (Shot 3): @Tung jabs a finger toward her as he snaps his last question, then closes his mouth.
- 10–11s (CUT to Shot 4): @Thu, without looking up, answers slowly and flatly as she picks up her chopsticks.
- 11–12s (Shot 4): @Thu keeps speaking evenly, eyes on her bowl, while @Tung stands frozen beside the stool in the soft background.
- 12–13s (Shot 4): @Thu keeps talking in a flat, almost kind voice, lifting a piece of braised fish with her chopsticks.
- 13–14s (Shot 4): @Thu keeps speaking softly and lays the piece of fish into the small child's bowl beside her.
- 14–15s (Shot 4): @Thu finishes her last words and closes her mouth, while @Tung stomps up the steep tiled staircase in the background, tugging at his shirt collar. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, cold, quiet and precise): "Lạ một cái, cổ áo anh cũng thơm đúng mùi nước hoa của cô dâu ấy."
- Turn 2, 5.4–9.8s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, loud and cornered): "Cô đừng tưởng tượng linh tinh! Tôi tiếp khách cả ngày, ai chả xịt nước hoa! Cô theo dõi tôi à?"
- Turn 3, 10.3–14.2s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, flat, almost kindly): "Mũi em tự biết. Anh tắm đi, giặt cả áo, kẻo con ngửi thấy."
- Pacing: @Thu speaks slowly and calmly, then @Tung answers quickly, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a stool scraping across tiles, heavy footsteps stomping up the stairs, chopsticks clicking softly, a moped passing in the alley. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 1 (`canh-03/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Bà Nhàn's small upstairs bedroom at night: a carved wooden bed with the mosquito net looped up, an old wooden wardrobe with a mirror, a side table with a warm bedside lamp, a window onto dark tiled roofs.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the old woman on the edge of the bed, slow push-in.
- Shot 2, 3–6s: 85mm close-up of the old woman leaning into the lamplight, locked off.
- Shot 3, 6–10s: 50mm over-the-shoulder shot from behind the old woman onto the daughter-in-law, locked off.
- Shot 4, 10–15s: 40mm medium two-shot across the bedside lamp, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan sits on the edge of the carved bed beside the warm bedside lamp, pats the low wooden chair next to her and is already speaking in a hushed voice, as @Thu slips into the room, mouth closed.
- 1–2s (Shot 1): @Thu sits down on the low chair, mouth closed, while @BaNhan keeps talking low and conspiratorially.
- 2–3s (Shot 1): @BaNhan glances at the door and keeps speaking, one hand cupped beside her mouth.
- 3–4s (CUT to Shot 2): @BaNhan leans toward the lamp and keeps whispering, her wrinkled face half lit.
- 4–5s (Shot 2): @BaNhan keeps talking low, her eyebrows rising meaningfully.
- 5–6s (Shot 2): @BaNhan whispers the last words with a small knowing nod and closes her mouth.
- 6–7s (CUT to Shot 3): @Thu lifts her eyes and answers, her voice catching.
- 7–8s (Shot 3): @Thu keeps speaking, her fingers knotting in her dark-green apron.
- 8–9s (Shot 3): @Thu keeps talking, hurt, her eyes glistening.
- 9–10s (Shot 3): @Thu finishes the question and closes her mouth, waiting.
- 10–11s (CUT to Shot 4): @BaNhan looks away at the dark window and answers in a dry, low voice.
- 11–12s (Shot 4): @BaNhan keeps speaking quietly, her thin hands folded on her knees, while @Thu listens with her mouth closed.
- 12–13s (Shot 4): @BaNhan keeps talking, turning back to @Thu with a rueful lift of her brows.
- 13–14s (Shot 4): @BaNhan finishes with a dry little shrug and closes her mouth.
- 14–15s (Shot 4): @BaNhan reaches for the red-lacquered box on the side table, while @Thu lowers her head, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, hushed and conspiratorial): "Ngồi đây mẹ bảo. Tuần trước mẹ thấy con bé váy đỏ ấy khoác tay thằng Tùng ở hiệu vàng."
- Turn 2, 6.2–9.5s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, hurt, voice catching): "Mẹ biết từ hôm ấy mà bây giờ mới nói với con ạ?"
- Turn 3, 10.0–14.0s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, dry, a little sad): "Nói sớm thì con có tin mẹ không? Hay lại nghĩ mẹ chồng đặt điều?"
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft night breeze at the window, a clock ticking on the wardrobe, a distant motorbike, the creak of an old wooden bed. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 2 (`canh-03/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Bà Nhàn's small upstairs bedroom at night: a carved wooden bed with the mosquito net looped up, an old wooden wardrobe with a mirror, a side table with a warm bedside lamp, a window onto dark tiled roofs.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot across the bedside lamp, holding the previous framing.
- Shot 2, 5–9s: 85mm close-up of the daughter-in-law, locked off.
- Shot 3, 9–12s: 50mm over-the-shoulder shot from behind the daughter-in-law onto the old woman and the open box, slow push-in.
- Shot 4, 12–15s: 40mm medium two-shot over the bedside lamp, slow push-in toward the papers.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan lifts a red-lacquered wooden box with gold inlay from the side table onto her lap and is already speaking slowly and gravely, while @Thu watches with her mouth closed.
- 1–2s (Shot 1): @BaNhan keeps speaking, both hands resting on the box.
- 2–3s (Shot 1): @BaNhan keeps talking in a low voice, her thumbs on the gold inlay of the lid.
- 3–4s (Shot 1): @BaNhan keeps speaking, her eyes on @Thu, the lamplight deep in her wrinkles.
- 4–5s (Shot 1): @BaNhan finishes and closes her mouth, resting both hands flat on the box.
- 5–6s (CUT to Shot 2): @Thu answers softly, her eyes on the lacquer lid.
- 6–7s (Shot 2): @Thu keeps speaking quietly, her gaze drifting far away.
- 7–8s (Shot 2): @Thu keeps talking in a soft, remembering voice.
- 8–9s (Shot 2): @Thu finishes and closes her mouth, swallowing.
- 9–10s (CUT to Shot 3): @BaNhan opens the lacquer lid and starts speaking briskly.
- 10–11s (Shot 3): @BaNhan keeps talking as she takes out a pink-red land title booklet with no readable writing.
- 11–12s (Shot 3): @BaNhan keeps speaking matter-of-factly, lifting out an old yellowed folded paper as well.
- 12–13s (CUT to Shot 4): @BaNhan keeps speaking briskly and holds the booklet and the folded paper out toward @Thu.
- 13–14s (Shot 4): @BaNhan keeps talking, the papers held steady in the lamplight, while @Thu stares at them with her mouth closed.
- 14–15s (Shot 4): @BaNhan finishes and closes her mouth as @Thu takes the booklet and the folded paper in both hands. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking slowly and softly, unhurried, with a short natural pause between phrases, low and grave): "Mười hai năm trước, con bán đất bố con để lại cho nó làm vốn."
- Turn 2, 5.3–8.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft, remembering): "Hồi ấy con chỉ mong anh ấy làm ăn được, đỡ khổ."
- Turn 3, 9.2–14.2s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, brisk, matter-of-fact): "Mẹ thì lo. Nên mẹ bắt nó cho con đứng tên nhà này, sáu mươi phần trăm công ty."
- Pacing: @BaNhan speaks slowly and calmly, then @Thu answers slowly and calmly, then @BaNhan answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft click of a lacquer lid, old paper rustling, the clock ticking, a night breeze at the window. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 3 (`canh-03/clip-3.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Bà Nhàn's small upstairs bedroom at night: a carved wooden bed with the mosquito net looped up, an old wooden wardrobe with a mirror, a side table with a warm bedside lamp, a window onto dark tiled roofs.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot over the bedside lamp, holding the previous framing.
- Shot 2, 5–8s: 85mm close-up of the old woman tapping her temple, locked off.
- Shot 3, 8–11s: 35mm wide shot of the small bedroom with both women by the lamp, slow push-in.
- Shot 4, 11–13s: 85mm close-up of the daughter-in-law over the booklet, locked off.
- Shot 5, 13–15s: 40mm medium two-shot across the lamp and the lacquer box, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu holds the pink-red land title booklet with no readable writing in both hands and is already speaking slowly, half in wonder, while @BaNhan watches with her mouth closed.
- 1–2s (Shot 1): @Thu keeps speaking softly, her fingers trembling slightly on the cover.
- 2–3s (Shot 1): @Thu keeps talking, turning the booklet over in her hands.
- 3–4s (Shot 1): @Thu keeps speaking, lifting her eyes to @BaNhan.
- 4–5s (Shot 1): @Thu finishes and closes her mouth, and @BaNhan taps her own temple with one finger and starts speaking dryly, a glint in her eyes.
- 5–6s (CUT to Shot 2): @BaNhan keeps talking, the corner of her mouth twitching with mischief.
- 6–7s (Shot 2): @BaNhan raises one bony finger and keeps speaking, her eyebrows lifting.
- 7–8s (Shot 2): @BaNhan keeps speaking, lower now, leaning toward @Thu across the lamp.
- 8–9s (CUT to Shot 3): @BaNhan keeps talking firmly, while @Thu listens with her mouth closed.
- 9–10s (Shot 3): @BaNhan nods at the booklet in @Thu's hands as she keeps speaking.
- 10–11s (Shot 3): @BaNhan finishes and closes her mouth, her eyes steady, and @Thu lowers her eyes to the booklet and answers slowly.
- 11–12s (CUT to Shot 4): @Thu keeps speaking, her voice heavy, her eyes glistening in the lamplight.
- 12–13s (Shot 4): @Thu keeps speaking softly, her thumb stroking the cover of the booklet.
- 13–14s (CUT to Shot 5): @Thu finishes and closes her mouth, swallowing hard.
- 14–15s (Shot 5): @BaNhan lays her wrinkled hand flat on the lacquer box lid between them, while @Thu breathes out slowly, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.3s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, half in wonder): "Con cứ tưởng mẹ quên chuyện này lâu rồi, mẹ chưa nhắc lần nào."
- Turn 2, 4.8–10.4s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, dry, a twinkle of mischief): "Mẹ già chứ chưa lẫn. Con trai mẹ yếu chỗ nào, mẹ biết, nên phải giữ cho con một đường lui."
- Turn 3, 10.9–14.0s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, heavy, close to tears): "Mong là không bao giờ phải dùng đến nó, mẹ ạ."
- Pacing: @Thu speaks slowly and calmly, then @BaNhan answers at an even everyday pace, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the clock ticking, the lamp buzzing faintly, a shaky breath, a dog barking far off in the alley. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 4 (`canh-03/clip-4.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Bà Nhàn's small upstairs bedroom at night: a carved wooden bed with the mosquito net looped up, an old wooden wardrobe with a mirror, a side table with a warm bedside lamp, a window onto dark tiled roofs.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot across the lamp and the lacquer box, holding the previous framing.
- Shot 2, 5–8s: 85mm close-up of the daughter-in-law straightening her back, slow push-in.
- Shot 3, 8–10s: 50mm medium shot of the daughter-in-law laying the papers back into the box, locked off.
- Shot 4, 10–13s: 85mm close-up of the old woman, locked off.
- Shot 5, 13–15s: 50mm medium two-shot from beside the window, slow pull-back from the two women.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan points a bony finger at the lacquer box and is already speaking slowly and firmly, while @Thu listens with her mouth closed, the booklet resting on her knees.
- 1–2s (Shot 1): @BaNhan keeps speaking, tapping the lid once with her fingertip.
- 2–3s (Shot 1): @BaNhan keeps talking, her gaze hard and steady on @Thu.
- 3–4s (Shot 1): @BaNhan keeps speaking firmly, her chin lifted.
- 4–5s (Shot 1): @BaNhan finishes and closes her mouth, waiting.
- 5–6s (CUT to Shot 2): @Thu slowly straightens her back and answers quietly.
- 6–7s (Shot 2): @Thu keeps speaking, her jaw setting as the words come.
- 7–8s (Shot 2): @Thu keeps talking in a level voice, her eyes steady and dry.
- 8–9s (CUT to Shot 3): @Thu keeps speaking as she lays the booklet and the folded paper back into the red-lacquered box, while @BaNhan listens with her mouth closed.
- 9–10s (Shot 3): @Thu keeps talking calmly, smoothing the folded paper flat inside the box.
- 10–11s (CUT to Shot 4): @Thu finishes and closes her mouth, and @BaNhan blinks, her eyebrows lifting, and asks a quick question.
- 11–12s (Shot 4): @BaNhan keeps talking, leaning closer to the lamp, her eyes narrowing.
- 12–13s (Shot 4): @BaNhan keeps speaking as a slow smile of understanding spreads across her face.
- 13–14s (CUT to Shot 5): @BaNhan keeps talking with a little approving nod, while @Thu shuts the lacquer lid with a soft click, mouth closed.
- 14–15s (Shot 5): @BaNhan finishes and closes her mouth, a small satisfied smile on her lips, while @Thu sits with her jaw set, silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking slowly and softly, unhurried, with a short natural pause between phrases, firm and unwavering): "Không dùng thì cất. Đừng để con hồ ly nào cướp phần của cái Na."
- Turn 2, 5.3–10.1s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, resolve hardening): "Vâng, con cất. Nhưng mẹ cứ để con may xong cái áo cưới cho cô ấy đã."
- Turn 3, 10.6–14.3s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, startled, then catching on): "Con may cho nó thật à? Mẹ hiểu rồi, con cao tay thật đấy."
- Pacing: @BaNhan speaks slowly and calmly, then @Thu answers slowly and calmly, then @BaNhan answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft click of a lacquer lid closing, the clock ticking, wind stirring the curtain, a distant temple bell. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 1 (`canh-04/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A glossy luxury apartment high above Hà Nội at night: floor-to-ceiling windows full of city lights, a white leather sofa, a marble kitchen island with a bottle of champagne and two glasses, cold blue-white light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium shot of the young woman sweeping in and dropping onto the white sofa, slow pan.
- Shot 2, 5–9s: 50mm over-the-shoulder shot from behind the young woman onto the man at the marble island.
- Shot 3, 9–13s: 85mm close-up of the young woman laughing on the sofa, locked off.
- Shot 4, 13–15s: 40mm medium two-shot as the man carries two glasses to the sofa, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy sweeps into the glossy apartment, stepping out of her beige high heels, and is already speaking fast, laughing.
- 1–2s (Shot 1): @Vy drops onto the white leather sofa and keeps talking gleefully, tucking her bare feet up.
- 2–3s (Shot 1): @Vy keeps boasting fast, tipping her head back with laughter.
- 3–4s (Shot 1): @Vy keeps talking, pulling a stiff statue face to mimic the wife.
- 4–5s (Shot 1): @Vy finishes her last words and closes her mouth with a snort of laughter.
- 5–6s (CUT to Shot 2): @Khai, at the marble kitchen island peeling the foil from a champagne bottle, asks a lazy question with one eyebrow raised.
- 6–7s (Shot 2): @Khai keeps talking in a slow drawl, twisting the wire off the cork.
- 7–8s (Shot 2): @Khai pops the cork and keeps speaking, champagne foaming over his fingers, his eyes narrowing.
- 8–9s (Shot 2): @Khai finishes and closes his mouth, pouring two glasses.
- 9–10s (CUT to Shot 3): @Vy waves the warning away and answers fast with a giggle.
- 10–11s (Shot 3): @Vy keeps talking, mimicking a prim little voice and rolling her eyes.
- 11–12s (Shot 3): @Vy keeps speaking fast, flicking her hand in the air.
- 12–13s (Shot 3): @Vy keeps laughing as she talks, wiggling her bare toes on the sofa.
- 13–14s (CUT to Shot 4): @Vy finishes and closes her mouth with a smirk, while @Khai carries two glasses of champagne over to the sofa, mouth closed.
- 14–15s (Shot 4): @Vy stretches out on the sofa with a satisfied smirk while @Khai stops beside her, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, gleeful and boastful): "Anh ơi, em đến tận tiệm vợ lão đặt may áo dài cưới. Mặt bà ấy cứ đơ ra như tượng!"
- Turn 2, 5.3–8.8s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking at a natural, even conversational pace, lazy, a flicker of unease): "Không khóc, không làm ầm à? Đàn bà im thế mới đáng ngại đấy."
- Turn 3, 9.3–13.3s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, giggling, mocking): "Ngại gì! Bà ấy còn hỏi em thích cổ cao hay cổ thuyền, lụa hay gấm, buồn cười chưa!"
- Pacing: @Vy speaks quickly, then @Khai answers at an even everyday pace, then @Vy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: high heels clattering onto marble, a champagne cork popping, bubbles fizzing into glass, the faint hum of city traffic far below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 2 (`canh-04/clip-2.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 7s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A glossy luxury apartment high above Hà Nội at night: floor-to-ceiling windows full of city lights, a white leather sofa, a marble kitchen island with a bottle of champagne and two glasses, cold blue-white light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot as the man carries two glasses to the sofa, holding the previous framing.
- Shot 2, 5–7s: 85mm close-up of the young woman sliding a ring onto her finger, slow push-in.
- Shot 3, 7–10s: 50mm over-the-shoulder shot from behind the man onto the young woman, locked off.
- Shot 4, 10–13s: 85mm close-up of the man's smug face, locked off.
- Shot 5, 13–15s: 50mm medium two-shot low across the sofa, slow push-in toward their hands.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai sits on the arm of the white sofa, hands @Vy a glass of champagne and is already speaking with a sly smile, taking a small dark velvet box from his pocket.
- 1–2s (Shot 1): @Khai keeps talking softly as he opens the velvet box to show a plain gold wedding ring.
- 2–3s (Shot 1): @Khai keeps speaking, an identical gold band glinting on his own ring finger.
- 3–4s (Shot 1): @Khai keeps talking, tilting the open box toward @Vy, his eyes fixed on her.
- 4–5s (Shot 1): @Khai finishes and closes his mouth, holding out the open box.
- 5–6s (CUT to Shot 2): @Vy slides the ring onto her own ring finger and answers him teasingly.
- 6–7s (Shot 2): @Vy keeps talking, turning the ring in the light and rolling her eyes.
- 7–8s (CUT to Shot 3): @Vy keeps speaking playfully, wagging her ringed finger at him.
- 8–9s (Shot 3): @Vy keeps talking with a mock sigh, while @Khai listens with his mouth closed.
- 9–10s (Shot 3): @Vy finishes and closes her mouth with a pout.
- 10–11s (CUT to Shot 4): @Khai answers with a smug little shrug.
- 11–12s (Shot 4): @Khai keeps speaking, mock-wounded, one hand pressed to his own chest.
- 12–13s (Shot 4): @Khai keeps talking with a sly sneer, nodding toward the city lights.
- 13–14s (CUT to Shot 5): @Khai finishes and closes his mouth as @Vy taps her ring against his matching ring with a tiny click.
- 14–15s (Shot 5): @Vy and @Khai smirk at the two identical gold bands side by side, mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking at a natural, even conversational pace, sly and possessive): "Đeo vào đi em. Về nhà rồi, còn đóng vai cô thư ký ngây thơ làm gì nữa."
- Turn 2, 5.4–9.9s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, teasing and playful): "Ba năm rồi, lão nào em diễn anh cũng ghen. Chồng gì mà trẻ con thế không biết."
- Turn 3, 10.4–13.7s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking at a natural, even conversational pace, smug, mock-wounded): "Ghen thì mới giữ được vợ chứ. Lão kia có biết giữ đâu."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a velvet box clicking open, ice settling in the bucket, a tiny metallic click of two rings, the city hum far below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 3 (`canh-04/clip-3.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A glossy luxury apartment high above Hà Nội at night: floor-to-ceiling windows full of city lights, a white leather sofa, a marble kitchen island with a bottle of champagne and two glasses, cold blue-white light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium two-shot low across the sofa, holding the previous framing.
- Shot 2, 3–6s: 85mm close-up of the man at the marble kitchen island, slow lateral track.
- Shot 3, 6–11s: 50mm medium shot of the young woman leaning on the marble, locked off.
- Shot 4, 11–13s: 85mm close-up of the man across the island, locked off.
- Shot 5, 13–15s: 35mm wide shot across the marble island toward the city windows, slow drift.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai rises from the arm of the sofa and is already speaking in a cool businesslike voice, while @Vy watches with her mouth closed.
- 1–2s (Shot 1): @Khai keeps talking as he walks to the marble kitchen island, @Vy following with her champagne glass.
- 2–3s (Shot 1): @Khai keeps speaking evenly and sets his glass down on the marble.
- 3–4s (CUT to Shot 2): @Khai flips open a black leather document folder and keeps talking, cool and flat.
- 4–5s (Shot 2): @Khai keeps speaking, laying sheets of paper with no readable writing on the marble.
- 5–6s (Shot 2): @Khai finishes and closes his mouth, squaring the papers on the marble.
- 6–7s (CUT to Shot 3): @Vy leans her elbows on the marble and answers fast and giddy, her eyes shining.
- 7–8s (Shot 3): @Vy keeps talking excitedly, fluttering her fingers like a bird flying off.
- 8–9s (Shot 3): @Vy keeps speaking fast, waving her champagne glass.
- 9–10s (Shot 3): @Vy keeps talking with a wicked giggle, tapping the papers.
- 10–11s (Shot 3): @Vy finishes, closes her mouth and drains her glass in one go.
- 11–12s (CUT to Shot 4): @Khai taps one sheet with a fingertip, the gold band glinting on his hand, and adds a dry warning in a low voice.
- 12–13s (Shot 4): @Khai keeps speaking quietly, holding @Vy's gaze, one eyebrow raised.
- 13–14s (CUT to Shot 5): @Khai finishes and closes his mouth, then shuts the black leather folder with a soft snap.
- 14–15s (Shot 5): @Khai refills two glasses from the champagne bottle while @Vy rolls her eyes with a grin, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.9s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking at a natural, even conversational pace, cool and businesslike): "Lão Tùng là con cá thứ ba. Trước đám hỏi, phải bắt lão nộp đủ năm tỷ với căn nhà ba tầng."
- Turn 2, 6.4–10.6s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, giddy, eyes shining): "Cầm tiền với sổ đỏ là bay, như hai lần trước. Lão chẳng kịp hiểu mình bị lừa thế nào!"
- Turn 3, 11.1–13.6s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking at a natural, even conversational pace, dry, a quiet warning): "Nhớ đấy, tiền phải vào trước, giấy tờ tính sau."
- Pacing: @Khai speaks at an even everyday pace, then @Vy answers quickly, then @Khai answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a leather folder flipping open, paper sliding on marble, a glass set down on stone, the low hum of a fridge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 4 (`canh-04/clip-4.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 10s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A glossy luxury apartment high above Hà Nội at night: floor-to-ceiling windows full of city lights, a white leather sofa, a marble kitchen island with a bottle of champagne and two glasses, cold blue-white light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm wide shot across the marble island toward the city windows, holding the previous framing.
- Shot 2, 3–6s: 50mm medium shot of the young woman against the city lights, slow push-in.
- Shot 3, 6–10s: 85mm close-up of the man by the window, locked off.
- Shot 4, 10–12s: 50mm over-the-shoulder shot from behind the man onto the young woman.
- Shot 5, 12–15s: 40mm medium two-shot in front of the floor-to-ceiling windows, slow pull-back revealing the glittering city.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy walks toward the floor-to-ceiling windows with a fresh glass of champagne and is already speaking slowly in a purring voice, like an innocent bride, while @Khai follows with his mouth closed.
- 1–2s (Shot 1): @Vy keeps speaking sweetly as she stops before the glass, the glittering city spread out below.
- 2–3s (Shot 1): @Vy turns to face @Khai against the city lights and keeps talking, a hand laid demurely over her heart.
- 3–4s (CUT to Shot 2): @Vy keeps speaking, lowering her eyes in mock modesty.
- 4–5s (Shot 2): @Vy keeps talking in a honeyed voice, batting her lashes.
- 5–6s (Shot 2): @Vy finishes with a sugary smile and closes her mouth.
- 6–7s (CUT to Shot 3): @Khai straightens an invisible tie and answers with a smirk.
- 7–8s (Shot 3): @Khai keeps talking, putting on a solemn lawyer's face.
- 8–9s (Shot 3): @Khai raises one warning finger and keeps speaking, mock-stern.
- 9–10s (Shot 3): @Khai keeps speaking, his lips twitching as he holds back a laugh, while @Vy listens with her mouth closed.
- 10–11s (CUT to Shot 4): @Khai finishes and closes his mouth, eyebrows raised, and @Vy gives a mock salute and chirps a quick reply.
- 11–12s (Shot 4): @Vy keeps talking playfully, her hand still at her brow.
- 12–13s (CUT to Shot 5): @Vy keeps speaking with an exaggerated little bow of her head.
- 13–14s (Shot 5): @Vy finishes and closes her mouth with a wink.
- 14–15s (Shot 5): @Vy and @Khai clink their champagne glasses in front of the glittering window, the two gold wedding rings flashing on their hands, mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking slowly and softly, unhurried, with a short natural pause between phrases, purring, sweet as honey): "Từ mai, em sẽ làm cô dâu ngoan nhất cái Hà Nội này, nói câu nào ngọt câu ấy."
- Turn 2, 6.2–10.2s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking at a natural, even conversational pace, smirking, mock-solemn): "Còn anh thành anh họ của em. Trước mặt lão, cấm gọi chồng ơi đấy nhé."
- Turn 3, 10.7–13.5s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, playful, a mock salute): "Dạ vâng, em nhớ rồi ạ, thưa anh họ luật sư đáng kính!"
- Pacing: @Vy speaks slowly and calmly, then @Khai answers at an even everyday pace, then @Vy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the crystal ring of two glasses clinking, champagne fizzing, a faint wind against the high windows, the city hum below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 1 (`canh-05/clip-1.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Thu's narrow áo dài tailor shop on an old-quarter silk street by day: bolts of jewel-toned silk stacked on wooden shelves to the ceiling, two headless dress forms in half-finished áo dài, an old black sewing machine on a worn wooden table, a tall standing fitting mirror, a long cutting table with tailor's chalk and paper patterns, a small brass bell above the glass door, soft daylight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 85mm close-up of the customer on the fitting stand, slow push-in.
- Shot 2, 3–5s: 35mm wide shot of the shop from behind the tall fitting mirror, locked off.
- Shot 3, 5–11s: 85mm close-up of the tailor fastening the silk, locked off.
- Shot 4, 11–13s: 50mm over-the-shoulder shot from behind the tailor onto the customer.
- Shot 5, 13–15s: 40mm medium two-shot at the fitting stand, slow arc.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy stands on the low fitting stand in her crimson dress, red silk draped over one shoulder, and is already speaking with a smug smile, chin lifted toward the mirror.
- 1–2s (Shot 1): @Vy keeps talking, savoring every word, while @Thu fastens the red silk at her shoulder with dressmaker's pins, mouth closed.
- 2–3s (Shot 1): @Vy keeps speaking, flicking her eyes sideways at @Thu with a little smile.
- 3–4s (CUT to Shot 2): @Vy keeps talking sweetly, smoothing the silk over her hip.
- 4–5s (Shot 2): @Vy keeps speaking with a little lift of her chin.
- 5–6s (CUT to Shot 3): @Vy finishes and closes her mouth, and @Thu slides one more pin into the silk and answers slowly without looking up.
- 6–7s (Shot 3): @Thu keeps speaking mildly, almost pleasantly, her fingers smoothing the fold.
- 7–8s (Shot 3): @Thu keeps talking softly, her eyes softening for a moment.
- 8–9s (Shot 3): @Thu keeps speaking, a faint far-off smile at the corner of her mouth.
- 9–10s (Shot 3): @Thu keeps talking quietly, folding the hem of the silk.
- 10–11s (Shot 3): @Thu finishes and closes her mouth, smoothing the silk flat.
- 11–12s (CUT to Shot 4): @Vy tosses back a quick needling reply in a sing-song voice.
- 12–13s (Shot 4): @Vy keeps talking fast, wrinkling her nose at the old shop around her.
- 13–14s (CUT to Shot 5): @Vy finishes and closes her mouth, her smile sharp.
- 14–15s (Shot 5): @Thu picks another pin from the pincushion in silence while @Vy's smug smile stiffens, both mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, smug, savoring every word): "Anh Tùng hứa sang tên cái nhà ba tầng cho em làm sính lễ. Chắc chị biết nhà nào."
- Turn 2, 5.7–10.5s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, mild, almost pleasant): "Nhà ấy à? Đẹp lắm. Cái Na sinh ra ở đấy, chập chững tập đi ở đấy."
- Turn 3, 11.0–14.0s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, needling, sing-song): "Thế thì chị dọn dần đi là vừa. Em không thích đồ cũ đâu."
- Pacing: @Vy speaks at an even everyday pace, then @Thu answers slowly and calmly, then @Vy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: silk rustling, the tiny click of pins, motorbikes passing outside, a wall clock ticking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 2 (`canh-05/clip-2.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Thu's narrow áo dài tailor shop on an old-quarter silk street by day: bolts of jewel-toned silk stacked on wooden shelves to the ceiling, two headless dress forms in half-finished áo dài, an old black sewing machine on a worn wooden table, a tall standing fitting mirror, a long cutting table with tailor's chalk and paper patterns, a small brass bell above the glass door, soft daylight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium two-shot at the fitting stand, holding the previous framing.
- Shot 2, 3–5s: 85mm close-up of the tailor looking up from the customer's hand, slow push-in.
- Shot 3, 5–10s: 50mm medium shot of the customer on the fitting stand, locked off.
- Shot 4, 10–13s: 50mm over-the-shoulder shot from behind the customer onto the tailor, locked off.
- Shot 5, 13–15s: 40mm medium two-shot beside the fitting mirror, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu takes @Vy's hand to measure the sleeve and is already speaking slowly and quietly, wrapping the yellow measuring tape around @Vy's wrist.
- 1–2s (Shot 1): @Thu keeps speaking as she slides the tape down toward @Vy's fingers.
- 2–3s (Shot 1): @Thu keeps talking softly, the tape stopping on a thin pale band of skin at the base of @Vy's ring finger.
- 3–4s (CUT to Shot 2): @Thu looks up from the pale ring mark and keeps asking, every word soft and sharp as a needle, her eyes steady on @Vy's face.
- 4–5s (Shot 2): @Thu finishes asking and closes her mouth, waiting.
- 5–6s (CUT to Shot 3): @Vy pulls her hand back, hides it behind her back and answers fast with a brittle laugh.
- 6–7s (Shot 3): @Vy keeps talking quickly, her cheeks flushing pink.
- 7–8s (Shot 3): @Vy keeps speaking fast, rolling her eyes to cover herself.
- 8–9s (Shot 3): @Vy keeps talking, tossing her hair with a forced laugh.
- 9–10s (Shot 3): @Vy finishes and closes her mouth, her hand still hidden behind her back.
- 10–11s (CUT to Shot 4): @Thu answers in a dry, unbothered voice, rolling the yellow measuring tape around two fingers.
- 11–12s (Shot 4): @Thu keeps speaking evenly, nodding toward @Vy's hidden hand.
- 12–13s (Shot 4): @Thu keeps talking calmly, the rolled tape resting in her palm.
- 13–14s (CUT to Shot 5): @Thu keeps speaking, her eyes never leaving @Vy.
- 14–15s (Shot 5): @Thu finishes and closes her mouth, while @Vy shifts her weight on the fitting stand, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, sharp as a needle): "Ngón áp út em có vết hằn. Nhẫn của ai mà đeo lâu thế hả em?"
- Turn 2, 5.4–9.6s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, flustered, covering with a laugh): "Nhẫn em đeo chơi thôi mà! Chị đo áo hay đo tay người ta đấy? Sao chị lắm chuyện thế!"
- Turn 3, 10.1–14.1s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, dry, unbothered): "Đo cả chứ em. Tay áo phải vừa tay người, lệch một phân là lộ ngay."
- Pacing: @Thu speaks slowly and calmly, then @Vy answers quickly, then @Thu answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft slither of a measuring tape, silk rustling sharply, a brittle laugh cut short, the street faint behind the glass. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 3 (`canh-05/clip-3.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Thu's narrow áo dài tailor shop on an old-quarter silk street by day: bolts of jewel-toned silk stacked on wooden shelves to the ceiling, two headless dress forms in half-finished áo dài, an old black sewing machine on a worn wooden table, a tall standing fitting mirror, a long cutting table with tailor's chalk and paper patterns, a small brass bell above the glass door, soft daylight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium two-shot beside the fitting mirror, holding the previous framing.
- Shot 2, 3–6s: 85mm close-up of the customer's over-sweet smile, locked off.
- Shot 3, 6–9s: 50mm over-the-shoulder shot from behind the customer onto the tailor, slow push-in.
- Shot 4, 9–13s: 85mm close-up of the tailor's face, very slow push-in.
- Shot 5, 13–15s: 35mm wide shot of the fitting corner with both women and the tall mirror, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy recovers her smile, tosses her hair and is already speaking in a mocking sing-song, while @Thu winds up the yellow measuring tape with her mouth closed.
- 1–2s (Shot 1): @Vy keeps talking sweetly, waving a hand at the red silk on her shoulder.
- 2–3s (Shot 1): @Vy leans toward @Thu and keeps speaking, all honey.
- 3–4s (CUT to Shot 2): @Vy keeps speaking with an over-sweet smile, her eyebrows arched.
- 4–5s (Shot 2): @Vy keeps talking, rubbing her thumb and fingers together as if counting money.
- 5–6s (Shot 2): @Vy keeps speaking with a little laugh at her own joke.
- 6–7s (CUT to Shot 3): @Vy finishes and closes her mouth, pleased with herself, and @Thu tucks the wound tape into her palm and starts answering slowly and calmly.
- 7–8s (Shot 3): @Thu keeps speaking in an even voice, the rolled tape resting in her palm.
- 8–9s (Shot 3): @Thu keeps speaking, unhurried, her gaze traveling once from @Vy's shoulders to her waist as if measuring.
- 9–10s (CUT to Shot 4): @Thu lifts her eyes to look straight into @Vy's eyes and keeps speaking slowly.
- 10–11s (Shot 4): @Thu keeps talking, every word weighed, her face perfectly still.
- 11–12s (Shot 4): @Thu keeps speaking quietly, without blinking.
- 12–13s (Shot 4): @Thu keeps talking in a low, level voice, still holding the look.
- 13–14s (CUT to Shot 5): @Thu says her last words and closes her mouth, while the smile drains from @Vy's face.
- 14–15s (Shot 5): @Vy blinks first and turns away toward the tall mirror, fussing with the red silk, while @Thu calmly picks up the pincushion, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.2s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, mocking and overly sweet): "Chị cứ may cho đẹp vào, em trả gấp đôi. Coi như em đền chị một ông chồng, chị lời quá còn gì."
- Turn 2, 6.7–14.0s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, calm, every word weighed): "Tiền em cứ giữ lấy. Chị may áo hai mươi năm rồi em ạ. Nhìn dáng là biết số đo, nhìn mắt là biết lòng người."
- Pacing: @Vy speaks at an even everyday pace, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft whir of a measuring tape winding up, silk rustling, the ticking wall clock, a moped horn far down the street. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 4 (`canh-05/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Thu's narrow áo dài tailor shop on an old-quarter silk street by day: bolts of jewel-toned silk stacked on wooden shelves to the ceiling, two headless dress forms in half-finished áo dài, an old black sewing machine on a worn wooden table, a tall standing fitting mirror, a long cutting table with tailor's chalk and paper patterns, a small brass bell above the glass door, soft daylight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the narrow inner staircase, slow tilt down.
- Shot 2, 3–6s: 85mm close-up of the old woman at the foot of the stairs, locked off.
- Shot 3, 6–11s: 50mm over-the-shoulder shot from behind the old woman onto the tailor at the cutting table.
- Shot 4, 11–15s: 85mm close-up of the old woman perking up, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan comes down the last steps of the narrow inner staircase with her bamboo walking stick and is already speaking low and gleeful.
- 1–2s (Shot 1): @BaNhan keeps talking as she reaches the bottom step, eyes twinkling.
- 2–3s (Shot 1): @BaNhan keeps speaking and points the stick toward the glass door, while @Thu at the cutting table looks up with her mouth closed.
- 3–4s (CUT to Shot 2): @BaNhan keeps speaking in a conspiratorial voice, the stick still aimed at the door.
- 4–5s (Shot 2): @BaNhan keeps talking, patting the carved bamboo stick with a sly grin.
- 5–6s (Shot 2): @BaNhan finishes, closes her mouth and taps the stick on the floor.
- 6–7s (CUT to Shot 3): @Thu picks up a handwritten order slip with no readable writing from the cutting table and answers in an even voice.
- 7–8s (Shot 3): @Thu keeps speaking thoughtfully, turning the slip toward the light.
- 8–9s (Shot 3): @Thu keeps talking matter-of-factly and holds the order slip up between two fingers.
- 9–10s (Shot 3): @Thu keeps speaking, her eyes narrowing on the slip.
- 10–11s (Shot 3): @Thu finishes and closes her mouth, folding the slip into her apron pocket.
- 11–12s (CUT to Shot 4): @BaNhan perks up and answers quickly with a sly grin.
- 12–13s (Shot 4): @BaNhan keeps talking fast, bobbing on her stick.
- 13–14s (Shot 4): @BaNhan keeps speaking eagerly, already turning toward the glass door.
- 14–15s (Shot 4): @BaNhan finishes and closes her mouth, bobbing her head eagerly toward the door, grinning. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, low, gleeful and conspiratorial): "Mẹ đứng ngay trên cầu thang nghe hết rồi. Con bé ấy có chồng, mẹ cá cả cái gậy này."
- Turn 2, 6.2–10.5s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, thoughtful and matter-of-fact): "Con cũng ngờ thế. Phiếu đặt may nó ghi quê Nam Định. Con định về tận nơi."
- Turn 3, 11.0–14.1s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking quickly in short lively phrases, every word still clear, perking up, eager): "Về tận nơi à? Cho mẹ đi với, ở nhà mãi mốc cả người!"
- Pacing: @BaNhan speaks at an even everyday pace, then @Thu answers at an even everyday pace, then @BaNhan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the brass bell still tinkling faintly, a bamboo stick tapping on wooden stairs, paper rustling, street noise outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 1 (`canh-06/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 28mm wide shot from the altar side over the round dining table, slow dolly-in.
- Shot 2, 3–5s: 50mm medium shot of the husband at the table with a fruit basket, slow pan.
- Shot 3, 5–10s: 85mm close-up of the wife reading the papers, locked off.
- Shot 4, 10–15s: 50mm over-the-shoulder shot from behind the wife onto the husband, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tung comes in carrying a big cellophane-wrapped fruit basket and is already speaking sweetly with an eager smile, while @Thu sits at the cleared dining table with her mouth closed.
- 1–2s (Shot 1): @Tung sets the basket on the table and keeps talking, too sweet.
- 2–3s (Shot 1): @Tung keeps speaking as he slides a thick stack of papers with no readable writing and a pen across to @Thu.
- 3–4s (CUT to Shot 2): @Tung keeps talking, tapping the pen on the stack.
- 4–5s (Shot 2): @Tung keeps speaking with a pleading tilt of his head.
- 5–6s (CUT to Shot 3): @Tung finishes his request and closes his mouth, and @Thu draws the stack toward herself without touching the pen and answers slowly.
- 6–7s (Shot 3): @Thu keeps speaking politely, unhurried, her eyes on the first page.
- 7–8s (Shot 3): @Thu keeps speaking evenly, turning the first page with one finger.
- 8–9s (Shot 3): @Thu keeps talking, reading line by line.
- 9–10s (Shot 3): @Thu keeps speaking softly without looking up.
- 10–11s (CUT to Shot 4): @Thu finishes and closes her mouth, still reading, and @Tung nudges the fruit basket toward her and adds a quick eager remark.
- 11–12s (Shot 4): @Tung keeps talking fast, his smile fixed, patting the cellophane.
- 12–13s (Shot 4): @Tung keeps speaking eagerly, leaning over the table.
- 13–14s (Shot 4): @Tung finishes and closes his mouth, his fingers drumming on the tabletop.
- 14–15s (Shot 4): @Tung watches her with a fixed smile, mouth closed, while @Thu turns another page in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, sugary, a little too sweet): "Mình ơi, ký giúp anh mấy tờ vay ngân hàng nhé, công trình mới đang cần vốn gấp lắm."
- Turn 2, 5.7–10.2s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, unhurried and polite): "Anh cứ để đấy. Giấy tờ thì em phải đọc đã, ký rồi khó rút lại."
- Turn 3, 10.7–13.7s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, overeager, nudging the basket): "Anh mua cả giỏ hoa quả cho mình đây này, toàn hàng nhập đấy!"
- Pacing: @Tung speaks at an even everyday pace, then @Thu answers slowly and calmly, then @Tung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: cellophane crinkling, paper sliding across wood, a pen rolling, fingers drumming on a table. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 2 (`canh-06/clip-2.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the wife onto the husband, holding the previous framing.
- Shot 2, 5–8s: 85mm close-up of the wife lifting her eyes from the page, slow push-in.
- Shot 3, 8–10s: 40mm medium two-shot across the table, locked off.
- Shot 4, 10–13s: 85mm close-up of the husband, locked off.
- Shot 5, 13–15s: 40mm medium two-shot across the table, slow push-in toward the pen between them.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tung leans over the table and is already speaking fast and impatiently, poking the pen at a corner of the page.
- 1–2s (Shot 1): @Tung keeps talking over her, tapping the pen on the stack, while @Thu turns the pages slowly with her mouth closed.
- 2–3s (Shot 1): @Tung keeps speaking fast, flapping his free hand at the papers.
- 3–4s (Shot 1): @Tung keeps talking, jabbing the pen at the place to sign.
- 4–5s (Shot 1): @Tung finishes, closes his mouth and holds out the pen.
- 5–6s (CUT to Shot 2): @Thu stops on one page, lifts her eyes to his face and starts asking slowly.
- 6–7s (Shot 2): @Thu keeps asking in a level voice, her eyes never leaving him.
- 7–8s (Shot 2): @Thu keeps speaking quietly, each word placed with care.
- 8–9s (CUT to Shot 3): @Thu keeps talking, one finger laid on the page with no readable writing.
- 9–10s (Shot 3): @Thu finishes the question and closes her mouth, while @Tung's jaw tightens.
- 10–11s (CUT to Shot 4): @Tung snaps back fast, waving the pen.
- 11–12s (Shot 4): @Tung keeps talking loudly, his face reddening.
- 12–13s (Shot 4): @Tung keeps shouting, flicking the stack of papers with the back of his hand.
- 13–14s (CUT to Shot 5): @Tung finishes and closes his mouth, breathing hard, a bead of sweat sliding from his temple.
- 14–15s (Shot 5): @Thu holds his gaze in silence while the pen hangs in the air between them, both mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, impatient, talking over her): "Đọc làm gì cho mất thời gian! Toàn chữ chuyên môn thôi, em cứ ký vào chỗ đánh dấu là xong!"
- Turn 2, 5.3–9.8s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, level and piercing): "Em đọc rồi. Sao trang đầu lại là hợp đồng tặng cho nhà đất hả anh?"
- Turn 3, 10.3–13.3s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, caught out, blustering): "Thủ tục nó bắt thế! Đàn bà biết gì mà hỏi! Ký nhanh lên!"
- Pacing: @Tung speaks quickly, then @Thu answers slowly and calmly, then @Tung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pages turning, a pen clicking, the clock ticking loud in the silence, a moped passing in the alley. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 3 (`canh-06/clip-3.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot across the table, holding the previous framing.
- Shot 2, 5–8s: 85mm close-up of the wife laying the pen down, locked off.
- Shot 3, 8–10s: 50mm over-the-shoulder shot from behind the husband onto the wife, locked off.
- Shot 4, 10–13s: 85mm close-up of the husband sneering, locked off.
- Shot 5, 13–15s: 35mm medium shot past the wife at the table as the husband turns toward the staircase, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tung rises from his stool and is already speaking fast and loud, his face flushed.
- 1–2s (Shot 1): @Tung keeps shouting, sweeping one arm around at the house, while @Thu sits perfectly still with her mouth closed.
- 2–3s (Shot 1): @Tung keeps talking loudly, jabbing a thumb at his own chest.
- 3–4s (Shot 1): @Tung keeps shouting, leaning both palms on the tabletop and rattling the teacups.
- 4–5s (Shot 1): @Tung finishes and closes his mouth, and @Thu lays the pen down on the papers and starts answering slowly and coldly.
- 5–6s (CUT to Shot 2): @Thu keeps speaking calmly, folding her hands on the stack of papers.
- 6–7s (Shot 2): @Thu keeps talking in a cold, even voice, her eyes level on @Tung.
- 7–8s (Shot 2): @Thu keeps speaking slowly, lifting one finger as she makes each point, while @Tung listens with his mouth closed.
- 8–9s (CUT to Shot 3): @Thu keeps talking, perfectly calm, while @Tung's breathing grows heavy.
- 9–10s (Shot 3): @Thu finishes and closes her mouth, holding his gaze.
- 10–11s (CUT to Shot 4): @Tung sneers and snaps back fast from across the table.
- 11–12s (Shot 4): @Tung keeps talking with his lip curling, miming a needle and thread with his fingers.
- 12–13s (Shot 4): @Tung keeps speaking fast, miming a tape measure stretched between his hands.
- 13–14s (CUT to Shot 5): @Tung finishes and closes his mouth, his nostrils flaring.
- 14–15s (Shot 5): @Tung turns on his heel toward the steep tiled staircase while @Thu squares the stack of papers with both hands in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, loud, red-faced, cornered): "Đã thế thì nói thẳng! Tôi muốn ly hôn. Nhà này, công ty này, một tay tôi gây dựng!"
- Turn 2, 4.9–9.9s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, cold and perfectly calm): "Ly hôn thì được. Nhưng ký gì, ký lúc nào, ở đâu, trước mặt ai, là em chọn."
- Turn 3, 10.4–13.4s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, sneering, contemptuous): "Cô lấy gì mà chọn? Cô chỉ biết cầm kim với thước dây thôi!"
- Pacing: @Tung speaks quickly, then @Thu answers slowly and calmly, then @Tung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a palm thudding on wood, teacups rattling, heavy footsteps stomping up tiled stairs, then the clock ticking in the silence. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 4 (`canh-06/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the girl on a middle step of the staircase, locked off.
- Shot 2, 3–7s: 85mm close-up of the girl hugging her knees, locked off.
- Shot 3, 7–11s: 50mm over-the-shoulder shot from behind the girl onto the mother sitting beside her.
- Shot 4, 11–15s: 85mm close-up two-shot of mother and daughter on the step, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Na sits hunched on a middle step of the dim staircase hugging her knees and is already speaking in a small hushed voice, while @Thu comes to the foot of the stairs, mouth closed.
- 1–2s (Shot 1): @Na keeps whispering, glancing up toward the dark upper floor.
- 2–3s (Shot 1): @Na keeps speaking softly, her chin trembling.
- 3–4s (CUT to Shot 2): @Na keeps talking in a hushed voice, blinking hard.
- 4–5s (Shot 2): @Na keeps speaking, squeezing her knees tighter.
- 5–6s (Shot 2): @Na keeps whispering, a tear welling in one eye.
- 6–7s (Shot 2): @Na finishes and rests her chin on her knees, mouth closed, as @Thu climbs the steps toward her.
- 7–8s (CUT to Shot 3): @Thu sits down on the step beside her and starts answering slowly and steadily.
- 8–9s (Shot 3): @Thu keeps speaking gently, her eyes on her daughter's face.
- 9–10s (Shot 3): @Thu keeps talking tenderly, shaking her head once.
- 10–11s (Shot 3): @Thu keeps speaking slowly as she tucks a loose pigtail behind @Na's ear.
- 11–12s (CUT to Shot 4): @Thu keeps talking softly, lifting @Na's chin with one finger.
- 12–13s (Shot 4): @Thu keeps speaking in a steady low voice, her gaze lifting up the dark staircase.
- 13–14s (Shot 4): @Thu finishes and closes her mouth, her jaw quietly set.
- 14–15s (Shot 4): @Na leans her head against her mother's arm, and both look up the dark staircase in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.8s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking at a natural, even conversational pace, hushed, trying not to cry): "Mẹ ơi, bố sắp sang ở với cô váy đỏ à? Cô ấy bảo con gọi là mẹ hai, con không muốn gọi đâu."
- Turn 2, 7.3–13.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, steady and tender): "Không muốn thì con không phải gọi. Con chỉ có một mẹ thôi, nhớ chưa con? Còn mẹ hai thì để mẹ tính."
- Pacing: @Na speaks at an even everyday pace, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a television murmuring faintly upstairs, the clock ticking, a soft sniffle, a moped fading away in the alley. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 1 (`canh-07/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Daytime inside the family's narrow tube house in an old-quarter alley: a ground-floor living room with a carved wooden sofa set and a low tea table, a steep tiled staircase, a family altar shelf with incense, a potted orchid, sunlight through the open folding wooden door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the visitor in the open doorway, slow push-in.
- Shot 2, 3–5s: 85mm close-up of the visitor's smooth smile, locked off.
- Shot 3, 5–10s: 50mm medium shot of the old woman on the carved sofa with her teacup, locked off.
- Shot 4, 10–15s: 85mm close-up of the visitor looking down at his folder, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai steps in through the open folding wooden door with a little bow and is already speaking politely in a smooth, oily voice, a black leather document folder tucked under his arm upside down.
- 1–2s (Shot 1): @Khai keeps talking smoothly, a corner of paper with no readable writing slipping out of the bottom edge of the folder.
- 2–3s (Shot 1): @Khai keeps speaking, his smile widening.
- 3–4s (CUT to Shot 2): @Khai keeps talking, smoothing his styled hair with one hand.
- 4–5s (Shot 2): @Khai finishes with another little bow and closes his mouth.
- 5–6s (CUT to Shot 3): @BaNhan, seated on the carved sofa with a teacup, nods her chin toward the folder and asks dryly.
- 6–7s (Shot 3): @BaNhan keeps talking, one eyebrow raised, looking him up and down.
- 7–8s (Shot 3): @BaNhan keeps speaking dryly, tapping the teacup with one fingernail.
- 8–9s (Shot 3): @BaNhan keeps talking, unimpressed, peering at the upside-down folder.
- 9–10s (Shot 3): @BaNhan finishes and closes her mouth, waiting, while @Khai listens with his mouth closed.
- 10–11s (CUT to Shot 4): @Khai glances down, sees the folder upside down, hurriedly flips it the right way up and blurts a quick apology.
- 11–12s (Shot 4): @Khai keeps talking fast in a flustered rush, his ears reddening.
- 12–13s (Shot 4): @Khai keeps speaking, a plain gold wedding ring glinting on his finger as he hugs the folder.
- 13–14s (Shot 4): @Khai finishes and closes his mouth, forcing a stiff smile.
- 14–15s (Shot 4): @Khai shifts his weight from foot to foot, the folder clutched to his chest, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking at a natural, even conversational pace, smooth and oily): "Cháu chào bà ạ. Cháu là luật sư, thay mặt anh Tùng đến làm việc với chị Thu."
- Turn 2, 5.4–9.7s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, dry and unimpressed): "Luật sư cơ à? Thế cậu cầm cái cặp ngược thế kia là theo luật nào?"
- Turn 3, 10.2–13.4s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking quickly in short lively phrases, every word still clear, flustered, flipping the folder): "Dạ, tại cháu vội quá ạ! Sáng nay tắc đường, cháu cuống hết cả lên."
- Pacing: @Khai speaks at an even everyday pace, then @BaNhan answers at an even everyday pace, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a moped buzzing past in the alley, a small teacup clinking on a tray, paper rustling, a rooster crowing somewhere. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 2 (`canh-07/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Daytime inside the family's narrow tube house in an old-quarter alley: a ground-floor living room with a carved wooden sofa set and a low tea table, a steep tiled staircase, a family altar shelf with incense, a potted orchid, sunlight through the open folding wooden door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the visitor sitting forward on the carved sofa, slow push-in.
- Shot 2, 3–5s: 85mm close-up of the visitor, locked off.
- Shot 3, 5–10s: 50mm over-the-shoulder shot from behind the visitor onto the wife, locked off.
- Shot 4, 10–15s: 40mm medium two-shot across the low tea table, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai sits forward on the carved sofa, fans sheets of paper with no readable writing across the low tea table and is already speaking fast and pushy, while @Thu sits opposite with her mouth closed.
- 1–2s (Shot 1): @Khai keeps talking, tapping each page with a fingertip, the gold wedding ring flashing on his hand.
- 2–3s (Shot 1): @Khai keeps talking fast, ticking off points on his fingers.
- 3–4s (CUT to Shot 2): @Khai leans in and keeps speaking quickly, his eyes hard behind the smile.
- 4–5s (Shot 2): @Khai keeps talking, wagging a pen toward @Thu.
- 5–6s (CUT to Shot 3): @Khai finishes with a slick little nod and closes his mouth, and @Thu lifts the clay teapot and answers slowly and dryly, without glancing at the papers.
- 6–7s (Shot 3): @Thu keeps speaking as she pours tea slowly into a small cup.
- 7–8s (Shot 3): @Thu keeps talking in a dry voice, her eyes on the teapot.
- 8–9s (Shot 3): @Thu keeps speaking evenly, setting the teapot down.
- 9–10s (Shot 3): @Thu keeps talking, sliding the cup across to @Khai with both hands.
- 10–11s (CUT to Shot 4): @Thu finishes and closes her mouth, and @Khai blinks and answers fast with a thin little laugh.
- 11–12s (Shot 4): @Khai keeps talking quickly, glancing from the cup to her face.
- 12–13s (Shot 4): @Khai keeps speaking, his pushy smile faltering.
- 13–14s (Shot 4): @Khai finishes and closes his mouth, frowning in confusion.
- 14–15s (Shot 4): @Thu sits back with her own cup, mouth closed, watching him over the rim. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking quickly in short lively phrases, every word still clear, pushy, rattling off terms): "Chị ký thuận tình, nhận một trăm triệu, để lại nhà với công ty. Ra toà là chị mất quyền nuôi con đấy."
- Turn 2, 5.7–10.2s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, dry, eyes on the teapot): "Một trăm triệu à? Còn rẻ hơn tiền vải cái áo cưới chị đang may đấy."
- Turn 3, 10.7–13.5s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking quickly in short lively phrases, every word still clear, thrown, a nervous laugh): "Vải gì cơ? Áo cưới của ai? Em không hiểu chị nói gì."
- Pacing: @Khai speaks quickly, then @Thu answers slowly and calmly, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper fanning across wood, tea pouring into a small cup, a cup set down on a wooden tray, the alley noise outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 3 (`canh-07/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Daytime inside the family's narrow tube house in an old-quarter alley: a ground-floor living room with a carved wooden sofa set and a low tea table, a steep tiled staircase, a family altar shelf with incense, a potted orchid, sunlight through the open folding wooden door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot across the low tea table, holding the previous framing.
- Shot 2, 5–9s: 50mm over-the-shoulder shot from behind the wife onto the visitor as he stands, slow tilt up.
- Shot 3, 9–12s: 85mm close-up of the wife with her teacup, locked off.
- Shot 4, 12–15s: 35mm medium shot of the wife at the tea table with the open folding door behind her, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu slides the papers back across the tea table toward @Khai with two fingers and is already speaking slowly and quietly.
- 1–2s (Shot 1): @Thu keeps speaking, her eyes dropping pointedly to the black leather folder on the sofa, while @Khai listens with his mouth closed.
- 2–3s (Shot 1): @Thu keeps talking in a cutting, unhurried voice, her face calm.
- 3–4s (Shot 1): @Thu keeps speaking softly as @Khai's ears redden.
- 4–5s (Shot 1): @Thu finishes, closes her mouth and sips her tea.
- 5–6s (CUT to Shot 2): @Khai springs up, scoops up the papers and the folder and answers fast, wagging a finger in the air.
- 6–7s (Shot 2): @Khai keeps talking loudly, the finger still wagging.
- 7–8s (Shot 2): @Khai keeps speaking fast and blustering, the folder clutched under his arm upside down again.
- 8–9s (Shot 2): @Khai keeps talking as he backs toward the open folding door.
- 9–10s (CUT to Shot 3): @Khai finishes and closes his mouth, and @Thu, without looking up, starts speaking slowly and mildly.
- 10–11s (Shot 3): @Thu keeps speaking calmly, turning her teacup a quarter turn on the table.
- 11–12s (Shot 3): @Thu keeps talking mildly, the faintest smile at the corner of her mouth.
- 12–13s (CUT to Shot 4): @Thu keeps speaking as @Khai stops in the open doorway behind her.
- 13–14s (Shot 4): @Thu finishes and closes her mouth, setting her cup down, while @Khai glances at the upside-down folder and flips it over.
- 14–15s (Shot 4): @Khai hurries out into the sunny alley with reddening ears, mouth closed, while @Thu stays seated in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, cutting and unhurried): "Cậu về bảo anh ấy tự đến mà nói, đừng thuê người cầm cặp ngược."
- Turn 2, 5.1–9.1s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking quickly in short lively phrases, every word still clear, blustering, wagging a finger): "Chị cứ đợi đấy! Rồi chị sẽ phải ân hận, đến lúc ấy đừng trách em không nói trước!"
- Turn 3, 9.6–13.3s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, mild, not looking up): "Cặp lại ngược rồi kìa cậu. Đi cẩn thận, kẻo rơi hết giấy."
- Pacing: @Thu speaks slowly and calmly, then @Khai answers quickly, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper sliding across wood, a sofa creaking, quick footsteps on tiles, the folding door rattling, the alley noise swelling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 4 (`canh-07/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Daytime inside the family's narrow tube house in an old-quarter alley: a ground-floor living room with a carved wooden sofa set and a low tea table, a steep tiled staircase, a family altar shelf with incense, a potted orchid, sunlight through the open folding wooden door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the old woman just inside the open door, slow push-in.
- Shot 2, 3–7s: 85mm close-up of the old woman's sly face, locked off.
- Shot 3, 7–11s: 50mm over-the-shoulder shot from behind the old woman onto the daughter-in-law.
- Shot 4, 11–15s: 40mm medium two-shot of both women at the open door, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan stands just inside the open folding door leaning on her bamboo walking stick, turns toward the room and is already speaking slyly.
- 1–2s (Shot 1): @BaNhan keeps talking, glancing back out at the sunny alley.
- 2–3s (Shot 1): @BaNhan keeps speaking, while @Thu comes down the last steps of the staircase with a cloth handbag, her mouth closed.
- 3–4s (CUT to Shot 2): @BaNhan wiggles her own ring finger and keeps speaking, eyes twinkling.
- 4–5s (Shot 2): @BaNhan keeps talking low, tapping her ring finger with her thumb.
- 5–6s (Shot 2): @BaNhan keeps speaking, one eyebrow cocked.
- 6–7s (Shot 2): @BaNhan finishes and closes her mouth, waiting.
- 7–8s (CUT to Shot 3): @Thu steps into her plastic sandals and answers slowly, a faint knowing smile on her lips.
- 8–9s (Shot 3): @Thu keeps speaking calmly, looking out at the alley.
- 9–10s (Shot 3): @Thu keeps talking in an even voice, settling the cloth handbag on her shoulder.
- 10–11s (Shot 3): @Thu keeps speaking, lifting two fingers side by side.
- 11–12s (CUT to Shot 4): @Thu keeps talking softly, while @BaNhan listens with her mouth closed.
- 12–13s (Shot 4): @Thu keeps speaking, her eyes steady on the alley.
- 13–14s (Shot 4): @Thu finishes and closes her mouth with a steady look out at the alley.
- 14–15s (Shot 4): @BaNhan's wrinkled face breaks into a knowing grin beside her, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.5s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, sly, eyes twinkling): "Con có để ý không? Cái nhẫn cậu luật sư đeo ấy, vàng trơn, giống hệt vết hằn trên tay con bé kia."
- Turn 2, 7.0–13.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, calm, a faint knowing smile): "Con thấy ngay từ lúc cậu ta gõ tay lên giấy tờ rồi. Nhẫn cưới thì bao giờ cũng phải có hai người đeo."
- Pacing: @BaNhan speaks at an even everyday pace, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the alley's morning bustle, a street vendor calling in the distance, sandals scuffing on the threshold, a bamboo stick tapping. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 1 (`canh-08/clip-1.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Daytime inside the family's narrow tube house in an old-quarter alley: a ground-floor living room with a carved wooden sofa set and a low tea table, a steep tiled staircase, a family altar shelf with incense, a potted orchid, sunlight through the open folding wooden door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the son hurrying in through the open folding door, slow pan.
- Shot 2, 3–5s: 85mm close-up of the son's overeager grin, locked off.
- Shot 3, 5–9s: 40mm medium two-shot of mother and son at the carved sofa, locked off.
- Shot 4, 9–12s: 85mm close-up of the old woman on the carved sofa, locked off.
- Shot 5, 12–15s: 50mm medium shot of the son, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tung hurries in through the open folding door, sets a large glossy gift box with a satin bow on the low tea table and is already speaking fast with an overeager grin.
- 1–2s (Shot 1): @Tung keeps talking quickly, waving toward the open door.
- 2–3s (Shot 1): @Tung keeps speaking, beaming at his mother on the carved sofa.
- 3–4s (CUT to Shot 2): @Tung keeps talking fast, patting the glossy gift box.
- 4–5s (Shot 2): @Tung finishes, rubbing his palms together hopefully, and closes his mouth.
- 5–6s (CUT to Shot 3): @BaNhan squints past him toward the door and answers in a vague, wandering voice, while @Tung listens with his mouth closed.
- 6–7s (Shot 3): @BaNhan keeps answering slowly, tilting her head as if confused.
- 7–8s (Shot 3): @BaNhan keeps speaking, peering harder toward the doorway.
- 8–9s (Shot 3): @BaNhan keeps talking vaguely, while @Tung's grin freezes.
- 9–10s (CUT to Shot 4): @BaNhan keeps speaking slowly, blinking innocently at the doorway.
- 10–11s (Shot 4): @BaNhan keeps talking, nodding as if approving a new maid.
- 11–12s (Shot 4): @BaNhan finishes and closes her mouth, her face blank and innocent.
- 12–13s (CUT to Shot 5): @Tung rubs the back of his neck and hisses a quick protest.
- 13–14s (Shot 5): @Tung finishes hissing through his teeth and closes his mouth.
- 14–15s (Shot 5): @Tung casts a pleading glance toward the open door, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.0s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, jittery and overeager): "Mẹ, đây là Vy, sắp làm con dâu mẹ. Mẹ chúc phúc cho chúng con đi, cô ấy có quà biếu mẹ."
- Turn 2, 5.5–11.7s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking slowly and softly, unhurried, with a short natural pause between phrases, vague and wandering, feigning confusion): "Con dâu mẹ đang ở tiệm may cơ mà. Cô này là giúp việc mới à? Trông cũng sáng sủa đấy."
- Turn 3, 12.2–13.5s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, mortified, hissing): "Mẹ! Cô ấy nghe thấy đấy!"
- Pacing: @Tung speaks quickly, then @BaNhan answers slowly and calmly, then @Tung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a gift box set down on wood, a bamboo stick tapping on tiles, the alley's Sunday chatter, a caged bird chirping next door. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 2 (`canh-08/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Daytime inside the family's narrow tube house in an old-quarter alley: a ground-floor living room with a carved wooden sofa set and a low tea table, a steep tiled staircase, a family altar shelf with incense, a potted orchid, sunlight through the open folding wooden door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the old woman at the foot of the staircase in three-quarter profile, slow push-in.
- Shot 2, 3–6s: 85mm close-up of the old woman's deadpan face, locked off.
- Shot 3, 6–11s: 50mm over-the-shoulder shot from behind the old woman onto the young woman at the door.
- Shot 4, 11–15s: 40mm medium two-shot from inside the room by the folding door, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan hobbles to a plastic bucket at the foot of the staircase, lifts the string mop out of it and is already speaking deadpan.
- 1–2s (Shot 1): @BaNhan holds the mop out toward the doorway and keeps talking as @Vy steps in through the folding door with a sweet smile, mouth closed.
- 2–3s (Shot 1): @BaNhan keeps speaking, her face perfectly blank, the mop dripping onto the tiles.
- 3–4s (CUT to Shot 2): @BaNhan keeps talking, counting off on her thin fingers.
- 4–5s (Shot 2): @BaNhan keeps speaking dead seriously, the mop still held out.
- 5–6s (Shot 2): @BaNhan finishes with one firm nod and closes her mouth.
- 6–7s (CUT to Shot 3): @Vy, in her crimson dress and beige high heels, gives a tinkling little laugh and answers fast and sugary.
- 7–8s (Shot 3): @Vy keeps talking sweetly, a hand pressed to her chest, her voice pitched too high.
- 8–9s (Shot 3): @Vy keeps speaking with a fixed smile, glancing at the dripping mop.
- 9–10s (Shot 3): @Vy keeps talking fast, shaking her head at the mop.
- 10–11s (Shot 3): @Vy finishes and closes her mouth, her smile stretched wide.
- 11–12s (CUT to Shot 4): @BaNhan answers in a bone-dry voice without a flicker, the mop still held out.
- 12–13s (Shot 4): @BaNhan keeps speaking slowly, unblinking, while @Vy listens with her mouth closed.
- 13–14s (Shot 4): @BaNhan keeps talking as @Vy's smile cracks and she takes the mop handle between two fingers.
- 14–15s (Shot 4): @BaNhan finishes and closes her mouth, while @Vy holds the mop at arm's length. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, deadpan and dead serious): "Vào đây cháu. Cầm lấy cái này, nhà này ngày nào cũng phải lau ba lần đấy, sáng, trưa, tối."
- Turn 2, 6.2–10.6s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, forced sweetness, voice too high): "Bà ơi, cháu là người yêu anh Tùng, sắp về làm dâu nhà mình ạ! Cháu không phải người làm đâu!"
- Turn 3, 11.1–14.1s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking slowly and softly, unhurried, with a short natural pause between phrases, unblinking, bone-dry): "Ừ, thế thì càng phải lau, cho quen tay đi."
- Pacing: @BaNhan speaks at an even everyday pace, then @Vy answers quickly, then @BaNhan answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water sloshing in a bucket, high heels clicking on tiles, a tinkling forced laugh, the alley's Sunday chatter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 3 (`canh-08/clip-3.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Daytime inside the family's narrow tube house in an old-quarter alley: a ground-floor living room with a carved wooden sofa set and a low tea table, a steep tiled staircase, a family altar shelf with incense, a potted orchid, sunlight through the open folding wooden door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 40mm medium two-shot from inside the room by the folding door, holding the previous framing.
- Shot 2, 3–6s: 85mm close-up of the old woman on the carved sofa with her teacup, locked off.
- Shot 3, 6–10s: 50mm medium shot of the young woman mopping by the altar cabinet, low angle, slow lateral track.
- Shot 4, 10–13s: 85mm close-up of the old woman cupping her ear, locked off.
- Shot 5, 13–15s: 35mm medium two-shot across the living room, the carved sofa and the bucket in frame, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan settles back on the carved sofa and is already speaking slowly, pointing her bamboo stick at the gap under the low wooden cabinet beneath the altar shelf, while @Vy mops the tiles, mouth closed.
- 1–2s (Shot 1): @BaNhan keeps speaking in a lordly voice, while @Vy mops in her crimson dress and beige high heels, her mouth closed.
- 2–3s (Shot 1): @BaNhan picks up her teacup and keeps talking, savoring every word.
- 3–4s (CUT to Shot 2): @BaNhan keeps speaking slowly, the teacup held under her chin.
- 4–5s (Shot 2): @BaNhan keeps talking, blowing gently on her tea.
- 5–6s (Shot 2): @BaNhan finishes, closes her mouth and lets her eyes droop shut as if dozing.
- 6–7s (CUT to Shot 3): @Vy bends low to reach the mop under the cabinet, wobbling on her high heels, and mutters fast under her breath, her face turned to the camera.
- 7–8s (Shot 3): @Vy keeps muttering sourly, her lip curling.
- 8–9s (Shot 3): @Vy keeps whispering through clenched teeth, poking the mop under the cabinet.
- 9–10s (Shot 3): @Vy finishes muttering, closes her mouth and wrings the mop out into the bucket with a hard twist.
- 10–11s (CUT to Shot 4): @BaNhan opens one eye and asks loudly and innocently, cupping a hand to her ear.
- 11–12s (Shot 4): @BaNhan keeps talking loudly, leaning toward @Vy.
- 12–13s (Shot 4): @BaNhan keeps speaking, tapping her own ear with one finger.
- 13–14s (CUT to Shot 5): @BaNhan keeps talking, eyebrows raised in innocence, while @Vy freezes over the bucket with a stiff fake smile.
- 14–15s (Shot 5): @BaNhan finishes, closes her mouth and quietly slips a tiny notebook with no readable writing out of her cardigan pocket. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking slowly and softly, unhurried, with a short natural pause between phrases, lordly, savoring it): "Gầm tủ nữa cháu. Con dâu cả nhà này lau bao năm nay, chưa kêu một câu nào."
- Turn 2, 6.2–10.0s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, sour, muttering under her breath): "Bà già lẩm cẩm. Đợi sang tên xong, tôi tống bà vào viện dưỡng lão cho rảnh nợ."
- Turn 3, 10.5–14.2s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, loud, innocently deaf): "Cháu nói gì đấy? Bà nghễnh ngãng, nói to lên cho bà nghe với."
- Pacing: @BaNhan speaks slowly and calmly, then @Vy answers quickly, then @BaNhan answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a wet mop swishing across tiles, water dripping into a bucket, high heels wobbling on the floor, a teacup clinking, the clock ticking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 4 (`canh-08/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 50mm medium shot of the old woman at the round table holding up a tiny notebook, slow push-in.
- Shot 2, 3–6s: 85mm close-up of the old woman's sly grin, locked off.
- Shot 3, 6–11s: 50mm over-the-shoulder shot from behind the old woman onto the daughter-in-law, locked off.
- Shot 4, 11–15s: 40mm medium two-shot across the round table, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan sits at the round dining table, holds up a tiny worn notebook with no readable writing and is already speaking with a sly grin, while @Thu comes in with her cloth handbag still on her shoulder, mouth closed.
- 1–2s (Shot 1): @BaNhan keeps talking, tapping the notebook cover, as @Thu sits down opposite her.
- 2–3s (Shot 1): @BaNhan keeps speaking, savoring every word, her eyebrows dancing.
- 3–4s (CUT to Shot 2): @BaNhan flips the little notebook open toward @Thu, its pages showing no readable writing, and keeps speaking.
- 4–5s (Shot 2): @BaNhan keeps talking, running a bony finger down the page.
- 5–6s (Shot 2): @BaNhan keeps speaking with a satisfied little sniff.
- 6–7s (CUT to Shot 3): @BaNhan finishes and closes her mouth, grinning, and @Thu's lips twitch as she answers with a half smile.
- 7–8s (Shot 3): @Thu keeps speaking softly, shaking her head in mock wonder.
- 8–9s (Shot 3): @Thu keeps talking, setting her cloth handbag down on a stool.
- 9–10s (Shot 3): @Thu keeps speaking, a soft laugh in her voice.
- 10–11s (Shot 3): @Thu finishes and closes her mouth, smiling.
- 11–12s (CUT to Shot 4): @BaNhan chuckles and answers with a quick reply, while @Thu's shoulders shake with a silent laugh, mouth closed.
- 12–13s (Shot 4): @BaNhan keeps talking through a chuckle, tucking the notebook back into her cardigan pocket.
- 13–14s (Shot 4): @BaNhan keeps speaking, wagging a finger, pleased with herself.
- 14–15s (Shot 4): @BaNhan finishes, closes her mouth and gives @Thu a slow wink while @Thu smiles. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.2s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, sly, enjoying every word): "Con giúp việc mới hôm nay hứa tống mẹ ra khỏi nhà đấy. Mẹ chép vào sổ cả rồi, từng chữ một."
- Turn 2, 6.7–10.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, a soft half smile in the voice): "Mẹ giả lẫn khéo thế, con suýt tin mẹ lẫn thật. Mẹ đóng phim được đấy."
- Turn 3, 11.2–14.1s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking quickly in short lively phrases, every word still clear, chuckling, pleased with herself): "Con lạ gì mẹ nữa, già thì phải diễn cho ra già chứ!"
- Pacing: @BaNhan speaks at an even everyday pace, then @Thu answers at an even everyday pace, then @BaNhan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a tiny notebook's pages flicking, a soft breath of laughter, rice scooped into a bowl, the clock ticking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 1 (`canh-09/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A quiet village house in the Red River Delta in the afternoon: a yellow-walled single-storey house with a tiled roof, a brick-paved front yard with areca palms and a water jar, an open front room with a wooden altar and framed photos on the wall, soft green-gold light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium two-shot at the brick gate, the wife in front with the slip, gentle push-in.
- Shot 2, 5–11s: 85mm close-up of the old mother leaning on her bamboo stick, locked off.
- Shot 3, 11–13s: 50mm medium shot of the wife from inside the open front room, the yard behind her, locked off.
- Shot 4, 13–15s: 28mm wide shot from the front-room step onto the two women in the yard, slow drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu steps in through the brick gate of a yellow-walled village house with a gift basket on her arm and is already speaking matter-of-factly, holding up a small handwritten slip with no readable writing beside the gatepost, while @BaNhan shuffles in behind her on her bamboo stick, mouth closed.
- 1–2s (Shot 1): @Thu keeps talking, her eyes moving from the slip to the yellow wall of the house.
- 2–3s (Shot 1): @Thu keeps speaking evenly, nodding once toward the open front room.
- 3–4s (Shot 1): @Thu keeps talking as she folds the slip into her blouse pocket.
- 4–5s (Shot 1): @Thu finishes and closes her mouth, while @BaNhan stops beside her, catching her breath.
- 5–6s (CUT to Shot 2): @BaNhan presses one hand to the small of her back and starts grumbling in a dry comic voice, her wrinkled face screwed up in mock pain.
- 6–7s (Shot 2): @BaNhan keeps grumbling, rubbing her lower back with her knuckles.
- 7–8s (Shot 2): @BaNhan keeps talking, glaring at the yellow house.
- 8–9s (Shot 2): @BaNhan keeps complaining, jabbing her bamboo stick toward the house.
- 9–10s (Shot 2): @BaNhan keeps going, tapping the stick on the bricks with each word.
- 10–11s (Shot 2): @BaNhan finishes with a sniff and closes her mouth.
- 11–12s (CUT to Shot 3): @Thu, hiding a smile, turns toward the open front room and answers quietly, lifting her chin at the wall inside.
- 12–13s (Shot 3): @Thu keeps speaking softly, her eyes on the yellow wall inside, while @BaNhan follows her gaze, mouth closed.
- 13–14s (CUT to Shot 4): @Thu finishes and closes her mouth, a knowing look in her eyes.
- 14–15s (Shot 4): @BaNhan squints toward the front room and lifts a hand to shade her eyes, while @Thu waits beside her with the gift basket, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, matter-of-fact, checking the slip): "Số nhà, tên xóm khớp hết với phiếu may cô ấy ghi. Đúng nhà này rồi mẹ."
- Turn 2, 5.2–10.5s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, grumpy and comic): "Ba tiếng ngồi xe khách, lưng mẹ gãy làm đôi rồi. Chẳng có gì thì con cõng mẹ về đấy."
- Turn 3, 11.0–13.5s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, quiet, a little knowing): "Có đấy mẹ ạ. Trên tường gian thờ kia kìa."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: chickens clucking in a neighbour's yard, areca leaves rustling, a distant motorbike on a village road, a bamboo stick tapping on bricks. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 2 (`canh-09/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A quiet village house in the Red River Delta in the afternoon: a yellow-walled single-storey house with a tiled roof, a brick-paved front yard with areca palms and a water jar, an open front room with a wooden altar and framed photos on the wall, soft green-gold light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot from the side wall, the two women in profile gazing up at the framed wedding photo on the wall at frame left, locked off.
- Shot 2, 5–10s: 85mm close-up of the wife looking up at the photo, locked off.
- Shot 3, 10–15s: 40mm medium two-shot of the two women beside the altar, slow lateral slide.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan stands beside @Thu beneath a large framed wedding photo on the yellow wall above a wooden altar, squints up at the bride and is already speaking, pointing her bamboo stick at the frame, while @Thu looks up with her mouth closed.
- 1–2s (Shot 1): In the frame a bride with long wavy dark-brown hair and winged eyeliner in a white gown smiles beside a lean groom with a styled black undercut and a thin moustache, while @BaNhan keeps talking, leaning closer on her stick.
- 2–3s (Shot 1): @BaNhan keeps talking, screwing up her eyes at the bride's wavy hair as incense smoke drifts across the glass.
- 3–4s (Shot 1): @BaNhan keeps going, turning her head toward @Thu, eyebrows knitted.
- 4–5s (Shot 1): @BaNhan finishes her question, closes her mouth and waits.
- 5–6s (CUT to Shot 2): @Thu, eyes still on the photo, answers slowly and quietly.
- 6–7s (Shot 2): @Thu keeps speaking low and steady, lifting her chin toward the groom in the frame.
- 7–8s (Shot 2): @Thu keeps talking, her gaze fixed on the thin moustache in the photo.
- 8–9s (Shot 2): @Thu keeps going slowly, her face perfectly calm.
- 9–10s (Shot 2): @Thu keeps speaking, finishing in the same low voice.
- 10–11s (CUT to Shot 3): @Thu closes her mouth as @BaNhan peers up at the groom's thin moustache, her jaw drops, and she blurts out a fast reply.
- 11–12s (Shot 3): @BaNhan keeps talking fast, jabbing her stick toward the groom, while @Thu stands beside her with her mouth closed.
- 12–13s (Shot 3): @BaNhan keeps going, flapping a hand at the photo, her eyebrows flying up.
- 13–14s (Shot 3): @BaNhan finishes and closes her mouth, turning to stare at @Thu.
- 14–15s (Shot 3): @Thu keeps her eyes on the wedding photo, lips pressed together, while @BaNhan waits beside her with her eyebrows high, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, squinting, puzzled): "Cô dâu trông quen quen. Phải con bé váy đỏ lau nhà cho mẹ hôm nọ không?"
- Turn 2, 5.4–9.6s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, low and steady): "Vâng, đúng nó đấy mẹ. Còn chú rể đứng bên cạnh, mẹ nhìn kỹ xem."
- Turn 3, 10.1–13.4s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking quickly in short lively phrases, every word still clear, stunned, then outraged): "Ối giời, cậu luật sư cầm cặp ngược! Hai đứa nó cưới nhau rồi à?"
- Pacing: @BaNhan speaks at an even everyday pace, then @Thu answers slowly and calmly, then @BaNhan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a slow wooden clock ticking, incense crackling softly, a rooster far off, a sharp intake of breath. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 3 (`canh-09/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A quiet village house in the Red River Delta in the afternoon: a yellow-walled single-storey house with a tiled roof, a brick-paved front yard with areca palms and a water jar, an open front room with a wooden altar and framed photos on the wall, soft green-gold light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 40mm medium two-shot of the two women beside the altar, holding the previous framing.
- Shot 2, 4–9s: 85mm close-up of the old mother, incense smoke behind her, locked off.
- Shot 3, 9–12s: 50mm over-the-shoulder shot from behind the old mother onto the wife.
- Shot 4, 12–15s: 50mm medium profile shot of the wife lifting the phone toward the photo on the wall, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu, still looking up at the wedding photo, is already speaking quietly and with certainty, while @BaNhan stands beside her leaning on her bamboo stick, mouth closed.
- 1–2s (Shot 1): @Thu keeps speaking calmly, her hands folded over the handle of the gift basket.
- 2–3s (Shot 1): @Thu keeps talking, glancing out toward the brick yard and the neighbouring houses beyond the gate.
- 3–4s (Shot 1): @Thu finishes, turning back to the photo.
- 4–5s (CUT to Shot 2): @Thu closes her mouth as @BaNhan nods sharply at the photo and starts speaking briskly, flapping a hand toward @Thu's blouse pocket.
- 5–6s (Shot 2): @BaNhan keeps talking briskly, jabbing a bony finger up at the frame.
- 6–7s (Shot 2): @BaNhan keeps going, tapping her bamboo stick on the tiles for emphasis.
- 7–8s (Shot 2): @BaNhan keeps talking, miming taking a picture with her thin old hands.
- 8–9s (Shot 2): @BaNhan finishes, eyebrows raised, nodding firmly.
- 9–10s (CUT to Shot 3): @BaNhan closes her mouth as @Thu takes out a phone with a glowing blank screen and starts answering slowly and thoughtfully.
- 10–11s (Shot 3): @Thu keeps speaking, the glowing blank screen lighting her chin, while @BaNhan listens with her back to the camera, mouth closed.
- 11–12s (Shot 3): @Thu keeps talking in a low cool voice, turning the phone over in her fingers.
- 12–13s (CUT to Shot 4): @Thu raises the phone toward the wedding photo on the wall as she keeps speaking.
- 13–14s (Shot 4): @Thu finishes, her eyes on the photo, a small cold smile on her lips.
- 14–15s (Shot 4): @Thu closes her mouth and quietly takes one picture of the wedding photo, while @BaNhan beside her purses her lips and gives a slow approving nod, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.9s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, quiet and certain): "Ba năm rồi mẹ ạ. Cỗ bày kín sân, cả xóm ai cũng biết."
- Turn 2, 4.4–8.7s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, brisk, nudging): "Thế thì con chụp ngay lại đi, mang về cho thằng Tùng nó sáng mắt ra."
- Turn 3, 9.2–14.0s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, thoughtful, a little cold): "Chưa được đâu mẹ. Bây giờ anh ấy đang mù, ảnh gì cũng bảo là ảnh ghép."
- Pacing: @Thu speaks at an even everyday pace, then @BaNhan answers at an even everyday pace, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft phone camera click, incense crackling, chickens clucking outside, wind in the areca palms. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 4 (`canh-09/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A narrow brick lane through a Red River Delta village at sunset: bamboo hedges, a pond with ducks, rice fields glowing gold beyond the low houses.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of the two women walking toward the camera down the brick lane, slow dolly back.
- Shot 2, 5–10s: 85mm close-up of the wife against the golden rice fields, locked off.
- Shot 3, 10–13s: 50mm medium shot of the old mother on the lane, the sunset behind her, slow push-in.
- Shot 4, 13–15s: 28mm wide shot of the two women on the brick lane, the rice fields glowing beyond them, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan and @Thu walk slowly up a narrow brick lane between bamboo hedges toward the camera at sunset; @BaNhan is already speaking with a gossipy tilt of her head, while @Thu carries the empty gift basket with her mouth closed.
- 1–2s (Shot 1): @BaNhan keeps talking, her bamboo stick tapping the bricks, nodding back toward the village.
- 2–3s (Shot 1): @BaNhan keeps going, lowering her voice as if sharing a secret, a crooked grin on her face.
- 3–4s (Shot 1): @BaNhan turns her face up to @Thu and keeps speaking, her grin gone and her eyes sharp.
- 4–5s (Shot 1): @BaNhan keeps talking, ending on a pointed question.
- 5–6s (CUT to Shot 2): @BaNhan closes her mouth; @Thu stops walking, looks out over the golden rice fields and answers slowly and coldly.
- 6–7s (Shot 2): @Thu keeps speaking very quietly, the sunset light on her face, her eyes unblinking.
- 7–8s (Shot 2): @Thu keeps talking, her fingers tightening on the basket handle.
- 8–9s (Shot 2): @Thu keeps speaking in the same low voice, her jaw set.
- 9–10s (Shot 2): @Thu keeps going, finishing as ducks glide across a still pond behind her.
- 10–11s (CUT to Shot 3): @Thu closes her mouth; @BaNhan breaks into a slow sly smile and answers with a dry chuckle.
- 11–12s (Shot 3): @BaNhan keeps talking, relishing it, wagging one finger.
- 12–13s (Shot 3): @BaNhan keeps going, chuckling, her eyes twinkling.
- 13–14s (CUT to Shot 4): @BaNhan finishes and closes her mouth, nodding to herself.
- 14–15s (Shot 4): @BaNhan and @Thu walk on side by side down the golden lane, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking quickly in short lively phrases, every word still clear, gossipy, then pointed): "Hàng xóm bảo năm nào con bé cũng về khoe vớ được đại gia. Con còn đợi đến bao giờ?"
- Turn 2, 5.3–9.8s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, cold and very quiet): "Đến đúng hôm anh ấy tự tay trao sính lễ cho vợ người ta, mẹ ạ."
- Turn 3, 10.3–13.5s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, relishing it, a sly chuckle): "Hay đấy. Lúc ấy thì mẹ phải ngồi hàng đầu mà xem."
- Pacing: @BaNhan speaks quickly, then @Thu answers slowly and calmly, then @BaNhan answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ducks quacking on the pond, bamboo creaking in the evening breeze, crickets starting up, a bamboo stick tapping on bricks. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 1 (`canh-10/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
The pavement outside Thu's áo dài tailor shop on an old-quarter silk street by day: a glass shop door, potted plants, parked motorbikes, a black luxury sedan with no badge at the curb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium two-shot at child height, the woman crouching before the girl by the shop door, slow push-in.
- Shot 2, 6–10s: 85mm close-up of the girl hugging the pink tablet, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the girl onto the woman.
- Shot 4, 13–15s: 35mm wide shot along the pavement outside the tailor shop, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): On the sunny pavement outside the tailor shop, @Vy crouches in front of @Na beside the potted plants, holds out a pink tablet with a glowing blank screen and is already speaking in a honeyed voice, while @Na clutches her backpack straps, mouth closed.
- 1–2s (Shot 1): @Vy keeps talking sweetly, tilting the glowing tablet toward @Na.
- 2–3s (Shot 1): @Vy keeps going, pointing up toward the rooftops with a wide smile.
- 3–4s (Shot 1): @Vy keeps talking as she sets the pink tablet into @Na's small hands.
- 4–5s (Shot 1): @Vy keeps speaking, glancing at a black luxury sedan with no badge idling at the curb.
- 5–6s (Shot 1): @Vy finishes and closes her mouth, smiling, while @Na hugs the tablet to her chest.
- 6–7s (CUT to Shot 2): @Na bounces on her toes and asks a fast excited question, her bright eyes wide.
- 7–8s (Shot 2): @Na keeps talking excitedly, pigtails bobbing.
- 8–9s (Shot 2): @Na keeps going, miming a swimming stroke with one arm, the tablet under the other.
- 9–10s (Shot 2): @Na finishes and closes her mouth, grinning down at the glowing screen.
- 10–11s (CUT to Shot 3): @Vy answers with a sweet smile, tilting her head toward the shop's glass door.
- 11–12s (Shot 3): @Vy keeps speaking softly, her eyes flicking to the shop and back.
- 12–13s (Shot 3): @Vy keeps talking, her voice sugary, one eyebrow lifting slyly.
- 13–14s (CUT to Shot 4): @Vy finishes, closes her mouth and straightens up.
- 14–15s (Shot 4): @Vy's smile cools into a smirk as she glances at the shop's glass door, while @Na beams down at the glowing screen, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, honeyed and coaxing): "Quà của cô đây, máy tính bảng mới tinh. Cuối tuần sang nhà bố, có bể bơi trên tầng thượng nhé."
- Turn 2, 6.2–9.8s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, bubbling with excitement): "Thật ạ? Con mang cả phao vịt sang bơi được không cô? Con bơi giỏi lắm!"
- Turn 3, 10.3–13.8s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, sweet, faintly sly): "Mang gì cũng được. Ở tiệm may suốt ngày với mẹ, chán lắm nhỉ?"
- Pacing: @Vy speaks at an even everyday pace, then @Na answers quickly, then @Vy answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: motorbikes buzzing past, a car engine idling softly, sparrows chirping in the potted plants, a shop bell jingling faintly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 2 (`canh-10/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Thu's narrow áo dài tailor shop on an old-quarter silk street by day: bolts of jewel-toned silk stacked on wooden shelves to the ceiling, two headless dress forms in half-finished áo dài, an old black sewing machine on a worn wooden table, a tall standing fitting mirror, a long cutting table with tailor's chalk and paper patterns, a small brass bell above the glass door, soft daylight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot following the girl from the glass door to the cutting table.
- Shot 2, 4–10s: 85mm close-up of the mother at the cutting table, locked off.
- Shot 3, 10–13s: 40mm medium two-shot across the cutting table, slow drift.
- Shot 4, 13–15s: 28mm wide shot of the shop from the silk shelves, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): The brass bell jingles as @Na bursts in through the glass door of the tailor shop with the pink tablet under her arm and is already speaking fast and breathlessly.
- 1–2s (Shot 1): @Na keeps talking, hopping toward the cutting table with her hands clasped as if pleading.
- 2–3s (Shot 1): @Na keeps going, bouncing on her toes, eyes huge.
- 3–4s (Shot 1): @Na keeps pleading, leaning over the edge of the long cutting table.
- 4–5s (CUT to Shot 2): @Na closes her mouth; @Thu, chalk in hand at the cutting table, looks up and begins to answer slowly with a soft smile.
- 5–6s (Shot 2): @Thu keeps speaking gently as she sets the chalk down and picks up a small folded jacket.
- 6–7s (Shot 2): @Thu keeps talking, folding the small jacket carefully, her smile steady.
- 7–8s (Shot 2): @Thu keeps going slowly, tucking the folded jacket into an open school backpack on the table.
- 8–9s (Shot 2): @Thu keeps speaking, patting the backpack flat.
- 9–10s (Shot 2): @Thu keeps talking, finishing with a small nod, her eyes glistening.
- 10–11s (CUT to Shot 3): @Thu closes her mouth; @Na blinks up at her and asks a quick surprised question, tilting her head.
- 11–12s (Shot 3): @Na keeps talking, her face lighting up, while @Thu listens with her mouth closed.
- 12–13s (Shot 3): @Na keeps going, giggling, rubbing one eye in mock tears.
- 13–14s (CUT to Shot 4): @Na finishes, closes her mouth and twirls toward the door hugging the tablet.
- 14–15s (Shot 4): @Thu zips the backpack in silence, blinking hard, her eyes rimmed red behind the smile. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, breathless, pleading): "Mẹ ơi, bố cho con sang chơi hai hôm cơ! Mẹ cho con đi nhé, đi mà!"
- Turn 2, 4.7–10.0s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, gentle, swallowing the hurt): "Ừ, con đi đi. Nhớ mang áo khoác, trên cao gió lạnh lắm đấy. Mẹ gấp sẵn cho rồi."
- Turn 3, 10.5–13.8s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, surprised and delighted): "Mẹ không giận ạ? Con cứ tưởng mẹ không cho, con còn định khóc cơ."
- Pacing: @Na speaks quickly, then @Thu answers slowly and calmly, then @Na answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the brass door bell jingling, small running footsteps, a zip closing, street traffic muffled behind the glass. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 3 (`canh-10/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Night in Thu's narrow áo dài tailor shop: the steel shutter half down, a single warm desk lamp over the old black sewing machine, bolts of silk fading into shadow on the shelves, two headless dress forms, a long cutting table with paper patterns.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the old mother at the foot of the narrow inner staircase, locked off.
- Shot 2, 5–10s: 85mm close-up of the wife at the sewing machine in the lamplight, locked off.
- Shot 3, 10–15s: 40mm medium two-shot of the two women at the sewing machine, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Night in the tailor shop: @BaNhan comes down the narrow inner staircase in her cardigan, one hand on the rail, and is already speaking in a low disapproving voice, her eyes on the lamplit sewing machine across the room.
- 1–2s (Shot 1): @BaNhan keeps talking as she reaches the bottom step, her bamboo stick tapping the tiles.
- 2–3s (Shot 1): @BaNhan keeps speaking, shaking her head slowly.
- 3–4s (Shot 1): @BaNhan keeps going, pointing her stick toward a red silk wedding áo dài embroidered with a gold phoenix on a headless dress form.
- 4–5s (Shot 1): @BaNhan finishes and closes her mouth, waiting at the foot of the stairs.
- 5–6s (CUT to Shot 2): @Thu stops the treadle under the single warm desk lamp and answers without turning round, her eyes glistening.
- 6–7s (Shot 2): @Thu keeps speaking steadily, the red silk motionless under her hands.
- 7–8s (Shot 2): @Thu keeps talking, her lips trembling once before she steadies them.
- 8–9s (Shot 2): @Thu keeps going quietly, smoothing the red silk with both palms.
- 9–10s (Shot 2): @Thu keeps speaking, finishing in a near whisper.
- 10–11s (CUT to Shot 3): @Thu closes her mouth; @BaNhan lowers herself onto a stool beside her, peers at her face and adds a dry remark.
- 11–12s (Shot 3): @BaNhan keeps talking dryly, nodding at @Thu's red eyes, while @Thu keeps her mouth closed.
- 12–13s (Shot 3): @BaNhan keeps speaking, her voice softening.
- 13–14s (Shot 3): @BaNhan keeps going, finishing with a small sigh.
- 14–15s (Shot 3): @BaNhan closes her mouth and watches @Thu, while @Thu blinks fast in the lamplight, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, low and disapproving): "Con để cái Na sang ở với con hồ ly ấy thật à? Mẹ chịu con đấy."
- Turn 2, 5.4–10.2s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, steady, close to tears): "Cấm thì nó càng thèm, mẹ ạ. Cứ để nó sang, tự nhìn xem người lớn thật thế nào."
- Turn 3, 10.7–14.2s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, dry, softening): "Nói thì cứng lắm, mà mắt con đỏ hoe từ nãy rồi kìa."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the slow clatter of the treadle sewing machine, the desk lamp humming, a motorbike passing beyond the half-closed shutter, slippers on wooden stairs. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 4 (`canh-10/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Night in Thu's narrow áo dài tailor shop: the steel shutter half down, a single warm desk lamp over the old black sewing machine, bolts of silk fading into shadow on the shelves, two headless dress forms, a long cutting table with paper patterns.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot of the two women at the sewing machine, holding the previous framing.
- Shot 2, 5–9s: 85mm close-up of the old mother on the stool, lamplight on her wrinkles, locked off.
- Shot 3, 9–12s: 35mm medium two-shot beside the dress form, the old mother on her stool at frame left, locked off.
- Shot 4, 12–15s: 85mm close-up of the wife at the dress form, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu, a single tear sliding down her cheek, lets out a tiny wet laugh and is already speaking slowly, waving a hand near her eyes, while @BaNhan on the stool beside her watches with her mouth closed.
- 1–2s (Shot 1): @Thu keeps speaking, rubbing one eye with the back of her wrist.
- 2–3s (Shot 1): @Thu keeps talking, nodding at the heap of red silk as if blaming the dust.
- 3–4s (Shot 1): @Thu keeps going, sniffing once.
- 4–5s (Shot 1): @Thu finishes and closes her mouth, looking down at the silk.
- 5–6s (CUT to Shot 2): @BaNhan speaks gruffly and tenderly, nodding at the red silk wedding áo dài on the dress form.
- 6–7s (Shot 2): @BaNhan keeps talking, her old eyes soft, one bony finger miming a wipe under her own eye.
- 7–8s (Shot 2): @BaNhan keeps going, pursing her lips in mock sternness.
- 8–9s (Shot 2): @BaNhan keeps speaking, wagging the finger at the precious silk.
- 9–10s (CUT to Shot 3): @BaNhan closes her mouth; @Thu dabs the tear away with a fingertip, stands and answers slowly.
- 10–11s (Shot 3): @Thu keeps speaking as she runs the yellow measuring tape around the narrow waist of the red áo dài on the dress form.
- 11–12s (Shot 3): @Thu keeps talking warmly, pulling the tape snug, while @BaNhan listens on the stool with her mouth closed.
- 12–13s (CUT to Shot 4): @Thu keeps speaking, her hand resting on the waist seam.
- 13–14s (Shot 4): @Thu keeps going, smoothing the gold phoenix on the red silk with her palm, and finishes with a small smile.
- 14–15s (Shot 4): @Thu closes her mouth and keeps smoothing the gold phoenix with a quiet, certain look, silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, a tiny wet laugh): "Con có khóc đâu mẹ. Lụa đỏ nhiều bụi lắm, bay vào mắt đấy ạ."
- Turn 2, 5.1–9.4s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, gruff but tender): "Ừ, bụi thì lau đi. Nước mắt mà rơi vào áo của nó thì phí lụa."
- Turn 3, 9.9–14.1s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, warm, quietly sure): "Mẹ đừng lo. Áo này con may khít, ai mặc cũng phải đứng thật thẳng."
- Pacing: @Thu speaks slowly and calmly, then @BaNhan answers at an even everyday pace, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the desk lamp humming, a soft sniff, silk rustling under fingertips, the night street quiet beyond the shutter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 1 (`canh-11/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A glossy luxury apartment high above Hà Nội by day: floor-to-ceiling windows over the city with a rooftop pool glinting below, a white leather sofa, a marble kitchen island, cold bright daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium shot from the window side of the girl kneeling on the rug by the white leather sofa, the marble kitchen island behind her, locked off.
- Shot 2, 5–10s: 85mm close-up of the young woman, cold daylight on her face, locked off.
- Shot 3, 10–15s: 40mm medium two-shot by the white leather sofa, slow drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the glossy apartment by day, @Na kneels on the pale rug by the white leather sofa, holds up a crayon drawing of four smiling stick figures with no writing and is already speaking earnestly.
- 1–2s (Shot 1): @Na keeps talking proudly, pointing to each stick figure in turn.
- 2–3s (Shot 1): @Na keeps speaking, turning the drawing toward the marble kitchen island with a hopeful smile.
- 3–4s (Shot 1): @Na keeps going, holding the drawing up high in both hands; a fresh red crayon streak shows on one white cushion beside her.
- 4–5s (Shot 1): @Na finishes and closes her mouth as @Vy walks in from the kitchen island behind her.
- 5–6s (CUT to Shot 2): @Vy spots the red streak on the white leather, her eyes flaring, and starts speaking fast and cold, pointing at it.
- 6–7s (Shot 2): @Vy keeps talking sharply, her red lips tight, her finger jabbing toward the cushion.
- 7–8s (Shot 2): @Vy keeps going, her voice rising, her winged eyes narrowing.
- 8–9s (Shot 2): @Vy keeps speaking coldly, glancing from the streak down at the girl.
- 9–10s (Shot 2): @Vy keeps talking as she pulls a tissue from a box on the arm of the sofa.
- 10–11s (CUT to Shot 3): @Vy closes her mouth and scrubs at the red streak; @Na slowly lowers the drawing against her chest and says a small apology, her eyes on the rug.
- 11–12s (Shot 3): @Na keeps speaking in a small voice, lips trembling, while @Vy scrubs the leather with her mouth closed.
- 12–13s (Shot 3): @Na keeps going, her eyes still on the rug.
- 13–14s (Shot 3): @Na finishes and closes her mouth, sitting back on her heels.
- 14–15s (Shot 3): @Vy keeps scrubbing the leather without looking at @Na, her face cold, while @Na hugs the drawing, eyes wet, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking at a natural, even conversational pace, earnest and proud): "Cô ơi, con vẽ cả nhà mình. Bố, mẹ, bà nội, với con. Con tặng cô đấy."
- Turn 2, 5.4–10.4s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, cold and sharp): "Vẽ thì vẽ ra giấy! Bôi lên ghế da của cô à? Cái ghế này đắt hơn cả tiệm may của mẹ cháu đấy!"
- Turn 3, 10.9–13.6s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking at a natural, even conversational pace, small, eyes down): "Con xin lỗi cô, con không cố ý đâu ạ."
- Pacing: @Na speaks at an even everyday pace, then @Vy answers quickly, then @Na answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the hum of air conditioning, crayons rolling on a glass table, a tissue squeaking on leather, faint city traffic far below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 2 (`canh-11/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A glossy luxury apartment high above Hà Nội by day: floor-to-ceiling windows over the city with a rooftop pool glinting below, a white leather sofa, a marble kitchen island, cold bright daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 40mm medium two-shot by the white leather sofa, holding the previous framing.
- Shot 2, 6–10s: 85mm close-up of the girl on the white sofa, slow push-in.
- Shot 3, 10–15s: 50mm medium shot of the young woman at the floor-to-ceiling window, the city bright behind her, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): A phone with a glowing blank screen at her ear, @Vy straightens up from the sofa and is already speaking fast and low into it with an irritated roll of her eyes, while @Na kneels by the sofa with her drawing, mouth closed.
- 1–2s (Shot 1): @Vy keeps talking, turning her back on the sofa, her lip curling.
- 2–3s (Shot 1): @Vy keeps going, flicking a glance back over her shoulder toward @Na.
- 3–4s (Shot 1): @Vy keeps speaking low and fast, wrinkling her nose, as she walks toward the floor-to-ceiling window.
- 4–5s (Shot 1): @Vy keeps talking, her free hand on her hip, her voice flat and cold.
- 5–6s (Shot 1): @Vy finishes and closes her mouth, listening to the phone, her back to the room.
- 6–7s (CUT to Shot 2): On the white sofa @Na, who has heard every word, begins to whisper slowly to herself, her lips trembling.
- 7–8s (Shot 2): @Na keeps whispering, the crayon drawing crumpling in her small hands.
- 8–9s (Shot 2): @Na keeps whispering, her chin wobbling, her eyes on the floor.
- 9–10s (Shot 2): @Na whispers the last words and closes her mouth, a tear sliding down her round cheek.
- 10–11s (CUT to Shot 3): @Vy at the window glances toward the front door and speaks quickly into the phone again, suddenly brisk.
- 11–12s (Shot 3): @Vy keeps talking fast, tapping her long red nails on the window glass.
- 12–13s (Shot 3): @Vy keeps going, a sly smile at the city below.
- 13–14s (Shot 3): @Vy finishes and closes her mouth, lowering the phone.
- 14–15s (Shot 3): @Vy slips the phone into her small white handbag and smooths her hair, never turning round, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, irritated and low, on the phone): "Con bé lì lắm anh ạ. Xong vụ này là em tống nó về với bà mẹ bán áo. Nhìn mặt nó em ngứa mắt."
- Turn 2, 6.2–10.1s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking slowly and softly, unhurried, with a short natural pause between phrases, hushed, lips trembling): "Cô ấy ghét con thật rồi. Con chỉ muốn ở với mẹ thôi."
- Turn 3, 10.6–13.4s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, suddenly brisk, eyes on the door): "Thôi em cúp đây, lão ấy sắp về rồi. Tối mình nói tiếp."
- Pacing: @Vy speaks quickly, then @Na answers slowly and calmly, then @Vy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone buzzing, the hum of air conditioning, long fingernails tapping on glass, paper crinkling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 3 (`canh-11/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A glossy luxury apartment high above Hà Nội by day: floor-to-ceiling windows over the city with a rooftop pool glinting below, a white leather sofa, a marble kitchen island, cold bright daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium two-shot at the apartment door, low angle, locked off.
- Shot 2, 5–10s: 85mm close-up of the crouching father, locked off.
- Shot 3, 10–15s: 40mm medium two-shot by the door, the standing father and the girl looking up at him, slow drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): The apartment front door swings open and @Tung walks in loosening his tie, as @Na scrambles up from beside her small school backpack and is already speaking in a small pleading voice.
- 1–2s (Shot 1): @Na keeps talking, stepping toward him with the backpack in both arms, while @Tung crouches down to her eye level with his mouth closed.
- 2–3s (Shot 1): @Na keeps going, her chin quivering, glancing back toward the window.
- 3–4s (Shot 1): @Na keeps speaking, hugging the backpack tight.
- 4–5s (Shot 1): @Na finishes and closes her mouth, looking up at him with wet eyes.
- 5–6s (CUT to Shot 2): @Tung sighs and answers in a tired, even voice, glancing at a phone with a glowing blank screen in his hand.
- 6–7s (Shot 2): @Tung keeps talking, forcing a weary smile.
- 7–8s (Shot 2): @Tung keeps speaking, his thumb already scrolling on the phone.
- 8–9s (Shot 2): @Tung keeps going, nodding absently at the screen.
- 9–10s (Shot 2): @Tung finishes, closes his mouth and stands up, thumbing the phone.
- 10–11s (CUT to Shot 3): @Na looks up at him and says a quiet flat line, her eyes wet.
- 11–12s (Shot 3): @Na keeps speaking flatly, while @Tung reads his phone with his mouth closed.
- 12–13s (Shot 3): @Na keeps going, staring at the glowing phone in his hand.
- 13–14s (Shot 3): @Na finishes and closes her mouth, holding her backpack.
- 14–15s (Shot 3): @Na stays still by the door, eyes wet, while @Tung walks past her toward the window, his eyes on the phone, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking at a natural, even conversational pace, small and pleading): "Bố ơi, đưa con về đi. Lúc nãy cô ấy gọi điện, con nghe thấy hết rồi."
- Turn 2, 5.4–9.9s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, tired and dismissive): "Con nghe nhầm rồi. Cô thương con lắm, còn mua cả máy tính bảng cho con đấy thôi."
- Turn 3, 10.4–14.1s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking at a natural, even conversational pace, quiet and flat): "Bố cũng chẳng chịu nghe con nói. Bố chỉ cắm mặt vào máy thôi."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the apartment door clicking shut, a tie sliding loose, the hum of air conditioning, a small sniffle. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 4 (`canh-11/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Night in Thu's narrow áo dài tailor shop: the steel shutter half down, a single warm desk lamp over the old black sewing machine, bolts of silk fading into shadow on the shelves, two headless dress forms, a long cutting table with paper patterns.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot at child height of the girl under the half-open shutter, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the kneeling mother in the lamplight, locked off.
- Shot 3, 10–15s: 40mm medium two-shot of mother and daughter in the lamplight, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Night in the tailor shop: @Na ducks in under the half-open steel shutter with her backpack, tears on her cheeks, and is already speaking fast between small sobs.
- 1–2s (Shot 1): @Na keeps talking in a rush of words, wiping her eyes with the back of her hand.
- 2–3s (Shot 1): @Na keeps going, her voice catching, the backpack slipping off one shoulder.
- 3–4s (Shot 1): @Na keeps speaking, sniffing hard, her small hands clenched on the straps.
- 4–5s (Shot 1): @Na finishes, shaking her head hard, pigtails swinging.
- 5–6s (CUT to Shot 2): @Na closes her mouth as @Thu kneels down before her in the warm lamplight and begins to answer softly.
- 6–7s (Shot 2): @Thu keeps speaking softly with a trembling smile, her eyes shining.
- 7–8s (Shot 2): @Thu keeps talking, her voice catching as she nods at her daughter.
- 8–9s (Shot 2): @Thu keeps going, the red wedding áo dài glowing on its dress form in the shadows behind her.
- 9–10s (Shot 2): @Thu keeps speaking and finishes, slowly opening her arms.
- 10–11s (CUT to Shot 3): @Thu closes her mouth, arms open; @Na steps into her mother's arms and says a small muffled reply, her face turned toward the camera.
- 11–12s (Shot 3): @Na keeps speaking in a small voice, her cheek against @Thu's shoulder.
- 12–13s (Shot 3): @Na keeps going, her eyes squeezed shut.
- 13–14s (Shot 3): @Na finishes and closes her mouth.
- 14–15s (Shot 3): @Thu rests her chin on @Na's head and the two hold each other close in the lamplight, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, sobbing, words tumbling out): "Mẹ ơi, nhà bố có bể bơi nhưng không có mẹ. Quà của cô ấy con để lại tất cả."
- Turn 2, 5.3–10.1s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, tender, voice catching): "Ừ. Con gái mẹ lớn thật rồi, biết tự tìm đường về. Lại đây với mẹ nào."
- Turn 3, 10.6–13.5s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking at a natural, even conversational pace, muffled and small): "Lần sau con không sang bên ấy nữa đâu, mẹ nhé."
- Pacing: @Na speaks quickly, then @Thu answers slowly and calmly, then @Na answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the shutter rattling, small hurried footsteps, a muffled sob, the desk lamp humming. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 1 (`canh-12/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Tùng's glass-walled director's office high in a Hà Nội tower by day: a big dark wood desk, white architectural models of towers under glass, a black leather chair, crisp cold daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the young woman perched on the edge of the dark wood desk, slow push-in.
- Shot 2, 6–11s: 85mm close-up of the man in the black leather chair, locked off.
- Shot 3, 11–15s: 40mm medium two-shot across the dark wood desk, slow drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the glass-walled director's office, @Vy perches on the edge of the dark wood desk, palms flat on the wood, tilts her head with a little pout and is already speaking sweetly, while @Tung leans back in the black leather chair with his mouth closed.
- 1–2s (Shot 1): @Vy keeps talking in a wheedling voice, twirling a strand of wavy hair.
- 2–3s (Shot 1): @Vy keeps going, glancing at the white tower models under glass.
- 3–4s (Shot 1): @Vy keeps speaking, holding up one hand with all her fingers spread.
- 4–5s (Shot 1): @Vy keeps talking, leaning toward him across the desk, her lashes fluttering.
- 5–6s (Shot 1): @Vy finishes and closes her mouth, lowering her lashes.
- 6–7s (CUT to Shot 2): @Tung rubs his jaw and answers hesitantly, his eyes sliding toward the window.
- 7–8s (Shot 2): @Tung keeps talking, tapping his gold wristwatch with one finger.
- 8–9s (Shot 2): @Tung keeps speaking, shifting in the leather chair.
- 9–10s (Shot 2): @Tung keeps going, waving one hand in a calming gesture.
- 10–11s (Shot 2): @Tung keeps talking, avoiding her eyes.
- 11–12s (CUT to Shot 3): @Tung closes his mouth; @Vy's sweet smile stiffens and she answers quickly with a pout, tapping the desk with one fingernail.
- 12–13s (Shot 3): @Vy keeps talking fast, pouting, her fingernail still tapping the wood.
- 13–14s (Shot 3): @Vy finishes and closes her mouth, while @Tung nods quickly, mouth closed.
- 14–15s (Shot 3): @Vy slides off the desk with a small smug smile, while @Tung reaches for his phone on the desk, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.9s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, sweet and wheedling): "Anh ơi, bố mẹ em ở quê khó tính lắm. Ngoài căn nhà, phải thêm năm tỷ sính lễ thì mới gả."
- Turn 2, 6.4–11.2s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, hesitant): "Năm tỷ thì anh xoay được. Còn căn nhà phải đợi bà ấy ký đã, em cứ từ từ."
- Turn 3, 11.7–13.8s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, pouting): "Từ từ đến bao giờ? Thế anh giục nhanh lên."
- Pacing: @Vy speaks at an even everyday pace, then @Tung answers at an even everyday pace, then @Vy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the hush of air conditioning, a leather chair creaking, distant city traffic far below, a pen clicking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 2 (`canh-12/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Tùng's glass-walled director's office high in a Hà Nội tower by day: a big dark wood desk, white architectural models of towers under glass, a black leather chair, crisp cold daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the young man standing across the desk, slow push-in.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the young man onto the director in his chair.
- Shot 3, 10–13s: 85mm close-up of the young man's sly half-smile, locked off.
- Shot 4, 13–15s: 40mm medium two-shot across the dark wood desk, slow arc.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the glass-walled office, @Khai stands across the dark wood desk, turns a black leather document folder the right way up with a showy flourish and is already speaking fast and smoothly.
- 1–2s (Shot 1): @Khai keeps talking, opening the folder and fanning a few papers with no readable writing.
- 2–3s (Shot 1): @Khai keeps going, smoothing his thin moustache with one finger, his sly half-smile fixed.
- 3–4s (Shot 1): @Khai keeps speaking smoothly, tapping the papers twice.
- 4–5s (Shot 1): @Khai finishes and closes his mouth, sliding the folder across the desk.
- 5–6s (CUT to Shot 2): @Tung nods slowly and answers in an even voice, tapping the folder, while @Khai in the foreground keeps his mouth closed.
- 6–7s (Shot 2): @Tung keeps talking, nodding along, a confident smile spreading.
- 7–8s (Shot 2): @Tung keeps speaking, picking up a pen.
- 8–9s (Shot 2): @Tung keeps going, pointing the pen toward the phone on the desk.
- 9–10s (Shot 2): @Tung finishes and closes his mouth, settling back in the black leather chair.
- 10–11s (CUT to Shot 3): @Khai spreads his palms and replies quickly with a generous grin.
- 11–12s (Shot 3): @Khai keeps talking, his voice silky, one eyebrow lifting.
- 12–13s (Shot 3): @Khai keeps going, the half-smile turning faintly mocking.
- 13–14s (CUT to Shot 4): @Khai finishes and closes his mouth, sliding the folder a little closer to @Tung.
- 14–15s (Shot 4): @Tung leans back with his mouth closed, nodding, while @Khai smooths his moustache and smiles, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking quickly in short lively phrases, every word still clear, slick and smooth): "Anh cứ chuyển trước vào tài khoản văn phòng luật của em. Ăn hỏi xong em lo sang tên một thể."
- Turn 2, 5.3–9.6s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, trusting, nodding along): "Được. Cậu là anh họ của Vy thì tôi tin. Chiều nay tôi bảo kế toán chuyển."
- Turn 3, 10.1–13.3s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking quickly in short lively phrases, every word still clear, generous, faintly mocking): "Người nhà cả mà anh. Phí luật sư em miễn hết, coi như quà cưới."
- Pacing: @Khai speaks quickly, then @Tung answers at an even everyday pace, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a leather folder sliding on wood, the hush of air conditioning, a chair creaking, a fingertip tapping leather. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 3 (`canh-12/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Tùng's glass-walled director's office high in a Hà Nội tower by day: a big dark wood desk, white architectural models of towers under glass, a black leather chair, crisp cold daylight over the city.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium two-shot by the window desk, locked off.
- Shot 2, 4–9s: 85mm close-up of the director, slow push-in.
- Shot 3, 9–12s: 40mm medium shot of the young woman, the man's back soft at the window behind her, locked off.
- Shot 4, 12–15s: 85mm close-up of the young woman, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the glass-walled office, @Vy stands at the desk beside @Tung, clasps her hands and is already speaking in an eager, sugary voice, while @Tung smiles with his mouth closed.
- 1–2s (Shot 1): @Vy keeps talking, tilting her head toward a slim black tablet with a glowing blank screen on the desk.
- 2–3s (Shot 1): @Vy keeps going, rolling her eyes playfully.
- 3–4s (Shot 1): @Vy finishes and closes her mouth, her eyes bright and eager.
- 4–5s (CUT to Shot 2): @Tung taps the slim black tablet with a flourish and starts answering proudly.
- 5–6s (Shot 2): @Tung keeps talking, spreading his arms wide, chin raised.
- 6–7s (Shot 2): @Tung keeps going expansively, a broad grin on his face.
- 7–8s (Shot 2): @Tung keeps speaking proudly, laying a palm on his chest.
- 8–9s (Shot 2): @Tung keeps talking as his phone buzzes on the desk beside him.
- 9–10s (CUT to Shot 3): @Tung closes his mouth and turns toward the window, lifting the phone to his ear with his back to her; @Vy begins to speak in a purring voice.
- 10–11s (Shot 3): @Vy keeps speaking sweetly to his back, her smile beginning to fade.
- 11–12s (Shot 3): @Vy keeps talking, her voice dropping, the sweetness draining from her face.
- 12–13s (CUT to Shot 4): @Vy keeps going, watching his back with flat eyes.
- 13–14s (Shot 4): @Vy says the last words with an ice-cold smile and closes her mouth.
- 14–15s (Shot 4): @Vy watches his back with flat, cold eyes, mouth closed, while @Tung's blurred figure at the window keeps listening to the phone. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.9s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, eager and sugary): "Chuyển chưa anh? Bố mẹ ở quê gọi em suốt từ sáng đến giờ."
- Turn 2, 4.4–9.2s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, proud and expansive): "Chuyển đủ rồi, không thiếu một xu. Từ giờ em là bà giám đốc, thích gì cứ bảo anh."
- Turn 3, 9.7–13.5s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, purring, then icy): "Cảm ơn ông xã. Anh yên tâm, em làm vợ anh, đúng một ngày thôi."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft tablet chime, a phone buzzing, the hush of air conditioning, heels shifting on a polished floor. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 4 (`canh-12/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Inside a mirrored glass elevator in a Hà Nội office tower by day: brushed steel walls, soft white light, the city skyline sliding past behind the glass.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium two-shot from the mirrored wall onto the pair, slow push-in.
- Shot 2, 4–10s: 85mm close-up of the young woman capping her lipstick, locked off.
- Shot 3, 10–13s: 50mm medium shot of the young man leaning on the brushed steel wall, locked off.
- Shot 4, 13–15s: 35mm wide shot of the pair and their mirror reflections, the skyline sliding past, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Inside a mirrored glass elevator, the steel doors sliding shut, @Khai leans toward @Vy and is already speaking fast and low, while @Vy touches up her red lipstick in the mirror with her mouth closed.
- 1–2s (Shot 1): @Khai keeps talking urgently, glancing at the closed doors.
- 2–3s (Shot 1): @Khai keeps going, patting the pocket of his beige chinos with a sly grin.
- 3–4s (Shot 1): @Khai finishes, raising his eyebrows at her reflection.
- 4–5s (CUT to Shot 2): @Khai closes his mouth; @Vy caps the lipstick with a click and answers with a cocky smile, watching his reflection.
- 5–6s (Shot 2): @Vy keeps talking, amused, smoothing one eyebrow with a fingertip.
- 6–7s (Shot 2): @Vy keeps going, rolling her eyes in mock weariness.
- 7–8s (Shot 2): @Vy keeps speaking, holding up three fingers with a smirk.
- 8–9s (Shot 2): @Vy keeps talking, her red lips curling.
- 9–10s (Shot 2): @Vy finishes with a little laugh and closes her mouth.
- 10–11s (CUT to Shot 3): @Khai leans back against the brushed steel wall and replies quickly with a smug grin.
- 11–12s (Shot 3): @Khai keeps talking, straightening his silver chain bracelet.
- 12–13s (Shot 3): @Khai finishes with a wink at her reflection.
- 13–14s (CUT to Shot 4): @Khai closes his mouth, while @Vy drops the lipstick into her small white handbag.
- 14–15s (Shot 4): The two stand side by side in silence, sharing a slow sly smile in the mirror as the skyline keeps sliding past the glass. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.0s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking quickly in short lively phrases, every word still clear, low and urgent): "Năm tỷ nằm gọn trong tài khoản rồi em. Tiệc xong là mình bay chuyến sớm nhất."
- Turn 2, 4.5–9.5s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, cocky and amused): "Đặt hạng thương gia nhé. Diễn vợ hiền ba lần rồi, lần này em phải được ngồi ghế tử tế."
- Turn 3, 10.0–13.0s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking quickly in short lively phrases, every word still clear, grinning, smug): "Hạng nhất luôn. Lão ấy trả tiền vé cho mình mà, khách sáo gì."
- Pacing: @Khai speaks quickly, then @Vy answers at an even everyday pace, then @Khai answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft hum of the elevator, a lipstick cap clicking shut, a gentle chime as floors pass, wind murmuring against the glass. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 1 (`canh-13/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A quiet rooftop café overlooking Hoàn Kiếm Lake in late afternoon: small wooden tables, rattan chairs, potted bougainvillea, the lake and its old trees glowing in golden light below.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the wife on the left of the small wooden table, the lake glowing behind her, locked off.
- Shot 2, 5–9s: 85mm close-up of the husband in the rattan chair, locked off.
- Shot 3, 9–15s: 50mm over-the-shoulder shot from behind the husband onto the wife.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): On a rooftop café in golden late-afternoon light, @Thu sits on the left of a small wooden table, hands folded beside her tea and a thin stack of papers with no readable writing, and is already speaking slowly and evenly.
- 1–2s (Shot 1): @Thu keeps talking calmly, her eyes steady across the table.
- 2–3s (Shot 1): @Thu keeps speaking, laying two fingers on the stack of papers.
- 3–4s (Shot 1): @Thu keeps going, sliding the papers a little toward the other side of the table.
- 4–5s (Shot 1): @Thu finishes and closes her mouth, folding her hands again.
- 5–6s (CUT to Shot 2): @Tung stops stirring his tea, leans back with a smug grin and answers fast.
- 6–7s (Shot 2): @Tung keeps talking with a surprised laugh, eyebrows high.
- 7–8s (Shot 2): @Tung keeps going, wagging his teaspoon in the air.
- 8–9s (Shot 2): @Tung keeps speaking, shaking his head in amusement.
- 9–10s (CUT to Shot 3): @Tung closes his mouth and spreads his arms along the rattan chair; @Thu calmly lifts her teacup and answers in a dry, light voice.
- 10–11s (Shot 3): @Thu keeps speaking lightly, the cup near her lips.
- 11–12s (Shot 3): @Thu keeps talking, glancing at the other tables with a faint smile.
- 12–13s (Shot 3): @Thu keeps going, her voice almost playful.
- 13–14s (Shot 3): @Thu keeps speaking and finishes, blowing gently on the tea.
- 14–15s (Shot 3): @Thu closes her mouth and sips her tea, watching him over the rim, while @Tung sits stiffly in the foreground, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, calm and even): "Em đồng ý ly hôn. Giấy tờ anh đưa, em ký hết, không tranh gì cả."
- Turn 2, 5.4–9.0s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, smug, a surprised laugh): "Thật à? Cô biết điều từ bao giờ thế? Tôi cứ tưởng phải lôi nhau ra toà."
- Turn 3, 9.5–13.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, dry, almost light): "Ra toà thì ít người xem quá. Chuyện vui thế này phải đông mới hay."
- Pacing: @Thu speaks slowly and calmly, then @Tung answers quickly, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: teaspoons clinking on china, a breeze in the bougainvillea, birds calling over the lake, distant traffic around the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 2 (`canh-13/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A quiet rooftop café overlooking Hoàn Kiếm Lake in late afternoon: small wooden tables, rattan chairs, potted bougainvillea, the lake and its old trees glowing in golden light below.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm over-the-shoulder shot from behind the husband onto the wife, holding the previous framing.
- Shot 2, 5–9s: 85mm close-up of the husband, the lake soft behind him, locked off.
- Shot 3, 9–15s: 40mm medium two-shot across the small table, slow lateral slide.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu raises one finger and is already speaking slowly, her eyes steady on @Tung, while @Tung holds his teacup halfway to his lips with his mouth closed.
- 1–2s (Shot 1): @Thu keeps speaking, every word placed, her finger still raised.
- 2–3s (Shot 1): @Thu keeps talking quietly, lowering her hand to the table.
- 3–4s (Shot 1): @Thu keeps speaking, her gaze unwavering, her face calm.
- 4–5s (Shot 1): @Thu finishes and closes her mouth, her eyes still on him.
- 5–6s (CUT to Shot 2): @Tung sets his cup down, tips his head back with a laugh and answers scornfully.
- 6–7s (Shot 2): @Tung keeps talking, laughing, sweeping a hand toward the other tables.
- 7–8s (Shot 2): @Tung keeps going, pointing at his own cheek with a mocking grimace.
- 8–9s (Shot 2): @Tung keeps speaking scornfully, shaking his head.
- 9–10s (CUT to Shot 3): @Tung closes his mouth, still smirking; @Thu answers slowly and evenly, resting her fingertips on the stack of papers.
- 10–11s (Shot 3): @Thu keeps speaking, unruffled, sliding the papers to the middle of the table.
- 11–12s (Shot 3): @Thu keeps talking calmly as @Tung's eyebrows climb, his mouth closed.
- 12–13s (Shot 3): @Thu keeps going, tapping the table once with a fingertip.
- 13–14s (Shot 3): @Thu keeps speaking, then finishes, watching him calmly over the rim of her teacup.
- 14–15s (Shot 3): @Thu closes her mouth, while @Tung leans forward over the table, his jaw jutting, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, every word placed): "Có một điều kiện. Em sẽ ký ở đám hỏi của anh, trước mặt hai họ."
- Turn 2, 5.4–9.4s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, laughing and scornful): "Trước mặt bao nhiêu người? Cô định tự bôi tro trát trấu vào mặt mình à?"
- Turn 3, 9.9–14.4s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, unruffled): "Còn áo cưới, em tự mang đến tận tay cô dâu. Hàng của em, em giao."
- Pacing: @Thu speaks slowly and calmly, then @Tung answers at an even everyday pace, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: china cups clinking, leaves rustling in the breeze, birds calling over the lake, a teacup set down on wood. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 3 (`canh-13/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A quiet rooftop café overlooking Hoàn Kiếm Lake in late afternoon: small wooden tables, rattan chairs, potted bougainvillea, the lake and its old trees glowing in golden light below.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot across the small table, holding the previous framing.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the husband onto the wife.
- Shot 3, 10–15s: 50mm medium shot of the husband in the rattan chair, slow drift.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tung leans forward over the table and is already speaking fast, tapping a finger on the stack of papers, while @Thu sits upright with her hands around her teacup, mouth closed.
- 1–2s (Shot 1): @Tung keeps talking, jabbing his finger at the papers.
- 2–3s (Shot 1): @Tung keeps going, his voice clipped and demanding.
- 3–4s (Shot 1): @Tung keeps speaking, narrowing his heavy-lidded eyes.
- 4–5s (Shot 1): @Tung finishes and closes his mouth, his jaw jutting.
- 5–6s (CUT to Shot 2): @Thu sets her teacup down without a sound and answers slowly with a faint smile.
- 6–7s (Shot 2): @Thu keeps speaking softly, her eyes drifting to the lake beyond the railing.
- 7–8s (Shot 2): @Thu keeps talking, the faint smile never leaving her lips.
- 8–9s (Shot 2): @Thu keeps going slowly, turning back to look at him.
- 9–10s (Shot 2): @Thu finishes and closes her mouth, folding her hands on the table.
- 10–11s (CUT to Shot 3): @Tung blinks, takes it for a yes and answers with a satisfied nod.
- 11–12s (Shot 3): @Tung keeps talking, leaning back in the rattan chair, pleased with himself.
- 12–13s (Shot 3): @Tung keeps going, waving one hand as if brushing off crumbs.
- 13–14s (Shot 3): @Tung finishes and closes his mouth, draining his teacup with a smug little smile.
- 14–15s (Shot 3): @Tung sets the empty cup down with a soft clink and straightens his gold wristwatch, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, pushy and demanding): "Tuỳ cô. Nhưng nhớ đấy, nhà phải về tay tôi. Tôi hứa với nhà gái rồi, cô đừng có lật lọng."
- Turn 2, 5.3–9.5s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, a faint smile in the voice): "Anh yên tâm. Căn nhà ấy sẽ về đúng tay người chủ thật của nó."
- Turn 3, 10.0–13.8s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, satisfied, oblivious): "Được. Thế mới phải chứ. Ký xong thì đường ai nấy đi, khỏi dây dưa."
- Pacing: @Tung speaks quickly, then @Thu answers slowly and calmly, then @Tung answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a finger tapping on paper, a teacup set down on wood, the breeze in the bougainvillea, a bicycle bell far below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 4 (`canh-13/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A quiet rooftop café overlooking Hoàn Kiếm Lake in late afternoon: small wooden tables, rattan chairs, potted bougainvillea, the lake and its old trees glowing in golden light below.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the husband in the rattan chair, holding the previous framing.
- Shot 2, 4–10s: 50mm over-the-shoulder shot from behind the standing husband down onto the seated wife.
- Shot 3, 10–13s: 35mm low-angle close-up of the standing husband, locked off.
- Shot 4, 13–15s: 40mm medium two-shot at the table, the lake behind, slow pull-back.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tung rises from the rattan chair, buttoning his suit jacket, and is already speaking in an arrogant, unhurried voice, looking down across the table at @Thu.
- 1–2s (Shot 1): @Tung keeps talking, a superior smile tugging at his mouth.
- 2–3s (Shot 1): @Tung keeps going, straightening his cuffs one by one.
- 3–4s (Shot 1): @Tung keeps speaking, tilting his chin up.
- 4–5s (CUT to Shot 2): @Tung closes his mouth, chin raised; @Thu looks up at him, holding her teacup in both hands, and answers slowly and quietly.
- 5–6s (Shot 2): @Thu keeps speaking, holding his gaze, her voice low and cutting.
- 6–7s (Shot 2): @Thu keeps talking, a faint smile at the corner of her mouth.
- 7–8s (Shot 2): @Thu keeps going, her eyes running over him from shoulders to waist as if taking his measurements.
- 8–9s (Shot 2): @Thu keeps speaking, lifting the teacup slightly as if in a toast.
- 9–10s (Shot 2): @Thu keeps talking, finishing evenly.
- 10–11s (CUT to Shot 3): @Thu closes her mouth; a flicker of confusion crosses @Tung's face, he snorts and mutters a dismissive reply.
- 11–12s (Shot 3): @Tung keeps talking, flicking a hand toward the teacups.
- 12–13s (Shot 3): @Tung keeps going, already turning away from the table.
- 13–14s (CUT to Shot 4): @Tung finishes and closes his mouth.
- 14–15s (Shot 4): @Tung walks off between the tables, while @Thu sips her tea and gazes out over the golden lake. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, arrogant, looking down at her): "Lấy nhau ngần ấy năm, giờ cô mới làm được một việc tôi hài lòng."
- Turn 2, 4.7–10.0s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and cutting): "Còn em, đến hôm nay mới đo được đúng số đo của anh. Vừa khít, không thừa một phân."
- Turn 3, 10.5–14.0s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, a dismissive snort): "Đo với chả đếm. Thôi tôi về đây, tiền nước thì cô trả nhé."
- Pacing: @Tung speaks at an even everyday pace, then @Thu answers slowly and calmly, then @Tung answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a rattan chair creaking, footsteps fading across the wooden deck, a teacup touching its saucer, birds over the lake. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 1 (`canh-14/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Thu's narrow áo dài tailor shop on an old-quarter silk street by day: bolts of jewel-toned silk stacked on wooden shelves to the ceiling, two headless dress forms in half-finished áo dài, an old black sewing machine on a worn wooden table, a tall standing fitting mirror, a long cutting table with tailor's chalk and paper patterns, a small brass bell above the glass door, soft daylight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a red silk wedding áo dài embroidered with a gold phoenix, a thin gold necklace, beige high heels.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the bride on the fitting stand before the tall mirror, slow arc.
- Shot 2, 6–11s: 85mm close-up of the tailor rising from the hem, locked off.
- Shot 3, 11–15s: 40mm medium two-shot beside the fitting mirror, slow drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the tailor shop by day, @Vy, in a red silk wedding áo dài embroidered with a gold phoenix, turns slowly on the low fitting stand before the tall mirror and is already speaking as she admires herself, while @Thu kneels at the hem with a pincushion, mouth closed.
- 1–2s (Shot 1): @Vy keeps talking, smoothing the gold phoenix over her waist, a mocking smile on her red lips.
- 2–3s (Shot 1): @Vy keeps going, lifting the hem a little to admire the stitching.
- 3–4s (Shot 1): @Vy keeps speaking, glancing down at @Thu with a smirk.
- 4–5s (Shot 1): @Vy keeps talking, tilting her chin at her own reflection.
- 5–6s (Shot 1): @Vy keeps speaking, turning her shoulders left and right before the mirror.
- 6–7s (CUT to Shot 2): @Vy finishes and closes her mouth; @Thu rises from the hem, steps back to look at it and answers slowly and dryly.
- 7–8s (Shot 2): @Thu keeps speaking calmly, her eyes running along the seam.
- 8–9s (Shot 2): @Thu keeps talking, sliding a pin into the pincushion on her wrist.
- 9–10s (Shot 2): @Thu keeps going, her face composed, one corner of her mouth lifting.
- 10–11s (Shot 2): @Thu finishes and closes her mouth, meeting @Vy's eyes in the mirror.
- 11–12s (CUT to Shot 3): @Vy's smile tightens and she answers with a quick needling question, her eyes narrowed at @Thu's reflection.
- 12–13s (Shot 3): @Vy keeps talking sharply, turning half round toward @Thu.
- 13–14s (Shot 3): @Vy keeps going, lifting her chin higher.
- 14–15s (Shot 3): @Vy closes her mouth and waits, while @Thu calmly steps up behind her at the shoulder seam, her face clear in the mirror, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.2s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, admiring herself, mocking): "Đẹp thật đấy. Chị may cho người cướp chồng mình mà khéo thế à? Em cứ tưởng chị cắt hỏng cho bõ tức."
- Turn 2, 6.7–10.6s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, calm and dry): "Làm nghề thì phải tử tế. Áo đẹp hay không còn tuỳ người mặc."
- Turn 3, 11.1–14.1s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, stung, needling): "Ý chị là em không xứng chứ gì? Chị nói thẳng ra xem nào."
- Pacing: @Vy speaks at an even everyday pace, then @Thu answers slowly and calmly, then @Vy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: silk rustling, a pin dropping into a tin, a wall clock ticking, street traffic muffled behind the glass. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 2 (`canh-14/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Thu's narrow áo dài tailor shop on an old-quarter silk street by day: bolts of jewel-toned silk stacked on wooden shelves to the ceiling, two headless dress forms in half-finished áo dài, an old black sewing machine on a worn wooden table, a tall standing fitting mirror, a long cutting table with tailor's chalk and paper patterns, a small brass bell above the glass door, soft daylight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a red silk wedding áo dài embroidered with a gold phoenix, a thin gold necklace, beige high heels.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 40mm medium two-shot beside the fitting mirror, holding the previous framing.
- Shot 2, 6–10s: 85mm close-up of the bride spinning round from the mirror, locked off.
- Shot 3, 10–15s: 50mm medium two-shot from the side of the fitting stand, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu stands behind @Vy at the tall mirror, slipping pins out of the shoulder seam of the red áo dài one by one, and is already speaking casually without looking up, while @Vy admires her reflection, mouth closed.
- 1–2s (Shot 1): @Thu keeps chatting lightly, dropping each pin into the pincushion.
- 2–3s (Shot 1): @Thu keeps talking with a small easy smile, her fingers working along the seam.
- 3–4s (Shot 1): @Thu keeps going, glancing up at the bride's reflection for a moment.
- 4–5s (Shot 1): @Thu keeps speaking pleasantly, while @Vy's smile in the mirror freezes.
- 5–6s (Shot 1): @Thu keeps talking a moment longer, then closes her mouth and returns her eyes to the seam.
- 6–7s (CUT to Shot 2): @Vy spins round away from the mirror to face @Thu and speaks fast and sharp, her eyes narrowed.
- 7–8s (Shot 2): @Vy keeps talking, her red nails curling at her sides.
- 8–9s (Shot 2): @Vy keeps going, her voice rising.
- 9–10s (Shot 2): @Vy finishes and closes her mouth, breathing hard through her nose.
- 10–11s (CUT to Shot 3): @Thu calmly slides another pin into the pincushion and answers lightly and innocently.
- 11–12s (Shot 3): @Thu keeps speaking, her face unreadable, while @Vy stares at her with her mouth closed.
- 12–13s (Shot 3): @Thu keeps talking, kneeling down to the hem.
- 13–14s (Shot 3): @Thu finishes and closes her mouth, her eyes on the hem.
- 14–15s (Shot 3): @Vy turns back toward the mirror, jaw tight, glaring at @Thu's reflection, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.9s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, casual, almost chatty): "Quê em ở Nam Định nhỉ? Chị vừa về dưới ấy. Làng em đẹp, nhà nào cũng treo ảnh cưới thật to."
- Turn 2, 6.4–10.0s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, sharp and suspicious): "Chị về quê em làm gì? Chị điều tra em à? Ai cho chị cái quyền ấy?"
- Turn 3, 10.5–13.9s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, light and innocent): "Chị đi giao áo cho mấy khách quen mà. Tiện thì ghé."
- Pacing: @Thu speaks at an even everyday pace, then @Vy answers quickly, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pins clicking into a tin, silk rustling, a wall clock ticking, a sharp swish of silk. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 3 (`canh-14/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Thu's narrow áo dài tailor shop on an old-quarter silk street by day: bolts of jewel-toned silk stacked on wooden shelves to the ceiling, two headless dress forms in half-finished áo dài, an old black sewing machine on a worn wooden table, a tall standing fitting mirror, a long cutting table with tailor's chalk and paper patterns, a small brass bell above the glass door, soft daylight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a red silk wedding áo dài embroidered with a gold phoenix, a thin gold necklace, beige high heels.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium two-shot from the side of the fitting stand, holding the previous framing.
- Shot 2, 4–7s: 85mm close-up of the bride glaring into the mirror, locked off.
- Shot 3, 7–12s: 50mm over-the-shoulder shot from behind the bride down onto the kneeling tailor.
- Shot 4, 12–15s: 40mm medium two-shot in the fitting corner, slow pull-back.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy leans in, points a red-nailed finger at @Thu's reflection in the tall mirror and is already speaking fast and low through her teeth, while @Thu kneels at the hem with a pincushion, mouth closed.
- 1–2s (Shot 1): @Vy keeps talking fast, her fingernail tapping the mirror glass, never touching @Thu.
- 2–3s (Shot 1): @Vy keeps going, her nostrils flared.
- 3–4s (Shot 1): @Vy keeps speaking spitefully, her winged eyes narrowed at the mirror.
- 4–5s (CUT to Shot 2): @Vy keeps talking, her voice rising, her chin jutting.
- 5–6s (Shot 2): @Vy keeps going, sweeping one hand at the silk shelves around the shop.
- 6–7s (Shot 2): @Vy keeps speaking through her teeth to the last word, glaring.
- 7–8s (CUT to Shot 3): @Vy closes her mouth; @Thu, still unpinning the hem with steady hands, begins to answer slowly and softly.
- 8–9s (Shot 3): @Thu keeps speaking softly, dropping a pin into the pincushion.
- 9–10s (Shot 3): @Thu keeps talking, lifting her eyes to the bride.
- 10–11s (Shot 3): @Thu keeps going, drops the last pin into the pincushion and slowly rises to her feet.
- 11–12s (Shot 3): @Thu keeps speaking, now standing an arm's length from @Vy, never touching her.
- 12–13s (CUT to Shot 4): @Thu keeps talking, folding her hands on her apron.
- 13–14s (Shot 4): @Thu finishes and closes her mouth, holding @Vy's gaze.
- 14–15s (Shot 4): @Vy's pointing hand slowly lowers, her jaw tight, while @Thu turns calmly toward the cutting table beside the mirror, where a long flat red garment box waits, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.1s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, hissing and spiteful): "Chị đừng có giở trò với em. Ngày vui của em mà có chuyện gì, em cho chị trắng tay ra đường, đến cái tiệm may cỏn con này cũng không còn!"
- Turn 2, 7.6–13.5s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft and unshakable): "Trắng tay thì chị quen rồi em ạ, ngày xưa chị cũng thế. Chị chỉ lo cho người chưa quen thôi."
- Pacing: @Vy speaks quickly, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a fingernail tapping on glass, pins clicking into a tin, silk rustling, the street muffled behind the glass door. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 4 (`canh-14/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Thu's narrow áo dài tailor shop on an old-quarter silk street by day: bolts of jewel-toned silk stacked on wooden shelves to the ceiling, two headless dress forms in half-finished áo dài, an old black sewing machine on a worn wooden table, a tall standing fitting mirror, a long cutting table with tailor's chalk and paper patterns, a small brass bell above the glass door, soft daylight from the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a red silk wedding áo dài embroidered with a gold phoenix, a thin gold necklace, beige high heels.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 40mm medium two-shot in the fitting corner, holding the previous framing.
- Shot 2, 4–10s: 85mm close-up of the tailor at the cutting table, the red box before her, slow push-in.
- Shot 3, 10–15s: 50mm over-the-shoulder shot from behind the tailor onto the bride on the fitting stand.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy turns her head from the mirror toward @Thu and is already speaking fast and sharp, her eyes darting, covering it with a brittle laugh, while @Thu stands at the cutting table, mouth closed.
- 1–2s (Shot 1): @Vy keeps talking fast, smoothing the red silk at her waist.
- 2–3s (Shot 1): @Vy keeps going, shaking her head too quickly.
- 3–4s (Shot 1): @Vy keeps speaking, swallowing.
- 4–5s (CUT to Shot 2): @Vy closes her mouth; @Thu lays a red khăn vấn headband into a long flat red garment box on the cutting table and begins to answer slowly and evenly.
- 5–6s (Shot 2): @Thu keeps speaking politely, smoothing the red headband flat inside the box.
- 6–7s (Shot 2): @Thu keeps talking, closing the lid of the red box.
- 7–8s (Shot 2): @Thu keeps going, knotting a gold ribbon around the red box.
- 8–9s (Shot 2): @Thu keeps speaking, smoothing the gold bow with her fingertips.
- 9–10s (Shot 2): @Thu keeps talking, lifting her eyes to the bride's reflection in the mirror, and finishes.
- 10–11s (CUT to Shot 3): @Thu closes her mouth, her hands resting on the box; @Vy calls out a bossy order a little too loudly from the fitting stand.
- 11–12s (Shot 3): @Vy keeps talking loudly, pointing at the red box.
- 12–13s (Shot 3): @Vy keeps going, her chin high.
- 13–14s (Shot 3): @Vy finishes and closes her mouth, standing stiff before the mirror in the red áo dài, her jaw tight.
- 14–15s (Shot 3): @Thu rests her palm on the red box and inclines her head politely, while @Vy stays rigid on the fitting stand, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.0s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, rattled, covering it): "Chị nói thế là ý gì? Sao lại nhìn em như thế? Em có nợ ai đâu."
- Turn 2, 4.5–10.1s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, polite and even): "Khăn vấn chị để riêng trong hộp này. Hôm ấy chị mang đến tận nơi, kèm một món quà nhỏ."
- Turn 3, 10.6–13.4s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, bossy, too loud): "Đến sớm vào, đừng để em phải đợi. Em ghét nhất là chờ."
- Pacing: @Vy speaks quickly, then @Thu answers slowly and calmly, then @Vy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a box lid closing softly, satin ribbon sliding, a wall clock ticking, a held breath. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 1 (`canh-15/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Night in Thu's narrow áo dài tailor shop: the steel shutter half down, a single warm desk lamp over the old black sewing machine, bolts of silk fading into shadow on the shelves, two headless dress forms, a long cutting table with paper patterns.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the wife at the sewing machine in the lamplight, locked off.
- Shot 2, 4–8s: 85mm close-up of the wife on the phone, lamplight on one side of her face, slow push-in.
- Shot 3, 8–12s: 50mm medium profile shot past the red áo dài on its dress form toward the wife, slow rack focus.
- Shot 4, 12–15s: 85mm close-up of the wife at the sewing table in the lamplight, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Night in the tailor shop under a single warm desk lamp: @Thu sits at the old black sewing machine with a phone with a glowing blank screen at her ear and is already speaking in a low, steady voice.
- 1–2s (Shot 1): @Thu keeps talking evenly, glancing at the half-lowered steel shutter.
- 2–3s (Shot 1): @Thu keeps speaking, her free hand running along the yellow measuring tape around her neck.
- 3–4s (Shot 1): @Thu keeps talking quietly, her eyes on the finished red silk wedding áo dài embroidered with a gold phoenix on a headless dress form across the room.
- 4–5s (CUT to Shot 2): @Thu keeps going, nodding slowly as she listens and answers.
- 5–6s (Shot 2): @Thu keeps speaking low, her jaw firm, the lamplight on her cheek.
- 6–7s (Shot 2): @Thu keeps talking, lowering her voice further, her eyes narrowing in thought.
- 7–8s (Shot 2): @Thu keeps speaking steadily, tapping two fingers on the sewing table.
- 8–9s (CUT to Shot 3): @Thu keeps talking, turning on the stool toward the dress form.
- 9–10s (Shot 3): @Thu keeps speaking, her eyes on the gold phoenix, the phone pressed to her ear.
- 10–11s (Shot 3): @Thu keeps going with a calm, decisive nod.
- 11–12s (Shot 3): @Thu keeps talking quietly into the phone, a small steady smile, her face clearly in view.
- 12–13s (CUT to Shot 4): @Thu adds her last calm words, then closes her mouth and lowers the phone.
- 13–14s (Shot 4): @Thu sets the phone down, its glow fading on her cheek, mouth closed.
- 14–15s (Shot 4): @Thu lifts her eyes toward the red wedding áo dài just beyond the frame, a steady gaze, silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–13.9s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, steady and low, on the phone), in Vietnamese with exact lip-sync, said exactly once: "Vâng, ảnh cưới với địa chỉ quê họ em gửi anh rồi. Họ lừa thế này là lần thứ ba rồi anh ạ, lần nào cũng một bài. Tối mai, ở sảnh tiệc khách sạn. Vâng, em sẽ giữ chân họ đến khi các anh tới. Em không run đâu, anh cứ tin em." (no subtitles)
- @Thu starts talking within the first second; whenever @Thu speaks, the face and lips are clearly visible in that shot; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the desk lamp humming, a soft click as the call ends, the steel shutter creaking in the night breeze, a motorbike passing far off. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 2 (`canh-15/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Night in Thu's narrow áo dài tailor shop: the steel shutter half down, a single warm desk lamp over the old black sewing machine, bolts of silk fading into shadow on the shelves, two headless dress forms, a long cutting table with paper patterns.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the girl on the narrow staircase, locked off.
- Shot 2, 6–11s: 85mm close-up of the mother crouching at the foot of the stairs, locked off.
- Shot 3, 11–15s: 40mm medium two-shot at the foot of the staircase, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): At the back of the lamplit tailor shop at night, @Na comes down the narrow inner staircase in her school uniform, rubbing her eyes, and is already speaking in a small sleepy voice.
- 1–2s (Shot 1): @Na keeps talking, holding the banister, her pigtails loose.
- 2–3s (Shot 1): @Na keeps asking, sitting down on the bottom step beside a small pair of white canvas shoes.
- 3–4s (Shot 1): @Na keeps speaking, hugging her knees, looking toward the lamp over the sewing machine.
- 4–5s (Shot 1): @Na keeps talking, pointing sleepily at the red áo dài glowing on its dress form.
- 5–6s (Shot 1): @Na finishes and closes her mouth, her chin on her knees.
- 6–7s (CUT to Shot 2): @Thu, crouching in front of the bottom step, answers warmly.
- 7–8s (Shot 2): @Thu keeps speaking gently, with a soft reassuring smile.
- 8–9s (Shot 2): @Thu keeps talking, tilting her head to meet @Na's eyes.
- 9–10s (Shot 2): @Thu keeps going and tucks a loose strand of hair behind @Na's ear.
- 10–11s (Shot 2): @Thu finishes and closes her mouth.
- 11–12s (CUT to Shot 3): @Na gives a small sleepy smile and says a drowsy reply.
- 12–13s (Shot 3): @Na keeps speaking drowsily, her eyelids drooping, while @Thu listens with her mouth closed.
- 13–14s (Shot 3): @Na finishes and closes her mouth, leaning her head against the banister.
- 14–15s (Shot 3): @Thu strokes @Na's hair once and watches her doze, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.0s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking at a natural, even conversational pace, sleepy and worried): "Mẹ ơi, mai mẹ đi đám hỏi của bố thật à? Mẹ có buồn không? Con thấy mẹ ngồi khâu mãi."
- Turn 2, 6.5–10.5s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, warm and reassuring): "Mẹ không đi ăn hỏi. Mẹ đi giao áo, giao xong là về với con ngay."
- Turn 3, 11.0–13.9s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking at a natural, even conversational pace, drowsy, comforted): "Thế con thức đợi mẹ về nhé. Con không ngủ đâu."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: small feet on wooden stairs, the desk lamp humming, a cricket chirping outside, the night street quiet beyond the shutter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 3 (`canh-15/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A glossy luxury apartment high above Hà Nội at night: floor-to-ceiling windows full of city lights, a white leather sofa, a marble kitchen island with a bottle of champagne and two glasses, cold blue-white light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the man at the marble kitchen island, slow push-in.
- Shot 2, 5–11s: 85mm close-up of the young woman, city lights behind her, locked off.
- Shot 3, 11–15s: 40mm medium two-shot across the marble kitchen island, slow arc.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the glossy apartment at night, @Tung stands at the marble kitchen island beside a small white handbag lying open, holds up two boarding passes with no readable writing and is already speaking with a puzzled frown.
- 1–2s (Shot 1): @Tung keeps talking, turning the passes over in his fingers.
- 2–3s (Shot 1): @Tung keeps going, one eyebrow raised, glancing toward the window.
- 3–4s (Shot 1): @Tung keeps speaking, holding the passes out at arm's length.
- 4–5s (Shot 1): @Tung finishes and closes his mouth, waiting, as @Vy walks in from the window.
- 5–6s (CUT to Shot 2): @Vy laughs brightly and answers fast and sweetly, plucking the boarding passes from his fingers.
- 6–7s (Shot 2): @Vy keeps talking too quickly, fluttering the passes in front of her smile.
- 7–8s (Shot 2): @Vy keeps going, pressing the passes to her heart with a dreamy look.
- 8–9s (Shot 2): @Vy keeps speaking, pouting playfully, her voice sugary.
- 9–10s (Shot 2): @Vy keeps talking, wagging one finger at him in mock offence.
- 10–11s (Shot 2): @Vy finishes and closes her mouth with a little pout.
- 11–12s (CUT to Shot 3): @Tung rubs the back of his neck and says a short sheepish line.
- 12–13s (Shot 3): @Tung keeps speaking sheepishly, while @Vy tucks the boarding passes deep into her handbag, mouth closed.
- 13–14s (Shot 3): @Tung finishes and closes his mouth.
- 14–15s (Shot 3): @Vy clicks the handbag shut and pours two glasses of champagne with a bright smile, while @Tung looks down, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, puzzled, half suspicious): "Sao trong túi em lại có hai vé bay sáng ngày kia? Xong tiệc là đi luôn à?"
- Turn 2, 5.4–10.7s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, bright and sugary, too quick): "Vé đi trăng mật của mình chứ còn gì! Em định để dành làm quà bất ngờ. Anh lại đa nghi rồi, em giận đấy."
- Turn 3, 11.2–13.5s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, sheepish): "Thôi, anh xin lỗi. Dạo này anh mệt quá."
- Pacing: @Tung speaks at an even everyday pace, then @Vy answers quickly, then @Tung answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: champagne glasses clinking, a handbag clasp clicking shut, the hum of the city far below, paper rustling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 4 (`canh-15/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the son striding in through the doorway, locked off.
- Shot 2, 5–10s: 85mm close-up of the old mother's face lit by a small flame at the altar, locked off.
- Shot 3, 10–15s: 50mm over-the-shoulder shot from behind the old mother onto the son, slow rack focus.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the family's narrow tube house in warm tungsten light, @Tung strides in through the doorway loosening his tie and is already speaking fast and irritably, while @BaNhan sits on a low stool beside the family altar with her back to the room, mouth closed.
- 1–2s (Shot 1): @Tung keeps talking, tossing his car keys onto the round dining table.
- 2–3s (Shot 1): @Tung keeps going, flinging one hand toward the street door.
- 3–4s (Shot 1): @Tung keeps speaking, standing over the table with his hands on his hips.
- 4–5s (Shot 1): @Tung finishes and closes his mouth, waiting.
- 5–6s (CUT to Shot 2): @BaNhan, without turning round, begins to answer slowly and heavily, lighting a stick of incense.
- 6–7s (Shot 2): @BaNhan keeps speaking, her face lit by the small flame, her eyes on the old framed photos.
- 7–8s (Shot 2): @BaNhan keeps talking, never turning to her son.
- 8–9s (Shot 2): @BaNhan keeps going, her voice low, the incense smoke rising past her face.
- 9–10s (Shot 2): @BaNhan keeps speaking, her wrinkled lips barely moving, her eyes half closed.
- 10–11s (CUT to Shot 3): @BaNhan sets the incense in the bowl and closes her mouth; @Tung snaps back with a sharp retort, his jaw tight.
- 11–12s (Shot 3): @Tung keeps talking sharply, rubbing his face with one hand.
- 12–13s (Shot 3): @Tung keeps going, jabbing a thumb at his own chest.
- 13–14s (Shot 3): @Tung finishes and closes his mouth.
- 14–15s (Shot 3): @Tung turns away toward the steep staircase, while @BaNhan stays bowed before the altar, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, irritated and defensive): "Mai mẹ có đến không? Hay mẹ lại ngồi nhà bênh cái Thu như mọi khi? Mẹ nói một câu đi."
- Turn 2, 5.3–10.0s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking slowly and softly, unhurried, with a short natural pause between phrases, heavy and quiet): "Mẹ sẽ đến. Mẹ đến để xem con trai mẹ tự tay đào hố chôn mình."
- Turn 3, 10.5–13.0s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, rattled, snapping): "Mẹ nói gở vừa thôi! Mai là ngày vui của con đấy."
- Pacing: @Tung speaks quickly, then @BaNhan answers slowly and calmly, then @Tung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: incense crackling, a small brass bell ringing once, a tie sliding loose, heavy footsteps on tiles. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 1 (`canh-16/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a red silk wedding áo dài embroidered with a gold phoenix, a matching red khăn vấn headband, a thin gold necklace, beige high heels.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: a stiff middle-aged couple in formal clothes at the front table and a few engagement guests, far in the background and out of focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium two-shot of the couple under the flower arch, locked off.
- Shot 2, 5–10s: 85mm close-up of the bride under the flower arch, slow push-in.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the bride onto the groom, locked off.
- Shot 4, 13–15s: 24mm wide shot from the center aisle toward the stage, the chandeliers blazing, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Under a flower arch on the low stage of the chandelier-lit banquet hall, @Tung stands beside @Vy, sweeps one arm toward the hall and is already speaking fast and proudly, while @Vy smiles beside him with her mouth closed.
- 1–2s (Shot 1): @Tung keeps talking, booming, his chest puffed out.
- 2–3s (Shot 1): @Tung keeps going, bowing his head toward the far tables, where a few guests sit far away, blurred and out of focus.
- 3–4s (Shot 1): @Tung keeps speaking grandly, one hand on his heart.
- 4–5s (Shot 1): @Tung keeps talking, beaming at the hall.
- 5–6s (CUT to Shot 2): @Tung closes his mouth; @Vy turns to him, lowers her eyes and answers slowly and sweetly.
- 6–7s (Shot 2): @Vy keeps speaking softly, her hands folded at her waist, her red khăn vấn glowing in the chandelier light.
- 7–8s (Shot 2): @Vy keeps talking, lifting her eyes to him with a demure smile.
- 8–9s (Shot 2): @Vy keeps going, a hidden smirk tugging at one corner of her mouth.
- 9–10s (Shot 2): @Vy keeps speaking, her smile hardening at the corners.
- 10–11s (CUT to Shot 3): @Vy closes her mouth, glancing toward the blurred front table far behind; @Tung gestures grandly at the trays of betrothal gifts under red cloth and calls out a ceremonial line.
- 11–12s (Shot 3): @Tung keeps talking, booming, his arm stretched toward the trays.
- 12–13s (Shot 3): @Tung keeps going, grinning at the guests.
- 13–14s (CUT to Shot 4): @Tung finishes and closes his mouth, beaming at the hall.
- 14–15s (Shot 4): @Tung stands proudly under the flower arch, his hand still raised toward the trays, while @Vy keeps her demure pose beside him, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.0s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, booming and proud): "Kính thưa các cụ, các bác! Cảm ơn mọi người đến chung vui với gia đình tôi trong ngày trọng đại này!"
- Turn 2, 5.5–10.0s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking slowly and softly, unhurried, with a short natural pause between phrases, sweet, a hidden smirk): "Em cảm ơn anh. Cả đời này em chỉ làm vợ anh thôi, anh nhớ nhé."
- Turn 3, 10.5–13.3s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, grand and ceremonial): "Xin mời nhà gái nhận lễ! Trầu cau, rượu chè đủ cả rồi!"
- Pacing: @Tung speaks quickly, then @Vy answers slowly and calmly, then @Tung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a ripple of polite applause, glasses clinking, a microphone hum, high heels on the stage boards. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 2 (`canh-16/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium two-shot at the gift table, locked off.
- Shot 2, 5–10s: 85mm close-up of the groom glancing toward the doors, locked off.
- Shot 3, 10–15s: 50mm over-the-shoulder shot from behind the groom onto the young man with the folder, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Beside a long white-clothed table of betrothal gift trays under red cloth, @Khai opens a black leather document folder the right way up and is already speaking smoothly to @Tung, who adjusts his cufflinks with his mouth closed.
- 1–2s (Shot 1): @Khai keeps talking, businesslike, showing him papers with no readable writing.
- 2–3s (Shot 1): @Khai keeps going, running a finger down to a blank space at the bottom of the page.
- 3–4s (Shot 1): @Khai keeps speaking, tapping the blank space twice.
- 4–5s (Shot 1): @Khai finishes and closes his mouth, holding the folder open.
- 5–6s (CUT to Shot 2): @Tung glances toward the tall doors at the far end of the hall and answers fast and impatiently.
- 6–7s (Shot 2): @Tung keeps talking, tapping his gold wristwatch.
- 7–8s (Shot 2): @Tung keeps going, rising onto his toes to look over the tables.
- 8–9s (Shot 2): @Tung keeps speaking, nodding firmly to himself.
- 9–10s (Shot 2): @Tung finishes and closes his mouth, his eyes still on the doors.
- 10–11s (CUT to Shot 3): @Khai uncaps a gold pen and replies smoothly, his voice oily and reassuring.
- 11–12s (Shot 3): @Khai keeps talking, holding the uncapped pen up between two fingers.
- 12–13s (Shot 3): @Khai keeps going, a sly half-smile spreading under his thin moustache.
- 13–14s (Shot 3): @Khai finishes and closes his mouth, laying the gold pen on the open folder.
- 14–15s (Shot 3): @Khai smooths his thin moustache with a sly half-smile, while @Tung keeps watching the doors, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking at a natural, even conversational pace, slick and businesslike): "Anh Tùng, giấy sang tên nhà đây. Chỉ thiếu mỗi chữ ký của chị Thu nữa thôi."
- Turn 2, 5.2–9.6s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, impatient, eyes on the door): "Sắp đến rồi. Cô ấy hứa ký ngay tại đây, trước bao nhiêu khách. Cô ấy chưa sai hẹn bao giờ."
- Turn 3, 10.1–13.4s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking at a natural, even conversational pace, oily and reassuring): "Bút em mở nắp sẵn rồi, chị ấy đến là ký được ngay."
- Pacing: @Khai speaks at an even everyday pace, then @Tung answers quickly, then @Khai answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: glasses clinking, a leather folder snapping shut, chandelier crystals tinkling, a wristwatch tapped twice. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 3 (`canh-16/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a red silk wedding áo dài embroidered with a gold phoenix, a matching red khăn vấn headband, a thin gold necklace, beige high heels.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the bride at the foot of the stage, turning toward the aisle, locked off.
- Shot 2, 5–11s: 85mm close-up of the tailor holding the red gift box, locked off.
- Shot 3, 11–15s: 50mm over-the-shoulder shot from behind the tailor onto the bride, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): At the foot of the flower-arched stage, @Vy turns toward the center aisle and is already speaking with a mocking smile, as @Thu walks up the aisle in her dark-green apron with the yellow measuring tape around her neck, carrying a large red gift box with a gold ribbon bow, mouth closed.
- 1–2s (Shot 1): @Vy keeps talking, eyebrows raised, eyeing the apron up and down.
- 2–3s (Shot 1): @Vy keeps going, folding her arms with a little laugh.
- 3–4s (Shot 1): @Vy keeps speaking, flicking a glance at the guests' tables.
- 4–5s (Shot 1): @Vy finishes and closes her mouth, arms folded, as @Thu stops a step away from her.
- 5–6s (CUT to Shot 2): @Thu answers slowly and pleasantly, holding the red box in front of her.
- 6–7s (Shot 2): @Thu keeps speaking, unhurried, with a small polite smile.
- 7–8s (Shot 2): @Thu keeps talking, nodding at the red wedding áo dài the bride is wearing.
- 8–9s (Shot 2): @Thu keeps going, glancing down at the gold bow on the red box.
- 9–10s (Shot 2): @Thu keeps speaking, lifting the red box slightly toward the bride.
- 10–11s (Shot 2): @Thu keeps talking, her small polite smile unchanged.
- 11–12s (CUT to Shot 3): @Thu closes her mouth; @Vy's eyes narrow at the red box and she answers with a quick sharp refusal.
- 12–13s (Shot 3): @Vy keeps talking sharply, waving the box away without touching it.
- 13–14s (Shot 3): @Vy keeps going, then finishes and closes her mouth, tightening her folded arms.
- 14–15s (Shot 3): @Vy takes half a step back from the red box, jaw tight, while @Thu stands still holding it out, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.0s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, mocking, eyebrows raised): "Chị đến thật đấy à? Đeo cả tạp dề đi ăn hỏi, đúng là bà thợ may. Khách khứa cười cho đấy."
- Turn 2, 5.5–11.1s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, pleasant and unhurried): "Chị đến giao hàng mà em. Áo em mặc rồi, còn món quà cưới này, chị chuẩn bị lâu lắm."
- Turn 3, 11.6–13.9s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, wary, suddenly sharp): "Quà gì? Em không nhận đâu! Chị mang về mà dùng."
- Pacing: @Vy speaks quickly, then @Thu answers slowly and calmly, then @Vy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: footsteps on carpet, chandelier crystals tinkling, rose petals underfoot, glasses clinking far off. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 4 (`canh-16/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the groom at the betrothal gift table, the open folder before him, locked off.
- Shot 2, 5–10s: 85mm close-up of the tailor across the gift table, slow push-in.
- Shot 3, 10–15s: 50mm over-the-shoulder shot from behind the tailor onto the groom, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): At the white-clothed gift table, @Tung taps an open black leather document folder with a gold pen on top and is already speaking fast and impatiently, as @Thu arrives opposite him carrying a large red gift box with a gold ribbon bow, mouth closed.
- 1–2s (Shot 1): @Tung keeps talking, flicking the gold pen toward the edge of the table.
- 2–3s (Shot 1): @Tung keeps going, clipped and curt, sweeping a hand at the hall.
- 3–4s (Shot 1): @Tung keeps speaking, checking his gold wristwatch.
- 4–5s (Shot 1): @Tung finishes and closes his mouth, holding out the pen.
- 5–6s (CUT to Shot 2): @Thu begins to answer slowly and firmly, ignoring the pen, her eyes on his.
- 6–7s (Shot 2): @Thu keeps speaking as she sets the red gift box down on the table beside the betrothal trays.
- 7–8s (Shot 2): @Thu keeps talking, resting one hand on the gold bow.
- 8–9s (Shot 2): @Thu keeps going, her gaze level.
- 9–10s (Shot 2): @Thu keeps speaking calmly, then finishes.
- 10–11s (CUT to Shot 3): @Thu closes her mouth, her hand on the gold bow; @Tung's eyes drop to the red box, a bead of sweat at his temple, and he asks a question too loudly.
- 11–12s (Shot 3): @Tung keeps talking too loudly, his jaw working.
- 12–13s (Shot 3): @Tung keeps going, pointing at the red box without touching it.
- 13–14s (Shot 3): @Tung finishes and closes his mouth.
- 14–15s (Shot 3): @Tung stares at the red box, sweat beading on his temple, while @Thu keeps her hand on the gold bow, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, impatient and clipped): "Bút đây, ký nhanh rồi về đi. Đừng làm mất thời gian của cả hội trường. Khách đang chờ ăn cỗ."
- Turn 2, 5.3–10.1s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, unhurried and firm): "Anh vội gì. Ký trước cả hội trường thì phải để hai họ xem cho rõ đã."
- Turn 3, 10.6–13.4s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, uneasy, too loud): "Còn xem cái gì nữa? Cô lại định bày trò gì ở đây?"
- Pacing: @Tung speaks quickly, then @Thu answers slowly and calmly, then @Tung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a pen rolling on paper, a box set down on linen, chandelier crystals tinkling, a tense hush over the hall. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 1 (`canh-17/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a red silk wedding áo dài embroidered with a gold phoenix, a matching red khăn vấn headband, a thin gold necklace, beige high heels.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium two-shot by the gift table, locked off.
- Shot 2, 6–10s: 85mm close-up of the bride, the red khăn vấn trembling, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the bride onto the tailor holding the framed photo.
- Shot 4, 13–15s: 40mm medium two-shot by the gift table, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): At the white-clothed gift table, @Thu unties the gold ribbon of a large red gift box, lifts the lid and is already speaking slowly and clearly, while @Vy stands beside the table with her mouth closed.
- 1–2s (Shot 1): @Thu raises from the box a large framed wedding photo of a young couple: a bride with long wavy dark-brown hair and winged eyeliner in a white gown beside a lean groom with a styled black undercut and a thin moustache, and keeps speaking.
- 2–3s (Shot 1): @Thu keeps talking clearly, holding the framed photo steady at chest height toward the hall.
- 3–4s (Shot 1): @Thu keeps speaking, every word placed, her calm eyes on the bride.
- 4–5s (Shot 1): @Thu keeps going, tilting the frame a little so the chandelier light falls on the glass.
- 5–6s (Shot 1): @Thu finishes and closes her mouth, her face calm above the gilded frame.
- 6–7s (CUT to Shot 2): @Vy, the colour draining from her face, starts to speak fast and shrill, flapping both hands at the photo without touching it.
- 7–8s (Shot 2): @Vy keeps talking shrilly, her eyes darting toward the hall.
- 8–9s (Shot 2): @Vy keeps going, shaking her head so the red khăn vấn trembles.
- 9–10s (Shot 2): @Vy finishes and closes her mouth, breathing hard.
- 10–11s (CUT to Shot 3): @Thu answers slowly and coolly, holding the framed photo perfectly still.
- 11–12s (Shot 3): @Thu keeps speaking, tilting her head toward the far end of the gift table.
- 12–13s (Shot 3): @Thu keeps talking, unbothered, her eyes never leaving the bride.
- 13–14s (CUT to Shot 4): @Thu keeps going, finishing with a small polite nod.
- 14–15s (Shot 4): @Thu closes her mouth and holds the framed photo still, while @Vy stares at it, breathing hard, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.0s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, clear, every word placed): "Quà của chị đây. Ảnh cưới lần trước của em, chị xin từ bàn thờ nhà em ở Nam Định."
- Turn 2, 6.5–9.9s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, shrill and cornered): "Ảnh ghép! Chị cắt ghép để bôi nhọ em! Mọi người đừng ai tin bà ta!"
- Turn 3, 10.4–14.1s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, cool, unbothered): "Ghép hay không, em hỏi cậu luật sư cầm cặp ngược kia xem."
- Pacing: @Thu speaks slowly and calmly, then @Vy answers quickly, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: satin ribbon sliding loose, a box lid lifting, chandelier crystals tinkling, a sudden hush across the hall. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 2 (`canh-17/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot past the framed photo onto the groom, locked off.
- Shot 2, 5–10s: 85mm close-up of the young man with the thin moustache, locked off.
- Shot 3, 10–15s: 50mm over-the-shoulder shot from behind the young man onto the groom, slow rack focus.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): A large framed wedding photo of a bride in a white gown beside a lean groom with a styled black undercut and a thin moustache stands among the betrothal trays; @Tung looks from the groom in the frame to @Khai and is already speaking slowly in a hollow voice, while @Khai holds the black leather folder tight, mouth closed.
- 1–2s (Shot 1): @Tung keeps talking, his voice hollow, pointing a limp finger at the photo.
- 2–3s (Shot 1): @Tung keeps going, his face slack, his eyes moving between the photo and the young man.
- 3–4s (Shot 1): @Tung keeps speaking, his voice dropping.
- 4–5s (Shot 1): @Tung finishes and closes his mouth, staring at @Khai.
- 5–6s (CUT to Shot 2): @Khai takes one step back, raising both palms, a plain gold wedding ring glinting on his finger, and answers fast with a forced laugh.
- 6–7s (Shot 2): @Khai keeps talking, his sly half-smile slipping.
- 7–8s (Shot 2): @Khai keeps going, laughing too loudly, sweat on his upper lip.
- 8–9s (Shot 2): @Khai keeps speaking, waving his raised palms.
- 9–10s (Shot 2): @Khai finishes and closes his mouth, palms still raised.
- 10–11s (CUT to Shot 3): @Tung's eyes drop to the plain gold wedding ring on @Khai's raised hand and he asks a short flat question.
- 11–12s (Shot 3): @Tung keeps speaking numbly, his eyes fixed on the ring.
- 12–13s (Shot 3): @Tung keeps talking, his voice going flat.
- 13–14s (Shot 3): @Tung closes his mouth as @Khai slowly lowers his ringed hand behind his back.
- 14–15s (Shot 3): @Tung keeps staring at the hidden hand, while @Khai's forced smile freezes, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking slowly and softly, unhurried, with a short natural pause between phrases, hollow and disbelieving): "Chú rể trong ảnh... là cậu à? Cậu bảo cậu là anh họ của Vy cơ mà?"
- Turn 2, 5.7–10.1s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking quickly in short lively phrases, every word still clear, flustered, forcing a laugh): "Anh nghe em giải thích! Ảnh ấy chụp đóng phim thôi, phim quảng cáo áo cưới ấy mà, anh tin em!"
- Turn 3, 10.6–13.1s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, numb, eyes on his hand): "Thế nhẫn trên tay cậu cũng là đạo cụ à?"
- Pacing: @Tung speaks slowly and calmly, then @Khai answers quickly, then @Tung answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a sudden hush in the hall, a chair scraping, the leather folder creaking in tight fingers, a dry swallow. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 3 (`canh-17/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the old mother rising at the front table, locked off.
- Shot 2, 6–9s: 85mm close-up of the groom, his face drained, locked off.
- Shot 3, 9–15s: 50mm over-the-shoulder shot from behind the groom onto the old mother, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): At the front banquet table under the chandeliers, @BaNhan rises from her chair, leaning on her carved bamboo walking stick, and is already speaking sharply and clearly, her eyes fixed on her son.
- 1–2s (Shot 1): @BaNhan keeps talking, dry and cutting.
- 2–3s (Shot 1): @BaNhan keeps going, lifting her stick a little toward the framed photo on the gift table.
- 3–4s (Shot 1): @BaNhan keeps speaking, one eyebrow raised.
- 4–5s (Shot 1): @BaNhan keeps talking, with a short mocking sniff.
- 5–6s (Shot 1): @BaNhan finishes and closes her mouth, both hands back on the stick.
- 6–7s (CUT to Shot 2): @Tung, his face drained of colour, asks slowly in a hollow voice.
- 7–8s (Shot 2): @Tung keeps speaking, ashen, his lips barely moving.
- 8–9s (Shot 2): @Tung finishes and closes his mouth, swallowing hard.
- 9–10s (CUT to Shot 3): @BaNhan taps her stick once on the floor and answers fast and briskly.
- 10–11s (Shot 3): @BaNhan keeps talking without a pause, her eyebrows raised.
- 11–12s (Shot 3): @BaNhan keeps going, rubbing her thumb and fingers together as if counting banknotes.
- 12–13s (Shot 3): @BaNhan keeps speaking, giving a small sharp nod.
- 13–14s (Shot 3): @BaNhan finishes and closes her mouth, both hands folded on top of her stick.
- 14–15s (Shot 3): @BaNhan looks back at him steadily, while @Tung sways slightly in the foreground, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, sharp and cutting): "Phim gì mà treo ảnh trên bàn thờ nhà gái những ba năm nay? Phim ấy chiếu dài quá nhỉ."
- Turn 2, 6.2–8.7s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking slowly and softly, unhurried, with a short natural pause between phrases, ashen and hollow): "Mẹ... mẹ biết chuyện này từ lâu rồi à?"
- Turn 3, 9.2–13.9s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking quickly in short lively phrases, every word still clear, brisk, merciless): "Từ hôm về quê nó. Cả làng biết, chỉ mỗi anh là không biết. Anh còn mải đếm tiền sính lễ."
- Pacing: @BaNhan speaks at an even everyday pace, then @Tung answers slowly and calmly, then @BaNhan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a chair scraping back, a bamboo stick tapping once on the floor, chandelier crystals tinkling, a heavy silence. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 4 (`canh-17/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- Extra: a stiff middle-aged couple in formal clothes at the front table and a few engagement guests, far in the background and out of focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the tailor beside the betrothal gift table, the front table far behind and out of focus, locked off.
- Shot 2, 5–9s: 85mm close-up of the groom, locked off.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the groom onto the tailor.
- Shot 4, 13–15s: 40mm medium two-shot by the gift table, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Beside the betrothal gift table under the chandeliers, @Thu turns her head toward the front table, where a stiff middle-aged couple sits far behind and out of focus, and is already speaking evenly and clearly.
- 1–2s (Shot 1): @Thu keeps talking calmly, almost gently, nodding toward the blurred couple.
- 2–3s (Shot 1): @Thu keeps speaking, holding up one finger as if quoting a price.
- 3–4s (Shot 1): @Thu keeps going, turning her calm eyes back across the table.
- 4–5s (Shot 1): @Thu keeps talking, then finishes with a small nod.
- 5–6s (CUT to Shot 2): @Thu closes her mouth; @Tung rakes both hands through his gelled hair and answers fast, his voice cracking.
- 6–7s (Shot 2): @Tung keeps talking, his eyes wide, his breath ragged.
- 7–8s (Shot 2): @Tung keeps going, holding up one hand with all his fingers spread.
- 8–9s (Shot 2): @Tung keeps speaking, his voice cracking higher.
- 9–10s (CUT to Shot 3): @Tung closes his mouth, breathing hard; @Thu answers quietly, standing calm and upright.
- 10–11s (Shot 3): @Thu keeps speaking quietly, while @Tung stares at her with his mouth closed.
- 11–12s (Shot 3): @Thu keeps talking, her eyes steady on him.
- 12–13s (Shot 3): @Thu keeps going, slow and final.
- 13–14s (CUT to Shot 4): @Thu finishes and closes her mouth.
- 14–15s (Shot 4): @Tung sinks onto a banquet chair, his gold wristwatch glinting, while @Thu stands calm and upright beside him, the guests a soft blur far behind. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, calm, almost gentle): "Còn ông bà ngồi bàn đầu là diễn viên thuê, một triệu một buổi. Em hỏi giá rồi."
- Turn 2, 5.4–9.0s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, desperate, voice cracking): "Diễn viên? Tôi chuyển cho chúng nó năm tỷ rồi! Năm tỷ đấy, cô có biết không?"
- Turn 3, 9.5–13.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and final): "Biết chứ. Tiền ấy anh tự tay chuyển mà. Anh mời nhầm hai họ rồi."
- Pacing: @Thu speaks at an even everyday pace, then @Tung answers quickly, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a banquet chair creaking under sudden weight, chandelier crystals tinkling, a glass tipping over softly on a tablecloth, a heavy hush. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 1 (`canh-18/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a red silk wedding áo dài embroidered with a gold phoenix, a matching red khăn vấn headband, a thin gold necklace, beige high heels.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 28mm wide shot of the bride standing at the long betrothal table below the stage, facing the camera, slow push-in.
- Shot 2, 3–5s: 50mm medium shot of the bride at the betrothal table, slow push-in.
- Shot 3, 5–10s: 50mm over-the-shoulder shot from behind the bride onto the tailor across the table, locked off.
- Shot 4, 10–15s: 85mm close-up of the bride whirling toward the hall, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy stands at the long betrothal table below the stage in her red wedding áo dài, chin raised, and is already speaking fast and venomous across the table.
- 1–2s (Shot 1): @Vy keeps talking fast, flicking one hand toward the covered trays of betrothal gifts.
- 2–3s (Shot 1): @Vy keeps speaking, leaning over the red cloth, eyes narrowed, her gold necklace catching the light.
- 3–4s (CUT to Shot 2): @Vy goes on without a pause, tapping one red fingernail on the tablecloth.
- 4–5s (Shot 2): @Vy finishes the last words with her chin high and closes her mouth, one hand still raised.
- 5–6s (CUT to Shot 3): @Thu, across the table in her green apron, draws a pink-red land title booklet with no readable writing from her apron pocket and starts answering slowly and coldly.
- 6–7s (Shot 3): @Thu lays the booklet flat on the red cloth and keeps speaking in a quiet ice-cold voice.
- 7–8s (Shot 3): @Thu keeps talking evenly, two fingers resting on the booklet, eyes steady on @Vy.
- 8–9s (Shot 3): @Thu goes on without raising her voice, while @Vy's raised hand sinks, mouth closed.
- 9–10s (Shot 3): @Thu finishes and closes her mouth, two fingers still on the booklet, while @Vy stares down at it with her mouth closed.
- 10–11s (CUT to Shot 4): @Vy whirls toward someone beyond the frame and snaps a furious question, jaw tight.
- 11–12s (Shot 4): @Vy keeps speaking fast at the unseen groom, one finger pointing back at the booklet.
- 12–13s (Shot 4): @Vy keeps talking, her voice climbing, her red khăn vấn headband trembling.
- 13–14s (Shot 4): @Vy says her last words and closes her mouth, breathing hard through her nose.
- 14–15s (Shot 4): @Vy stands rigid with her mouth closed and her jaw tight, the gold phoenix on her silk rising and falling with each breath. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, venomous, chin raised): "Ảnh cũ thì sao nào? Chị vẫn phải ký ly hôn, căn nhà kia vẫn là sính lễ của em!"
- Turn 2, 5.1–9.6s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and ice-cold): "Sổ đỏ căn nhà ấy đây em. Đứng tên chị, từ mười hai năm trước rồi."
- Turn 3, 10.1–13.9s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, rounding on someone off-frame): "Anh Tùng! Anh hứa cho em cái nhà của vợ anh à? Anh lừa cả em đấy à?"
- Pacing: @Vy speaks quickly, then @Thu answers slowly and calmly, then @Vy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a murmur rippling through unseen guests, silk rustling, the soft tap of a booklet laid on cloth, a chandelier crystal tinkling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 2 (`canh-18/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium two-shot of mother and son beside the first round table below the stage, slow push-in.
- Shot 2, 4–10s: 85mm close-up of the old mother leaning on her walking stick, locked off.
- Shot 3, 10–13s: 40mm over-the-shoulder shot from behind the old mother onto her son, locked off.
- Shot 4, 13–15s: 28mm wide shot of mother and son by the first round table under the chandeliers, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tung turns from the stage toward @BaNhan, palms spread wide, his face flushed, and is already speaking fast, while @BaNhan leans on her carved bamboo walking stick with her mouth closed.
- 1–2s (Shot 1): @Tung keeps talking fast, tapping his own chest with his fingertips.
- 2–3s (Shot 1): @Tung keeps speaking, his voice rising, his spread hands trembling in the air.
- 3–4s (Shot 1): @Tung goes on, waving one hand toward the stage and the gold heart backdrop.
- 4–5s (CUT to Shot 2): @Tung finishes and closes his mouth, and @BaNhan lifts her chin and starts answering slowly and sternly.
- 5–6s (Shot 2): @BaNhan keeps speaking slowly, her wrinkled face perfectly still, eyes fixed on her son.
- 6–7s (Shot 2): @BaNhan goes on in a heavy stern voice, both thin hands folded over the head of her bamboo stick.
- 7–8s (Shot 2): @BaNhan keeps speaking without blinking, one eyebrow lifting slightly.
- 8–9s (Shot 2): @BaNhan keeps talking, tapping one finger on the head of the stick.
- 9–10s (Shot 2): @BaNhan says the last words slowly, her lips thin.
- 10–11s (CUT to Shot 3): @BaNhan closes her mouth, and @Tung, his spread hands dropping, starts asking a childish question.
- 11–12s (Shot 3): @Tung keeps talking fast, his voice cracking, his eyes darting to his mother's face.
- 12–13s (Shot 3): @Tung keeps speaking, swaying half a step back.
- 13–14s (CUT to Shot 4): @Tung finishes and closes his mouth, his shoulders sagging.
- 14–15s (Shot 4): @BaNhan taps the tip of her stick once on the carpet, both silent, while @Tung lowers his eyes with his mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, frantic disbelief): "Không thể nào! Nhà con bỏ tiền ra xây, công ty con một tay gây dựng cơ mà!"
- Turn 2, 4.7–10.3s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking slowly and softly, unhurried, with a short natural pause between phrases, stern and heavy): "Bằng tiền mảnh đất bố cái Thu để lại đấy. Giấy con ký, con quên, chứ mẹ chưa quên."
- Turn 3, 10.8–13.3s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, cornered, almost childish): "Sao hồi ấy mẹ không nhắc con lấy một câu hả mẹ?"
- Pacing: @Tung speaks quickly, then @BaNhan answers slowly and calmly, then @Tung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a sharp hush falling over unseen guests, wine glasses chiming softly, the tap of a bamboo stick on carpet. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 3 (`canh-18/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the tailor bending over the signing table, slow tilt up.
- Shot 2, 5–9s: 85mm close-up of the husband sinking onto a banquet chair, locked off.
- Shot 3, 9–12s: 40mm medium two-shot across the table, the tailor standing over the seated husband, locked off.
- Shot 4, 12–15s: 85mm close-up of the tailor, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu bends over the white tablecloth with an uncapped black pen, divorce papers with no readable writing in front of her, and is already speaking in a level businesslike voice.
- 1–2s (Shot 1): @Thu keeps talking evenly as she signs the papers in one unhurried stroke.
- 2–3s (Shot 1): @Thu keeps speaking, turning the page and signing again without looking up.
- 3–4s (Shot 1): @Thu straightens up and goes on calmly, squaring the stack beside the pink-red land title booklet.
- 4–5s (Shot 1): @Thu finishes and closes her mouth, sliding the signed papers across the table toward @Tung.
- 5–6s (CUT to Shot 2): @Tung sinks heavily onto a banquet chair and starts answering in a broken whisper, his face drained.
- 6–7s (Shot 2): @Tung keeps whispering, his hands open on his knees, eyes glistening.
- 7–8s (Shot 2): @Tung keeps talking, his voice cracking, staring up at her.
- 8–9s (Shot 2): @Tung finishes and closes his mouth, lips trembling.
- 9–10s (CUT to Shot 3): @Thu caps the pen and answers slowly and quietly, looking down at @Tung.
- 10–11s (Shot 3): @Thu keeps speaking calmly, not unkind, her hands resting on the signed papers.
- 11–12s (Shot 3): @Thu keeps talking, her voice softening a little.
- 12–13s (CUT to Shot 4): @Thu keeps speaking slowly, her eyes steady and calm.
- 13–14s (Shot 4): @Thu says the last words and closes her mouth.
- 14–15s (Shot 4): @Thu smooths the yellow tailor's measuring tape around her neck in silence, mouth closed, her eyes on the papers. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, businesslike, pen still moving): "Đơn ly hôn em ký rồi. Nhà, với sáu mươi phần trăm cổ phần, là của em."
- Turn 2, 5.2–8.7s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, broken, barely above a whisper): "Thu ơi, anh xin em. Anh mất hết rồi, anh còn gì nữa đâu."
- Turn 3, 9.2–14.0s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, calm, cool, not unkind): "Còn chứ. Anh còn nợ con một bữa cơm, con bé vẫn để phần bát cho bố."
- Pacing: @Thu speaks at an even everyday pace, then @Tung answers at an even everyday pace, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a pen scratching across paper, a banquet chair creaking under sudden weight, a hushed hall, one long shaky breath. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 4 (`canh-18/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a red silk wedding áo dài embroidered with a gold phoenix, a matching red khăn vấn headband, a thin gold necklace, beige high heels.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the man in black slipping behind the flower arch, handheld.
- Shot 2, 5–9s: 85mm close-up of the bride in the shadows, golden light flickering on her face.
- Shot 3, 9–13s: 40mm medium two-shot of the couple edging along the back of the backdrop, slow lateral track.
- Shot 4, 13–15s: 28mm wide shot of the dark wings behind the stage as the couple reaches the side door, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khai slips behind the flower arch with the black leather document folder under his arm, glances back and is already speaking fast in a low hiss.
- 1–2s (Shot 1): @Khai keeps hissing urgently, tapping the folder with two fingers.
- 2–3s (Shot 1): @Khai keeps talking quickly over his shoulder, eyes darting to the gaps in the roses.
- 3–4s (Shot 1): @Khai goes on in a rapid whisper, golden light from the hall flickering through the roses onto his face.
- 4–5s (Shot 1): @Khai finishes and closes his mouth, beckoning someone in after him.
- 5–6s (CUT to Shot 2): @Vy hurries in, gathers the long front flap of her red wedding áo dài in one hand and answers in a breathless whisper.
- 6–7s (Shot 2): @Vy keeps whispering fast, pointing toward a dark side door beyond the coils of cable.
- 7–8s (Shot 2): @Vy keeps whispering, her eyes on the glowing gaps in the arch, her red khăn vấn headband askew.
- 8–9s (Shot 2): @Vy finishes and closes her mouth, catching her breath.
- 9–10s (CUT to Shot 3): @Khai nods and replies low and quick, already moving along the back of the backdrop.
- 10–11s (Shot 3): @Khai keeps speaking low and decisive, while @Vy follows close behind with her mouth closed.
- 11–12s (Shot 3): @Khai keeps talking under his breath, the folder pressed to his chest.
- 12–13s (Shot 3): @Khai finishes and closes his mouth, one hand reaching for the handle of the dark side door.
- 13–14s (CUT to Shot 4): Both stand silent at the side door, golden light flickering over their faces as the murmur of the hall swells behind the backdrop.
- 14–15s (Shot 4): @Khai eases the side door open onto darkness, and @Vy follows him through in tiny steps, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking quickly in short lively phrases, every word still clear, hushed and urgent): "Tiền vẫn nằm yên trong tài khoản. Đi ngay, kẻo bà vợ cả lại lôi thêm cái gì ra nữa!"
- Turn 2, 5.1–8.7s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, breathless whisper): "Lối thoát hiểm sau bếp, anh đi trước đi. Xe em đỗ sẵn ở cửa sau rồi."
- Turn 3, 9.2–13.0s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking at a natural, even conversational pace, low and decisive, already moving): "Hai vé bay sáng ngày kia trong túi em, đổi ngay sang chuyến đêm nay."
- Pacing: @Khai speaks quickly, then @Vy answers quickly, then @Khai answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the muffled murmur of the banquet hall beyond the backdrop, rustling silk, quick hushed footsteps on wooden boards, a cable rattling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 1 (`canh-19/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A narrow hotel service corridor behind the banquet hall at night: bare concrete walls, stacked banquet chairs and linen carts, humming fluorescent light, a frosted glass exit door at the far end pulsing with blue and red light from outside.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a red silk wedding áo dài embroidered with a gold phoenix, a matching red khăn vấn headband, a thin gold necklace, beige high heels.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium tracking shot backward in front of the bride as she shuffles along the corridor.
- Shot 2, 5–9s: 85mm close-up of the man in black spinning round, locked off.
- Shot 3, 9–12s: 50mm over-the-shoulder shot from behind the man in black onto the bride, locked off.
- Shot 4, 12–15s: 40mm medium two-shot tracking backward in front of the couple down the corridor.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy shuffles along the empty service corridor in tiny hobbled steps, the tight red wedding áo dài holding her knees together, and is already speaking fast and breathless.
- 1–2s (Shot 1): @Vy keeps whining as she totters forward, one hand on the bare concrete wall, her beige high heels clacking.
- 2–3s (Shot 1): @Vy keeps talking breathlessly, glaring ahead down the corridor.
- 3–4s (Shot 1): @Vy goes on, panting, her knees held together by the tight silk.
- 4–5s (Shot 1): @Vy finishes and closes her mouth, gasping for air.
- 5–6s (CUT to Shot 2): @Khai, striding ahead, spins round, waving the black leather document folder, and answers in a sharp exasperated hiss.
- 6–7s (Shot 2): @Khai keeps hissing, pointing the folder at her tight red silk.
- 7–8s (Shot 2): @Khai keeps talking fast, his thin moustache twitching, eyes flicking to the far door.
- 8–9s (Shot 2): @Khai finishes and closes his mouth, beckoning hard with the folder.
- 9–10s (CUT to Shot 3): @Vy pouts and starts answering back in a sulky voice, still shuffling toward him in tiny steps.
- 10–11s (Shot 3): @Vy keeps talking sulkily, smoothing the gold phoenix on her silk with one hand.
- 11–12s (Shot 3): @Vy keeps speaking, lips pouting, while @Khai listens with his mouth closed.
- 12–13s (CUT to Shot 4): @Vy finishes and closes her mouth as @Khai turns back toward the far door.
- 13–14s (Shot 4): @Vy shuffles faster in tiny steps after @Khai, both silent, the frosted exit door glowing ahead of them.
- 14–15s (Shot 4): @Vy's flushed face and smudged red lipstick lead the frame as she hurries on behind @Khai, both silent, mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, panting and whiny): "Anh đợi em với! Áo bó quá, đầu gối em dính chặt vào nhau, chỉ nhích được từng tí một!"
- Turn 2, 5.1–8.7s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking quickly in short lively phrases, every word still clear, exasperated hiss): "Áo vợ thằng Tùng may mà em cũng dám mặc à? Nhấc chân lên, nhanh lên nào!"
- Turn 3, 9.2–13.0s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, sulky, still shuffling): "Đẹp thì em mặc! Ai biết hôm nay lại phải chạy thục mạng thế này!"
- Pacing: @Vy speaks quickly, then @Khai answers quickly, then @Vy answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: fluorescent hum, high heels clacking fast on concrete, rustling silk, a linen cart rattling as they pass. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 2 (`canh-19/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A narrow hotel service corridor behind the banquet hall at night: bare concrete walls, stacked banquet chairs and linen carts, humming fluorescent light, a frosted glass exit door at the far end pulsing with blue and red light from outside.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a red silk wedding áo dài embroidered with a gold phoenix, a matching red khăn vấn headband, a thin gold necklace, beige high heels.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 40mm medium two-shot tracking backward in front of the couple down the corridor, holding the previous framing.
- Shot 2, 4–9s: 85mm close-up of the man in black, blue and red light sweeping his face, locked off.
- Shot 3, 9–12s: 50mm over-the-shoulder shot from behind the man in black onto the bride, slow push-in.
- Shot 4, 12–15s: 100mm extreme close-up of the bride's face, blue and red light sweeping across it, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy hurries the last steps toward the frosted glass exit door behind @Khai and is already speaking in a frantic hiss, flapping a hand at the door.
- 1–2s (Shot 1): @Vy keeps whispering fast, while @Khai pulls up short before the glass with his mouth closed.
- 2–3s (Shot 1): @Vy keeps talking, pointing past him at the door, her face washed red then blue by the light through the glass.
- 3–4s (Shot 1): @Vy goes on urgently, tugging at the tight red silk at her knees.
- 4–5s (CUT to Shot 2): @Vy finishes and closes her mouth, and @Khai, his eyes on the pulsing glass, starts answering in a flat hollow voice.
- 5–6s (Shot 2): @Khai keeps speaking flatly, nodding at the frosted glass.
- 6–7s (Shot 2): @Khai keeps talking, the blue and red light sweeping across his face, the folder hanging limp at his side.
- 7–8s (Shot 2): @Khai goes on in the same hollow voice, his shoulders dropping.
- 8–9s (Shot 2): @Khai keeps speaking quietly to the end, staring at the glass.
- 9–10s (CUT to Shot 3): @Khai closes his mouth, and @Vy turns her head to look back down the long corridor and starts murmuring slowly in a shaky whisper.
- 10–11s (Shot 3): @Vy keeps whispering, her fingers twisting the red silk at her hip.
- 11–12s (Shot 3): @Vy keeps murmuring, her eyes wide.
- 12–13s (CUT to Shot 4): @Vy keeps whispering, the light flashing red then blue across her cheek.
- 13–14s (Shot 4): @Vy finishes and closes her mouth, her lips trembling.
- 14–15s (Shot 4): @Vy stands motionless with her mouth closed, blue and red light sweeping across her face and the red khăn vấn headband. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, frantic whisper): "Anh đứng ngây ra đấy làm gì? Mở cửa ra đi, xe mình ở ngay ngoài kia rồi!"
- Turn 2, 4.7–9.2s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking at a natural, even conversational pace, flat and hollow): "Em nhìn qua kính mà xem. Đèn xanh, đèn đỏ. Xe ngoài kia không phải xe mình đâu."
- Turn 3, 9.7–13.4s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking slowly and softly, unhurried, with a short natural pause between phrases, shaky, almost a whisper): "Bà thợ may ấy đo cả đường chạy của mình rồi, anh ơi."
- Pacing: @Vy speaks quickly, then @Khai answers at an even everyday pace, then @Vy answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a siren whooping once outside, fluorescent hum, fast shallow breathing, silk rustling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 3 (`canh-19/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A narrow hotel service corridor behind the banquet hall at night: bare concrete walls, stacked banquet chairs and linen carts, humming fluorescent light, a frosted glass exit door at the far end pulsing with blue and red light from outside.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a red silk wedding áo dài embroidered with a gold phoenix, a matching red khăn vấn headband, a thin gold necklace, beige high heels.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the tailor stepping through the swinging kitchen door, slow pan.
- Shot 2, 5–9s: 85mm close-up of the bride whirling round, locked off.
- Shot 3, 9–12s: 50mm over-the-shoulder shot from behind the bride onto the tailor, locked off.
- Shot 4, 12–15s: 40mm medium two-shot in profile down the corridor, slow drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu steps through the swinging kitchen door in her green apron, stops several paces away with her hands folded and is already speaking in a dry, almost polite voice.
- 1–2s (Shot 1): @Thu keeps talking evenly, tilting her head toward the noise of the banquet hall behind her.
- 2–3s (Shot 1): @Thu keeps speaking, the kitchen door still swinging on its hinge behind her.
- 3–4s (Shot 1): @Thu goes on calmly, her eyes resting on the tight red silk.
- 4–5s (Shot 1): @Thu finishes and closes her mouth, hands still folded on her green apron.
- 5–6s (CUT to Shot 2): @Vy whirls round and answers fast in a cracked, furious voice, tears smearing her winged eyeliner.
- 6–7s (Shot 2): @Vy keeps sobbing out the words, her chin trembling and her chest heaving.
- 7–8s (Shot 2): @Vy keeps talking fast, pointing down at her own hobbled knees.
- 8–9s (Shot 2): @Vy finishes and closes her mouth, breathing hard.
- 9–10s (CUT to Shot 3): @Thu answers slowly and evenly from where she stands, keeping her distance.
- 10–11s (Shot 3): @Thu keeps speaking calmly, one hand lifting toward the hem without coming any closer.
- 11–12s (Shot 3): @Thu keeps talking, her voice never rising, the blue and red light pulsing on the wall behind @Vy.
- 12–13s (CUT to Shot 4): @Thu keeps speaking evenly, while @Vy listens with her mouth closed and her chest heaving.
- 13–14s (Shot 4): @Thu finishes, closes her mouth and gives one small nod.
- 14–15s (Shot 4): @Vy looks down at her own hobbled knees in the tight silk with her mouth closed, while @Thu stands still and silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, dry, almost polite): "Em đi đâu mà vội thế? Tiệc còn chưa xong, hai họ vẫn đang chờ kia mà."
- Turn 2, 5.2–8.6s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, sobbing with fury): "Chị cố tình may chật để em không chạy được! Chị tính cả rồi chứ gì!"
- Turn 3, 9.1–13.6s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, even and unhurried): "Áo dài thì phải khít. Mặc nó để bước cho đàng hoàng, đâu phải để chạy."
- Pacing: @Thu speaks at an even everyday pace, then @Vy answers quickly, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a fluorescent tube buzzing and flickering, a kitchen door swinging on its hinge, ragged sobbing breath, a distant siren. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 4 (`canh-19/clip-4.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A narrow hotel service corridor behind the banquet hall at night: bare concrete walls, stacked banquet chairs and linen carts, humming fluorescent light, a frosted glass exit door at the far end pulsing with blue and red light from outside.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a red silk wedding áo dài embroidered with a gold phoenix, a matching red khăn vấn headband, a thin gold necklace, beige high heels.
- @Khai = Khải, 30, Vy's secret husband who poses as her lawyer cousin; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 85mm close-up of the bride facing the frosted glass exit door, blue and red light pulsing on her face, locked off.
- Shot 2, 4–8s: 40mm medium two-shot of the couple before the frosted door, slow push-in.
- Shot 3, 8–10s: 85mm close-up of the man in black, blue and red light on his face, locked off.
- Shot 4, 10–13s: 50mm over-the-shoulder shot from behind the man in black onto the bride, locked off.
- Shot 5, 13–15s: 35mm wide two-shot of the couple before the frosted door, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy stands facing the frosted glass exit door, blue and red light pulsing over her smudged red lipstick, and is already asking a small lost question without looking away.
- 1–2s (Shot 1): @Vy keeps speaking in a small voice, her eyes glistening in the pulsing light.
- 2–3s (Shot 1): @Vy keeps talking, glancing at the dark corridor behind her and back at the glass.
- 3–4s (Shot 1): @Vy goes on, her voice thinning to almost nothing.
- 4–5s (CUT to Shot 2): @Vy finishes and closes her mouth, and @Khai sets the black leather document folder down on the concrete and starts answering in a low bitter voice.
- 5–6s (Shot 2): @Khai slowly raises both open hands to shoulder height, still talking, with a dry half-laugh.
- 6–7s (Shot 2): @Khai keeps speaking bitterly, his raised palms bathed in blue and red light.
- 7–8s (Shot 2): @Khai keeps talking, a crooked half-smile under his thin moustache.
- 8–9s (CUT to Shot 3): @Khai goes on with a dry laugh, shaking his head slowly at the glass.
- 9–10s (Shot 3): @Khai keeps speaking to the last words, his eyes half-closed.
- 10–11s (CUT to Shot 4): @Khai closes his mouth, and @Vy slowly raises her trembling hands too, the red silk sleeves sliding down her wrists, and starts murmuring in a broken voice.
- 11–12s (Shot 4): @Vy keeps murmuring, her eyes on the floor, while @Khai stands with his hands raised and his mouth closed.
- 12–13s (Shot 4): @Vy keeps speaking in a hollow whisper to the end of the line.
- 13–14s (CUT to Shot 5): @Vy finishes the last word, closes her mouth and lowers her eyes.
- 14–15s (Shot 5): Both stand with open raised hands and mouths closed as the blue and red light floods over their faces and the gold phoenix on her silk. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, small and lost): "Giờ mình phải làm sao hả anh? Cửa trước, cửa sau đều có người canh rồi."
- Turn 2, 4.9–10.2s, spoken on camera by @Khai (man of 30, smooth lazy tenor, slightly nasal, sly and drawling, speaking at a natural, even conversational pace, bitter, with a dry half-laugh): "Giơ tay lên. Lừa hai lão trót lọt, đến lão thứ ba lại trắng tay vì một người cầm thước dây."
- Turn 3, 10.7–13.2s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking slowly and softly, unhurried, with a short natural pause between phrases, broken and hollow): "Thôi anh. Tại em đặt áo cưới nhầm tiệm."
- Pacing: @Vy speaks at an even everyday pace, then @Khai answers at an even everyday pace, then @Vy answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a siren winding down just outside, the crackle of a distant radio, fluorescent hum, one shaky breath. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 1 (`canh-20/clip-1.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium tracking shot of the man trudging into the middle of the deserted hall with a phone at his ear.
- Shot 2, 4–8s: 85mm close-up of his face as he sinks onto a banquet chair, locked off.
- Shot 3, 8–11s: 40mm medium shot of him seated alone among the empty tables, slow drift.
- Shot 4, 11–13s: 85mm close-up of his face, the phone at his ear, locked off.
- Shot 5, 13–15s: 100mm extreme close-up of the phone on his knee above the petal-strewn carpet, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tung trudges into the middle of the empty banquet hall, a phone with a glowing blank screen pressed to his ear, and is already speaking in a flat hollow voice, his suit jacket crumpled.
- 1–2s (Shot 1): @Tung keeps talking into the phone in short tired phrases, stepping over scattered rose petals.
- 2–3s (Shot 1): @Tung stops walking and keeps speaking, his free hand rubbing his forehead.
- 3–4s (Shot 1): @Tung keeps talking into the phone, eyes half-closed, his face grey in the low light.
- 4–5s (CUT to Shot 2): @Tung sinks onto a banquet chair, still speaking flatly into the phone.
- 5–6s (Shot 2): @Tung keeps speaking, his free hand hanging between his knees.
- 6–7s (Shot 2): @Tung keeps talking, a bitter little breath escaping between phrases.
- 7–8s (Shot 2): @Tung keeps speaking quietly, nodding at nothing.
- 8–9s (CUT to Shot 3): @Tung keeps talking, slumped on the chair among the abandoned round tables, one chandelier glowing low above him.
- 9–10s (Shot 3): @Tung goes on in a dull murmur, staring at the drooping flower arch on the stage.
- 10–11s (Shot 3): @Tung keeps speaking, his voice dropping lower.
- 11–12s (CUT to Shot 4): @Tung keeps murmuring into the phone, his eyes wet.
- 12–13s (Shot 4): @Tung says the last tired words, closes his mouth and lowers the phone from his ear.
- 13–14s (CUT to Shot 5): @Tung's hand lays the phone with its glowing blank screen on his knee, rose petals scattered on the carpet below.
- 14–15s (Shot 5): A single rose petal drifts down and settles beside @Tung's polished black shoe. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.9s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, flat and hollow, drained of everything), in Vietnamese with exact lip-sync, said exactly once: "Vâng, tôi nghe đây. Tài khoản bị phong toả rồi ạ? Năm tỷ trả về công ty... Vâng, công ty của vợ tôi. Hai người ấy khai cả rồi à? Không, tôi chưa về đâu, về cũng chẳng còn ai đợi. Tôi ngồi đây thêm một lúc. Cảm ơn anh." (no subtitles)
- @Tung starts talking within the first second; whenever @Tung speaks, the face and lips are clearly visible in that shot; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the hum of a nearly empty hall, a phone call clicking off, a chair creaking, rose petals settling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 2 (`canh-20/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium two-shot of the old mother standing beside her seated son under the single chandelier, slow push-in.
- Shot 2, 5–9s: 85mm close-up of the son lifting his wet face, locked off.
- Shot 3, 9–13s: 40mm over-the-shoulder shot from behind the seated son up to the old mother, locked off.
- Shot 4, 13–15s: 50mm medium two-shot of mother and son under the single chandelier, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan stands beside @Tung's chair, leaning on her carved bamboo walking stick, and is already speaking slowly and heavily down to him, while @Tung sits slumped with his mouth closed.
- 1–2s (Shot 1): @BaNhan keeps speaking in a heavy sorrowful voice, her eyes on the top of her son's head.
- 2–3s (Shot 1): @BaNhan keeps talking slowly, both thin hands folded on the head of her stick.
- 3–4s (Shot 1): @BaNhan goes on, her gaze lifting to the drooping flower arch on the stage.
- 4–5s (Shot 1): @BaNhan keeps speaking toward the last words, her voice catching slightly.
- 5–6s (CUT to Shot 2): @BaNhan closes her mouth, and @Tung lifts his wet face and starts asking a bitter question, eyes red-rimmed.
- 6–7s (Shot 2): @Tung keeps speaking bitterly, his voice cracking, his hands limp on his knees.
- 7–8s (Shot 2): @Tung keeps talking, a wet half-laugh escaping him.
- 8–9s (Shot 2): @Tung finishes and closes his mouth, staring up at her.
- 9–10s (CUT to Shot 3): @BaNhan answers in a dry cutting voice, her wrinkled hand tightening on the stick.
- 10–11s (Shot 3): @BaNhan keeps speaking, dry and cutting, looking down at him without blinking.
- 11–12s (Shot 3): @BaNhan keeps talking, tipping her head toward the drooping flower arch on the stage.
- 12–13s (Shot 3): @BaNhan keeps speaking slowly, while @Tung lowers his head with his mouth closed.
- 13–14s (CUT to Shot 4): @BaNhan finishes her last words and closes her mouth.
- 14–15s (Shot 4): @Tung lifts his tear-streaked face toward his mother, his chin trembling, mouth closed, while @BaNhan stands silent over him. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.1s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking slowly and softly, unhurried, with a short natural pause between phrases, heavy and sorrowful): "Mẹ đặt tên con là Tùng, mong con cứng như cây tùng, gió mấy cũng đứng."
- Turn 2, 5.6–8.8s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, bitter, self-pitying): "Mẹ ra đây để mắng con nốt đấy à? Mắng đi, con chịu hết mà."
- Turn 3, 9.3–13.6s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, dry and cutting): "Mắng gì nữa. Một tà váy đỏ lướt qua là cây tùng nhà mẹ đổ rạp."
- Pacing: @BaNhan speaks slowly and calmly, then @Tung answers quickly, then @BaNhan answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the slow tap of a bamboo stick on carpet, a long shaky breath, the hush of the empty hall, a chair creaking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 3 (`canh-20/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium two-shot of mother and son under the single chandelier, holding the previous framing.
- Shot 2, 6–11s: 85mm close-up of the old mother, her eyes on the dim stage, locked off.
- Shot 3, 11–13s: 50mm over-the-shoulder shot from behind the old mother onto her son, locked off.
- Shot 4, 13–15s: 85mm close-up two-shot of mother and son side by side, slow drift.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan lowers herself slowly onto the banquet chair beside @Tung, while @Tung is already speaking slowly in a cracked voice without looking up.
- 1–2s (Shot 1): @Tung keeps speaking, his voice breaking, while @BaNhan lays the bamboo walking stick across her knees with her mouth closed.
- 2–3s (Shot 1): @Tung keeps talking through tears, rose petals around their feet.
- 3–4s (Shot 1): @Tung goes on, shaking his head slowly at himself.
- 4–5s (Shot 1): @Tung keeps speaking, wiping his wet cheek with the back of his hand.
- 5–6s (Shot 1): @Tung finishes and closes his mouth, his chin trembling.
- 6–7s (CUT to Shot 2): @BaNhan starts answering slowly and firmly, her eyes on the dim stage.
- 7–8s (Shot 2): @BaNhan keeps speaking firmly but gently, her wrinkled face lit by the single chandelier.
- 8–9s (Shot 2): @BaNhan keeps talking slowly, her thin fingers resting on the stick across her knees.
- 9–10s (Shot 2): @BaNhan goes on, firm, pressing her lips thin between phrases.
- 10–11s (Shot 2): @BaNhan says her last words slowly and steadily and closes her mouth.
- 11–12s (CUT to Shot 3): @Tung turns to her and starts asking in a small lost voice, his red-rimmed eyes searching her face.
- 12–13s (Shot 3): @Tung keeps asking quietly, his hands open on his knees.
- 13–14s (CUT to Shot 4): @Tung keeps speaking softly, leaning toward her.
- 14–15s (Shot 4): @Tung finishes and closes his mouth, while @BaNhan slowly turns her head to study his face, her lips pursed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking slowly and softly, unhurried, with a short natural pause between phrases, cracking into tears): "Mẹ ơi, con sai thật rồi. Ngọc trong nhà không biết giữ, lại đi rước sỏi ngoài đường về."
- Turn 2, 6.2–10.9s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking slowly and softly, unhurried, with a short natural pause between phrases, firm but gentle): "Sai thì sửa. Nhưng sửa thế nào, lần này không đến lượt con chọn nữa đâu."
- Turn 3, 11.4–14.2s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, small and lost): "Thế bây giờ con phải bắt đầu từ đâu hả mẹ?"
- Pacing: @Tung speaks slowly and calmly, then @BaNhan answers slowly and calmly, then @Tung answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a chair creaking as she sits, a distant door closing somewhere in the hotel, quiet sniffing, the hush of the empty hall. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 4 (`canh-20/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A lavish hotel banquet hall set for an engagement ceremony in the evening: round tables with white cloths and red roses, a low stage with a flower arch and a gold heart backdrop with no letters, trays of betrothal gifts covered in red cloth, crystal chandeliers, warm golden light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 85mm close-up two-shot of mother and son side by side, holding the previous framing.
- Shot 2, 3–6s: 50mm medium two-shot from a low angle as the old mother rises and stands over her seated son, locked off.
- Shot 3, 6–11s: 85mm close-up of the son looking up, locked off.
- Shot 4, 11–15s: 35mm medium-wide two-shot from the stage edge, the old mother between the empty tables and her son seated in the foreground, slow pull-back.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan, sitting beside @Tung, is already speaking in a dry wry voice, one eyebrow raised, while @Tung watches her with wet eyes and his mouth closed.
- 1–2s (Shot 1): @BaNhan keeps talking dryly, pointing her stick toward the far doors of the hall.
- 2–3s (Shot 1): @BaNhan keeps speaking, tilting her head as she weighs her words.
- 3–4s (CUT to Shot 2): @BaNhan goes on as she plants the tip of the bamboo walking stick on the carpet and rises slowly from the chair.
- 4–5s (Shot 2): @BaNhan keeps talking in the same wry voice, standing over @Tung, one thin hand spread palm-up.
- 5–6s (Shot 2): @BaNhan says the last words with a small shrug and closes her mouth, and @Tung nods slowly and starts answering in a quiet steady voice.
- 6–7s (CUT to Shot 3): @Tung keeps speaking quietly, his jaw setting, his eyes clear.
- 7–8s (Shot 3): @Tung keeps talking, looking up at her without blinking.
- 8–9s (Shot 3): @Tung goes on, his hands closing slowly on his knees.
- 9–10s (Shot 3): @Tung keeps speaking steadily to the end of the line.
- 10–11s (Shot 3): @Tung finishes and closes his mouth, still looking up at her.
- 11–12s (CUT to Shot 4): @BaNhan turns toward the far doors, then glances back and adds a brisk parting remark, speaking quickly.
- 12–13s (Shot 4): @BaNhan keeps talking briskly, wagging one thin finger at him.
- 13–14s (Shot 4): @BaNhan finishes and closes her mouth, then shuffles off between the empty tables, her stick tapping on the carpet.
- 14–15s (Shot 4): @Tung sits alone among the scattered rose petals with his mouth closed, watching her small figure go. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, dry and wry): "Sáng mai ra tiệm may mà xin lỗi vợ con. Nó có tha hay không, mẹ không dám hứa."
- Turn 2, 5.9–10.7s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet resolve): "Tha hay không, con vẫn phải đi. Con nợ cô ấy nhiều hơn một câu xin lỗi."
- Turn 3, 11.2–13.9s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking quickly in short lively phrases, every word still clear, a brisk parting jab): "Mà nhớ, đi tay không thôi, quà cáp nó không nhận đâu."
- Pacing: @BaNhan speaks at an even everyday pace, then @Tung answers slowly and calmly, then @BaNhan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a bamboo stick tapping slowly away across the carpet, a chair creaking, the hum of the empty hall. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 1 (`canh-21/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A construction company boardroom high in a Hà Nội tower by day: a long glossy table lined with black leather chairs, white architectural models along the wall, floor-to-ceiling windows over the city, crisp daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the woman in the tall black leather chair at the head of the table, the city windows behind her, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the husband standing at the corner of the table, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the husband onto the woman at the head of the table, locked off.
- Shot 4, 13–15s: 40mm medium two-shot at the head of the table in profile, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu sits in the tall black leather chair at the head of the long glossy table, the yellow measuring tape around her neck, and is already speaking dryly, nodding at an empty chair.
- 1–2s (Shot 1): @Thu keeps talking in the same dry tone, one hand resting flat on a stack of papers with no readable writing.
- 2–3s (Shot 1): @Thu keeps speaking, eyebrows lifted toward the corner of the table.
- 3–4s (Shot 1): @Thu goes on evenly, nodding again at the empty chair beside her.
- 4–5s (Shot 1): @Thu finishes and closes her mouth, waiting.
- 5–6s (CUT to Shot 2): @Tung, standing at the corner of the table in his charcoal suit with his hands clasped, starts answering slowly and humbly, head bowed.
- 6–7s (Shot 2): @Tung keeps speaking quietly, his eyes on the glossy tabletop.
- 7–8s (Shot 2): @Tung keeps talking, his clasped hands tightening, a bead of sweat at his temple.
- 8–9s (Shot 2): @Tung goes on, lifting his eyes to her for a moment.
- 9–10s (Shot 2): @Tung finishes and closes his mouth, lowering his eyes.
- 10–11s (CUT to Shot 3): @Thu squares the stack of papers with both hands and answers in a clear businesslike voice, looking straight at @Tung.
- 11–12s (Shot 3): @Thu keeps speaking crisply, tapping the top sheet once with a pen.
- 12–13s (Shot 3): @Thu keeps talking, her eyes never leaving him.
- 13–14s (CUT to Shot 4): @Thu finishes and closes her mouth, laying the pen neatly beside the papers.
- 14–15s (Shot 4): @Tung swallows and nods once at the corner of the table, his face toward her, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, dry, nodding at a chair): "Anh ngồi đi. Họp cổ đông chứ có phải hầu toà đâu mà anh đứng mãi thế."
- Turn 2, 5.2–10.0s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking slowly and softly, unhurried, with a short natural pause between phrases, humble, head bowed): "Anh đứng được rồi. Em là cổ đông lớn nhất, em quyết thế nào anh nghe thế."
- Turn 3, 10.5–14.0s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, crisp and businesslike): "Ghế giám đốc cần người đọc giấy trước khi ký. Anh chưa làm được."
- Pacing: @Thu speaks at an even everyday pace, then @Tung answers slowly and calmly, then @Thu answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the quiet hum of air conditioning, papers squared against the glossy table, a pen set down, faint city traffic far below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 2 (`canh-21/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A construction company boardroom high in a Hà Nội tower by day: a long glossy table lined with black leather chairs, white architectural models along the wall, floor-to-ceiling windows over the city, crisp daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 40mm medium two-shot at the head of the table in profile, holding the previous framing.
- Shot 2, 4–10s: 85mm close-up of the woman at the head of the table, locked off.
- Shot 3, 10–13s: 50mm medium shot of the husband at the corner of the table, slow push-in.
- Shot 4, 13–15s: 28mm wide two-shot across the corner of the table toward the city windows, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tung swallows, his head bowed and his clasped hands tightening, and is already speaking slowly, while @Thu watches him with her mouth closed.
- 1–2s (Shot 1): @Tung keeps speaking humbly, his eyes on the table.
- 2–3s (Shot 1): @Tung keeps talking, lifting his eyes to her for a moment.
- 3–4s (Shot 1): @Tung goes on, nodding to himself as if to seal the promise.
- 4–5s (CUT to Shot 2): @Tung finishes and closes his mouth, and @Thu starts answering slowly and firmly, her face calm.
- 5–6s (Shot 2): @Thu keeps speaking, sliding a single sheet with no readable writing down the glossy table toward @Tung.
- 6–7s (Shot 2): @Thu keeps talking evenly, her fingertips leaving the sheet.
- 7–8s (Shot 2): @Thu keeps speaking, her eyes steady on him.
- 8–9s (Shot 2): @Thu goes on to the last words without blinking.
- 9–10s (Shot 2): @Thu finishes and closes her mouth.
- 10–11s (CUT to Shot 3): @Tung stares at the sheet, spreads both hands wide and starts answering fast and high-pitched.
- 11–12s (Shot 3): @Tung keeps talking fast, his eyebrows jumping up, his voice rising.
- 12–13s (Shot 3): @Tung keeps speaking, pointing one finger at the sheet.
- 13–14s (CUT to Shot 4): @Tung finishes and closes his mouth, his spread hands shaking in the air.
- 14–15s (Shot 4): @Thu folds her hands on the table and holds his gaze without a word, the city glittering in the window behind her, both mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.3s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking slowly and softly, unhurried, with a short natural pause between phrases, swallowing his pride): "Anh hiểu. Em cứ xếp, việc gì anh cũng làm, không kêu một câu."
- Turn 2, 4.8–9.8s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, firm and level): "Từ thứ hai, anh xuống công trường ngoài Đông Anh làm đội trưởng, sáu giờ sáng có mặt."
- Turn 3, 10.3–13.9s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking quickly in short lively phrases, every word still clear, outraged, voice jumping high): "Đội trưởng á? Anh làm sếp mười năm nay, giờ em bắt anh đi bê gạch à?"
- Pacing: @Tung speaks slowly and calmly, then @Thu answers slowly and calmly, then @Tung answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a sheet of paper sliding across a glossy table, a sharp exhale, air conditioning humming. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 3 (`canh-21/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A construction company boardroom high in a Hà Nội tower by day: a long glossy table lined with black leather chairs, white architectural models along the wall, floor-to-ceiling windows over the city, crisp daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 28mm wide two-shot across the corner of the table toward the city windows, holding the previous framing.
- Shot 2, 3–6s: 85mm close-up of the woman at the head of the table, locked off.
- Shot 3, 6–10s: 50mm over-the-shoulder shot from behind the woman onto the husband, locked off.
- Shot 4, 10–15s: 40mm medium two-shot across the corner of the table, slow drift.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu sits very still at the head of the table and is already speaking slowly and quietly, her eyes steady on @Tung, the city glittering in the window behind her.
- 1–2s (Shot 1): @Thu keeps speaking, weighing each word, her chin level.
- 2–3s (Shot 1): @Thu keeps talking quietly and taps one fingertip on the glass case of a white architectural model beside her.
- 3–4s (CUT to Shot 2): @Thu keeps speaking, her fingertip resting on the glass case.
- 4–5s (Shot 2): @Thu goes on in the same low voice, her gaze never leaving him.
- 5–6s (Shot 2): @Thu says the last words slowly and closes her mouth.
- 6–7s (CUT to Shot 3): @Tung lowers his head, lets out a long breath and starts answering slowly in a low voice.
- 7–8s (Shot 3): @Tung keeps speaking, his spread hands sinking back to his sides.
- 8–9s (Shot 3): @Tung keeps talking quietly, nodding to himself.
- 9–10s (Shot 3): @Tung finishes and closes his mouth, a pained half-smile on his lips.
- 10–11s (CUT to Shot 4): @Thu adds a dry matter-of-fact remark, ticking the points off on her fingers.
- 11–12s (Shot 4): @Thu keeps talking dryly, folding down a second finger, while @Tung listens with his mouth closed.
- 12–13s (Shot 4): @Thu keeps speaking, folding down a third finger.
- 13–14s (Shot 4): @Thu goes on to the last word and lays her hand flat on the papers.
- 14–15s (Shot 4): @Thu closes her mouth, while @Tung straightens his back, his chin lifting a little, his face turned toward her, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.0s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet, each word weighed): "Thế mà không giữ nổi một cái nhà. Xuống đấy học xây cho chắc đã, rồi hẵng tính chuyện khác."
- Turn 2, 6.5–9.9s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking slowly and softly, unhurried, with a short natural pause between phrases, deflating, accepting): "Được. Anh đi. Anh sẽ học lại từ viên gạch đầu tiên."
- Turn 3, 10.4–14.2s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, dry, matter-of-fact): "Ăn lương công nhật như mọi người. Không xe đưa đón, không thư ký riêng."
- Pacing: @Thu speaks slowly and calmly, then @Tung answers slowly and calmly, then @Thu answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a fingertip tapping on a glass case, a long exhale, the low hum of the city beyond the glass. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 4 (`canh-21/clip-4.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A construction company boardroom high in a Hà Nội tower by day: a long glossy table lined with black leather chairs, white architectural models along the wall, floor-to-ceiling windows over the city, crisp daylight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 40mm medium two-shot across the corner of the table, holding the previous framing.
- Shot 2, 4–6s: 85mm close-up of the husband, his eyes glistening, locked off.
- Shot 3, 6–10s: 50mm over-the-shoulder shot from behind the husband onto the woman rising from the black leather chair, slow tilt up.
- Shot 4, 10–13s: 85mm close-up of the woman, her fingers on the yellow tape, locked off.
- Shot 5, 13–15s: 40mm medium two-shot at the corner of the table, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tung lingers at the corner of the table, fingers opening and closing at his sides, and is already speaking slowly and pleadingly.
- 1–2s (Shot 1): @Tung keeps speaking, his voice catching, while @Thu gathers the papers into a neat stack with her mouth closed.
- 2–3s (Shot 1): @Tung keeps talking, swallowing hard between phrases.
- 3–4s (Shot 1): @Tung keeps speaking, leaning a little toward her across the corner of the table.
- 4–5s (CUT to Shot 2): @Tung keeps talking quietly, his voice dropping almost to a whisper, eyes glistening.
- 5–6s (Shot 2): @Tung keeps asking to the last word, his eyes searching her face.
- 6–7s (CUT to Shot 3): @Tung finishes his question and closes his mouth, waiting, while @Thu rises from the black leather chair and starts answering slowly and gently.
- 7–8s (Shot 3): @Thu keeps speaking softly, her fingers resting on the yellow tailor's measuring tape around her neck.
- 8–9s (Shot 3): @Thu keeps talking gently, her eyes kind but unmoving.
- 9–10s (Shot 3): @Thu keeps speaking, her thumb running along the tiny marks of the tape.
- 10–11s (CUT to Shot 4): @Thu goes on quietly, never looking away from him.
- 11–12s (Shot 4): @Thu keeps talking, her voice soft and final.
- 12–13s (Shot 4): @Thu keeps speaking slowly toward the last words.
- 13–14s (CUT to Shot 5): @Thu finishes the last words and closes her mouth, while @Tung's shoulders sink, his mouth closed.
- 14–15s (Shot 5): @Thu tucks the papers under her arm and walks past @Tung toward the glass door, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.3s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking slowly and softly, unhurried, with a short natural pause between phrases, pleading, voice catching): "Em này. Anh biết mình không có quyền hỏi. Nhưng còn chúng mình, anh còn cơ hội nào nữa không em?"
- Turn 2, 6.8–13.8s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, gentle but final): "Em cầm kim cả đời, em biết. Áo rách thì vá được anh ạ. Lòng người rách rồi, vá khéo mấy cũng còn vết khâu."
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a leather chair sighing as she rises, papers tapped into a stack, soft footsteps on carpet, a glass door swinging shut. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed or hurried delivery, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 1 (`canh-22/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A plain visiting room at a police station by day: pale green walls, a long wooden table with two plastic chairs facing each other, a barred window with soft daylight, a slow ceiling fan.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a creased, crumpled red silk wedding áo dài embroidered with a gold phoenix, bare-headed without the khăn vấn, faded red lipstick, plain plastic slippers.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium shot from beside the barred window of the young woman slumped at the long wooden table, slow push-in.
- Shot 2, 5–11s: 50mm over-the-shoulder shot from behind the young woman onto the tailor, locked off.
- Shot 3, 11–13s: 85mm close-up of the young woman in the creased red áo dài, locked off.
- Shot 4, 13–15s: 40mm medium two-shot across the table in profile, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy sits slumped on a plastic chair at the long wooden table in her creased red wedding áo dài, hair loose, and is already speaking in a flat bitter voice without lifting her eyes.
- 1–2s (Shot 1): @Vy keeps talking bitterly, picking at a loose gold thread on her sleeve.
- 2–3s (Shot 1): @Vy keeps speaking, a crooked smile on her faded red lips.
- 3–4s (Shot 1): @Vy goes on, plucking at the creased silk over her knees.
- 4–5s (Shot 1): @Vy keeps talking to the last words, still not looking up.
- 5–6s (CUT to Shot 2): @Vy closes her mouth, and @Thu, seated opposite, folds her work-roughened hands on the table and starts answering slowly and quietly.
- 6–7s (Shot 2): @Thu keeps speaking in a low direct voice, the yellow tailor's measuring tape around her neck.
- 7–8s (Shot 2): @Thu keeps talking calmly, leaning a little forward over her folded hands.
- 8–9s (Shot 2): @Thu goes on gently, her eyes on @Vy's bowed head.
- 9–10s (Shot 2): @Thu keeps speaking, unhurried, as the ceiling fan turns slowly above.
- 10–11s (Shot 2): @Thu finishes and closes her mouth, waiting.
- 11–12s (CUT to Shot 3): @Vy gives a hollow sneer and starts answering fast without looking up.
- 12–13s (Shot 3): @Vy keeps talking, her fingers stopping on the gold thread.
- 13–14s (CUT to Shot 4): @Vy finishes and closes her mouth, eyes on the tabletop.
- 14–15s (Shot 4): @Thu waits in silence across the table, hands folded, her calm face toward @Vy, while @Vy twists the loose gold thread, both mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking at a natural, even conversational pace, bitter and flat): "Chị đến xem em thảm hại thế nào à? Hay đến đòi lại cái áo cưới em đang mặc?"
- Turn 2, 5.7–11.0s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and direct): "Áo em cứ giữ, chị may rồi thì nó là của em. Chị chỉ muốn hỏi em một câu."
- Turn 3, 11.5–13.8s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, a hollow sneer): "Hỏi đi chị. Ở trong này thì em thừa thời gian."
- Pacing: @Vy speaks at an even everyday pace, then @Thu answers slowly and calmly, then @Vy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a ceiling fan whirring slowly, a plastic chair creaking, a distant metal door clanging somewhere in the station. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 2 (`canh-22/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A plain visiting room at a police station by day: pale green walls, a long wooden table with two plastic chairs facing each other, a barred window with soft daylight, a slow ceiling fan.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a creased, crumpled red silk wedding áo dài embroidered with a gold phoenix, bare-headed without the khăn vấn, faded red lipstick, plain plastic slippers.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 40mm medium two-shot across the table in profile, holding the previous framing.
- Shot 2, 4–10s: 85mm close-up of the young woman, her chin trembling, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the young woman onto the tailor, slow push-in.
- Shot 4, 13–15s: 40mm medium two-shot across the table in profile, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu leans forward a little over the table and is already asking her question in a plain searching voice, while @Vy's eyes slowly rise to meet hers.
- 1–2s (Shot 1): @Thu keeps speaking gently, her folded hands still on the wood.
- 2–3s (Shot 1): @Thu keeps asking quietly, her eyes searching @Vy's face.
- 3–4s (Shot 1): @Thu keeps talking to the last word of the question.
- 4–5s (CUT to Shot 2): @Thu closes her mouth, and @Vy starts answering slowly, her chin trembling.
- 5–6s (Shot 2): @Vy keeps speaking, her eyes shining wet.
- 6–7s (Shot 2): @Vy keeps talking slowly, both hands twisting the creased red silk in her lap.
- 7–8s (Shot 2): @Vy keeps speaking, her voice thinning, a tear gathering on her lashes.
- 8–9s (Shot 2): @Vy goes on in a broken voice as a tear slides down her cheek.
- 9–10s (Shot 2): @Vy finishes and closes her mouth, lips pressed together.
- 10–11s (CUT to Shot 3): @Thu answers slowly and evenly in a low steady voice, her eyes never leaving @Vy's face.
- 11–12s (Shot 3): @Thu keeps speaking, not unkind, her hands folded on the table.
- 12–13s (Shot 3): @Thu keeps talking, her voice level and quiet.
- 13–14s (CUT to Shot 4): @Thu keeps speaking softly toward the last words.
- 14–15s (Shot 4): @Thu finishes and closes her mouth, while @Vy wipes her wet cheek with the back of her wrist, her face toward the tailor. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, plain and searching): "Ba người đàn ông ấy, kể cả anh Tùng, em có thương ai thật lòng không?"
- Turn 2, 4.9–9.7s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking slowly and softly, unhurried, with a short natural pause between phrases, close to tears): "Em chỉ thương tiền thôi. Từ bé em nghèo đến mức đi học phải đi chân đất."
- Turn 3, 10.2–14.1s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, steady, not unkind): "Nghèo thì chị hiểu. Chị cũng từng nghèo, nhưng chị chưa cướp của ai."
- Pacing: @Thu speaks at an even everyday pace, then @Vy answers slowly and calmly, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the ceiling fan whirring, a stifled sniff, the creak of a plastic chair, distant footsteps in a corridor. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 3 (`canh-22/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A plain visiting room at a police station by day: pale green walls, a long wooden table with two plastic chairs facing each other, a barred window with soft daylight, a slow ceiling fan.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a creased, crumpled red silk wedding áo dài embroidered with a gold phoenix, bare-headed without the khăn vấn, faded red lipstick, plain plastic slippers.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 40mm medium two-shot across the table in profile, holding the previous framing.
- Shot 2, 4–9s: 85mm close-up of the tailor across the table, slow push-in.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the tailor onto the young woman, her face crumpling, locked off.
- Shot 4, 13–15s: 35mm medium two-shot from the end of the table, slow arc.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Vy wipes her cheek with the back of her wrist and is already speaking sharply through her tears.
- 1–2s (Shot 1): @Vy keeps talking fast and sharp, her wet eyes narrowed.
- 2–3s (Shot 1): @Vy keeps speaking, flicking one hand toward the door.
- 3–4s (Shot 1): @Vy finishes and closes her mouth, jaw tight, glaring across the table.
- 4–5s (CUT to Shot 2): @Thu starts answering slowly and kindly, her voice softening.
- 5–6s (Shot 2): @Thu keeps speaking, resting one open hand flat on the table between them without reaching across.
- 6–7s (Shot 2): @Thu keeps talking quietly, her eyes warm and steady.
- 7–8s (Shot 2): @Thu keeps speaking, nodding once toward the door as if toward the street outside.
- 8–9s (Shot 2): @Thu goes on gently to the last words.
- 9–10s (CUT to Shot 3): @Thu closes her mouth with a faint warm smile, and @Vy's face crumples as she starts answering fast through sobs.
- 10–11s (Shot 3): @Vy keeps sobbing out the words, both hands pressed to her chest.
- 11–12s (Shot 3): @Vy keeps talking through tears, shaking her head.
- 12–13s (Shot 3): @Vy finishes and closes her mouth, gasping for breath.
- 13–14s (CUT to Shot 4): @Vy bends forward over the table, her loose hair falling around her wet face, mouth closed.
- 14–15s (Shot 4): @Thu sits still and watches her quietly across the table, hands folded, her face calm and tired, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.8s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, snapping through tears): "Giảng đạo đức xong chưa chị? Xong thì về đi, em không cần ai thương hại."
- Turn 2, 4.3–9.3s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, kind and quiet): "Chưa xong. Khi nào ra, nếu muốn học một cái nghề tử tế, em cứ đến tiệm chị."
- Turn 3, 9.8–13.0s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, sobbing, words rushing out): "Sao chị lại tốt với em thế? Em định cướp hết của chị cơ mà!"
- Pacing: @Vy speaks quickly, then @Thu answers slowly and calmly, then @Vy answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ragged sobbing, the ceiling fan whirring, a plastic chair scraping, birds faint outside the barred window. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 4 (`canh-22/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A plain visiting room at a police station by day: pale green walls, a long wooden table with two plastic chairs facing each other, a barred window with soft daylight, a slow ceiling fan.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Vy = Vy, 24, Tùng's glamorous young secretary who is secretly a con artist; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; a creased, crumpled red silk wedding áo dài embroidered with a gold phoenix, bare-headed without the khăn vấn, faded red lipstick, plain plastic slippers.
- Wardrobe: in this shot @Vy wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot from the end of the table, holding the previous framing.
- Shot 2, 5–9s: 85mm close-up of the young woman lifting her wet face, locked off.
- Shot 3, 9–12s: 50mm medium two-shot as the tailor rises beside the table, slow tilt up.
- Shot 4, 12–15s: 40mm over-the-shoulder shot from behind the seated young woman up to the standing tailor, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu is already speaking slowly and tiredly across the table, her hands folded, while @Vy stays bent over the table with her mouth closed.
- 1–2s (Shot 1): @Thu keeps speaking gently, shaking her head a little.
- 2–3s (Shot 1): @Thu keeps talking quietly, her eyes on @Vy's bowed head.
- 3–4s (Shot 1): @Thu goes on, then lets out a slow breath.
- 4–5s (Shot 1): @Thu keeps speaking to the last words.
- 5–6s (CUT to Shot 2): @Thu closes her mouth, and @Vy lifts her wet face and starts asking a quick wary question.
- 6–7s (Shot 2): @Vy keeps asking sharply, her eyes narrowed and searching.
- 7–8s (Shot 2): @Vy keeps talking fast, leaning toward the tailor across the table.
- 8–9s (Shot 2): @Vy finishes and closes her mouth, waiting.
- 9–10s (CUT to Shot 3): @Thu rises slowly from the plastic chair and starts answering in a quiet voice.
- 10–11s (Shot 3): @Thu keeps speaking slowly, smoothing her green apron as she stands beside the table.
- 11–12s (Shot 3): @Thu keeps talking softly, her hand drifting to the yellow tailor's measuring tape around her neck.
- 12–13s (CUT to Shot 4): @Thu keeps speaking, quiet and final, while @Vy looks up at her with her mouth closed, tears dripping onto the creased red silk.
- 13–14s (Shot 4): @Thu finishes the last words and closes her mouth.
- 14–15s (Shot 4): @Thu turns toward the door without looking back, while @Vy bows her head low over the table, her shoulders shaking under the gold phoenix, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, tired and gentle): "Chị không tốt đâu em. Chị làm thế là vì chị thôi, chứ chẳng phải vì em."
- Turn 2, 5.7–8.7s, spoken on camera by @Vy (young woman of 24, high honeyed soprano with a coy lilt that can snap cold and sharp, speaking quickly in short lively phrases, every word still clear, caught off guard, wary): "Vì chị á? Thế chị được cái gì? Chị nói em nghe xem nào."
- Turn 3, 9.2–13.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and final): "Chị không muốn thêm người vợ nào phải ngồi may áo cưới cho chồng mình nữa."
- Pacing: @Thu speaks slowly and calmly, then @Vy answers quickly, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a plastic chair scraping back, the ceiling fan whirring, soft footsteps toward the door, quiet sobbing. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 1 (`canh-23/clip-1.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A busy construction site on the edge of Hà Nội at sunrise: rising concrete pillars, steel scaffolding, a tall yellow tower crane, stacks of red bricks and cement bags, golden dust in the air.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; a yellow hard hat, a sweat-darkened white shirt with the sleeves rolled up, dusty dark work trousers, black rubber boots.
- Wardrobe: in this shot @Tung wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: a few construction workers in hard hats far off on the scaffolding, small and blurred
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the man setting a stack of red bricks down on the pile, slow pan.
- Shot 2, 4–8s: 85mm close-up of his sweating face under the yellow hard hat, locked off.
- Shot 3, 8–11s: 40mm medium shot from a low angle against the rising concrete pillars, slow drift.
- Shot 4, 11–13s: 85mm close-up of his dusty face, locked off.
- Shot 5, 13–15s: 100mm extreme close-up of his blistered palms holding a red brick, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Tung, in a yellow hard hat, sets a stack of red bricks down on the pile, presses a hand to his lower back and is already muttering wryly to himself.
- 1–2s (Shot 1): @Tung keeps muttering under his breath, rubbing his lower back, his white shirt dark with sweat.
- 2–3s (Shot 1): @Tung keeps talking to himself with a wry snort, shaking his head.
- 3–4s (Shot 1): @Tung straightens up, still muttering, and wipes the sweat from his brow with his forearm.
- 4–5s (CUT to Shot 2): @Tung keeps muttering, squinting up at the rising concrete pillars, dust on his cheek.
- 5–6s (Shot 2): @Tung keeps talking quietly to himself, a crooked smile tugging at his mouth.
- 6–7s (Shot 2): @Tung keeps muttering, turning his blistered palms up to look at them.
- 7–8s (Shot 2): @Tung keeps talking to himself, his lips dry.
- 8–9s (CUT to Shot 3): @Tung keeps muttering, his gaze drifting across the site toward the yellow tower crane.
- 9–10s (Shot 3): @Tung goes on under his breath, his voice dropping.
- 10–11s (Shot 3): @Tung keeps talking to himself, his face falling still.
- 11–12s (CUT to Shot 4): @Tung keeps murmuring, a bitter little laugh escaping him.
- 12–13s (Shot 4): @Tung says the last words softly and closes his mouth.
- 13–14s (CUT to Shot 5): @Tung looks down at the red brick dust on his blistered palms, mouth closed.
- 14–15s (Shot 5): @Tung picks up the next red brick and weighs it in one hand, the crane motor whining in the distance. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–12.9s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, wry, muttering to himself), in Vietnamese with exact lip-sync, said exactly once: "Ôi, cái lưng. Ngày trước ngồi phòng máy lạnh, ký một chữ là xong cả toà nhà. Giờ mới biết một viên gạch nặng bao nhiêu. Bốn trăm viên một ngày, tay phồng rộp hết. Ấy thế mà cái nhà của chính mình thì lại để đổ. Đáng đời mày." (no subtitles)
- @Tung starts talking within the first second; whenever @Tung speaks, the face and lips are clearly visible in that shot; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: bricks clunking onto a pile, a distant cement mixer churning, the tower crane motor whining, heavy breathing. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, rushed delivery, slow drawn-out delivery or long pauses inside a sentence, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 2 (`canh-23/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A busy construction site on the edge of Hà Nội at sunrise: rising concrete pillars, steel scaffolding, a tall yellow tower crane, stacks of red bricks and cement bags, golden dust in the air.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; a yellow hard hat, a sweat-darkened white shirt with the sleeves rolled up, dusty dark work trousers, black rubber boots.
- Wardrobe: in this shot @Tung wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium tracking shot of the girl running up the muddy path toward the brick pile.
- Shot 2, 5–9s: 85mm close-up of the father crouching to her height, locked off.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the father onto the girl, locked off.
- Shot 4, 13–15s: 40mm medium two-shot at the girl's eye level, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Na runs up the muddy path in her school uniform, holding a stainless steel tiffin lunch box in both hands, and is already speaking fast and bright.
- 1–2s (Shot 1): @Na keeps talking breathlessly as she runs, her red hair ties bouncing.
- 2–3s (Shot 1): @Na keeps speaking, lifting the tiffin box high as she reaches the brick pile.
- 3–4s (Shot 1): @Na goes on proudly, hugging the box to her chest.
- 4–5s (Shot 1): @Na finishes and closes her mouth, beaming, the tiffin box held out.
- 5–6s (CUT to Shot 2): @Tung, in his yellow hard hat, crouches down to her height, takes the tiffin box carefully in his dusty hands and starts answering slowly, his voice thick.
- 6–7s (Shot 2): @Tung keeps speaking softly, blinking, the box held close.
- 7–8s (Shot 2): @Tung keeps talking, his voice catching.
- 8–9s (Shot 2): @Tung goes on with a small wet laugh, shaking his head.
- 9–10s (CUT to Shot 3): @Tung closes his mouth, and @Na nods hard and starts answering fast, wagging a finger like a little teacher.
- 10–11s (Shot 3): @Na keeps talking quickly, still wagging her finger, while @Tung listens with his mouth closed.
- 11–12s (Shot 3): @Na keeps speaking proudly, her chin up.
- 12–13s (Shot 3): @Na keeps talking, pointing at the tiffin box.
- 13–14s (CUT to Shot 4): @Na finishes and closes her mouth, beaming.
- 14–15s (Shot 4): @Tung holds the tiffin box against his chest, blinking hard, while @Na grins up at him, her face bright, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, bright and breathless): "Bố ơi, mẹ gửi cơm cho bố này! Có cả trứng rán, con ôm khư khư suốt đường đấy!"
- Turn 2, 5.1–9.3s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking slowly and softly, unhurried, with a short natural pause between phrases, moved, voice thick): "Mẹ con vẫn nhớ bố thích trứng rán à? Bố cứ tưởng mẹ quên rồi."
- Turn 3, 9.8–13.1s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, a proud little messenger): "Nhớ chứ! Mẹ còn dặn bố phải ăn hết, không được bỏ mứa hạt nào."
- Pacing: @Na speaks quickly, then @Tung answers slowly and calmly, then @Na answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: small running footsteps on gravel, the clink of a tiffin box, the distant crane motor, morning birds. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 3 (`canh-23/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A busy construction site on the edge of Hà Nội at sunrise: rising concrete pillars, steel scaffolding, a tall yellow tower crane, stacks of red bricks and cement bags, golden dust in the air.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; a yellow hard hat, a sweat-darkened white shirt with the sleeves rolled up, dusty dark work trousers, black rubber boots.
- Wardrobe: in this shot @Tung wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot at the girl's eye level, holding the previous framing.
- Shot 2, 5–10s: 85mm close-up of the father, steam curling from the open tiffin box, slow push-in.
- Shot 3, 10–12s: 50mm over-the-shoulder shot from behind the father onto the girl, locked off.
- Shot 4, 12–15s: 40mm medium two-shot at eye level as their little fingers hook together, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Na leans in beside @Tung and is already speaking in a clear earnest voice, swinging her arms, while @Tung lifts the lid of the stainless steel tiffin lunch box with his mouth closed.
- 1–2s (Shot 1): @Na keeps talking proudly as steam curls up from rice and a golden fried egg.
- 2–3s (Shot 1): @Na keeps speaking, pointing at the egg.
- 3–4s (Shot 1): @Na keeps talking earnestly, rising on her toes.
- 4–5s (Shot 1): @Na finishes and closes her mouth, looking up at him.
- 5–6s (CUT to Shot 2): @Tung's eyes redden as he starts answering slowly.
- 6–7s (Shot 2): @Tung keeps speaking slowly, his voice catching.
- 7–8s (Shot 2): @Tung keeps speaking tearfully, a slow smile breaking through.
- 8–9s (Shot 2): @Tung keeps talking, nodding firmly as he makes the promise.
- 9–10s (Shot 2): @Tung finishes, closes his mouth and wipes his eyes with the back of his wrist.
- 10–11s (CUT to Shot 3): @Na holds up her little finger and starts chirping fast with a delighted grin.
- 11–12s (Shot 3): @Na keeps talking, waggling her raised little finger at @Tung.
- 12–13s (CUT to Shot 4): @Na keeps speaking, eyebrows raised in mock warning, as @Tung reaches out his dusty little finger.
- 13–14s (Shot 4): @Na finishes and closes her mouth as @Tung hooks his little finger around hers.
- 14–15s (Shot 4): The two hooked fingers give a little shake between them in the golden light, @Na and @Tung smiling and silent, the yellow tower crane blurred far behind. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking at a natural, even conversational pace, earnest and proud): "Mẹ bảo bố làm đội trưởng giỏi thì chủ nhật được đến xem con múa văn nghệ."
- Turn 2, 5.4–9.6s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking slowly and softly, unhurried, with a short natural pause between phrases, tearful, a promise): "Bố sẽ đến. Lần này bố sẽ đến sớm nhất, ngồi ngay hàng ghế đầu."
- Turn 3, 10.1–13.7s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, delighted, holding up a pinky): "Bố hứa rồi đấy nhé! Ngoắc tay đi bố, không được quên như mọi lần đâu!"
- Pacing: @Na speaks at an even everyday pace, then @Tung answers slowly and calmly, then @Na answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a tiffin lid clinking, steam hissing softly, the distant crane, a quiet sniff. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 4 (`canh-23/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
A busy construction site on the edge of Hà Nội at sunrise: rising concrete pillars, steel scaffolding, a tall yellow tower crane, stacks of red bricks and cement bags, golden dust in the air.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; a yellow hard hat, a sweat-darkened white shirt with the sleeves rolled up, dusty dark work trousers, black rubber boots.
- Wardrobe: in this shot @Tung wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium two-shot by the cement bags at the edge of the site, locked off.
- Shot 2, 6–10s: 85mm close-up of the son under the yellow hard hat, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the son onto the old mother, locked off.
- Shot 4, 13–15s: 40mm medium two-shot by the cement bags, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan stands by the cement bags on her carved bamboo walking stick, looks @Tung up and down and is already speaking in a dry teasing voice.
- 1–2s (Shot 1): @BaNhan keeps talking dryly, nodding at his sunburned face, while @Tung wipes his sweaty face with an old towel, mouth closed.
- 2–3s (Shot 1): @BaNhan keeps speaking, pointing the tip of her stick at his calloused hands.
- 3–4s (Shot 1): @BaNhan keeps talking, eyeing his sweat-soaked shirt.
- 4–5s (Shot 1): @BaNhan goes on, a dry glint in her eyes.
- 5–6s (Shot 1): @BaNhan finishes the last words and closes her mouth, lips pursed.
- 6–7s (CUT to Shot 2): @Tung breaks into a tired laugh and starts answering her sheepishly.
- 7–8s (Shot 2): @Tung keeps speaking, rubbing the back of his sunburned neck.
- 8–9s (Shot 2): @Tung keeps talking with a tired grin under the yellow hard hat.
- 9–10s (Shot 2): @Tung finishes and closes his mouth, still grinning.
- 10–11s (CUT to Shot 3): @BaNhan answers fast with a perfectly straight face.
- 11–12s (Shot 3): @BaNhan keeps talking deadpan, chin lifted.
- 12–13s (Shot 3): @BaNhan keeps speaking quickly, flicking a glance at his dusty work clothes.
- 13–14s (CUT to Shot 4): @BaNhan finishes and closes her mouth, tapping her stick on the dusty ground.
- 14–15s (Shot 4): @BaNhan purses her lips to hide a smile, while @Tung grins under the yellow hard hat, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.0s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, dry and teasing): "Nhìn con xem, mặt đen nhẻm, tay chai sạn, áo ướt đẫm mồ hôi. Giờ trông con mới giống cây tùng."
- Turn 2, 6.5–10.0s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, laughing, a little sheepish): "Mẹ khen con hay mẹ chê con đấy ạ? Nghe cứ như mắng ấy."
- Turn 3, 10.5–13.2s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking quickly in short lively phrases, every word still clear, quick deadpan): "Khen. Chê thì mẹ để dành cho lúc con mặc com-lê."
- Pacing: @BaNhan speaks at an even everyday pace, then @Tung answers at an even everyday pace, then @BaNhan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the tower crane groaning as it turns, a towel flapping, a short tired laugh, a bamboo stick tapping on dry ground. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 1 (`canh-24/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; a new plum-purple silk áo dài with tiny gold embroidered flowers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- Wardrobe: in this shot @BaNhan wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the old mother at the foot of the stairs strung with tiny lights, slow arc.
- Shot 2, 5–10s: 85mm close-up of the wife laughing, locked off.
- Shot 3, 10–13s: 40mm medium two-shot at the foot of the stairs, locked off.
- Shot 4, 13–15s: 28mm wide shot of the dining area dressed for the birthday, both women by the stairs, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan comes down the last tiled stairs in a new plum-purple silk áo dài, turns slowly on the spot with her bamboo walking stick and is already speaking fast and gleeful.
- 1–2s (Shot 1): @BaNhan keeps talking, holding out one sleeve to show off the tiny gold flowers.
- 2–3s (Shot 1): @BaNhan keeps speaking gleefully, patting the silk at her chest.
- 3–4s (Shot 1): @BaNhan goes on, turning to show off the back of the áo dài.
- 4–5s (Shot 1): @BaNhan keeps talking with a cheeky wink.
- 5–6s (CUT to Shot 2): @BaNhan finishes and closes her mouth, and @Thu, coming out of the kitchen wiping her hands on her green apron, laughs and starts answering warmly.
- 6–7s (Shot 2): @Thu keeps speaking warmly, stepping closer to admire the tiny gold embroidered flowers on the sleeve.
- 7–8s (Shot 2): @Thu keeps talking, her eyes crinkling with amusement.
- 8–9s (Shot 2): @Thu keeps speaking, laughing softly.
- 9–10s (Shot 2): @Thu finishes and closes her mouth, still smiling.
- 10–11s (CUT to Shot 3): @BaNhan lifts her chin and answers fast with mock seriousness.
- 11–12s (Shot 3): @BaNhan keeps talking, wagging one finger, while @Thu listens with her mouth closed.
- 12–13s (Shot 3): @BaNhan keeps speaking, nose in the air.
- 13–14s (CUT to Shot 4): @BaNhan finishes and closes her mouth, then twirls her bamboo walking stick like a dancer.
- 14–15s (Shot 4): @Thu shakes her head with a silent laugh, mouth closed, while @BaNhan poses in the purple silk, the birthday cake waiting on the round table. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.1s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking quickly in short lively phrases, every word still clear, giddy and delighted): "Bảy mươi mốt tuổi mới có cái áo dài con dâu may đẹp thế này. Mẹ phải đi bước nữa thôi!"
- Turn 2, 5.6–9.6s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, laughing warmly): "Mẹ cứ thong thả. Mặc thế này ra phố, các cụ ông xếp hàng dài đấy."
- Turn 3, 10.1–13.7s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking quickly in short lively phrases, every word still clear, mock-serious, chin up): "Thế thì mẹ chọn ông nào nấu cơm ngon, chứ đẹp trai thì mẹ chán rồi."
- Pacing: @BaNhan speaks quickly, then @Thu answers at an even everyday pace, then @BaNhan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: slippers shuffling on tiled stairs, silk rustling, warm laughter, a pot simmering in the kitchen. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 2 (`canh-24/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium two-shot at the foot of the steep tiled staircase strung with tiny lights, slow push-in.
- Shot 2, 5–9s: 85mm close-up of the mother crouching to her daughter's height, slow tilt down.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the mother onto the girl, locked off.
- Shot 4, 13–15s: 40mm medium two-shot at the foot of the stairs, slow pan toward the front door.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Na hurries down the stairs, catches @Thu, who is passing with a plate of peaches, by the hem of her green apron, and is already speaking fast and pleading with wide eyes.
- 1–2s (Shot 1): @Na keeps talking quickly, bouncing on the bottom step, while @Thu listens with her mouth closed.
- 2–3s (Shot 1): @Na keeps speaking, pressing her palms together under her chin.
- 3–4s (Shot 1): @Na goes on, peeking up at her mother's face.
- 4–5s (Shot 1): @Na finishes and closes her mouth, eyes wide, and @Thu sets the plate on the step and starts answering slowly and softly.
- 5–6s (CUT to Shot 2): @Thu crouches down to @Na's height and keeps speaking gently.
- 6–7s (Shot 2): @Thu keeps talking softly, tucking a loose strand of hair behind her daughter's ear.
- 7–8s (Shot 2): @Thu keeps speaking, her eyes warm, nodding toward the birthday table.
- 8–9s (Shot 2): @Thu finishes and closes her mouth with a smile.
- 9–10s (CUT to Shot 3): @Na beams and starts chirping a quick reply.
- 10–11s (Shot 3): @Na keeps talking fast, picking up the paper birthday crown from the step.
- 11–12s (Shot 3): @Na keeps speaking, plonking the paper crown on her own head.
- 12–13s (Shot 3): @Na keeps talking, already edging toward the front door.
- 13–14s (CUT to Shot 4): @Na finishes, closes her mouth and runs off toward the front door.
- 14–15s (Shot 4): @Thu straightens up and smiles after her in silence, the plate of peaches on the step. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, pleading and excited): "Mẹ ơi, con lỡ mời bố đến thổi nến với bà rồi. Mẹ đừng giận con, mẹ nhé!"
- Turn 2, 4.9–8.8s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft and reassuring): "Giận gì. Hôm nay là ngày của bà, ai thương bà thì cứ đến."
- Turn 3, 9.3–13.1s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, already running off): "Thế con ra đầu ngõ đợi bố nhé! Bố lâu rồi không về, chắc quên đường mất."
- Pacing: @Na speaks quickly, then @Thu answers slowly and calmly, then @Na answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: small feet pattering on tiled stairs, a plate set down on tile, a soft laugh, the kitchen fan whirring. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 3 (`canh-24/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; a new plum-purple silk áo dài with tiny gold embroidered flowers, cloth slippers, carved bamboo walking stick.
- Wardrobe: in this shot @BaNhan wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the old mother peering toward the open front door, locked off.
- Shot 2, 5–10s: 85mm close-up of the man on the threshold holding a cake box, slow push-in.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the man onto the old mother, locked off.
- Shot 4, 13–15s: 40mm medium two-shot at the front door, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan in her purple áo dài peers toward the open front door and is already speaking in a slow mock-stern voice, leaning on her stick.
- 1–2s (Shot 1): @BaNhan keeps speaking, squinting with exaggerated suspicion.
- 2–3s (Shot 1): @BaNhan keeps talking slowly, waving her stick at the doorway.
- 3–4s (Shot 1): @BaNhan goes on, eyebrows raised high.
- 4–5s (Shot 1): @BaNhan finishes and closes her mouth, waiting.
- 5–6s (CUT to Shot 2): @Tung, standing on the threshold in his charcoal suit with his face tanned dark from the site and a cake box in both arms, starts answering shyly.
- 6–7s (Shot 2): @Tung keeps speaking, a boyish smile spreading.
- 7–8s (Shot 2): @Tung keeps talking and lifts the cake box toward her like a schoolboy with a prize.
- 8–9s (Shot 2): @Tung keeps speaking proudly, his ears going pink.
- 9–10s (Shot 2): @Tung finishes and closes his mouth, still holding the box out.
- 10–11s (CUT to Shot 3): @BaNhan answers in a dry teasing voice, tapping the box lid with one finger.
- 11–12s (Shot 3): @BaNhan keeps talking, her eyes twinkling.
- 12–13s (Shot 3): @BaNhan keeps speaking, beckoning him inside with her stick.
- 13–14s (CUT to Shot 4): @BaNhan finishes, closes her mouth and takes the cake box from his hands.
- 14–15s (Shot 4): @Tung ducks his head with a sheepish grin and steps over the threshold, mouth closed, while @BaNhan holds the cake box to her chest. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking slowly and softly, unhurried, with a short natural pause between phrases, mock-stern, peering): "Ơ kìa, khách nào đến muộn thế này? Sao cứ đứng mãi ngoài cửa thế?"
- Turn 2, 5.3–9.6s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, shy, almost boyish): "Con chúc mẹ sống lâu trăm tuổi. Bánh này con mua bằng lương đội trưởng đấy ạ."
- Turn 3, 10.1–13.8s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, teasing, eyes twinkling): "Tiền mồ hôi nên bánh ngọt hơn hẳn mọi năm đấy. Vào đi con."
- Pacing: @BaNhan speaks slowly and calmly, then @Tung answers at an even everyday pace, then @BaNhan answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a motorbike puttering past in the alley, a paper cake box rustling, a soft chuckle. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 4 (`canh-24/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
Evening inside the family's narrow three-storey tube house in an old-quarter alley: a ground-floor dining area with a round wooden table set with rice bowls and dishes, low wooden stools, a small kitchen with a gas stove behind, a steep tiled staircase, a family altar shelf with incense, warm tungsten light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, a yellow tailor's measuring tape around her neck, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the wife lighting the candles on the birthday cake, locked off.
- Shot 2, 5–10s: 85mm close-up of the husband at the edge of the table, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the husband onto the wife across the cake, locked off.
- Shot 4, 13–15s: 40mm medium two-shot across the birthday cake, slow tilt up.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu lights a match, touches it to the first thin candle on the cream birthday cake and is already speaking in a practical, even voice.
- 1–2s (Shot 1): @Thu keeps talking, lighting the candles one by one.
- 2–3s (Shot 1): @Thu keeps speaking, nodding toward an empty chair at the round table.
- 3–4s (Shot 1): @Thu goes on, shaking out the match and lighting another.
- 4–5s (Shot 1): @Thu finishes and closes her mouth, the flame creeping down the match.
- 5–6s (CUT to Shot 2): @Tung, standing at the edge of the table with his hands folded, starts answering quietly with his eyes lowered.
- 6–7s (Shot 2): @Tung keeps speaking humbly, his voice thick.
- 7–8s (Shot 2): @Tung keeps talking, glancing at the warm room around him.
- 8–9s (Shot 2): @Tung goes on, his eyes lifting to her for a moment.
- 9–10s (Shot 2): @Tung finishes and closes his mouth, looking down again.
- 10–11s (CUT to Shot 3): @Thu answers slowly and calmly, looking straight at @Tung across the cake.
- 11–12s (Shot 3): @Thu keeps speaking evenly, the candle flames trembling between them.
- 12–13s (Shot 3): @Thu keeps talking, kind but clear, while @Tung listens with his mouth closed.
- 13–14s (CUT to Shot 4): @Thu keeps speaking, holding his gaze to the last word.
- 14–15s (Shot 4): @Thu finishes and closes her mouth and turns toward the staircase, while @Tung nods slowly a respectful step back from the table. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, practical, lighting candles): "Ghế của anh cạnh cái Na, con nó để phần từ chiều, ai hỏi cũng không nhường."
- Turn 2, 5.2–9.7s, spoken on camera by @Tung (man of 37, deep heavy baritone, clipped and self-important, speaking at a natural, even conversational pace, humble and grateful): "Cảm ơn em cho anh về ăn bữa cơm này. Anh cứ sợ em không cho anh vào."
- Turn 3, 10.2–14.1s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, calm and kind, a clear line): "Anh về vì mẹ với con. Còn bữa cơm, em nấu cho người nhà."
- Pacing: @Thu speaks at an even everyday pace, then @Tung answers at an even everyday pace, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a match flaring, candles catching with a soft hiss, a pot lid rattling in the kitchen, the alley quiet outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 1 (`canh-25/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
One year later at dawn, Thu's áo dài tailor shop now spread over two floors on the old-quarter silk street: new wooden shelves of jewel-toned silk, three sewing machines, dress forms in finished áo dài by the window, a wide fitting mirror, a small brass bell above the glass door, warm morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; an elegant ivory silk áo dài of her own design, a yellow tailor's measuring tape around her neck, low beige sandals.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- Wardrobe: in this shot @Thu wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the old mother on the wooden staircase, the tall new silk shelves behind her, slow pan.
- Shot 2, 4–9s: 85mm close-up of the woman in ivory silk, locked off.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the woman onto the old mother, locked off.
- Shot 4, 13–15s: 40mm medium two-shot by the cutting table at the foot of the stairs, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan comes down the wooden staircase with her bamboo walking stick, waving it proudly at the full shelves of silk, and is already speaking fast and bright.
- 1–2s (Shot 1): @BaNhan keeps talking proudly as she reaches the bottom step, pointing her stick up toward the second floor.
- 2–3s (Shot 1): @BaNhan keeps speaking, her wrinkled face beaming.
- 3–4s (Shot 1): @BaNhan goes on, gesturing at the three sewing machines in a row.
- 4–5s (CUT to Shot 2): @BaNhan finishes and closes her mouth, and @Thu, in an elegant ivory silk áo dài, steps out from between the tall shelves with a fresh bolt of silk in her arms and starts answering slowly and warmly.
- 5–6s (Shot 2): @Thu keeps speaking warmly, her hand resting on the yellow tailor's measuring tape around her neck.
- 6–7s (Shot 2): @Thu keeps talking softly, her eyes shining.
- 7–8s (Shot 2): @Thu keeps speaking, a grateful smile at the corner of her mouth.
- 8–9s (Shot 2): @Thu goes on to the last words, looking at her mother-in-law.
- 9–10s (CUT to Shot 3): @Thu closes her mouth, and @BaNhan flaps a hand and starts answering fast, brushing it all off.
- 10–11s (Shot 3): @BaNhan keeps talking briskly, waving her stick toward the glass door.
- 11–12s (Shot 3): @BaNhan keeps speaking, shooing @Thu toward the door with one hand.
- 12–13s (Shot 3): @BaNhan keeps talking, peering out at the street through the glass.
- 13–14s (CUT to Shot 4): @BaNhan finishes and closes her mouth, patting the edge of the cutting table twice.
- 14–15s (Shot 4): @Thu smiles and sets the bolt of silk on the cutting table, while @BaNhan settles onto a stool beside it, beaming, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking quickly in short lively phrases, every word still clear, proud, showing off): "Mới một năm mà tiệm lên hai tầng, khách đặt may xếp lịch đến tận Tết rồi đấy."
- Turn 2, 4.9–9.1s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, warm and grateful): "Nhờ mẹ giữ cho con một đường lui, con mới dám bước tiếp, mẹ ạ."
- Turn 3, 9.6–13.4s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking quickly in short lively phrases, every word still clear, brushing off the sentiment): "Thôi, khen nhau đủ rồi, mở cửa đi con, kẻo khách mở hàng lại sang tiệm khác!"
- Pacing: @BaNhan speaks quickly, then @Thu answers slowly and calmly, then @BaNhan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the brass door bell tinkling faintly in a draft, slippers on wooden stairs, silk rustling, the old quarter waking up outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 2 (`canh-25/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
One year later at dawn, Thu's áo dài tailor shop now spread over two floors on the old-quarter silk street: new wooden shelves of jewel-toned silk, three sewing machines, dress forms in finished áo dài by the window, a wide fitting mirror, a small brass bell above the glass door, warm morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaNhan = Bà Nhàn, 70, Tùng's sharp-witted mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; an elegant ivory silk áo dài of her own design, a yellow tailor's measuring tape around her neck, low beige sandals.
- Wardrobe: in this shot @Thu wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot by the cutting table, holding the previous framing.
- Shot 2, 5–11s: 85mm close-up of the woman in ivory silk, locked off.
- Shot 3, 11–13s: 50mm over-the-shoulder shot from behind the woman onto the old mother on her stool, locked off.
- Shot 4, 13–15s: 40mm medium two-shot at the cutting table, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @BaNhan sits on a stool by the cutting table, unfolds a newspaper with no readable writing at arm's length and is already speaking in a smug gossipy voice, while @Thu stands beside her with her mouth closed.
- 1–2s (Shot 1): @BaNhan keeps talking, peering over the top of the page, while @Thu threads a needle.
- 2–3s (Shot 1): @BaNhan keeps speaking with relish, tapping the newspaper with one bony finger.
- 3–4s (Shot 1): @BaNhan keeps talking, her voice rising with satisfaction.
- 4–5s (Shot 1): @BaNhan goes on with a triumphant nod.
- 5–6s (CUT to Shot 2): @BaNhan closes her mouth, and @Thu glances toward the staircase and starts answering slowly in a hushed voice, lowering one hand in a gentle hushing gesture.
- 6–7s (Shot 2): @Thu keeps speaking softly, one finger raised toward the second floor.
- 7–8s (Shot 2): @Thu keeps whispering gently, her eyes on the stairs.
- 8–9s (Shot 2): @Thu keeps speaking in a hushed voice.
- 9–10s (Shot 2): @Thu goes on softly, pointing up at the ceiling.
- 10–11s (Shot 2): @Thu finishes the warning and closes her mouth.
- 11–12s (CUT to Shot 3): @BaNhan answers in a quick sheepish whisper, folding the newspaper in half.
- 12–13s (Shot 3): @BaNhan keeps whispering sheepishly, pressing the folded paper flat on her knee.
- 13–14s (CUT to Shot 4): @BaNhan finishes and closes her mouth, tucking the folded newspaper under her stool with a little shrug.
- 14–15s (Shot 4): @BaNhan folds her hands on her stick and looks innocently at the ceiling, while @Thu draws the thread through the ivory silk with a smile, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking at a natural, even conversational pace, smug and gossipy): "Báo đăng hai đứa lừa đảo ấy lĩnh án rồi đây này. Đấy, cái kết cho tiểu tam!"
- Turn 2, 5.7–10.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, hushed, a gentle warning): "Mẹ đọc khẽ thôi, cái Na nghe thấy lại hỏi đấy. Con bé đang soạn cặp trên gác."
- Turn 3, 11.2–13.7s, spoken on camera by @BaNhan (old woman of 70, thin raspy voice with a slight tremble and dry wit, drawn-out old Hà Nội vowels, speaking quickly in short lively phrases, every word still clear, sheepish whisper): "Ừ nhỉ. Mẹ gấp lại đây, mẹ chưa nói gì nhé."
- Pacing: @BaNhan speaks at an even everyday pace, then @Thu answers slowly and calmly, then @BaNhan answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: newspaper rustling, a needle and thread whispering through silk, a stool creaking, a sewing machine idling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 3 (`canh-25/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
One year later at dawn, Thu's áo dài tailor shop now spread over two floors on the old-quarter silk street: new wooden shelves of jewel-toned silk, three sewing machines, dress forms in finished áo dài by the window, a wide fitting mirror, a small brass bell above the glass door, warm morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; an elegant ivory silk áo dài of her own design, a yellow tailor's measuring tape around her neck, low beige sandals.
- Wardrobe: in this shot @Thu wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium two-shot at the foot of the wooden staircase in the morning light, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the kneeling mother, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the mother onto the girl, locked off.
- Shot 4, 13–15s: 40mm medium two-shot at the girl's eye level in profile, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Na comes down the last wooden stairs in her school uniform, stops in front of @Thu, who kneels to straighten the red scarf at her neck, and is already asking in a curious earnest voice, head tilted.
- 1–2s (Shot 1): @Na keeps asking, eyes wide, while @Thu's fingers work the knot, mouth closed.
- 2–3s (Shot 1): @Na keeps speaking earnestly, twisting one pigtail around her finger.
- 3–4s (Shot 1): @Na goes on, pointing back up the stairs.
- 4–5s (Shot 1): @Na keeps talking, lowering her voice as if sharing a secret.
- 5–6s (CUT to Shot 2): @Na finishes and closes her mouth, and @Thu finishes knotting the red scarf and starts answering slowly with a gentle smile.
- 6–7s (Shot 2): @Thu keeps speaking softly, amused, looking into her daughter's eyes.
- 7–8s (Shot 2): @Thu keeps talking gently, her eyes crinkling.
- 8–9s (Shot 2): @Thu keeps speaking, with a tiny nod.
- 9–10s (Shot 2): @Thu finishes, smiling, and closes her mouth.
- 10–11s (CUT to Shot 3): @Na scrunches up her nose and starts protesting fast, pointing at the shelves of silk.
- 11–12s (Shot 3): @Na keeps talking fast, frowning on the shop's behalf, while @Thu listens with her mouth closed.
- 12–13s (Shot 3): @Na keeps asking, arms folded.
- 13–14s (CUT to Shot 4): @Na finishes and closes her mouth, eyebrows knitted.
- 14–15s (Shot 4): @Thu, still kneeling, smiles at her daughter and smooths her pigtails in silence, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking at a natural, even conversational pace, curious and wide-eyed): "Mẹ ơi, tiểu tam là gì ạ? Có phải là mẹ hai không? Con nghe bà đọc to lắm."
- Turn 2, 5.9–9.6s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, smiling, gently amused): "Tiểu tam là người đi đặt may áo cưới nhầm tiệm, con ạ."
- Turn 3, 10.1–13.4s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, indignant on the shop's behalf): "Ơ, nhưng tiệm mình may đẹp nhất phố mà mẹ! Sao lại nhầm được ạ?"
- Pacing: @Na speaks at an even everyday pace, then @Thu answers slowly and calmly, then @Na answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: small shoes on wooden stairs, a backpack zip, the brass bell tinkling faintly, motorbikes waking up in the street. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 4 (`canh-25/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action Vietnamese family drama with a sharp comic bite, set in Hà Nội today; warm natural grade with jewel-toned silks glowing in a tailor shop, muted old-quarter ochres, glossy cold tones for the wealthy world, golden banquet light, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.

[LOCATION]
One year later at dawn, Thu's áo dài tailor shop now spread over two floors on the old-quarter silk street: new wooden shelves of jewel-toned silk, three sewing machines, dress forms in finished áo dài by the window, a wide fitting mirror, a small brass bell above the glass door, warm morning light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, calm and quietly brilliant wife who runs a small áo dài tailor shop in the old quarter; slim, lightly sun-tanned, long black hair in a low loose bun, gentle watchful dark eyes, no makeup, work-roughened hands; an elegant ivory silk áo dài of her own design, a yellow tailor's measuring tape around her neck, low beige sandals.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- Wardrobe: in this shot @Thu wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot at the girl's eye level in profile, holding the previous framing.
- Shot 2, 5–9s: 85mm close-up of the girl bouncing on her toes, locked off.
- Shot 3, 9–12s: 50mm over-the-shoulder shot from behind the girl onto the kneeling mother, slow push-in.
- Shot 4, 12–15s: 28mm wide two-shot of mother and daughter by the wide fitting mirror, the glass door glowing beyond, slow pull-back.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Thu, still kneeling, is already speaking in an amused voice, while @Na runs a finger along the yellow tailor's measuring tape around @Thu's neck, mouth closed.
- 1–2s (Shot 1): @Thu keeps speaking playfully, letting @Na study the tiny marks on the tape.
- 2–3s (Shot 1): @Thu keeps talking, tapping the tape with one fingertip.
- 3–4s (Shot 1): @Thu goes on with a conspiratorial smile.
- 4–5s (Shot 1): @Thu finishes and closes her mouth with a smile.
- 5–6s (CUT to Shot 2): @Na looks up at @Thu and starts asking fast and eager, bouncing on her toes.
- 6–7s (Shot 2): @Na keeps talking quickly, pointing at her own shoulders and waist.
- 7–8s (Shot 2): @Na keeps asking, then lays a small hand over her heart.
- 8–9s (Shot 2): @Na finishes the question and closes her mouth, eyes wide.
- 9–10s (CUT to Shot 3): @Thu answers slowly and softly, lifting the yellow tailor's measuring tape from her own neck.
- 10–11s (Shot 3): @Thu keeps speaking tenderly, holding the tape between her hands.
- 11–12s (Shot 3): @Thu keeps talking softly and surely, while @Na listens with her mouth closed.
- 12–13s (CUT to Shot 4): @Thu keeps speaking, draping the yellow tape loosely over @Na's shoulders like a scarf.
- 13–14s (Shot 4): @Thu says the last words and closes her mouth, then rises and takes @Na's hand.
- 14–15s (Shot 4): @Thu and @Na stand hand in hand, looking out through the glass door at the old-quarter street glowing in the morning sun, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in Vietnamese with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking at a natural, even conversational pace, amused, playing along): "Vì khách nào mẹ cũng đo rất kỹ mà. Chỗ nào khách giấu, thước của mẹ cũng thấy."
- Turn 2, 5.4–9.0s, spoken on camera by @Na (girl of 9, high clear child's voice, bright and earnest, speaking quickly in short lively phrases, every word still clear, eager, bouncing on her toes): "Vai, eo mẹ đều đo được. Thế lòng người thì mẹ có đo được không ạ?"
- Turn 3, 9.5–13.7s, spoken on camera by @Thu (woman of 34, soft low mezzo, warm and very steady, never raises her voice, speaking slowly and softly, unhurried, with a short natural pause between phrases, soft, certain and tender): "Đo được con ạ. Người thật lòng thì số đo không bao giờ thay đổi."
- Pacing: @Thu speaks at an even everyday pace, then @Na answers quickly, then @Thu answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and sounds clearly different from the other speaker in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soft zip of a measuring tape, the brass bell tinkling as a breeze stirs the door, distant motorbikes and birdsong in the old quarter. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, Southern or Central Vietnamese accents.
```
