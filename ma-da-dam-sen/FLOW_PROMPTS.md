# Ma Da Đầm Sen: Lời Nguyền Tháng Bảy — Bộ 90 Prompt Google Flow Omni (15 Cảnh × 6 Clips × 10s)

- **Giọng Người Dẫn Chuyện (cố định cả 90 clip):** Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; đọc nhanh liên thanh như oan-thai-doi-me, ~4.0 âm tiết/giây, liền một hơi, không ngắt giữa câu.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 90 clips × 10s — 69 clip VO + 21 clip thoại; lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 20 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 58 clip ảnh nhân vật (Ingredients), 12 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** clip VO được tăng tốc giọng thêm 1.18x khi tải về (`FLOWKIT_VOICE_TEMPO` mặc định 1.18, đặt 1.0 để tắt), giữ nguyên khung hình 10s; clip lip-sync không bao giờ bị tăng tốc để khớp khẩu hình.
- **Màu phim & ánh sáng:** Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py ma-da-dam-sen` sinh lại toàn bộ clip, README, kịch bản.

---

## Cảnh 01 - Clip 1 (`canh-01/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Dusk in the seventh lunar month: a narrow earthen embankment path along a vast lotus pond at the edge of a Northern Vietnamese village, tall lotus leaves, a bamboo hedge and tiled roofs in the distance.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 24mm aerial drone slow descending glide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: High aerial view of a vast lotus pond at dusk, thousands of round lotus leaves rippling in a cold wind beside a small village of tiled roofs.
- 3.0–7.0s: The drone glides low over the dark water between pink lotus flowers as the last orange light fades and mist rises from the surface.
- 7.0–10.0s: The camera settles above a narrow earthen embankment path that runs along the pond toward the village gate. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Làng Hạ Liên có đầm sen đẹp nhất vùng, nhưng cứ vào tháng bảy âm lịch, đầm lại đòi đúng một mạng người." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind sweeping across lotus leaves, frogs croaking, a distant temple bell. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 2 (`canh-01/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Dusk in the seventh lunar month: a narrow earthen embankment path along a vast lotus pond at the edge of a Northern Vietnamese village, tall lotus leaves, a bamboo hedge and tiled roofs in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm stabilized gimbal side-tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Side-tracking view along the narrow earthen embankment path beside the vast lotus pond at dusk, tall lotus leaves swaying in the fading light with no person in the opening frames.
- 3.0–7.0s: @Ngan enters the frame walking briskly along the embankment path pulling a small wheeled suitcase, glancing at the dark water as her free hand tightens on her cloth shoulder bag.
- 7.0–10.0s: @Ngan slows her steps as a cold gust bends the tall lotus leaves toward the path. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngân, cô giáo trẻ dạy ở thành phố, bỏ dở kỳ nghỉ hè để về quê vì bà nội gọi điện, giọng run như sắp khóc." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: suitcase wheels rattling on dry earth, wind through lotus leaves. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 3 (`canh-01/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Dusk in the seventh lunar month: a narrow earthen embankment path along a vast lotus pond at the edge of a Northern Vietnamese village, tall lotus leaves, a bamboo hedge and tiled roofs in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @CoTham = the mysterious young woman of the lotus pond from thirty years ago: pale wet skin, long soaked black hair with lotus stems, dark sorrowful eyes; soaked plain white Northern village blouse and black trousers, barefoot.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm telephoto locked-off shot over the shoulder; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Wide view across the misty lotus pond at dusk, dense green lotus leaves swaying over dark water.
- 3.0–7.0s: Far out in the middle of the lotus pond, @CoTham stands waist-deep in the dark water among tall lotus stems, her long wet black hair hanging over her face.
- 7.0–10.0s: @CoTham stands motionless in the misty water far from the bank, facing toward the shore. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Giữa đầm sen mịt mù sương, có một cô gái áo trắng đứng ngập nước đến ngang hông, im lìm nhìn về phía cô." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a low wind, water lapping, the croaking of frogs suddenly stopping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 4 (`canh-01/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Dusk in the seventh lunar month: a narrow earthen embankment path along a vast lotus pond at the edge of a Northern Vietnamese village, tall lotus leaves, a bamboo hedge and tiled roofs in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: The narrow dirt embankment road beside the misty lotus pond at dusk, lotus leaves rustling in the breeze.
- 3.0–7.0s: @Ngan stands on the dirt embankment beside her suitcase, cupping one hand to her mouth and calling out toward the middle of the pond.
- 7.0–10.0s: @Ngan lowers her hand and peers anxiously across the darkening water. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Ngan (woman of 26, strictly standard Hà Nội strictly standard Hà Nội Northern accent (never Southern accent) (never Southern accent), clear warm mezzo, steady but breathless with fear, speaking at a brisk, urgent, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Này em ơi, trời tối rồi, sao còn đứng giữa đầm thế kia? Lên bờ đi, nguy hiểm lắm!" (no subtitles)
- From 3.0s onward, @Ngan's face and lips stay clearly visible while speaking; after the last word @Ngan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind over the water, frogs silent, a faint ripple. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 5 (`canh-01/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Dusk in the seventh lunar month: a narrow earthen embankment path along a vast lotus pond at the edge of a Northern Vietnamese village, tall lotus leaves, a bamboo hedge and tiled roofs in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm slow rack focus from the face to the pond; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Ngan stares out at the pond, her eyes widening.
- 3.0–7.0s: The focus shifts past her shoulder to the empty spot among the lotus leaves where slow rings of ripples spread across the black water.
- 7.0–10.0s: A single pink lotus flower slowly folds its petals closed as the ripples fade. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Chớp mắt một cái, bóng trắng biến mất, chỉ còn những vòng nước loang dần và một bông sen đang khép cánh lại." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: faint water dripping, a soft hollow plop, then silence. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 01 - Clip 6 (`canh-01/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Dusk in the seventh lunar month: a narrow earthen embankment path along a vast lotus pond at the edge of a Northern Vietnamese village, tall lotus leaves, a bamboo hedge and tiled roofs in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm low-angle tracking shot along the path; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Ngan turns back toward the embankment path ahead.
- 3.0–7.0s: Low on the dry earthen path, a trail of wet bare footprints glistens in the dusk, leading away from the pond toward the village.
- 7.0–10.0s: @Ngan grips her suitcase handle, staring down at the dark wet prints as the camera holds low on the path. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Và khi cô quay lại, trên con đường đất khô ráo phía trước, một hàng dấu chân trần ướt sũng đang dẫn thẳng về làng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a cold wind, water dripping from lotus leaves, quick shallow breathing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 1 (`canh-02/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Evening: inside Bà Hạnh's old three-room tiled house — a low wooden dining tray on a bamboo mat, an ancestral altar with incense and an oil lamp, wooden doors open to a brick yard and the black lotus pond beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Slow push-in toward the open wooden doorway of the old three-room tiled house at evening, warm amber oil-lamp light glowing against the dark brick yard.
- 3.0–7.0s: In the dim doorway, @BaHanh holds a small oil lamp as @Ngan steps inside with her suitcase; @BaHanh takes @Ngan's hand and glances past her toward the dark pond.
- 7.0–10.0s: @BaHanh turns to the ancestral altar, lifting three lit incense sticks toward the open door. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bà Hạnh ngoài bảy mươi, sống với đứa cháu trai út, và từ đầu tháng bảy, đêm nào bà cũng thắp hương ra phía đầm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets, the crackle of the oil lamp wick, a dog barking far away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 2 (`canh-02/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Evening: inside Bà Hạnh's old three-room tiled house — a low wooden dining tray on a bamboo mat, an ancestral altar with incense and an oil lamp, wooden doors open to a brick yard and the black lotus pond beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Over @Ngan's shoulder, @BaHanh speaks close to her granddaughter, the oil lamp lighting her deep-lined face.
- 3.0–7.0s: @BaHanh squeezes @Ngan's wrist, her eyes darting toward the open door.
- 7.0–10.0s: @BaHanh falls silent, her mouth closing, prayer beads still in her fingers. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.8s, spoken on camera by @BaHanh (old woman of 74, strictly standard Hà Nội Northern accent (never Southern accent), soft raspy voice trembling with worry, speaking at a brisk, urgent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Con về là bà mừng rồi. Nhớ lời bà, tháng bảy này tối đến tuyệt đối không được bén mảng ra gần đầm sen." (no subtitles)
- @BaHanh's face and lips stay clearly visible while speaking; after the last word @BaHanh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: incense crackling, crickets, wind moving the wooden door. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 3 (`canh-02/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Evening: inside Bà Hạnh's old three-room tiled house — a low wooden dining tray on a bamboo mat, an ancestral altar with incense and an oil lamp, wooden doors open to a brick yard and the black lotus pond beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm wide static shot of the dining mat; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Wide static view of the woven bamboo mat and low wooden dining tray with steaming bowls under warm oil-lamp light inside the quiet old house.
- 3.0–7.0s: The camera frames @Khoi sitting cross-legged at the low dining tray, grinning toward his sister off-frame as he scoops rice into his bowl with a slight tremor in his hand.
- 7.0–10.0s: @Khoi's smile fades as he sets the chopsticks down and rubs the dark shadows under his eyes. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Khôi, cậu em mười chín tuổi, cười xòa bảo bà lẩm cẩm, nhưng cả tuần nay đêm nào cậu cũng mơ thấy mình đang chìm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: chopsticks tapping bowls, crickets outside, a soft laugh. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 4 (`canh-02/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Evening: inside Bà Hạnh's old three-room tiled house — a low wooden dining tray on a bamboo mat, an ancestral altar with incense and an oil lamp, wooden doors open to a brick yard and the black lotus pond beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium close-up, static; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Medium close-up of @Khoi talking with a lopsided grin, chopsticks in hand.
- 3.0–7.0s: @Khoi shrugs, still talking, though his eyes flick toward the dark doorway behind his sister.
- 7.0–10.0s: @Khoi looks down at his bowl, his grin gone. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.2s, spoken on camera by @Khoi (young man of 19, strictly standard Hà Nội strictly standard Hà Nội Northern accent (never Southern accent) (never Southern accent), light tenor, shaky and breathless, speaking at a brisk, urgent, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chị đừng tin bà, chuyện ma da bắt người chỉ là chuyện người lớn dọa trẻ con cho khỏi đi tắm đầm thôi." (no subtitles)
- @Khoi's face and lips stay clearly visible while speaking; after the last word @Khoi closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets, a moth tapping against the oil lamp. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 5 (`canh-02/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Evening: inside Bà Hạnh's old three-room tiled house — a low wooden dining tray on a bamboo mat, an ancestral altar with incense and an oil lamp, wooden doors open to a brick yard and the black lotus pond beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 100mm macro insert shot, slow tilt; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Extreme close-up of @Khoi's bare ankle resting on the bamboo mat in the lamplight.
- 3.0–7.0s: The camera slowly tilts along the ankle, revealing a dark purple bruise shaped like five long fingers wrapped around the skin.
- 7.0–10.0s: A single drop of water falls from the ankle onto the mat. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngân để ý thấy cổ chân Khôi có một vệt bầm tím, hằn rõ như vết ngón tay ai đó vừa nắm chặt." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a slow drip, crickets, a sudden hush. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 02 - Clip 6 (`canh-02/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Evening: inside Bà Hạnh's old three-room tiled house — a low wooden dining tray on a bamboo mat, an ancestral altar with incense and an oil lamp, wooden doors open to a brick yard and the black lotus pond beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm slow pull-back from the altar to the open door; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Slow pull-back from the ancestral altar where incense smoke curls upward in the warm oil-lamp glow toward the open wooden doorway.
- 3.0–7.0s: @BaHanh steps up to the altar with prayer beads in her fingers, lights three incense sticks with trembling hands and turns toward the open doorway.
- 7.0–10.0s: The camera settles framing @BaHanh in the doorway as incense smoke drifts out toward the dark pond. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bà Hạnh nhìn vết bầm, mặt cắt không còn giọt máu, rồi lặng lẽ châm thêm ba nén hương hướng ra phía đầm sen." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: incense crackle, wind, a distant splash from the pond. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 1 (`canh-03/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Deep night: a back bedroom with a mosquito-net bed and a barred wooden window facing the lotus pond, a single blue shaft of moonlight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm static medium shot through the mosquito net; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Static medium view of the dark back bedroom at night, a single shaft of cold blue moonlight falling through the barred wooden window onto the white mosquito net.
- 3.0–7.0s: Through the white mosquito net, @Khoi lies on the bed; his eyes open suddenly and he lifts his head toward the barred window, listening.
- 7.0–10.0s: @Khoi sits up slowly inside the mosquito net, his face turned toward the moonlit window. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Nửa đêm, Khôi choàng tỉnh vì nghe ngoài đầm có giọng con gái gọi tên mình, ngọt ngào và ướt át như vừa ngoi lên." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint distant girl's voice humming over water, crickets, the creak of the bed. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 2 (`canh-03/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Deep night: the black lotus pond under cold moonlight, mist drifting between the leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @CoTham = the mysterious young woman of the lotus pond from thirty years ago: pale wet skin, long soaked black hair with lotus stems, dark sorrowful eyes; soaked plain white Northern village blouse and black trousers, barefoot.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm telephoto locked-off shot across the pond; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Telephoto view across the misty lotus pond under cold moonlight, silver ripples moving gently between dark lotus leaves with no person in the opening frames.
- 3.0–7.0s: Among the tall lotus stems, @CoTham appears waist-deep in the water, lifting her pale face toward the house and whispering softly.
- 7.0–10.0s: @CoTham extends one pale hand palm-up toward the shore as mist drifts past. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.6s, spoken on camera by @CoTham (young woman's cold breathy whisper, strictly standard Hà Nội Northern accent (never Southern accent), faint watery echo, speaking at a brisk pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Khôi ơi, dưới đầm mát lắm, xuống đây với em đi. Em đợi anh lâu lắm rồi, lạnh lắm Khôi ơi." (no subtitles)
- From 3.0s onward, @CoTham's face and lips stay clearly visible while speaking; after the last word @CoTham closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water dripping, a breathy echoing whisper, frogs falling silent. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 3 (`canh-03/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Deep night: the moonlit brick yard of the old house leading down to the edge of the black lotus pond, mist on the water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm handheld follow shot from behind; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Handheld view of the moonlit brick yard outside the open wooden doorway of the old house, mist curling up from the lotus pond at the edge of the yard.
- 3.0–7.0s: @Khoi steps barefoot out of the dark doorway into the moonlit brick yard, walking with slow stiff steps straight toward the pond.
- 7.0–10.0s: @Khoi reaches the wet grass at the water's edge under the cold moonlight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Như bị ai giật dây, Khôi bước ra sân, chân trần lạnh ngắt, mắt mở trừng trừng mà không hề chớp lấy một lần." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: bare feet on cold bricks, crickets, the whisper of lotus leaves. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 4 (`canh-03/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Deep night: the moonlit brick yard of the old house leading down to the edge of the black lotus pond, mist on the water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide shot from the water looking back at the shore; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Wide view from the misty lotus pond looking back toward the moonlit grassy bank and brick yard, round lotus leaves swaying on the dark water.
- 3.0–7.0s: @Khoi stands knee-deep among the lotus leaves as @Ngan runs barefoot down the moonlit bank and splashes into the shallows behind him.
- 7.0–10.0s: @Ngan wraps both arms around @Khoi's shoulders from behind, holding him steady in the shallow water. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngân tỉnh giấc vì tiếng cửa kẽo kẹt, cô lao ra kịp lúc nước đầm đã ngập đến đầu gối em trai mình." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: splashing water, rapid breathing, frogs croaking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 5 (`canh-03/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Deep night: the moonlit brick yard of the old house leading down to the edge of the black lotus pond, mist on the water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm handheld medium two-shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Knee-deep in the water, @Ngan turns @Khoi around by the shoulders and shouts into his blank face.
- 3.0–7.0s: @Ngan shakes @Khoi gently, her wet hair stuck to her cheeks.
- 7.0–10.0s: @Khoi blinks once, slowly, his eyes coming back into focus. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–4.7s, spoken on camera by @Ngan (woman of 26, strictly standard Hà Nội strictly standard Hà Nội Northern accent (never Southern accent) (never Southern accent), clear warm mezzo, steady but breathless with fear, speaking at a brisk, urgent, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Khôi! Tỉnh lại đi em! Em đang làm cái gì thế này? Nhìn chị đây này, Khôi!" (no subtitles)
- @Ngan's face and lips stay clearly visible while speaking; after the last word @Ngan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water sloshing, frogs, a cold wind. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 03 - Clip 6 (`canh-03/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Deep night: the moonlit brick yard of the old house leading down to the edge of the black lotus pond, mist on the water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm slow tilt down from the siblings to the water; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Ngan guides @Khoi back onto the grassy bank, both of them soaked and shivering in the moonlight.
- 3.0–7.0s: The camera tilts down to the dark water where they stood; long dark lotus stems and a strand of black hair drift across the ripples.
- 7.0–10.0s: The ripples slowly settle across the dark surface of the pond. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Khôi chẳng nhớ gì cả, nhưng Ngân thì nhìn rõ, ngay chỗ em vừa đứng, mặt nước nổi lên một nắm tóc dài đen nhánh." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: dripping water, chattering teeth, a low hollow gurgle. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 1 (`canh-04/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Grey early morning: the old house's back bedroom with a mosquito-net bed, its door open to the brick yard, mist lying on the lotus pond beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm low-angle slow dolly along the floor; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Low-angle dolly shot along the red-brick floor of the old house in grey early morning light, following a line of wet bare footprints leading in from the open yard door.
- 3.0–7.0s: The camera follows the footprints across the bedroom floor as @Ngan walks beside them, looking down closely.
- 7.0–10.0s: The footprints end beside the mosquito-net bed; @Ngan stops there and looks at the pillow. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Sáng hôm sau, từ mép đầm vào tận giường Khôi là một hàng dấu chân trần còn ướt, nhỏ nhắn như chân con gái." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a rooster crowing far off, dripping water, soft footsteps. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 2 (`canh-04/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Grey early morning: the old house's back bedroom with a mosquito-net bed, its door open to the brick yard, mist lying on the lotus pond beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up insert, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Ngan lifts the edge of the mosquito net.
- 3.0–7.0s: On the pillow lies a large wet lotus leaf, its stem wound with several strands of long black hair, water soaking into the cotton.
- 7.0–10.0s: @Ngan's fingers hover above the leaf, trembling, without touching it. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trên gối của Khôi là một chiếc lá sen còn đẫm nước, cuống lá quấn mấy sợi tóc dài không phải của ai trong nhà." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water seeping, a distant rooster, a held breath. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 3 (`canh-04/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Grey early morning: the old house's back bedroom with a mosquito-net bed, its door open to the brick yard, mist lying on the lotus pond beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot, static; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Static view of the mosquito-net bed in grey morning light, a fresh wet green lotus leaf resting on the pillow beside the open window.
- 3.0–7.0s: The camera frames @BaHanh standing beside @Ngan at the bed; @BaHanh looks at the lotus leaf and speaks to @Ngan in a hushed, trembling whisper.
- 7.0–10.0s: @BaHanh sits slowly on the edge of the bed, her hands clasped together. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.6s, spoken on camera by @BaHanh (old woman of 74, strictly standard Hà Nội Northern accent (never Southern accent), soft raspy voice trembling with worry, speaking at a brisk, urgent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Nó chọn thằng Khôi rồi con ạ. Ba mươi năm nay, tháng bảy nào nó cũng về đòi đúng một người." (no subtitles)
- From 3.0s onward, @BaHanh's face and lips stay clearly visible while speaking; after the last word @BaHanh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft sob, morning birds, dripping water. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 4 (`canh-04/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Grey early morning: the old house's back bedroom with a mosquito-net bed, its door open to the brick yard, mist lying on the lotus pond beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm slow arc around the two women; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Ngan sits beside @BaHanh on the bed edge, holding her grandmother's hands.
- 3.0–7.0s: @BaHanh points a shaking finger toward the window and the misty pond beyond.
- 7.0–10.0s: @Ngan turns her head to the window, jaw tightening. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bà kể, người bị đầm bắt đi năm nào cũng là con cháu mấy nhà sống quanh bờ, và luôn đúng vào đêm rằm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning birds, wind on the window shutter. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 5 (`canh-04/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Grey morning: a stone water jar in the brick yard of the old house, mist lying on the lotus pond beyond the gate.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, static; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Medium view of an old stone water jar and wooden dipper in the misty brick yard, grey morning mist drifting over the lotus pond beyond the gate.
- 3.0–7.0s: @Khoi squats beside the stone water jar, scrubbing his ankle with a coconut-husk brush as water splashes onto the wet bricks.
- 7.0–10.0s: @Khoi pauses, looking down at the dark mark on his ankle, breathing fast. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Khôi ngồi bên chum nước kỳ cọ cổ chân đến rát đỏ, nhưng vết hằn đen sẫm ấy cứ loang dần như mực." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water splashing, a brush scraping skin, roosters. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 04 - Clip 6 (`canh-04/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Grey morning: a stone water jar in the brick yard of the old house, mist lying on the lotus pond beyond the gate.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close-up of @Khoi looking up from the water jar, water dripping from his hair.
- 3.0–7.0s: @Khoi speaks in a low shaking voice, eyes red-rimmed.
- 7.0–10.0s: @Khoi swallows hard and looks toward the misty pond. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.4s, spoken on camera by @Khoi (young man of 19, strictly standard Hà Nội strictly standard Hà Nội Northern accent (never Southern accent) (never Southern accent), light tenor, shaky and breathless, speaking at a brisk, urgent, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Không phải mơ đâu chị ạ. Đêm qua em thấy rõ cô ấy nắm chân em, tay lạnh như đá." (no subtitles)
- @Khoi's face and lips stay clearly visible while speaking; after the last word @Khoi closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: dripping water, a far-off cow bell. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 1 (`canh-05/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Morning: the front porch of Ông Lý's large old brick house with a tiled roof, potted bonsai and a stone courtyard, the lotus pond visible behind a bamboo hedge.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm low-angle static shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Low-angle view of the front porch of an old brick house with potted bonsai, a carved wooden table and steaming porcelain teapot in muted morning light.
- 3.0–7.0s: The camera frames @OngLy sitting upright on a carved wooden chair on the porch, setting down his teacup and looking toward the pond with narrow eyes.
- 7.0–10.0s: @OngLy turns his head toward the courtyard gate as footsteps approach. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lý từng làm trưởng thôn hơn hai mươi năm, là người duy nhất trong làng chưa từng có con cháu bị đầm bắt." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birdsong, the clink of a tea cup, a broom sweeping somewhere. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 2 (`canh-05/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Morning: the front porch of Ông Lý's large old brick house with a tiled roof, potted bonsai and a stone courtyard, the lotus pond visible behind a bamboo hedge.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: View across the carved wooden tea table on the porch where steam rises from a small porcelain teapot, the bamboo hedge and lotus pond visible in the background.
- 3.0–7.0s: Over @Ngan's shoulder, @OngLy speaks from his chair with a dismissive wave of his hand and pours tea without looking up.
- 7.0–10.0s: @OngLy's fingers tighten around the porcelain teacup on the table. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–9.4s, spoken on camera by @OngLy (man of 72, strictly standard Hà Nội Northern accent (never Southern accent), deep stern gravelly baritone, speaking at a brisk, clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ma da thì phải tìm người thế mạng mới được đầu thai. Cô cứ làm mâm cúng, giữ thằng bé trong nhà là xong." (no subtitles)
- From 3.0s onward, @OngLy's face and lips stay clearly visible while speaking; after the last word @OngLy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: tea pouring, birds, wind in bamboo. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 3 (`canh-05/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Morning: the front porch of Ông Lý's large old brick house with a tiled roof, potted bonsai and a stone courtyard, the lotus pond visible behind a bamboo hedge.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 100mm macro insert on the tea table; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Close view of a weathered wooden table on the porch in grey daylight, a ceramic teapot resting on the wood.
- 3.0–7.0s: @OngLy's wrinkled hand sets a small porcelain teacup down hard on the table, amber tea sloshing over the rim.
- 7.0–10.0s: @OngLy's fingers grip the teacup tightly as the spilled tea spreads across the dark wood. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngân hỏi người chết đuối đầu tiên là ai, tay ông Lý khựng lại, nước trà sóng sánh tràn ra mặt bàn gỗ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a sharp clink, tea dripping, a crow cawing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 4 (`canh-05/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Morning: the front porch of Ông Lý's large old brick house with a tiled roof, potted bonsai and a stone courtyard, the lotus pond visible behind a bamboo hedge.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, static; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close-up of @OngLy rising from his chair, face rigid, eyes avoiding the camera.
- 3.0–7.0s: @OngLy speaks sharply, his jaw working, a vein standing out at his temple.
- 7.0–10.0s: @OngLy turns away toward his front door, leaning on his cane. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–4.4s, spoken on camera by @OngLy (man of 72, strictly standard Hà Nội Northern accent (never Southern accent), deep stern gravelly baritone, speaking at a brisk, clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chuyện từ đời nào rồi! Cô về nghỉ đi, đừng hỏi han chuyện cũ nữa!" (no subtitles)
- @OngLy's face and lips stay clearly visible while speaking; after the last word @OngLy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: the chair scraping, wind in bamboo, a door creaking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 5 (`canh-05/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Late morning: the old village communal temple with red pillars and a tiled roof, its quiet back shrine room full of dust and cobwebs.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm slow push-in through the temple gate; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Slow push-in through the mossy stone gate of the old village communal temple in late morning light, red wooden pillars and quiet courtyard ahead.
- 3.0–7.0s: @Ngan walks through the temple courtyard into the dusty back shrine room, stopping before a small forgotten incense bowl covered in cobwebs on a low shelf.
- 7.0–10.0s: @Ngan reaches out and gently brushes the cobwebs from the incense bowl. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trên đường về, Ngân đi qua đình làng, thấy sau hậu cung có một bát hương nhỏ không tên, bị bỏ mặc phủ đầy mạng nhện." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: temple wind chimes, pigeons cooing, dust settling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 05 - Clip 6 (`canh-05/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Late morning: the old village communal temple with red pillars and a tiled roof, its quiet back shrine room full of dust and cobwebs.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium close-up, slow rack focus; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Ngan kneels before the cleaned incense bowl and lights a single incense stick.
- 3.0–7.0s: Focus shifts from @Ngan's face to the thin smoke, which bends sideways and drifts toward the open temple door as if pulled by a draft.
- 7.0–10.0s: @Ngan turns to follow the smoke with her eyes, toward the distant pond. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cụ thủ từ bảo, đó là bát hương của con bé Thắm mồ côi, người ba mươi năm trước bị cả làng gọi là kẻ trộm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: incense hiss, wind chimes, a sudden cold gust. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 1 (`canh-06/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: the grassy bank of the lotus pond, a low offering tray on a straw mat with rice, boiled chicken, white paper clothes and a ring of white candles, black water beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide static shot from the water; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Wide view across the dark water toward the grassy bank at night, where a low offering tray with rice and a circle of lit white candles glows on a straw mat.
- 3.0–7.0s: On the bank behind the ring of candles, @BaHanh kneels on the straw mat and bows three times with joined palms and lit incense sticks.
- 7.0–10.0s: @BaHanh places a folded set of white paper clothes beside the water's edge. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Tối đó, bà Hạnh bày mâm cúng ngay bờ đầm, có cả bộ quần áo giấy trắng, khấn xin cho cháu mình được tha." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: candle flames fluttering, crickets, frogs, a soft murmured prayer. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 2 (`canh-06/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: the grassy bank of the lotus pond, a low offering tray on a straw mat with rice, boiled chicken, white paper clothes and a ring of white candles, black water beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Slow push-in on the ring of lit white candles and incense sticks burning on the straw mat at the edge of the dark lotus pond at night.
- 3.0–7.0s: The camera tilts up to frame @BaHanh kneeling in prayer with @Ngan standing behind her holding a flashlight, watching the candle flames.
- 7.0–10.0s: @Ngan lifts her gaze from the candles toward the dark lotus pond. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngân đứng sau lưng bà, tay cầm chiếc đèn pin, và cô đếm được mười hai ngọn nến đang cháy đều trong gió lặng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: dead calm, a single cricket, candle wicks sizzling. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 3 (`canh-06/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: the grassy bank of the lotus pond, a low offering tray on a straw mat with rice, boiled chicken, white paper clothes and a ring of white candles, black water beyond.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 50mm low-angle close tracking shot along the candle ring; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close on the ring of white candles on the dark grass, all burning steadily.
- 3.0–7.0s: One by one, starting from the flame nearest the water, the candles snuff out with thin trails of smoke, the darkness moving up the bank.
- 7.0–10.0s: Only the last candle beside the paper clothes still burns, its flame bending toward the pond. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Rồi từng ngọn nến tắt phụt, lần lượt từ phía gần nước nhất, như có ai đang bước từ dưới đầm lên bờ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft puffs of extinguished flames, water lapping, a wet footstep on grass. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 4 (`canh-06/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: the grassy bank of the lotus pond, a low offering tray on a straw mat with rice, boiled chicken, white paper clothes and a ring of white candles, black water beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm handheld medium close-up; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Handheld view of a bright flashlight beam sweeping across the dark lotus leaves and rippling water at the edge of the pond at night.
- 3.0–7.0s: The camera frames @Ngan on the bank swinging the flashlight beam toward the water and calling out urgently as she steps back.
- 7.0–10.0s: @Ngan stops still, holding the flashlight beam steady on the water's edge. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.5s, spoken on camera by @Ngan (woman of 26, strictly standard Hà Nội strictly standard Hà Nội Northern accent (never Southern accent) (never Southern accent), clear warm mezzo, steady but breathless with fear, speaking at a brisk, urgent, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Bà ơi, đứng dậy đi bà! Có cái gì đang đi lên từ dưới nước kìa, mình vào nhà ngay đi bà!" (no subtitles)
- From 3.0s onward, @Ngan's face and lips stay clearly visible while speaking; after the last word @Ngan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rapid breathing, wet slapping steps on the grass, wind rising. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 5 (`canh-06/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: the grassy bank of the lotus pond, a low offering tray on a straw mat with rice, boiled chicken, white paper clothes and a ring of white candles, black water beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @CoTham = the mysterious young woman of the lotus pond from thirty years ago: pale wet skin, long soaked black hair with lotus stems, dark sorrowful eyes; soaked plain white Northern village blouse and black trousers, barefoot.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm static wide shot in the flashlight beam; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Static wide view of the grassy water's edge in a flashlight beam at night, where soaked white paper clothes lie on the wet grass beside dark lotus leaves.
- 3.0–7.0s: The white paper clothes stir in the cold wind at the bank as the faint pale figure of @CoTham appears standing quietly at the water's edge.
- 7.0–10.0s: @CoTham stands motionless in the flickering flashlight beam beside the dark lotus leaves. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trong quầng đèn pin, bộ quần áo giấy trắng đã ướt sũng, đang từ từ đứng thẳng lên như có ai vừa mặc vào." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wet paper rustling, water dripping, a long breathy sigh. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 06 - Clip 6 (`canh-06/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Deep night: a back bedroom with a mosquito-net bed and a barred wooden window facing the lotus pond, a single blue shaft of moonlight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up through the mosquito net, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the dark bedroom at night, cold cyan moonlight filtering through the wooden window bars onto the white mosquito net.
- 3.0–7.0s: The camera pushes in slowly on @Khoi lying flat on his pillow fast asleep, his eyes tightly shut and his face pale.
- 7.0–10.0s: @Khoi remains motionless with his eyes closed in sleep while the corner of his closed mouth forms a faint, eerie smile. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cùng lúc ấy, trong nhà, Khôi đang ngủ say bỗng cười khúc khích, tiếng cười trong trẻo của một cô gái lạ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a girl's clear echoing giggle, crickets stopping abruptly. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 1 (`canh-07/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Hot hazy noon: the gate of Bà Hạnh's house opening onto the embankment path beside the lotus pond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide static shot at the gate; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Wide static view of the open wooden gate leading from the brick yard onto the earthen embankment path beside the sunlit lotus pond at hazy noon.
- 3.0–7.0s: @Ngan hurries out through the gate into the noon glare and stops short beside a pair of white plastic sandals lying on the embankment path.
- 7.0–10.0s: @Ngan looks up from the sandals toward the wide green lotus pond. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trưa hôm sau, Ngân chỉ chợp mắt có nửa tiếng, tỉnh dậy đã không thấy Khôi đâu, đôi dép tổ ong nằm chỏng chơ ngoài cổng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: cicadas buzzing, hot wind, footsteps stopping. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 2 (`canh-07/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Hot hazy noon: the lotus pond under a white sky, a narrow embankment path, small round bamboo basket boats among the leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm handheld medium shot tracking along the embankment; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Handheld tracking view along the narrow earthen embankment path beside the vast lotus pond at hazy noon, round bamboo basket boats floating in the distance.
- 3.0–7.0s: @Ngan runs along the embankment path cupping her hands around her mouth and calling out across the pond.
- 7.0–10.0s: @Ngan pauses on the path, breathing hard as she scans the dense lotus leaves. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.8s, spoken on camera by @Ngan (woman of 26, strictly standard Hà Nội strictly standard Hà Nội Northern accent (never Southern accent) (never Southern accent), clear warm mezzo, steady but breathless with fear, speaking at a brisk, urgent, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Khôi ơi! Khôi! Em ở đâu thì trả lời chị một tiếng đi, chị xin em đấy Khôi ơi!" (no subtitles)
- From 3.0s onward, @Ngan's face and lips stay clearly visible while speaking; after the last word @Ngan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: cicadas, an echoing voice over the water, ducks taking off. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 3 (`canh-07/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Hot hazy noon: the lotus pond under a white sky, a narrow embankment path, small round bamboo basket boats among the leaves.

[CHARACTERS]
- Extra: a few village men in conical hats paddling round bamboo basket boats, faces shaded, seen from above (unnamed)
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 24mm high-angle crane shot over the pond; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: High above the lotus pond, several round bamboo basket boats spread out across the water.
- 3.0–7.0s: Village men in conical hats push long bamboo poles down through the lotus leaves, stirring up dark mud.
- 7.0–10.0s: A pole lifts out of the water dripping with a tangle of black lotus roots. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cả xóm đổ ra, đàn ông chèo thuyền thúng, dùng sào tre khua khắp mặt đầm, nhưng chỉ vớt lên toàn rễ sen đen kịt." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: poles splashing, men calling to each other, cicadas. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 4 (`canh-07/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Hot hazy noon: the lotus pond under a white sky, a narrow embankment path, small round bamboo basket boats among the leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm water-level tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Water-level tracking view moving through dense green lotus leaves and tall stems on the pond under a hazy white noon sky.
- 3.0–7.0s: @Ngan wades chest-deep through the lotus leaves, pushing the stems aside with both arms as an old bamboo basket boat drifts ahead.
- 7.0–10.0s: @Ngan reaches out and grips the woven rim of the bamboo basket boat. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngân lội ra tận chỗ nước ngang ngực thì thấy giữa đám lá sen có một chiếc thuyền thúng cũ trôi lững lờ, không người chèo." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water sloshing, lotus leaves rustling, distant shouting. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 5 (`canh-07/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Hot hazy noon: the lotus pond under a white sky, a narrow embankment path, small round bamboo basket boats among the leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm top-down overhead shot into the boat; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Overhead view looking down at the round woven rim of a bamboo basket boat floating among green lotus leaves on the pond at noon.
- 3.0–7.0s: Inside the boat, @Khoi lies curled on his side; @Ngan leans over the rim and touches @Khoi's cheek as he takes a steady breath.
- 7.0–10.0s: The camera frames @Khoi's hand holding an old tarnished silver lotus-bud hairpin. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Khôi nằm co quắp trong lòng thuyền, môi tím ngắt, người lạnh toát, tay nắm chặt một chiếc trâm bạc cũ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water lapping the boat, a weak gasp, cicadas. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 07 - Clip 6 (`canh-07/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Late afternoon: inside the old house by the ancestral altar, soft grey light through the wooden doors.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 100mm macro insert, then rack focus; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Macro close-up of a tarnished silver hairpin shaped like a lotus bud resting on a folded white cloth on a wooden table in soft afternoon light.
- 3.0–7.0s: Focus racks up from the table to reveal @BaHanh leaning over the cloth, her eyes wide and one hand pressed to her chest.
- 7.0–10.0s: @BaHanh lowers her gaze over the silver hairpin, tears glistening on her lined cheeks. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bà Hạnh nhận ra ngay chiếc trâm bạc ấy, kỷ vật của Thắm, cô gái mồ côi khuất bóng nơi đầm sen năm xưa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a heavy silence, wind on the door, a soft sob. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 1 (`canh-08/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: inside the old house by the ancestral altar, an oil lamp on a low table, rain pouring outside the open door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Slow push-in on an old dark wooden chest beneath the ancestral altar inside the house at night, warm oil-lamp light flickering as rain falls outside.
- 3.0–7.0s: @BaHanh kneels before the wooden chest with @Ngan beside her, lifts the lid and takes out a faded black-and-white photograph into the lamplight.
- 7.0–10.0s: @BaHanh hands the old photograph to @Ngan in silence. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đêm đó, bà Hạnh mở rương gỗ dưới bàn thờ, lấy ra tấm ảnh cũ chụp ông nội Ngân cùng mấy người trong làng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain on the tiles, the chest lid creaking, the lamp wick sputtering. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 2 (`canh-08/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: inside the old house by the ancestral altar, an oil lamp on a low table, rain pouring outside the open door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 100mm macro insert on the photograph; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close on the old black-and-white photograph in @Ngan's hands: a row of village men standing in front of a temple gate.
- 3.0–7.0s: The camera slowly pushes in on the man in the center, younger but with the same hard narrow eyes, holding a ring of large keys.
- 7.0–10.0s: @Ngan's thumb rests beside the man's face, trembling. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Trong ảnh, ông Lý thời trẻ đứng giữa, tay cầm chùm chìa khóa hòm công đức của đình, ánh mắt sắc lạnh y như bây giờ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain on the roof, the lamp wick hissing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 3 (`canh-08/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: inside the old house by the ancestral altar, an oil lamp on a low table, rain pouring outside the open door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: View of the flickering amber oil-lamp flame on the low wooden table inside the house at night, heavy rain pouring past the open doorway.
- 3.0–7.0s: The camera frames @BaHanh across the table over @Ngan's shoulder as @BaHanh speaks softly, holding her wooden prayer beads.
- 7.0–10.0s: @BaHanh lowers her eyes toward the table in the warm lamplight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.8s, spoken on camera by @BaHanh (old woman of 74, strictly standard Hà Nội Northern accent (never Southern accent), soft raspy voice trembling with worry, speaking at a brisk, urgent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Năm ấy hòm công đức mất sạch, ông Lý bảo chính mắt ông thấy con Thắm lẻn vào đình lúc nửa đêm." (no subtitles)
- From 3.0s onward, @BaHanh's face and lips stay clearly visible while speaking; after the last word @BaHanh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain growing heavier, thunder far away. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 4 (`canh-08/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: inside the old house by the ancestral altar, an oil lamp on a low table, rain pouring outside the open door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, static; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close-up of @BaHanh, tears glistening on her lined face in the warm lamplight.
- 3.0–7.0s: @BaHanh speaks in a hushed, emotional voice, her chin trembling.
- 7.0–10.0s: @BaHanh presses both hands to her face, her shoulders trembling. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–7.3s, spoken on camera by @BaHanh (old woman of 74, strictly standard Hà Nội Northern accent (never Southern accent), soft raspy voice trembling with worry, speaking at a brisk, urgent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cả làng đuổi theo nó ra tận bờ đầm. Ông nhà bà cũng cầm đuốc đứng đó, nhìn nó khuất dưới đầm mà không ai giúp." (no subtitles)
- @BaHanh's face and lips stay clearly visible while speaking; after the last word @BaHanh closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heavy rain, a roll of thunder, a sob. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 5 (`canh-08/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: inside the old house by the ancestral altar, an oil lamp on a low table, rain pouring outside the open door.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm slow pull-back toward the open door; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Slow pull-back from the low wooden table and flickering oil lamp toward the open doorway where night rain falls into the dark brick yard.
- 3.0–7.0s: @Ngan sits quietly at the table holding the faded photograph in her lap, then turns her head toward the rain-swept doorway.
- 7.0–10.0s: The camera pulls back through the doorway, framing @Ngan inside the lamplit room with the dark pond beyond. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngân chợt hiểu, những người bị đầm bắt suốt ba mươi năm qua đều là con cháu của những kẻ đứng trên bờ đêm ấy." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain, thunder, a distant splash. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 08 - Clip 6 (`canh-08/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: the back bedroom, mosquito-net bed, rain streaming down the barred window, a dim oil lamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up through the mosquito net, static; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Static view of the rain-streaked barred wooden window and white mosquito net in the dim bedroom at night, lit by a low oil lamp.
- 3.0–7.0s: Through the mosquito net, @Khoi rests on the bed with a damp cloth on his forehead, turning his head restlessly on the pillow.
- 7.0–10.0s: Drops of water glisten along the edge of the wooden bedframe in the dim lamplight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Còn Khôi, nằm sốt mê man trong buồng, cứ thì thào bằng giọng con gái rằng em không hề lấy trộm thứ gì." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain on the window, dripping water, a faint girl's whisper. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 1 (`canh-09/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Flashback, thirty years earlier, a stormy night in the seventh lunar month: the same lotus pond and muddy embankment in heavy rain, lit only by flaming torches; desaturated and grainy.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @ThamXua = Thắm when alive, a slim 19-year-old orphan village girl; long black hair in a single braid, frightened dark eyes; plain plain white Northern village blouse and black trousers, barefoot.
- Extra: a crowd of village men holding flaming torches far behind her, blurred silhouettes in the rain (unnamed)
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm handheld tracking shot alongside; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Handheld tracking view along a rain-swept muddy embankment beside the lotus pond on a stormy night, distant orange torchlight reflecting on wet mud.
- 3.0–7.0s: @ThamXua runs barefoot through the rain along the muddy embankment, her braided hair swinging as she glances back toward the distant torches.
- 7.0–10.0s: @ThamXua steadies herself on the wet bank beside the dark lotus leaves, breathing fast. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ba mươi năm trước, cũng một đêm mưa tháng bảy, Thắm chạy trối chết dọc bờ đầm, phía sau là cả một rừng đuốc." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pouring rain, thunder, distant angry shouting, splashing footsteps. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 2 (`canh-09/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Flashback, thirty years earlier, a stormy night in the seventh lunar month: the same lotus pond and muddy embankment in heavy rain, lit only by flaming torches; desaturated and grainy.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @ThamXua = Thắm when alive, a slim 19-year-old orphan village girl; long black hair in a single braid, frightened dark eyes; plain plain white Northern village blouse and black trousers, barefoot.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium close-up lit by off-frame torchlight; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Rain-swept muddy embankment beside the lotus pond at night, orange torchlight reflecting on wet mud and lotus leaves.
- 3.0–7.0s: @ThamXua kneels on the wet mud in the pouring rain, her hands clasped in front of her chest as she pleads.
- 7.0–10.0s: @ThamXua looks up through the rain with tears mixing with rainwater on her pale face. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–7.5s, spoken on camera by @ThamXua (young woman of 19, strictly standard Hà Nội Northern accent (never Southern accent), clear trembling voice, pleading, speaking at a brisk, urgent pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Cháu không lấy! Cháu thề có trời đất, cháu không hề động vào hòm công đức của đình!" (no subtitles)
- From 3.0s onward, @ThamXua's face and lips stay clearly visible while speaking; after the last word @ThamXua closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain, thunder, crackling torches, angry murmuring. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 3 (`canh-09/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Flashback, thirty years earlier, a stormy night in the seventh lunar month: the same lotus pond and muddy embankment in heavy rain, lit only by flaming torches; desaturated and grainy.

[CHARACTERS]
- Extra: the younger Ông Lý, about 42, gaunt with hard narrow eyes, in an olive-green jacket, at the front of a crowd of blurred torch-bearing villagers (no reference image)
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 35mm low-angle shot through the rain; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Low angle through the rain: a wall of flaming torches held by blurred villagers on the muddy bank.
- 3.0–7.0s: At the front, a gaunt man in an olive-green jacket thrusts his torch toward the pond, his face hard in the firelight.
- 7.0–10.0s: The torchlight flickers across the black pond surface ahead of the crowd. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Không ai tin cô. Người ta dồn cô ra sát mép nước, và người hô to nhất chính là ông Lý thời trẻ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pouring rain, crackling torches, a harsh distant shout, thunder. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 4 (`canh-09/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Flashback, thirty years earlier, a stormy night in the seventh lunar month: the same lotus pond and muddy embankment in heavy rain, lit only by flaming torches; desaturated and grainy.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @ThamXua = Thắm when alive, a slim 19-year-old orphan village girl; long black hair in a single braid, frightened dark eyes; plain plain white Northern village blouse and black trousers, barefoot.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm static wide shot from the water; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Wide view from the rain-swept lotus pond looking toward the muddy bank at night, orange torchlight flickering across the wet grass.
- 3.0–7.0s: A single solitary figure, @ThamXua alone on the muddy bank, steps backward in the rain as tall lotus stems and mist surround her.
- 7.0–10.0s: Raindrops and spreading ripples rock the dark lotus leaves across the water. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Thắm lùi thêm một bước trên bờ đất ướt, tà áo trắng khuất dần sau những tàu lá sen đen sẫm trong màn mưa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: pouring rain, wind rustling lotus leaves, distant voices falling silent. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 5 (`canh-09/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Flashback, thirty years earlier, a stormy night in the seventh lunar month: the same lotus pond and muddy embankment in heavy rain, lit only by flaming torches; desaturated and grainy.

[CHARACTERS]
- Extra: blurred torch-bearing villagers standing still on the bank, out of focus (unnamed)
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 50mm water-level static shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Water-level view in the falling rain as dark lotus leaves and a pale lotus bud rock on the ripples of the pond.
- 3.0–7.0s: Beyond the swaying lotus stems, warm orange torchlight reflects across the wet muddy bank in the rain.
- 7.0–10.0s: Concentric ripples slowly widen across the dark water surface under the rain. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Cô vùng vẫy, một bàn tay nhô lên khỏi mặt nước như cầu cứu, nhưng hàng chục ngọn đuốc trên bờ không ai nhúc nhích." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: rain on the water, a muffled gasp, then only rain. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 09 - Clip 6 (`canh-09/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Flashback dawn after the storm: the still lotus pond under a grey sky, mist on the water, torch stubs smoking in the mud; desaturated and grainy.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 24mm slow aerial pull-back; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Grey dawn over the still lotus pond after the storm, mist drifting on the water.
- 3.0–7.0s: On the muddy bank, burned-out torch stubs lie smoking among footprints.
- 7.0–10.0s: The camera rises slowly, the pond silent and empty under the grey sky. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Sáng hôm sau, không thấy hòm tiền, cũng chẳng thấy bóng Thắm đâu, cả làng bảo nhau rằng đầm sen đã giữ người ở lại." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: dripping leaves, a lone crow, wind. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 1 (`canh-10/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night of the full moon: the back bedroom, moonlight pouring through the barred window onto the mosquito-net bed.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Inside the moonlit bedroom at night, a white mosquito net hanging over the wooden bed beside the barred window.
- 3.0–7.0s: @Khoi sits upright on the edge of the wooden bed in a trance, holding a small antique silver hairpin in his hand and slowly combing his hair.
- 7.0–10.0s: @Khoi stares blankly toward the moonlit window with the silver hairpin in his hand. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đêm rằm tháng bảy, trăng tròn vằng vặc, Khôi bỗng hết sốt, ngồi dậy chải đầu bằng chiếc trâm bạc như một cô gái." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets stopping, a slow scrape of metal through hair, distant water. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 2 (`canh-10/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night of the full moon: the back bedroom, moonlight pouring through the barred window onto the mosquito-net bed.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm over-the-shoulder shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: View from the bedroom doorway looking toward the barred window and moonlit bed, silver moonlight reflecting on the brick floor.
- 3.0–7.0s: Over @Ngan's shoulder in the doorway, @Khoi looks up from the moonlit bed with the silver hairpin in his hand and speaks in a calm, distant voice.
- 7.0–10.0s: @Khoi rises slowly from the edge of the bed in the moonlight. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.0s, spoken on camera by @Khoi (young man of 19, strictly standard Hà Nội strictly standard Hà Nội Northern accent (never Southern accent) (never Southern accent), light tenor, shaky and breathless, speaking at a brisk, urgent, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chị ơi, cô ấy bảo đêm nay là đêm cuối cùng rồi. Em phải xuống trả lại cho cô ấy." (no subtitles)
- From 3.0s onward, @Khoi's face and lips stay clearly visible while speaking; after the last word @Khoi closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: crickets, wind, a faint watery hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 3 (`canh-10/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night of the full moon: the moonlit brick yard and the bank of the lotus pond, mist on the water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm wide tracking shot from the side; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Wide side-tracking view across the moonlit brick yard leading down to the misty bank of the lotus pond under a full moon.
- 3.0–7.0s: @Khoi walks steadily across the moonlit yard toward the pond while @Ngan holds onto his arm with both hands, trying to pull him back.
- 7.0–10.0s: @Khoi steps into the shallow water at the bank as @Ngan stops at the edge. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Khôi đi thẳng ra đầm, Ngân giữ thế nào cũng không lại, người cậu nặng trịch và lạnh như một khúc gỗ ngâm nước." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: heels scraping grass, splashing, crickets, wind. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 4 (`canh-10/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night of the full moon: the moonlit brick yard and the bank of the lotus pond, mist on the water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm static medium shot at the water's edge; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: @Ngan stands at the edge of the pond staring at the spreading rings on the moonlit water.
- 3.0–7.0s: @Ngan takes a deep breath and wades forward into the deep water among the lotus leaves.
- 7.0–10.0s: Moonlit ripples rock the lotus leaves across the surface of the pond. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Không kịp nghĩ ngợi, Ngân hít một hơi thật sâu rồi lội xuống làn nước đêm, nơi em trai cô vừa khuất bóng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a deep inhale, a splash, then muffled silence. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 5 (`canh-10/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Underwater at the bottom of the lotus pond: murky green-black water, a forest of lotus stems and roots, shafts of moonlight from above, drifting silt.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @CoTham = the mysterious young woman of the lotus pond from thirty years ago: pale wet skin, long soaked black hair with lotus stems, dark sorrowful eyes; soaked plain white Northern village blouse and black trousers, barefoot.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm underwater slow drift shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Slow underwater drift through murky green-black water at the bottom of the lotus pond, pale moonlight filtering between tall lotus stems and roots.
- 3.0–7.0s: Among the tangled lotus roots underwater, @CoTham stands quietly in the dark water, her long black hair floating around her pale face.
- 7.0–10.0s: @CoTham slowly extends one arm and points downward toward the soft mud at the bottom of the pond. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Dưới đáy đầm, giữa rừng rễ sen chằng chịt, Thắm đứng đó, tóc xõa bồng bềnh, lặng lẽ chỉ tay xuống lớp bùn." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: muffled underwater rumble, bubbles, a low distant hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 10 - Clip 6 (`canh-10/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Underwater at the bottom of the lotus pond: murky green-black water, a forest of lotus stems and roots, shafts of moonlight from above, drifting silt.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm underwater close-up; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Soft dark mud and tangled lotus roots at the bottom of the pond underwater, drifting silt in the pale moonlight.
- 3.0–7.0s: @Ngan pulls out an old brass box wrapped in lotus roots and long black hair, a crane engraved on its tarnished lid.
- 7.0–10.0s: @Ngan clutches the box to her chest and swims upward hard toward the moonlight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngân thọc tay xuống bùn, chạm phải một chiếc hộp kim loại lạnh ngắt, quấn chặt trong rễ sen và những sợi tóc dài." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: muffled underwater sounds, a metallic scrape, bubbles rushing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 1 (`canh-11/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night of the full moon: the muddy bank of the lotus pond, moonlight and mist.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide static shot from the water; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Wide view from the moonlit lotus pond looking toward the muddy grass bank at night, silver ripples spreading across the water.
- 3.0–7.0s: @Ngan surfaces from the water holding a tarnished brass box to her chest while @Khoi rests safely on the muddy bank, breathing steadily.
- 7.0–10.0s: @Ngan wades ashore and kneels beside @Khoi on the bank, resting one hand on his shoulder. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngân ngoi lên, thấy Khôi đã nằm sẵn trên bờ, ho sặc sụa nhưng còn sống, như có ai vừa đặt cậu lên đó." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: gasping, coughing, water dripping, frogs. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 2 (`canh-11/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night of the full moon: the muddy bank of the lotus pond, moonlight and mist.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 100mm macro insert, slow tilt; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close on @Ngan's muddy hands prying open the tarnished brass box on the wet grass.
- 3.0–7.0s: Inside, old silver coins glint in the moonlight, packed in faded old red cloth.
- 7.0–10.0s: The camera tilts to the lid, where an engraved crane catches the moonlight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bên trong hộp trầu là những đồng bạc trắng của đình làng, và nắp hộp khắc hình con hạc, vật gia truyền nhà ông Lý." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a rusty hinge creak, coins clinking, frogs. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 3 (`canh-11/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Grey dawn: the stone courtyard and front porch of Ông Lý's old brick house, mist from the pond drifting over the bamboo hedge.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot, static; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Static medium view of the stone courtyard and front porch of the old brick house at grey dawn, morning mist drifting over the bamboo hedge.
- 3.0–7.0s: In the courtyard, @Ngan holds the tarnished brass box out toward @OngLy on his porch and speaks firmly.
- 7.0–10.0s: @OngLy looks down at the brass box, his face pale and rigid. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.5s, spoken on camera by @Ngan (woman of 26, strictly standard Hà Nội strictly standard Hà Nội Northern accent (never Southern accent) (never Southern accent), clear warm mezzo, steady but breathless with fear, speaking at a brisk, urgent, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ông nhìn kỹ đi! Hộp trầu nhà ông, tiền công đức của đình, nằm dưới đáy đầm ba mươi năm nay đấy!" (no subtitles)
- From 3.0s onward, @Ngan's face and lips stay clearly visible while speaking; after the last word @Ngan closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: roosters, wind in bamboo, dripping water. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 4 (`canh-11/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Grey dawn: the stone courtyard and front porch of Ông Lý's old brick house, mist from the pond drifting over the bamboo hedge.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close-up of @OngLy shouting, his narrow eyes blazing.
- 3.0–7.0s: @OngLy jabs his cane toward the courtyard gate, his hand shaking.
- 7.0–10.0s: @OngLy's gaze drops to the brass box and he swallows hard. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.8s, spoken on camera by @OngLy (man of 72, strictly standard Hà Nội Northern accent (never Southern accent), deep stern gravelly baritone, speaking at a brisk, clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Láo toét! Hộp trầu thì nhà nào chẳng có. Cô dám vu cho tôi thì cả làng này sẽ không tha cho cô đâu!" (no subtitles)
- @OngLy's face and lips stay clearly visible while speaking; after the last word @OngLy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: roosters, wind, the cane tapping stone. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 5 (`canh-11/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Grey dawn: the stone courtyard and front porch of Ông Lý's old brick house, mist from the pond drifting over the bamboo hedge.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm low-angle shot on the porch steps; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Low-angle view of the weathered stone steps of the front porch at grey dawn, damp mist clinging to the stones.
- 3.0–7.0s: @Ngan steps up, kneels by the stone porch steps and places the tarnished silver lotus hairpin on the top step before rising and turning away.
- 7.0–10.0s: The camera holds low on the silver hairpin resting on the stone step. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngân không cãi. Cô chỉ đặt chiếc trâm bạc của Thắm lên bậc thềm nhà ông, rồi lặng lẽ bỏ về." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: footsteps on stone, roosters, a cold breeze. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 11 - Clip 6 (`canh-11/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Grey dawn: the stone courtyard and front porch of Ông Lý's old brick house, mist from the pond drifting over the bamboo hedge.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up on the hands; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Close view of the tarnished silver lotus hairpin resting on the stone porch step in the cold grey dawn light.
- 3.0–7.0s: The camera tilts up to @OngLy standing on the porch looking down at the hairpin, his weathered hands trembling on the head of his walking cane.
- 7.0–10.0s: @OngLy closes his eyes, his jaw tight. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lý đứng nhìn chiếc trâm rất lâu. Ba mươi năm rồi, lần đầu tiên ông thấy bàn tay mình run lên không dừng được." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind in bamboo, a distant temple bell, ragged breathing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 1 (`canh-12/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: Ông Lý's dark bedroom with a heavy carved wooden bed, a tall cabinet and a window facing the lotus pond, a single oil lamp turned low.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm static medium shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Static medium view of a dark bedroom at night with a carved wooden bed, a tall wooden cabinet and a dim oil lamp flickering near the window.
- 3.0–7.0s: On the carved wooden bed, @OngLy lies awake; his eyes turn toward the window and he props himself up on one elbow, listening.
- 7.0–10.0s: @OngLy sits up on the edge of the bed, looking toward the moonlit window. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đêm ấy, ông Lý nghe ngoài đầm có tiếng con gái gọi đúng tên cúng cơm của ông, cái tên chẳng ai còn nhớ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a faint girl's voice calling from far over water, crickets, the bed creaking. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 2 (`canh-12/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: Ông Lý's dark bedroom with a heavy carved wooden bed, a tall cabinet and a window facing the lotus pond, a single oil lamp turned low.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 24mm low-angle dolly along the floor; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Rain-streaked wooden window and dark brick floor of the old bedroom at night, a thin trail of water glistening on the tiles.
- 3.0–7.0s: @OngLy sits on the edge of his wooden bed in the dim oil-lamp light, looking down in shock at the wet trail on the floor.
- 7.0–10.0s: @OngLy grips his wooden cane with trembling hands as the oil lamp flickers. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Từ cửa sổ vào tận đầu giường, những vệt nước loang dần trên nền gạch, kéo theo mùi bùn tanh lạnh của đáy đầm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: slow wet footsteps, dripping water, the lamp flame sputtering. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 3 (`canh-12/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: Ông Lý's dark bedroom with a heavy carved wooden bed, a tall cabinet and a window facing the lotus pond, a single oil lamp turned low.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
- @CoTham = the mysterious young woman of the lotus pond from thirty years ago: pale wet skin, long soaked black hair with lotus stems, dark sorrowful eyes; soaked plain white Northern village blouse and black trousers, barefoot.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: View across the dark bedroom floor where wet footprints glisten in the dim oil-lamp light near the foot of the carved wooden bed.
- 3.0–7.0s: The camera tilts up over @OngLy's shoulder to reveal @CoTham standing quietly at the foot of the bed, looking at him with calm, sorrowful eyes.
- 7.0–10.0s: @OngLy leans back against the wooden headboard, gripping the blanket. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lý ngẩng đầu lên, thấy Thắm đang đứng lặng ngay cuối giường, đôi mắt buồn rượi nhìn ông không lời oán trách." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: steady dripping, the lamp hissing, ragged breathing. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 4 (`canh-12/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: Ông Lý's dark bedroom with a heavy carved wooden bed, a tall cabinet and a window facing the lotus pond, a single oil lamp turned low.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up with a slight Dutch angle, static; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close-up of @OngLy pressed against the headboard, his face wet with tears and sweat.
- 3.0–7.0s: @OngLy pleads with his palms pressed together, his voice breaking.
- 7.0–10.0s: @OngLy bows his head down onto his joined hands, sobbing. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.7s, spoken on camera by @OngLy (man of 72, strictly standard Hà Nội Northern accent (never Southern accent), deep stern gravelly baritone, speaking at a brisk, clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Là tao lấy, Thắm ạ! Tao sợ quá nên mới đổ tội cho mày. Tao xin mày, tha cho tao!" (no subtitles)
- @OngLy's face and lips stay clearly visible while speaking; after the last word @OngLy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: sobbing, dripping water, wind rattling the shutters. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 5 (`canh-12/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: Ông Lý's dark bedroom with a heavy carved wooden bed, a tall cabinet and a window facing the lotus pond, a single oil lamp turned low.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @CoTham = the mysterious young woman of the lotus pond from thirty years ago: pale wet skin, long soaked black hair with lotus stems, dark sorrowful eyes; soaked plain white Northern village blouse and black trousers, barefoot.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm static wide shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Wide static view of the moonlit wooden window and dim oil lamp inside the quiet bedroom at night.
- 3.0–7.0s: @CoTham turns from the bed and walks slowly toward the moonlit window, her figure fading softly into the shadow beside the frame.
- 7.0–10.0s: A small puddle of water on the brick floor reflects the flickering oil-lamp flame. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Thắm không nói gì. Cô chỉ quay đi, để lại trên nền gạch một vũng nước nhỏ, phản chiếu ánh đèn dầu leo lét." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft wet footsteps fading, the lamp hissing, crickets returning. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 12 - Clip 6 (`canh-12/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Pre-dawn: Ông Lý's bedroom in cold blue light through the window, the oil lamp burned out.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Slow push-in on the bedroom window as cold blue pre-dawn light fills the room and the oil lamp on the table stands unlit.
- 3.0–7.0s: On the edge of the carved bed, @OngLy sits hunched in the blue dawn light, then straightens his back and wipes his face with both hands.
- 7.0–10.0s: @OngLy takes hold of his wooden walking cane and stands up. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Gà gáy canh tư, ông Lý vẫn ngồi đó, lần đầu tiên sau ba mươi năm, ông quyết định sẽ nói ra sự thật." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a rooster crowing, a cold wind, the cane tapping the floor. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 1 (`canh-13/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Morning: the stone courtyard of the old village temple with red pillars and a tiled roof, villagers gathered as blurred figures in the background, soft grey sky.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
- Extra: villagers gathering in the background, blurred and out of focus (unnamed)
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide static shot of the temple courtyard; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Wide static view of the stone courtyard of the old village temple in soft morning mist, red wooden pillars and a large wooden drum on a stand.
- 3.0–7.0s: @OngLy steps up to the wooden temple drum and beats it with a padded stick as blurred villagers gather in the courtyard, then walks to the small incense bowl.
- 7.0–10.0s: @OngLy kneels slowly on the stone courtyard before the small incense bowl. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Sáng hôm ấy, ông Lý gõ trống đình, gọi cả làng ra sân, đứng trước bát hương không tên của Thắm mà quỳ xuống." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: deep drum beats echoing, murmuring villagers, birds. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 2 (`canh-13/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Morning: the stone courtyard of the old village temple with red pillars and a tiled roof, villagers gathered as blurred figures in the background, soft grey sky.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm close-up, static; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close-up of @OngLy kneeling, his face grey and wet, looking up toward the off-frame crowd.
- 3.0–7.0s: @OngLy speaks loudly and clearly, his voice shaking but steady.
- 7.0–10.0s: @OngLy lowers his forehead to the stone courtyard. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–6.2s, spoken on camera by @OngLy (man of 72, strictly standard Hà Nội Northern accent (never Southern accent), deep stern gravelly baritone, speaking at a brisk, clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Ba mươi năm trước, chính tôi lấy tiền công đức rồi đổ tội cho con Thắm. Nó chịu oan khuất vì tôi." (no subtitles)
- @OngLy's face and lips stay clearly visible while speaking; after the last word @OngLy closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a stunned hush, wind chimes, a single gasp. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 3 (`canh-13/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Morning: the stone courtyard of the old village temple with red pillars and a tiled roof, villagers gathered as blurred figures in the background, soft grey sky.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
- Extra: villagers in the background, blurred and out of focus (unnamed)
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Slow push-in across the misty stone courtyard of the village temple where incense smoke rises before the red wooden pillars.
- 3.0–7.0s: Among the blurred villagers, @BaHanh presses both hands to her mouth, then kneels down on the stone courtyard with tears on her cheeks.
- 7.0–10.0s: @BaHanh bows her head toward the incense bowl, wooden prayer beads in her joined hands. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.2s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bà Hạnh bật khóc. Chồng bà và bao người khác đã chọn im lặng đêm ấy, để rồi con cháu phải trả giá." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: sobbing, murmuring, wind chimes. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 4 (`canh-13/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Morning: the stone courtyard of the old village temple with red pillars and a tiled roof, villagers gathered as blurred figures in the background, soft grey sky.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide two-shot, slow tilt down; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Stone courtyard of the village communal temple in soft morning light, red wooden pillars and warm incense smoke in the background.
- 3.0–7.0s: @Ngan and @Khoi stand side by side in the courtyard in full view from head to toe, @Ngan holding @Khoi's hand as he looks down at his clean, healed ankle.
- 7.0–10.0s: @Ngan and @Khoi look at each other in quiet relief as morning sunlight warms the courtyard. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngân siết chặt tay em trai. Vết hằn lạnh buốt nơi cổ chân Khôi, từ sáng hôm ấy, đã nhạt dần như chưa từng có." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind chimes, a soft exhale, distant birds. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 5 (`canh-13/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Morning: the stone courtyard of the old village temple with red pillars and a tiled roof, villagers gathered as blurred figures in the background, soft grey sky.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm over-the-shoulder shot; one smooth camera move from start to end, no cuts.
- Continuity: continues the same moment, place and lighting as the previous shot; same framing axis, no jump.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Over @Ngan's shoulder, @Khoi turns to her and speaks quietly, a tired smile on his face.
- 3.0–7.0s: @Khoi's eyes glisten as he talks, color returning to his cheeks.
- 7.0–10.0s: @Ngan pulls @Khoi into a brief hug. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 0.4–5.9s, spoken on camera by @Khoi (young man of 19, strictly standard Hà Nội strictly standard Hà Nội Northern accent (never Southern accent) (never Southern accent), light tenor, shaky and breathless, speaking at a brisk, urgent, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chị ơi, em không còn nghe thấy tiếng cô ấy gọi nữa. Lần đầu tiên sau mấy tuần, em thấy ấm người." (no subtitles)
- @Khoi's face and lips stay clearly visible while speaking; after the last word @Khoi closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind chimes, birds, soft murmurs of the crowd. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 13 - Clip 6 (`canh-13/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Late afternoon: the temple's back shrine room, the small incense bowl now cleaned, red cloth beneath it and fresh lotus flowers beside it.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 100mm macro insert, slow push-in on the incense bowl; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close on the small incense bowl, now cleaned, sitting on new red cloth beside fresh pink lotus flowers.
- 3.0–7.0s: Three new incense sticks burn straight upward, their smoke rising in still air.
- 7.0–10.0s: A carved wooden name tablet stands behind the bowl, seen from the side so no writing is visible. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–5.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngay tối hôm ấy, cả làng lập đàn cầu siêu cho Thắm, và bát hương không tên cuối cùng đã có chủ." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: incense crackling, distant chanting, wind chimes. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 1 (`canh-14/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: the bank of the lotus pond lit by hundreds of small paper lotus lanterns floating on the black water, a simple altar with incense on the bank, villagers as distant blurred silhouettes.

[CHARACTERS]
- Extra: villagers on the bank as tiny distant silhouettes (unnamed)
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 24mm aerial slow descending glide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Aerial view of the black lotus pond at night, hundreds of small glowing paper lotus lanterns drifting across the water.
- 3.0–7.0s: The drone glides low over the lanterns, their warm light flickering between the dark lotus leaves.
- 7.0–10.0s: The camera settles over the bank where tiny silhouettes kneel before a small altar. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Đêm ấy, hàng trăm ngọn đèn hoa đăng được thả xuống đầm sen, ánh lửa nhỏ lấp lánh trải dài như một dải ngân hà." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft chanting, water lapping, a gentle wind. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 2 (`canh-14/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: the bank of the lotus pond lit by hundreds of small paper lotus lanterns floating on the black water, a simple altar with incense on the bank, villagers as distant blurred silhouettes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot at water level; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Water-level view of glowing paper lotus lanterns floating on the dark pond at night beside the grassy bank.
- 3.0–7.0s: At the water's edge, @BaHanh kneels with @Ngan beside her, placing the silver hairpin inside a paper lotus lantern and setting it gently on the water.
- 7.0–10.0s: The glowing lantern drifts out across the pond as @Ngan puts a comforting arm around @BaHanh's shoulders. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bà Hạnh run run thả chiếc đèn cuối cùng, trên đó bà tự tay đặt chiếc trâm bạc, trả lại cho người con gái năm xưa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: water lapping, soft chanting, a gentle breeze. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 3 (`canh-14/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: the bank of the lotus pond lit by hundreds of small paper lotus lanterns floating on the black water, a simple altar with incense on the bank, villagers as distant blurred silhouettes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @ThamXua = Thắm when alive, a slim 19-year-old orphan village girl; long black hair in a single braid, frightened dark eyes; plain plain white Northern village blouse and black trousers, barefoot.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 85mm telephoto slow push-in across the lanterns; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Telephoto slow push-in across dozens of warm glowing paper lotus lanterns drifting on the calm black water of the pond at night.
- 3.0–7.0s: Between the floating lanterns across the water, @ThamXua appears standing dry and calm in clean white clothes, her hair neatly braided, looking toward the bank.
- 7.0–10.0s: @ThamXua lowers her head in a slow, peaceful bow under the warm lantern light. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Giữa đầm, Thắm hiện lên lần cuối, không còn ướt sũng, áo trắng khô ráo, mái tóc tết gọn gàng như ngày còn sống." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: soft chanting, water lapping, a faint wind chime. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 4 (`canh-14/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: the bank of the lotus pond lit by hundreds of small paper lotus lanterns floating on the black water, a simple altar with incense on the bank, villagers as distant blurred silhouettes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium shot, static; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Static medium view of the grassy pond bank at night, warm golden light from floating paper lanterns reflecting on the water.
- 3.0–7.0s: On the bank, @Khoi steps forward with joined palms and bows three times toward the lantern-lit pond.
- 7.0–10.0s: @Khoi lifts his head, his eyes shining in the warm lantern light as he watches the water. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Khôi đứng trên bờ, chắp tay vái theo. Cậu biết, chiếc đèn có trâm bạc kia vừa dừng lại ngay trước mặt cô gái." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: chanting, lapping water, crickets. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 5 (`canh-14/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: the bank of the lotus pond lit by hundreds of small paper lotus lanterns floating on the black water, a simple altar with incense on the bank, villagers as distant blurred silhouettes.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 50mm slow pull-back over the water; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Close on a cluster of closed lotus buds among the floating lanterns.
- 3.0–7.0s: One after another, the lotus buds slowly open into full pink blooms in the lantern light.
- 7.0–10.0s: The camera pulls back to reveal the whole pond blooming under the moon. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bóng cô gái mờ dần rồi tan vào ánh đèn, và lần đầu tiên sau ba mươi năm, cả đầm sen nở bung giữa đêm trăng." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a soft rustle of opening petals, distant chanting, wind. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 14 - Clip 6 (`canh-14/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: the bank of the lotus pond lit by hundreds of small paper lotus lanterns floating on the black water, a simple altar with incense on the bank, villagers as distant blurred silhouettes.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @OngLy = Ông Lý, 72, the former village chief; tall and gaunt, slicked-back grey hair, hard narrow eyes; faded olive-green collared jacket over a white undershirt, dark trousers, carved wooden walking cane.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm medium two-shot, static; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Medium view of the quiet pond bank at night where hundreds of paper lanterns glow across the dark water in the background.
- 3.0–7.0s: @OngLy stands near the edge of the bank leaning on his cane as @Ngan walks up beside him; @OngLy lifts his head and gives her a slow nod.
- 7.0–10.0s: @Ngan nods once in return, and both look out across the drifting lanterns. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ông Lý đứng tách khỏi đám đông, xin được dựng một tấm bia đá nhỏ bên bờ đầm, để làng đời đời nhớ cái tên Thắm." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: chanting, water lapping, crickets. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 1 (`canh-15/clip-1.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Bright misty morning a year later: the lotus pond in full bloom, a small new stone stele with incense on the bank, the village road beyond.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 24mm aerial slow forward glide; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Aerial view of the vast lotus pond in full pink bloom under a soft morning mist.
- 3.0–7.0s: The drone glides forward over the flowers toward a small new stone stele on the bank, incense smoke rising.
- 7.0–10.0s: The camera settles on the stele, seen from behind so no writing is visible, fresh lotus flowers at its base. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Một năm sau, đầm sen làng Hạ Liên nở rộ chưa từng thấy, và tháng bảy năm ấy không còn ai bị gọi tên nữa." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: morning birds, gentle wind over lotus leaves, a distant temple bell. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 2 (`canh-15/clip-2.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Bright misty morning a year later: the lotus pond in full bloom, a small new stone stele with incense on the bank, the village road beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @BaHanh = Bà Hạnh, 74, their grandmother; small and stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face; brown Northern village blouse, black trousers, wooden prayer beads on her wrist.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 35mm side-tracking shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Morning mist drifting over the blooming pink lotus pond beside a small stone memorial stele on the grassy bank.
- 3.0–7.0s: Only two people, @Ngan and her grandmother @BaHanh, stand side by side before the stone stele as @Ngan places glowing incense sticks in the censer.
- 7.0–10.0s: @BaHanh and @Ngan bow their heads quietly together beside the sunny lotus pond. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Ngân về thăm bà, mang theo bó hương thắp cho Thắm. Bà Hạnh giờ đã khỏe, sáng nào cũng ra bờ đầm quét lá." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birds, a broom sweeping, gentle wind. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 3 (`canh-15/clip-3.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Bright misty morning a year later: the lotus pond in full bloom, a small new stone stele with incense on the bank, the village road beyond.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
- @Khoi = Khôi, 19, Ngân's younger brother, university student home for summer; lanky, short tousled black hair, pale tired face; faded navy T-shirt, grey shorts, white plastic honeycomb sandals.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 50mm medium two-shot; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Medium view of the sunlit embankment path and blooming pink lotus flowers swaying in the morning breeze.
- 3.0–7.0s: @Khoi walks up the embankment to @Ngan looking healthy and bright, gesturing happily toward the blooming lotus pond.
- 7.0–10.0s: @Ngan smiles warmly and ruffles @Khoi's hair. The shot settles on this as its final frame.

[AUDIO]
- Dialogue 3.0–8.3s, spoken on camera by @Khoi (young man of 19, strictly standard Hà Nội strictly standard Hà Nội Northern accent (never Southern accent) (never Southern accent), light tenor, shaky and breathless, speaking at a brisk, urgent, fast-clipped pace, every word spoken once clearly without stutter), in Vietnamese with exact lip-sync, said exactly once: "Chị thấy không, năm nay ai cũng bảo đầm sen đẹp nhất từ trước tới giờ. Chắc cô ấy vui lắm." (no subtitles)
- From 3.0s onward, @Khoi's face and lips stay clearly visible while speaking; after the last word @Khoi closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: birds, light laughter, wind in lotus leaves. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 4 (`canh-15/clip-4.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Late afternoon: a roadside bus stop at the edge of the village, the lotus pond glowing gold behind it.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.
- @Ngan = Ngân, 26, young literature teacher from the city; slim, straight black hair tied low at the neck, calm determined eyes; cream short-sleeve blouse, dark-brown trousers, flat sandals, small cloth shoulder bag.
Nobody else appears in the shot.

[SHOT]
- Framing & motion: 28mm wide shot, slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.
- 0.0–3.0s: Wide slow push-in on a quiet rural roadside bus stop at the edge of the village in golden late-afternoon sunlight, the blooming lotus pond glowing behind it.
- 3.0–7.0s: @Ngan steps up to the bus stop with her small wheeled suitcase and turns to look back over her shoulder at the peaceful pond.
- 7.0–10.0s: @Ngan smiles faintly and turns forward toward the road. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.7s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Chiều hôm ấy, Ngân ra bến xe về thành phố. Ngoảnh lại lần cuối, cô thấy mặt đầm sen yên ả, phẳng lặng như gương." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a distant bus engine approaching, cicadas, wind. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 5 (`canh-15/clip-5.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Dusk: the far corner of the lotus pond, deep shadow under overhanging bamboo, mist on the water.

[CHARACTERS]
- Extra: a distant dark figure standing waist-deep in the pond, face hidden in shadow (unnamed, no reference image)
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 85mm telephoto slow push-in; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: Telephoto view across the darkening pond toward its far corner under overhanging bamboo.
- 3.0–7.0s: The camera slowly pushes in: a dark figure stands waist-deep among the leaves, motionless, face hidden in shadow.
- 7.0–10.0s: The figure slowly turns its head toward the village. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.4s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Nhưng nếu nhìn lâu hơn chút nữa, Ngân sẽ thấy ở góc đầm xa nhất, một bóng người khác đang đứng ngập trong nước." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: wind dying, frogs stopping abruptly, a low hum. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```

---

## Cảnh 15 - Clip 6 (`canh-15/clip-6.md`)

```markdown
One continuous 10-second live-action shot, 16:9 widescreen, 24 fps.

[STYLE]
Photorealistic live-action Vietnamese atmospheric mystery drama film set in a Northern Vietnamese lotus-pond village in the seventh lunar month; gritty grade with deep charcoal-black shadows, murky jade-green water, wet earth browns and pale lotus pinks, natural skin texture, subtle 35mm film grain.

[LIGHTING]
Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.

[LOCATION]
Night: the whole lotus pond from high above under a hazy moon, mist rising.

[CHARACTERS]
No named characters and no other people appear in this shot.

[SHOT]
- Framing & motion: 24mm slow aerial pull-back into darkness; one smooth camera move from start to end, no cuts.
- Continuity: new camera setup; establish the place and light cleanly from the first frame.

[TIMELINE]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame.
- 0.0–3.0s: High above the lotus pond at night, mist drifting over the dark leaves.
- 3.0–7.0s: The camera slowly pulls back and rises as the moon disappears behind clouds.
- 7.0–10.0s: Far below, a single ring of ripples spreads across the black water in the center of the pond. The shot settles on this as its final frame.

[AUDIO]
- Narration 0.4–6.9s by an off-screen male narrator (Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words), in Vietnamese, said exactly once: "Bởi năm ấy, bên bờ đầm, đâu chỉ có một nỗi oan khuất chưa lời giải. Và đầm sen làng Hạ Liên vẫn còn đang đợi." (no subtitles)
- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.
- Nobody on screen speaks; every mouth on screen stays closed.
- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.
- SFX: a deep low drone, wind, a single distant splash. Ambience continues to 10.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.
```
