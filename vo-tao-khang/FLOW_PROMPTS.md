# Vợ Tào Khang — Bộ 150 Prompt Google Flow Omni (25 Cảnh × 6 Clips × 10s)

- **Giọng Người Dẫn Chuyện (cố định cả 150 clip):** Vietnamese woman about 50, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm low alto with a slight husk, fast fluent heartfelt family-drama storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; đọc nhanh liên thanh như oan-thai-doi-me, ~4.0 âm tiết/giây, liền một hơi, không ngắt giữa câu.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 150 clips × 10s — 0 clip VO + 150 clip thoại; lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 51 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 99 clip ảnh nhân vật (Ingredients), 0 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** clip VO được tăng tốc giọng thêm 1.18x khi tải về (`FLOWKIT_VOICE_TEMPO` mặc định 1.18, đặt 1.0 để tắt), giữ nguyên khung hình 10s; clip lip-sync không bao giờ bị tăng tốc để khớp khẩu hình.
- **Màu phim & ánh sáng:** Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py vo-tao-khang` sinh lại toàn bộ clip, README, kịch bản.

---

## Cảnh 01 - Clip 1 (`canh-01/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 24mm aerial descending glide from the rooftops down to an upper-floor window; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: High aerial view over the dark tiled roofs of the old quarter before dawn, thin mist drifting between rooftops and yellow streetlamps glowing in the narrow alleys below.
- 3.0–7.0s: The camera glides down past tangled overhead wires to a small upper-floor window of a narrow tube house, where @BaNhan swings open the wooden shutters and murmurs to herself, her wrinkled face clear in the lamplight.
- 7.0–10.0s: @BaNhan closes her mouth and gazes down at the warm light and soft steam spilling from the kitchen window below, one hand pressed to her lower back. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mới bốn giờ sáng, cả phố còn ngủ say, con dâu tôi đã lục đục dưới bếp đồ xôi rồi." (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a distant rooster, a cold breeze, wooden shutters creaking, a soft hiss of steam below. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 2 (`canh-01/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, slow push-in toward the altar shelf; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The dim kitchen before dawn, a big aluminum sticky-rice steamer rattling on the gas stove beside a small family altar shelf glowing with a tiny red lamp.
- 3.0–7.0s: @Thu steps in front of the altar shelf in her green apron, raises three lit incense sticks to her forehead and whispers a prayer, her lips moving softly in the red glow.
- 7.0–10.0s: @Thu closes her mouth, plants the incense sticks in the small bowl on the shelf and turns toward the steamer as a thick cloud of steam rolls up. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Con lạy tổ tiên, mười hai năm làm dâu, con chỉ xin chồng con làm ăn suôn sẻ, cả nhà bình an." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, the steamer lid rattling, the gas flame purring, a faint crackle of incense. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 3 (`canh-01/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up framing her face and hands over the table, slow tilt; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu bends over the wooden table with her face and work-roughened hands both in frame, scooping warm sticky rice onto a square of green banana leaf as she starts to murmur to herself.
- 3.0–7.0s: @Thu keeps murmuring with a faint wry smile, her lips moving clearly while her fingers fold the banana-leaf corners into a neat parcel.
- 7.0–10.0s: @Thu closes her mouth and sets the finished parcel beside a growing row of identical green parcels, her calloused fingertips resting on the last one. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Hồi anh ấy còn trắng tay, cả nhà sống nhờ mấy gói xôi này, tay có chai đi một chút cũng chẳng sao." (no subtitles)
- @Thu keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: banana leaves rustling, a soft steam hiss, the gas flame purring. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 4 (`canh-01/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 40mm medium low-angle shot from the foot of the staircase, slow tilt up; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The steep tiled staircase in the dim light, a faint glow from the kitchen climbing the steps, the upper floor still dark.
- 3.0–7.0s: @BaNhan comes slowly down the stairs in her brown cardigan, leaning on her bamboo walking stick, and mutters to herself with her wrinkled face turned toward the light.
- 7.0–10.0s: @BaNhan closes her mouth and pauses on the lowest step with one hand pressed to her lower back, her eyes fixed on the warm kitchen. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Lưng đau quá không ngủ được, thôi xuống đỡ con Thu một tay, nó gánh cả cái nhà này rồi." (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: slow footsteps on tiles, the tap of a bamboo stick, steam hissing below. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 5 (`canh-01/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder two-shot across the dining table, slow dolly; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The wooden dining table beside the stove, a plate of banana-leaf parcels and two low stools, steam drifting through the warm light.
- 3.0–7.0s: @BaNhan lowers herself onto a stool by the table as @Thu turns from the stove, and @BaNhan speaks to her softly, her wrinkled face creased with concern.
- 7.0–10.0s: @BaNhan finishes speaking and keeps her eyes on @Thu, both hands resting on top of her bamboo stick. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thu ơi, con nghỉ tay ăn miếng xôi đi đã, tối qua thằng Tùng lại về muộn hả con?" (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, a stool creaking, a rooster outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 6 (`canh-01/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up over the table, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu sets a small bowl of warm sticky rice in front of @BaNhan, wiping her hands on her green apron.
- 3.0–7.0s: @Thu speaks gently with a thin tired smile, her eyes sliding away toward the dark staircase.
- 7.0–10.0s: @Thu turns back to the stove and lifts the steamer lid again, her shoulders tight under the faded blue blouse. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh ấy dạo này nhiều việc lắm mẹ ạ, mẹ cứ lên ngủ thêm đi, con lo được hết." (no subtitles)
- @Thu keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, chopsticks against a bowl, a distant moped. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 1 (`canh-02/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: A quiet old-quarter street corner at dawn, yellow streetlamps still glowing and mist over the pavement, a small sticky-rice stall steaming under a big faded umbrella.
- 3.0–7.0s: @Thu lifts the lid of the steaming pot as an elderly woman street sweeper in an orange vest pauses by the stall with her bamboo broom, and @Thu calls to her warmly with a bright smile.
- 7.0–10.0s: @Thu closes her mouth and holds out a warm banana-leaf parcel across the basket, and the sweeper leans her broom on the umbrella pole and takes it with both hands. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cô ơi, sương lạnh thế này, cô ngồi làm gói xôi nóng đã, sáng nào cháu cũng phần cô một gói." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a moped passing, steam hissing, a bamboo broom sweeping the pavement. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 2 (`canh-02/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: Close on the stall's low plastic stool and the bamboo basket of banana leaves, steam drifting across the frame in the grey dawn.
- 3.0–7.0s: @Thu sits on the low stool, opens a small empty red velvet earring box with her thumb and murmurs to herself, her lips moving softly as she gazes at the bare velvet.
- 7.0–10.0s: @Thu closes her mouth and rests her thumb on the empty velvet slot, her eyes glistening in the grey dawn light. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Đôi bông tai cưới, của hồi môn duy nhất, mười hai năm trước mình bán đi cho anh ấy làm vốn." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, the soft click of a box lid, a moped far away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 3 (`canh-02/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 3.0–7.0s: @BaNhan shuffles into the kitchen on her bamboo walking stick, looks up at the small white home camera and speaks up to it with a fond crinkled smile.
- 7.0–10.0s: @BaNhan closes her mouth and gives the camera a small wave, then lowers herself onto a stool beside the covered plate of parcels. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.6s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thu ơi, thằng Tùng nó làm giám đốc rồi, con còn ra gánh xôi làm gì cho khổ thân hả con?" (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a bamboo stick tapping on tiles, a stool creaking, a rooster outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 4 (`canh-02/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up, slow rack focus; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The edge of the stall's low stool with an old cracked smartphone lying face-up beside the basket, its screen glowing blank in the dawn light.
- 3.0–7.0s: @Thu picks up the old phone, looks at its glowing blank screen with a soft laugh, then holds it close to her mouth and speaks into it warmly.
- 7.0–10.0s: @Thu closes her mouth with a small relieved smile and slips the phone back into her apron pocket as steam drifts past the umbrella. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mẹ ơi, anh ấy giàu thì giàu, con vẫn phải giữ cái nghề, lỡ mai kia nhà mình lại trắng tay." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, a distant moped, soft dawn birdsong. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 5 (`canh-02/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm over-the-shoulder shot from behind the customer, gentle dolly; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The steaming pot under the faded umbrella, banana-leaf parcels lined up in the bamboo basket, a moped parked at the curb.
- 3.0–7.0s: @Thu stands behind the pot facing a woman customer in a pink raincoat, holds up a warm banana-leaf parcel and speaks to her with a bright smile.
- 7.0–10.0s: @Thu finishes speaking and tucks an extra spoonful of pork floss into the parcel, then hands it across the basket as the customer nods. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Xôi xéo hành phi nóng đây, chị ăn thử đi, em gói thêm cho chị ít ruốc nhé!" (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, rustling banana leaves, mopeds passing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 6 (`canh-02/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Dawn on a Hà Nội old-quarter pavement corner: a small sticky-rice stall with a bamboo basket, a steaming pot and banana leaves under a big faded umbrella, low plastic stools, mopeds passing, blue-grey dawn light and yellow streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- Extra: a woman customer in a pink raincoat
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, slow crane up into a wide view; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu wipes her hands on her green apron and nods toward the distant skyline, starting to speak to the customer in the pink raincoat with a shy proud smile.
- 3.0–7.0s: @Thu keeps speaking with her face turned up toward the far glass towers, a wistful light in her eyes, as the camera begins to rise above the faded umbrella.
- 7.0–10.0s: The camera keeps rising above the umbrella to reveal glass towers on the distant skyline catching the sunrise, while @Thu stands silent beside the tiny steaming stall below. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.2s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chồng em làm ở tòa nhà kính đằng kia chị ạ, ngày xưa hai vợ chồng chỉ dám đứng dưới đường mà nhìn." (no subtitles)
- @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: mopeds, morning street noise rising, steam hissing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 1 (`canh-03/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: Morning light through the open front door of the narrow house, a small mirror hanging beside the steep tiled staircase, a leather briefcase on a stool.
- 3.0–7.0s: @Tung steps in front of the mirror in his charcoal-grey suit with a sleek phone pressed to his ear, smoothing his gelled hair as he speaks into it in a clipped bossy tone.
- 7.0–10.0s: @Tung closes his mouth, lowers the phone and fastens the gold watch on his wrist, studying his reflection with his chin raised. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cậu đánh xe ra đầu ngõ đón tôi, lau cho bóng vào, hôm nay tôi ký hợp đồng lớn đấy." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a moped outside, the click of a watch clasp, morning birds. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 2 (`canh-03/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm close-up at child height, slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The foot of the steep staircase seen from child height, a small red toy drum with two wooden sticks resting on the bottom step in the morning light.
- 3.0–7.0s: @Na comes down the last steps in her school uniform and red scarf, hugs the little red drum to her chest and whispers to herself, her bright eyes turned toward the mirror.
- 7.0–10.0s: @Na closes her mouth and rises onto her toes at the bottom of the stairs, holding the drum tight, waiting with a hopeful face. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Lần này mình phải rủ được bố đi xem diễn, năm nào cũng chỉ có mẹ với bà đến thôi." (no subtitles)
- From 3.0s onward, @Na's face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: light footsteps on tiles, a soft drum tap, a moped outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 3 (`canh-03/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium two-shot, slow dolly; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The space beside the mirror and the staircase, a leather briefcase on a stool, warm morning light falling across the tiled floor.
- 3.0–7.0s: @Na steps up to @Tung holding the little red drum to her chest and speaks up at him, her pigtails bobbing.
- 7.0–10.0s: @Na finishes and waits with her eyes fixed on @Tung's face, her small fingers tight around the drumsticks. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bố ơi, chiều nay bố đến xem con đánh trống nhé, cô giáo bảo ai cũng có bố mẹ đến." (no subtitles)
- From 3.0s onward, @Na's face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a moped outside, morning birds. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 4 (`canh-03/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up over the drum, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung glances down at @Na and gives the top of her head one quick distracted pat, his other hand already lifting his briefcase.
- 3.0–7.0s: @Tung speaks to @Na while checking the gold watch on his wrist, his eyes never quite meeting hers.
- 7.0–10.0s: @Na lowers the little red drum slowly to her side, her lower lip tucked in as @Tung turns away toward the door. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bố bận họp cả ngày, con bảo mẹ đi xem cho, bố còn phải kiếm tiền nuôi cả nhà." (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a briefcase clasp clicking, footsteps on tiles. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 5 (`canh-03/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide two-shot from the kitchen, slow lateral dolly; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The kitchen near the open front door, a bowl of steaming sticky rice with fried shallots resting on the wooden dining table.
- 3.0–7.0s: @Thu comes from the stove carrying the bowl of steaming sticky rice in both hands and speaks to @Tung as he reaches the doorway.
- 7.0–10.0s: @Thu holds the bowl out toward @Tung across the gap between them, steam rising between her hands. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh ăn bát xôi rồi hẵng đi, em đồ từ sáng sớm, vẫn còn nóng nguyên đây này." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, a moped idling outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 6 (`canh-03/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot, slow push-in on the bowl; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung looks at the bowl with a curl of his lip, already half-turned toward the open front door.
- 3.0–7.0s: @Tung speaks curtly over his shoulder and walks out into the bright alley without looking back, his briefcase swinging.
- 7.0–10.0s: @Thu stands alone in the doorway holding the steaming bowl in both hands, the steam thinning in the cold morning air. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thôi, xôi với chả xôi, ngày nào cũng xôi, anh ra ngoài ăn cho sạch sẽ." (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: footsteps leaving, a car door shutting outside, an engine pulling away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 1 (`canh-04/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 24mm wide shot, slow dolly through the glass office; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A bright glass-walled office high above the city, the large white desk gleaming in cold morning light with the skyline stretching beyond the windows.
- 3.0–7.0s: @Vy walks in through the glass door in her crimson dress and beige high heels, mists a little perfume into the air by the desk and murmurs to herself with a slow smile.
- 7.0–10.0s: @Vy closes her red lips and runs one fingertip along the back of the black leather chair, her winged eyes sweeping across the skyline. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.5s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Tầng hai mươi, nhìn ra cả thành phố, rồi cả căn phòng này lẫn ông chủ của nó sẽ là của mình." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: high heels clicking on a polished floor, a soft perfume spritz, air conditioning hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 2 (`canh-04/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium two-shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The white desk with a glossy black lacquered lunch box resting beside a framed family photo of Thu, Tùng and Na, the city skyline blurred in the windows behind.
- 3.0–7.0s: @Tung strolls in through the glass door with his briefcase and finds @Vy standing by the desk, and he speaks to her with a slow pleased grin, breathing in the air.
- 7.0–10.0s: @Tung closes his mouth and sinks into the black leather chair, while @Vy stands beside the desk turning her thin gold necklace between her fingers. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Vy à, em về làm thư ký mới ba tháng mà phòng anh lúc nào cũng thơm mùi nước hoa của em." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a glass door sighing shut, footsteps on a polished floor, air conditioning hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 3 (`canh-04/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy slides a glossy black lacquered lunch box across the white desk toward @Tung and begins to speak in a sweet soft voice.
- 3.0–7.0s: @Vy keeps speaking as she leans one hand on the edge of the desk, tilting her head with a honeyed smile while @Tung looks up at her.
- 7.0–10.0s: @Vy closes her mouth and waits with her head tilted, her red nails resting beside the lunch box, as @Tung reaches for the lid. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.2s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh Tùng ơi, em tự tay nấu cơm trưa cho anh đấy, dạo này anh gầy đi nhiều quá." (no subtitles)
- @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a lunch box sliding on the desk, air conditioning hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 4 (`canh-04/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: @Tung lifts the lid of a glossy black lacquered lunch box and looks at the neat rows of food inside.
- 3.0–7.0s: @Tung speaks to @Vy with a slow pleased grin, leaning back in the black leather chair.
- 7.0–10.0s: @Vy lowers her eyes with a modest closed-mouth smile, her fingers trailing along the edge of the white desk. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Lâu lắm rồi mới có người lo cho anh một bữa trưa tử tế thế này đấy em ạ." (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a lid lifting, chair leather creaking, faint traffic below. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 5 (`canh-04/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium shot, slow lateral dolly; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A slim waste bin beside the glass wall of the office, cold city light falling across the polished floor.
- 3.0–7.0s: @Vy walks to the glass wall, drops a crumpled plain paper takeaway bag into the waste bin and murmurs under her breath with a mocking little smile, glancing back over her shoulder.
- 7.0–10.0s: @Vy closes her red lips, brushes her palms together and smooths the front of her crimson dress, her eyes cold. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cơm nhà hàng dưới phố đấy, đàn ông chỉ cần nghe hai chữ tự tay là mềm lòng ngay." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper crumpling, high heels on the floor, air conditioning hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 6 (`canh-04/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on the desk corner, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy strolls back to the corner of the white desk, tilts her head toward a framed family photo of Thu, Tùng and Na and speaks to it in a sugary whisper.
- 3.0–7.0s: @Vy keeps whispering with a sweet smile as she reaches out one manicured finger and slowly lays the frame face down on the desk.
- 7.0–10.0s: @Vy closes her mouth, her red fingernails resting on the back of the face-down frame, her smile reflected cold in the glossy white surface. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.2s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Nhà ba người đẹp quá nhỉ, tiếc là tấm ảnh này sắp phải thay người đứng cạnh anh rồi." (no subtitles)
- @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft tap of a frame on the desk, air conditioning hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 1 (`canh-05/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
An upscale café at noon: velvet armchairs, brass lamps, marble tables, tall windows facing a leafy street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide establishing shot, slow pan across the room; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A hushed upscale café at noon, sunlight filtering through tall windows onto velvet armchairs and marble tables under warm brass lamps.
- 3.0–7.0s: @Vy slips in through the café door in her crimson dress and dark sunglasses, a phone pressed to her ear, and speaks into it in a low honeyed voice while glancing around.
- 7.0–10.0s: @Vy closes her mouth and keeps the phone to her ear, listening, her eyes searching toward a secluded corner half-hidden behind a tall potted palm. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh yêu ơi, em ra rồi đây, em bảo lão là đi gặp khách hàng, anh ngồi chỗ nào đấy?" (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft clinking of cups, a café door chime, muted street sounds. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 2 (`canh-05/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
An upscale café at noon: velvet armchairs, brass lamps, marble tables, tall windows facing a leafy street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The secluded corner table behind the potted palm, two coffee cups on the marble and a velvet armchair angled toward the window.
- 3.0–7.0s: @Khai leans back in the velvet armchair in his black slim-fit shirt with a phone at his ear, and speaks into it in a lazy low voice with a sly half-smile.
- 7.0–10.0s: @Khai closes his mouth, sets the phone face down on the marble and lifts his coffee cup slightly toward the café entrance, his silver chain bracelet catching the lamplight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Góc trong cùng, sau chậu cau ấy, em cứ đi thẳng vào, chỗ này kín đáo, chẳng ai nhìn thấy đâu." (no subtitles)
- From 3.0s onward, @Khai's face and lips stay clearly visible while speaking; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: cups clinking, a low murmur, a café door chime. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 3 (`canh-05/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm over-the-shoulder two-shot, gentle dolly; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The corner table in warm lamplight, an empty velvet armchair facing the one by the window, a steaming cup set before it.
- 3.0–7.0s: @Vy sinks into the empty armchair and slips off her sunglasses as @Khai leans toward her across the marble table and speaks in a low lazy voice.
- 7.0–10.0s: @Khai taps one finger on the table with a sly grin, waiting, while @Vy folds her hands on her white handbag and studies him. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.0s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thế nào em, lão giám đốc cắn câu chưa? Hợp đồng lớn sắp ký rồi đấy." (no subtitles)
- From 3.0s onward, @Khai's face and lips stay clearly visible while speaking; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: cups clinking, a low café murmur. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 4 (`canh-05/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy stirs her coffee slowly, the spoon circling, her winged eyes lifting to meet @Khai's.
- 3.0–7.0s: @Vy speaks to @Khai in a cool clipped voice, the sweetness gone from her face.
- 7.0–10.0s: @Vy sets the spoon down on the saucer with a precise click and leans back, her red lips pressed into a thin line. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Nửa năm thôi anh, em sẽ khiến lão bỏ vợ, sang tên hết nhà cửa cho em." (no subtitles)
- @Vy keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a spoon clinking on porcelain, a low café murmur. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 5 (`canh-05/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium two-shot, slow lateral dolly; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Khai rests his elbows on the marble table and lowers his head toward @Vy, his half-smile fading.
- 3.0–7.0s: @Khai speaks quietly to @Vy, glancing once toward the café windows and the leafy street outside.
- 7.0–10.0s: @Khai sits back and lifts his coffee cup in a small toast toward @Vy, his eyes sharp above the rim. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Đừng để lão biết có anh, đàn ông ngu đến mấy cũng có lúc tỉnh ra đấy em." (no subtitles)
- @Khai keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a low café murmur, a car passing outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 6 (`canh-05/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on her face over the coffee cup, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy stirs her coffee in slow circles with a silver spoon and answers @Khai with a sweet smile, her red lips moving softly.
- 3.0–7.0s: @Vy keeps speaking as the sweetness drains from her face, her winged eyes lifting cold and still above the cup.
- 7.0–10.0s: @Vy closes her mouth and sets the spoon on the saucer with a precise click, while @Khai raises his cup to her at the soft edge of the frame. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.4s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh yên tâm, lão mê em như điếu đổ, đến lúc lão tỉnh ra thì lão đã trắng tay rồi." (no subtitles)
- @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a spoon circling porcelain, a soft café murmur. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 1 (`canh-06/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot, slow dolly-in across the kitchen; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The dim kitchen at night lit by one warm bulb, the charcoal stove glowing low, a white dress shirt and a loosened silk tie draped carelessly over a dining chair.
- 3.0–7.0s: @BaNhan comes slowly down the steep staircase leaning on her bamboo walking stick, stops beside the chair, sniffs the air and mutters to herself with her wrinkled face tight.
- 7.0–10.0s: @BaNhan closes her mouth and stares at the rumpled white shirt hanging from the chair, a pair of polished black shoes left askew beneath it. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thằng Tùng lại gần nửa đêm mới về, mùi rượu lẫn mùi nước hoa lạ nồng nặc cả nhà." (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the charcoal stove crackling softly, a dog barking far away, a door closing upstairs. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 2 (`canh-06/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium two-shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The wooden dining chair under the warm bulb, the white shirt and loose tie draped over its back, the charcoal stove glowing beside it.
- 3.0–7.0s: @Thu comes down the last stairs in her faded blouse and picks up the white shirt from the chair, as @BaNhan, leaning on her stick by the table, speaks to her in a low tired voice.
- 7.0–10.0s: @BaNhan closes her mouth and shakes her head slowly, while @Thu folds the shirt over her arm and lifts the collar toward the light, her brows drawing together. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.8s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Khuya rồi con còn xuống làm gì, áo của nó cứ để đấy, đêm nào con cũng phải giặt cho nó à?" (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft footsteps, fabric rustling, the stove crackling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 3 (`canh-06/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on her face above the collar, slow rack focus; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu turns the white collar toward the bulb beside her face, revealing a smudge of bright red lipstick on the fabric, and starts to speak to @BaNhan in a trembling whisper.
- 3.0–7.0s: @Thu keeps speaking as she lifts a single long wavy brown hair from the shoulder of the shirt and holds it up in the warm light beside her face.
- 7.0–10.0s: @Thu closes her mouth, her eyes wide and wet above the shirt, while @BaNhan's wrinkled hand tightens on her bamboo stick at the edge of the frame. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.2s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mẹ ơi, son đỏ trên cổ áo, còn sợi tóc xoăn màu nâu này, đâu phải tóc của con." (no subtitles)
- @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a sharp intake of breath, the stove crackling, silence. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 4 (`canh-06/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The foot of the steep staircase in the dim warm light, the dining table between the stairs and the glowing stove.
- 3.0–7.0s: @Tung appears on the lower stairs loosening his collar, and @Thu holds up the white shirt toward him from across the table and speaks in a trembling but steady voice.
- 7.0–10.0s: @Thu keeps the shirt raised between them, her knuckles pale, while @Tung stops two steps above the floor. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.0s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh Tùng, vệt son trên áo anh là của ai? Anh nói thật với em đi." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the stove crackling, a creaking stair. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 5 (`canh-06/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung rolls his eyes and waves one hand dismissively, stepping down onto the tiled floor.
- 3.0–7.0s: @Tung speaks flatly to @Thu without looking at the shirt, his jaw set and his eyelids heavy with drink.
- 7.0–10.0s: @Tung turns his back on @Thu and climbs the stairs again, one hand on the rail, leaving her below. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Tiếp khách thì dính son là chuyện thường, cô đừng nghĩ linh tinh rồi làm ầm lên." (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heavy footsteps on the stairs, the stove crackling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 6 (`canh-06/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium shot from the kitchen, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The bottom of the steep tiled staircase in the dim kitchen, the bulb's warm light fading and the charcoal stove reduced to faint embers.
- 3.0–7.0s: @Thu sits down on the lowest stair with the white shirt clutched in both hands in her lap and whispers to herself, her lips trembling, her back against the wall.
- 7.0–10.0s: @Thu closes her mouth and sits motionless on the step as pale blue dawn light slowly creeps under the front door, the shirt still crushed in her hands. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bao nhiêu năm vợ chồng, đến một câu nói thật anh ấy cũng chẳng cho mình nữa rồi." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: embers ticking, a distant rooster at dawn, silence. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 1 (`canh-07/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 3.0–7.0s: The camera sweeps down to the infinity pool terrace, where @Tung, his suit jacket off, stands by a white lounger with a phone at his ear and speaks into it in a flat dutiful voice.
- 7.0–10.0s: @Tung closes his mouth, lowers the phone and tosses it onto the lounger with a smirk, the pool's edge blending into the shining sea behind him. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh còn kẹt công tác ở Đà Nẵng, sinh nhật em anh không về kịp, em với con cứ ăn trước đi." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: gentle waves, palm fronds rustling, distant seabirds. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 2 (`canh-07/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Sunset at a luxury seaside resort: an infinity pool terrace with white loungers, palm trees, the sea glowing orange.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, slow lateral dolly along the pool; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Two white loungers at the edge of the infinity pool, a small table between them holding two glasses of orange juice, the sea glowing beyond.
- 3.0–7.0s: @Vy in her crimson dress sits on one lounger and hands @Tung a glass of orange juice as he settles beside her, and she teases him in a sweet mocking voice.
- 7.0–10.0s: @Vy closes her mouth and clinks her glass against @Tung's, the two of them sitting close and gazing out at the orange sea. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Công tác gì mà chỉ có hai đứa mình, bên bể bơi nhìn ra biển thế này hả anh?" (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: gentle waves, glasses clinking, a soft breeze. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 3 (`canh-07/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: @Vy turns toward @Tung on the lounger, resting her chin on her hand, the sunset gilding her wavy hair.
- 3.0–7.0s: @Vy speaks to @Tung in a sweet coaxing voice, her winged eyes half-lowered.
- 7.0–10.0s: @Vy tilts her head and waits with a soft closed-mouth smile, turning the glass slowly between her fingers. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ở bên anh em mới biết thế nào là được yêu, vợ anh có biết chiều anh thế này không?" (no subtitles)
- @Vy keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: waves lapping, a soft breeze. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 4 (`canh-07/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Sunset at a luxury seaside resort: an infinity pool terrace with white loungers, palm trees, the sea glowing orange.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, slow pull-back; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung sets his glass down on the small table and leans back on the lounger with a long sigh.
- 3.0–7.0s: @Tung speaks to @Vy with a dismissive shrug, his eyes on the darkening sea.
- 7.0–10.0s: @Vy lays her hand lightly over @Tung's on the armrest as the last sunlight fades behind them. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cô ấy chỉ biết xôi với chợ thôi em ạ, sống với cô ấy anh thấy mình già đi mười tuổi." (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: waves, a breeze through the palms. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 5 (`canh-07/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 40mm over-the-shoulder shot across the birthday cake, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The wooden dining table in the dim kitchen at night, a small round birthday cake with a single unlit candle, three bowls and one empty chair.
- 3.0–7.0s: @Na carefully lights the single candle with a match while @Thu, facing the camera across the cake, speaks to her softly with a thin brave smile, both faces lit by the tiny flame.
- 7.0–10.0s: @Thu closes her mouth and rests her hand on @Na's shoulder as both glance at the empty chair across the table, the candle flickering between them. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bố bận công tác rồi, sinh nhật mẹ con ước giúp mẹ một điều đi, rồi mình thổi nến." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a match striking, a faint candle hiss, rain beginning outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 6 (`canh-07/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Na clasps her small hands together in front of the candle and closes her eyes for a moment.
- 3.0–7.0s: @Na opens her eyes and speaks softly to @Thu, her face glowing in the candlelight.
- 7.0–10.0s: @Thu presses her lips together and strokes @Na's hair, her eyes glistening as the candle flame trembles. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mẹ ơi, con ước bố về ăn cơm với mẹ con mình, như hồi nhà mình còn nghèo ấy." (no subtitles)
- @Na keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a candle flickering, soft rain on the roof. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 1 (`canh-08/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The dining table in the dim kitchen, a sleek black smartphone lying face-up beside a car key, the bulb casting a warm circle of light.
- 3.0–7.0s: The phone buzzes with a blank white glow as @Thu steps over from the stove, looks down at it and murmurs to herself, her brows knitting, her face lit from below.
- 7.0–10.0s: @Thu closes her mouth and hesitates with her damp hand hovering above the glowing phone, glancing once toward the dark staircase. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh Tuấn kế toán à? Nửa đêm rồi, kế toán gì mà gọi cho anh ấy vào giờ này?" (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone buzzing on wood, a dripping tap. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 2 (`canh-08/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow push-in on her face; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu picks up the phone and its screen casts a cold white glow up across her face, her eyes fixing on it as her lips start to move in a broken whisper.
- 3.0–7.0s: @Thu keeps whispering with her pupils trembling and her voice catching, the phone shaking slightly in her hand.
- 7.0–10.0s: @Thu closes her mouth and slowly presses her free hand over it, a single tear sliding down her cheek in the cold light. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Trời ơi, cô gái váy đỏ này đang tựa vào vai chồng mình, anh Tuấn kế toán là thế này đây à?" (no subtitles)
- @Thu keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the tap dripping, a heavy silence. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 3 (`canh-08/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The steep staircase and the dining table in the dim kitchen, the phone's cold glow the brightest light in the room.
- 3.0–7.0s: @Tung strides down the last stairs and stops on the far side of the table from @Thu, pointing at the phone in her hand as he speaks sharply.
- 7.0–10.0s: @Tung holds out his open palm across the table, waiting, while @Thu stays where she is with the phone held against her chest. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cô lục điện thoại của tôi à? Cô còn biết tôn trọng chồng mình không hả?" (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heavy footsteps on tiles, the tap dripping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 4 (`canh-08/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu sets the glowing phone face-down on the table between them, her hand trembling as she lets go.
- 3.0–7.0s: @Thu speaks to @Tung with her chin lifted and her voice cracking, tears standing in her eyes.
- 7.0–10.0s: @Thu keeps her gaze locked on @Tung, breathing hard, her fingers gripping the edge of the table. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mười hai năm em bán cả bông tai cưới cho anh làm ăn, anh trả em thế này sao?" (no subtitles)
- @Thu keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone set down on wood, the tap dripping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 5 (`canh-08/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm over-the-shoulder shot, slow dolly; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung picks his phone up off the table and slips it into his trouser pocket without looking at @Thu.
- 3.0–7.0s: @Tung speaks coldly to @Thu with a flick of his hand toward the room around them, his mouth twisted.
- 7.0–10.0s: @Tung turns away and climbs the stairs two at a time, leaving @Thu alone at the table under the swaying bulb. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chuyện cũ rồi, đừng lôi ra kể công mãi, tôi chán cái nhà này lắm rồi." (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: footsteps on the stairs, a door shutting hard upstairs. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 6 (`canh-08/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 3.0–7.0s: @BaNhan stands pressed against the wall of the landing in her brown cardigan, both hands clenched on her bamboo walking stick, and whispers to herself with trembling lips.
- 7.0–10.0s: @BaNhan closes her mouth, lowers her head and shuts her eyes, her thin shoulders shaking as the light from below flickers across her wrinkled face. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.6s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Tôi nghe hết rồi, thằng con tôi dứt ruột đẻ ra mà nỡ nói với vợ nó những lời như thế." (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a door closing upstairs, the faint drip of a tap below, silence. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 1 (`canh-09/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium shot from across the curb, slow pan following her; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A black luxury sedan with no badge glides to a stop at the curb beside the small sticky-rice stall, dawn mist curling around its glossy doors.
- 3.0–7.0s: @Vy steps out of the car in her crimson dress, slipping on dark sunglasses and murmuring to herself with a thin smile, her face and red lips clearly visible as she speaks.
- 7.0–10.0s: @Vy finishes speaking and closes her lips, then walks slowly toward the steaming stall, her heels clicking on the wet pavement, the car door left open behind her. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thì ra bà vợ bán xôi của anh Tùng ngồi ở đây, để xem chị ta mặt mũi thế nào." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a car engine idling, high heels clicking on wet pavement, mopeds passing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 2 (`canh-09/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on her face and hands, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Banana leaves and a bamboo basket of steaming sticky rice on the stall table, wisps of steam drifting through the blue dawn light.
- 3.0–7.0s: @Thu glances up from wrapping a parcel of sticky rice, her hands stopping in mid-fold, and whispers to herself under her breath, her face and lips clearly visible in the dawn light.
- 7.0–10.0s: @Thu finishes whispering and closes her mouth, standing perfectly still with her eyes fixed on something beyond the stall as the steam drifts across her face. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chiếc váy đỏ này, đúng là cô gái trong tấm ảnh đêm qua rồi, cô ta đến đây làm gì?" (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing from the pot, distant mopeds, a dog barking far away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 3 (`canh-09/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Dawn on a Hà Nội old-quarter pavement corner: a small sticky-rice stall with a bamboo basket, a steaming pot and banana leaves under a big faded umbrella, low plastic stools, mopeds passing, blue-grey dawn light and yellow streetlamps.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder shot from behind the stall toward the street, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The front of the stall seen across the steaming pot, a stack of folded banana leaves and an empty low plastic stool on the pavement.
- 3.0–7.0s: @Vy stops in front of the stall and lowers her sunglasses slightly, smiling sweetly at @Thu, who stands behind the pot holding a banana leaf.
- 7.0–10.0s: @Vy finishes speaking with her head tilted, one hand resting on her white handbag, while @Thu keeps her eyes steady on her. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chị cho em một gói xôi xéo, nghe nói ngày xưa anh Tùng mê xôi của chị lắm." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, a moped passing, the soft rustle of banana leaves. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 4 (`canh-09/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium two-shot across the stall, gentle handheld; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu sets down the banana leaf and straightens her back, facing @Vy across the steaming pot.
- 3.0–7.0s: @Thu speaks calmly to @Vy, her jaw firm and her rough hands resting flat on the edge of the stall table.
- 7.0–10.0s: @Thu gestures once toward the empty plastic stool, her gaze level, while @Vy's smile tightens at the corners. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ngày xưa hay bây giờ, anh ấy vẫn là chồng tôi, cô muốn ăn xôi thì cứ ngồi xuống." (no subtitles)
- @Thu keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, a ladle tapping the pot rim, distant traffic. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 5 (`canh-09/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on the woman in red, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy takes off her sunglasses and lets her eyes drift slowly down to @Thu's hands on the stall table.
- 3.0–7.0s: @Vy speaks to @Thu in a soft sweet voice, a thin smile on her red lips, one eyebrow lifting.
- 7.0–10.0s: @Vy holds her gaze on @Thu's work-roughened hands with her chin lifted, as @Thu's fingers slowly curl inward. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chị giữ được bếp, nhưng giữ không nổi chồng đâu chị ạ, nhìn đôi tay chị kìa." (no subtitles)
- @Vy keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, a moped horn far away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 6 (`canh-09/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot of the lonely stall, slow dolly back; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A folded banknote lies on the round bamboo tray of sticky rice, the black luxury sedan with no badge pulling away from the curb in the background.
- 3.0–7.0s: @Thu stands alone behind the stall, slowly lifts both hands palm up to look at the calluses and cracked skin, and murmurs to herself, her face and lips clearly visible.
- 7.0–10.0s: @Thu finishes speaking and closes her mouth, still looking down at her open hands in the blue dawn light as the steam rises around her. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Đôi bàn tay này nuôi anh ấy mười hai năm, giờ lại bị người ta đem ra chê cười." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a car driving away, steam hissing, the first birds of the morning. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 1 (`canh-10/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium shot, slow glide along the dinner table; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A wooden dining table under one warm bulb, set with a full family dinner of braised fish, stir-fried morning glory, crab soup and a pot of rice, steam curling up from the dishes.
- 3.0–7.0s: @Thu sets a steaming bowl of crab soup at the head of the table, then turns toward the steep staircase and calls up with a small smile, her face and lips clearly visible.
- 7.0–10.0s: @Thu finishes calling and closes her mouth, smoothing her apron and waiting beside the table with her eyes on the stairs, four bowls and four pairs of chopsticks laid neatly in place. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh Tùng ơi, xuống ăn cơm đi anh, hôm nay em nấu cá kho với canh cua anh thích đấy." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a charcoal stove crackling, a pot lid rattling softly, slow footsteps creaking on the stairs above. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 2 (`canh-10/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm over-the-shoulder shot from behind her toward him, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The dinner table in the warm kitchen light, a pair of chopsticks laid across an untouched bowl of rice.
- 3.0–7.0s: @Tung sits at the head of the table in his charcoal suit and puts his chopsticks down, speaking flatly to @Thu across the dishes.
- 7.0–10.0s: @Tung leans back with his arms folded, while @Thu sits motionless in the foreground across from him, a soup ladle still in her hand. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mình ly hôn đi, tôi không chịu nổi cái mùi bếp núc với gánh xôi của cô nữa." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: chopsticks clicking on porcelain, the charcoal stove crackling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 3 (`canh-10/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on her face past his shoulder, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu slowly lowers the ladle into the soup bowl, her eyes locked on @Tung.
- 3.0–7.0s: @Thu speaks to @Tung in a low trembling voice, her chin lifting and her knuckles whitening on the table edge.
- 7.0–10.0s: @Thu holds his gaze without blinking, a tear sliding down one cheek as her lips press together. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh nói lại xem, anh định bỏ mẹ con em vì một đứa con gái kém anh mười mấy tuổi à?" (no subtitles)
- @Thu keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the soup bowl clinking, rain beginning outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 4 (`canh-10/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot from the end of the table, slow tilt up; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A bamboo walking stick leaning against a low stool at the corner of the dinner table, a small rice bowl in front of it.
- 3.0–7.0s: @BaNhan rises abruptly from her stool on her bamboo walking stick, her thin hands trembling, and speaks sharply across the table, her wrinkled face and lips clearly visible.
- 7.0–10.0s: @BaNhan finishes speaking and closes her mouth as the chopsticks slip from her fingers and clatter onto the dinner tray, her eyes fixed hard across the table. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.6s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mày vừa nói cái gì hả Tùng? Mẹ còn sống sờ sờ ra đây mà mày dám đòi bỏ vợ à?" (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a stool scraping on tiles, chopsticks clattering onto a tray. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 5 (`canh-10/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder shot from behind the son toward the mother, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The dinner tray with scattered chopsticks and cooling dishes, the steep tiled staircase in the dim background.
- 3.0–7.0s: @BaNhan stands leaning on her bamboo walking stick and speaks sharply across the table to @Tung, her wrinkled face trembling.
- 7.0–10.0s: @BaNhan points a shaking finger at @Tung from across the table, while @Tung looks away and clenches his jaw. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mày quên ai bán bông tai cưới cho mày làm ăn rồi à? Mày còn là con người không?" (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain on the roof, a walking stick tapping the tiled floor. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 6 (`canh-10/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on his face, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung stands up from the table and buttons his suit jacket, avoiding his mother's eyes.
- 3.0–7.0s: @Tung speaks coldly to @BaNhan, his jaw tight and his gaze fixed on the front door.
- 7.0–10.0s: @Tung turns his shoulder away from the table and stands still, breathing hard through his nose. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mẹ đừng bênh cô ấy nữa, con có quyền được sống cho mình, con quyết rồi mẹ ạ." (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain on the roof, a chair scraping back. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 1 (`canh-11/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot from the staircase, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A glowing charcoal stove in the dark kitchen beside an aluminum basin of soaking sticky rice, a single warm bulb swaying slightly overhead.
- 3.0–7.0s: @Thu sits alone on a low stool beside the stove, rinsing the soaked rice with both hands and whispering to herself in a thin voice, tears dripping into the basin, her face and lips visible in the orange glow.
- 7.0–10.0s: @Thu finishes whispering and closes her mouth, her wet hands resting still in the rice and her shoulders shaking silently. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mười hai năm đồ xôi nuôi anh ấy, giờ anh ấy lại chê nhà mình hôi mùi bếp." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal crackling, water swishing in a basin, crickets outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 2 (`canh-11/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on her face, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu glances up toward the dark staircase and whispers to herself, her lips moving softly in the stove's orange glow, a tear running down to her chin.
- 3.0–7.0s: @Thu finishes whispering, closes her mouth and presses the back of her wrist against her lips, holding her breath and listening.
- 7.0–10.0s: @Thu lowers her wrist and wipes her cheeks with her apron, breathing slowly to steady herself, her lips closed. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.4s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Không được khóc to, mẹ mà thức dậy thì lại lo, con bé mà nhìn thấy thì nó sợ lắm." (no subtitles)
- @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal ticking, a faint snore from upstairs, crickets. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 3 (`canh-11/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot from the side of the stove, slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The bottom of the steep tiled staircase in the dim kitchen, the clay stove glowing orange beside the basin of soaking rice.
- 3.0–7.0s: @Na tiptoes down into the kitchen and wraps her small arms around @Thu's back, and @Thu turns her wet face toward her daughter and speaks softly, her lips clearly visible.
- 7.0–10.0s: @Thu finishes speaking and closes her mouth, covering @Na's small hands with her own, while @Na keeps her cheek pressed against her mother's shoulder. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Na à, sao con lại xuống đây? Muộn rồi, con lên ngủ đi, mẹ chỉ ngâm gạo thôi mà." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: small footsteps on tiles, charcoal crackling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 4 (`canh-11/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on the girl's face beside her mother's shoulder, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Na rests her chin on @Thu's shoulder, her bright eyes wet and wide in the orange stove light.
- 3.0–7.0s: @Na speaks softly into @Thu's ear, her small hands holding tight around her mother's waist.
- 7.0–10.0s: @Na leans her forehead against @Thu's cheek and closes her eyes, holding very still. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mẹ đừng khóc nữa, bố không cần mẹ thì con với bà cần mẹ, mẹ nhé." (no subtitles)
- @Na keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal crackling, a soft sniffle. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 5 (`canh-11/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, slow arc around the stove; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu turns on the stool and cups @Na's face in both hands, wiping her daughter's tears with her thumbs.
- 3.0–7.0s: @Thu speaks to @Na with a small trembling smile, nodding firmly as her own eyes glisten.
- 7.0–10.0s: @Thu draws @Na into a tight hug, resting her chin on the girl's head, her eyes open and steady on the stove. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ừ, mẹ không khóc nữa, mẹ còn có con, có bà, mẹ phải sống cho đàng hoàng." (no subtitles)
- @Thu keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal crackling, rain easing outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 6 (`canh-11/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on the clay stove, slow tilt up to her face; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Grey charcoal embers inside a clay stove in the dark kitchen, a faint orange glow pulsing between them.
- 3.0–7.0s: @Thu kneels beside the stove and fans the coals with a woven bamboo hand fan, speaking firmly to herself as the embers flare bright orange, her face and lips lit by the glow.
- 7.0–10.0s: @Thu finishes speaking and closes her mouth, fanning steadily with her jaw set, the fierce orange flames filling the bottom of the frame and lighting her dry eyes. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cháy lên nào, sáng mai còn cả nồi xôi phải đồ, từ nay không ai bắt mình gục ngã được nữa." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: charcoal crackling and flaring, a bamboo fan swishing, a soft whoosh of air. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 1 (`canh-12/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium shot gliding beside her toward the windows; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Morning light pours through floor-to-ceiling windows onto a white marble kitchen island, a pale sofa and a vase of white orchids in an empty luxury apartment.
- 3.0–7.0s: @Vy strolls across the apartment in her crimson dress with a glowing phone pressed to her ear, speaking into it with a lazy smile, her face and red lips clearly visible.
- 7.0–10.0s: @Vy finishes speaking and closes her lips, stopping at the glass wall with the phone still at her ear, the city skyline spread out below in glossy cold light. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh ạ, căn hộ lão Tùng thuê cho em, một tháng tiền nhà bằng cả năm vợ lão bán xôi." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint city hum far below, an air conditioner whispering, heels on a polished floor. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 2 (`canh-12/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up, slow rack focus from the stick to her face; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A plastic pregnancy test stick showing two faint pink lines lies on the white marble kitchen island beside a cup of coffee.
- 3.0–7.0s: @Vy picks up the plastic pregnancy test stick showing two faint pink lines, turns it in her manicured fingers and murmurs to herself with a sly smile, her red lips clearly visible.
- 7.0–10.0s: @Vy finishes speaking and closes her lips, slipping the test stick into her small white handbag and checking her reflection in the window with a small closed smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Que này mua lại của con bạn đang bầu, hai vạch rõ thế này, đàn ông nào chả tin." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a coffee cup set down on marble, distant traffic. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 3 (`canh-12/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The marble kitchen island in cold morning light, a set of car keys and a leather wallet lying beside a coffee cup.
- 3.0–7.0s: @Vy holds out the plastic pregnancy test stick showing two faint pink lines to @Tung, her eyes shining and one hand resting on her flat stomach.
- 7.0–10.0s: @Tung stares at the test stick in her hand with his eyebrows rising, one hand going to his forehead, while @Vy watches his face with a sweet smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh ơi, mình có con rồi, bác sĩ bảo nhiều khả năng là con trai đấy anh." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the refrigerator humming, a soft gasp. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 4 (`canh-12/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on his face, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung takes the test stick from @Vy's hand and looks at it, a wide grin spreading across his face.
- 3.0–7.0s: @Tung speaks eagerly to @Vy, nodding again and again, his eyes bright.
- 7.0–10.0s: @Tung holds @Vy's hand in both of his and beams at her, while she lowers her eyes with a soft closed smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Con trai thật à em? Anh sẽ lo cho mẹ con em đầy đủ, anh hứa với em." (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the city hum, a short delighted laugh. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 5 (`canh-12/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm over-the-shoulder shot from behind him toward her, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy slides her hand out of @Tung's hands and lets her smile fade, her eyes turning serious.
- 3.0–7.0s: @Vy speaks firmly to @Tung, her voice soft but her gaze hard, one fingertip tapping the marble island.
- 7.0–10.0s: @Vy lifts her chin and waits with her arms folded, as @Tung slowly nods. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Nhưng con em không thể là con ngoài giá thú, anh phải ly hôn ngay, sang tên căn nhà cho con." (no subtitles)
- @Vy keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a fingernail tapping marble, the air conditioner humming. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 6 (`canh-12/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up two-shot, slow push-in onto her face; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung nods at once without hesitation and speaks eagerly to @Vy across the marble island, his face and lips clearly visible.
- 3.0–7.0s: @Tung finishes speaking and closes his mouth, and @Vy steps around the island and leans her head on his shoulder, her face turned toward the camera.
- 7.0–10.0s: Resting on his shoulder where he cannot see her face, @Vy lets her sweet look drop and her red lips curl slowly into a cold closed smile, her winged eyes narrowing. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–4.9s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Được, tuần này anh ly hôn, căn nhà ở phố cổ anh sang tên cho con mình luôn." (no subtitles)
- @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint city hum, a slow exhale. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 1 (`canh-13/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium shot from the kitchen toward the front door, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The ground-floor kitchen of the tube house in soft afternoon light, the big aluminum sticky-rice steamer on the gas stove and the steep tiled staircase on the right.
- 3.0–7.0s: @Vy steps in through the open front door in her crimson dress carrying a wicker basket of fruit, calling out sweetly into the house with raised eyebrows, her face and red lips clearly visible.
- 7.0–10.0s: @Vy finishes calling and closes her lips, sets the fruit basket on the wooden dining table and runs one finger along its edge, inspecting the dust with a faint smirk. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chị Thu ơi, em mang ít hoa quả sang chào chị cả, chị có nhà không ạ?" (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the alley outside, high heels on tiles, a wicker basket set down. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 2 (`canh-13/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder shot from behind the stove toward the dining table, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The wooden dining table with a wicker basket of fruit on it, the staircase and the small family altar shelf in the background.
- 3.0–7.0s: @Vy stands by the table with one hand resting on her flat stomach, smiling sweetly as she speaks to @Thu, who stands by the stove holding a dish towel.
- 7.0–10.0s: @Vy glances up at the staircase as if measuring the house, while @Thu stays rooted by the stove, her grip tightening on the towel. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Em đến xem nhà một chút, sắp tới em với con trai anh Tùng sẽ về đây ở." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a moped passing in the alley, a dripping tap. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 3 (`canh-13/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on her face, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu folds the dish towel and sets it on the stove, standing several steps away from @Vy.
- 3.0–7.0s: @Thu speaks evenly to @Vy and points toward the open front door, her arm steady and her eyes cold.
- 7.0–10.0s: @Thu keeps her arm pointed at the door with her jaw set, staying well apart from @Vy across the kitchen. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Đây là nhà của mẹ con tôi, mời cô về cho, tôi không muốn nói chuyện với cô." (no subtitles)
- @Thu keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the tap dripping, a car engine pulling into the alley outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 4 (`canh-13/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot of the bottom of the staircase, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The steep tiled staircase seen from the kitchen, the open front door bright behind it and a car's shadow sliding past the doorway outside.
- 3.0–7.0s: @Vy glances quickly at the doorway, then clutches her stomach and lowers herself onto the bottom stair by herself, with nobody near her, wailing out loud as she sits, her face and lips clearly visible.
- 7.0–10.0s: @Vy finishes crying out and closes her mouth, sitting hunched on the bottom step with one hand on her stomach and the other on the stair rail, peeking at the front door from under her lashes. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ối, đau quá, chị Thu ơi, sao chị nỡ làm thế với em, anh Tùng ơi, cứu con em với!" (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a car door closing outside, the front gate creaking open. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 5 (`canh-13/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm over-the-shoulder shot from behind her toward the doorway, slow handheld drift; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The bright front doorway of the tube house with the alley beyond, dust floating in the afternoon light.
- 3.0–7.0s: @Tung strides in through the doorway in his charcoal suit and stops short, pointing at @Thu across the kitchen and shouting at her.
- 7.0–10.0s: @Tung keeps his arm pointed at @Thu from several steps away, his face flushed, while @Thu stands motionless in the foreground by the stove with her hands at her sides. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cô làm cái gì cô ấy thế hả? Cô ấy đang mang thai con của tôi đấy!" (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the front gate clanging open, quick footsteps on tiles. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 6 (`canh-13/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on her face, slow tilt up to the shelf; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The kitchen in afternoon light, the gas stove and the sticky-rice steamer, a folded dish towel and an abandoned wicker fruit basket on the counter.
- 3.0–7.0s: @Thu stands alone beside the stove with her arms hanging at her sides and whispers to herself, her eyes moving from the empty bottom stair to the open doorway, her face and lips clearly visible.
- 7.0–10.0s: @Thu finishes whispering, closes her mouth and lifts her eyes upward, and the camera tilts up from her face to the small white home camera on the high kitchen shelf, its tiny green light blinking steadily. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Không ai tin mình cả, mình chẳng chạm vào cô ta, chỉ có trời biết, đất biết thôi." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the tap dripping, a faint electronic beep. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 1 (`canh-14/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot across the table, slow dolly across; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Morning light falls across the bare wooden dining table where a few printed pages with only faint unreadable lines of ink lie beside a cheap ballpoint pen.
- 3.0–7.0s: @Tung steps up to the table in his charcoal suit, taps the pages with one finger and speaks curtly toward the kitchen, his face and lips clearly visible.
- 7.0–10.0s: @Tung finishes speaking and closes his mouth, drops the pen onto the last page and steps back with his hands in his pockets, his eyes turned away. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Đơn ly hôn tôi soạn sẵn rồi, cô ký vào đây cho xong, đừng bắt tôi phải chờ nữa." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a moped passing outside, paper rustling, the gas stove ticking as it cools. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 2 (`canh-14/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on her face and hands, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The dining table in morning light, the pages and the ballpoint pen waiting in front of an empty low stool.
- 3.0–7.0s: @Thu sits down on the stool, signs the last page in one steady stroke and speaks calmly to @Tung, dry-eyed, her face and lips clearly visible.
- 7.0–10.0s: @Thu finishes speaking and closes her mouth, sets the pen down and squares the pages neatly with her back straight, while @Tung stands at the edge of the frame looking away. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mười hai năm dọn cơm trên cái bàn này, em ký đây, em không lấy gì, chỉ xin nuôi con Na." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a pen scratching on paper, a deep slow breath. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 3 (`canh-14/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm over-the-shoulder shot from behind her toward him, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The foot of the tiled staircase beside the table, a stack of empty cardboard boxes leaning against the wall.
- 3.0–7.0s: @Tung stands by the staircase with his hands in his suit pockets and speaks coldly down at @Thu, who stays seated at the table.
- 7.0–10.0s: @Tung picks up the signed pages, folds them into his jacket and turns his face away from @Thu. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Căn nhà này tôi xây, cô dọn đi trong tuần này, đừng để Vy phải nhìn thấy cô." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper rustling, a car horn in the alley. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 4 (`canh-14/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot toward the front door, slow pan; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The front doorway of the tube house, two packed cloth bags and a rolled straw mat waiting on the threshold.
- 3.0–7.0s: @BaNhan comes down the last stairs with an old rattan basket on her arm and her bamboo walking stick, as @Na, standing by the packed bags, looks up at her and speaks, the girl's face and lips clearly visible.
- 7.0–10.0s: @Na finishes speaking and closes her mouth, while @BaNhan walks slowly to the doorway and stands beside her granddaughter, pulling her brown cardigan tight, her chin raised. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bà ơi, bà xách làn đi đâu thế ạ? Bà cũng dọn đi với mẹ con con thật ạ?" (no subtitles)
- From 3.0s onward, @Na's face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: slow footsteps on the stairs, a walking stick tapping on tiles. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 5 (`canh-14/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on her face, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The bright doorway with the packed bags on the threshold, a strip of morning sun across the tiled floor.
- 3.0–7.0s: @BaNhan stands in the doorway leaning on her stick and speaks to @Tung without looking at him, her voice shaking but her chin high.
- 7.0–10.0s: @BaNhan turns her face toward the alley, while @Tung stands a few steps behind her with his mouth closed and his hands hanging. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mẹ đi theo con dâu, con trai tôi chết từ hôm nó bỏ vợ bỏ con rồi." (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the alley waking up, a rooster far away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 6 (`canh-14/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 28mm medium-wide high-angle shot from the stairs, slow crane down; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The empty ground floor seen from above, the bare dining table, the cold stove and the sticky-rice steamer with no steam.
- 3.0–7.0s: @Tung stands alone in the middle of the kitchen in his charcoal suit, looking slowly around at the bare walls and muttering to himself, his face and lips clearly visible.
- 7.0–10.0s: @Tung finishes speaking and closes his mouth, rooted to the spot with his hands in his pockets, the open front door bright and empty behind him. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Đi hết thì càng tốt, nhà cửa từ nay sạch sẽ, yên tĩnh, nhưng sao lại vắng thế này nhỉ?" (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: silence, a faint echo from the alley, a refrigerator humming. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 1 (`canh-15/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 24mm wide shot from the doorway, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A tiny rented room at night lit by a bare yellow bulb, a single wooden bed against the wall, packed cloth bags on the floor and rain dripping from a dark ceiling stain into an aluminum basin.
- 3.0–7.0s: @Na steps into the room close to the camera in her school clothes, hugging a small cloth bag, looks up at the dripping ceiling and calls back over her shoulder, her face and lips clearly visible.
- 7.0–10.0s: @Na finishes speaking and closes her mouth, crouching beside the aluminum basin to watch another drop land and ripple the water under the bare bulb. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mẹ ơi, phòng mình bé tí thế này à? Mưa dột cả vào chậu rồi này mẹ." (no subtitles)
- From 3.0s onward, @Na's face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain on a tin roof, water dripping into a metal basin. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 2 (`canh-15/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A tiny rented room in a crowded Hà Nội boarding alley at night: a single wooden bed, a folding table, a small barred window, a hot plate, an aluminum basin catching drips from the leaking ceiling, a bare yellow bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, slow pan following her; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The cramped room with a damp concrete floor, the big aluminum sticky-rice steamer standing beside a folding table.
- 3.0–7.0s: @Thu mops the wet floor with quick strong strokes and speaks warmly toward the doorway with a small smile, her face and lips clearly visible.
- 7.0–10.0s: @Thu finishes speaking and closes her mouth, sets the sticky-rice steamer neatly in the corner and wipes her hands on her apron, looking around the room with her chin up. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Phòng bé nhưng ấm, mẹ lau một tí là sạch ngay, coi như mình chuyển nhà thôi con ạ." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a mop on wet concrete, rain on the roof, the basin dripping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 3 (`canh-15/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm over-the-shoulder shot from behind the younger woman toward the mother, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The edge of the wooden bed under the bare bulb, a small knotted handkerchief bundle resting on the thin blanket.
- 3.0–7.0s: @BaNhan sits on the bed and holds out the small knotted handkerchief bundle to @Thu with both trembling hands, speaking softly.
- 7.0–10.0s: @BaNhan holds the bundle out toward @Thu and nods insistently, her wrinkled eyes wet. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Con ạ, mẹ còn ít vàng dành dụm, con cầm lấy mà mở một quán xôi cho tử tế." (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain on the roof, the basin dripping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 4 (`canh-15/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A tiny rented room in a crowded Hà Nội boarding alley at night: a single wooden bed, a folding table, a small barred window, a hot plate, an aluminum basin catching drips from the leaking ceiling, a bare yellow bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on the two pairs of hands, slow tilt up to her face; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu kneels beside the bed and gently folds @BaNhan's fingers back over the handkerchief bundle.
- 3.0–7.0s: @Thu speaks softly to @BaNhan, holding her mother-in-law's hands in her own rough palms.
- 7.0–10.0s: @Thu smiles through wet eyes and rests her forehead briefly against @BaNhan's knuckles. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mẹ giữ lấy mà dưỡng già, con còn đôi bàn tay, con sẽ làm lại từ đầu mẹ ạ." (no subtitles)
- @Thu keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain softening, the basin dripping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 5 (`canh-15/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot across the folding table, slow dolly-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The folding table under the bare yellow bulb, an open exercise book and a crayon drawing of three figures holding hands, with no words on the page.
- 3.0–7.0s: @Na sits at the folding table in her school clothes, touching each figure in the drawing with a red crayon and whispering to herself, her face and lips clearly visible under the yellow bulb.
- 7.0–10.0s: @Na finishes whispering and closes her mouth, smoothing the drawing flat and looking at it with a small closed-mouth smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Đây là bà, đây là mẹ, đây là con, nắm tay nhau thật chặt, không ai bỏ ai." (no subtitles)
- From 3.0s onward, @Na's face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a crayon scratching on paper, rain on the roof. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 6 (`canh-15/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A tiny rented room in a crowded Hà Nội boarding alley at night: a single wooden bed, a folding table, a small barred window, a hot plate, an aluminum basin catching drips from the leaking ceiling, a bare yellow bulb.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on her face on the mat, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Faint streetlight from the small barred window falls across a straw mat and a thin blanket on the floor of the dark room, the bulb switched off.
- 3.0–7.0s: @Thu lies down on her side on the straw mat, fully clothed, pulls the thin blanket up and whispers to herself with a faint smile, her face and lips visible in the streetlight.
- 7.0–10.0s: @Thu finishes whispering, closes her mouth and her eyes, and sinks into a deep sleep with slow even breathing, one hand resting open on the mat. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Từ nay không phải thức chờ ai về nữa, mình ngủ một giấc cho thật ngon thôi." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: light rain, slow steady breathing, a distant moped. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 1 (`canh-16/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- Extra: two workers in grey overalls carrying kitchen things out the front door
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, slow pan across the kitchen; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The ground-floor kitchen of the tube house half-emptied, the big aluminum sticky-rice steamer on the floor beside a new dark-wood bar counter, deep red velvet curtains hanging over the window.
- 3.0–7.0s: @Vy stands in the middle of the kitchen in her crimson dress, pointing one manicured finger at the steamer and speaking sharply to the two workers in grey overalls, her face and red lips clearly visible.
- 7.0–10.0s: @Vy finishes speaking and closes her lips into a smile, running her hand along the new bar counter as the two workers carry the big aluminum steamer out the front door. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Dọn hết nồi niêu của bà vợ cũ đi, nhà này giờ có quầy rượu với rèm nhung đỏ rồi." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: furniture scraping, a steamer lid clanging, high heels on tiles. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 2 (`canh-16/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm over-the-shoulder shot from behind his chair toward her, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The large white desk in the glass office, a thin stack of documents with faint unreadable lines and a gold pen laid neatly on top.
- 3.0–7.0s: @Vy leans over the desk beside @Tung's leather chair, slides the documents toward him and speaks sweetly, tapping the bottom of the page with a red fingernail, her face and lips clearly visible.
- 7.0–10.0s: @Vy finishes speaking and straightens up, smiling down at @Tung with closed lips, one hand resting lightly on the back of his chair. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh ký vào đây cho em, giấy ủy quyền thôi mà, để em lo hết giấy tờ cho con." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: papers sliding on a desk, the air conditioner humming, distant city traffic. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 3 (`canh-16/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on his face and hands, slow tilt down; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung picks up the gold pen with a relaxed grin, glancing up at @Vy.
- 3.0–7.0s: @Tung speaks lightly to @Vy as he signs page after page without reading, his pen moving fast.
- 7.0–10.0s: @Tung caps the gold pen and slides the signed stack back across the desk, leaning back in his chair with a satisfied sigh. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Em lo thì anh yên tâm, anh ký luôn, mấy cái giấy tờ này anh chả buồn đọc." (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a pen scratching quickly, pages flipping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 4 (`canh-16/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The signed documents lying on the white desk, faint unreadable lines of ink and a fresh dark scrawl at the bottom of the page.
- 3.0–7.0s: @Vy's red-nailed fingers close a slim white folder over the documents and lift it to her chest as she whispers to herself, her red lips moving clearly in the frame.
- 7.0–10.0s: @Vy finishes whispering and her red lips close and curl into a cold smile, her sharp winged eyes narrowing above the white folder. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Một chữ ký thôi, cả công ty lẫn căn nhà lão vừa đuổi vợ đi, giờ đều nằm trong tay mình." (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a folder snapping shut, the air conditioner humming. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 5 (`canh-16/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a black luxury sedan with no badge parked in a dim underground car park, the elevator doors glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up through the windshield, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A dim underground car park, a black luxury sedan with no badge parked in a row of concrete pillars, the elevator doors glowing in the distance.
- 3.0–7.0s: @Khai sits behind the wheel of the black sedan, drumming his fingers on the steering wheel and muttering to himself, his face and lips clearly visible through the windshield.
- 7.0–10.0s: @Khai finishes speaking and closes his mouth, leaning forward with his eyes on the distant elevator doors as they slide open, a sly half-smile spreading under his thin moustache. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ký mỗi tờ giấy mà đi lâu thế, lão Tùng mà nghi ngờ thì hỏng hết cả kế hoạch." (no subtitles)
- From 3.0s onward, @Khai's face and lips stay clearly visible while speaking; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: fingers drumming on leather, a distant elevator chime, an echoing car park. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 16 - Clip 6 (`canh-16/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Inside a black luxury sedan with no badge parked in a dim underground car park, the elevator doors glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot from the back seat, locked-off; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the black luxury sedan in the dim car park, the passenger door swinging open and the elevator doors glowing beyond the windshield.
- 3.0–7.0s: @Vy slides into the passenger seat holding the slim white folder, and @Khai turns to her and speaks with a sly grin.
- 7.0–10.0s: @Khai taps the white folder in her lap with one finger, while @Vy settles back in her sunglasses with a satisfied closed smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Xong rồi chứ em? Ba tháng nữa mình rút hết tiền, bay ra nước ngoài sống như vua." (no subtitles)
- From 3.0s onward, @Khai's face and lips stay clearly visible while speaking; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a car door shutting, an engine starting, an echoing car park. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 1 (`canh-17/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: A dark old-quarter street before dawn, yellow streetlamps glowing on mossy walls as warm light and thick steam spill from the small sticky-rice shop onto the empty pavement.
- 3.0–7.0s: @Thu lifts a big pot lid behind the worn wooden counter while @BaNhan steps into the lit doorway with her carved bamboo walking stick and speaks fondly to her, face and lips clearly visible.
- 7.0–10.0s: @BaNhan finishes speaking and closes her mouth, shaking her head with a soft smile, as @Thu glances up at her through the rising steam. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Sáu tháng nay ngày nào con cũng mở quán từ lúc trời còn tối, không mệt hả con?" (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing from big pots, a walking stick tapping the doorstep, roosters crowing in the alley. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 2 (`canh-17/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on Thu behind the counter, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu scoops glossy sticky rice onto a fresh banana leaf and answers @BaNhan with a gentle smile, her face and lips clearly visible in the warm steam.
- 3.0–7.0s: @Thu finishes speaking and closes her mouth, folding the banana leaf into a neat parcel with quick practiced hands.
- 7.0–10.0s: @Thu sets the parcel on the rows along the counter, her calm smile glowing gold in the steam as @BaNhan nods softly at the edge of the frame. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.9s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Không mệt đâu mẹ, quán mình chẳng có biển hiệu gì, chỉ có nồi xôi ngon, mở muộn là khách phải chờ." (no subtitles)
- @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam rushing, banana leaves rustling, a wooden spoon scraping the pot. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 3 (`canh-17/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
- Extra: a long queue of office workers and students waiting under the streetlamps, a young woman in a work blazer at its front
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium tracking shot along the queue; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The old-quarter pavement in front of the glowing shop, parked mopeds lining the curb under yellow streetlamps and the first pale blue light above the rooftops.
- 3.0–7.0s: @Na walks along the long queue carrying a tray of banana-leaf parcels, stops beside the young woman in a work blazer and speaks up to her with wide eyes, her lips clearly visible.
- 7.0–10.0s: @Na closes her mouth and grins as the young woman nods, the queue stretching behind them all the way back to the corner of the street. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Hàng dài đến tận đầu phố rồi, cô đi xe cả tiếng chỉ để mua xôi mẹ cháu thật ạ?" (no subtitles)
- From 3.0s onward, @Na's face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: shuffling footsteps, mopeds idling, steam hissing in the distance. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 4 (`canh-17/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up two-shot from table height, slow lateral slide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A low wooden table at the back of the shop piled with fresh green banana leaves, a bundle of bamboo strings and a small stool in the warm light.
- 3.0–7.0s: @BaNhan sits on the low stool folding banana leaves around sticky rice and speaks warmly to @Na, who kneels beside her wrapping a parcel with a bamboo string.
- 7.0–10.0s: @BaNhan closes her mouth with crinkled smiling eyes as @Na holds up a neatly finished parcel, both of them beaming in the warm lamplight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Buộc lạt chặt tay vào cháu, nhà mình mất nhà mất cửa, nhưng còn nhau là còn tất cả." (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: banana leaves crinkling, bamboo strings tightening, steam in the background. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 5 (`canh-17/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The worn wooden counter with an empty steaming pot and a few last banana-leaf parcels, warm light falling onto the pavement.
- 3.0–7.0s: @Thu leans over the counter and speaks warmly to a few customers holding banana-leaf parcels, tilting the empty pot to show it.
- 7.0–10.0s: @Thu presses her palms together in a small apologetic bow, smiling, as the customers nod and step back onto the pavement. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Xôi hôm nay hết sớm rồi, mai cả nhà quay lại, em để phần trước cho nhé!" (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam fading, mopeds passing, a ladle tapping the empty pot. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 17 - Clip 6 (`canh-17/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on Thu behind the counter, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu wipes her work-roughened hands on her dark-green cloth apron, looks down at them and speaks softly to herself, her face and lips clearly visible.
- 3.0–7.0s: @Thu finishes speaking and closes her mouth, turning her rough, rice-flecked palms up in front of her and studying them in the warm light.
- 7.0–10.0s: @Thu rests her hands flat on the wooden counter and lifts her face, calm and upright, her eyes bright in the rising steam and the first light of dawn. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.2s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Người ta chê đôi bàn tay này thô ráp, giờ chính nó nuôi cả bà, cả con mình đấy." (no subtitles)
- @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam settling, a distant temple bell, birds waking in the alley. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 1 (`canh-18/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium shot, slow dolly across the office; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The glass-walled director's office in cold morning light, loose papers covered in faint unreadable lines scattered across the large white desk beside the architectural model of a residential tower.
- 3.0–7.0s: @Tung strides in from the door holding his phone to his ear, its screen turned away, and speaks sharply into it, his face and lips clearly visible.
- 7.0–10.0s: @Tung finishes speaking and closes his mouth, lowering the phone and staring at the scattered papers, one roof piece of the tower model sitting crooked on its top floor. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Sao lại hủy hợp đồng? Tuần này đã ba bên hủy rồi, anh nói rõ lý do cho tôi!" (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: air conditioning hum, a phone ringing unanswered in the next room, footsteps on the carpet. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 2 (`canh-18/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The large white desk with a black leather chair, a closed laptop and a framed family photo of Thu, Tùng and Na lying face down.
- 3.0–7.0s: @Tung sits in the black leather chair, flips open the thick folder the accountant has set before him and speaks sharply up at her, his face and lips clearly visible.
- 7.0–10.0s: @Tung closes his mouth and stares at pages of faint unreadable figures, his hand frozen on the paper, as the accountant lowers her eyes. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chị nói sao? Tài khoản công ty mình chỉ còn có vài trăm nghìn đồng thôi à?" (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper sliding on the desk, the accountant's shallow breathing, the city hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 3 (`canh-18/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- Extra: a middle-aged woman accountant in a grey cardigan holding a folder
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm close-up on Tùng, slow drift; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung rises from the black leather chair with the open folder in his hand as the accountant in the grey cardigan steps back a pace.
- 3.0–7.0s: @Tung shouts across the desk toward the accountant, his face flushed and a vein standing out on his temple.
- 7.0–10.0s: @Tung drops the folder onto the desk and leans on its edge with both hands, breathing hard, as the accountant hurries out. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Tiền đâu hết rồi? Ai rút hết tiền của công ty tôi? Gọi Vy lên đây ngay!" (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the folder landing on the desk, heavy breathing, a door closing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 4 (`canh-18/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot across the desk, slow rack focus from the slips to his face; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A stack of transfer slips on the white desk in sharp focus, each covered in faint unreadable lines and the same blue ink scrawl at the bottom.
- 3.0–7.0s: Focus racks to @Tung leaning over the desk behind the slips, sliding a finger from one blue scrawl to the next as he mutters to himself, his face and lips clearly visible.
- 7.0–10.0s: @Tung closes his mouth, lets the slips drop onto the desk and slowly draws his phone from his jacket pocket. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Lệnh chuyển tiền nào cũng có chữ ký ủy quyền của Vy, người mà mình tin nhất đời." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: paper rustling, a long silence, distant traffic far below. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 5 (`canh-18/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up by the window, slow arc; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung presses the phone to his ear, its screen turned away, turns toward the floor-to-ceiling window and speaks hoarsely into it, his face and lips clearly visible.
- 3.0–7.0s: @Tung finishes speaking and closes his mouth, lowers the phone, taps its softly glowing screen turned away from the camera and lifts it back to his ear.
- 7.0–10.0s: @Tung lets the phone drop to his side and leans his forehead against the cold glass, his breath fogging the window above the grey skyline. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–4.9s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Nghe máy đi Vy, anh gọi em hai mươi cuộc rồi, sao chỉ toàn thuê bao thế này?" (no subtitles)
- @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a phone ringing out again and again, a flat automated tone, the hum of the city below. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 18 - Clip 6 (`canh-18/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: A busy Hà Nội street at dusk, rush-hour mopeds streaming past far beyond a row of parked bikes, neon shop lights flickering on above the pavement.
- 3.0–7.0s: @Tung walks slowly along the pavement in his creased charcoal-grey suit, his shirt collar askew, muttering to himself with his face and lips clearly visible.
- 7.0–10.0s: @Tung stops beside a lamppost, closes his mouth and stares blankly at the blur of distant headlights, his arms hanging loose at his sides. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Công ty mất rồi, tiền cũng mất, Vy cũng chẳng thấy đâu, giờ mình biết đi đâu đây?" (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: roaring rush-hour traffic, horns, a buzzing neon tube. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 1 (`canh-19/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 3.0–7.0s: @Tung walks into frame in his soaked suit, stops in front of the glowing window and murmurs to himself, rain running down his face and his lips clearly visible.
- 7.0–10.0s: @Tung closes his mouth and steps closer to the glass, then goes rigid, his eyes fixed on something inside the café. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Đèn quán quen của Vy vẫn sáng, gọi cả ngày không nghe máy, chắc cô ấy ngồi trong này." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steady rain on the pavement, water gurgling in a gutter, a car hissing past far away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 2 (`canh-19/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
An upscale café at night: velvet armchairs, brass lamps, marble tables, rain-streaked floor-to-ceiling windows facing the street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot past the brass lamps, slow lateral slide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A corner table of the upscale café, a marble top with two tall glasses of fruit juice, brass lamps glowing and rain streaking the window behind.
- 3.0–7.0s: @Vy sits in a velvet armchair resting her head on @Khai's shoulder as he lifts his glass toward hers and speaks to her with a sly grin, his lips clearly visible.
- 7.0–10.0s: @Khai closes his mouth and they clink glasses, @Vy smiling widely with one hand resting on her flat stomach, her small white handbag on the marble table. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cụng ly đi em, lão Tùng mất sạch cơ nghiệp rồi mà vẫn đinh ninh sắp có con trai đấy." (no subtitles)
- From 3.0s onward, @Khai's face and lips stay clearly visible while speaking; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: glasses clinking, soft rain on the window, a coffee machine hissing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 3 (`canh-19/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot through the rain, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The rain-streaked café window from outside, warm blurred light behind the glass and rain dripping from the awning edge.
- 3.0–7.0s: @Tung stands on the wet pavement facing the window, rain soaking his hair and suit, and speaks hoarsely to himself, his face and lips clearly visible.
- 7.0–10.0s: @Tung closes his mouth and stands motionless in the rain, water running down his face, his jaw clenched and his hands hanging open at his sides. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Nó tựa đầu vào vai thằng khác, cái bụng vẫn phẳng lì, thế mà bảo đang có con với mình." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain pouring, distant thunder, water dripping from an awning. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 4 (`canh-19/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm over-the-shoulder shot across the table, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The corner café table under brass lamps, two half-finished glasses of fruit juice on the marble top beside a small white handbag.
- 3.0–7.0s: @Tung stands dripping wet beside the table and speaks hoarsely down at @Vy, who stays seated in the velvet armchair an arm's length away.
- 7.0–10.0s: @Vy leans back in the armchair, crosses her legs and looks up at @Tung with a slow, unbothered smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Vy, gã này là ai? Còn đứa con của anh, em giải thích cho anh nghe đi!" (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain dripping from his clothes onto the floor, a hushed café, a cup set down on a saucer. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 5 (`canh-19/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on Vy, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy tilts her head and looks up at @Tung with a mocking half-smile, one hand resting flat on her stomach.
- 3.0–7.0s: @Vy speaks lightly and sharply, tapping her flat stomach twice with her red-nailed fingertips.
- 7.0–10.0s: @Vy lifts her glass and takes a slow sip, her feline eyes never leaving @Tung's face. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Con nào hả anh? Que thử thai em mua mười nghìn ngoài hiệu thuốc đấy, anh ngây thơ thật." (no subtitles)
- @Vy keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: ice clinking in a glass, rain on the window. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 19 - Clip 6 (`canh-19/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium two-shot, slow pan following her; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy rises from the velvet armchair, slings her small white handbag over her shoulder and speaks coolly to @Tung from an arm's length away.
- 3.0–7.0s: @Vy finishes with a cold little shrug, turns on her heel and walks toward the café door, heels clicking on the floor.
- 7.0–10.0s: @Tung stands alone and dripping beside the empty table, staring after her as the glass door swings shut. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.4s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh tưởng em yêu cái bụng phệ của anh à? Em yêu tiền của anh thôi, giờ tiền hết rồi." (no subtitles)
- @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heels clicking, the café door swinging shut, rain rushing in for a moment. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 1 (`canh-20/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium shot down the alley, slow push-in toward the gate; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A narrow rain-soaked alley at night, a single streetlamp lighting puddles and a closed steel gate with a long paper seal of faint unreadable lines pasted across it.
- 3.0–7.0s: @Tung walks up to the sealed gate in his soaked suit, stares at the paper seal and speaks hoarsely to himself, his face and lips clearly visible under the streetlamp.
- 7.0–10.0s: @Tung closes his mouth and lays one palm flat on the wet iron bars beside the seal, rain beading on the paper and dripping from the gate. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ngân hàng niêm phong nhà rồi sao? Vy đem căn nhà này đi thế chấp từ bao giờ thế này?" (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heavy rain, water rushing in a gutter, a dog barking far away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 2 (`canh-20/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up from step level, slow drift; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The worn stone doorstep below the sealed steel gate, rainwater pooling on it under the yellow streetlamp.
- 3.0–7.0s: @Tung sinks into frame onto the wet doorstep, his phone hanging loosely from one hand, and murmurs to himself with rain dripping from his hair, his face and lips clearly visible.
- 7.0–10.0s: @Tung closes his mouth and sits hunched with his forearms on his knees, staring at the dark phone in his hand. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Giờ thì chẳng còn ai để gọi nữa, vợ con, mẹ già, mình tự tay đuổi đi cả rồi." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain pattering on fabric, the gate dripping, distant thunder. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 3 (`canh-20/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung lifts the phone and wipes the rain off it with his thumb, the screen turned away from the camera, speaking quietly to himself with his face and lips clearly visible.
- 3.0–7.0s: @Tung closes his mouth and taps the phone; a pale glow lights up his wet face while the screen stays turned away from the camera.
- 7.0–10.0s: @Tung holds the phone closer, shielding it from the rain with his other hand, his eyes narrowing as his thumb scrolls. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–4.9s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cái camera bếp Thu cài cho mình ngày xưa, không biết đoạn ghi hình cũ còn lưu không." (no subtitles)
- @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain on the phone, soft taps, thunder rolling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 4 (`canh-20/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 100mm extreme close-up on his face, static; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Raindrops falling past the yellow streetlamp in a dark blur, a faint pale glow trembling in the foreground.
- 3.0–7.0s: @Tung's face fills the frame, lit only by the cold glow of the phone below the frame, his eyes tracking something small as he whispers to himself, his lips clearly visible.
- 7.0–10.0s: @Tung closes his mouth, his eyes stop moving and his breath catches, his lips trembling. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chiều hôm ấy đây rồi, Vy tự ngồi xuống cầu thang, tự ôm bụng, tự kêu lên mà." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain, a sharp intake of breath, distant thunder. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 5 (`canh-20/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up, slow pull back; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung lowers the glowing phone onto his knee, stares at the rain-soaked alley and speaks hoarsely to himself, his face and lips clearly visible.
- 3.0–7.0s: @Tung finishes speaking, closes his mouth and presses the back of his hand against it, his shoulders starting to shake under the soaked suit.
- 7.0–10.0s: @Tung bows his head over his knees on the doorstep, the phone's glow fading out beside him in the rain. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.9s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thu chưa từng chạm vào cô ta, thế mà mình quát vào mặt vợ mười hai năm, chẳng một lời xin lỗi." (no subtitles)
- @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain intensifying, a choked breath, water dripping from the gate. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 20 - Clip 6 (`canh-20/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: Grey dawn light creeps into the narrow alley as the rain eases to a fine drizzle, the streetlamp still glowing beside the sealed gate.
- 3.0–7.0s: @Tung rises into frame from the doorstep below, wipes his face with his sleeve and speaks quietly to himself with a set jaw, his face and lips clearly visible.
- 7.0–10.0s: @Tung closes his mouth, pockets his phone and walks away down the wet alley toward the brightening street, his back straight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Trời sáng rồi, phải ra đồn công an tố cáo Vy, ít ra cũng làm được một việc tử tế." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: light drizzle, footsteps on wet concrete, the first moped starting in the distance. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 1 (`canh-21/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium shot, slow crane down through the hall; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A bright modern airport departure hall, morning sun pouring through the tall glass walls onto the polished stone floor as a white airliner rolls slowly along the runway beyond.
- 3.0–7.0s: @Khai and @Vy walk into frame wearing dark sunglasses, each pulling a hard-shell suitcase, and @Khai leans toward @Vy speaking low, his lips clearly visible.
- 7.0–10.0s: @Khai closes his mouth with a sly half-smile as @Vy smirks behind her sunglasses, the two of them strolling on toward the check-in counters. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Tiền chuyển sang tài khoản nước ngoài hết chưa em? Hôm nay bay rồi, không được sót đồng nào." (no subtitles)
- From 3.0s onward, @Khai's face and lips stay clearly visible while speaking; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: airport hall echo, a distant jet engine, suitcase wheels rolling on stone. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 2 (`canh-21/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A bright modern airport departure hall: polished stone floor, check-in counters, tall glass walls, travelers with suitcases in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up two-shot tracking alongside them; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy slips her hand into @Khai's as they walk and answers him with an easy smile, her red lips clearly visible below her dark sunglasses.
- 3.0–7.0s: @Vy finishes speaking and closes her mouth, and the pair stride hand in hand across the gleaming floor with relaxed shoulders.
- 7.0–10.0s: @Vy swings her small white handbag at her side as @Khai squeezes her hand, the check-in counters drawing nearer behind them. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–4.9s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Hết rồi anh, cả công ty lẫn căn nhà của lão, giờ chỉ việc lên máy bay thôi." (no subtitles)
- @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: suitcase wheels rolling on stone, heels clicking, a soft chime echoing in the hall. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 3 (`canh-21/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium two-shot, slow backward dolly; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Khai leans his head toward @Vy as they walk, sliding his sunglasses down his nose.
- 3.0–7.0s: @Khai speaks with a sly grin, his voice low, as @Vy smirks behind her sunglasses.
- 7.0–10.0s: @Khai slides his sunglasses back up and strolls on toward the counters beside @Vy, his suitcase rolling behind him. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Qua được cửa này là mình giàu cả đời em ạ, lão Tùng giờ chắc đang ngồi khóc ở đâu đó." (no subtitles)
- @Khai keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: suitcase wheels, footsteps echoing, a distant jet engine. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 4 (`canh-21/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A bright modern airport departure hall: polished stone floor, check-in counters, tall glass walls, travelers with suitcases in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- Extra: two police officers in dark-green uniforms walking calmly toward her
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder shot onto Vy from the counter side, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The check-in counters in bright morning light, the polished stone floor stretching empty in front of them.
- 3.0–7.0s: @Vy stops short with her suitcase as the two officers walk calmly toward her, one holding up a paper with faint unreadable lines, and she murmurs to herself, her lips clearly visible.
- 7.0–10.0s: @Vy closes her mouth and slowly lowers her sunglasses, her fingers going still on the suitcase handle as the officers stop a calm step away. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Sao công an lại đứng chờ ngay quầy thủ tục, tờ giấy kia không lẽ là lệnh bắt mình?" (no subtitles)
- From 3.0s onward, @Vy's face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: suitcase wheels stopping, measured footsteps on stone, the hall falling quiet. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 5 (`canh-21/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A bright modern airport departure hall: polished stone floor, check-in counters, tall glass walls, travelers with suitcases in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Vy = Vy, 24, Tùng's glamorous new secretary; slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick; fitted crimson sleeveless midi dress, thin gold necklace, beige high heels, small white handbag with no logo.
- Extra: two police officers in dark-green uniforms walking calmly toward her
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on Vy, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Vy pulls off her sunglasses and lifts her chin at the two police officers standing a calm step away from her.
- 3.0–7.0s: @Vy speaks sharply, one hand tightening on the strap of her small white handbag as she takes a half step back.
- 7.0–10.0s: @Vy goes silent, her red lips pressed together and her eyes darting toward the exit while the officers stand still and wait. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Vy (young woman of 24, strictly standard Hà Nội Northern accent (never Southern accent), sweet honeyed soprano that turns cold and sharp, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Các anh nhầm người rồi, tôi là vợ giám đốc, các anh có biết tôi là ai không?" (no subtitles)
- @Vy keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Vy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a hushed hall, a distant chime, a heel scraping the stone floor. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 21 - Clip 6 (`canh-21/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
A bright modern airport departure hall: polished stone floor, check-in counters, tall glass walls, travelers with suitcases in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khai = Khải, 30, Vy's secret lover and partner in her scheme; lean, styled black undercut hair, thin moustache, sly half-smile; black slim-fit shirt with rolled sleeves, beige chinos, white sneakers, silver chain bracelet.
- Extra: a police officer in a dark-green uniform standing calmly a step away from him
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A stretch of polished stone floor near the counters, a hard-shell suitcase standing upright in a pool of sunlight.
- 3.0–7.0s: @Khai lets go of the suitcase handle and speaks quietly to the police officer standing calmly a step away, his sly grin gone and his lips clearly visible.
- 7.0–10.0s: @Khai closes his mouth and holds out both wrists toward the officer as a boarding pass with faint unreadable print slips from his fingers onto the cold stone floor. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Khai (man of 30, strictly standard Hà Nội Northern accent (never Southern accent), smooth lazy tenor, sly and mocking, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thôi, hết đường chạy rồi, các anh cứ làm việc đi, tôi xin tự giác đi theo." (no subtitles)
- From 3.0s onward, @Khai's face and lips stay clearly visible while speaking; after the last word @Khai closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the suitcase settling on its wheels, a hushed hall, paper landing on stone. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 1 (`canh-22/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up from the far end of the pavement, slow rack focus from the glowing shop to his face; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The old-quarter street before dawn, the sticky-rice shop glowing soft and warm at the far end of a dark wet pavement, steam rising into the lamplight through a light drizzle.
- 3.0–7.0s: @Tung steps into the foreground, gaunt in a creased rain-stained suit, and focus racks to his hollow face as he murmurs to himself, his lips clearly visible.
- 7.0–10.0s: @Tung closes his mouth and stands still in the drizzle, his sunken eyes fixed on the warm light of the distant shop. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Quán của Thu đây rồi, mình còn mặt mũi nào mà xếp hàng mua xôi của cô ấy nữa." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: light drizzle, steam hissing far away, a moped passing in the distance. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 2 (`canh-22/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- 0.0–3.0s: The worn wooden counter of the shop, banana-leaf parcels stacked beside a steaming pot under a warm bulb.
- 3.0–7.0s: @Thu looks up from wrapping a parcel as @Tung steps up to the counter in his creased suit, and she speaks to him in a low, steady voice, her lips clearly visible.
- 7.0–10.0s: @Thu closes her mouth and they look at each other across the counter in silence, the steam drifting between them. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Anh Tùng? Sao anh gầy rộc thế này, quần áo nhàu nát, anh đứng ngoài ấy từ bao giờ?" (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, drizzle on the awning, a parcel set down on wood. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 3 (`canh-22/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on Tùng over Thu's shoulder, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung rests both hands on the edge of the wooden counter, his eyes red-rimmed and wet.
- 3.0–7.0s: @Tung speaks to @Thu in a cracked, pleading voice, leaning toward her across the counter.
- 7.0–10.0s: @Tung's voice gives out and he lowers his gaze to the steaming pot, his hands still clinging to the counter edge. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thu ơi, anh sai rồi, anh mù quáng, em cho anh về với mẹ con em được không?" (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam, drizzle, his unsteady breathing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 4 (`canh-22/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm over-the-shoulder shot onto Thu, static; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu wraps a fresh scoop of hot sticky rice in a banana leaf, ties it with a bamboo string and begins to speak as she holds it out across the counter.
- 3.0–7.0s: @Thu speaks to @Tung calmly and evenly, setting the warm banana-leaf parcel into his open hands without letting her fingers linger.
- 7.0–10.0s: @Thu straightens behind the counter with her hands folded on her apron, her face steady and her eyes dry. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–4.7s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Gói xôi này em mời anh, còn cơm nhà, chính anh đã tự tay bỏ đi rồi." (no subtitles)
- @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: banana leaf crinkling, steam hissing, drizzle. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 5 (`canh-22/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium low-angle shot from the pavement, slow crane down; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The wet pavement in front of the shop glistening under warm light spilling from the counter, steam drifting over the curb.
- 3.0–7.0s: @Tung sinks to his knees on the wet pavement, holding the warm banana-leaf parcel against his chest, and speaks hoarsely to it, his face and lips clearly visible.
- 7.0–10.0s: @Tung closes his mouth and bows his head over the parcel, tears dropping onto the green banana leaf as the drizzle falls around him. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Xôi vẫn nóng như ngày xưa em đồ cho anh, thế mà anh từng chê xôi với chả xôi." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: drizzle, knees meeting wet concrete, a muffled sob. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 22 - Clip 6 (`canh-22/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up beside the steaming pot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The warm interior of the shop behind the counter, big pots steaming and banana leaves stacked on a shelf.
- 3.0–7.0s: @Thu walks back from the counter to the steaming pot without looking back and speaks softly to herself, her eyes wet but steady and her lips clearly visible.
- 7.0–10.0s: @Thu closes her mouth and lifts the lid of the big pot in a cloud of golden steam, her face calm as she gets back to work. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Thương thì vẫn còn thương, nhưng giờ mình đã học được cách thương lấy chính mình rồi." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pot lid lifting, a rush of steam, rice being stirred. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 1 (`canh-23/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Evening on a narrow wooden staircase leading up to a closed door above the sticky-rice shop, warm light under the door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot from the top of the stairs, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A narrow wooden staircase climbing to a closed door, a thin strip of warm light glowing underneath it.
- 3.0–7.0s: @Tung climbs the last steps, stops in front of the door and whispers to himself, his face half lit by the light under the door and his lips clearly visible.
- 7.0–10.0s: @Tung closes his mouth and lifts one hand to knock, but it hovers just short of the wood and slowly drops back to his side. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mẹ ở ngay sau cánh cửa này, mà mình chẳng dám gõ, mẹ còn nhận đứa con bất hiếu này không?" (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: creaking wooden steps, a moped passing in the street below. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 2 (`canh-23/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Evening in a small cozy room above the sticky-rice shop: a low wooden bed, a family altar with incense, a window over the old-quarter street, a warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide shot from inside the room toward the door, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The cozy room above the shop lit by a warm lamp, incense smoke curling from the small family altar beside the window.
- 3.0–7.0s: @BaNhan opens the door leaning on her carved bamboo walking stick, finds @Tung on the threshold and speaks to him with a hard, tired face.
- 7.0–10.0s: @BaNhan keeps one hand on the door frame, blocking the way in, while @Tung stands with his head lowered on the threshold. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mày đến đây làm gì? Mẹ già rồi, không còn gì cho mày lấy nữa đâu con." (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the door creaking open, a walking stick tapping the floor, faint street noise. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 3 (`canh-23/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on Tùng, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung lifts his red-rimmed eyes to @BaNhan from the threshold, his hands empty and open at his sides.
- 3.0–7.0s: @Tung speaks to his mother in a low, breaking voice, his chin trembling.
- 7.0–10.0s: @Tung falls quiet and bows his head deeply, waiting, the warm lamplight catching the stubble on his jaw. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mẹ ơi, con không lấy gì nữa, con chỉ xin mẹ cho con được làm người tử tế lại." (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the lamp humming softly, a moped passing below. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 4 (`canh-23/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Evening in a small cozy room above the sticky-rice shop: a low wooden bed, a family altar with incense, a window over the old-quarter street, a warm lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, static; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @BaNhan studies @Tung's bowed head for a long moment, both hands folded on top of her bamboo walking stick.
- 3.0–7.0s: @BaNhan speaks firmly and slowly to @Tung, tapping the stick once on the floor at the end of her words.
- 7.0–10.0s: @Tung nods without lifting his head as @BaNhan presses her lips into a thin, trembling line. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Tử tế thì phải làm cả đời, mai con ra quán rửa bát, làm thuê cho con Thu đi." (no subtitles)
- @BaNhan keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the stick tapping on wood, the lamp's soft hum, a quiet street below. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 5 (`canh-23/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 85mm close-up on Tùng, slow tilt down; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung lifts his wet eyes to @BaNhan on the threshold and answers her in a low, steady voice, his chin trembling and his face and lips clearly visible.
- 3.0–7.0s: @Tung finishes speaking and closes his mouth, then bows his head very low before his mother, his eyes closing.
- 7.0–10.0s: A single tear slides down @Tung's stubbled cheek and drops onto the worn floorboards as he stays bowed in the warm lamplight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.2s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Vâng, con nghe mẹ, bao nhiêu năm con cãi mẹ rồi, từ nay mẹ bảo gì con cũng làm." (no subtitles)
- @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a deep unsteady breath, the lamp hum, silence. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 23 - Clip 6 (`canh-23/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium shot inside the room, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the cozy room, the small family altar glows with incense beside the window over the lit old-quarter street.
- 3.0–7.0s: @BaNhan closes the wooden door slowly, leans her back against it with both hands on her bamboo walking stick and murmurs to herself, her lips clearly visible.
- 7.0–10.0s: @BaNhan closes her mouth, lifts the cuff of her brown knitted cardigan and dabs her eyes, her wrinkled face softening in the warm lamplight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Nó dại thì nó chịu, nhưng dù sao nó vẫn là đứa con mình mang nặng đẻ đau." (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the door latch clicking, a soft sniff, incense crackling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 1 (`canh-24/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Afternoon in a primary school hall: a small stage with paper flower decorations and colorful bunting, rows of plastic chairs filled with parents.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- Extra: rows of parents seen from behind in plastic chairs
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot from the back of the hall, slow crane down; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Colorful bunting and paper flowers strung high across a bright primary school hall in the afternoon, the small decorated stage glowing at the far end.
- 3.0–7.0s: @Tung steps into the aisle at the back of the hall behind rows of parents in plastic chairs and murmurs to himself, his face and lips clearly visible.
- 7.0–10.0s: @Tung closes his mouth and stands still with his eyes glistening, gazing over the rows of parents toward the stage. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Hội trường chật kín phụ huynh thế này, vậy mà chín năm nay mình chưa đến xem con lần nào." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: scattered applause, chairs scraping, a small drum tapping offstage. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 2 (`canh-24/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Afternoon in a primary school hall: a small stage with paper flower decorations and colorful bunting, rows of plastic chairs filled with parents.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up from the foot of the stage, slow tracking; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The small stage framed with paper flowers and colorful bunting, warm afternoon light falling across its empty wooden boards.
- 3.0–7.0s: @Na marches to the front edge of the stage beating a small red drum, pauses and whispers to herself while scanning the rows of parents below, her lips clearly visible.
- 7.0–10.0s: @Na closes her mouth and starts drumming again, her eyes still searching the rows of chairs. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bố có đến không nhỉ? Mẹ bảo hôm nay bố đến mà, sao con tìm mãi chẳng thấy đâu?" (no subtitles)
- From 3.0s onward, @Na's face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a small drum beating a steady march, scattered applause. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 3 (`canh-24/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 50mm medium two-shot from the side, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The last row of plastic chairs at the back of the hall, warm light from the high windows falling across empty seats.
- 3.0–7.0s: @Tung sits stiffly beside @Thu in the last row as @Thu speaks softly to him with her eyes on the stage, her hands folded in her lap and her lips clearly visible.
- 7.0–10.0s: @Thu closes her mouth with a quiet smile as @Tung lifts one hand and waves toward the stage, his eyes glistening. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Con bé tìm anh suốt từ nãy đấy, anh giơ tay vẫy đi cho con nhìn thấy bố." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the little drum from the stage, applause swelling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 4 (`canh-24/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm wide two-shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A quiet backstage corner of the school hall, paper flowers and folded bunting piled on a chair in soft afternoon light.
- 3.0–7.0s: @Na runs into frame with her small red drum and stops in front of @Tung, looking up at him and speaking breathlessly.
- 7.0–10.0s: @Na beams up at @Tung, still holding her drumsticks, while he stands before her with his hands at his sides. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bố đến thật rồi! Bố ơi, lần sau bố đến sớm hơn để ngồi hàng đầu nhé." (no subtitles)
- From 3.0s onward, @Na's face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: distant applause from the hall, quick small footsteps, the drum bumping against her hip. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 5 (`canh-24/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Backstage corner of the school hall after the show, paper decorations, soft afternoon light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot from child height, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Tung kneels down to @Na's eye level on the backstage floor, his creased suit trousers touching the boards.
- 3.0–7.0s: @Tung speaks softly and earnestly to @Na, holding up his little finger toward her.
- 7.0–10.0s: @Na hooks her little finger around @Tung's and they hold the pinky promise between them, both smiling. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bố hứa, từ nay buổi diễn nào của con, bố cũng đến sớm nhất, ngồi hàng đầu tiên." (no subtitles)
- @Tung keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: faint applause from the hall, paper decorations rustling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 24 - Clip 6 (`canh-24/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Backstage corner of the school hall after the show, paper decorations, soft afternoon light.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on Thu in the doorway, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A doorway at the edge of the backstage corner, soft afternoon light and a string of paper flowers hanging across it.
- 3.0–7.0s: @Thu steps into the doorway with her hands folded in front of her, watching quietly, and murmurs to herself, her lips clearly visible.
- 7.0–10.0s: @Thu closes her mouth, her eyes shining, and a small smile settles on her face as she lets out a long, quiet breath. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mình tha thứ không phải để quay lại với anh ấy, mà để con mình còn có bố." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft applause fading, a breeze through the paper flowers. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 1 (`canh-25/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

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
- Framing & motion: 35mm medium shot from the street, slow push-in to the doorway; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The old-quarter street at first light, the sticky-rice shop's warm light spilling across the pavement and thick steam billowing from a row of big pots behind the worn wooden counter.
- 3.0–7.0s: @Thu lifts a steamer lid behind the counter as @BaNhan steps up beside it with her bamboo walking stick and speaks fondly to her, her lips clearly visible.
- 7.0–10.0s: @BaNhan closes her mouth and shakes her head with a smile while @Thu turns the rice, the first gold light of sunrise touching the rooftops above the shop. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @BaNhan (old woman of 70, strictly standard Hà Nội Northern accent (never Southern accent), frail raspy voice, trembling but firm, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mới một năm đã ba cửa hàng, sao con còn tự tay đồ mẻ xôi đầu cho mệt hả con?" (no subtitles)
- From 3.0s onward, @BaNhan's face and lips stay clearly visible while speaking; after the last word @BaNhan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam roaring, birds waking, a walking stick tapping the floor. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 2 (`canh-25/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @BaNhan = Bà Nhàn, 70, Tùng's mother who lives with Thu; small and thin, white hair in a neat low bun, kind deeply wrinkled face; brown knitted cardigan over a grey blouse, black trousers, cloth slippers, carved bamboo walking stick.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on Thu at the steamer, slow arc; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu turns the glossy sticky rice with a wooden paddle and answers @BaNhan with a calm smile, her rough hands moving with easy confidence and her lips clearly visible.
- 3.0–7.0s: @Thu finishes speaking and closes her mouth, then straightens and looks out at the street through the rising steam, her eyes bright.
- 7.0–10.0s: @Thu's calm face glows in the golden steam of the first sunlight while @BaNhan nods softly at the edge of the frame. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.2s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mẻ đầu là mẻ của nhà mình mẹ ạ, tay con vẫn chai, nhưng lòng con giờ nhẹ lắm." (no subtitles)
- @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam hissing, the wooden paddle scraping, sparrows chirping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 3 (`canh-25/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Tung = Tùng, 37, Thu's husband, newly rich construction company director; tall, slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes; tailored charcoal-grey suit, white shirt open at the collar, gold wristwatch, polished black shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot in the back corner, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: A corner at the back of the shop, a big plastic basin of soapy water and a tall stack of bowls on a low stool.
- 3.0–7.0s: @Tung sits on a low stool with his shirt sleeves rolled up, washing a bowl in the soapy basin and murmuring to himself, his face and lips clearly visible.
- 7.0–10.0s: @Tung closes his mouth, sets the clean bowl on the stack and glances toward the front of the shop with a quiet, humble look. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Tung (man of 37, strictly standard Hà Nội Northern accent (never Southern accent), deep confident baritone, impatient and cold, speaking at a brisk, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Làm thuê cho vợ cũ cũng được, mỗi cái bát rửa sạch là trả bớt một chút nợ ân tình." (no subtitles)
- From 3.0s onward, @Tung's face and lips stay clearly visible while speaking; after the last word @Tung closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water sloshing, bowls clinking, steam in the background. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 4 (`canh-25/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide two-shot by the counter, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The front counter of the shop in golden morning light, a small stack of banana-leaf parcels and bamboo strings beside a steaming pot.
- 3.0–7.0s: @Na in her school uniform hops onto a stool beside @Thu at the counter and looks up at her mother, speaking earnestly.
- 7.0–10.0s: @Na rests her chin on her hands on the counter, gazing up at @Thu, as @Thu turns toward her with a soft smile. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Na (girl of 9, strictly standard Hà Nội Northern accent (never Southern accent), high clear child's voice, earnest, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Mẹ ơi, sau này lớn lên con muốn giỏi giang như mẹ, không cần dựa vào ai cả." (no subtitles)
- From 3.0s onward, @Na's face and lips stay clearly visible while speaking; after the last word @Na closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning street sounds, steam, a stool scraping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 5 (`canh-25/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Thu wipes her hands on her dark-green apron and tucks a loose strand of hair behind @Na's ear.
- 3.0–7.0s: @Thu speaks gently and firmly to @Na, her eyes steady on her daughter's face.
- 7.0–10.0s: @Na nods hard and @Thu hands her a warm banana-leaf parcel for school, both of them smiling in the golden light. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Con cứ sống tử tế, chăm chỉ, ai bỏ con mà đi thì người thiệt là họ, không phải con." (no subtitles)
- @Thu keeps the mouth closed until 3.0s, then the face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steam, a banana leaf crinkling, birds outside. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 25 - Clip 6 (`canh-25/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese family melodrama film set in Hà Nội today; warm natural grade with soft golden kitchen light, muted old-quarter ochres, cool blue-grey dawn and rain, glossy cold tones for the wealthy world, natural skin texture, subtle 35mm film grain, shallow depth of field.

[LIGHTING]
Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.

[LOCATION]
Sunrise over the tiled roofs of Hà Nội's old quarter seen from a low drone: golden light, steam rising from the open doorway of a small sticky-rice shop on a corner street.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Thu = Thu, 34, hardworking wife who sells sticky rice at dawn; slim, lightly sun-tanned, long black hair in a low loose bun, gentle tired eyes, no makeup, work-roughened hands; faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, dark-green cloth apron, plastic sandals.
- @Na = Na, 9, Thu and Tùng's daughter; small, round face, bright dark eyes, black hair in two short pigtails with red hair ties; white short-sleeve school shirt, navy pleated skirt, red scarf knotted at the neck, white canvas shoes.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm low aerial drone shot, slow rising pull-back from the shop doorway over the rooftops; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Low aerial view of a small corner shop in Hà Nội's old quarter at sunrise, a column of white steam rising from its empty golden doorway.
- 3.0–7.0s: @Thu steps into the doorway holding @Na's hand, the camera still low in front of them, and speaks softly to @Na while looking out at the sunrise, her face and lips clearly visible.
- 7.0–10.0s: @Thu closes her mouth and smiles as the camera rises over a sea of mossy tiled roofs, mother and daughter small in the glowing doorway beneath a wide golden sky. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Thu (woman of 34, strictly standard Hà Nội Northern accent (never Southern accent), soft warm mezzo, gentle but firm, speaking at a brisk, fluent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Người ta có thể đi tìm hương lạ, nhưng vợ tào khang thì cả đời chỉ có một thôi con ạ." (no subtitles)
- From 3.0s onward, @Thu's face and lips stay clearly visible while speaking; after the last word @Thu closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft morning wind, distant temple bells, the city waking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```
