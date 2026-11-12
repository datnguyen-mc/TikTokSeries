# Bảy Ngày Sinh Tồn (Seven Days in the Stone Age) — Bộ 96 Prompt Google Flow Omni (24 Cảnh × 4 Clips × 15s)

- **Không có người dẫn chuyện:** 100% lời thoại do nhân vật nói trên hình — cả 96 clip là thoại khớp khẩu hình. Giọng gốc của mỗi nhân vật (tuổi, chất giọng) giữ nguyên văn ở mọi clip để Omni không đổi người nói.
- **Nhịp giọng theo cảnh:** mỗi lượt thoại có nhịp riêng nối sau giọng gốc — **nhanh** (cãi vã, hoảng hốt, rượt đuổi, khoe khoang; tốc độ ×1.2), **vừa** (trò chuyện thường), **chậm** (xúc động, thú nhận, câu chốt lặng người; tốc độ ×0.9). Khung thoại tính theo nhịp nên câu chậm ít chữ hơn. Cả phim: 106 lượt nhanh, 108 lượt vừa, 65 lượt chậm.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 96 clips × 15s, tất cả là clip thoại (9 clip có hai lượt thoại); lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 18 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 78 clip ảnh nhân vật (Ingredients), 0 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** không có clip VO nên runner không tăng tốc giọng clip nào; tốc độ nói nằm trong prompt (nhịp từng lượt) để khớp khẩu hình.
- **Màu phim & ánh sáng:** Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py bay-ngay-sinh-ton` sinh lại toàn bộ clip, README, kịch bản.

---

## Cảnh 01 - Clip 1 (`canh-01/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Cúc Phương primeval forest in northern Vietnam today, late afternoon: giant old trees with huge buttress roots, thick lianas, ferns and mossy limestone boulders, green-gold sunlight slanting through the canopy, a narrow paved visitor road glimpsed through the leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium shot of the YouTuber kneeling at the giant buttress root with a fat worm held up to his chest camera, slow push-in.
- Shot 2, 6–10s: 85mm close-up of the cameraman lowering his gimbal, locked off.
- Shot 3, 10–13s: 40mm medium two-shot of both men at the buttress root, slight handheld drift.
- Shot 4, 13–15s: 100mm extreme close-up of the worm on a broad fern leaf, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang kneels at the giant buttress root, pinches a fat wriggling worm between two fingers and is already speaking to his chest camera in a pained, theatrical voice.
- 1–2s (Shot 1): @Khang keeps talking fast, scrunching his face in mock agony as he lifts the worm toward the little lens.
- 2–3s (Shot 1): @Khang presses his free hand to his stomach and sways, still talking, eyes squeezed half shut.
- 3–4s (Shot 1): @Khang tilts his head back and dangles the worm above his face while he keeps speaking.
- 4–5s (Shot 1): @Khang raises the worm higher, voice trembling for effect, as the speech reaches its big finish.
- 5–6s (Shot 1): @Khang finishes the line, closes his mouth and freezes with the worm just above his lips in a heroic pose.
- 6–7s (CUT to Shot 2): @Bin lowers the gimbal from his eye and starts speaking in a flat, unbothered voice, his face completely deadpan.
- 7–8s (Shot 2): @Bin keeps talking as he holds up an empty, crumpled bag of gummy candy and shakes it once.
- 8–9s (Shot 2): @Bin points one finger at the wriggling worm while he goes on, eyebrows never moving.
- 9–10s (Shot 2): @Bin finishes the sentence and closes his mouth, staring over the top of his round glasses.
- 10–11s (CUT to Shot 3): @Khang stares at the worm wriggling between his fingers and starts speaking fast, eyes wide, nose wrinkled.
- 11–12s (Shot 3): @Khang tosses the worm away over his shoulder, still talking quickly and wiping his fingers on his cargo trousers.
- 12–13s (Shot 3): @Khang finishes, closes his mouth and scrambles to his feet, waving @Bin toward a pile of dry sticks.
- 13–14s (CUT to Shot 4): In extreme close-up the fat worm lands on a broad fern leaf and wriggles calmly in the green-gold light.
- 14–15s (Shot 4): The worm inches along the fern leaf while two pairs of shoes walk away across the leaf litter in soft focus behind it. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.1s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, theatrical suffering, hamming it up for the lens): "Day three. No food, no clean water. I have no choice, I have to eat this worm to survive!"
- Turn 2, 6.6–10.2s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking at a natural, even conversational pace, flat and deadpan, utterly unbothered): "Cut! Khang, we're out of gummy worms. That one's real."
- Turn 3, 10.7–12.5s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, grossed out, tossing the worm away): "Real? Forget it. Fire scene first."
- Pacing: @Khang speaks quickly, then @Bin answers at an even everyday pace, then @Khang answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: insects buzzing and birdsong in the canopy, distant gibbon calls, dry leaves crunching under knees, the crinkle of an empty plastic candy bag, the soft whir of a gimbal motor. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 01 - Clip 2 (`canh-01/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Cúc Phương primeval forest in northern Vietnam today, late afternoon: giant old trees with huge buttress roots, thick lianas, ferns and mossy limestone boulders, green-gold sunlight slanting through the canopy, a narrow paved visitor road glimpsed through the leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 24mm wide shot of the YouTuber spinning a wooden drill over a pile of tinder while the cameraman crouches hidden behind the buttress root at frame right, locked off.
- Shot 2, 4–7s: 85mm close-up of the cameraman stepping out from behind the root with a lighter, slow push-in.
- Shot 3, 7–10s: 50mm over-the-shoulder shot from behind the YouTuber onto the cameraman, locked off.
- Shot 4, 10–15s: 40mm medium two-shot of the YouTuber hissing at the cameraman beside the smoking tinder, handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang kneels over a pile of dry tinder, spinning a wooden drill between his palms like a kung fu star, and is already speaking loudly to his chest camera.
- 1–2s (Shot 1): Behind the buttress root @Bin, crouched out of the YouTuber's view, reaches round and touches a small lighter flame to the tinder while @Khang keeps talking.
- 2–3s (Shot 1): A curl of white smoke rises from the tinder; @Khang keeps spinning and talking faster, eyes wide in staged amazement.
- 3–4s (Shot 1): @Khang springs to his feet with both fists raised high, finishes his triumphant line and closes his mouth in a frozen victory pose.
- 4–5s (CUT to Shot 2): @Bin steps out from behind the root holding up the lighter and starts speaking in a bored, flat voice.
- 5–6s (Shot 2): @Bin keeps talking as he flicks the lighter once, a small steady flame standing up in front of his round glasses.
- 6–7s (Shot 2): @Bin lets the flame go out and goes on in the same flat tone, tilting his head toward the smoking pile.
- 7–8s (CUT to Shot 3): @Bin keeps speaking, holding up three fingers of his free hand, face expressionless.
- 8–9s (Shot 3): @Bin lowers the hand and keeps talking, eyes fixed on @Khang over the rims of his glasses.
- 9–10s (Shot 3): @Bin finishes the last words with a tiny shrug and closes his mouth.
- 10–11s (CUT to Shot 4): @Khang darts to @Bin's side, cups one hand over the little camera on his own chest and starts whispering sharply.
- 11–12s (Shot 4): @Khang keeps whispering fast through his teeth, eyes darting left and right, hand pressed over the lens.
- 12–13s (Shot 4): @Khang jabs a finger toward the small microphone on his harness, still whispering urgently into @Bin's face.
- 13–14s (Shot 4): @Khang finishes, closes his mouth and glares at @Bin, nostrils flaring, while @Bin blinks back, mouth closed.
- 14–15s (Shot 4): Beside them the tinder keeps smoking on the forest floor as @Bin slips the lighter into his yellow windbreaker pocket, both mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, showman bravado, playing to the lens): "Friction, friction, patience makes fire! There's smoke! I can survive anywhere!"
- Turn 2, 4.2–10.0s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking at a natural, even conversational pace, bored and flat, stating the obvious): "That's my lighter. Three years, I've lit every fire for you. You've never made one yourself."
- Turn 3, 10.5–13.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, a sharp hissed whisper, scolding): "Keep your voice down! The mic picks up everything."
- Pacing: @Khang speaks quickly, then @Bin answers at an even everyday pace, then @Khang answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a wooden drill whirring against a board, the click and hiss of a pocket lighter, crackling tinder catching, birdsong and insects in the canopy, leaves rustling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 01 - Clip 3 (`canh-01/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Cúc Phương primeval forest in northern Vietnam today, late afternoon: giant old trees with huge buttress roots, thick lianas, ferns and mossy limestone boulders, green-gold sunlight slanting through the canopy, a narrow paved visitor road glimpsed through the leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
- Extra: a few cheerful tourists in sun hats riding a white open-sided electric shuttle along the paved road, small and far behind the leaves in soft focus, waving
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 40mm medium two-shot of both men by the buttress root with the gap in the leaves and the paved road behind the YouTuber, locked off.
- Shot 2, 4–10s: 24mm wide shot of the YouTuber spreading his arms across the gap in the leaves as the shuttle rolls past behind him, handheld.
- Shot 3, 10–15s: 85mm close-up of the cameraman behind his gimbal, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bin, gimbal in one hand, is already speaking in a flat voice and lifts his other hand to point past @Khang's shoulder.
- 1–2s (Shot 1): @Bin keeps talking evenly while, through the leaves behind @Khang, a white open-sided electric shuttle glides along the paved road.
- 2–3s (Shot 1): The tourists on the shuttle wave cheerfully toward the men as @Bin goes on, his pointing finger never moving.
- 3–4s (Shot 1): @Bin finishes, closes his mouth and lowers his hand, while @Khang's eyes go wide.
- 4–5s (CUT to Shot 2): @Khang glances back at the road, whips round to face the gimbal again and starts speaking fast, flapping one hand.
- 5–6s (Shot 2): @Khang steps sideways into the gap in the leaves and spreads both arms wide to hide the shuttle, still talking quickly.
- 6–7s (Shot 2): @Khang keeps talking, bobbing left and right to keep his body between the gimbal and the rolling shuttle.
- 7–8s (Shot 2): @Khang waggles his fingers in the air like drifting fog while he keeps speaking.
- 8–9s (Shot 2): @Khang flaps both hands up toward the canopy, still talking, eyebrows raised high.
- 9–10s (Shot 2): @Khang finishes, closes his mouth and stays frozen with his arms spread across the gap, panting.
- 10–11s (CUT to Shot 3): @Bin regards him over the gimbal and answers slowly with a thin, dry smile.
- 11–12s (Shot 3): @Bin keeps talking slowly, tilting his head, the brim of his bucket hat shading his round glasses.
- 12–13s (Shot 3): @Bin lets a small pause hang, then goes on in the same lazy, teasing voice.
- 13–14s (Shot 3): @Bin keeps speaking slowly, lifting the gimbal back up toward his eye.
- 14–15s (Shot 3): @Bin finishes, closes his mouth and waits behind the gimbal with the same thin smile. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking at a natural, even conversational pace, flat and matter-of-fact): "Khang, the tourist shuttle drove behind you. Third time. They waved."
- Turn 2, 4.9–9.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, flustered, waving it away): "So cut it! Make it look like deep jungle. Add monkey howls, add some fog."
- Turn 3, 9.9–14.3s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking slowly and softly, unhurried, with a short natural pause between phrases, dry, with a thin teasing smile): "Sure. So, tonight at the guesthouse, goat hotpot or hill chicken?"
- Pacing: @Bin speaks at an even everyday pace, then @Khang answers quickly, then @Bin answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the soft electric whine and rolling tires of a passing open shuttle on asphalt, birdsong and cicadas, leaves rustling, boots shuffling on dry leaves. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 01 - Clip 4 (`canh-01/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Cúc Phương primeval forest in northern Vietnam today, late afternoon: giant old trees with huge buttress roots, thick lianas, ferns and mossy limestone boulders, green-gold sunlight slanting through the canopy, a narrow paved visitor road glimpsed through the leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the cameraman reading from his glowing phone, locked off.
- Shot 2, 5–8s: 50mm medium shot of the YouTuber glancing at the phone and folding his arms, slow push-in.
- Shot 3, 8–10s: 85mm close-up of the YouTuber rolling his eyes, locked off.
- Shot 4, 10–15s: 50mm over-the-shoulder shot from behind the YouTuber onto the cameraman, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bin swipes his phone with a thumb, its screen only a soft glow, and is already speaking fast as if reading aloud.
- 1–2s (Shot 1): @Bin keeps reading quickly, eyes flicking across the glowing screen, completely deadpan.
- 2–3s (Shot 1): @Bin turns the glowing phone toward @Khang without looking up, still talking.
- 3–4s (Shot 1): @Bin keeps talking briskly, tapping the glowing screen with one finger, the gimbal hanging from his other hand.
- 4–5s (Shot 1): @Bin finishes the last words, closes his mouth and holds the phone out at arm's length.
- 5–6s (CUT to Shot 2): @Khang glances at the glowing screen for a single second, curls his lip and starts speaking in a lazy, scornful voice.
- 6–7s (Shot 2): @Khang folds his arms across his chest harness, still talking, chin lifted.
- 7–8s (Shot 2): @Khang tilts his head back as he keeps speaking, a lopsided smirk on his face.
- 8–9s (CUT to Shot 3): @Khang rolls his eyes up toward the canopy and goes on, giving a little dismissive snort.
- 9–10s (Shot 3): @Khang finishes, closes his mouth and keeps his arms folded over the chest harness, smirking.
- 10–11s (CUT to Shot 4): @Bin slowly lowers the phone and answers slowly, looking straight at @Khang.
- 11–12s (Shot 4): @Bin keeps speaking quietly and evenly, his eyes steady behind the round glasses.
- 12–13s (Shot 4): @Bin keeps talking slowly, not blinking behind his round glasses, letting each word land.
- 13–14s (Shot 4): @Bin finishes the question, closes his mouth and waits in silence, the phone hanging at his side.
- 14–15s (Shot 4): In the foreground @Khang's folded arms slowly loosen and his head tilts, the smirk gone, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, reading aloud fast, deadpan): "This comment: five-star survival, sleeps in a guesthouse, eats goat hotpot. Ten thousand likes."
- Turn 2, 5.4–9.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, smug and dismissive): "Keyboard warriors. One night out here and they'd cry for mommy."
- Turn 3, 9.9–13.9s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and pointed, no smile): "Have you ever spent one real night in the jungle?"
- Pacing: @Bin speaks quickly, then @Khang answers at an even everyday pace, then @Bin answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: cicadas and birdsong in the late afternoon canopy, a thumb tapping a phone screen, leaves shifting underfoot, a soft breeze in the ferns. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 02 - Clip 1 (`canh-02/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night inside a wooden stilt-house guesthouse room at the edge of the forest: warm yellow lamp light, woven bamboo walls, a low wooden table with a small hotpot bubbling on a portable gas stove, a window where silent lightning flickers over dark limestone peaks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot across the low table with the hotpot steaming between them, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the YouTuber sputtering over the hotpot, handheld.
- Shot 3, 10–15s: 50mm over-the-shoulder shot from behind the YouTuber onto the cameraman, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bin leans across the low table and is already speaking fast, pushing his glowing phone right up to @Khang's face.
- 1–2s (Shot 1): @Khang freezes with his chopsticks halfway to his mouth, a strip of goat meat dangling, while @Bin keeps talking.
- 2–3s (Shot 1): @Bin keeps talking quickly, waggling the glowing phone a hand's width from @Khang's nose.
- 3–4s (Shot 1): @Bin taps the glowing screen twice, eyebrows high, still speaking with a gleeful grin.
- 4–5s (Shot 1): @Bin finishes and closes his mouth as @Khang sputters and coughs on the hot broth, eyes watering.
- 5–6s (CUT to Shot 2): @Khang drops his chopsticks on the table with a clatter and starts speaking fast in a hoarse voice.
- 6–7s (Shot 2): @Khang keeps talking hoarsely, thumping his own chest with the flat of his hand, eyes streaming.
- 7–8s (Shot 2): @Khang points across the table, then at himself, still talking fast, cheeks flushed from the broth.
- 8–9s (Shot 2): @Khang counts on three fingers as he keeps talking, leaning forward over the steaming pot.
- 9–10s (Shot 2): @Khang finishes, closes his mouth and stares, breathing hard through his nose.
- 10–11s (CUT to Shot 3): @Bin sets the glowing phone face down on the table and answers slowly, totally deadpan.
- 11–12s (Shot 3): @Bin keeps speaking slowly, picking up his own chopsticks and lifting a piece of meat from the pot.
- 12–13s (Shot 3): @Bin finishes the sentence with a tiny shrug, closes his mouth and starts to chew.
- 13–14s (Shot 3): @Khang slumps back against the woven bamboo wall and stares at the ceiling, mouth closed, while @Bin chews calmly.
- 14–15s (Shot 3): Silent lightning flickers in the window behind them as the hotpot keeps bubbling, both men silent, mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, fast and gleeful, rubbing it in): "Khang, someone filmed you ordering pizza delivery into the jungle. Two million views already!"
- Turn 2, 5.1–9.3s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, hoarse and sputtering, outraged): "Who filmed it? That night it was just you, me, and the delivery guy!"
- Turn 3, 9.8–13.0s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow, dry, deadpan): "The delivery guy is subscribed to your channel."
- Pacing: @Bin speaks quickly, then @Khang answers quickly, then @Bin answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: hotpot broth bubbling on a portable gas stove, the low hiss of the burner, chopsticks clattering on wood, rain pattering on the roof, distant rolling thunder. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 02 - Clip 2 (`canh-02/clip-2.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night inside a wooden stilt-house guesthouse room at the edge of the forest: warm yellow lamp light, woven bamboo walls, a low wooden table with a small hotpot bubbling on a portable gas stove, a window where silent lightning flickers over dark limestone peaks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm over-the-shoulder shot from behind the YouTuber onto the cameraman reading his buzzing phone, slow push-in.
- Shot 2, 6–9s: 85mm close-up of the YouTuber shooting up to his feet with his multitool, handheld tilt up.
- Shot 3, 9–15s: 40mm medium two-shot across the low table, the YouTuber standing and the cameraman seated, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bin's phone buzzes on the table; he picks it up, its screen only a soft glow, and is already speaking in an even voice as he reads.
- 1–2s (Shot 1): @Bin keeps talking, eyes moving across the glowing screen, his face sagging little by little.
- 2–3s (Shot 1): @Bin pushes his round glasses up his nose with one finger, still reading aloud evenly.
- 3–4s (Shot 1): @Bin keeps speaking, lips pressed thin between phrases, his shoulders dropping inside the yellow windbreaker.
- 4–5s (Shot 1): @Bin lowers the phone and looks up over his glasses, finishing the last words.
- 5–6s (Shot 1): @Bin closes his mouth and sets the glowing phone down beside the hotpot.
- 6–7s (CUT to Shot 2): @Khang shoots up to his feet, knocking the table edge with his knee, and starts speaking fast, voice cracking.
- 7–8s (Shot 2): @Khang pulls the red folding multitool from his belt pouch and holds it up beside his face, still talking fast.
- 8–9s (Shot 2): @Khang finishes, closes his mouth and shakes the multitool in the air, chest heaving.
- 9–10s (CUT to Shot 3): @Bin looks up at him from his floor cushion and answers slowly, without a trace of a smile.
- 10–11s (Shot 3): @Bin keeps speaking slowly, miming a tiny sawing motion with two fingers as if cutting a sandwich.
- 11–12s (Shot 3): @Bin goes on in the same flat voice, picking up the glowing phone again.
- 12–13s (Shot 3): @Bin keeps talking slowly, turning the glowing phone toward @Khang like evidence.
- 13–14s (Shot 3): @Bin keeps speaking slowly, a hint of pity in his raised eyebrows above the round glasses.
- 14–15s (Shot 3): @Bin finishes, closes his mouth and sets the phone down, while @Khang's hand with the multitool slowly sinks. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking at a natural, even conversational pace, reading bad news, slowly deflating): "The multitool brand just texted. They're canceling the sponsorship and want the deposit back."
- Turn 2, 5.9–8.9s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, outraged, voice cracking): "Canceling? Three years I've promoted their multitools! They cut anything!"
- Turn 3, 9.4–14.2s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow, pitiless and deadpan): "You only cut sandwiches and shoelaces. Three million subscribers know it now."
- Pacing: @Bin speaks at an even everyday pace, then @Khang answers quickly, then @Bin answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a phone buzzing on a wooden table, hotpot bubbling, a floor cushion scraping as someone stands, rain on the roof, distant thunder. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 02 - Clip 3 (`canh-02/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night inside a wooden stilt-house guesthouse room at the edge of the forest: warm yellow lamp light, woven bamboo walls, a low wooden table with a small hotpot bubbling on a portable gas stove, a window where silent lightning flickers over dark limestone peaks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 40mm medium two-shot of the YouTuber buckling on his chest harness by the table as lightning flickers in the window, slow push-in.
- Shot 2, 5–10s: 24mm wide shot of the cameraman spreading his arms across the doorway, handheld.
- Shot 3, 10–13s: 85mm close-up of the YouTuber's steady face, locked off.
- Shot 4, 13–15s: 35mm over-the-shoulder shot from behind the YouTuber onto the cameraman in the doorway, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang looks at the silent lightning flickering in the window and is already speaking, fast and determined, jaw set.
- 1–2s (Shot 1): @Khang picks the black chest harness up from the table and lifts it over his head, still talking.
- 2–3s (Shot 1): @Khang settles the small camera at the center of his chest, still speaking quickly.
- 3–4s (Shot 1): @Khang snaps the harness buckle shut with a loud click, eyes fixed ahead as he talks.
- 4–5s (Shot 1): @Khang tugs the strap tight, finishes his words and closes his mouth.
- 5–6s (CUT to Shot 2): @Bin darts to the doorway, plants himself in it with both arms spread across the frame and starts speaking fast.
- 6–7s (Shot 2): @Bin keeps talking urgently, nodding out toward the flickering storm without leaving the doorway.
- 7–8s (Shot 2): @Bin shakes his head hard, glasses slipping, still talking fast with his arms spread.
- 8–9s (Shot 2): @Bin keeps speaking, voice rising, bucket hat askew, palms flat on both sides of the door frame.
- 9–10s (Shot 2): @Bin finishes the question and closes his mouth, still blocking the doorway, breathing hard.
- 10–11s (CUT to Shot 3): @Khang looks at him calmly and answers at an even pace, eyes steady.
- 11–12s (Shot 3): @Khang keeps speaking evenly, tapping the camera on his chest once with two fingers.
- 12–13s (Shot 3): @Khang finishes, closes his mouth and gives a single firm nod, lightning glinting on the little camera lens.
- 13–14s (CUT to Shot 4): Over @Khang's shoulder @Bin stays in the doorway, slowly lowering his arms, mouth closed.
- 14–15s (Shot 4): @Khang steps toward the door as white lightning flickers across the window, both men silent, mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, decisive, chin up): "Fine. Tonight I sleep alone in the Cave of Hands. Real footage. No cuts."
- Turn 2, 5.1–9.3s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, alarmed, pleading fast): "There's a storm coming! The cave is closed! You'd risk your life for views?"
- Turn 3, 9.8–12.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, calm and final): "Wait at the ranger station. Six a.m."
- Pacing: @Khang speaks quickly, then @Bin answers quickly, then @Khang answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: rain drumming on the roof, thunder rolling over the mountains, the click of a plastic buckle, nylon straps tightening, a wooden floor creaking under quick steps. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 02 - Clip 4 (`canh-02/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night inside a wooden stilt-house guesthouse room at the edge of the forest: warm yellow lamp light, woven bamboo walls, a low wooden table with a small hotpot bubbling on a portable gas stove, a window where silent lightning flickers over dark limestone peaks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm over-the-shoulder shot from behind the YouTuber onto the cameraman in the doorway, his face lit from below, locked off.
- Shot 2, 4–8s: 85mm close-up of the cameraman's face lit from below by his glowing phone, slow push-in.
- Shot 3, 8–11s: 50mm medium shot of the YouTuber shouldering the orange backpack with a grin, locked off.
- Shot 4, 11–15s: 24mm wide shot from the dark veranda back toward the lit doorway, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bin holds his glowing phone under his chin so the light hits his face from below and is already speaking in a low, spooky voice.
- 1–2s (Shot 1): @Bin keeps talking slowly and mysteriously, widening his eyes behind the round glasses.
- 2–3s (Shot 1): @Bin raises his free hand and wiggles his fingers like falling rain as he goes on.
- 3–4s (Shot 1): @Bin leans closer, still speaking in a hushed storyteller's voice, the light trembling on his face.
- 4–5s (CUT to Shot 2): @Bin keeps telling the tale, eyes darting toward the window and back.
- 5–6s (Shot 2): @Bin spreads his hand slowly in the air as if a flash of lightning were opening, still speaking low.
- 6–7s (Shot 2): @Bin keeps talking, his eyebrows climbing as the tale reaches its end.
- 7–8s (Shot 2): @Bin finishes the legend, lowers the phone and closes his mouth, watching @Khang.
- 8–9s (CUT to Shot 3): @Khang swings the bright orange backpack onto one shoulder, grins and answers at an easy pace.
- 9–10s (Shot 3): @Khang keeps talking with a showman's wink, tapping the camera on his chest with a thumb.
- 10–11s (Shot 3): @Khang finishes, closes his mouth and steps past @Bin through the doorway, still grinning.
- 11–12s (CUT to Shot 4): @Khang strides out onto the dark wooden veranda toward the camera as @Bin, in the lit doorway behind him, starts calling after him fast.
- 12–13s (Shot 4): @Bin keeps talking quickly from the doorway, one hand raised, leaning out into the rain.
- 13–14s (Shot 4): @Bin finishes and closes his mouth as a white flash of lightning lights the veranda and the peaks beyond.
- 14–15s (Shot 4): In the white flash @Khang, backpack on, raises one hand over his shoulder without turning round, both mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.6s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking at a natural, even conversational pace, low and spooky, telling a ghost story): "Villagers say a god once stepped out of the lightning, taught the cave people fire, then left with the thunder."
- Turn 2, 8.1–10.3s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, amused, a cocky grin): "Nice. Tonight I'll be that god."
- Turn 3, 10.8–13.5s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, calling after him, teasing): "A god who needs me to light his fires?"
- Pacing: @Bin speaks at an even everyday pace, then @Khang answers at an even everyday pace, then @Bin answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: heavy rain on the roof, the hiss of the gas stove, wooden floorboards creaking under boots, wind gusting through the open door, a loud crack of thunder with the lightning flash. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 03 - Clip 1 (`canh-03/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night inside a large limestone cave today during a raging storm: a wide arched mouth, a huge stalactite shaped like an elephant, a dry earthen floor, a rock wall covered with hundreds of faded red-ochre hand stencils with one bigger hand in the middle and a slightly smaller hand beside it, sheets of rain and white lightning beyond the entrance, light only from a headlamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 24mm wide shot from deep inside the cave toward the rain-filled mouth, the YouTuber sitting cross-legged in the headlamp's pool of light, locked off.
- Shot 2, 4–8s: 50mm medium shot of the YouTuber holding the small camera out toward his face, slow push-in.
- Shot 3, 8–13s: 85mm close-up of his headlamp-lit face staring into the little lens, locked off.
- Shot 4, 13–15s: 35mm over-the-shoulder shot from behind the YouTuber toward the rain-filled cave mouth, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang sits cross-legged on the dry earthen floor, a headlamp on his forehead, holding the small camera out at arm's length, and is already whispering to it.
- 1–2s (Shot 1): @Khang keeps whispering, turning his head slowly so the headlamp beam slides across the elephant-shaped stalactite above.
- 2–3s (Shot 1): Behind him a sheet of rain pours across the cave mouth as @Khang keeps talking in a hushed voice.
- 3–4s (Shot 1): @Khang swings the camera briefly toward the rain at the entrance, still whispering, then brings it back to his face.
- 4–5s (CUT to Shot 2): @Khang leans in toward the little lens and keeps speaking softly, eyes glinting in the headlamp light.
- 5–6s (Shot 2): @Khang shakes his head slowly as he goes on, a drop of rainwater running down his temple.
- 6–7s (Shot 2): @Khang jerks a thumb back toward the pouring rain as he finishes the sentence.
- 7–8s (Shot 2): @Khang closes his mouth for a breath, then stares straight into the little lens and starts speaking again, faster.
- 8–9s (CUT to Shot 3): @Khang keeps talking fast and intense, pointing a finger at the lens, jaw tight.
- 9–10s (Shot 3): @Khang narrows his eyes and leans closer, still talking quickly to the camera.
- 10–11s (Shot 3): @Khang taps his own chest twice as he keeps speaking, the headlamp beam bobbing.
- 11–12s (Shot 3): @Khang holds the stare through the last words, nostrils flaring, rain roaring at the mouth behind him.
- 12–13s (Shot 3): @Khang finishes, closes his mouth and holds the camera steady, breathing hard through his nose.
- 13–14s (CUT to Shot 4): Over his shoulder a white flash of lightning fills the cave mouth and lights the wall of red hands for an instant, his mouth closed.
- 14–15s (Shot 4): Thunder rolls; @Khang turns his head toward the wall of faded red hands, the headlamp beam swinging onto them, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in two parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–7.2s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, hushed whisper, half thrilled): "Eleven p.m., in the Cave of Hands. Nobody with me. Nobody lighting my fires. That rain is real."
- Part 2, 7.7–12.5s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, intense, eyes locked on the lens): "So if you think I fake it, watch closely. This time it's one hundred percent real."
- Pacing: @Khang speaks at an even everyday pace, then @Khang continues quickly; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: heavy rain roaring at the cave mouth, water dripping from the stalactite, wind moaning through the cave, a deep roll of thunder after a lightning flash. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 03 - Clip 2 (`canh-03/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night inside a large limestone cave today during a raging storm: a wide arched mouth, a huge stalactite shaped like an elephant, a dry earthen floor, a rock wall covered with hundreds of faded red-ochre hand stencils with one bigger hand in the middle and a slightly smaller hand beside it, sheets of rain and white lightning beyond the entrance, light only from a headlamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the YouTuber walking along the rock wall as his headlamp beam sweeps the faded red hands, slow pan.
- Shot 2, 4–8s: 24mm wide shot of the hand-stencilled wall with the bigger red hand in the middle and the YouTuber in profile before it, slow push-in.
- Shot 3, 8–11s: 85mm close-up of the YouTuber's face in profile as he raises his hand toward the wall, locked off.
- Shot 4, 11–15s: 50mm medium shot in profile of the YouTuber with his palm flat inside the big red hand, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang walks slowly along the rock wall, the headlamp beam sliding over rows of faded red handprints, and is already speaking softly in awe.
- 1–2s (Shot 1): @Khang keeps talking slowly, hovering his fingertips just off the faded red stencils.
- 2–3s (Shot 1): The headlamp beam drifts across hundreds of small red hands as @Khang goes on in a low, reverent voice.
- 3–4s (Shot 1): @Khang finishes, closes his mouth and stops, the beam settling on one red hand much bigger than all the rest.
- 4–5s (CUT to Shot 2): @Khang steps back to take in the whole wall and starts speaking again at an easy pace, half grinning to his chest camera.
- 5–6s (Shot 2): @Khang keeps talking, nodding up at the big red hand in the middle of the wall.
- 6–7s (Shot 2): @Khang wipes his right palm on his trousers as he goes on, playing it up for the viewers.
- 7–8s (Shot 2): @Khang keeps speaking, spreading his fingers wide and wiggling them toward the camera on his chest.
- 8–9s (CUT to Shot 3): @Khang raises his open hand toward the big red stencil, still talking with a showman's smirk.
- 9–10s (Shot 3): @Khang keeps talking as his palm moves closer to the rock, the headlamp lighting his fingers.
- 10–11s (Shot 3): @Khang finishes the sentence and closes his mouth, holding his breath, palm a finger's width from the wall.
- 11–12s (CUT to Shot 4): @Khang presses his palm flat into the big red hand, every finger matching the outline exactly, and starts speaking fast, eyes widening.
- 12–13s (Shot 4): @Khang keeps talking quickly, glancing from his hand to the chest camera and back, a laugh rising in his voice.
- 13–14s (Shot 4): @Khang finishes with a short delighted laugh and closes his mouth, hand still flat on the stencil.
- 14–15s (Shot 4): @Khang stays with his palm pressed to the wall, grinning in disbelief, mouth closed, as lightning flickers faintly behind him. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–4.0s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, hushed and awed): "Here they are. Hundreds of ancient handprints, red ochre."
- Part 2, 4.5–10.6s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, playful, hamming it up for viewers): "Locals say the biggest one is the fire god's hand. Let's see how big a god is."
- Part 3, 11.1–13.8s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, amazed, breaking into a laugh): "Oh... perfect fit. The god's hand is my size?"
- Pacing: @Khang speaks slowly and calmly, then @Khang continues at an even everyday pace, then @Khang continues quickly; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: rain roaring outside the cave mouth, steady dripping water, boots scuffing on dry earth, a palm patting cool rock, distant thunder. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 03 - Clip 3 (`canh-03/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night inside a large limestone cave today during a raging storm: a wide arched mouth, a huge stalactite shaped like an elephant, a dry earthen floor, a rock wall covered with hundreds of faded red-ochre hand stencils with one bigger hand in the middle and a slightly smaller hand beside it, sheets of rain and white lightning beyond the entrance, light only from a headlamp.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot in profile of the YouTuber with his palm on the stencil as dust rains from the ceiling, handheld shake.
- Shot 2, 4–8s: 85mm close-up of the YouTuber's straining face, handheld.
- Shot 3, 8–13s: 35mm medium shot of the YouTuber turning his face to his chest camera, his hand glowing on the wall, slow push-in.
- Shot 4, 13–15s: 100mm extreme close-up of his hand on the red stencil with white light pouring between the fingers, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): A deep boom of thunder shakes the cave; @Khang, palm still on the wall, is already shouting fast, eyes darting up to the ceiling.
- 1–2s (Shot 1): Dust and grit trickle down from the elephant-shaped stalactite as @Khang keeps shouting, ducking his head.
- 2–3s (Shot 1): @Khang keeps talking fast, the headlamp beam jerking across the trembling rock as he looks around.
- 3–4s (Shot 1): @Khang finishes, closes his mouth and tries to pull his hand off the wall, but it does not move.
- 4–5s (CUT to Shot 2): @Khang tugs his arm back hard and starts shouting fast again, his palm stuck flat on the big red hand.
- 5–6s (Shot 2): @Khang braces his other hand and one boot against the wall and pulls, still talking fast through clenched teeth.
- 6–7s (Shot 2): A thin white glow seeps out between his fingers as @Khang keeps shouting, sweat shining on his forehead.
- 7–8s (Shot 2): @Khang winces at the heat rising from the rock, breath hissing, and finishes the sentence.
- 8–9s (CUT to Shot 3): @Khang closes his mouth, stops pulling, turns his face down to the camera on his chest and begins speaking slowly, voice low.
- 9–10s (Shot 3): @Khang keeps speaking slowly to the little lens, his face lit white from the glowing wall.
- 10–11s (Shot 3): @Khang swallows and goes on softly, eyes shining, the white light growing brighter around him.
- 11–12s (Shot 3): @Khang keeps talking softly to the lens, a small crooked smile on his lips.
- 12–13s (Shot 3): @Khang finishes, closes his mouth and looks back at his glowing hand.
- 13–14s (CUT to Shot 4): Blinding white light pours out between his fingers on the red hand stencil as the rock trembles.
- 14–15s (Shot 4): A white flash of lightning swallows the whole frame until everything is pure white. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in two parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–7.6s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, panicked, shouting over thunder, breathless): "Hear that? Lightning, right above us! The cave is shaking! My hand's stuck! I can't pull it off! The rock's getting hot like coal!"
- Part 2, 8.1–11.7s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and sincere, to the lens): "Bin, if you ever see this... don't cut anything."
- Pacing: @Khang speaks quickly, then @Khang continues slowly and calmly; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 11.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a deafening thunderclap right overhead, rock rumbling and grinding, grit pattering on the floor, a rising electric hum and crackle from the wall, a final sharp crack of thunder with the white flash. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 03 - Clip 4 (`canh-03/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Misty dawn on a sandy bank of a clear jungle stream at the foot of a towering limestone cliff, more than ten thousand years ago: untouched giant trees, reeds, smooth river stones, birdsong, no roads, no buildings, no people.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm close-up of the YouTuber's face resting on the wet sand as his eyes open, locked off.
- Shot 2, 4–7s: 24mm wide shot of the misty stream bank at the foot of the towering limestone cliff, the YouTuber sitting up beside his orange backpack, slow pull-back.
- Shot 3, 7–10s: 35mm medium shot of the YouTuber on his knees calling toward the reeds, handheld.
- Shot 4, 10–15s: 85mm close-up of the YouTuber looking down at his chest camera with its tiny red light, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang lies on his side on the wet sand, cheek in the grit, eyes fluttering open, and is already speaking slowly in a groggy voice.
- 1–2s (Shot 1): @Khang keeps talking slowly, pressing one hand to his forehead and squinting into the pale mist.
- 2–3s (Shot 1): @Khang pushes himself up on one elbow, still speaking slowly, sand stuck to his cheek.
- 3–4s (Shot 1): @Khang blinks at the clear stream sliding past his boots as he keeps talking, voice thick and dazed.
- 4–5s (CUT to Shot 2): @Khang sits up beside his bright orange backpack beneath the towering limestone cliff and keeps speaking, looking around.
- 5–6s (Shot 2): @Khang finishes the question, closes his mouth and turns his head slowly from the stream to the giant trees.
- 6–7s (Shot 2): @Khang gets up onto his knees, raises one hand to the side of his face and calls out loudly toward the reeds.
- 7–8s (CUT to Shot 3): @Khang keeps shouting into the mist, turning left and right, eyes narrowed.
- 8–9s (Shot 3): @Khang finishes calling, closes his mouth and listens; only birdsong answers from the giant trees.
- 9–10s (Shot 3): @Khang looks down at the small camera on his chest, sees its tiny red light still glowing, and starts talking fast with a shaky laugh.
- 10–11s (CUT to Shot 4): @Khang lifts the camera on its harness toward his face and keeps talking quickly, grinning with a trembling jaw.
- 11–12s (Shot 4): @Khang pats his own chest and arms as if checking he is in one piece, still talking fast.
- 12–13s (Shot 4): @Khang keeps talking, raising one fist in a shaky victory pump, breath unsteady.
- 13–14s (Shot 4): @Khang finishes with a breathless laugh and closes his mouth, still holding the camera close.
- 14–15s (Shot 4): @Khang's grin fades as he looks past the lens at the misty untouched valley, mouth closed, chest rising and falling. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–5.6s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, groggy and confused, wincing): "Ow... my head. Is it morning? Why am I lying by a stream?"
- Part 2, 6.1–9.0s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, calling out loudly, half laughing): "Bin! You there? Don't hide and film me!"
- Part 3, 9.5–13.7s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, shaky laugh, forcing his showman voice): "Camera's still recording. Okay, everyone, I got hit by lightning and I'm still alive!"
- Pacing: @Khang speaks slowly and calmly, then @Khang continues at an even everyday pace, then @Khang continues quickly; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a clear stream gurgling over smooth stones, dawn birdsong and insects, wet sand crunching, distant gibbon calls echoing off the cliff. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 04 - Clip 1 (`canh-04/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A pristine limestone valley in the Stone Age by morning: a clear stream winding between reed beds, giant primeval trees, sandy banks printed with large three-toed animal tracks, mist lifting off karst peaks, no roads, no buildings, no trash.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium tracking shot of the YouTuber walking along the stream holding his phone up high, handheld follow.
- Shot 2, 4–7s: 85mm close-up of the YouTuber frowning at his glowing phone, locked off.
- Shot 3, 7–11s: 24mm wide shot of the giant primeval trees with the YouTuber turning a full circle among them, slow pan.
- Shot 4, 11–15s: 50mm medium shot of the YouTuber with a stiff grin facing the silent forest, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang walks along the sandy bank holding his phone high above his head, its screen only a soft glow, and is already speaking in a puzzled voice.
- 1–2s (Shot 1): @Khang keeps talking, waving the glowing phone left and right in search of a signal.
- 2–3s (Shot 1): @Khang climbs onto a smooth river stone and stretches the phone higher, still speaking.
- 3–4s (Shot 1): @Khang lowers the glowing phone, frowns at it and keeps talking, glancing up and down the empty bank.
- 4–5s (CUT to Shot 2): @Khang stares at the glowing screen, jaw tight, as he goes on at an even pace.
- 5–6s (Shot 2): @Khang points toward the far bend of the stream where a road should be, finishing his words.
- 6–7s (Shot 2): @Khang closes his mouth, slips the phone into a pocket and takes a long breath.
- 7–8s (CUT to Shot 3): @Khang forces a big grin, starts talking fast and turns in a slow circle so his chest camera sweeps the giant trees.
- 8–9s (Shot 3): @Khang keeps talking quickly, laughing too loudly, pointing up at a trunk as wide as a house.
- 9–10s (Shot 3): @Khang knocks on the enormous trunk with his knuckles, still talking fast, eyebrows raised.
- 10–11s (Shot 3): @Khang spreads his arms toward the forest and keeps talking, his voice getting louder.
- 11–12s (CUT to Shot 4): @Khang raises one hand beside his face and keeps calling out quickly toward the trees.
- 12–13s (Shot 4): @Khang finishes calling out and closes his mouth, the grin stiff on his face.
- 13–14s (Shot 4): @Khang waits, eyes flicking across the silent trees, mouth closed, breathing fast.
- 14–15s (Shot 4): Mist drifts between the giant trunks and nobody steps out; @Khang's forced grin slowly drains away, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in two parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–6.2s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, puzzled, losing patience): "No signal. Not one bar. Where's the road? Where's the guesthouse? It was right here yesterday."
- Part 2, 6.7–13.0s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, forced laugh, calling to a hidden friend): "Okay, I get it. Bin set up a prank. Nice props, man, the trees are as big as houses! Come out!"
- Pacing: @Khang speaks at an even everyday pace, then @Khang continues quickly; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a clear stream rippling over stones, wild birdsong and insects, boots crunching on sand, leaves rustling, a distant gibbon call. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 04 - Clip 2 (`canh-04/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A pristine limestone valley in the Stone Age by morning: a clear stream winding between reed beds, giant primeval trees, sandy banks printed with large three-toed animal tracks, mist lifting off karst peaks, no roads, no buildings, no trash.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the YouTuber squatting beside a huge three-toed footprint pressed deep in the sand, slow push-in.
- Shot 2, 4–7s: 85mm close-up of the YouTuber's face as he studies the print, locked off.
- Shot 3, 7–12s: 24mm wide shot of the YouTuber standing with one boot inside the giant print, the reed beds behind him, locked off.
- Shot 4, 12–15s: 85mm close-up of the YouTuber whipping round toward the swaying reeds, handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang squats beside a huge round three-toed footprint pressed deep into the sand and is already speaking slowly, eyes fixed on it.
- 1–2s (Shot 1): @Khang keeps talking slowly, tracing the rim of the print with one finger.
- 2–3s (Shot 1): @Khang spreads both hands over the print to measure it, still speaking softly.
- 3–4s (Shot 1): @Khang touches each of the three round toe marks in turn as he goes on.
- 4–5s (CUT to Shot 2): @Khang looks up from the print and keeps speaking quietly, his brow furrowed.
- 5–6s (Shot 2): @Khang swallows and keeps talking, glancing along the line of prints leading toward the reeds.
- 6–7s (Shot 2): @Khang finishes, closes his mouth and stands up slowly, brushing sand from his knees.
- 7–8s (CUT to Shot 3): @Khang sets his boot inside the print, which swallows it with room to spare, and starts speaking again at an even pace.
- 8–9s (Shot 3): @Khang keeps talking, looking down at his boot dwarfed by the print, shaking his head.
- 9–10s (Shot 3): @Khang lifts one hand and holds two fingers apart like a split hoof as he goes on.
- 10–11s (Shot 3): @Khang keeps speaking, then lowers the hand slowly, his face going still.
- 11–12s (Shot 3): @Khang finishes and closes his mouth as the tall reeds behind him sway and rustle.
- 12–13s (CUT to Shot 4): @Khang whips round toward the swaying reeds, lifts one finger in the air and whispers fast, eyes wide.
- 13–14s (Shot 4): @Khang keeps whispering, sinking into a low crouch and staring at the reeds as he finishes the question.
- 14–15s (Shot 4): @Khang freezes in the low crouch, mouth closed, as the tall reeds keep swaying. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–6.4s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and wary, studying the track): "This footprint... it's as big as a dinner tray. Three round toes. That's something heavy."
- Part 2, 6.9–11.6s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, thinking aloud, uneasy): "Nothing in Cuc Phuong is this big anymore. And gaur have split hooves."
- Part 3, 12.1–13.9s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, an urgent whisper): "Shh! Wait... what's behind those bushes?"
- Pacing: @Khang speaks slowly and calmly, then @Khang continues at an even everyday pace, then @Khang continues quickly; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: reeds rustling heavily with no wind, a clear stream trickling, birds suddenly falling silent, sand crunching under a boot, a heavy animal breathing somewhere behind the reeds. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 04 - Clip 3 (`canh-04/clip-3.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A pristine limestone valley in the Stone Age by morning: a clear stream winding between reed beds, giant primeval trees, sandy banks printed with large three-toed animal tracks, mist lifting off karst peaks, no roads, no buildings, no trash.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm over-the-shoulder shot from behind the YouTuber lying behind a mossy boulder, his face in profile at frame left, through the parted reeds onto a huge rhino drinking on the far bank, slow push-in.
- Shot 2, 4–9s: 85mm close-up of the YouTuber's face pressed low beside the boulder, locked off.
- Shot 3, 9–15s: 50mm medium shot past the boulder with the YouTuber's face in profile in the foreground and the rhino across the stream in the background, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang lies flat on his belly behind a mossy boulder, parting the reeds with two fingers, and is already whispering slowly to his chest camera.
- 1–2s (Shot 1): Across the stream a huge grey rhino with one thick horn stands in the shallows drinking, while @Khang keeps whispering.
- 2–3s (Shot 1): @Khang keeps whispering slowly, eyes huge, not blinking as he watches the rhino's folded skin shift.
- 3–4s (Shot 1): @Khang keeps whispering, inching higher behind the boulder for a better look.
- 4–5s (CUT to Shot 2): @Khang finishes, closes his mouth for a breath, then starts whispering again, faster and urgent.
- 5–6s (Shot 2): @Khang keeps whispering fast, shaking his head in disbelief, sweat beading on his upper lip.
- 6–7s (Shot 2): @Khang keeps whispering quickly, pointing one finger back over the boulder toward the far bank.
- 7–8s (Shot 2): @Khang keeps whispering, a wild disbelieving grin twitching at the corners of his mouth.
- 8–9s (Shot 2): @Khang presses his palm flat to the boulder and keeps whispering fast.
- 9–10s (CUT to Shot 3): @Khang finishes, closes his mouth, and across the stream the rhino lifts its dripping head from the water.
- 10–11s (Shot 3): The rhino turns its great head toward the boulder; @Khang ducks lower and starts whispering slowly, barely breathing.
- 11–12s (Shot 3): @Khang keeps whispering slowly, pressing himself flat into the moss, eyes locked on the rhino.
- 12–13s (Shot 3): @Khang breathes the last words and closes his mouth, holding his breath.
- 13–14s (Shot 3): Behind @Khang, across the stream, the rhino holds its stare, water dripping from its horn, ears flicking; @Khang does not move, mouth closed.
- 14–15s (Shot 3): The rhino snorts softly and swings its heavy head away from the reeds while @Khang lets out a slow silent breath, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–4.4s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, barely breathing, in awe): "Everyone... a rhino. A real rhino, thirty meters from me."
- Part 2, 4.9–9.4s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, rushed whisper, disbelieving): "Rhinos went extinct in Vietnam in two thousand eleven! Bin can't rent one of these!"
- Part 3, 9.9–13.1s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, holding his breath, a thin whisper): "It's looking at me... stay down, stay down."
- Pacing: @Khang speaks slowly and calmly, then @Khang continues quickly, then @Khang continues slowly and calmly; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a large animal slurping and snorting at the water's edge, water dripping, reeds rustling, the stream flowing, birdsong gone quiet. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 04 - Clip 4 (`canh-04/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A pristine limestone valley in the Stone Age by morning: a clear stream winding between reed beds, giant primeval trees, sandy banks printed with large three-toed animal tracks, mist lifting off karst peaks, no roads, no buildings, no trash.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot past the boulder of the YouTuber rising to his knees as the rhino plods away into the forest across the stream, locked off.
- Shot 2, 4–8s: 24mm wide shot from the side of the YouTuber standing on the boulder in profile against the misty valley and karst peaks, slow pull-back.
- Shot 3, 8–11s: 35mm medium shot of the YouTuber on the boulder turning from the valley, slow push-in.
- Shot 4, 11–15s: 85mm close-up of the YouTuber holding his small camera toward his face, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Across the stream the rhino turns and plods toward the trees while @Khang, rising to his knees behind the boulder, is already speaking slowly and quietly.
- 1–2s (Shot 1): @Khang keeps talking slowly, watching the rhino's grey rump vanish between the giant trunks.
- 2–3s (Shot 1): @Khang climbs up onto the top of the mossy boulder, still speaking softly, eyes on the forest edge.
- 3–4s (Shot 1): @Khang finishes, closes his mouth and straightens up on top of the boulder, the orange backpack on his shoulders.
- 4–5s (CUT to Shot 2): @Khang stands on the boulder against the misty valley and starts speaking again at an even pace, turning his head slowly across the view.
- 5–6s (Shot 2): @Khang keeps talking as mist lifts off the karst peaks and the stream winds through untouched reed beds below.
- 6–7s (Shot 2): @Khang shakes his head slowly as he goes on, one hand raised to shade his eyes.
- 7–8s (Shot 2): @Khang keeps speaking, pointing up at the clear sky where the lightning came from.
- 8–9s (CUT to Shot 3): @Khang lowers his hand and keeps talking, his voice dropping, jaw working.
- 9–10s (Shot 3): @Khang finishes the thought, closes his mouth and lets out a long breath.
- 10–11s (Shot 3): @Khang draws a deep breath, lifts the small camera on its harness toward his face and starts speaking fast into it.
- 11–12s (CUT to Shot 4): @Khang holds the little lens close and keeps talking fast, nodding to himself.
- 12–13s (Shot 4): @Khang finishes with a firm set of the jaw and closes his mouth.
- 13–14s (Shot 4): @Khang stares into the little lens for a long moment, breathing deeply, mouth closed.
- 14–15s (Shot 4): @Khang lowers the camera, turns to face the empty valley and squares his shoulders, mouth closed, the orange backpack on his back. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–3.6s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and slow, in awe): "No roads. No trash. Not one motorbike engine."
- Part 2, 4.1–9.9s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, thinking aloud, a dawning realisation): "Either I'm dreaming, or the lightning sent me back to a time before people built roads."
- Part 3, 10.4–13.1s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, a deep breath, rallying himself): "Alright. Real survival. No Bin. No guesthouse. No cuts."
- Pacing: @Khang speaks slowly and calmly, then @Khang continues at an even everyday pace, then @Khang continues quickly; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: heavy footfalls thudding away into the forest, branches swishing as something large passes, the stream flowing, wind in the reeds, birdsong slowly returning. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 05 - Clip 1 (`canh-05/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Dense primeval jungle beside a stream at midday in the Stone Age: lianas as thick as a wrist hanging from giant trees, clumps of bamboo, wild banana plants, mossy rocks, dappled sunlight on a carpet of leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the YouTuber kneeling over a broad banana leaf laid with his gear, slow push-in.
- Shot 2, 4–7s: 85mm close-up of the YouTuber holding the folded silver blanket beside his face, locked off.
- Shot 3, 7–11s: 50mm medium shot of the YouTuber sitting back on his heels counting on his fingers, locked off.
- Shot 4, 11–15s: 24mm wide shot of the YouTuber rising from his gear under the giant trees and hanging lianas, slow pan.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang kneels over a broad banana leaf laid with his gear and is already speaking at an even pace, pointing at a red folding multitool.
- 1–2s (Shot 1): @Khang keeps talking, tapping a small silver whistle on a cord, then a tightly folded silver blanket.
- 2–3s (Shot 1): @Khang picks up a shiny gold packet of instant noodles and shakes it so it crinkles, still speaking.
- 3–4s (Shot 1): @Khang sets the packet down and keeps talking, touching a small folding solar charger panel and a pocket lighter.
- 4–5s (CUT to Shot 2): @Khang lifts the folded silver blanket beside his face and keeps speaking to his chest camera, eyebrows raised.
- 5–6s (Shot 2): @Khang tilts the folded blanket so it flashes in the dappled sun, still talking evenly.
- 6–7s (Shot 2): @Khang finishes, closes his mouth and lays the blanket back on the leaf.
- 7–8s (CUT to Shot 3): @Khang sits back on his heels, holds up three fingers and starts talking fast.
- 8–9s (Shot 3): @Khang keeps talking quickly, pinching his nose for a moment with his other hand.
- 9–10s (Shot 3): @Khang keeps counting on his three fingers, tapping each one as he talks fast.
- 10–11s (Shot 3): @Khang keeps talking, patting his stomach and then shaking three fingers at the lens.
- 11–12s (CUT to Shot 4): @Khang stands up and points past the bamboo toward the hanging lianas, still talking fast.
- 12–13s (Shot 4): @Khang finishes, closes his mouth and brushes the dirt from his hands.
- 13–14s (Shot 4): @Khang tucks the gear into his trouser pockets and harness pouches, mouth closed.
- 14–15s (Shot 4): @Khang strides toward a thick liana hanging from a giant tree, mouth closed, dappled sunlight sliding over his shoulders. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in two parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–6.9s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, brisk show-and-tell for the viewers): "Inventory: one multitool, one whistle, one silver emergency blanket, one pack of instant noodles, and a solar charger."
- Part 2, 7.4–12.5s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, counting it off fast, teacher mode): "Rule of three: three minutes without air, three days without water, three weeks without food. First, water."
- Pacing: @Khang speaks at an even everyday pace, then @Khang continues quickly; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: insects buzzing, birdsong in the canopy, a crinkling foil noodle packet, a soft clink of metal tools on a leaf, the stream babbling nearby. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 05 - Clip 2 (`canh-05/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Dense primeval jungle beside a stream at midday in the Stone Age: lianas as thick as a wrist hanging from giant trees, clumps of bamboo, wild banana plants, mossy rocks, dappled sunlight on a carpet of leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the YouTuber beside a thick liana hanging from a giant tree, multitool in hand, slow push-in.
- Shot 2, 4–7s: 24mm low-angle wide shot of the YouTuber reaching up to cut the liana high above his head, locked off.
- Shot 3, 7–10s: 85mm close-up of the YouTuber's face beneath the cut end of the liana as clear water drips, locked off.
- Shot 4, 10–15s: 50mm medium shot of the YouTuber sipping from his palm and turning to his chest camera, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang stands beside a liana as thick as a wrist hanging from a giant tree and is already speaking evenly, patting the vine with his free hand.
- 1–2s (Shot 1): @Khang keeps talking, wagging a finger back toward the stream behind him.
- 2–3s (Shot 1): @Khang unfolds the small saw of his red multitool, still speaking at an even pace.
- 3–4s (Shot 1): @Khang keeps talking as he wraps his hand around the liana and looks up along it.
- 4–5s (CUT to Shot 2): @Khang reaches high above his head and starts sawing the liana there, finishing his sentence.
- 5–6s (Shot 2): @Khang saws through the top of the liana, then starts talking fast again, eyes bright.
- 6–7s (Shot 2): @Khang crouches and saws through the liana low near the ground, still talking quickly.
- 7–8s (CUT to Shot 3): @Khang lifts the cut length of vine, tilting the lower end down, and keeps talking fast.
- 8–9s (Shot 3): Clear water begins to drip from the cut end; @Khang points at it, finishes and closes his mouth, holding his cupped palm under the drops.
- 9–10s (Shot 3): @Khang sips the water from his palm and starts speaking slowly, licking his lips with satisfaction.
- 10–11s (CUT to Shot 4): @Khang keeps talking slowly, letting more drops fall into his palm, eyes half closed in pleasure.
- 11–12s (Shot 4): @Khang keeps speaking, then catches himself, eyes darting sideways in the middle of a word.
- 12–13s (Shot 4): @Khang keeps talking slowly, correcting himself with a sheepish wave of the hand.
- 13–14s (Shot 4): @Khang finishes, closes his mouth and gives his chest camera a tight, innocent smile.
- 14–15s (Shot 4): @Khang raises the dripping vine like a trophy toward the lens, mouth closed, drops sparkling in the dappled sun. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–5.1s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, confident survival-expert lecture): "Never drink unboiled stream water out here. But this vine holds clean water."
- Part 2, 5.6–8.6s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, excited, hurrying): "Cut the top first, then the bottom. There! It's dripping!"
- Part 3, 9.1–13.5s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, smug, then a sheepish slip): "Sweet. I read this in my script... I mean, a book."
- Pacing: @Khang speaks at an even everyday pace, then @Khang continues quickly, then @Khang continues slowly and calmly; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a small saw rasping through fibrous vine, the vine creaking, clear water dripping onto leaves, birdsong and insects, the stream nearby. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 05 - Clip 3 (`canh-05/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Dense primeval jungle beside a stream at midday in the Stone Age: lianas as thick as a wrist hanging from giant trees, clumps of bamboo, wild banana plants, mossy rocks, dappled sunlight on a carpet of leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm close-up of the YouTuber flicking a wet lighter that only sparks, locked off.
- Shot 2, 4–7s: 35mm medium shot of the YouTuber tossing the lighter into the orange backpack and kneeling over a dry board, handheld.
- Shot 3, 7–11s: 24mm wide shot of the YouTuber kneeling in a shaft of sunlight spinning a wooden drill between his palms, locked off.
- Shot 4, 11–15s: 85mm close-up of his sweating face as he spins harder, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang kneels on the leaf carpet flicking a pocket lighter that only spits sparks and is already talking fast, frowning at it.
- 1–2s (Shot 1): @Khang shakes the lighter hard and keeps talking, the wheel scraping with no flame.
- 2–3s (Shot 1): @Khang blows on the lighter, flicks again, sparks only, and keeps talking in a rising voice.
- 3–4s (Shot 1): @Khang finishes with an exasperated groan and closes his mouth, glaring at the lighter.
- 4–5s (CUT to Shot 2): @Khang tosses the lighter into the open orange backpack and starts speaking again at an even pace, putting on a confident smile.
- 5–6s (Shot 2): @Khang sets a flat dry board on the ground and presses one boot on it, still talking.
- 6–7s (Shot 2): @Khang holds up a straight wooden drill stick to his chest camera like a magician, still speaking.
- 7–8s (CUT to Shot 3): @Khang sets the stick in a notch on the board and begins spinning it between his flat palms, talking as he works.
- 8–9s (Shot 3): @Khang keeps spinning faster, hands sliding down the stick, still explaining evenly.
- 9–10s (Shot 3): @Khang keeps talking through quick breaths, sweat starting to bead on his forehead.
- 10–11s (Shot 3): @Khang finishes the explanation, closes his mouth and spins harder, jaw clenched.
- 11–12s (CUT to Shot 4): @Khang glances up at his chest camera and starts talking fast, still spinning the stick.
- 12–13s (Shot 4): @Khang keeps talking quickly, a drop of sweat falling off his nose onto the board.
- 13–14s (Shot 4): @Khang finishes, closes his mouth and grits his teeth, palms whirling the stick.
- 14–15s (Shot 4): No smoke rises from the notch; @Khang keeps spinning, breathing hard through his nose, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in three parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–4.0s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, frustrated, flicking a dead lighter): "Now fire. Lighter... it won't light. Soaked from last night? Come on!"
- Part 2, 4.5–10.3s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, recovering, a confident teacher voice): "No problem. Old-school method: the hand drill. Spin fast, friction makes heat, heat makes fire."
- Part 3, 10.8–13.2s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, breathless, forcing the hype): "Watch closely, everyone, smoke is coming any second!"
- Pacing: @Khang speaks quickly, then @Khang continues at an even everyday pace, then @Khang continues quickly; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the scrape and click of a wet lighter wheel, a wooden drill squeaking and whirring in a notch, heavy breathing, insects buzzing, birdsong. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 05 - Clip 4 (`canh-05/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Dense primeval jungle beside a stream at midday in the Stone Age: lianas as thick as a wrist hanging from giant trees, clumps of bamboo, wild banana plants, mossy rocks, dappled sunlight on a carpet of leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium overhead shot of the YouTuber lying on his back on the leaves holding the small camera above his face, locked off.
- Shot 2, 4–8s: 85mm close-up of the YouTuber's face looking up into the little lens, locked off.
- Shot 3, 8–11s: 24mm wide shot of the YouTuber lying on the leaf carpet beside the board and drill under the giant trees, slow rise.
- Shot 4, 11–15s: 85mm close-up of his face with a tired crooked smile, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang lies on his back on the leaf carpet holding the small camera above his face and is already speaking slowly, voice hoarse with exhaustion.
- 1–2s (Shot 1): @Khang turns one hand toward the lens to show a palm covered in swollen red blisters, still talking slowly.
- 2–3s (Shot 1): @Khang tilts the camera toward the board beside him, where the drill tip is only blackened and no smoke rises, and keeps speaking.
- 3–4s (Shot 1): @Khang finishes, closes his mouth and lets his arm drop onto the leaves with a long exhale.
- 4–5s (CUT to Shot 2): @Khang stares up at the canopy for a breath, then looks into the lens and starts speaking at an even pace, quieter.
- 5–6s (Shot 2): @Khang keeps talking, his showman smile gone, eyes steady on the lens.
- 6–7s (Shot 2): @Khang swallows and keeps speaking, the dappled light trembling across his sweaty face.
- 7–8s (Shot 2): @Khang keeps talking, shaking his head slowly against the dry leaves under him.
- 8–9s (CUT to Shot 3): @Khang keeps speaking evenly, flexing his red blistered fingers in the air above his chest.
- 9–10s (Shot 3): @Khang keeps talking as he lifts the camera a little higher, eyes wet and shining in the sunlight.
- 10–11s (Shot 3): @Khang finishes, closes his mouth for a moment, then starts speaking again with a small tired smile.
- 11–12s (CUT to Shot 4): @Khang keeps talking evenly, letting out a soft breath of a laugh.
- 12–13s (Shot 4): @Khang keeps speaking, rubbing his thumb over a blister, eyes on the lens.
- 13–14s (Shot 4): @Khang keeps talking quietly, the crooked smile settling into something calmer and softer.
- 14–15s (Shot 4): @Khang finishes, closes his mouth and lets the camera rest on his chest, staring up at the canopy. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in two parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–4.0s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, drained and hoarse): "Two hours. Blisters everywhere. Not one wisp of smoke."
- Part 2, 4.5–13.8s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, quiet honesty, no performance, then a small rueful smile): "Okay, confession. Three years running a survival channel, and I have never made a fire myself. Nobody will ever see this. So why not be honest."
- Pacing: @Khang speaks slowly and calmly, then @Khang continues at an even everyday pace; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: insects droning in the afternoon heat, dry leaves rustling under a body, distant birdsong, a slow tired breath. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 06 - Clip 1 (`canh-06/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A wide jungle stream in the Stone Age in afternoon light: a big flat-topped boulder in the middle of the current, thick reeds on the near bank, a dense forest edge about twenty meters away on the far bank, sun glare on the water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the boy crouched on top of the flat boulder in the middle of the stream, shouting toward the near bank, handheld.
- Shot 2, 4–9s: 85mm close-up of the YouTuber pushing out of the reeds on the near bank, panting, locked off.
- Shot 3, 9–12s: 24mm wide shot down the stream with the boy on the boulder in the middle and the tiger pacing under the trees on the far bank, slow push-in.
- Shot 4, 12–15s: 135mm close-up of the tiger standing at the water's edge on the far bank, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Snail crouches on top of the flat boulder in the middle of the stream, clutching the rock with both hands, and is already shouting fast toward the near bank.
- 1–2s (Shot 1): @Snail keeps shouting, waving one small arm, his big eyes darting toward the far bank.
- 2–3s (Shot 1): @Snail points a shaking finger across the water as he keeps shouting, the tuft of hair on his head bobbing.
- 3–4s (Shot 1): @Snail keeps shouting the last words, hugging his knees in his small bark-cloth tunic, breathing in quick gasps.
- 4–5s (CUT to Shot 2): @Khang pushes out through the tall reeds onto the near bank, chest heaving, and starts shouting fast toward the boulder.
- 5–6s (Shot 2): @Khang keeps shouting, both palms raised toward the boy as if to hold him in place.
- 6–7s (Shot 2): @Khang keeps talking fast, glancing across the stream toward the far bank, sweat on his face.
- 7–8s (Shot 2): @Khang taps his own temple with two fingers, still talking quickly, eyes flicking around for an idea.
- 8–9s (Shot 2): @Khang finishes, closes his mouth and swallows hard, staring across the water at the far bank.
- 9–10s (CUT to Shot 3): @Snail on the boulder points across the stream and starts shouting fast again, while on the far bank a striped tiger paces under the trees.
- 10–11s (Shot 3): @Snail keeps shouting, voice cracking, as the tiger stops pacing on the far bank and turns its head toward the near bank.
- 11–12s (Shot 3): @Snail keeps shouting quickly, scrambling to the highest point of the boulder, as the tiger takes one slow step toward the edge of its own bank.
- 12–13s (CUT to Shot 4): @Snail finishes and closes his mouth, frozen with his knees pulled up and both hands flat on the rock.
- 13–14s (Shot 4): On the far bank the tiger stands at the edge of the water, head low, amber eyes fixed across the stream, tail swaying.
- 14–15s (Shot 4): The tiger lowers its nose toward the water on its own side of the stream and stays there, ears forward, never stepping in. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.3s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, high-pitched panic, shouting): "Help! Help! The tiger's been waiting for me since the sun was high!"
- Turn 2, 4.8–8.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, breathless, shouting, thinking fast): "Stay up there! Don't jump in the water! I'm thinking, don't be scared!"
- Turn 3, 9.2–12.2s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, a shrill warning, pointing): "Stranger! It's looking at you now! It's going to cross!"
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: rushing stream water, a low rumbling growl from the far bank, reeds thrashing as someone pushes through, quick panting breaths, cicadas. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 06 - Clip 2 (`canh-06/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A wide jungle stream in the Stone Age in afternoon light: a big flat-topped boulder in the middle of the current, thick reeds on the near bank, a dense forest edge about twenty meters away on the far bank, sun glare on the water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the YouTuber at the edge of the reeds shaking open a crackling silver blanket, handheld.
- Shot 2, 4–8s: 24mm wide shot down the stream with the YouTuber on the near bank holding the blazing silver blanket high, the boy on the boulder in the middle and the tiger on the far bank, locked off.
- Shot 3, 8–12s: 85mm close-up of the boy on the boulder lit by the flashing silver light, locked off.
- Shot 4, 12–15s: 50mm over-the-shoulder shot from behind the YouTuber past the raised blanket toward the far bank, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang pulls the folded silver blanket from his cargo pocket, shakes it open with a loud crackle and is already shouting fast across the stream.
- 1–2s (Shot 1): @Khang hoists the silver blanket high over his head with both arms so it catches the sun and flares, still shouting.
- 2–3s (Shot 1): @Khang waves the blazing silver sheet from side to side, shouting fast toward the far bank, eyes wide.
- 3–4s (Shot 1): @Khang rises on his toes and spreads the blanket wider above him, still shouting, cords standing out in his neck.
- 4–5s (CUT to Shot 2): @Khang finishes the shout and closes his mouth for a breath, the silver sheet flashing sunlight across the water.
- 5–6s (Shot 2): @Khang starts shouting again fast, holding his ground on the near bank, never turning his back to the far bank.
- 6–7s (Shot 2): Light from the blanket dances over the far bank as @Khang keeps shouting, and the tiger there stops and squints.
- 7–8s (Shot 2): @Khang keeps shouting, stamping one boot at the edge of his own bank, then finishes and closes his mouth as the tiger takes a step back.
- 8–9s (CUT to Shot 3): @Snail on the boulder stares at the flashing silver light, eyes huge, and starts crying out fast with delight.
- 9–10s (Shot 3): @Snail keeps shouting excitedly, pointing at the far bank with one small hand.
- 10–11s (Shot 3): @Snail bounces on his knees on the boulder, still shouting, a huge grin on his round face.
- 11–12s (Shot 3): @Snail finishes, closes his mouth and claps both hands to his chest, beaming.
- 12–13s (CUT to Shot 4): @Khang raises the whistle on its cord to his lips and blows sharp bursts, the blanket still held high.
- 13–14s (Shot 4): Across the stream the tiger flattens its ears, turns away and slinks back between the trees of the far bank.
- 14–15s (Shot 4): The tiger's striped tail vanishes into the forest; @Khang lowers the whistle and the blanket, chest heaving, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.6s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, yelling and making himself big, then panting): "Hey! Go away! Look at this! Shiny, huh? Big, huh? I'm bigger than you! Look big, make noise, never turn your back and run!"
- Turn 2, 8.1–11.4s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, squealing with wonder): "The silver skin shines like the sun! The tiger's backing off!"
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 11.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a foil blanket crackling and snapping in the wind, the rushing stream, a low growl fading into the forest, a sharp whistle blowing in short bursts, a boy's delighted gasp. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 06 - Clip 3 (`canh-06/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A wide jungle stream in the Stone Age in afternoon light: a big flat-topped boulder in the middle of the current, thick reeds on the near bank, a dense forest edge about twenty meters away on the far bank, sun glare on the water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of the YouTuber wading knee-deep toward the near bank with the boy riding on his back, handheld follow.
- Shot 2, 5–10s: 85mm close-up of the YouTuber's face with the boy's hand reaching past his cheek to the silver blanket, locked off.
- Shot 3, 10–12s: 24mm wide shot of the two of them on the sandy near bank as the boy hops down, locked off.
- Shot 4, 12–15s: 85mm close-up of the boy holding up a small stream-snail shell beside his grin, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang wades knee-deep through the stream toward the near bank with @Snail riding on his back, and @Snail is already talking excitedly, patting the silver blanket over @Khang's shoulders.
- 1–2s (Shot 1): @Snail keeps talking, rubbing a corner of the crinkling silver blanket between his fingers, eyes round.
- 2–3s (Shot 1): @Snail holds the shiny corner up to the sun and keeps talking, the light flashing on his face.
- 3–4s (Shot 1): @Snail leans over @Khang's shoulder to peer at his own reflection in the blanket, still talking.
- 4–5s (Shot 1): @Snail finishes, closes his mouth and presses his cheek to the shiny blanket, grinning.
- 5–6s (CUT to Shot 2): @Khang, still wading, glances back over his shoulder and starts answering evenly, a tired smile on his face.
- 6–7s (Shot 2): @Khang keeps talking at an easy pace, gently tugging the blanket edge out of the small fingers.
- 7–8s (Shot 2): @Khang keeps speaking, raising his eyebrows with a wry little shrug under the boy's weight.
- 8–9s (Shot 2): @Khang steps up onto the sand and keeps talking, looking up at the boy on his back.
- 9–10s (Shot 2): @Khang finishes the question, closes his mouth and crouches so @Snail can slide down.
- 10–11s (CUT to Shot 3): @Snail hops down onto the sand and starts talking fast, fingering the string of shells on his wrist.
- 11–12s (Shot 3): @Snail keeps talking fast, holding up a small spiral stream-snail shell right in front of @Khang's nose.
- 12–13s (CUT to Shot 4): @Snail keeps talking quickly, tapping the shell and then his own chest, beaming.
- 13–14s (Shot 4): @Snail points up toward the limestone cliff beyond the trees with the shell, still talking fast.
- 14–15s (Shot 4): @Snail finishes, closes his mouth and grins up at @Khang with the shell held high. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking at a natural, even conversational pace, delighted and awed): "Silver skin! Shinier than water! Even the tiger's scared! Let me touch!"
- Turn 2, 5.2–9.9s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, tired, amused, matter-of-fact): "It's not skin, it's a blanket. Twelve bucks online. Where do you live?"
- Turn 3, 10.4–14.0s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, proud and bouncy, showing his shell): "My name is like this! I live in the cave up there!"
- Pacing: @Snail speaks at an even everyday pace, then @Khang answers at an even everyday pace, then @Snail answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: water sloshing around wading legs, a foil blanket crinkling, the stream rushing over the boulder, bare feet landing on wet sand, birds calling at the forest edge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 06 - Clip 4 (`canh-06/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A wide jungle stream in the Stone Age in afternoon light: a big flat-topped boulder in the middle of the current, thick reeds on the near bank, a dense forest edge about twenty meters away on the far bank, sun glare on the water.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the girl stepping out of the reeds with a bamboo spear held level across her body, handheld.
- Shot 2, 4–8s: 85mm close-up of the YouTuber raising both hands, locked off.
- Shot 3, 8–13s: 35mm over-the-shoulder shot from behind the YouTuber onto the girl, slow push-in.
- Shot 4, 13–15s: 24mm wide shot of the two on the sandy bank with the stream and the boulder behind them, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Stream steps fast out of the tall reeds, a long bamboo spear with a chipped stone head held level across her body in both hands, and is already speaking sharply.
- 1–2s (Shot 1): @Stream plants her bare feet on the sand, still speaking fast, the stream-snail necklace swinging on her chest.
- 2–3s (Shot 1): @Stream keeps talking, eyes narrowing as they run down @Khang's olive-green shirt, the spear still held crosswise.
- 3–4s (Shot 1): @Stream finishes the question, closes her mouth and holds her ground, jaw tight.
- 4–5s (CUT to Shot 2): @Khang shoots both hands up, palms open, and starts talking fast, eyes flicking to the spear.
- 5–6s (Shot 2): @Khang keeps talking quickly, jerking his head back toward the boulder in the stream.
- 6–7s (Shot 2): @Khang keeps talking, pinching the front of his olive-green shirt between finger and thumb to show it.
- 7–8s (Shot 2): @Khang finishes, closes his mouth and holds his hands high, breathing hard, a shaky half smile on his face.
- 8–9s (CUT to Shot 3): @Stream tilts her head at the strange word, then starts speaking evenly, her eyes still wary.
- 9–10s (Shot 3): @Stream keeps talking, lowering the spear a little but keeping it across her body.
- 10–11s (Shot 3): @Stream jerks her chin toward the limestone cliff upstream as she keeps speaking.
- 11–12s (Shot 3): @Stream keeps speaking evenly, studying @Khang's face as if deciding something, her grip easing on the spear.
- 12–13s (Shot 3): @Stream finishes, closes her mouth and steps aside to let him pass, the spear now upright in one hand.
- 13–14s (CUT to Shot 4): @Khang lowers his hands slowly and walks ahead of her along the sand, mouth closed, glancing back at the spear.
- 14–15s (Shot 4): @Stream follows two paces behind with the spear held upright, mouth closed, the snail-shell necklace clicking against her chest. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.7s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, fierce and guarded, demanding): "Don't move! Away from my brother! Why is your skin green?"
- Turn 2, 4.2–8.1s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, hands up, placating, talking fast): "Easy! I just saved him from a tiger! It's a shirt, not skin!"
- Turn 3, 8.6–12.6s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, wary and curious, laying down terms): "What is shirt? Come. Grandmother decides if you're man or ghost."
- Pacing: @Stream speaks quickly, then @Khang answers quickly, then @Stream answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: reeds rustling and parting, the stream rushing over the boulder, bare feet on wet sand, snail shells clicking on a necklace, birds calling at the forest edge. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 07 - Clip 1 (`canh-07/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A large limestone cave more than ten thousand years ago at dusk, home of a small Stone Age clan: a wide arched mouth, a huge stalactite shaped like an elephant, bare rock walls with no handprints or drawings, a hearth fire in the middle, hides drying on poles, rattan baskets of snails, sleeping beds of dry leaves, a stream running below the entrance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, a long bamboo spear with a chipped stone tip, barefoot.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 24mm wide shot of the cave mouth at dusk with @Roar planted in the entrance facing the lens, slow push-in.
- Shot 2, 3–5s: 85mm close-up of @Roar under the elephant-shaped stalactite, locked off.
- Shot 3, 5–10s: 50mm medium shot of @Stream stepping up into the cave mouth, handheld follow.
- Shot 4, 10–15s: 50mm over-the-shoulder shot from behind @Stream onto @Roar, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Roar stands planted in the wide cave mouth with his bamboo spear held upright and is already shouting, harsh, chest pushed out.
- 1–2s (Shot 1): @Roar keeps talking, flaring his nostrils and sniffing the air toward the jungle path as if catching a strange smell.
- 2–3s (Shot 1): @Roar keeps shouting and jerks his chin toward the dark trees, his boar-tusk necklace swaying on the hide vest.
- 3–4s (CUT to Shot 2): @Roar keeps speaking through clenched teeth, heavy brows drawn down, knuckles tight around the upright spear shaft.
- 4–5s (Shot 2): @Roar finishes the warning, closes his mouth and breathes hard through his nose, blocking the entrance.
- 5–6s (CUT to Shot 3): @Stream steps up from the path into the cave mouth and answers fast, chin raised, the rattan basket on her back.
- 6–7s (Shot 3): @Stream keeps talking firmly and moves sideways to stand between @Roar and a blurred figure far down the path.
- 7–8s (Shot 3): @Stream keeps speaking and points one hand back toward the stream below, her red-ochre stripes catching the last light.
- 8–9s (Shot 3): @Stream keeps talking, eyes narrowing at @Roar, her bare feet planted wide on the earthen floor.
- 9–10s (Shot 3): @Stream finishes with the pointed question, closes her mouth and holds his stare without blinking.
- 10–11s (CUT to Shot 4): @Roar answers coldly with a tight mouth, lifting his gaze over the top of her head toward the path.
- 11–12s (Shot 4): @Roar keeps talking in a flat low voice and thumps his free fist once against his own boar-hide vest.
- 12–13s (Shot 4): @Roar keeps speaking, his eyes sliding past @Stream to study the blurred figure waiting on the path.
- 13–14s (Shot 4): @Roar finishes the question, closes his mouth and sets his jaw, the spear still upright at his side.
- 14–15s (Shot 4): @Stream stays in front of him with her arms at her sides, breathing steadily, both mouths closed in the fading dusk light. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.5s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking quickly in short lively phrases, every word still clear, harsh and suspicious, barking each word): "Stream! Why bring a stranger here? He smells strange. The tiger will follow!"
- Turn 2, 5.0–9.5s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, firm, standing her ground): "The tiger already came. He chased it off and saved Snail. Where were you, Roar?"
- Turn 3, 10.0–13.4s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking at a natural, even conversational pace, cold and flat): "Hunting, to feed the cave. What did he bring?"
- Pacing: @Roar speaks quickly, then @Stream answers quickly, then @Roar answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: evening cicadas rising from the jungle, the stream rushing below the cave mouth, the hearth fire crackling deep inside, bare feet scuffing on packed earth. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 07 - Clip 2 (`canh-07/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A large limestone cave more than ten thousand years ago at dusk, home of a small Stone Age clan: a wide arched mouth, a huge stalactite shaped like an elephant, bare rock walls with no handprints or drawings, a hearth fire in the middle, hides drying on poles, rattan baskets of snails, sleeping beds of dry leaves, a stream running below the entrance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of @Moon seated by the hearth cradling the green bamboo ember tube, slow push-in.
- Shot 2, 4–9s: 50mm over-the-shoulder shot from behind @Moon onto @Khang kneeling in the firelight, locked off.
- Shot 3, 9–12s: 85mm close-up of @Moon's lined face in the firelight, locked off.
- Shot 4, 12–15s: 35mm medium two-shot of @Moon and @Khang on either side of the hearth, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Moon sits by the hearth cradling a thick green bamboo ember tube in both hands and is already speaking, slow and grave.
- 1–2s (Shot 1): @Moon keeps speaking slowly, her calm eyes travelling up @Khang from his muddy boots to his face.
- 2–3s (Shot 1): @Moon keeps talking with weight in every word, the red-ochre dot on her forehead glowing in the firelight.
- 3–4s (Shot 1): @Moon finishes and closes her mouth as @Khang drops to his knees before her, the orange backpack still on his shoulders.
- 4–5s (CUT to Shot 2): @Khang answers fast and eagerly, both palms raised, his face lit orange by the hearth.
- 5–6s (Shot 2): @Khang keeps talking quickly, pressing one hand to his chest and shaking his head at the food baskets.
- 6–7s (Shot 2): @Khang keeps speaking and gestures toward a bed of dry leaves against the bare rock wall.
- 7–8s (Shot 2): @Khang keeps talking and taps his own chest with a showman's grin, nodding hard.
- 8–9s (Shot 2): @Khang finishes the promise, closes his mouth and swallows, still kneeling, while @Moon watches with her mouth closed.
- 9–10s (CUT to Shot 3): @Moon answers slowly with a faint lift of one eyebrow, her voice low and husky.
- 10–11s (Shot 3): @Moon sets the ember tube across her knees and keeps speaking, slow and deliberate.
- 11–12s (Shot 3): @Moon raises both open hands in front of her face, fingers spread, counting the suns as she speaks.
- 12–13s (CUT to Shot 4): @Moon keeps speaking with weight in every word, her open hands held still between them in the firelight.
- 13–14s (Shot 4): @Moon speaks the last words slowly and lowers her hands onto the ember tube as @Khang nods, mouth closed.
- 14–15s (Shot 4): @Moon finishes, closes her mouth and holds his gaze, while @Khang breathes out slowly on his knees, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.7s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and grave, measuring every word): "Stranger. This cave does not feed strange mouths."
- Turn 2, 4.2–8.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, eager and fast, a little too polite): "Grandma, I don't need food. Just a safe place to sleep. I'll feed myself!"
- Turn 3, 8.9–14.3s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and final, like speaking a law): "Feed yourself? Good. Seven suns, by your own hands. Live, and you stay."
- Pacing: @Moon speaks slowly and calmly, then @Khang answers quickly, then @Moon answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the hearth fire crackling and popping, rustling dry leaves and shuffling bare feet in the dark, wind sighing across the cave mouth, a hide creaking on its drying pole. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 07 - Clip 3 (`canh-07/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A large limestone cave more than ten thousand years ago at dusk, home of a small Stone Age clan: a wide arched mouth, a huge stalactite shaped like an elephant, bare rock walls with no handprints or drawings, a hearth fire in the middle, hides drying on poles, rattan baskets of snails, sleeping beds of dry leaves, a stream running below the entrance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 24mm low-angle medium shot of @Khang with the elephant-shaped stalactite looming above him, slow push-in.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind @Khang at the bare wall onto @Stream, locked off.
- Shot 3, 10–12s: 35mm medium two-shot of @Khang and @Stream at the bare rock wall, locked off.
- Shot 4, 12–15s: 85mm close-up of @Khang's face beside his palm pressed flat on the bare rock, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang stands frozen under the elephant-shaped stalactite, head tilted back, and is already speaking slowly, half to himself.
- 1–2s (Shot 1): @Khang keeps talking in a low voice, his eyes tracing the long trunk-like curve of the stalactite.
- 2–3s (Shot 1): @Khang turns slowly toward the wide arched mouth of the cave as he keeps speaking, breath held between words.
- 3–4s (Shot 1): @Khang keeps speaking, one hand drifting up to the small camera on his chest harness without pressing it.
- 4–5s (Shot 1): @Khang finishes the name of the cave, closes his mouth and walks straight toward the bare rock wall.
- 5–6s (CUT to Shot 2): @Stream follows a step behind and asks, puzzled, head tilted, as @Khang lays his palm flat on the smooth stone.
- 6–7s (Shot 2): @Stream keeps talking and sweeps one hand across the bare smoke-stained rock to show there is nothing on it.
- 7–8s (Shot 2): @Stream keeps speaking with a small frown, the snail-shell necklace clicking softly on her chest.
- 8–9s (Shot 2): @Stream keeps talking, eyes narrowing at his strange words, while @Khang stays silent with his mouth closed.
- 9–10s (Shot 2): @Stream finishes, closes her mouth and folds her arms, waiting for an answer.
- 10–11s (CUT to Shot 3): @Khang answers in a hushed whisper, sliding his palm slowly across the empty wall.
- 11–12s (Shot 3): @Khang keeps whispering and spreads his fingers wide on the smooth stone exactly where a handprint should be.
- 12–13s (CUT to Shot 4): @Khang keeps whispering, eyes wide and glistening in the firelight, his breath catching between words.
- 13–14s (Shot 4): @Khang whispers the last words, his spread fingers trembling slightly against the bare rock.
- 14–15s (Shot 4): @Khang finishes, closes his mouth and swallows hard, his palm still pressed to the cold wall in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and stunned, half to himself): "Wait... that elephant stalactite. This entrance. It's the Cave of Hands."
- Turn 2, 5.3–9.6s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, puzzled and a little wary): "Hands? The wall has only stone and smoke. You talk strange words."
- Turn 3, 10.1–14.1s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, a hushed whisper, piecing it together): "No hands yet. That means... I got here before the handprints."
- Pacing: @Khang speaks slowly and calmly, then @Stream answers at an even everyday pace, then @Khang answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the hearth fire crackling behind them, water dripping from the stalactite into a small pool, the stream rushing below the cave mouth, a palm sliding over dry rock. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 07 - Clip 4 (`canh-07/clip-4.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night inside the large Stone Age clan cave: the elephant-shaped stalactite, bare rock walls with no handprints, a hearth fire glowing red, sleeping beds of dry leaves, hides on poles, deep shadows beyond the firelight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: a few clan members in bark-cloth tunics and hide wraps asleep around the distant glowing hearth, dark silhouettes in soft focus
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 24mm close-up of @Khang's face as seen from the small camera he holds at arm's length, slight handheld wobble.
- Shot 2, 5–10s: 50mm medium shot of @Khang hunched against the rock wall in the dark corner with the distant hearth behind him, slow push-in.
- Shot 3, 10–15s: 85mm close-up of @Khang's face in the faint red glow, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang sits in the dark far corner of the cave holding the small chest camera at arm's length toward his face and is already whispering to it.
- 1–2s (Shot 1): @Khang keeps whispering, glancing over his shoulder at the sleeping shapes around the distant hearth.
- 2–3s (Shot 1): @Khang keeps talking low into the lens, eyebrows raised, the tiny red recording light glowing below his chin.
- 3–4s (Shot 1): @Khang keeps whispering and shakes his head slowly, as if he cannot believe his own words.
- 4–5s (Shot 1): @Khang finishes the thought, closes his mouth and lets out a long shaky breath in the dark.
- 5–6s (CUT to Shot 2): @Khang shifts his back against the cold rock wall and starts speaking again with a tired half-smile.
- 6–7s (Shot 2): @Khang keeps talking and traces a big frame in the air with his free hand, a flicker of the old showman in his eyes.
- 7–8s (Shot 2): @Khang keeps speaking wryly and lets the hand drop onto his muddy knee.
- 8–9s (Shot 2): @Khang keeps talking as his smile fades, his eyes going back to the small lens.
- 9–10s (Shot 2): @Khang finishes the sentence, closes his mouth and lowers his eyes to the dirt floor.
- 10–11s (CUT to Shot 3): @Khang lifts his eyes to the lens and speaks again, slowly and honestly, the showman gone from his face.
- 11–12s (Shot 3): @Khang keeps speaking slowly, his jaw tight, the red light trembling slightly in his hand.
- 12–13s (Shot 3): @Khang keeps speaking softly, swallowing between words, his eyes shining in the faint firelight.
- 13–14s (Shot 3): @Khang says the last words slowly, staring straight into the small lens without blinking.
- 14–15s (Shot 3): @Khang finishes, closes his mouth and keeps holding the camera in silence, breathing slowly in the dark corner. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in two parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–9.4s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, hushed whisper to the lens, then low and wry): "Everyone... I think this is the Stone Age. Over ten thousand years ago. Grandma gave me seven days. Seven-day survival. Like my video titles."
- Part 2, 9.9–13.9s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and honest, the showman gone): "Only now, if I fail, nobody can cut it out."
- Pacing: @Khang speaks at an even everyday pace, then @Khang continues slowly and calmly; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the distant hearth crackling softly, slow breathing of sleepers in the dark, crickets and frogs outside the cave mouth, water dripping onto stone. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 08 - Clip 1 (`canh-08/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A shallow rocky stretch of the jungle stream in the Stone Age, morning: round pebbles, clear ankle-deep water, flat stones covered with small dark snails, a big boulder on the bank, sunlight sparkling.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium shot of @Khang bent over the ankle-deep water with his hands hovering, handheld follow.
- Shot 2, 3–5s: 24mm wide shot of the sparkling shallows with @Khang facing the lens and @Stream on the boulder beside him, locked off.
- Shot 3, 5–10s: 85mm close-up of @Stream on the boulder with her chin on her hand, locked off.
- Shot 4, 10–15s: 35mm medium two-shot of @Khang sitting soaked in the shallows with @Stream on the boulder behind him, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang crouches in the ankle-deep water with both hands hovering over a darting fish and is already talking fast to his chest camera.
- 1–2s (Shot 1): @Khang keeps talking in a breathless rush, creeping one boot forward over the round wet pebbles.
- 2–3s (Shot 1): @Khang plunges both hands into the water with a shout as the silver fish flicks away between his fingers.
- 3–4s (CUT to Shot 2): @Khang's boot slides on a mossy pebble and he lands on his backside in a big splash, still talking.
- 4–5s (Shot 2): @Khang finishes the complaint, closes his mouth and wipes stream water from his face, soaked to the chest.
- 5–6s (CUT to Shot 3): @Stream sits on the big boulder on the bank, chin on one hand, and answers with a laugh in her voice.
- 6–7s (Shot 3): @Stream keeps talking and points lazily at a fish gliding calmly around his muddy boots.
- 7–8s (Shot 3): @Stream keeps speaking, her red-ochre striped cheeks lifting in a wide grin.
- 8–9s (Shot 3): @Stream keeps talking, tilting her head at him as he drips, while @Khang listens with his mouth closed.
- 9–10s (Shot 3): @Stream finishes, closes her mouth and presses her lips together to hold back another laugh.
- 10–11s (CUT to Shot 4): @Khang flops both arms into the water and fires back in a whiny voice, pointing up at her.
- 11–12s (Shot 4): @Khang keeps talking and flicks a handful of water toward her boulder with an exaggerated pout.
- 12–13s (Shot 4): @Khang keeps speaking and slumps back on his hands in the shallow water, eyes rolling up to the sky.
- 13–14s (Shot 4): @Khang finishes, closes his mouth and lets his head flop back dramatically, water streaming from his hair.
- 14–15s (Shot 4): @Khang sits dripping in the sparkling stream with his mouth closed, while @Stream grins down at him in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, breathless and frantic, mid-chase): "Day two. Starving. Fish, hold still... Ah! Slipped again! That's ten in a row!"
- Turn 2, 5.1–9.4s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, amused, laughing between the words): "You chased fish all morning. The fish are not tired. You are."
- Turn 3, 9.9–13.5s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, deflated and whiny, flopping down): "Then you catch one! Stop laughing, I'm about to faint."
- Pacing: @Khang speaks quickly, then @Stream answers at an even everyday pace, then @Khang answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the shallow stream babbling over round pebbles, a big splash as a body hits the water, morning birdsong and cicadas in the jungle, water dripping from soaked clothes. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 08 - Clip 2 (`canh-08/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A shallow rocky stretch of the jungle stream in the Stone Age, morning: round pebbles, clear ankle-deep water, flat stones covered with small dark snails, a big boulder on the bank, sunlight sparkling.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium two-shot of @Stream sliding down from the boulder into the shallows beside @Khang, slow push-in.
- Shot 2, 3–5s: 85mm close-up of @Stream holding a flat stone crusted with small dark snails up beside her face, locked off.
- Shot 3, 5–10s: 50mm over-the-shoulder shot from behind @Stream onto @Khang kneeling in the water, slow push-in.
- Shot 4, 10–15s: 35mm medium two-shot of @Stream pouring snails into @Khang's open palm, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Stream slides down from the boulder into the ankle-deep water beside @Khang and is already speaking, calm and matter-of-fact.
- 1–2s (Shot 1): @Stream keeps talking as she crouches and slips her fingers under a flat stone in the stream bed.
- 2–3s (Shot 1): @Stream keeps speaking and lifts the dripping stone, its underside crusted with small dark stream snails.
- 3–4s (CUT to Shot 2): @Stream holds the stone up beside her face, still talking, eyebrows raised at him like a patient teacher.
- 4–5s (Shot 2): @Stream finishes with a dry little smile and closes her mouth, the wet snails glistening in the sun.
- 5–6s (CUT to Shot 3): @Khang lurches up onto his knees in the water and bursts out talking, eyes fixed on the snails.
- 6–7s (Shot 3): @Khang keeps talking fast and clasps both hands together in front of his chest like a prayer.
- 7–8s (Shot 3): @Khang keeps speaking excitedly, bouncing on his knees in the shallows with a huge grin.
- 8–9s (Shot 3): @Khang keeps talking and points both index fingers at her, beaming, water dripping from his elbows.
- 9–10s (Shot 3): @Khang finishes and closes his mouth, still beaming, as @Stream peels snails off the stone into her rattan basket.
- 10–11s (CUT to Shot 4): @Stream answers with a puzzled frown at the strange word, dropping snails one by one into her basket.
- 11–12s (Shot 4): @Stream keeps talking and takes hold of his wrist, turning his palm up toward the sky.
- 12–13s (Shot 4): @Stream keeps speaking firmly and pours a handful of wet snails into his open palm.
- 13–14s (Shot 4): @Stream finishes her warning, closes her mouth and taps his palm once with one finger.
- 14–15s (Shot 4): @Khang stares down at the wet snails in his palm with his mouth closed, while @Stream wades back toward the boulder in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.1s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, calm and matter-of-fact, a teacher): "No chasing. Lift the stones, find snails. Snails don't run. Good for you."
- Turn 2, 5.6–9.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, overjoyed, words tumbling out): "Food that doesn't run! Exactly what I need! Stream, you're an angel!"
- Turn 3, 9.7–13.7s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, puzzled, then firm and practical): "What is angel? Roast snails first. Raw ones hurt your belly."
- Pacing: @Stream speaks at an even everyday pace, then @Khang answers quickly, then @Stream answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the shallow stream babbling, a flat stone lifting out of the water with a wet suck, tiny snail shells clicking into a rattan basket, morning birdsong. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 08 - Clip 3 (`canh-08/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Daytime inside the large Stone Age clan cave: soft daylight from the wide arched mouth, the elephant-shaped stalactite, bare rock walls with no handprints, a hearth fire in the middle, rattan baskets of snails, sleeping beds of dry leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: a few small clan children in knee-length bark-cloth tunics crowd in around the hearth in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 85mm close-up of @Snail's wide eyes fixed on a crinkling plain gold foil packet, slow push-in.
- Shot 2, 4–8s: 50mm medium shot of @Khang tearing the packet open beside the hearth, locked off.
- Shot 3, 8–13s: 85mm close-up of @Snail crunching dry noodles with shining eyes, handheld.
- Shot 4, 13–15s: 24mm wide shot of the hearth as small children crowd around @Snail and @Khang, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Snail crouches by the hearth staring at a crinkling plain gold foil packet in @Khang's hands and is already shouting, eyes huge.
- 1–2s (Shot 1): @Snail keeps talking fast, bouncing on his heels, both small hands reaching toward the shiny packet.
- 2–3s (Shot 1): @Snail keeps speaking and tilts his head to listen as the foil crackles in @Khang's fingers.
- 3–4s (Shot 1): @Snail finishes with a pleading grin and closes his mouth, the little tuft on his shaved head quivering.
- 4–5s (CUT to Shot 2): @Khang tears the gold foil packet open with a showman's flourish and starts speaking warmly.
- 5–6s (Shot 2): @Khang keeps talking and slides out a block of dry wavy noodles, holding it up to the firelight.
- 6–7s (Shot 2): @Khang keeps speaking and snaps off a small piece of the dry noodle block with a crisp crack.
- 7–8s (Shot 2): @Khang keeps talking and offers the piece to @Snail, miming slow chewing with his own jaw.
- 8–9s (CUT to Shot 3): @Khang finishes and closes his mouth as @Snail pops the piece into his mouth and crunches loudly.
- 9–10s (Shot 3): @Snail's eyes go round as he chews, then he shouts with his mouth half full, pointing at the packet.
- 10–11s (Shot 3): @Snail keeps shouting with joy and jumps to his feet beside the hearth, cheeks bulging.
- 11–12s (Shot 3): @Snail spins toward the cave and keeps calling out, waving both arms at the other children.
- 12–13s (Shot 3): @Snail finishes the call, closes his mouth and crunches another bite, grinning from ear to ear.
- 13–14s (CUT to Shot 4): Small children in bark-cloth tunics scramble in around the hearth, peering at the gold packet in @Khang's hands.
- 14–15s (Shot 4): @Khang holds the packet high with a closed-mouth grin, while @Snail chews beside him with bulging cheeks, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.7s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, breathless and dazzled, bouncing): "A gold leaf that sings! What's inside? Show me, Silver Skin!"
- Turn 2, 4.2–8.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, warm and teasing, like a show host): "Instant noodles, Snail. My last pack. Try a bite. Chew slowly."
- Turn 3, 8.7–12.6s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, a joyful yell, mouth half full): "Dry worms! Dry worms taste so good! Everybody! The stranger has dry worms!"
- Pacing: @Snail speaks quickly, then @Khang answers at an even everyday pace, then @Snail answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: crinkling foil, a crisp crack of dry noodles snapping, loud crunching, the hearth fire crackling, small bare feet pattering on the cave floor. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 08 - Clip 4 (`canh-08/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Daytime inside the large Stone Age clan cave: soft daylight from the wide arched mouth, the elephant-shaped stalactite, bare rock walls with no handprints, a hearth fire in the middle, rattan baskets of snails, sleeping beds of dry leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: a few small clan children in knee-length bark-cloth tunics hold out cupped hands around the hearth in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of @Moon seated by the hearth with the ember tube across her knees, slow push-in.
- Shot 2, 4–9s: 50mm over-the-shoulder shot from behind @Moon onto @Khang sharing noodle crumbs into small cupped hands, slow drift.
- Shot 3, 9–13s: 85mm close-up of @Moon sniffing the small seasoning sachet, locked off.
- Shot 4, 13–15s: 35mm medium two-shot of @Moon and @Khang beside the hearth, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Moon sits by the hearth with the green bamboo ember tube across her knees and is already speaking slowly, eyes on @Khang.
- 1–2s (Shot 1): @Moon keeps speaking quietly, her gaze following the noodle crumbs between his fingers.
- 2–3s (Shot 1): @Moon keeps talking, her lined face very still, the hearth fire reflected in her calm eyes.
- 3–4s (Shot 1): @Moon finishes and closes her mouth as @Khang turns toward her, a small handful of noodle crumbs in his palm.
- 4–5s (CUT to Shot 2): @Khang answers easily, dropping crumbs into the small cupped hands of a child in soft focus.
- 5–6s (Shot 2): @Khang keeps talking, holding up one finger for the single pack, then sweeping his hand toward the children.
- 6–7s (Shot 2): @Khang keeps speaking with a warm grin, sprinkling the last crumbs into another pair of small hands.
- 7–8s (Shot 2): @Khang keeps talking and tears open a tiny plain foil seasoning sachet with his fingertips.
- 8–9s (Shot 2): @Khang finishes, closes his mouth and holds the open sachet out under @Moon's nose with a hopeful smile.
- 9–10s (CUT to Shot 3): @Moon sniffs the sachet, frowns deeply at the smell, then answers in an even warm voice.
- 10–11s (Shot 3): @Moon keeps speaking and studies @Khang's face for a long moment without blinking.
- 11–12s (Shot 3): @Moon keeps talking evenly and lifts one wrinkled hand toward the glowing hearth beside them.
- 12–13s (Shot 3): @Moon keeps speaking and nods once, slowly, her white hair knot and bone pin catching the firelight.
- 13–14s (CUT to Shot 4): @Moon finishes, closes her mouth and lowers her hand back onto the green ember tube.
- 14–15s (Shot 4): @Khang bows his head to her with his mouth closed and a slow grin spreading, while @Moon watches him in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.3s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and quiet, watching closely): "Hungry, and still you feed the children."
- Turn 2, 3.8–8.8s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, warm and easy, a little proud): "One pack, Grandma. Eat alone, you're full once. Share it, the whole cave smiles."
- Turn 3, 9.3–13.4s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking at a natural, even conversational pace, even and warm, granting a favour): "One who shares is no ghost. Tonight, sleep near the fire."
- Pacing: @Moon speaks slowly and calmly, then @Khang answers at an even everyday pace, then @Moon answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the hearth fire crackling, noodle crumbs pattering into small hands, a foil sachet tearing, a long sniff, soft daylight wind at the cave mouth. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 09 - Clip 1 (`canh-09/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A rainy night inside the large Stone Age clan cave: wind blows rain in through the wide arched mouth, the hearth is only wet grey ash with a thin thread of smoke, the elephant-shaped stalactite, bare rock walls, people huddled on beds of dry leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, empty-handed with no bamboo tube, barefoot.
- Wardrobe: in this shot @Moon wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of @Snail clutching the cold bamboo ember tube, tears on his cheeks, handheld.
- Shot 2, 5–9s: 50mm medium shot of @Moon kneeling beside the wet grey ash of the hearth, slow push-in.
- Shot 3, 9–11s: 85mm close-up of @Moon's lined face above her open palm hovering over the ash, locked off.
- Shot 4, 11–15s: 35mm medium two-shot of @Snail pressed against @Moon's side by the dead hearth, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Snail kneels on the damp cave floor hugging the cold bamboo ember tube to his chest and is already speaking through sobs, tears streaming.
- 1–2s (Shot 1): @Snail keeps talking through sobs, glancing at the rain blowing in through the dark cave mouth.
- 2–3s (Shot 1): @Snail keeps speaking in a rush and holds the cold tube out toward the hearth with both shaking hands.
- 3–4s (Shot 1): @Snail keeps talking, his chin trembling, rainwater dripping from the tuft on his shaved head.
- 4–5s (Shot 1): @Snail finishes, closes his mouth and sniffs hard, clutching the cold tube to his chest again.
- 5–6s (CUT to Shot 2): @Moon kneels beside the wet grey ash of the hearth and answers slowly, her voice low and heavy.
- 6–7s (Shot 2): @Moon keeps speaking slowly and holds her open palm low over the ash, feeling for any warmth.
- 7–8s (Shot 2): @Moon keeps talking as her fingers spread over the ash where only a thin thread of smoke rises.
- 8–9s (Shot 2): @Moon keeps speaking with long pauses, her jaw tightening, the red-ochre dot on her forehead dark in the blue light.
- 9–10s (CUT to Shot 3): @Moon keeps speaking slowly and closes her palm into a loose fist above the cold ash.
- 10–11s (Shot 3): @Moon finishes the last words, closes her mouth and lets her hand fall onto her knee.
- 11–12s (CUT to Shot 4): @Snail presses against her side and asks in a small hiccuping voice, staring at the dark mouth of the cave.
- 12–13s (Shot 4): @Snail keeps talking through sobs, tightening both arms around the cold bamboo tube.
- 13–14s (Shot 4): @Snail finishes, closes his mouth and buries his wet face against @Moon's dark hide cloak.
- 14–15s (Shot 4): @Moon wraps one arm around @Snail with her mouth closed, her eyes fixed on the rain beyond the cave mouth. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, crying hard, the words tumbling out): "I fell asleep! Rain blew in, the fire's dead! The tube is cold, Grandma!"
- Turn 2, 5.1–10.9s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and heavy, steadying herself): "Our fire-maker left us last season. We keep fire. We cannot make it."
- Turn 3, 11.4–13.9s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking at a natural, even conversational pace, sobbing, a small hiccuping voice): "If the tiger comes tonight, what then?"
- Pacing: @Snail speaks quickly, then @Moon answers slowly and calmly, then @Snail answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: heavy rain hissing at the cave mouth, gusts of wind, water dripping and splashing on stone, wet ash sizzling faintly, a child's sobbing breaths. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 09 - Clip 2 (`canh-09/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A rainy night inside the large Stone Age clan cave: wind blows rain in through the wide arched mouth, the hearth is only wet grey ash with a thin thread of smoke, the elephant-shaped stalactite, bare rock walls, people huddled on beds of dry leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, a long bamboo spear with a chipped stone tip, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: a few clan members in bark-cloth tunics and hide wraps shrink back on their leaf beds in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium shot of @Roar rising to his feet beside the dead hearth with his spear held upright, handheld.
- Shot 2, 5–9s: 85mm close-up of @Khang standing up into the cold blue storm light, locked off.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind @Khang onto @Roar, slow push-in.
- Shot 4, 13–15s: 24mm wide shot of the dark rainy cave with both men facing each other across the cold hearth, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Roar shoots up from his leaf bed beside the dead hearth, bamboo spear held upright in one fist, and is already shouting.
- 1–2s (Shot 1): @Roar keeps shouting and jabs a finger of his free hand toward @Khang across the cold ash.
- 2–3s (Shot 1): @Roar keeps talking loudly and sweeps his free arm toward the rain lashing the cave mouth as lightning flashes white.
- 3–4s (Shot 1): @Roar keeps shouting and turns his head to the huddled clan, his boar-tusk necklace swinging.
- 4–5s (Shot 1): @Roar finishes, closes his mouth and breathes hard with flaring nostrils, the spear still upright.
- 5–6s (CUT to Shot 2): @Khang pushes himself up off the damp floor and answers fast, palms open, standing his ground.
- 6–7s (Shot 2): @Khang keeps talking quickly and points one finger up at the stormy sky beyond the cave mouth.
- 7–8s (Shot 2): @Khang keeps speaking and taps his own chest once with a determined nod, jaw set.
- 8–9s (Shot 2): @Khang finishes the promise, closes his mouth and holds @Roar's stare, breathing hard.
- 9–10s (CUT to Shot 3): @Roar answers with a contemptuous sneer, leaning in, his voice dropping low and slow.
- 10–11s (Shot 3): @Roar keeps speaking and twirls two fingers in the air, mocking someone spinning a fire stick.
- 11–12s (Shot 3): @Roar keeps talking with a scornful snort, glancing down at the cold wet ash.
- 12–13s (Shot 3): @Roar finishes, closes his mouth and turns his broad back on @Khang, spear upright.
- 13–14s (CUT to Shot 4): @Khang stands alone by the cold hearth with his mouth closed, fists tightening, as lightning flashes across the cave mouth.
- 14–15s (Shot 4): @Khang turns toward the rain at the cave mouth with his mouth closed, his chest rising and falling. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking quickly in short lively phrases, every word still clear, loud and accusing, playing to the cave): "Since he came: a tiger, rain, and now the fire's dead! He's bad luck!"
- Turn 2, 5.3–8.6s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, fast and defiant, standing his ground): "Rain isn't my fault! Give me till sunrise. I'll make fire!"
- Turn 3, 9.1–12.1s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking at a natural, even conversational pace, contemptuous, almost a sneer): "Two days spinning sticks, and not even smoke."
- Pacing: @Roar speaks quickly, then @Khang answers quickly, then @Roar answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: heavy rain hissing at the cave mouth, a sharp crack of thunder, wind gusting, bare feet shuffling back on damp stone, water dripping from the ceiling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 09 - Clip 3 (`canh-09/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Blue pre-dawn light in a dry corner of the Stone Age clan cave under a low rock overhang: a flat stone work area, split dry bamboo, a pile of fluffy tinder, the cold wet hearth visible behind, rain easing outside the mouth.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of @Khang kneeling at the flat stone under the rock overhang, slow push-in.
- Shot 2, 4–7s: 85mm close-up of @Khang's face bent over the split bamboo as he carves a notch, locked off.
- Shot 3, 7–10s: 50mm over-the-shoulder shot from behind @Khang onto @Stream pressing the split bamboo down, locked off.
- Shot 4, 10–15s: 35mm medium two-shot of @Khang sawing hard while @Stream holds the bamboo steady, handheld.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang kneels at a flat stone under the dry rock overhang, a split dry bamboo tube in his hands, and is already speaking, low and reflective.
- 1–2s (Shot 1): @Khang keeps talking as he lays one split bamboo half curved side up on the flat stone.
- 2–3s (Shot 1): @Khang keeps speaking and carves a shallow notch across the bamboo with his small multitool.
- 3–4s (Shot 1): @Khang keeps talking and blows the shavings away, his eyes distant with the memory.
- 4–5s (CUT to Shot 2): @Khang keeps speaking and stuffs a pinch of fluffy tinder under the notch with his thumb.
- 5–6s (Shot 2): @Khang keeps talking with a rueful shake of his head and folds the multitool away.
- 6–7s (Shot 2): @Khang finishes, closes his mouth and picks up a thin flat strip of dry bamboo.
- 7–8s (CUT to Shot 3): @Stream kneels opposite him in the blue pre-dawn light with her arms folded and answers with flat doubt.
- 8–9s (Shot 3): @Stream keeps speaking and tilts her head at the split bamboo as if it were a silly toy.
- 9–10s (Shot 3): @Stream finishes, closes her mouth, then presses both ends of the split bamboo down hard onto the stone.
- 10–11s (CUT to Shot 4): @Khang sets the bamboo strip across the notch and starts sawing hard, talking urgently.
- 11–12s (Shot 4): @Khang keeps talking fast, sawing back and forth in quick hard strokes, sweat beading on his forehead.
- 12–13s (Shot 4): @Khang keeps speaking in breathless bursts, arms pumping, fine brown bamboo dust gathering under the notch.
- 13–14s (Shot 4): @Khang finishes, presses his lips shut and keeps sawing, jaw clenched, breath hissing through his nose.
- 14–15s (Shot 4): @Stream holds the bamboo steady with her mouth closed and her eyes fixed on the notch, as @Khang saws on in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.5s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, low and reflective, remembering): "I once filmed an old Muong man making fire by sawing bamboo. I thought he was faking."
- Turn 2, 7.0–9.2s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, doubtful and flat): "Bamboo burns. It doesn't make fire."
- Turn 3, 9.7–13.3s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, urgent and breathless, sawing hard): "Hold tight! Saw fast, and the bamboo dust heats into an ember!"
- Pacing: @Khang speaks at an even everyday pace, then @Stream answers at an even everyday pace, then @Khang answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a small multitool scraping dry bamboo, the rasp of bamboo sawing on bamboo, rain easing to a drip outside the cave mouth, heavy breathing, birds stirring before dawn. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 09 - Clip 4 (`canh-09/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Blue pre-dawn light in a dry corner of the Stone Age clan cave under a low rock overhang: a flat stone work area, split dry bamboo, a pile of fluffy tinder, the cold wet hearth visible behind, rain easing outside the mouth.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: a few clan members in bark-cloth tunics and hide wraps crowd in behind the overhang in soft focus, raising their hands
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 85mm close-up of @Khang's face over a smoking nest of bamboo dust and tinder in his cupped hands, handheld.
- Shot 2, 4–9s: 50mm over-the-shoulder shot from behind @Khang onto @Moon stepping into the new firelight, slow push-in.
- Shot 3, 9–12s: 35mm medium two-shot of @Moon and @Khang beside the small new fire, locked off.
- Shot 4, 12–15s: 85mm close-up of @Khang's tear-streaked face lit by the flames, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang kneels over a thin curl of smoke rising from the bamboo dust and is already talking fast, eyes wide.
- 1–2s (Shot 1): @Khang keeps talking breathlessly as he tips a tiny red ember from the notch into a nest of fluffy tinder.
- 2–3s (Shot 1): @Khang cups the tinder nest to his lips, whispering, and blows gently as a soft orange glow pulses inside.
- 3–4s (Shot 1): Flames burst from the tinder in his hands and @Khang cries out the last words, laying it onto a pile of dry twigs.
- 4–5s (CUT to Shot 2): @Khang closes his mouth and stares at the young fire, as @Moon steps in from the dark into its glow.
- 5–6s (Shot 2): @Moon stops beside the small fire, the flames lighting her lined face, and starts speaking slowly and solemnly.
- 6–7s (Shot 2): @Moon keeps speaking and raises the green bamboo ember tube in both hands toward the flame.
- 7–8s (Shot 2): @Moon keeps talking slowly, looking down at @Khang with calm piercing eyes.
- 8–9s (Shot 2): @Moon finishes the naming, closes her mouth and lays one hand on @Khang's shoulder.
- 9–10s (CUT to Shot 3): @Khang looks up at her with brimming eyes and starts speaking slowly, his voice cracking.
- 10–11s (Shot 3): @Khang keeps talking softly and holds up his blistered palms in the warm firelight.
- 11–12s (Shot 3): @Khang keeps speaking as a tear slides down his stubbled cheek, a shaky laugh in his breath.
- 12–13s (CUT to Shot 4): @Khang keeps talking slowly, staring into the flames while the clan cheers behind him in soft focus.
- 13–14s (Shot 4): @Khang says the last words in a near whisper and wipes his eyes with the red bandana on his wrist.
- 14–15s (Shot 4): @Khang finishes, presses his lips together and smiles through tears at the little fire, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.0s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, frantic whisper rising to a cry of joy): "Smoke! There's an ember! Into the tinder, blow gently, gently... It's burning!"
- Turn 2, 4.5–9.1s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and solemn, giving him a name): "Thunder brought us a fire-maker. Your name is Fire-Maker."
- Turn 3, 9.6–14.0s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and tearful, voice cracking): "Twenty-nine years old, and this is my first fire ever."
- Pacing: @Khang speaks quickly, then @Moon answers slowly and calmly, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a soft whoosh as dry tinder catches, small flames crackling, the clan clapping and stamping their feet, the last of the rain dripping at the cave mouth. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 10 - Clip 1 (`canh-10/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Daytime inside the large Stone Age clan cave: soft daylight from the wide arched mouth, the elephant-shaped stalactite, bare rock walls with no handprints, a hearth fire in the middle, rattan baskets of snails, sleeping beds of dry leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of @Stream kneeling at a leaf bed beside the hearth, a small hide-covered shape curled next to her, slow push-in.
- Shot 2, 5–10s: 85mm close-up of @Khang crouched across the leaf bed, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind @Khang onto @Stream, locked off.
- Shot 4, 13–15s: 35mm medium two-shot of @Stream and @Khang on either side of the leaf bed by the hearth, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Stream kneels by a leaf bed beside the hearth, dabbing a wet leaf on the forehead of a small child curled under a hide, and is already speaking fast.
- 1–2s (Shot 1): @Stream keeps talking quickly and glances at @Khang, the wet leaf trembling in her fingers.
- 2–3s (Shot 1): @Stream keeps speaking and lays her palm on the hide over the child's curled-up belly.
- 3–4s (Shot 1): @Stream keeps talking, touches the back of her hand to the child's hot cheek and pulls it back.
- 4–5s (Shot 1): @Stream finishes, closes her mouth and looks across at @Khang, her breath quick and shallow.
- 5–6s (CUT to Shot 2): @Khang crouches across the leaf bed and answers calmly, pinching his finger and thumb together to show something tiny.
- 6–7s (Shot 2): @Khang keeps talking clearly and gently, pointing toward the cave mouth and the stream below.
- 7–8s (Shot 2): @Khang keeps speaking and squints at an imaginary speck held between his finger and thumb.
- 8–9s (Shot 2): @Khang keeps talking and taps his own belly with two fingers to show where it bites.
- 9–10s (Shot 2): @Khang finishes, closes his mouth and lowers his hand, his eyes on the small curled-up shape.
- 10–11s (CUT to Shot 3): @Stream leans toward him and asks fast with a frown, her hands spread wide in confusion.
- 11–12s (Shot 3): @Stream keeps talking and peers at the air above the leaf bed as if hunting for the tiny bugs.
- 12–13s (Shot 3): @Stream finishes, closes her mouth and turns her eyes back to @Khang, waiting for an answer.
- 13–14s (CUT to Shot 4): @Khang reaches behind him for a fresh green bamboo tube leaning on the hearth stones, mouth closed.
- 14–15s (Shot 4): @Khang sets the green bamboo tube upright on the floor between them, mouth closed, as @Stream watches in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.3s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, worried, the words rushing out): "Snail drank from the mud pool. Now his belly hurts and he's burning."
- Turn 2, 4.8–9.8s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, calm and clear, explaining gently): "Still water has tiny bugs, too small to see. They bite you from inside."
- Turn 3, 10.3–13.0s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, urgent and puzzled): "Bugs we can't see? How do we catch them?"
- Pacing: @Stream speaks quickly, then @Khang answers at an even everyday pace, then @Stream answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the hearth fire crackling, a feverish child's quick shallow breathing, a wet leaf dabbing skin, daylight wind murmuring at the cave mouth. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 10 - Clip 2 (`canh-10/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Daytime inside the large Stone Age clan cave: soft daylight from the wide arched mouth, the elephant-shaped stalactite, bare rock walls with no handprints, a hearth fire in the middle, rattan baskets of snails, sleeping beds of dry leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of @Khang and @Stream by the hearth, slow push-in.
- Shot 2, 5–10s: 85mm close-up of @Stream with her arms folded, locked off.
- Shot 3, 10–12s: 50mm over-the-shoulder shot from behind @Stream onto @Khang lifting the water-filled bamboo tube, locked off.
- Shot 4, 12–15s: 85mm close-up of the green bamboo tube leaning into the flames with @Khang's face just beyond it, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang lifts the fresh green bamboo tube between them and is already speaking, firm and certain.
- 1–2s (Shot 1): @Khang keeps talking as he trims the top of the green tube open with his small multitool.
- 2–3s (Shot 1): @Khang keeps speaking and pours clear stream water into the green tube from an old bamboo water tube.
- 3–4s (Shot 1): @Khang keeps talking and sweeps his free hand around the cave to include everyone in it.
- 4–5s (Shot 1): @Khang finishes, closes his mouth and sets the full green tube upright on the floor.
- 5–6s (CUT to Shot 2): @Stream folds her arms and answers in a skeptical, scolding voice, her eyebrows drawn together.
- 6–7s (Shot 2): @Stream keeps talking and points at the fire, then at the water in the green tube.
- 7–8s (Shot 2): @Stream keeps speaking and flicks her fingers apart like flames swallowing something whole.
- 8–9s (Shot 2): @Stream keeps talking and shakes her head slowly, the snail-shell necklace clicking on her chest.
- 9–10s (Shot 2): @Stream finishes, closes her mouth and lifts her chin, waiting for him to fail.
- 10–11s (CUT to Shot 3): @Khang answers quickly with a confident grin and lifts the water-filled green tube.
- 11–12s (Shot 3): @Khang keeps talking fast as he leans the tube at a slant against the hearth stones, its base in the embers.
- 12–13s (CUT to Shot 4): @Khang keeps speaking and taps the thick green skin of the bamboo with one knuckle.
- 13–14s (Shot 4): @Khang says the last word, closes his mouth and sits back on his heels, eyes on the tube.
- 14–15s (Shot 4): Flames lick the side of the green bamboo tube while @Khang watches it with his mouth closed, forearms on his knees. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, firm and certain, laying down a rule): "We boil them. From now on, the whole cave drinks boiled water."
- Turn 2, 5.2–9.9s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, skeptical, almost scolding): "Water kills fire. Fire eats bamboo. Put it in fire, you get ashes."
- Turn 3, 10.4–14.0s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, quick and confident, a friendly dare): "Green bamboo burns slow. The water boils before the bamboo catches. Watch."
- Pacing: @Khang speaks at an even everyday pace, then @Stream answers at an even everyday pace, then @Khang answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the hearth fire crackling, water glugging from one bamboo tube into another, a multitool scraping fresh green bamboo, a wet tube settling against hot stones. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 10 - Clip 3 (`canh-10/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Daytime inside the large Stone Age clan cave: soft daylight from the wide arched mouth, the elephant-shaped stalactite, bare rock walls with no handprints, a hearth fire in the middle, rattan baskets of snails, sleeping beds of dry leaves.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of @Stream's face above the bubbling mouth of the green bamboo tube, steam rising between, slow push-in.
- Shot 2, 5–10s: 35mm medium two-shot of @Khang pouring steaming water into a short bamboo cup beside @Stream, locked off.
- Shot 3, 10–13s: 85mm close-up of @Stream counting on her fingers, locked off.
- Shot 4, 13–15s: 50mm over-the-shoulder shot from behind @Khang onto @Stream, slow drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Stream crouches over the green bamboo tube leaning in the fire, steam curling from its mouth, and is already speaking fast, amazed.
- 1–2s (Shot 1): @Stream keeps talking as she leans closer, then flinches back from the hot steam, blinking hard.
- 2–3s (Shot 1): @Stream keeps speaking and points at the water bubbling up at the mouth of the tube.
- 3–4s (Shot 1): @Stream keeps talking and runs a fingertip near the green skin of the bamboo, barely scorched by the flames.
- 4–5s (Shot 1): @Stream finishes her question, closes her mouth and stares at @Khang, eyes shining.
- 5–6s (CUT to Shot 2): @Khang wraps a big leaf around the hot tube, lifts it from the fire and answers calmly.
- 6–7s (Shot 2): @Khang keeps talking as he pours the steaming water into a short bamboo cup.
- 7–8s (Shot 2): @Khang keeps speaking and sets the cup on a flat stone, pinching his finger and thumb together for small sips.
- 8–9s (Shot 2): @Khang keeps talking and slides the steaming cup toward @Stream along the flat stone.
- 9–10s (Shot 2): @Khang finishes, closes his mouth and nods at the cup, leaving it to cool.
- 10–11s (CUT to Shot 3): @Stream holds up one hand and starts counting on her fingers, speaking carefully and proudly.
- 11–12s (Shot 3): @Stream keeps talking, folding down a second finger and glancing at the green tube.
- 12–13s (Shot 3): @Stream keeps speaking and folds down more fingers one by one, frowning with concentration.
- 13–14s (CUT to Shot 4): @Stream finishes the list, closes her mouth and closes her hand into a small fist.
- 14–15s (Shot 4): @Stream lifts her chin with a proud little smile, mouth closed, as @Khang grins back at her in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, amazed, the words tumbling out): "The water bubbles like a fish breathing! The bamboo is still green! Fire, is this magic?"
- Turn 2, 5.7–9.3s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, calm and practical): "No magic. Let it cool, then give Snail small sips."
- Turn 3, 9.8–13.8s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, careful and proud, counting each step): "I'll remember. Green bamboo, stream water, big fire, bubbles, then drink."
- Pacing: @Stream speaks quickly, then @Khang answers at an even everyday pace, then @Stream answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: water bubbling and hissing inside the bamboo tube, steam whispering, the hearth fire crackling, hot water pouring into a bamboo cup. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 10 - Clip 4 (`canh-10/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night inside the large Stone Age clan cave: the elephant-shaped stalactite, bare rock walls with no handprints, a hearth fire glowing red, sleeping beds of dry leaves, hides on poles, deep shadows beyond the firelight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of @Snail propped on the leaf bed sipping from a bamboo cup, ember light on his face, slow push-in.
- Shot 2, 5–10s: 50mm medium shot of @Khang sitting with his back against the rock wall beside the leaf bed, locked off.
- Shot 3, 10–13s: 85mm close-up of @Snail's drowsy face on the leaf bed, locked off.
- Shot 4, 13–15s: 35mm medium two-shot of @Snail curled on the leaf bed and @Khang against the wall beside him, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Snail props himself on one elbow on the leaf bed, a short bamboo cup in his hands, and is already speaking slowly and weakly.
- 1–2s (Shot 1): @Snail keeps talking and takes a small sip of warm water between the words.
- 2–3s (Shot 1): @Snail keeps speaking with a faint smile on his pale sweaty face, rubbing his belly with one small hand.
- 3–4s (Shot 1): @Snail keeps talking slowly and lifts the bamboo cup a little toward @Khang.
- 4–5s (Shot 1): @Snail finishes, closes his mouth and takes another small sip of the warm water.
- 5–6s (CUT to Shot 2): @Khang, sitting with his back against the rock wall beside him, answers softly with a teasing smile.
- 6–7s (Shot 2): @Khang keeps talking tenderly, takes the cup from @Snail's hands and sets it on the floor.
- 7–8s (Shot 2): @Khang keeps speaking and pulls the hide blanket up over @Snail's small shoulders.
- 8–9s (Shot 2): @Khang keeps talking softly and mimes pouring water into a tube with one cupped hand.
- 9–10s (Shot 2): @Khang finishes, closes his mouth and leans his back against the wall, watching over him.
- 10–11s (CUT to Shot 3): @Snail answers with drooping eyelids and a cheeky little smile, his voice drowsy.
- 11–12s (Shot 3): @Snail keeps talking sleepily, his small hand finding @Khang's sleeve and holding on to it.
- 12–13s (Shot 3): @Snail keeps speaking with his eyes half closed, his head sinking into the leaf bed.
- 13–14s (CUT to Shot 4): @Snail keeps talking in a sleepy murmur, his breathing slowing and his small fingers loosening.
- 14–15s (Shot 4): @Snail finishes, closes his mouth and falls asleep holding the sleeve, while @Khang sits still with his mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking slowly and softly, unhurried, with a short natural pause between phrases, weak and slow, a faint smile): "Fire... my belly stopped biting. Hot water beats mud water."
- Turn 2, 4.9–9.6s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, soft and tender, half teasing): "Better than dry worms? Sleep now. Tomorrow I'll teach you to boil water."
- Turn 3, 10.1–14.1s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking at a natural, even conversational pace, drowsy, eyes drooping, a cheeky smile): "Dry worms are better. But with you here, I'm not scared."
- Pacing: @Snail speaks slowly and calmly, then @Khang answers at an even everyday pace, then @Snail answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: embers ticking and hissing softly in the hearth, slow breathing of sleepers in the dark, crickets outside the cave mouth, a hide blanket rustling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 11 - Clip 1 (`canh-11/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Morning at the wide arched mouth of the Stone Age clan cave: the elephant-shaped stalactite above, a flat earthen terrace where the clan gathers, the jungle and the stream below, soft sunlight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, a long bamboo spear with a chipped stone tip, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: a ring of clan members in bark-cloth tunics and hide wraps watch from the edge of the earthen terrace in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium shot of @Roar striding across the earthen terrace toward the lens, spear upright, handheld follow.
- Shot 2, 6–10s: 85mm close-up of @Khang looking from the upright spear to @Roar, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind @Khang onto @Roar, slow push-in.
- Shot 4, 13–15s: 24mm wide shot of the sunlit terrace with the spear standing upright between the two men and the clan watching, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Roar strides across the earthen terrace toward @Khang, bamboo spear held upright, and is already shouting so the whole clan can hear.
- 1–2s (Shot 1): @Roar keeps talking loudly and jabs a finger at the hearth smoke drifting out of the cave mouth behind them.
- 2–3s (Shot 1): @Roar keeps speaking and pats his own flat belly with a wide palm, sneering.
- 3–4s (Shot 1): @Roar keeps shouting and drives the butt of his spear into the earth so it stands upright just in front of @Khang's boots.
- 4–5s (Shot 1): @Roar keeps speaking and points up at the sun climbing above the elephant-shaped stalactite.
- 5–6s (Shot 1): @Roar finishes, closes his mouth and folds his thick arms over his boar-hide vest.
- 6–7s (CUT to Shot 2): @Khang looks down at the upright spear, then up at @Roar, and answers coolly.
- 7–8s (Shot 2): @Khang keeps talking with a small crooked grin, pointing at @Roar and then down at the stream below.
- 8–9s (Shot 2): @Khang keeps speaking and mimes a fish wriggling with one flat hand.
- 9–10s (Shot 2): @Khang finishes with a tilted head, closes his mouth and waits, eyebrows raised.
- 10–11s (CUT to Shot 3): @Roar leans in over the upright spear and answers fast and hard, his heavy brows low.
- 11–12s (Shot 3): @Roar keeps talking and jerks his chin at the folded silver blanket poking out of @Khang's orange backpack.
- 12–13s (Shot 3): @Roar keeps speaking and swings one arm out toward the jungle path leading away from the cave.
- 13–14s (CUT to Shot 4): @Roar finishes, closes his mouth and stares him down with flaring nostrils.
- 14–15s (Shot 4): @Khang holds @Roar's stare with his mouth closed and gives one slow nod, as the clan watches in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.7s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking quickly in short lively phrases, every word still clear, loud and challenging, playing to the crowd): "Fire-Maker! Fire is not food. At high sun, whoever brings more food, the cave listens to."
- Turn 2, 6.2–9.8s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, cool and amused, accepting the dare): "A contest? Fine. You hunt, I fish. And the loser?"
- Turn 3, 10.3–13.4s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking quickly in short lively phrases, every word still clear, fast and hard, a threat): "The loser takes his silver skin and leaves this cave."
- Pacing: @Roar speaks quickly, then @Khang answers at an even everyday pace, then @Roar answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: morning birdsong over the jungle, the stream rushing below the terrace, a spear butt thudding into packed earth, bare feet shifting on dirt, wind in the bamboo. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 11 - Clip 2 (`canh-11/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A slow deep pool of the jungle stream in the Stone Age under bright sun: a bank of flat rocks, clumps of bamboo, split bamboo strips and a half-woven funnel-shaped fish trap lying on the stones.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 85mm close-up of @Khang pushing his hand into the mouth of a half-woven bamboo funnel, his face beside it, slow push-in.
- Shot 2, 3–5s: 35mm medium two-shot of @Khang and @Stream sitting on the flat rocks weaving bamboo strips, locked off.
- Shot 3, 5–10s: 85mm close-up of @Stream smiling at @Khang, locked off.
- Shot 4, 10–15s: 50mm over-the-shoulder shot from behind @Stream onto @Khang, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang sits cross-legged on a flat rock holding a half-woven funnel fish trap and is already speaking, eager like a teacher.
- 1–2s (Shot 1): @Khang keeps talking and slides his hand easily into the wide mouth of the bamboo funnel.
- 2–3s (Shot 1): @Khang keeps speaking and wiggles his fingers inside the narrow inner end to show the fish cannot turn back.
- 3–4s (CUT to Shot 2): @Khang keeps talking and pulls his hand out the slow way, then tugs a split bamboo strip tighter through the weave.
- 4–5s (Shot 2): @Khang keeps speaking and holds the trap up proudly toward @Stream, who sits weaving beside him.
- 5–6s (CUT to Shot 3): @Khang finishes and closes his mouth as @Stream turns her eyes from the trap to his face.
- 6–7s (Shot 3): @Stream answers softly with a small teasing smile, looking at him and not at the trap.
- 7–8s (Shot 3): @Stream keeps talking and nods up toward the cave high on the cliff above the stream.
- 8–9s (Shot 3): @Stream keeps speaking gently, her fingers still threading a bamboo strip without looking down.
- 9–10s (Shot 3): @Stream finishes, closes her mouth and keeps smiling at him with her head tilted.
- 10–11s (CUT to Shot 4): @Khang's grin fades and he answers slowly and quietly, lowering the trap into his lap.
- 11–12s (Shot 4): @Khang keeps talking quietly, looking down at the bamboo funnel in his hands.
- 12–13s (Shot 4): @Khang keeps speaking slowly and glances across the deep slow pool at the jungle beyond.
- 13–14s (Shot 4): @Khang keeps talking with a rueful breath, his thumb rubbing the red bandana on his wrist.
- 14–15s (Shot 4): @Khang finishes, closes his mouth and goes back to weaving in silence, while @Stream watches him. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, eager, explaining like a teacher): "It's a fish trap. Easy to swim in, impossible to find the way out."
- Turn 2, 5.9–9.9s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, soft and teasing, a small smile): "Like you. You wandered into our cave and can't find home."
- Turn 3, 10.4–14.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and quiet, caught off guard): "Yeah... like me. I don't even know where home is."
- Pacing: @Khang speaks at an even everyday pace, then @Stream answers at an even everyday pace, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the slow deep pool lapping at flat rocks, split bamboo strips creaking as they are woven, bamboo leaves rustling in a breeze, cicadas in the warming air. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 11 - Clip 3 (`canh-11/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 7s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
High noon at the mouth of the Stone Age clan cave: hard overhead sunlight, short shadows, the clan gathered on the earthen terrace, the elephant-shaped stalactite above.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, a long bamboo spear with a chipped stone tip, barefoot.
- Extra: a ring of clan members in bark-cloth tunics and hide wraps stand silent on the earthen terrace in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of @Moon rising to her feet on the sunlit terrace, slow push-in.
- Shot 2, 5–7s: 85mm close-up of @Roar's sweaty face under the hard noon sun, locked off.
- Shot 3, 7–10s: 35mm medium shot of @Roar holding up his bamboo spear with its stone tip broken off, handheld.
- Shot 4, 10–15s: 50mm over-the-shoulder shot from behind @Roar onto @Moon, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Moon rises from her seat on the sunlit terrace and is already speaking evenly, her eyes on the path below.
- 1–2s (Shot 1): @Moon keeps talking and shades her eyes with one hand against the hard noon sun.
- 2–3s (Shot 1): @Moon keeps speaking as @Roar trudges up onto the terrace, spear in hand, his knees caked with mud.
- 3–4s (Shot 1): @Moon keeps talking, her gaze dropping to his empty free hand and muddy knees.
- 4–5s (Shot 1): @Moon finishes the question, closes her mouth and waits, straight-backed and still.
- 5–6s (CUT to Shot 2): @Roar stops before her and answers loudly and fast, refusing to meet her eyes, sweat on his brow.
- 6–7s (Shot 2): @Roar keeps talking and spreads his thick arms wide to show how huge the boar was.
- 7–8s (CUT to Shot 3): @Roar keeps speaking and holds up his bamboo spear, its stone tip broken off to a jagged stump.
- 8–9s (Shot 3): @Roar keeps talking and jerks a thumb back toward the jungle, his jaw clenched.
- 9–10s (Shot 3): @Roar finishes, closes his mouth and lowers the spear, breathing hard through his nose.
- 10–11s (CUT to Shot 4): @Moon steps closer and answers slowly and gently, her voice low and husky.
- 11–12s (Shot 4): @Moon keeps speaking and lays one wrinkled hand on @Roar's thick forearm.
- 12–13s (Shot 4): @Moon keeps talking slowly and looks around at the silent clan on the terrace.
- 13–14s (Shot 4): @Moon keeps speaking and gives his thick forearm a small firm squeeze of comfort.
- 14–15s (Shot 4): @Moon finishes, closes her mouth and lets go, while @Roar looks down at the broken spear with his mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking at a natural, even conversational pace, even and direct, no warmth yet): "High sun. You left at dawn, Roar. Why are your hands empty?"
- Turn 2, 5.4–9.5s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking quickly in short lively phrases, every word still clear, defensive and loud, avoiding her eyes): "The boar was huge! My spear hit stone and broke. Not my fault!"
- Turn 3, 10.0–14.2s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and gentle, closing the matter): "No one blames you. Some hunts feed us, some don't."
- Pacing: @Moon speaks at an even everyday pace, then @Roar answers quickly, then @Moon answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: noon cicadas buzzing loudly, the stream far below, a heavy tread on dry earth, a broken spear shaft scraping the ground, hot wind over the terrace. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 11 - Clip 4 (`canh-11/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A slow deep pool of the jungle stream in the Stone Age under bright sun: a bank of flat rocks, clumps of bamboo, split bamboo strips and a half-woven funnel-shaped fish trap lying on the stones.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, a long bamboo spear with a chipped stone tip, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: a few small clan children in knee-length bark-cloth tunics clap and splash on the far rocks in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium shot of @Khang lifting the dripping fish trap full of silver fish out of the pool, slow push-in.
- Shot 2, 5–8s: 85mm close-up of @Roar on the flat rocks with his jaw clenched, locked off.
- Shot 3, 8–12s: 50mm over-the-shoulder shot from behind @Roar onto @Khang, locked off.
- Shot 4, 12–15s: 35mm medium two-shot of @Khang and @Roar on the flat rocks beside the full trap, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang hauls the funnel fish trap up out of the deep pool, water pouring through the bamboo, and is already speaking plainly.
- 1–2s (Shot 1): @Khang keeps talking as silver fish flip and flash inside the trap in the bright sun.
- 2–3s (Shot 1): @Khang keeps speaking and carries the dripping trap up onto the flat rocks toward @Roar.
- 3–4s (Shot 1): @Khang keeps talking and sets the trap down on the stones, the live fish still wriggling inside.
- 4–5s (Shot 1): @Khang finishes, closes his mouth and straightens up, wiping his wet hands on his cargo trousers.
- 5–6s (CUT to Shot 2): @Roar stands on the flat rocks with his broken spear and answers in a low growl through clenched teeth.
- 6–7s (Shot 2): @Roar keeps talking with his heavy brows low, his eyes flicking from the fish to @Khang's face.
- 7–8s (Shot 2): @Roar finishes, closes his mouth and looks away, the muscles of his jaw bunching.
- 8–9s (CUT to Shot 3): @Khang steps closer and answers slowly and sincerely, his voice dropping low.
- 9–10s (Shot 3): @Khang keeps talking and shakes his head gently, one open palm held out toward @Roar.
- 10–11s (Shot 3): @Khang keeps speaking and nods up toward the cave where the children are waiting.
- 11–12s (Shot 3): @Khang keeps talking slowly, his eyes steady on @Roar even though the hunter will not look at him.
- 12–13s (CUT to Shot 4): @Khang keeps speaking quietly as small children clap and splash on the far rocks behind them.
- 13–14s (Shot 4): @Khang keeps speaking with quiet weight, his open hand still held out between them.
- 14–15s (Shot 4): @Khang finishes and closes his mouth, as @Roar turns his broad back and walks off along the rocks with his mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, plain and friendly, no gloating): "Roar, these fish feed the whole cave. One trap works all season."
- Turn 2, 5.2–8.0s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking quickly in short lively phrases, every word still clear, a low growl through clenched teeth): "You won. Don't talk like you care about me."
- Turn 3, 8.5–14.1s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and sincere, reaching out): "I don't want to beat you. I just want no child going hungry tonight."
- Pacing: @Khang speaks at an even everyday pace, then @Roar answers quickly, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: water pouring through a bamboo trap, fish flapping wetly inside it, children clapping and splashing, the slow pool lapping at the rocks, bamboo creaking in the breeze. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 12 - Clip 1 (`canh-12/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night inside the large Stone Age clan cave: the elephant-shaped stalactite, bare rock walls with no handprints, a hearth fire glowing red, sleeping beds of dry leaves, hides on poles, deep shadows beyond the firelight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of @Snail's face bathed in flickering blue-white glow from a small camera screen, slow push-in.
- Shot 2, 5–8s: 50mm medium two-shot of @Khang holding the glowing camera for @Snail beside the hearth, locked off.
- Shot 3, 8–10s: 85mm close-up of @Khang's wistful face in the firelight, locked off.
- Shot 4, 10–15s: 50mm over-the-shoulder shot from behind @Khang onto @Snail, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Snail kneels close beside the hearth staring into a small glowing camera screen in @Khang's hands and is already speaking in a breathless rush, mouth wide open.
- 1–2s (Shot 1): @Snail keeps talking fast as blue-white light flickers across his round cheeks and huge eyes.
- 2–3s (Shot 1): @Snail keeps speaking and pokes one small finger toward the glowing screen, then pulls it back.
- 3–4s (Shot 1): @Snail keeps talking and presses both hands to his cheeks in wonder.
- 4–5s (Shot 1): @Snail finishes, closes his mouth and leans even closer to the glow.
- 5–6s (CUT to Shot 2): @Khang holds the camera with its small screen flipped out toward the boy and answers softly, smiling.
- 6–7s (Shot 2): @Khang keeps talking and tilts the glowing screen so the light washes over both their faces.
- 7–8s (Shot 2): @Khang keeps speaking and nods toward the dark rock wall as if warm water could pour out of it.
- 8–9s (CUT to Shot 3): @Khang keeps talking and glances at the red-glowing hearth with a small shrug.
- 9–10s (Shot 3): @Khang keeps speaking quietly as a tiny red light blinks on the camera body under his thumb.
- 10–11s (CUT to Shot 4): @Khang finishes, closes his mouth and lowers his eyes to the glowing screen.
- 11–12s (Shot 4): @Snail looks up from the glow and asks fast, frowning with honest puzzlement.
- 12–13s (Shot 4): @Snail keeps talking and tugs at @Khang's sleeve with one small hand.
- 13–14s (Shot 4): @Snail finishes the question, closes his mouth and waits, his eyes fixed on @Khang's face.
- 14–15s (Shot 4): @Snail keeps staring up at him with his mouth closed, the screen glow flickering over his face in the silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.3s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, breathless wonder, mouth falling open): "Tiny people live in the seeing stone! A thousand fires, bright like stars!"
- Turn 2, 4.8–10.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, soft and wistful, homesick): "That's my home. Bright all night. Hot water comes from the walls. Nobody keeps fire."
- Turn 3, 10.7–13.4s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, quick and curious, blurting it out): "Then why did you leave home and come here?"
- Pacing: @Snail speaks quickly, then @Khang answers at an even everyday pace, then @Snail answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the hearth fire crackling and popping, fish sizzling on bamboo skewers over the coals, a faint electronic hum from the camera, crickets outside the cave mouth. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 12 - Clip 2 (`canh-12/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night inside the large Stone Age clan cave: the elephant-shaped stalactite, bare rock walls with no handprints, a hearth fire glowing red, sleeping beds of dry leaves, hides on poles, deep shadows beyond the firelight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium two-shot of @Stream and @Khang sitting close at one corner of the hearth, slow push-in.
- Shot 2, 3–5s: 85mm close-up of @Stream in the dancing firelight, locked off.
- Shot 3, 5–10s: 50mm over-the-shoulder shot from behind @Stream onto @Khang, locked off.
- Shot 4, 10–15s: 35mm medium two-shot of @Stream and @Khang beside the hearth, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Stream sits by the hearth with a small sleeping child curled in her lap and is already speaking slowly and softly, eyes on @Khang.
- 1–2s (Shot 1): @Stream keeps talking and strokes the sleeping child's back under a hide blanket.
- 2–3s (Shot 1): @Stream keeps speaking as the firelight dances across the red-ochre stripes on her cheeks.
- 3–4s (CUT to Shot 2): @Stream keeps talking softly and tilts her head to read his face.
- 4–5s (Shot 2): @Stream finishes the question, closes her mouth and waits, her hand still on the child's back.
- 5–6s (CUT to Shot 3): @Khang sits at the corner of the hearth with his forearms on his knees and answers quietly, his voice heavy.
- 6–7s (Shot 3): @Khang keeps talking and stares into the flames rather than at her.
- 7–8s (Shot 3): @Khang keeps speaking and spreads his blistered hands wide, as if over a huge crowd.
- 8–9s (Shot 3): @Khang keeps talking and lets his hands fall back onto his knees.
- 9–10s (Shot 3): @Khang finishes the last flat word, closes his mouth and swallows, eyes still on the flames.
- 10–11s (CUT to Shot 4): @Stream turns to him and answers with a puzzled frown, her voice gentle and searching.
- 11–12s (Shot 4): @Stream keeps talking and curls her free fingers into little claws by her face, imitating a playful tiger.
- 12–13s (Shot 4): @Stream keeps speaking with a faint smile at the memory, glancing down at the child in her lap.
- 13–14s (Shot 4): @Stream keeps talking and looks back up at @Khang, waiting for his answer.
- 14–15s (Shot 4): @Stream finishes, closes her mouth and holds his gaze in the dancing firelight. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.8s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and soft, genuinely curious): "Your home has so many fires. Why weren't you happy there?"
- Turn 2, 5.3–9.6s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, quiet and heavy, admitting it): "Back there, I told survival stories to millions of people. All fake."
- Turn 3, 10.1–14.4s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, puzzled, gently searching): "What is fake? Like Snail playing tiger to scare the little ones?"
- Pacing: @Stream speaks slowly and calmly, then @Khang answers at an even everyday pace, then @Stream answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the hearth fire crackling softly, a child's slow sleeping breath, embers popping, wind sighing at the dark cave mouth. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 12 - Clip 3 (`canh-12/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night inside the large Stone Age clan cave: the elephant-shaped stalactite, bare rock walls with no handprints, a hearth fire glowing red, sleeping beds of dry leaves, hides on poles, deep shadows beyond the firelight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium two-shot of @Khang and @Stream at the corner of the hearth, slow push-in.
- Shot 2, 3–7s: 85mm close-up of @Khang turning a dead lighter in his fingers in the firelight, locked off.
- Shot 3, 7–11s: 50mm over-the-shoulder shot from behind @Khang onto @Stream, locked off.
- Shot 4, 11–15s: 35mm medium two-shot of @Khang and @Stream beside the hearth, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang sits at the corner of the hearth turning a small plastic lighter over in his fingers and is already speaking, low and bitter.
- 1–2s (Shot 1): @Khang keeps talking and flicks the dead lighter once with his thumb; it gives no flame.
- 2–3s (Shot 1): @Khang keeps speaking, staring into the low flames, his voice dropping lower with each word.
- 3–4s (CUT to Shot 2): @Khang keeps talking and turns the dead lighter slowly between finger and thumb.
- 4–5s (Shot 2): @Khang keeps speaking, a crooked bitter smile tugging at one corner of his mouth.
- 5–6s (Shot 2): @Khang keeps talking and rubs his eyes with his free hand, shoulders sagging.
- 6–7s (Shot 2): @Khang finishes, closes his mouth and tosses the dead lighter into the grey ash at the edge of the hearth.
- 7–8s (CUT to Shot 3): @Stream watches him without a smile and answers plainly and seriously, her hand resting on the sleeping child.
- 8–9s (Shot 3): @Stream keeps talking, her eyes steady on his face across the low flames.
- 9–10s (Shot 3): @Stream keeps speaking and leans slightly toward him as she asks the question.
- 10–11s (Shot 3): @Stream finishes the question, closes her mouth and waits for his answer without blinking.
- 11–12s (CUT to Shot 4): @Khang lifts his eyes from the fire to hers and answers slowly and quietly.
- 12–13s (Shot 4): @Khang keeps speaking slowly, a long breath between the words, his jaw softening.
- 13–14s (Shot 4): @Khang finishes, closes his mouth and holds her gaze, his shoulders loosening.
- 14–15s (Shot 4): @Stream gives one small slow nod with her mouth closed, as the fire crackles between them in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, low and bitter, confessing): "Exactly. Someone else made my fires. The fish came from a market. I just acted hungry."
- Turn 2, 6.7–10.7s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, plain and serious, no smile): "Here, whoever fakes it really starves. These days, are you faking?"
- Turn 3, 11.2–14.0s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and quiet, finally honest): "No. For the first time, I'm not."
- Pacing: @Khang speaks at an even everyday pace, then @Stream answers at an even everyday pace, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the hearth fire crackling, the dry click of a dead lighter, a small plastic object dropping into soft ash, crickets and a distant owl outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 12 - Clip 4 (`canh-12/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night inside the large Stone Age clan cave: the elephant-shaped stalactite, bare rock walls with no handprints, a hearth fire glowing red, sleeping beds of dry leaves, hides on poles, deep shadows beyond the firelight.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium two-shot of @Stream and @Khang beside the hearth, slow push-in.
- Shot 2, 3–6s: 85mm close-up of @Stream looking down at @Khang's blistered palm in her hands, locked off.
- Shot 3, 6–11s: 50mm over-the-shoulder shot from behind @Stream onto @Khang unclipping the small camera from his chest, slow push-in.
- Shot 4, 11–15s: 85mm close-up of @Stream in the warm firelight, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Stream reaches over and takes @Khang's right hand, turning it palm up in the firelight, and is already speaking, warm and matter-of-fact.
- 1–2s (Shot 1): @Stream keeps talking and runs her thumb gently over the raw blisters on his palm.
- 2–3s (Shot 1): @Stream keeps speaking and glances down at his scraped muddy boots, then back to his face.
- 3–4s (CUT to Shot 2): @Stream keeps talking and taps his palm lightly with one finger, her eyes on the blisters.
- 4–5s (Shot 2): @Stream keeps speaking with a small firm nod, still holding his hand in both of hers.
- 5–6s (Shot 2): @Stream finishes and closes her mouth as the small camera on @Khang's chest gives a single beep and its red light goes dark.
- 6–7s (CUT to Shot 3): @Khang glances down at the dark camera and answers sheepishly with an embarrassed half-smile.
- 7–8s (Shot 3): @Khang keeps talking and unclips the small camera from his chest harness with his free hand.
- 8–9s (Shot 3): @Khang keeps speaking, turning the dark camera over and tapping it once with a fingertip.
- 9–10s (Shot 3): @Khang keeps talking and shrugs with a sheepish breath of a laugh.
- 10–11s (Shot 3): @Khang finishes, closes his mouth and sets the camera down on a flat stone beside the hearth.
- 11–12s (CUT to Shot 4): @Stream looks at the camera, then up at him, and answers slowly and softly.
- 12–13s (Shot 4): @Stream keeps speaking softly and closes her fingers around his blistered hand.
- 13–14s (Shot 4): @Stream keeps talking with a small warm smile in the firelight, her eyes on his.
- 14–15s (Shot 4): @Stream finishes, closes her mouth and keeps holding his hand as the fire crackles in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, warm and matter-of-fact): "Real people get blisters, scraped feet, empty bellies. You are a real person now."
- Turn 2, 5.9–10.9s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, sheepish, a little embarrassed): "The seeing stone is going to sleep. Battery's almost gone. Not much more filming."
- Turn 3, 11.4–14.2s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and soft, an invitation): "Let it sleep. Talk to me instead."
- Pacing: @Stream speaks at an even everyday pace, then @Khang answers at an even everyday pace, then @Stream answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a single soft electronic beep, the hearth fire crackling and popping, a plastic clip unsnapping, crickets and frogs outside the dark cave mouth. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 13 - Clip 1 (`canh-13/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Early misty morning at the mouth of the Stone Age clan cave: thick white mist over the jungle below, cool grey-blue light, an empty bed of dry leaves just inside the entrance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium tracking shot of the young forager running from the empty leaf bed to the cave mouth, handheld follow from the front.
- Shot 2, 3–9s: 85mm close-up of the old clan leader gazing out at the mist, slow push-in.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the old woman onto the young forager, locked off.
- Shot 4, 13–15s: 24mm wide shot of both at the misty cave mouth from inside the cave, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Stream runs barefoot out of the dim cave past an empty bed of dry leaves and is already speaking fast, breath short, eyes on @Moon.
- 1–2s (Shot 1): @Stream keeps talking as she points back at the flattened leaf bed, where no spear leans against the rock any more.
- 2–3s (Shot 1): @Stream reaches @Moon's side at the misty cave mouth, finishes her words and closes her mouth, chest heaving.
- 3–4s (CUT to Shot 2): @Moon keeps her eyes on the white mist below and begins answering slowly in a low husky voice, without turning her head.
- 4–5s (Shot 2): @Moon keeps speaking slowly, her calm eyes fixed on the place where the jungle disappears into the mist.
- 5–6s (Shot 2): @Moon's fingers tighten around the green bamboo ember tube against her hide cloak as she goes on.
- 6–7s (Shot 2): @Moon talks on in a husky murmur, jaw set, a slow breath lifting her narrow shoulders.
- 7–8s (Shot 2): @Moon lowers her eyes for a moment as she says the last heavy words.
- 8–9s (Shot 2): @Moon finishes and closes her mouth, the red ochre dot on her forehead still in the grey light.
- 9–10s (CUT to Shot 3): @Stream steps around to face her and starts speaking fast, both hands open, her voice climbing.
- 10–11s (Shot 3): @Stream keeps talking quickly, pointing down into the mist toward the jungle, while @Moon listens with her mouth closed.
- 11–12s (Shot 3): @Stream's breath catches as she goes on, the snail-shell necklace trembling on her chest.
- 12–13s (Shot 3): @Stream finishes the last words and closes her mouth, staring at @Moon, jaw tight.
- 13–14s (CUT to Shot 4): @Moon turns her head slowly toward @Stream, mouth closed, her lips pressed thin.
- 14–15s (Shot 4): Both stand silent at the cave mouth as white mist drifts in around their bare feet, mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.1s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, breathless and urgent): "Grandmother, Roar's bed is cold. He left before moonset."
- Turn 2, 3.6–9.0s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and heavy, eyes on the mist): "He went after the rhino, alone. Losing to the stranger burned him inside."
- Turn 3, 9.5–12.8s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, rising alarm, pleading): "A rhino can crush a man. He can't do this alone!"
- Pacing: @Stream speaks quickly, then @Moon answers slowly and calmly, then @Stream answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: quick bare footsteps on damp stone, water dripping at the cave mouth, distant birdcalls muffled by thick mist, dry leaves rustling in a cool breeze. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 13 - Clip 2 (`canh-13/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Early misty morning at the mouth of the Stone Age clan cave: thick white mist over the jungle below, cool grey-blue light, an empty bed of dry leaves just inside the entrance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the young man in the olive shirt at the misty cave mouth, slow push-in.
- Shot 2, 5–9s: 85mm close-up of the old clan leader, locked off.
- Shot 3, 9–13s: 35mm over-the-shoulder shot from behind the old woman onto the young man, slow push-in.
- Shot 4, 13–15s: 85mm close-up of the young man, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang yanks the laces of his brown hiking boots tight, straightens up and is already speaking to @Moon in an even, practical voice.
- 1–2s (Shot 1): @Khang keeps talking as he lifts a plastic whistle on a cord and lets it drop against his chest harness.
- 2–3s (Shot 1): @Khang slips a folded multitool into his trouser pocket while he goes on speaking.
- 3–4s (Shot 1): @Khang nods toward the misty jungle below as he speaks, the small chest camera dark on its harness.
- 4–5s (Shot 1): @Khang finishes and closes his mouth, waiting, both hands on the harness straps.
- 5–6s (CUT to Shot 2): @Moon studies him and answers slowly in a low husky voice, her calm eyes narrowing.
- 6–7s (Shot 2): @Moon keeps speaking, the green bamboo ember tube resting in the crook of her arm.
- 7–8s (Shot 2): @Moon tilts her head as she finishes her question and closes her mouth.
- 8–9s (Shot 2): @Khang holds her gaze in silence, mouth closed, breathing out once through his nose.
- 9–10s (CUT to Shot 3): @Khang starts answering slowly and quietly, his showman grin gone, eyes steady on @Moon.
- 10–11s (Shot 3): @Khang keeps talking in a low honest voice while @Moon watches him with her mouth closed.
- 11–12s (Shot 3): @Khang touches two fingers to his own chest as he goes on speaking.
- 12–13s (Shot 3): @Khang glances out toward the misty jungle below and keeps speaking softly, his voice low.
- 13–14s (CUT to Shot 4): @Khang says the last words looking straight at @Moon, his stubbled jaw set.
- 14–15s (Shot 4): @Khang finishes and closes his mouth and waits, a strand of mist drifting across his face. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, steady and practical, already geared up): "Grandma, let me find him. I have a whistle. Stream knows tracks."
- Turn 2, 5.2–8.5s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, probing, weighing him up): "Roar wants you gone. Why look for him?"
- Turn 3, 9.0–14.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, quiet and sincere, the grin gone): "Hating me doesn't make him less one of us. Our people come home."
- Pacing: @Khang speaks at an even everyday pace, then @Moon answers slowly and calmly, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: boot laces pulled tight, a plastic whistle tapping against a chest strap, water dripping at the cave mouth, muffled birdcalls in the mist. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 13 - Clip 3 (`canh-13/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Deep primeval jungle in the Stone Age in the morning: damp earth with fresh footprints, broken twigs, leaves turned pale side up, giant trunks and hanging lianas, shafts of light through the canopy.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 35mm medium shot of the young forager crouching over the footprints, slow push-in.
- Shot 2, 6–11s: 50mm close-up of the young man lifting a whistle on a cord, handheld.
- Shot 3, 11–13s: 35mm over-the-shoulder shot from behind the young man onto the forager raising one hand, locked off.
- Shot 4, 13–15s: 24mm wide shot of both among giant trunks and hanging lianas, slow push-in toward the dark undergrowth.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Stream crouches low over a line of fresh bare footprints pressed into the damp earth and is already speaking in a low, certain voice.
- 1–2s (Shot 1): @Stream traces the rim of a huge three-toed rhino print beside the human footprints with one finger as she talks.
- 2–3s (Shot 1): @Stream picks up a snapped twig and turns it in a shaft of light, still speaking.
- 3–4s (Shot 1): @Stream flips a fallen leaf over to show its pale underside while she keeps talking, @Khang bending close behind her.
- 4–5s (Shot 1): @Stream presses two fingers into the soft edge of a footprint as she goes on.
- 5–6s (Shot 1): @Stream finishes, closes her mouth and looks up at @Khang, eyes sharp.
- 6–7s (CUT to Shot 2): @Khang lifts the plastic whistle on its cord from his chest and starts talking fast, eyebrows up, eager.
- 7–8s (Shot 2): @Khang keeps speaking quickly, wagging the whistle between two fingers like a teacher.
- 8–9s (Shot 2): @Khang holds up three fingers as he goes on, his showman energy back in his face.
- 9–10s (Shot 2): @Khang talks on, pointing the whistle out toward the deep green trees.
- 10–11s (Shot 2): @Khang keeps talking fast as he raises the whistle toward his lips.
- 11–12s (CUT to Shot 3): @Khang closes his mouth with the whistle at his lips as @Stream flicks one flat hand up beside him, head cocked, listening.
- 12–13s (Shot 3): @Stream whispers, barely moving, her eyes sliding toward the dark undergrowth down the slope.
- 13–14s (CUT to Shot 4): @Stream finishes the whisper, closes her mouth and points one finger down the slope.
- 14–15s (Shot 4): @Khang gives three short sharp whistle blows toward the slope while @Stream holds perfectly still beside him, mouth closed, listening. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.8s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, focused tracker, low and certain): "Roar's footprints follow the rhino tracks. Here, broken twigs, leaves turned over. Not long ago."
- Turn 2, 6.3–11.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, quick and eager, explaining): "A whistle carries farther than shouting. Three blasts means help. If he hears it, he'll shout back."
- Turn 3, 11.9–13.5s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking slowly and softly, unhurried, with a short natural pause between phrases, a sharp whisper, hand raised): "Shh... listen. Down there."
- Pacing: @Stream speaks at an even everyday pace, then @Khang answers quickly, then @Stream answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: damp leaves crunching underfoot, a twig cracking, water dripping from the canopy, insects humming, then near silence broken by three short shrill whistle blows echoing through the trees. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 13 - Clip 4 (`canh-13/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A limestone sinkhole in the primeval jungle at midday: a pit about four meters deep with steep mossy rock walls, ferns and reeds hanging over the rim, a big tree right at the edge, a shaft of sunlight reaching the soft earthen bottom.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, a long bamboo spear with a chipped stone tip, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm high-angle medium shot from the rim down onto the hunter sitting against the rock wall, locked off.
- Shot 2, 4–9s: 50mm low-angle close-up of the young man kneeling at the rim and looking down, slow push-in.
- Shot 3, 9–12s: 40mm medium shot of the hunter at the bottom, his swollen ankle in the foreground, slow push-in.
- Shot 4, 12–15s: 85mm close-up of the hunter's face in the shaft of sunlight, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Roar sits slumped against the mossy rock wall at the bottom of the sinkhole and is already shouting up hoarsely, chin raised, eyes hard.
- 1–2s (Shot 1): @Roar keeps shouting, one big hand waving the rim away, his bamboo spear lying flat in the dirt beside him.
- 2–3s (Shot 1): @Roar pushes on the rock to rise, winces, and drops back down as he shouts the last words.
- 3–4s (Shot 1): @Roar finishes and closes his mouth, breathing hard through his nose, his left ankle swollen and purple.
- 4–5s (CUT to Shot 2): @Khang kneels at the fern-lined rim, both hands on the edge, and starts answering firmly, looking straight down.
- 5–6s (Shot 2): @Khang keeps talking calmly, nodding down toward the purple swollen ankle at the bottom of the pit.
- 6–7s (Shot 2): @Khang holds out one flat palm in a stay-there gesture as he goes on.
- 7–8s (Shot 2): @Khang keeps speaking evenly, his eyes measuring the steep mossy wall below him.
- 8–9s (Shot 2): @Khang finishes and closes his mouth, still leaning over the rim, fern fronds brushing his arms.
- 9–10s (CUT to Shot 3): @Roar lets his head fall back against the rock and starts speaking low, the force draining out of his voice.
- 10–11s (Shot 3): @Roar keeps talking slowly, his eyes drifting up to the fringe of reeds along the rim.
- 11–12s (Shot 3): @Roar's broad shoulders sag as he goes on, his voice dropping lower.
- 12–13s (CUT to Shot 4): @Roar speaks the last words almost under his breath, swallowing hard, his eyes still on the rim.
- 13–14s (Shot 4): @Roar finishes and closes his mouth, his eyes still fixed on the bright rim above.
- 14–15s (Shot 4): @Roar sits silent, mouth closed, his chest rising and falling slowly in the shaft of sunlight. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.8s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking quickly in short lively phrases, every word still clear, shouting up, proud and hoarse): "Go away! I don't need pity! I can climb out myself!"
- Turn 2, 4.3–8.6s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, firm and calm, leaning over the rim): "With your ankle that swollen? How? Sit still. Don't try to stand."
- Turn 3, 9.1–13.7s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking slowly and softly, unhurried, with a short natural pause between phrases, voice dropping, worn out): "I've been here since night. The tiger walked the edge twice."
- Pacing: @Roar speaks quickly, then @Khang answers at an even everyday pace, then @Roar answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: pebbles trickling down a rock wall, ferns rustling at the rim, a hoarse voice echoing off stone, cicadas droning, distant birds. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 14 - Clip 1 (`canh-14/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A limestone sinkhole in the primeval jungle at midday: a pit about four meters deep with steep mossy rock walls, ferns and reeds hanging over the rim, a big tree right at the edge, a shaft of sunlight reaching the soft earthen bottom.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of the pair pulling long lianas off a giant trunk at the sinkhole rim, handheld.
- Shot 2, 5–10s: 50mm close-up of the young forager holding the braided end taut, slow push-in.
- Shot 3, 10–15s: 50mm over-the-shoulder shot from behind the forager onto the young man braiding, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang hauls a long green liana down from a giant trunk at the sinkhole rim and is already talking fast, @Stream tugging another vine beside him.
- 1–2s (Shot 1): @Khang snaps a single thin vine between his fists to show how weak it is, still talking.
- 2–3s (Shot 1): @Khang lays three long vines side by side on the moss and starts braiding them, speaking quickly.
- 3–4s (Shot 1): @Khang keeps talking as his hands flip the three strands over one another in a tight braid.
- 4–5s (Shot 1): @Khang pushes the loose end toward @Stream and finishes his words with an urgent nod.
- 5–6s (CUT to Shot 2): @Khang closes his mouth; @Stream takes hold of the end with both hands, braces her bare feet and starts asking, puzzled.
- 6–7s (Shot 2): @Stream keeps speaking as she leans back and pulls the thick braid taut, eyes narrowing at it.
- 7–8s (Shot 2): @Stream runs her thumb along the twisted strands while she talks, head tilted.
- 8–9s (Shot 2): @Stream glances from the rope to the rattan basket on her own back as she goes on.
- 9–10s (Shot 2): @Stream finishes her question and closes her mouth, eyebrows raised at @Khang.
- 10–11s (CUT to Shot 3): @Khang freezes mid-braid, eyes darting sideways, then starts answering with an awkward half-laugh.
- 11–12s (Shot 3): @Khang keeps talking, scratching his stubbled jaw with one hand, eyes sliding away from hers.
- 12–13s (Shot 3): @Khang quickly corrects himself, waving one hand toward the far treetops as he speaks.
- 13–14s (Shot 3): @Khang finishes with a sheepish grin and closes his mouth, going back to the braid.
- 14–15s (Shot 3): @Khang twists the three strands tighter in silence, mouth closed, the thick green rope growing in his hands. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, quick and busy, hands working): "One vine snaps. Braid three together and it'll hold a buffalo. Pull it tight for me!"
- Turn 2, 5.7–10.0s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, curious, testing the rope): "Where did you learn this? We braid baskets, never rope this thick."
- Turn 3, 10.5–13.8s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, flustered, covering it fast): "The internet. I mean... a place very far away."
- Pacing: @Khang speaks quickly, then @Stream answers at an even everyday pace, then @Khang answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: long lianas tearing loose from a trunk with a rush of leaves, dry vine fibers creaking as they twist, cicadas droning, a woodpecker tapping far off. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 14 - Clip 2 (`canh-14/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 6s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A limestone sinkhole in the primeval jungle at midday: a pit about four meters deep with steep mossy rock walls, ferns and reeds hanging over the rim, a big tree right at the edge, a shaft of sunlight reaching the soft earthen bottom.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, a long bamboo spear with a chipped stone tip, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–6s: 50mm medium shot of the young man kneeling beside the hunter's swollen ankle at the bottom of the sinkhole, slow push-in.
- Shot 2, 6–10s: 85mm close-up of the hunter's face, jaw clenched, handheld.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the hunter onto the young man, locked off.
- Shot 4, 13–15s: 35mm medium two-shot of both against the mossy wall in the shaft of sunlight, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang kneels on the soft earth beside @Roar, gently pressing the purple swollen ankle with two fingers, and is already speaking calmly.
- 1–2s (Shot 1): @Khang keeps talking as he lays two straight sticks along either side of the ankle.
- 2–3s (Shot 1): @Khang pulls the red bandana from his trouser pocket and keeps speaking evenly, eyes on the joint.
- 3–4s (Shot 1): @Khang wraps the red bandana around the sticks while he goes on, glancing up at @Roar.
- 4–5s (Shot 1): @Khang talks on with a small shrug, holding both ends of the bandana ready.
- 5–6s (Shot 1): @Khang finishes and closes his mouth, then pulls the bandana knot tight around the splint.
- 6–7s (CUT to Shot 2): @Roar clenches his jaw, the cords of his neck standing out, and starts speaking through gritted teeth.
- 7–8s (Shot 2): @Roar keeps talking hard and fast, sweat on his heavy brows, both fists pressed into the dirt.
- 8–9s (Shot 2): @Roar keeps speaking through his teeth, his head pressed back against the mossy rock.
- 9–10s (Shot 2): @Roar lets out one hoarse cry, then clamps his mouth shut, panting through his nose.
- 10–11s (CUT to Shot 3): @Khang ties off the knot, glances up at him and starts answering with a crooked smirk.
- 11–12s (Shot 3): @Khang keeps talking dryly, opening one hand toward the empty pit around them.
- 12–13s (Shot 3): @Khang tilts his head as he goes on, the smirk widening, while @Roar stares at him with his mouth closed.
- 13–14s (CUT to Shot 4): @Khang finishes and closes his mouth, sitting back on his heels beside the neat red-bound splint.
- 14–15s (Shot 4): @Roar lets out a long breath through his nose, mouth closed, the corner of his lip twitching. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.8s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, calm medic voice, hands busy): "Not broken, just twisted. I'll splint it. If it hurts, scream. No shame in that."
- Turn 2, 6.3–9.4s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking quickly in short lively phrases, every word still clear, through gritted teeth, then a roar): "Hunters don't scream! A hunter screams, the animals run! Argh!"
- Turn 3, 9.9–13.5s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, dry, with a crooked smirk): "There are no animals down here. Just you and me."
- Pacing: @Khang speaks at an even everyday pace, then @Roar answers quickly, then @Khang answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: two sticks knocking together, cloth knotted and pulled tight, harsh breathing echoing off the rock walls, pebbles trickling, cicadas far above. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 14 - Clip 3 (`canh-14/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A limestone sinkhole in the primeval jungle at midday: a pit about four meters deep with steep mossy rock walls, ferns and reeds hanging over the rim, a big tree right at the edge, a shaft of sunlight reaching the soft earthen bottom.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, his left ankle splinted between two straight sticks bound with a red bandana, leaning on a wooden staff, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- Wardrobe: in this shot @Roar and @Khang wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of both against the mossy wall, slow push-in.
- Shot 2, 5–10s: 50mm over-the-shoulder shot from behind the hunter onto the young man tying the rope, locked off.
- Shot 3, 10–13s: 85mm close-up of the hunter studying the knot on his chest, slow push-in.
- Shot 4, 13–15s: 35mm medium two-shot of both at the bottom of the sinkhole, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Roar turns his face aside from @Khang toward the mossy wall and is already speaking, low and gruff.
- 1–2s (Shot 1): @Roar keeps talking slowly, his jaw working, as @Khang loops the thick vine rope behind his back.
- 2–3s (Shot 1): @Roar goes on in a rough murmur, still refusing to look at @Khang, his wooden staff propped beside him.
- 3–4s (Shot 1): @Roar keeps speaking, staring at the rock as @Khang passes the rope across his broad chest over the boar-hide vest.
- 4–5s (Shot 1): @Roar finishes and closes his mouth, nostrils flaring, his face still turned to the rock.
- 5–6s (CUT to Shot 2): @Khang forms a small loop in the rope and starts answering in an even, matter-of-fact voice.
- 6–7s (Shot 2): @Khang keeps talking as he feeds the rope end up through the small loop.
- 7–8s (Shot 2): @Khang goes on speaking while he takes the end around the standing rope, eyes on his hands.
- 8–9s (Shot 2): @Khang talks on with a wry little shrug, tucking the end back down through the loop.
- 9–10s (Shot 2): @Khang finishes and closes his mouth, pulling the knot snug against @Roar's chest.
- 10–11s (CUT to Shot 3): @Roar looks down at the knot and starts speaking, his heavy brows drawing together.
- 11–12s (Shot 3): @Roar keeps talking as he tugs the rope with one hand and feels the loop stay firm without tightening.
- 12–13s (Shot 3): @Roar runs his thumb over the knot as he goes on, a grudging note in his voice.
- 13–14s (CUT to Shot 4): @Roar lifts his eyes to @Khang at last and asks the last words, his voice rough.
- 14–15s (Shot 4): @Roar finishes and closes his mouth; @Khang just taps the knot twice with a small grin, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking slowly and softly, unhurried, with a short natural pause between phrases, low and gruff, face turned away): "Why save me? I wanted you out of our cave."
- Turn 2, 5.1–10.1s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, matter-of-fact, a little wry): "Where I'm from, the village helps whoever falls. Kick me out once you're up."
- Turn 3, 10.6–14.4s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking at a natural, even conversational pace, grudging curiosity): "Strange knot. Tight, but it doesn't squeeze. Who taught you?"
- Pacing: @Roar speaks slowly and calmly, then @Khang answers at an even everyday pace, then @Roar answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the thick vine rope rasping as it is looped and knotted, heavy breathing, pebbles trickling down the wall, cicadas far above. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 14 - Clip 4 (`canh-14/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A limestone sinkhole in the primeval jungle at midday: a pit about four meters deep with steep mossy rock walls, ferns and reeds hanging over the rim, a big tree right at the edge, a shaft of sunlight reaching the soft earthen bottom.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, his left ankle splinted between two straight sticks bound with a red bandana, leaning on a wooden staff, barefoot.
- Wardrobe: in this shot @Khang and @Roar wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the young man hauling the rope wrapped around the big tree trunk, handheld.
- Shot 2, 4–7s: 24mm wide shot of the sinkhole rim as the hunter is hauled up onto the grass, slow push-in.
- Shot 3, 7–11s: 85mm close-up of the hunter lying on his back in the grass, locked off.
- Shot 4, 11–15s: 35mm medium two-shot of both on the grassy rim, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang braces his boots against the roots of the big tree, the vine rope wrapped once around its trunk, and is already shouting the rhythm, hauling hard.
- 1–2s (Shot 1): @Khang heaves back on the rope, still shouting, while a second pair of hands hauls behind him in soft focus.
- 2–3s (Shot 1): @Khang keeps shouting as the rope creaks around the trunk and inches up out of the pit.
- 3–4s (Shot 1): @Khang finishes and closes his mouth, leaning his whole weight back, teeth bared with effort.
- 4–5s (CUT to Shot 2): @Roar rolls over the grassy rim onto his back, the red-bound splint dragging behind him, and starts speaking between gasps.
- 5–6s (Shot 2): @Roar lies flat on the grass, chest heaving, and keeps talking breathlessly up at the sky.
- 6–7s (Shot 2): @Roar turns his head toward @Khang, still talking, sweat running into his heavy brows.
- 7–8s (CUT to Shot 3): @Roar speaks slowly and solemnly, his deep-set eyes fixed on @Khang, his breath still ragged.
- 8–9s (Shot 3): @Roar lifts one big hand off the grass as he keeps talking, his voice rough and steady.
- 9–10s (Shot 3): @Roar says the last words with weight, jaw set, his hand held out.
- 10–11s (Shot 3): @Roar finishes and closes his mouth, his hand still raised, breathing hard.
- 11–12s (CUT to Shot 4): @Khang drops to one knee beside him, clasps the raised hand and starts answering with a breathless laugh.
- 12–13s (Shot 4): @Khang keeps talking, grinning wide, as he pulls @Roar up to sitting on the grassy rim.
- 13–14s (Shot 4): @Khang finishes with a wink and closes his mouth, still holding the big hand in his.
- 14–15s (Shot 4): @Roar huffs a short laugh through his nose, mouth closed, still holding @Khang's hand, both chests heaving. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, straining, shouting the rhythm): "Pull! One, two, three! Around the tree, so he can't fall!"
- Turn 2, 4.2–10.4s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking slowly and softly, unhurried, with a short natural pause between phrases, out of breath, solemn): "I'm up. From today, you are my brother. Whoever wants you gone, goes through me."
- Turn 3, 10.9–13.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, laughing, relieved): "Then, Roar, stop calling me stranger, okay?"
- Pacing: @Khang speaks quickly, then @Roar answers slowly and calmly, then @Khang answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the vine rope creaking around a tree trunk, bark rasping, grunts of effort, soil and pebbles spilling into the pit, heavy panting, leaves rustling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 15 - Clip 1 (`canh-15/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A jungle stream bank in the Stone Age in late afternoon: the water suddenly brown and fast, branches and leaves racing past, reed beds and big rocks along the bank, the sun still bright overhead while black clouds cover the distant headwater peaks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, his left ankle splinted between two straight sticks bound with a red bandana, leaning on a wooden staff, barefoot.
- Wardrobe: in this shot @Khang and @Roar wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot of the young man helping the limping hunter along the stream bank, handheld follow.
- Shot 2, 5–10s: 85mm close-up of the hunter leaning on his staff, locked off.
- Shot 3, 10–12s: 50mm over-the-shoulder shot from behind the hunter onto the young man, handheld.
- Shot 4, 12–15s: 24mm wide shot of the brown stream racing past the pair as a big branch sweeps by, slow pan.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang walks along the stream bank with @Roar's arm over his shoulder, stops short, and is already speaking uneasily, eyes on the water.
- 1–2s (Shot 1): @Khang keeps talking as he stares at the brown, fast water churning where it ran clear this morning.
- 2–3s (Shot 1): @Khang leans closer to the water, still speaking, while @Roar steadies himself on his wooden staff.
- 3–4s (Shot 1): @Khang dips two fingers into the muddy water and frowns at them as he talks.
- 4–5s (Shot 1): @Khang finishes his question and closes his mouth, looking up at @Roar.
- 5–6s (CUT to Shot 2): @Roar waves one big hand at the water and starts answering in a gruff, dismissive voice.
- 6–7s (Shot 2): @Roar keeps talking, shifting his weight onto the staff to spare the splinted ankle.
- 7–8s (Shot 2): @Roar shrugs his broad shoulders as he goes on, unbothered, his eyes already on the path ahead.
- 8–9s (Shot 2): @Roar keeps speaking, half turning to limp on along the bank, the staff tapping the stones.
- 9–10s (Shot 2): @Roar finishes and closes his mouth, already limping one step forward along the reed-lined bank.
- 10–11s (CUT to Shot 3): @Khang takes hold of @Roar's arm, points up at the bright sun and starts talking fast.
- 11–12s (Shot 3): @Khang keeps speaking quickly, swinging his pointing hand down to the racing water.
- 12–13s (CUT to Shot 4): A thick leafy branch races past them on the brown current as @Khang keeps talking, pointing after it.
- 13–14s (Shot 4): @Khang finishes and closes his mouth, eyes darting to the wet line on the rocks where the water is climbing.
- 14–15s (Shot 4): @Roar stares down at the rising water in silence, mouth closed, his knuckles tightening on the staff. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, uneasy, slowing to a stop): "Wait. This morning the stream was clear. Why is it brown now?"
- Turn 2, 5.2–9.3s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking at a natural, even conversational pace, dismissive, waving it off): "Rain upstream makes the water brown. Every season. Nothing to fear."
- Turn 3, 9.8–13.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, urgent, pointing hard): "It's sunny here. But look at those branches racing. The water's rising fast!"
- Pacing: @Khang speaks at an even everyday pace, then @Roar answers at an even everyday pace, then @Khang answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: fast muddy water rushing and gurgling, a heavy branch knocking against rocks as it races past, reeds hissing in the wind, a wooden staff tapping on stones. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 15 - Clip 2 (`canh-15/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A jungle stream bank in the Stone Age in late afternoon: the water suddenly brown and fast, branches and leaves racing past, reed beds and big rocks along the bank, the sun still bright overhead while black clouds cover the distant headwater peaks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm low-angle medium shot of the young man standing on a tall rock and pointing upstream, handheld.
- Shot 2, 4–9s: 50mm over-the-shoulder shot from behind the young man onto the forager climbing up beside him, locked off.
- Shot 3, 9–13s: 85mm close-up of the young man with the wind in his face, slow push-in.
- Shot 4, 13–15s: 24mm wide shot from behind both on the rock toward black clouds over the distant peaks under a bright sun, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang scrambles up onto a tall rock above the bank, straightens, and is already speaking fast, one arm stretched toward the upstream peaks.
- 1–2s (Shot 1): @Khang keeps talking, squinting past the bright sun at a wall of black clouds over the distant headwaters.
- 2–3s (Shot 1): @Khang turns his head back toward the bank as he goes on, his pointing arm still raised.
- 3–4s (Shot 1): @Khang keeps speaking quickly, sweeping his hand from the clouds down along the brown stream.
- 4–5s (CUT to Shot 2): @Khang finishes and closes his mouth as @Stream climbs the rock beside him, bare feet finding the cracks.
- 5–6s (Shot 2): @Stream straightens, follows his arm with her eyes and starts asking in a low, careful voice.
- 6–7s (Shot 2): @Stream keeps talking, glancing down at the brown water racing along the foot of the rock.
- 7–8s (Shot 2): @Stream's hand closes around the snail-shell necklace on her chest as she goes on.
- 8–9s (Shot 2): @Stream finishes her question and closes her mouth, her lips pressed pale.
- 9–10s (CUT to Shot 3): @Khang turns to face her and starts answering fast and sharp, no grin left on his face.
- 10–11s (Shot 3): @Khang keeps talking, slicing one flat hand down through the air like a falling wall of water.
- 11–12s (Shot 3): @Khang goes on quickly, his eyes locked on hers, his jaw tight.
- 12–13s (Shot 3): @Khang finishes the last words and closes his mouth, breathing hard, his eyes still on hers.
- 13–14s (CUT to Shot 4): @Stream turns back toward the black clouds in silence, mouth closed, the wind whipping her long hair.
- 14–15s (Shot 4): Both stand still on the rock under the bright sun, mouths closed, while thunder rolls faintly from the dark peaks. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.3s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, urgent, pointing upstream): "Look, black clouds all over the headwaters. Tonight all that water comes here."
- Turn 2, 4.8–8.8s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, quiet, working it out): "Our cave sits by the stream. Can water reach our beds?"
- Turn 3, 9.3–12.9s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, sharp warning, no showman left): "Flash floods don't creep. It hits all at once and takes everything!"
- Pacing: @Khang speaks quickly, then @Stream answers at an even everyday pace, then @Khang answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: rushing brown water below, a low far-off rumble of thunder from the distant peaks, reeds hissing in a rising wind, bare feet scraping on rock. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 15 - Clip 3 (`canh-15/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A jungle stream bank in the Stone Age in late afternoon: the water suddenly brown and fast, branches and leaves racing past, reed beds and big rocks along the bank, the sun still bright overhead while black clouds cover the distant headwater peaks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, his left ankle splinted between two straight sticks bound with a red bandana, leaning on a wooden staff, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- Wardrobe: in this shot @Roar and @Khang wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 85mm close-up of the hunter leaning on his staff, eyes on the black clouds, slow push-in.
- Shot 2, 4–7s: 50mm medium two-shot of the hunter and the young man on the bank, locked off.
- Shot 3, 7–10s: 85mm close-up of the young man turning sharply, handheld.
- Shot 4, 10–15s: 35mm over-the-shoulder shot from behind the young man onto the hunter pointing toward the cliffs, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Roar leans on his wooden staff staring upstream at the black clouds and is already speaking slowly, his voice low and far away.
- 1–2s (Shot 1): @Roar keeps talking, his heavy brows drawing down, the brown water roaring past below him.
- 2–3s (Shot 1): @Roar's eyes darken and go distant as he goes on, his knuckles pale on the staff.
- 3–4s (Shot 1): @Roar keeps speaking slowly, swallowing once between the words, his gaze fixed on the clouds.
- 4–5s (CUT to Shot 2): @Roar lowers his head as he talks on, while @Khang turns to stare at him.
- 5–6s (Shot 2): @Roar says the last heavy words almost under his breath, his grip loosening on the staff.
- 6–7s (Shot 2): @Roar finishes and closes his mouth, jaw tight, eyes on the ground.
- 7–8s (CUT to Shot 3): @Khang turns sharply toward @Roar and starts talking fast, his breath quick.
- 8–9s (Shot 3): @Khang keeps speaking quickly, his eyes searching the cliffs above the trees.
- 9–10s (Shot 3): @Khang finishes the question and closes his mouth, staring at @Roar, his chest rising fast.
- 10–11s (CUT to Shot 4): @Roar lifts his head, raises his staff toward the distant limestone cliffs and starts answering fast and firm.
- 11–12s (Shot 4): @Roar keeps talking with force, holding the staff high toward a dark ledge on the cliff face.
- 12–13s (Shot 4): @Roar turns his head over his shoulder as he calls out the last order, his voice booming.
- 13–14s (Shot 4): @Roar finishes and closes his mouth, the staff still raised toward the cliff.
- 14–15s (Shot 4): @Khang nods once, mouth closed, already backing away along the bank toward the reeds. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.6s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking slowly and softly, unhurried, with a short natural pause between phrases, low and haunted, remembering): "When I was small, water once filled the lower cave. Some elders didn't make it."
- Turn 2, 7.1–9.5s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, urgent, turning on him): "Then we can't wait! Is there higher ground?"
- Turn 3, 10.0–13.8s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking quickly in short lively phrases, every word still clear, decisive, pointing up the cliff): "The upper cave, in the cliff. Stream, take Fire the short way!"
- Pacing: @Roar speaks slowly and calmly, then @Khang answers quickly, then @Roar answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the brown current roaring louder, a branch thudding against rocks, thunder rumbling far upstream, reeds thrashing in the wind. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 15 - Clip 4 (`canh-15/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A jungle stream bank in the Stone Age in late afternoon: the water suddenly brown and fast, branches and leaves racing past, reed beds and big rocks along the bank, the sun still bright overhead while black clouds cover the distant headwater peaks.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium tracking shot leading the young forager as she runs through tall reeds, handheld.
- Shot 2, 4–9s: 50mm close-up of the young man running and panting, handheld follow.
- Shot 3, 9–13s: 35mm medium tracking shot leading the forager across wet rocks, handheld.
- Shot 4, 13–15s: 24mm wide shot of both leaping a gap between big rocks toward the limestone cliff, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Stream sprints into a wall of tall reeds, swinging one arm forward, and is already shouting directions without breaking stride.
- 1–2s (Shot 1): @Stream keeps calling out fast, pushing reed stalks aside, her long hair flying.
- 2–3s (Shot 1): @Stream glances back once over her shoulder as she keeps talking, reed leaves whipping her arms.
- 3–4s (Shot 1): @Stream keeps shouting, pointing ahead toward a line of wet rocks beyond the last reeds.
- 4–5s (CUT to Shot 2): @Stream closes her mouth, eyes forward, as @Khang crashes through the reeds behind her, chest heaving.
- 5–6s (Shot 2): @Khang starts talking between ragged breaths, sweat streaming down his stubbled face as he runs.
- 6–7s (Shot 2): @Khang keeps speaking, half to himself, ducking a whipping reed as his boots slip in the mud.
- 7–8s (Shot 2): @Khang goes on panting the words, his chest harness bouncing against his shirt.
- 8–9s (Shot 2): @Khang finishes and closes his mouth, gulping air, his eyes on her back ahead of him.
- 9–10s (CUT to Shot 3): @Stream hops onto the first wet rock and starts answering steadily, eyes ahead, never looking back.
- 10–11s (Shot 3): @Stream keeps talking calmly as she jumps from rock to rock, arms out for balance.
- 11–12s (Shot 3): @Stream goes on in a firm even voice, her bare feet sure on the slick stone.
- 12–13s (Shot 3): @Stream finishes the last words and closes her mouth, a small set smile on her lips.
- 13–14s (CUT to Shot 4): @Stream leaps a gap between two big rocks, mouth closed, with @Khang landing right behind her.
- 14–15s (Shot 4): Both run on along the rocks toward the distant limestone cliff, mouths closed, the brown stream roaring beside them. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.3s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, commanding, on the run): "This way! Through the reeds, across the rocks, then the cave! Stay close!"
- Turn 2, 4.8–8.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, panting, half to himself): "What if Grandma doesn't believe me? Back home, even the truth gets ignored."
- Turn 3, 9.2–12.8s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, steady, eyes ahead, not looking back): "Here is different. I believe you. Grandmother listens to me."
- Pacing: @Stream speaks quickly, then @Khang answers quickly, then @Stream answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: bare feet and boots pounding through reeds, reed stalks swishing and whipping, ragged breathing, splashes on wet rocks, the stream roaring behind. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 16 - Clip 1 (`canh-16/clip-1.md`)

```markdown
A 15-second live-action film sequence of 3 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Late afternoon inside the large Stone Age clan cave: golden light through the wide arched mouth, the elephant-shaped stalactite, bare rock walls, the clan grilling fish over the hearth, the stream below the entrance now loud and brown.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: a few clan members in bark-cloth tunics and hide wraps sit around the hearth holding fish skewers, freezing mid-bite, in soft focus
Nobody else appears in the shot.

[SHOT LIST — 3 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 24mm wide shot from the hearth toward the golden cave mouth as the young man runs in, slow push-in.
- Shot 2, 5–11s: 85mm close-up of the old clan leader seated by the hearth, locked off.
- Shot 3, 11–15s: 50mm over-the-shoulder shot from behind the old woman onto the young man, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang runs in through the golden cave mouth toward the hearth, sweat-soaked and gasping, and is already shouting toward @Moon.
- 1–2s (Shot 1): @Khang skids to a stop by the fire, still talking fast, as the seated clan members freeze with fish skewers in their hands.
- 2–3s (Shot 1): @Khang points back out of the cave mouth toward the stream as he keeps speaking.
- 3–4s (Shot 1): @Khang keeps talking urgently, hands on his knees for one breath, then straightening.
- 4–5s (Shot 1): @Khang finishes and closes his mouth, chest heaving, sweat dripping from his chin, eyes on @Moon.
- 5–6s (CUT to Shot 2): @Moon stays seated by the hearth, only lifting her head, and starts answering slowly and calmly.
- 6–7s (Shot 2): @Moon keeps speaking in her low husky voice, her eyes steady on @Khang.
- 7–8s (Shot 2): @Moon tilts her chin toward the bright sky beyond the cave mouth as she goes on.
- 8–9s (Shot 2): @Moon talks on slowly, turning a fish skewer over the coals with one hand.
- 9–10s (Shot 2): @Moon's gaze sweeps across the hushed clan around the fire as she keeps speaking.
- 10–11s (Shot 2): @Moon finishes and closes her mouth, eyebrows slightly raised at @Khang, her hands still on the skewer.
- 11–12s (CUT to Shot 3): @Khang steps closer to the fire and starts talking fast, his voice cracking with urgency.
- 12–13s (Shot 3): @Khang keeps speaking, flinging one arm back toward the roaring stream outside.
- 13–14s (Shot 3): @Khang presses a hand flat to his own chest as he goes on.
- 14–15s (Shot 3): @Khang finishes and closes his mouth, breathing hard, while @Moon watches him without a word. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.6s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, breathless, bursting in): "Grandma, we must move to the upper cave now! A flood is coming tonight!"
- Turn 2, 5.1–10.9s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, unmoved, calm and slow): "The sky is clear. It is not the water season. Why frighten the cave?"
- Turn 3, 11.4–14.1s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, desperate, pleading): "The stream's brown and rising! I saw it myself!"
- Pacing: @Khang speaks quickly, then @Moon answers slowly and calmly, then @Khang answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: running boots on the rock floor, ragged breathing, fish sizzling over the hearth, a crackling fire, chatter dying away, the stream roaring louder outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 16 - Clip 2 (`canh-16/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Late afternoon inside the large Stone Age clan cave: golden light through the wide arched mouth, the elephant-shaped stalactite, bare rock walls, the clan grilling fish over the hearth, the stream below the entrance now loud and brown.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- Extra: clan members in bark-cloth tunics and hide wraps murmur around the hearth, mothers pulling small children close, in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the old clan leader seated by the hearth, slow push-in.
- Shot 2, 5–9s: 85mm close-up of the young forager stepping forward into the firelight, handheld.
- Shot 3, 9–13s: 35mm over-the-shoulder shot from behind the forager onto the old woman, locked off.
- Shot 4, 13–15s: 85mm close-up of the old clan leader, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Moon sits by the hearth with the green bamboo ember tube across her knees and is already speaking in a measured voice.
- 1–2s (Shot 1): @Moon keeps talking evenly as, behind her in soft focus, mothers draw small children closer.
- 2–3s (Shot 1): @Moon raises one weathered hand, palm down, as she goes on in the same even voice.
- 3–4s (Shot 1): @Moon keeps speaking, her eyes moving over the children and the old ones by the fire.
- 4–5s (Shot 1): @Moon finishes and closes her mouth, lowering her hand to the bamboo tube.
- 5–6s (CUT to Shot 2): @Stream steps forward into the firelight and starts speaking fast, chin raised.
- 6–7s (Shot 2): @Stream keeps talking quickly, counting off on her fingers as she leans toward @Moon.
- 7–8s (Shot 2): @Stream folds down one more finger as she goes on, the red ochre stripes on her cheeks catching the firelight.
- 8–9s (Shot 2): @Stream finishes and closes her mouth, standing straight, breathing hard, her fists closed at her sides.
- 9–10s (CUT to Shot 3): @Moon looks up at @Stream and starts answering slowly and gravely, her voice dropping low.
- 10–11s (Shot 3): @Moon keeps speaking low, her lined face lit by the fire, while @Stream listens with her mouth closed.
- 11–12s (Shot 3): @Moon turns her head toward the golden cave mouth as she goes on.
- 12–13s (Shot 3): @Moon talks on slowly, her fingers resting on the green bamboo ember tube in her lap.
- 13–14s (CUT to Shot 4): @Moon says the last words looking straight at @Stream, her jaw firm.
- 14–15s (Shot 4): @Moon finishes and closes her mouth, her calm eyes unmoving, as the murmur of the clan dies down. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.5s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking at a natural, even conversational pace, measured, weighing the danger): "Climbing to the upper cave at night, children and elders fall."
- Turn 2, 5.0–8.6s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, quick and fierce, stepping forward): "Grandmother, Fire has never been wrong. Fire, boiled water, the fish trap!"
- Turn 3, 9.1–14.1s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, grave and slow): "If he's wrong, the cave climbs in the dark for a stranger."
- Pacing: @Moon speaks at an even everyday pace, then @Stream answers quickly, then @Moon answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a low murmur running through the clan, a small child whimpering, the fire crackling, fish fat hissing on the coals, the stream roaring outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 16 - Clip 3 (`canh-16/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Late afternoon inside the large Stone Age clan cave: golden light through the wide arched mouth, the elephant-shaped stalactite, bare rock walls, the clan grilling fish over the hearth, the stream below the entrance now loud and brown.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, his left ankle splinted between two straight sticks bound with a red bandana, leaning on a wooden staff, barefoot.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.
- Wardrobe: in this shot @Roar wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: the whole clan in bark-cloth tunics and hide wraps sits around the hearth, falling silent and turning to look, in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 24mm wide shot from the hearth toward the golden cave mouth as the hunter limps in on his staff, locked off.
- Shot 2, 4–8s: 50mm medium shot of the hunter stopping before the seated old woman, slow push-in.
- Shot 3, 8–10s: 85mm close-up of the old clan leader looking up, locked off.
- Shot 4, 10–15s: 35mm over-the-shoulder shot from behind the old woman onto the hunter, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Roar limps in through the golden cave mouth on his wooden staff, the red-bound splint on his left ankle, and is already speaking slowly and loudly.
- 1–2s (Shot 1): @Roar keeps talking as he drags the splinted foot across the rock floor, the hushed clan turning to stare.
- 2–3s (Shot 1): @Roar plants his staff with a thud and goes on, his deep voice filling the cave.
- 3–4s (Shot 1): @Roar keeps speaking slowly, each word heavy, his eyes fixed on @Moon by the hearth.
- 4–5s (CUT to Shot 2): @Roar stops before @Moon and lays one hand on his own boar-hide chest as he speaks.
- 5–6s (Shot 2): @Roar keeps talking, tipping his chin back toward the cave mouth and the jungle beyond it.
- 6–7s (Shot 2): @Roar says the last words firmly, looking down into @Moon's upturned face, his jaw set.
- 7–8s (Shot 2): @Roar finishes and closes his mouth, standing tall on his staff in the silent cave.
- 8–9s (CUT to Shot 3): @Moon looks up at him, her lips parting, and asks almost in a whisper.
- 9–10s (Shot 3): @Moon finishes and closes her mouth, her calm eyes wide for once.
- 10–11s (CUT to Shot 4): @Roar shakes his head once and starts answering fast and forceful, leaning on his staff.
- 11–12s (Shot 4): @Roar keeps talking hard, pointing his staff out toward the roaring brown stream.
- 12–13s (Shot 4): @Roar leans toward @Moon as he goes on, his boar-tusk necklace swinging.
- 13–14s (Shot 4): @Roar calls out the last words with force, one big hand sweeping upward toward the cliff.
- 14–15s (Shot 4): @Roar finishes and closes his mouth, breathing hard, waiting for @Moon's answer in the silent cave. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.4s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and loud, every word a vow): "He is no stranger. He saved me from the pit, with the tiger circling. I trust him."
- Turn 2, 7.9–9.8s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking at a natural, even conversational pace, stunned, almost a whisper): "Roar? You hated him most."
- Turn 3, 10.3–14.1s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking quickly in short lively phrases, every word still clear, forceful, urging her up): "Hate was yesterday. Muddy water is tonight. Grandmother, take the cave up!"
- Pacing: @Roar speaks slowly and calmly, then @Moon answers at an even everyday pace, then @Roar answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a wooden staff thudding on rock, a dragging bare foot, the fire crackling in a sudden hush, the stream roaring outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 16 - Clip 4 (`canh-16/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Late afternoon inside the large Stone Age clan cave: golden light through the wide arched mouth, the elephant-shaped stalactite, bare rock walls, the clan grilling fish over the hearth, the stream below the entrance now loud and brown.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: clan members in bark-cloth tunics and hide wraps gather bundles while small children are joined to adults by loose vine safety cords, in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium shot of the old clan leader rising by the hearth and holding out the bamboo ember tube, slow push-in.
- Shot 2, 5–9s: 50mm close-up of the young man knotting a vine cord, handheld.
- Shot 3, 9–12s: 50mm over-the-shoulder shot from behind the young man onto the old woman, locked off.
- Shot 4, 12–15s: 85mm close-up of the old clan leader, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Moon rises from the hearth, straight-backed, and is already speaking in a firm voice that carries across the cave.
- 1–2s (Shot 1): @Moon keeps talking as the clan members around the fire scramble to their feet in soft focus.
- 2–3s (Shot 1): @Moon holds out the green bamboo ember tube as she goes on, and a small child's hands reach in from the frame edge to take it.
- 3–4s (Shot 1): @Moon keeps speaking, her hand lingering on the tube a moment before she lets go.
- 4–5s (Shot 1): @Moon finishes and closes her mouth, watching the small hands carry the tube away.
- 5–6s (CUT to Shot 2): @Khang kneels beside a small child, ties a loose vine safety cord around the child's waist and starts talking fast over his shoulder.
- 6–7s (Shot 2): @Khang keeps calling out quickly as he ties the other end to the wrist of a woman beside the child.
- 7–8s (Shot 2): @Khang keeps speaking, tugging the knot twice to test it, eyes sweeping the cave.
- 8–9s (Shot 2): @Khang finishes and closes his mouth, rising to his feet, breathing fast.
- 9–10s (CUT to Shot 3): @Moon turns, looks straight at @Khang and starts speaking slowly and evenly.
- 10–11s (Shot 3): @Moon keeps talking in a low steady voice, while @Khang stands still with his mouth closed.
- 11–12s (Shot 3): @Moon takes one step toward him as she goes on, her hide cloak swaying.
- 12–13s (CUT to Shot 4): @Moon says the last words slowly, her calm eyes never leaving his face.
- 13–14s (Shot 4): @Moon finishes and closes her mouth, the red ochre dot steady on her forehead.
- 14–15s (Shot 4): @Moon holds his gaze in silence, mouth closed, as the golden light fades on the cave wall behind her. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking at a natural, even conversational pace, decisive, her voice carrying): "Everyone! Children first. Snail, carry the fire tube. Don't let it die."
- Turn 2, 5.4–8.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, quick orders, hands busy): "Tie each child to an adult! Stream and I go last!"
- Turn 3, 9.2–13.4s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and even, a warning): "Fire-Maker. If no water comes, you leave at sunrise."
- Pacing: @Moon speaks at an even everyday pace, then @Khang answers quickly, then @Moon answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the clan stirring, hide bundles rustling, vine cords pulled tight, children's quick footsteps, the hearth crackling, the stream roaring outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 17 - Clip 1 (`canh-17/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night during a flash flood in the Stone Age: a narrow ledge-cave high on a limestone cliff lit by flickering torches, heavy rain, and far below a roaring brown flood surging over the stream banks toward the mouth of the lower cave.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, empty-handed with no bamboo tube, barefoot.
- Wardrobe: in this shot @Moon wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: the clan in bark-cloth tunics and hide wraps huddles under the rock overhang by torchlight, small children sitting in a row, in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium tracking shot of the young forager moving along a row of huddled children under the ledge, handheld follow.
- Shot 2, 4–8s: 85mm close-up of the old clan leader staring at an empty hollow in the rock, locked off.
- Shot 3, 8–12s: 50mm over-the-shoulder shot from behind the old woman onto the forager, slow push-in.
- Shot 4, 12–15s: 85mm close-up of the forager in the torchlight, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Stream moves fast along a row of huddled children under the torchlit rock overhang, touching each small shoulder, and is already speaking breathlessly.
- 1–2s (Shot 1): @Stream keeps talking fast, spinning to search the faces packed under the ledge, rain blowing in behind her.
- 2–3s (Shot 1): @Stream touches the last small shoulder and her hand stops in midair as she keeps calling out.
- 3–4s (Shot 1): @Stream finishes and closes her mouth, her face pale in the torchlight, chest heaving.
- 4–5s (CUT to Shot 2): @Moon stares at an empty hollow in the rock beside her and starts speaking fast, her voice shaking.
- 5–6s (Shot 2): @Moon keeps talking quickly, touching the bare stone where the green bamboo ember tube lay.
- 6–7s (Shot 2): @Moon's weathered fingers tremble on the cold wet rock as she goes on.
- 7–8s (Shot 2): @Moon finishes and closes her mouth, lips pressed tight, eyes on the empty hollow.
- 8–9s (CUT to Shot 3): @Stream turns slowly toward the edge of the ledge and starts speaking low and slow, each word heavy.
- 9–10s (Shot 3): @Stream keeps talking, staring down past the ledge into the dark rain and the roaring flood below.
- 10–11s (Shot 3): @Stream's hand closes around the snail-shell necklace at her chest as she goes on speaking.
- 11–12s (Shot 3): @Stream keeps speaking slowly, her lower lip trembling between the words, rain on her lashes.
- 12–13s (CUT to Shot 4): @Stream swallows and says the last words almost to herself, her eyes glistening in the torchlight.
- 13–14s (Shot 4): @Stream keeps speaking in a low voice, rain beading on the red ochre stripes on her cheeks.
- 14–15s (Shot 4): @Stream finishes and closes her mouth, breathing shakily, her eyes fixed on the darkness below. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.4s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, breathless and frantic): "Grandmother, one is missing! Where's Snail? Has anyone seen Snail?"
- Turn 2, 3.9–7.7s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking quickly in short lively phrases, every word still clear, quick, her voice shaking): "The fire tube is gone too. He put it down to climb."
- Turn 3, 8.2–14.2s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and numb, the truth sinking in): "He went back down for the fire. Since the night it died, he blames himself."
- Pacing: @Stream speaks quickly, then @Moon answers quickly, then @Stream answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: heavy rain hammering the rock, torches sputtering and hissing in the wind, the flood roaring far below, a baby whimpering, thunder rolling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 17 - Clip 2 (`canh-17/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; it intercuts the two places or times named in the shot list, each shot keeping its own place and light, with sound continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night in the flooding lower Stone Age cave and the cliff face above it: brown water pouring in through the wide mouth and rising around stone pillars, the elephant-shaped stalactite, rain lashing the cliff where a vine rope hangs down from torchlight high above.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm close-up of the boy standing on a ledge of a stone pillar in the dark flooded cave, red ember glow on his face, slow push-in.
- Shot 2, 5–9s: 35mm medium shot of the young man roping down the rain-lashed cliff, his headlamp beam cutting the rain, handheld.
- Shot 3, 9–13s: 50mm close-up of the boy clinging to the stone pillar above the swirling water, handheld.
- Shot 4, 13–15s: 24mm wide shot of the rain-lashed cliff and the flooded cave mouth at its foot as a headlamp beam descends, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Each shot keeps the lighting of its own place and time; faces, wardrobe and props stay consistent; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Snail stands on a dry ledge of a stone pillar in the dark flooded cave, hugging the bamboo tube, and is already speaking in quick panting gasps.
- 1–2s (Shot 1): @Snail peeks into the open end of the tube at the red glowing embers, still talking fast, his eyes shining.
- 2–3s (Shot 1): @Snail presses the tube against his small chest as he keeps talking to it, brown water swirling around the pillar below his feet.
- 3–4s (Shot 1): @Snail keeps speaking breathlessly to the embers, a shaky grin on his round face, his head and shoulders dry.
- 4–5s (Shot 1): @Snail finishes and closes his mouth and wraps one arm around the stone pillar, brown water lapping at the ledge below his bare feet.
- 5–6s (CUT to Shot 2): On the cliff above, @Khang hangs on the braided vine rope against the wet rock, his headlamp beam cutting down through the rain, and starts shouting downward.
- 6–7s (Shot 2): @Khang keeps shouting as he walks his boots down the wet rock, the rope wrapped around his waist and over one shoulder.
- 7–8s (Shot 2): @Khang keeps calling out, rain streaming down his stubbled face, his eyes searching the dark cave mouth below.
- 8–9s (Shot 2): @Khang lowers himself another stride down the cliff, still shouting through the rain.
- 9–10s (CUT to Shot 3): Down in the flooded cave, @Snail jerks his head up toward the cave mouth and starts crying out, tears on his cheeks.
- 10–11s (Shot 3): @Snail keeps shouting, his voice cracking, hugging the tube and the pillar together.
- 11–12s (Shot 3): @Snail calls out again, glancing at the brown water swirling just below the ledge, his head and shoulders dry.
- 12–13s (Shot 3): @Snail finishes and closes his mouth, his small chest hitching, his eyes on the cave mouth.
- 13–14s (CUT to Shot 4): On the cliff, the white headlamp beam swings toward the flooded cave mouth far below as @Khang slides faster down the rope, mouth closed.
- 14–15s (Shot 4): @Khang's small lit figure descends the rain-lashed cliff toward the dark cave mouth, where a faint red ember glow flickers inside, mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.3s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, panting, half laughing with relief): "Found it! Still glowing! Little fire, this time I won't let you die!"
- Turn 2, 4.8–9.3s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, shouting down through the rain): "Snail! Stay there, hold the stone pillar! I'm coming down! When I whistle, shout back!"
- Turn 3, 9.8–12.5s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, crying out, his voice cracking): "Fire! The water's up to my legs! I'm here!"
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.5s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: brown water gushing into the cave and swirling around stone pillars, rain lashing the cliff, a vine rope creaking, boots scraping on wet rock, embers hissing softly inside a bamboo tube. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 17 - Clip 3 (`canh-17/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night during a flash flood in the Stone Age: a narrow ledge-cave high on a limestone cliff lit by flickering torches, heavy rain, and far below a roaring brown flood surging over the stream banks toward the mouth of the lower cave.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, his left ankle splinted between two straight sticks bound with a red bandana, leaning on a wooden staff, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- Wardrobe: in this shot @Roar and @Khang wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium shot of the hunter sitting braced against a rock at the ledge edge with the rope wrapped around his back, handheld.
- Shot 2, 5–9s: 50mm high-angle close-up of the young man hanging on the rope below, looking up into the rain, handheld.
- Shot 3, 9–13s: 50mm low-angle medium shot of the hunter at the ledge edge in the rain and torchlight, slow push-in.
- Shot 4, 13–15s: 24mm wide shot down the wet cliff from the ledge along the taut rope, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Roar sits braced against a rock at the edge of the torchlit ledge, the vine rope wrapped around his back, and is already shouting down into the rain.
- 1–2s (Shot 1): @Roar keeps shouting, both fists locked on the rope, his splinted leg stretched straight out in front of him.
- 2–3s (Shot 1): @Roar leans back hard against the rock as the rope jerks taut, still shouting.
- 3–4s (Shot 1): @Roar keeps shouting down, rain running off his heavy brows and his boar-tusk necklace.
- 4–5s (Shot 1): @Roar finishes and closes his mouth, teeth gritted, holding the rope tight against his back.
- 5–6s (CUT to Shot 2): Below the ledge, @Khang hangs on the taut rope against the wet cliff, tips his head back and starts shouting up, firm and fast.
- 6–7s (Shot 2): @Khang keeps shouting up, one hand flat against the rock, his headlamp beam glaring into the rain.
- 7–8s (Shot 2): @Khang points up at the ledge as he goes on shouting, water streaming off his chin.
- 8–9s (Shot 2): @Khang finishes and closes his mouth, then walks his boots another step down the cliff.
- 9–10s (CUT to Shot 3): @Roar plants his good heel against a ridge of rock, leans back and starts shouting down, deep and booming.
- 10–11s (Shot 3): @Roar keeps shouting, the rope sliding slowly through his fists as he pays it out.
- 11–12s (Shot 3): @Roar's jaw clenches as he goes on, rain lashing across the torchlight.
- 12–13s (Shot 3): @Roar finishes the last words and closes his mouth, breathing hard, his eyes locked on the dark below.
- 13–14s (CUT to Shot 4): Seen from the ledge, the taut rope runs down the wet cliff to @Khang's small figure and white headlamp beam as he descends, mouth closed.
- 14–15s (Shot 4): @Khang's headlamp drops steadily toward the brown flood churning at the foot of the cliff while the rope creaks. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.5s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking quickly in short lively phrases, every word still clear, shouting down over the rain): "The rope only reaches the big rock! Past that, I can't hold you!"
- Turn 2, 5.0–8.6s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, shouting up, firm and fast): "Enough! Hold tight, back against the rock. Don't stand on that ankle!"
- Turn 3, 9.1–12.9s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking at a natural, even conversational pace, a booming growl): "Fire! Bring the boy back. And bring yourself back too!"
- Pacing: @Roar speaks quickly, then @Khang answers quickly, then @Roar answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: rain hammering the ledge, the vine rope creaking and rasping over rock, torches hissing, the flood roaring below, a long roll of thunder. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 17 - Clip 4 (`canh-17/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night in the flooding lower Stone Age cave and the cliff face above it: brown water pouring in through the wide mouth and rising around stone pillars, the elephant-shaped stalactite, rain lashing the cliff where a vine rope hangs down from torchlight high above.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the young man wading into the flooded cave as his headlamp beam finds the boy on the pillar, handheld follow.
- Shot 2, 4–8s: 50mm close-up of the boy on the young man's shoulders hugging the bamboo tube, handheld.
- Shot 3, 8–12s: 24mm wide shot leading the young man as he wades out of the cave mouth with the boy on his shoulders toward a huge boulder, handheld.
- Shot 4, 12–15s: 50mm low-angle medium shot of both on top of the huge boulder as a surge of brown water rolls past below, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang wades through brown water up to his thighs into the dark flooded cave, his headlamp beam sweeping, and is already shouting toward a stone pillar.
- 1–2s (Shot 1): @Khang keeps shouting as his beam lands on @Snail standing on a dry pillar ledge above the swirling water, hugging the bamboo tube.
- 2–3s (Shot 1): @Khang reaches the pillar and holds up both arms to @Snail, still shouting fast.
- 3–4s (Shot 1): @Khang finishes and closes his mouth, lifts @Snail off the ledge and swings him up onto his shoulders, the water only at his own thighs.
- 4–5s (CUT to Shot 2): @Snail sits high on @Khang's shoulders, one arm hugging the bamboo tube, and starts crying out stubbornly, tears streaming.
- 5–6s (Shot 2): @Snail keeps talking through his tears, refusing to let go of the tube, his head and shoulders dry high above the water.
- 6–7s (Shot 2): @Snail clutches the tube tighter against his chest as he keeps crying out, the red ember glow on his chin.
- 7–8s (Shot 2): @Snail finishes and closes his mouth, his small chest hitching, one hand holding on to @Khang's hair.
- 8–9s (CUT to Shot 3): @Khang turns toward the cave mouth and starts answering fast, half laughing, his eyes on a huge boulder outside.
- 9–10s (Shot 3): @Khang keeps shouting as he wades out through the cave mouth, the brown water at his thighs, @Snail held tight on his shoulders.
- 10–11s (Shot 3): @Khang keeps talking fast, nodding toward the huge boulder at the foot of the cliff.
- 11–12s (Shot 3): @Khang finishes and closes his mouth, pushing through the current toward the boulder.
- 12–13s (CUT to Shot 4): @Khang hauls himself up onto the wet boulder with @Snail on his shoulders, mouth closed, his boots scrabbling on the rock.
- 13–14s (Shot 4): @Khang sets @Snail down on the flat top of the boulder and crouches over him, both mouths closed.
- 14–15s (Shot 4): A surge of muddy brown water rolls past the boulder and into the cave mouth below them while @Khang and @Snail hold still on the dry top, mouths closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, urgent, wading in): "Snail! Your hand! Arms around my neck, don't let go!"
- Turn 2, 3.9–7.8s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, crying, clinging on stubbornly): "The fire tube! I'm not letting go! Grandmother said don't let it die!"
- Turn 3, 8.3–11.6s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, fast and firm, half laughing): "Fine, keep it! Onto that rock, quick, here comes the water!"
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 11.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: brown water churning and roaring through the cave mouth, boots sloshing through deep water, rain lashing outside, a rising rumble as a surge of muddy water rolls in. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 18 - Clip 1 (`canh-18/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night at the foot of the limestone cliff during the flood: the flat top of a huge boulder just above churning brown water, rain lashing, torchlight from a ledge-cave high above, a vine rope hanging down the wet rock face.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 24mm wide shot of the huge boulder in the churning brown flood at the foot of the cliff with the young man standing on top, slow push-in.
- Shot 2, 3–7s: 50mm close-up of the boy huddled on the boulder top hugging the bamboo tube, locked off.
- Shot 3, 7–11s: 35mm medium two-shot of the pair on the boulder top, handheld.
- Shot 4, 11–15s: 85mm close-up of the young man looking up at the torches, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang stands on top of the huge boulder in the churning brown flood, one arm around @Snail, and is already shouting up the dark cliff at full voice.
- 1–2s (Shot 1): @Khang keeps shouting upward, cupping his free hand beside his mouth, rain lashing across his headlamp beam.
- 2–3s (Shot 1): @Khang finishes and closes his mouth, breathing hard, staring up at the torches high on the ledge.
- 3–4s (CUT to Shot 2): @Snail huddles against @Khang's side on the flat boulder top, hugging the bamboo tube, and starts speaking in a small shaking voice.
- 4–5s (Shot 2): @Snail keeps talking slowly, his eyes on the brown water churning below the edge of the boulder, his head and shoulders dry.
- 5–6s (Shot 2): @Snail's lower lip trembles as he goes on, rain dripping from the tuft of hair on his head.
- 6–7s (Shot 2): @Snail tightens his arms around the tube as he asks the last words.
- 7–8s (CUT to Shot 3): @Snail finishes and closes his mouth, looking up at @Khang with big wet eyes.
- 8–9s (Shot 3): @Khang crouches down to @Snail's level and starts answering gently, one hand flat on the rough rock.
- 9–10s (Shot 3): @Khang keeps speaking softly, patting the huge boulder under them twice with his open hand.
- 10–11s (Shot 3): @Khang turns his head and his headlamp beam up toward the cliff as he goes on talking.
- 11–12s (CUT to Shot 4): @Khang keeps talking calmly, pointing up at the flickering torches on the ledge high above.
- 12–13s (Shot 4): @Khang says the last words with a steady half smile, rain running down his stubbled face.
- 13–14s (Shot 4): @Khang finishes and closes his mouth, still looking up at the torches.
- 14–15s (Shot 4): @Khang lifts the whistle to his lips and gives three short sharp blows toward the ledge, his eyes fixed on the torchlight. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–2.8s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, bellowing up the cliff): "Everyone! Down here! Two of us, both alive!"
- Turn 2, 3.3–7.3s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking slowly and softly, unhurried, with a short natural pause between phrases, small and shaking): "Fire... the water's higher. Will the rock get swept away?"
- Turn 3, 7.8–13.6s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, gentle and coaxing, steady): "This rock is huge, the water can't move it. See the torches? Stream's throwing a rope."
- Pacing: @Khang speaks quickly, then @Snail answers slowly and calmly, then @Khang answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: churning brown floodwater roaring around the boulder, rain lashing stone, torches hissing high above, distant thunder, three short shrill whistle blows at the very end. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 18 - Clip 2 (`canh-18/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night at the foot of the limestone cliff during the flood: the flat top of a huge boulder just above churning brown water, rain lashing, torchlight from a ledge-cave high above, a vine rope hanging down the wet rock face.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: clan members in bark-cloth tunics and hide wraps line the torchlit ledge behind her, hauling on the rope in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the young forager at the edge of the torchlit ledge swinging a stone-weighted rope, handheld.
- Shot 2, 4–8s: 50mm close-up of the young man on the boulder catching the rope, handheld.
- Shot 3, 8–12s: 35mm low-angle medium shot of the forager hauling the rope with the clan behind her, slow push-in.
- Shot 4, 12–15s: 24mm wide shot from the ledge down the wet cliff as a small child rises on the rope toward the torches, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Stream stands at the edge of the torchlit ledge swinging a vine rope with a stone tied to its end, and is already shouting down into the rain.
- 1–2s (Shot 1): @Stream keeps shouting as she tosses the weighted rope out over the edge, rain streaming down her face.
- 2–3s (Shot 1): @Stream leans out to watch it fall, still shouting down, one hand braced on the wet rock.
- 3–4s (Shot 1): @Stream finishes and closes her mouth, holding the upper end of the rope, her eyes locked on the boulder below.
- 4–5s (CUT to Shot 2): Down on the boulder, @Khang catches the weighted end of the rope in both hands and starts shouting up fast.
- 5–6s (Shot 2): @Khang keeps talking quickly while his hands loop the rope as a harness around a small back in soft focus beside him.
- 6–7s (Shot 2): @Khang keeps speaking fast as his fingers form a bowline knot, his eyes flicking up to the ledge.
- 7–8s (Shot 2): @Khang finishes and closes his mouth, tugs the knot twice and raises a thumb to the ledge.
- 8–9s (CUT to Shot 3): @Stream, rope in both hands at the ledge edge with the clan lined up behind her, starts shouting down fast.
- 9–10s (Shot 3): @Stream keeps shouting, leaning her whole weight back on the rope as the hands behind her haul.
- 10–11s (Shot 3): @Stream calls out the count, heaving on the rope with each word, wet hair stuck to her cheeks.
- 11–12s (Shot 3): @Stream finishes and closes her mouth, hauling hand over hand, teeth clenched.
- 12–13s (CUT to Shot 4): Looking down from the ledge, a small child with his back to camera rises up the wet cliff on the rope, hugging a glowing bamboo tube.
- 13–14s (Shot 4): @Stream hauls hand over hand at the frame edge, mouth closed, as the small child comes closer to the torchlight.
- 14–15s (Shot 4): Far below on the boulder, @Khang's headlamp beam follows the rising rope, his mouth closed. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.4s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, shouting down from the ledge): "Fire! The rope has a stone! Hands up and catch!"
- Turn 2, 3.9–7.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, fast and focused, hands working): "Got it! Tying Snail first. Bowline, it won't slip, don't worry!"
- Turn 3, 7.7–11.6s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, fierce, leading the pull): "Snail, hug the fire tube! The whole cave is pulling! One, two, pull!"
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 11.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: rain hammering the ledge, a stone-weighted rope whirring through the air and thudding onto the boulder, the vine rope creaking, the clan grunting as they haul, the flood roaring below. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow or drawn-out delivery, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 18 - Clip 3 (`canh-18/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night at the foot of the limestone cliff during the flood: the flat top of a huge boulder just above churning brown water, rain lashing, torchlight from a ledge-cave high above, a vine rope hanging down the wet rock face.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm close-up of the young man on the boulder as his chest-harness buckle pops open, handheld.
- Shot 2, 4–8s: 35mm low-angle medium shot of the young forager at the ledge edge shouting down with the rope in her hands, handheld.
- Shot 3, 8–13s: 85mm close-up of the young man holding the small camera above the water, slow push-in.
- Shot 4, 13–15s: 24mm wide shot of the small camera drifting away on the brown flood into the rain with the boulder behind, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang reaches up for the dangling rope on top of the boulder as the buckle of his chest harness pops open, and is already shouting, eyes wide.
- 1–2s (Shot 1): @Khang keeps shouting as the small chest camera slides off his harness, and his free hand closes around it just above the churning water.
- 2–3s (Shot 1): @Khang holds the rope in one fist and the little camera in the other, its red light blinking, still shouting at it.
- 3–4s (Shot 1): @Khang finishes and closes his mouth, frozen between his two hands, breathing fast.
- 4–5s (CUT to Shot 2): High on the torchlit ledge, @Stream leans over the edge with the upper end of the rope in her hands and starts shouting down fiercely.
- 5–6s (Shot 2): @Stream keeps shouting, pointing hard at the boulder below, rain streaming down her face.
- 6–7s (Shot 2): @Stream keeps shouting down, wrapping the rope around her own forearm to hold it steady.
- 7–8s (Shot 2): @Stream finishes and closes her mouth, braced at the ledge edge, staring down.
- 8–9s (CUT to Shot 3): @Khang looks at the little camera in his hand, rain beading on its blinking red light, and starts speaking slowly and quietly.
- 9–10s (Shot 3): @Khang keeps talking low, his thumb brushing once over the wet camera body, his jaw working.
- 10–11s (Shot 3): @Khang keeps speaking softly and opens his fingers; the camera drops into the brown water below the boulder.
- 11–12s (Shot 3): @Khang goes on quietly as he takes the rope in both hands, his eyes following the camera on the water.
- 12–13s (Shot 3): @Khang says the last words in a low steady voice, both fists tight on the rope.
- 13–14s (CUT to Shot 4): The small camera drifts away on the churning brown flood into the rain, its red light blinking, as @Khang closes his mouth on the boulder behind.
- 14–15s (Shot 4): The blinking red light shrinks into the dark rain while @Khang holds the rope with both hands, mouth closed, watching it go. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, frantic, clutching at it): "The strap snapped! No... all seven days are in there!"
- Turn 2, 3.9–7.5s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, screaming down, fierce): "Fire! Let the seeing stone go! Hold the rope with both hands!"
- Turn 3, 8.0–13.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and quiet, letting go): "Go, then. Three million viewers aren't worth one boy holding a fire tube."
- Pacing: @Khang speaks quickly, then @Stream answers quickly, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a sharp plastic click as a buckle pops open, rain hammering, the flood roaring around the boulder, a small splash, the vine rope creaking taut. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 18 - Clip 4 (`canh-18/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Night during a flash flood in the Stone Age: a narrow ledge-cave high on a limestone cliff lit by flickering torches, heavy rain, and far below a roaring brown flood surging over the stream banks toward the mouth of the lower cave.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, empty-handed with no bamboo tube, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera.
- Wardrobe: in this shot @Moon and @Khang wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
- Extra: the clan in bark-cloth tunics and hide wraps crowds the torchlit ledge behind them in soft focus, shoulders sagging as they breathe out
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the old clan leader at the edge of the torchlit ledge looking down at the flood, locked off.
- Shot 2, 4–7s: 50mm high-angle close-up of the young man lying on his back on the wet rock, handheld.
- Shot 3, 7–11s: 35mm over-the-shoulder shot from behind the young man onto the old woman kneeling beside him, slow push-in.
- Shot 4, 11–15s: 85mm close-up of the old clan leader in the torch and ember light, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Moon stands at the edge of the torchlit ledge staring down at the roaring brown flood and is already speaking, hushed, her eyes fixed on the water.
- 1–2s (Shot 1): @Moon keeps speaking quietly as the brown water churns over the mouth of the lower cave far below.
- 2–3s (Shot 1): @Moon's hand tightens on her hide cloak as she says the last words.
- 3–4s (Shot 1): @Moon finishes and closes her mouth, then turns from the edge toward the rope.
- 4–5s (CUT to Shot 2): @Khang lies flat on his back on the wet rock of the ledge, soaked and muddy, his chest harness empty, and starts asking between gasps.
- 5–6s (Shot 2): @Khang keeps talking breathlessly, lifting his head to look around the torchlit ledge.
- 6–7s (Shot 2): @Khang pushes himself up on one elbow as he finishes his question, rain running off his face.
- 7–8s (CUT to Shot 3): @Khang closes his mouth, chest heaving, as @Moon kneels beside him and, behind her, small hands open a bamboo tube glowing with red embers.
- 8–9s (Shot 3): @Moon starts speaking slowly and warmly, looking into @Khang's face, the ember glow on her cheek.
- 9–10s (Shot 3): @Moon keeps talking in her low husky voice, nodding toward the clan crowding the ledge behind her.
- 10–11s (Shot 3): @Moon lays one weathered hand on @Khang's empty chest harness as she goes on.
- 11–12s (CUT to Shot 4): @Moon keeps speaking slowly, her calm eyes glistening in the torchlight above him.
- 12–13s (Shot 4): @Moon says the last words with weight, her hand still resting on his chest.
- 13–14s (Shot 4): @Moon keeps speaking slowly to the end, the red ochre dot on her forehead lit by the embers.
- 14–15s (Shot 4): @Moon finishes and closes her mouth, holding his gaze in silence as rain drips from the rock overhead. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.4s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking at a natural, even conversational pace, hushed, eyes on the water): "The water came. The lower cave is flooded."
- Turn 2, 3.9–7.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, out of breath, lying on the rock): "Is everyone here, Grandma? Did Snail keep the fire?"
- Turn 3, 7.7–13.9s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and warm, every word weighed): "All here. The fire lives, the people live. You gave your stone for our fire."
- Pacing: @Moon speaks at an even everyday pace, then @Khang answers at an even everyday pace, then @Moon answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: rain easing on the rock ledge, torches hissing, the flood roaring far below, heavy ragged breathing, a bamboo cap popping off, embers crackling softly. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 19 - Clip 1 (`canh-19/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Clear golden dawn after the flood, seen from a ledge-cave high on the limestone cliff: the valley below covered in mud and fallen trees, the stream back in its bed, mist rising off the jungle.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: a dozen clan members in bark-cloth tunics and hide wraps stand along the ledge looking down at the valley, seen from behind in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 24mm wide shot along the cliff ledge over the mud-covered valley, the old woman in the foreground turning to camera, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the survivalist in the low dawn sun, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the survivalist onto the old woman, locked off.
- Shot 4, 13–15s: 35mm medium two-shot in profile at the ledge edge, the misty valley glowing below, slow drift.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): On the sunlit ledge above the mud-covered valley, @Moon turns from the edge toward @Khang, the bamboo ember tube in her arms, and is already speaking slowly.
- 1–2s (Shot 1): @Moon keeps speaking, each word weighed, the dawn sun lighting the deep lines of her face and the red dot on her forehead.
- 2–3s (Shot 1): @Moon lifts her chin toward the drowned valley behind her as she goes on, while @Khang listens with his mouth closed.
- 3–4s (Shot 1): @Moon keeps talking slowly, her calm eyes resting on the empty chest harness strapped over his torn shirt.
- 4–5s (Shot 1): @Moon finishes and closes her mouth; @Khang shakes his head with a tired smile, draws a breath and starts answering.
- 5–6s (CUT to Shot 2): @Khang keeps talking warmly, his stubble grown into a short dark beard, counting names on the fingers of one blistered hand.
- 6–7s (Shot 2): @Khang keeps speaking, tipping his head toward the clan standing along the ledge behind him.
- 7–8s (Shot 2): @Khang goes on, his voice catching slightly, his eyes shining in the low gold light.
- 8–9s (Shot 2): @Khang keeps talking, pressing one blistered palm flat against his chest over the empty harness.
- 9–10s (Shot 2): @Khang finishes and closes his mouth, looking down at his muddy boots, while @Moon draws a breath beside him.
- 10–11s (CUT to Shot 3): @Moon steps closer, lays one small wrinkled hand on his forearm and answers, her low voice softening.
- 11–12s (Shot 3): @Moon keeps speaking, holding his gaze, the bamboo ember tube tucked against her hide cloak.
- 12–13s (Shot 3): @Moon keeps going, nodding once toward the clan along the ledge as she says the last words.
- 13–14s (CUT to Shot 4): @Moon finishes and closes her mouth, a rare small smile creasing her lined face.
- 14–15s (Shot 4): @Khang bows his head to her, mouth closed, while mist curls off the drowned valley below them in the dawn sun. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.2s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and grave, like a law spoken aloud): "Seventh sun. You lived, and you saved the cave."
- Turn 2, 4.7–9.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, humble, shaking his head, warm): "Not alone. Stream fed me, Roar held the rope, Snail kept the fire."
- Turn 3, 9.9–13.7s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking at a natural, even conversational pace, warm and final, a rare small smile): "Then you are of the cave. We never walk alone."
- Pacing: @Moon speaks slowly and calmly, then @Khang answers at an even everyday pace, then @Moon answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: dawn birdsong across the valley, water dripping off the cliff, a soft wind on the ledge, the stream trickling far below, bare feet shifting on stone. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 19 - Clip 2 (`canh-19/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
The lower Stone Age cave the morning after the flood: wet mud on the floor, the elephant-shaped stalactite, the bare damp rock wall in soft daylight, a flat grinding stone with red-ochre powder and a hollow reed tube.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium shot of the old woman kneeling at the flat grinding stone beside the bare wet wall, slow push-in.
- Shot 2, 5–9s: 85mm close-up of the young forager holding a hollow reed, locked off.
- Shot 3, 9–12s: 50mm over-the-shoulder shot from behind the young forager onto the old woman, locked off.
- Shot 4, 12–15s: 35mm medium two-shot of both women turning to the bare wall, the elephant-shaped stalactite behind, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the damp lower cave, @Moon kneels at a flat grinding stone, rolling a pebble through red-ochre powder, and is already speaking in a steady voice.
- 1–2s (Shot 1): @Moon keeps speaking as she tips water from a large snail shell onto the powder, turning it into a red paste.
- 2–3s (Shot 1): @Moon keeps going, lifting her red-stained fingers toward the bare wet wall beside her.
- 3–4s (Shot 1): @Moon keeps talking, her eyes moving slowly across the empty rock, while @Stream watches with her mouth closed.
- 4–5s (Shot 1): @Moon finishes and closes her mouth, wiping her red fingertips on the edge of the grinding stone.
- 5–6s (CUT to Shot 2): @Stream steps in holding a hollow reed tube, tilts her head and starts speaking eagerly.
- 6–7s (Shot 2): @Stream keeps talking, turning the hollow reed between her fingers and peering through it at the daylight.
- 7–8s (Shot 2): @Stream keeps speaking, glancing from the red paste to the bare wall with bright eyes.
- 8–9s (Shot 2): @Stream asks her last question with her eyebrows raised, then closes her mouth and waits.
- 9–10s (CUT to Shot 3): @Moon looks up at her and answers slowly, setting the pebble down on the grinding stone.
- 10–11s (Shot 3): @Moon keeps speaking, holding up one wrinkled hand and spreading the fingers wide.
- 11–12s (Shot 3): @Moon keeps going slowly, pointing one red-stained finger at the very middle of the bare wall.
- 12–13s (CUT to Shot 4): @Moon keeps talking as both women turn their faces toward the empty rock in the soft daylight.
- 13–14s (Shot 4): @Moon finishes and closes her mouth, nodding once, while @Stream breathes in and grips the reed tighter.
- 14–15s (Shot 4): @Stream carries a small shell cup of red paste toward the wall, mouth closed, while @Moon watches in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking at a natural, even conversational pace, steady, announcing a new law): "From today, whoever saves the cave leaves a hand on the wall."
- Turn 2, 5.4–9.0s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, curious and eager, turning the reed): "Red earth and water, blown through a reed. Fire first?"
- Turn 3, 9.5–13.7s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and certain, nodding): "Yes. His hand is biggest. Put it in the middle."
- Pacing: @Moon speaks at an even everyday pace, then @Stream answers at an even everyday pace, then @Moon answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: stone grinding on stone, water dripping from the cave roof, runoff trickling across the mud floor, birdsong outside the bright mouth. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 19 - Clip 3 (`canh-19/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
The lower Stone Age cave the morning after the flood: wet mud on the floor, the elephant-shaped stalactite, the bare damp rock wall in soft daylight, a flat grinding stone with red-ochre powder and a hollow reed tube.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium two-shot at the bare wall, his palm flat in the middle of the rock as she puffs red mist through a reed, slow push-in.
- Shot 2, 5–9s: 85mm close-up of the young forager lowering the reed, locked off.
- Shot 3, 9–12s: 50mm over-the-shoulder shot from behind the young forager onto the survivalist and the fresh red hand, locked off.
- Shot 4, 12–15s: 35mm medium two-shot at the wall, the fresh red hand between them, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): At the bare wall, @Khang holds his palm flat in the middle of the rock while @Stream puffs red mist around his fingers, and he is already whispering.
- 1–2s (Shot 1): @Khang keeps whispering, staring at the red outline forming around his spread fingers on the wet stone.
- 2–3s (Shot 1): @Khang keeps whispering, his breath shaking, while @Stream moves the reed slowly along his thumb in soft red puffs.
- 3–4s (Shot 1): @Khang goes on in a hushed voice, his eyes wide and wet above his short beard, never leaving his own hand.
- 4–5s (Shot 1): @Khang finishes, closes his mouth and slowly peels his palm off the rock, leaving a bright red hand outline, as @Stream lowers the reed.
- 5–6s (CUT to Shot 2): @Stream asks gently, red dust on her lips, searching his face with her bright dark eyes.
- 6–7s (Shot 2): @Stream keeps speaking, nodding at the red hand on the wall with a small proud smile.
- 7–8s (Shot 2): @Stream goes on warmly, touching the dry rock just beside the stencil with one fingertip.
- 8–9s (Shot 2): @Stream finishes and closes her mouth, waiting, while @Khang stares at the wall, his jaw trembling.
- 9–10s (CUT to Shot 3): @Khang lets out a shaky laugh, tears brimming, and starts answering, his voice cracking.
- 10–11s (Shot 3): @Khang keeps talking, wiping his eyes with the back of his wrist, laughing and crying at once.
- 11–12s (Shot 3): @Khang keeps speaking, holding up his red-dusted palm beside the red hand on the wall.
- 12–13s (CUT to Shot 4): @Khang goes on, shaking his head at himself, tears running down into his beard.
- 13–14s (Shot 4): @Khang finishes the last words with a broken grin, his eyes on the stencil.
- 14–15s (Shot 4): @Khang closes his mouth and breathes out shakily beside the fresh red hand, while @Stream watches him in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, a stunned whisper): "The big hand in the middle... it's mine. Always was."
- Turn 2, 4.9–8.5s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, gentle, puzzled, proud of her work): "What's wrong, Fire? No rain will ever wash it away."
- Turn 3, 9.0–14.0s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, laughing through tears): "No. Ten thousand years from now, some idiot will fit his hand in it."
- Pacing: @Khang speaks slowly and calmly, then @Stream answers at an even everyday pace, then @Khang answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: soft puffs of air through a hollow reed, a fine spray hissing on wet stone, water dripping in the cave, morning birdsong outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 19 - Clip 4 (`canh-19/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
The lower Stone Age cave the morning after the flood: wet mud on the floor, the elephant-shaped stalactite, the bare damp rock wall in soft daylight, a flat grinding stone with red-ochre powder and a hollow reed tube.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot at the wall, holding the previous framing, slow push-in.
- Shot 2, 5–9s: 85mm close-up of the survivalist turning to her, locked off.
- Shot 3, 9–12s: 50mm over-the-shoulder shot from behind the survivalist onto the young forager at the wall.
- Shot 4, 12–15s: 85mm close-up of the young forager in profile, the two red hands sharp on the wall beyond her, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Stream steps up beside @Khang, presses her small hand flat on the rock right next to his red stencil, and is already speaking softly.
- 1–2s (Shot 1): @Stream keeps talking, spreading her fingers wide on the damp stone, her eyes on the two hands.
- 2–3s (Shot 1): @Stream keeps speaking, a shy smile tugging at her mouth, while @Khang watches her with his mouth closed.
- 3–4s (Shot 1): @Stream goes on, lifting the hollow reed toward her chin with her free hand.
- 4–5s (Shot 1): @Stream finishes and closes her mouth, puts the reed to her lips, and @Khang turns toward her, swallowing.
- 5–6s (CUT to Shot 2): @Khang asks slowly and quietly, his eyes on her face, while soft red mist puffs out of focus beside him.
- 6–7s (Shot 2): @Khang keeps speaking haltingly, his voice low, his bearded jaw tight, his eyes never leaving her.
- 7–8s (Shot 2): @Khang goes on, glancing toward the daylight at the cave mouth and back to her.
- 8–9s (Shot 2): @Khang finishes his question, closes his mouth and waits, breathing slowly, the empty harness rising and falling on his chest.
- 9–10s (CUT to Shot 3): @Stream lowers the reed and peels her hand off the rock, two red hands now side by side, and answers without looking at him.
- 10–11s (Shot 3): @Stream keeps speaking, her eyes fixed on the wall, red dust on her fingertips.
- 11–12s (Shot 3): @Stream keeps talking evenly, touching the edge of her own red hand with one finger.
- 12–13s (CUT to Shot 4): @Stream goes on, her chin lifting, blinking fast, still not looking at him.
- 13–14s (Shot 4): @Stream keeps speaking steadily, a single tear sliding down past the red stripes on her cheek.
- 14–15s (Shot 4): @Stream finishes the last words and closes her mouth, gazing at the two red hands side by side, while @Khang watches her in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, soft and shy, eyes on the wall): "My hand next to yours. So everyone knows they went together."
- Turn 2, 4.9–8.9s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, hesitant, low and honest): "Stream... if I have to leave, will you be angry?"
- Turn 3, 9.4–14.4s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, steady, not looking at him): "A stream goes far but marks the stone. If you go, your hand stays."
- Pacing: @Stream speaks at an even everyday pace, then @Khang answers slowly and calmly, then @Stream answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: soft puffs of air through a reed, a fine spray hissing on stone, water dripping in the cave, morning birdsong outside, a slow breath. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 20 - Clip 1 (`canh-20/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
The jungle stream in the Stone Age at midday after the flood: the water clear again, a gravel bar with drying driftwood, a bundle of grass set up as a target, children of the clan playing on the stones.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: a few small clan children in knee-length bark-cloth tunics crouch on the river stones around the boy, grinning, in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the boy on a river stone holding a flat holed stone up like a camera, handheld follow.
- Shot 2, 4–9s: 85mm close-up of the survivalist on a boulder, laughing, locked off.
- Shot 3, 9–12s: 50mm over-the-shoulder shot from behind the survivalist onto the boy and the children.
- Shot 4, 12–15s: 24mm wide shot of the sunny gravel bar and the clear stream, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): On a sunny river stone, @Snail holds a flat stone with a hole in it up to his face like a camera and is already shouting excitedly into it.
- 1–2s (Shot 1): @Snail keeps talking fast, swinging the stone toward the clear stream and back to his own grinning face.
- 2–3s (Shot 1): @Snail keeps going, flexing one skinny arm for the stone, while the children around him bounce on their heels.
- 3–4s (Shot 1): @Snail finishes with a big proud grin and closes his mouth; on a boulder nearby, @Khang bursts out laughing and starts to answer.
- 4–5s (CUT to Shot 2): @Khang laughs and asks, shaking his head, his muddy elbows propped on his knees.
- 5–6s (Shot 2): @Khang keeps talking, wiping a tear of laughter from his eye with his wrist.
- 6–7s (Shot 2): @Khang goes on, his grin softening into something rueful, pointing at the boy.
- 7–8s (Shot 2): @Khang keeps speaking, tapping the empty chest harness on his torn shirt with two fingers.
- 8–9s (Shot 2): @Khang finishes and closes his mouth, still smiling, as @Snail spins around to face him.
- 9–10s (CUT to Shot 3): @Snail answers fast, jabbing the flat stone toward @Khang, his big eyes shining.
- 10–11s (Shot 3): @Snail keeps talking quickly, holding the stone up proudly to show off the hole.
- 11–12s (Shot 3): @Snail keeps going, pressing one eye to the hole as if filming @Khang.
- 12–13s (CUT to Shot 4): @Snail finishes, closes his mouth and grins through the hole in the stone.
- 13–14s (Shot 4): @Khang shakes with silent laughter, lips pressed together, and raises both hands in surrender as the children crowd closer.
- 14–15s (Shot 4): @Snail turns the stone toward the children on the gravel bar, mouth closed, while @Khang watches him fondly from the boulder. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.4s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, bursting with excitement, a tiny showman): "Hello everyone! Fire, fish, boiled water! I can survive anywhere!"
- Turn 2, 3.9–8.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, laughing, a little rueful): "Who taught you that? That line was a lie for three years."
- Turn 3, 8.7–12.3s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, quick and proud): "You say it to your stone every morning! Now I have one!"
- Pacing: @Snail speaks quickly, then @Khang answers at an even everyday pace, then @Snail answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: the clear stream rippling over stones, small bare feet splashing in the shallows, cicadas in the midday heat, driftwood creaking in the sun. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 20 - Clip 2 (`canh-20/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 7s, 9s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
The jungle stream in the Stone Age at midday after the flood: the water clear again, a gravel bar with drying driftwood, a bundle of grass set up as a target, children of the clan playing on the stones.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Roar = Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, his left ankle splinted between two straight sticks bound with a red bandana, leaning on a wooden staff, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera.
- Wardrobe: in this shot @Roar and @Khang wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium shot of the hunter seated on a flat rock with a half-woven fish trap, slow push-in.
- Shot 2, 5–7s: 24mm wide shot across the empty gravel bar, the survivalist in profile and the grass bundle far right, locked off.
- Shot 3, 7–9s: 85mm close-up of the survivalist, sweaty and grinning ruefully, locked off.
- Shot 4, 9–15s: 50mm over-the-shoulder shot from behind the survivalist onto the hunter, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): On the sunny gravel bar, @Roar sits on a flat rock with his splinted ankle stretched out, weaving a fish trap, and is already speaking with a gruff grin.
- 1–2s (Shot 1): @Roar keeps talking, squeezing his eyes shut in mockery and flapping one big hand at the sky.
- 2–3s (Shot 1): @Roar opens his eyes wide and keeps speaking, pointing two fingers from his eyes toward the grass bundle downstream.
- 3–4s (Shot 1): @Roar keeps going, miming a slow release with his open hand, while @Khang lifts the bamboo spear upright beside him, mouth closed.
- 4–5s (Shot 1): @Roar says the last words as @Khang walks out onto the empty gravel, sets his feet and raises the spear toward the grass bundle.
- 5–6s (CUT to Shot 2): @Roar closes his mouth as @Khang sends the spear arcing toward the grass bundle; it skids into the gravel far wide of it, and he starts complaining fast.
- 6–7s (Shot 2): @Khang keeps talking fast, both palms up at the untouched grass bundle, sweat running into his short beard.
- 7–8s (CUT to Shot 3): @Khang keeps going, pointing at the neat half-woven fish trap on @Roar's lap, his eyebrows high.
- 8–9s (Shot 3): @Khang keeps talking, shaking his head at his own blistered palms with a crooked laugh.
- 9–10s (CUT to Shot 4): @Khang finishes, closes his mouth and drops to sit on the gravel beside @Roar's rock, as @Roar starts answering.
- 10–11s (Shot 4): @Roar keeps speaking in his deep voice, tapping @Khang's blistered palm with one thick finger.
- 11–12s (Shot 4): @Roar keeps talking, lifting the half-woven fish trap and turning it in the sun.
- 12–13s (Shot 4): @Roar goes on, laying one heavy hand on @Khang's shoulder, his fierce eyes softening.
- 13–14s (Shot 4): @Roar keeps speaking, leaning closer, his gruff voice dropping warm on the final word.
- 14–15s (Shot 4): @Roar closes his mouth and a slow wide grin breaks across his fierce face, his shoulders shaking with a silent laugh. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.3s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking at a natural, even conversational pace, gruff and teasing, laughing for once): "Eyes closed, you only hit sky. Eyes open, see the target, let go."
- Turn 2, 5.8–9.1s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, frustrated, half laughing at himself): "You learned traps in one morning. I still can't hit anything!"
- Turn 3, 9.6–14.1s, spoken on camera by @Roar (man of 30, deep rough bass, gruff and forceful, speaking at a natural, even conversational pace, warm and gruff, almost proud): "Your hands make fire and traps. Leave the spear to me, brother."
- Pacing: @Roar speaks at an even everyday pace, then @Khang answers quickly, then @Roar answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a bamboo spear skidding across gravel, the stream rippling, split rattan creaking in big hands, cicadas, a breeze rustling the reeds. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 20 - Clip 3 (`canh-20/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
The lower Stone Age cave on the seventh day: the elephant-shaped stalactite and, on the rock wall, two fresh red-ochre hand stencils side by side, a big hand and a slightly smaller hand, with bare rock around them; a hearth fire burning.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the survivalist crouching beside the boy at the firelit wall, slow push-in.
- Shot 2, 4–8s: 85mm close-up of the boy drawing on the rock with a lump of charcoal, locked off.
- Shot 3, 8–11s: 50mm over-the-shoulder shot from behind the survivalist onto the boy and the charcoal drawing beside the two red hands.
- Shot 4, 11–15s: 85mm close-up of the survivalist in the firelight, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): By the firelit wall with the two red hands, @Khang crouches beside @Snail, who is scratching charcoal lines on the rock, and is already asking with a curious smile.
- 1–2s (Shot 1): @Khang keeps speaking, tilting his head at the charcoal stick figure taking shape beside the red hands.
- 2–3s (Shot 1): @Khang keeps going, tapping his own chest where the camera used to sit in the empty harness.
- 3–4s (Shot 1): @Khang finishes his question and closes his mouth, eyebrows raised, while @Snail adds a square to the figure's chest.
- 4–5s (CUT to Shot 2): @Snail keeps drawing and starts answering in a careful, focused voice without looking up.
- 5–6s (Shot 2): @Snail keeps talking, adding short rays around the square with quick charcoal strokes.
- 6–7s (Shot 2): @Snail keeps speaking, his eyes intent on the wall, black dust on his small fingers.
- 7–8s (Shot 2): @Snail goes on, his voice dropping a little, the charcoal pausing over the rock.
- 8–9s (CUT to Shot 3): @Snail keeps talking, turning to look up at @Khang with big serious eyes.
- 9–10s (Shot 3): @Snail keeps speaking earnestly, pointing the charcoal at the little box on the figure's chest.
- 10–11s (Shot 3): @Snail finishes and closes his mouth, waiting for a verdict, while @Khang stares at the drawing.
- 11–12s (CUT to Shot 4): @Khang swallows hard and answers slowly, his voice thick, his eyes shining in the firelight.
- 12–13s (Shot 4): @Khang keeps speaking softly, laying one hand gently on @Snail's shaved head.
- 13–14s (Shot 4): @Khang finishes the last words almost in a whisper and closes his mouth.
- 14–15s (Shot 4): @Khang breathes out and smiles, mouth closed, his eyes wet in the flickering firelight. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.0s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, curious, gently amused): "What's this? Why's he wearing a box on his chest?"
- Turn 2, 4.5–10.6s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking at a natural, even conversational pace, earnest, absorbed in his drawing): "It's you and your seeing stone. The water took it. I drew it so it's not sad."
- Turn 3, 11.1–13.9s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, moved, voice thick): "It's beautiful. Best picture I've ever had."
- Pacing: @Khang speaks at an even everyday pace, then @Snail answers at an even everyday pace, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: charcoal scratching on rock, the hearth fire crackling, water dripping from the stalactite, the stream murmuring outside the cave. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 20 - Clip 4 (`canh-20/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Late afternoon at the mouth of the Stone Age clan cave: black storm clouds rolling over the karst peaks, distant thunder, wind in the jungle, warm firelight behind, and on the inner wall two red-ochre hand stencils.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Moon = Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium two-shot at the cave mouth, storm clouds rolling over the karst peaks behind them, slow push-in.
- Shot 2, 4–8s: 85mm close-up of the survivalist with his palm on the rock wall, locked off.
- Shot 3, 8–12s: 50mm over-the-shoulder shot from behind the survivalist onto the old woman, locked off.
- Shot 4, 12–15s: 85mm close-up of the old woman, lightning flickering on her face, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): At the cave mouth, @Moon stands beside @Khang watching black storm clouds roll over the karst peaks, and is already speaking slowly.
- 1–2s (Shot 1): @Moon keeps speaking, her white hair stirring in the rising wind, a far flicker of lightning behind the peaks.
- 2–3s (Shot 1): @Moon goes on, her calm eyes narrowing at the clouds, the bamboo ember tube held against her cloak.
- 3–4s (Shot 1): @Moon finishes and closes her mouth; @Khang turns from the storm and reaches toward the inner rock wall.
- 4–5s (CUT to Shot 2): @Khang lays his palm flat on the rock beside the two red hands and starts speaking, his eyes narrowing.
- 5–6s (Shot 2): @Khang keeps talking, pressing harder, then jerks his hand back off the stone.
- 6–7s (Shot 2): @Khang keeps speaking, staring down into his open palm, rubbing his fingertips together.
- 7–8s (Shot 2): @Khang goes on, lifting his warm palm toward @Moon, his breath quickening.
- 8–9s (CUT to Shot 3): @Khang finishes and closes his mouth, looking at @Moon, as she turns her face to him.
- 9–10s (Shot 3): @Moon answers slowly, laying her own wrinkled hand on the wall beside his red stencil.
- 10–11s (Shot 3): @Moon keeps speaking, her voice low and certain, as thunder rolls over the peaks outside.
- 11–12s (Shot 3): @Moon goes on, turning her eyes to the dark clouds beyond the cave mouth.
- 12–13s (CUT to Shot 4): @Moon keeps speaking slowly, lightning flickering across the deep lines of her face.
- 13–14s (Shot 4): @Moon says the last words softly, her eyes resting on his face, then closes her mouth.
- 14–15s (Shot 4): @Moon stands in silence, mouth closed, the wind tugging at her hide cloak as she looks at him. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.3s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and grave, listening to the sky): "Thunder again. Like the night you came."
- Turn 2, 3.8–8.1s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, uneasy, half laughing in disbelief): "You feel it too? Since noon, the wall has been getting warmer."
- Turn 3, 8.6–14.0s, spoken on camera by @Moon (old woman of 65, low slow husky voice with weight in every word, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow, tender and final): "Thunder brought you. Thunder will call you home. The cave remembers its own."
- Pacing: @Moon speaks slowly and calmly, then @Khang answers at an even everyday pace, then @Moon answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.0s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: distant rolling thunder, wind rushing through the jungle canopy, the hearth fire crackling behind, the first fat raindrops on broad leaves. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 21 - Clip 1 (`canh-21/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A storm at night inside the lower Stone Age cave: white lightning flashing through the wide mouth onto the rock wall with two red-ochre hand stencils side by side and a small charcoal stick figure, the elephant-shaped stalactite, a flickering hearth fire, the clan standing back in the shadows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: the rest of the clan in bark-cloth tunics and hide wraps stands back in the shadows near the hearth, faces lost in darkness, in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium shot from the wall of red hands, the survivalist in the foreground facing the rock and the young forager behind him, locked off.
- Shot 2, 5–9s: 85mm close-up of the survivalist turning around, lightning flickering on his face, locked off.
- Shot 3, 9–13s: 50mm over-the-shoulder shot from behind the young forager onto the survivalist against the wall of red hands.
- Shot 4, 13–15s: 85mm close-up of the young forager, eyes wet in the firelight, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the storm-lit cave, @Khang stands facing the wall of red hands while @Stream stands behind him gripping her basket strap, and she is already speaking slowly.
- 1–2s (Shot 1): @Stream keeps speaking softly, her knuckles pale on the rattan strap, while @Khang stays still with his mouth closed.
- 2–3s (Shot 1): A white flash of lightning floods the cave as @Stream goes on, her voice low and unsteady.
- 3–4s (Shot 1): @Stream keeps talking, taking one small step closer to his back, her eyes glistening.
- 4–5s (Shot 1): @Stream keeps speaking, nearly whispering now, her chin trembling in the firelight as thunder rolls outside.
- 5–6s (CUT to Shot 2): @Stream finishes and closes her mouth; @Khang turns around to face her and starts answering in a low voice.
- 6–7s (Shot 2): @Khang keeps speaking gently, his eyes moving over her face, lightning flickering across his short beard.
- 7–8s (Shot 2): @Khang keeps talking, glancing past her toward the hearth and the clan in the shadows.
- 8–9s (Shot 2): @Khang goes on, his voice catching, one hand lifting toward her and stopping halfway.
- 9–10s (CUT to Shot 3): @Khang keeps speaking, looking out at the white sheets of rain beyond the cave mouth.
- 10–11s (Shot 3): @Khang keeps talking, his jaw tight, swallowing hard between phrases as the hearth fire flickers on his face.
- 11–12s (Shot 3): @Khang keeps going, his eyes returning to hers, brimming in the flicker of lightning.
- 12–13s (Shot 3): @Khang finishes and closes his mouth; @Stream lowers her eyes and draws a ragged breath.
- 13–14s (CUT to Shot 4): @Stream answers in a small breaking voice, nodding once, her lips trembling.
- 14–15s (Shot 4): @Stream finishes and closes her mouth, her eyes wet, as another white flash lights her face and fades. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and hurt, voice barely steady): "Are you really leaving, Fire? Here there's fire, fish, me. Not enough?"
- Turn 2, 5.7–12.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, turning to her, gentle and torn): "More than enough. More than anywhere I've lived. But my mom is waiting, and my friend is searching."
- Turn 3, 12.7–14.2s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, voice breaking, holding back tears): "Then you must go."
- Pacing: @Stream speaks slowly and calmly, then @Khang answers at an even everyday pace, then @Stream answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: rolling thunder, rain roaring beyond the cave mouth, wind gusting through the entrance, the hearth fire hissing and crackling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 21 - Clip 2 (`canh-21/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A storm at night inside the lower Stone Age cave: white lightning flashing through the wide mouth onto the rock wall with two red-ochre hand stencils side by side and a small charcoal stick figure, the elephant-shaped stalactite, a flickering hearth fire, the clan standing back in the shadows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 85mm close-up of the young forager, holding the previous framing.
- Shot 2, 3–6s: 50mm medium two-shot as she rises on tiptoe toward him, slow push-in.
- Shot 3, 6–10s: 85mm close-up of the survivalist turning a small shell in his fingers, locked off.
- Shot 4, 10–15s: 50mm over-the-shoulder shot from behind the survivalist onto the young forager, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Stream lifts the necklace of small stream-snail shells off over her head with both hands and is already speaking, her voice wavering.
- 1–2s (Shot 1): @Stream keeps speaking, holding the shell necklace out between them, the shells clicking softly.
- 2–3s (Shot 1): @Stream keeps talking, motioning him down with a small tug of the cord.
- 3–4s (CUT to Shot 2): @Khang bends his head; @Stream rises on her tiptoes and loops the necklace over his neck, still speaking.
- 4–5s (Shot 2): @Stream keeps talking softly as she settles the shells against his torn shirt with careful fingers.
- 5–6s (Shot 2): @Stream finishes and closes her mouth, her hands lingering on the cord, as @Khang lifts one small shell and starts to speak slowly.
- 6–7s (CUT to Shot 3): @Khang keeps speaking slowly, turning the small shell in his fingers, his eyes fixed on it.
- 7–8s (Shot 3): @Khang goes on, a dawning smile spreading as he looks from the shell to her.
- 8–9s (Shot 3): @Khang keeps speaking softly, his voice catching, his eyes shining in the firelight.
- 9–10s (Shot 3): @Khang finishes his question and closes his mouth, searching her face, the shell still between his fingers.
- 10–11s (CUT to Shot 4): @Stream nods quickly, laughing through her tears, and answers in a warm, trembling voice, her eyes on his.
- 11–12s (Shot 4): @Stream keeps speaking, tapping the shells on his chest with one finger, tears running past the red stripes on her cheeks.
- 12–13s (Shot 4): @Stream keeps talking, smiling and crying at once, her chin lifted bravely in the flicker of the storm.
- 13–14s (Shot 4): @Stream goes on, pressing her palm flat over the shells against his chest.
- 14–15s (Shot 4): @Stream finishes the last words and closes her mouth, while lightning flashes white across both their faces. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.4s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, voice wavering, holding back tears): "Bend down. Where you live, there are no stream snails. Remember us with this."
- Turn 2, 5.9–9.9s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow realization, a soft wondering smile): "Snail... Stream. Stream snails. You're giving me both of you?"
- Turn 3, 10.4–14.4s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking at a natural, even conversational pace, laughing through tears): "Yes. Take both of us, so you never get lost again."
- Pacing: @Stream speaks at an even everyday pace, then @Khang answers slowly and calmly, then @Stream answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: small shells clicking on a cord, rain hammering outside the cave mouth, low thunder, the hearth fire crackling. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 21 - Clip 3 (`canh-21/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A storm at night inside the lower Stone Age cave: white lightning flashing through the wide mouth onto the rock wall with two red-ochre hand stencils side by side and a small charcoal stick figure, the elephant-shaped stalactite, a flickering hearth fire, the clan standing back in the shadows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera, a necklace of small stream-snail shells.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot of the boy clinging to the survivalist's legs in the firelight, handheld.
- Shot 2, 4–10s: 85mm close-up of the survivalist kneeling to the boy's height, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the survivalist onto the boy, slow push-in.
- Shot 4, 13–15s: 35mm medium two-shot of the two holding each other before the wall of red hands, lightning at the mouth, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Snail runs out of the firelight and wraps both arms around @Khang's legs, the flat stone still clutched in one fist, and is already shouting through tears.
- 1–2s (Shot 1): @Snail keeps shouting through tears, tipping his head back to look up at @Khang's face.
- 2–3s (Shot 1): @Snail keeps talking fast, holding up the flat stone with the hole as if to prove he is ready.
- 3–4s (Shot 1): @Snail finishes, sobs once and closes his mouth, pressing his wet face into @Khang's muddy trousers.
- 4–5s (CUT to Shot 2): @Khang kneels down to the boy's height, takes his small shoulders in both hands and starts speaking.
- 5–6s (Shot 2): @Khang keeps speaking gently, brushing the tears from @Snail's cheek with his thumb.
- 6–7s (Shot 2): @Khang keeps talking, counting on his fingers in front of the boy's wet eyes.
- 7–8s (Shot 2): @Khang goes on, tapping the flat stone in the boy's fist with one finger.
- 8–9s (Shot 2): @Khang keeps speaking, lightning flaring white across his bearded face, his eyes wet but steady.
- 9–10s (Shot 2): @Khang keeps talking warmly, squeezing the boy's shoulders, a proud smile breaking through.
- 10–11s (CUT to Shot 3): @Khang finishes and closes his mouth; @Snail sniffs hard, his lower lip trembling, and starts to answer.
- 11–12s (Shot 3): @Snail keeps speaking slowly in a wobbly voice, holding the flat stone up between them.
- 12–13s (Shot 3): @Snail keeps talking, his face crumpling, tears running down his round cheeks.
- 13–14s (CUT to Shot 4): @Snail finishes the last words, closes his mouth and flings his arms around @Khang's neck.
- 14–15s (Shot 4): @Khang holds the boy tight, mouth closed, eyes squeezed shut, as lightning flashes white across the cave mouth behind them. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.0s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, sobbing, desperate and fast): "Don't go, Fire! Take me with you! I'll bring my seeing stone!"
- Turn 2, 4.5–10.3s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, kneeling, gentle and proud): "Stay and teach them: boiling water, fish traps, bamboo fire. Nobody does it better than you."
- Turn 3, 10.8–13.6s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking slowly and softly, unhurried, with a short natural pause between phrases, lip wobbling, brave through tears): "Then say hello everyone for me, okay?"
- Pacing: @Snail speaks quickly, then @Khang answers at an even everyday pace, then @Snail answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: rain roaring outside the cave mouth, thunder rumbling, the hearth fire crackling, small bare feet pattering on stone. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 21 - Clip 4 (`canh-21/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
A storm at night inside the lower Stone Age cave: white lightning flashing through the wide mouth onto the rock wall with two red-ochre hand stencils side by side and a small charcoal stick figure, the elephant-shaped stalactite, a flickering hearth fire, the clan standing back in the shadows.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera, a necklace of small stream-snail shells.
- @Stream = Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, no necklace, a woven rattan basket on her back, barefoot.
- Wardrobe: in this shot @Khang and @Stream wear the outfits written above, not the outfit in the reference image; faces and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium shot of the survivalist pressing his hand into the big red stencil on the wall, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the young forager backing away in the storm light, handheld.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the young forager onto the survivalist at the glowing wall.
- Shot 4, 13–15s: 85mm close-up of the survivalist beside his glowing hand, the frame burning to white, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the storm-lit cave, @Khang lays his open hand into the big red stencil in the middle of the wall, fingers sliding into place, and is already speaking slowly.
- 1–2s (Shot 1): @Khang keeps speaking softly, staring at his hand fitting the red outline exactly, his breath unsteady.
- 2–3s (Shot 1): @Khang turns his head over his shoulder toward @Stream and keeps talking, his voice low and steady.
- 3–4s (Shot 1): @Khang goes on, his eyes on her, as the rock under his palm begins to tremble and dust trickles down.
- 4–5s (Shot 1): @Khang keeps speaking, a faint white glow starting to seep between his fingers on the stencil.
- 5–6s (CUT to Shot 2): @Khang finishes and closes his mouth; @Stream backs away from the trembling wall and starts shouting over the thunder.
- 6–7s (Shot 2): @Stream keeps shouting, her long hair whipping in the wind, white lightning flaring across her wet face.
- 7–8s (Shot 2): @Stream keeps calling out fast, one arm raised toward him, tears streaming past the red stripes on her cheeks.
- 8–9s (Shot 2): @Stream keeps going, her voice ringing over the roar of the rain as she steps back again.
- 9–10s (Shot 2): @Stream finishes her cry and closes her mouth, her chest heaving, her eyes locked on him.
- 10–11s (CUT to Shot 3): @Khang, his palm still pressed to the glowing stencil, looks back at her and answers slowly, his face lit white.
- 11–12s (Shot 3): @Khang keeps speaking, holding her gaze as white light pours brighter between his fingers.
- 12–13s (Shot 3): @Khang goes on softly, the stream-snail shells on his chest trembling with the rock.
- 13–14s (CUT to Shot 4): @Khang finishes the last words and closes his mouth, a small calm smile in his short beard.
- 14–15s (Shot 4): A blinding white lightning flash floods the cave and swallows the whole frame in pure white. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and calm, a quiet goodbye): "My hand still fits. Stream, take care of Snail, and the cave."
- Turn 2, 5.7–9.6s, spoken on camera by @Stream (young woman of 19, clear warm alto, direct and curious, speaking quickly in short lively phrases, every word still clear, shouting over the thunder, in tears): "Go, Fire-Maker! The cave will remember you until the stones wear away!"
- Turn 3, 10.1–13.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and tender, a last promise): "I'll remember you too. Even ten thousand years apart."
- Pacing: @Khang speaks slowly and calmly, then @Stream answers quickly, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a deep rumble shaking the rock, thunder cracking right overhead, roaring rain, a rising electric hum, then one huge thunderclap. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 22 - Clip 1 (`canh-22/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Early morning inside the same large limestone cave today after the storm: the elephant-shaped stalactite, the wall of hundreds of faded red-ochre hand stencils with one bigger hand in the middle and a slightly smaller hand right beside it, rescue ropes on the floor, flashlight beams in the dusty air.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; torn mud-stained olive-green tactical shirt, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera, a necklace of small stream-snail shells.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: two forest rangers in olive-green uniforms and caps, carrying flashlights and a handheld radio, hurry in behind the young man in soft focus
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 35mm medium shot following the cameraman as he runs in through the flashlight beams, handheld.
- Shot 2, 4–8s: 85mm close-up of the survivalist lying at the foot of the wall, squinting into the light, locked off.
- Shot 3, 8–12s: 50mm over-the-shoulder shot from behind the survivalist onto the cameraman kneeling over him.
- Shot 4, 12–15s: 24mm wide shot of the cave, flashlight beams crossing the wall of faded red hands, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Flashlight beams sweep the dusty cave as @Bin runs in toward the foot of the wall and is already shouting, his round glasses flashing.
- 1–2s (Shot 1): @Bin keeps shouting fast over his shoulder to the rangers behind him, pointing at the figure on the ground.
- 2–3s (Shot 1): @Bin drops to his knees beside @Khang, still talking, his flashlight shaking in his hand.
- 3–4s (Shot 1): @Bin finishes his frantic question and closes his mouth, staring, as @Khang's eyes flutter open.
- 4–5s (CUT to Shot 2): @Khang, lying on the dusty floor with a short dark beard and torn shirt, squints into the light and speaks slowly, dazed.
- 5–6s (Shot 2): @Khang keeps speaking in a hoarse voice, lifting one blistered hand to shade his eyes.
- 6–7s (Shot 2): @Khang goes on, a slow dazed smile spreading through his beard as he recognizes the face above him.
- 7–8s (Shot 2): @Khang finishes and closes his mouth, blinking; @Bin's face crumples and he bursts out talking again.
- 8–9s (CUT to Shot 3): @Bin keeps talking fast, half laughing, half sobbing, holding @Khang's shoulders with both hands.
- 9–10s (Shot 3): @Bin keeps going, waving his flashlight toward the cave mouth and the rangers behind him.
- 10–11s (Shot 3): @Bin keeps talking, tears fogging his round glasses, shaking his head in disbelief.
- 11–12s (Shot 3): @Bin goes on rapidly, pushing his bucket hat back and wiping his eyes with his sleeve.
- 12–13s (CUT to Shot 4): @Bin finishes and closes his mouth, gasping, both hands still on @Khang's shoulders.
- 13–14s (Shot 4): The rangers' flashlight beams cross the wall of faded red hands above them, while @Khang lies still, mouth closed, smiling faintly.
- 14–15s (Shot 4): @Bin bows his forehead onto @Khang's shoulder, mouth closed, as the rangers crouch nearby in soft focus. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–3.4s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, frantic, breaking down with relief): "Khang! He's here! Call the rescue team! Are you alive?"
- Turn 2, 3.9–7.1s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, dazed and hoarse, half dreaming): "Bin... it's really you. What day is it?"
- Turn 3, 7.6–12.4s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, fast, laughing and sobbing at once): "You've been missing seven days! The whole country searched! The rangers flipped this forest upside down!"
- Pacing: @Bin speaks quickly, then @Khang answers slowly and calmly, then @Bin answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: running footsteps on the dusty cave floor, a handheld radio hissing static, water dripping, morning birdsong outside the mouth, heavy panting. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 22 - Clip 2 (`canh-22/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Early morning inside the same large limestone cave today after the storm: the elephant-shaped stalactite, the wall of hundreds of faded red-ochre hand stencils with one bigger hand in the middle and a slightly smaller hand right beside it, rescue ropes on the floor, flashlight beams in the dusty air.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; torn mud-stained olive-green tactical shirt, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera, a necklace of small stream-snail shells.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 50mm medium two-shot of the survivalist sitting up against the wall, the cameraman steadying him, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the cameraman, flashlight glare on his round glasses, handheld.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the cameraman onto the survivalist, locked off.
- Shot 4, 13–15s: 85mm close-up of the survivalist, the faded red hands soft behind him, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang pushes himself up to sit against the wall of faded red hands, touches the shell necklace at his neck, and is already speaking slowly.
- 1–2s (Shot 1): @Khang keeps speaking in a low wondering voice, rolling one small shell between his fingers, while @Bin steadies his shoulder.
- 2–3s (Shot 1): @Khang goes on slowly, his eyes drifting over the elephant-shaped stalactite and the wall of hands.
- 3–4s (Shot 1): @Khang keeps talking quietly, a faint smile in his beard, as if remembering a far-off place.
- 4–5s (Shot 1): @Khang finishes and closes his mouth; @Bin stares at him, then at the necklace, and starts firing questions.
- 5–6s (CUT to Shot 2): @Bin keeps talking fast, flicking one shell on the necklace with a finger, his eyebrows shooting up.
- 6–7s (Shot 2): @Bin keeps going, tapping the empty clip on @Khang's chest harness where the camera should be.
- 7–8s (Shot 2): @Bin keeps asking rapidly, pushing his round glasses up his nose, eyes darting over the empty harness.
- 8–9s (Shot 2): @Bin keeps talking, both palms up, leaning in close to @Khang's face.
- 9–10s (Shot 2): @Bin finishes his last question and closes his mouth, waiting, his lips pressed tight.
- 10–11s (CUT to Shot 3): @Khang answers in an even voice, looking down at the empty harness and patting it once.
- 11–12s (Shot 3): @Khang keeps speaking calmly, spreading his empty blistered hands on his knees and looking at them.
- 12–13s (Shot 3): @Khang goes on, a strange peaceful smile settling on his bearded face.
- 13–14s (CUT to Shot 4): @Khang finishes the last words and closes his mouth, lifting his eyes to @Bin.
- 14–15s (Shot 4): @Khang sits quietly against the wall of red hands, mouth closed, holding one shell of his necklace between two fingers. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and dreamy, still half elsewhere): "Seven days... it was seven days there too. Seven suns."
- Turn 2, 4.9–9.4s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, rapid-fire, baffled): "What are you saying? Where's this necklace from? Where's the camera? What did you film?"
- Turn 3, 9.9–13.9s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, calm and plain, strangely at peace): "The camera's gone. Seven days, and not one second of footage."
- Pacing: @Khang speaks slowly and calmly, then @Bin answers quickly, then @Khang answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.9s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a handheld radio hissing static nearby, water dripping in the cave, birdsong outside, small shells clicking, distant footsteps on grit. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 22 - Clip 3 (`canh-22/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 9s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Early morning inside the same large limestone cave today after the storm: the elephant-shaped stalactite, the wall of hundreds of faded red-ochre hand stencils with one bigger hand in the middle and a slightly smaller hand right beside it, rescue ropes on the floor, flashlight beams in the dusty air.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; torn mud-stained olive-green tactical shirt, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera, a necklace of small stream-snail shells.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium shot of the cameraman pacing in the dusty flashlight haze, handheld follow.
- Shot 2, 5–9s: 85mm close-up of the survivalist looking at his own calloused palms, locked off.
- Shot 3, 9–12s: 50mm over-the-shoulder shot from behind the survivalist onto the cameraman stopping mid-step.
- Shot 4, 12–15s: 35mm medium two-shot of the two men sitting side by side against the wall of faded red hands, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bin springs to his feet, both hands on his bucket hat, and is already talking fast as he paces in a tight circle.
- 1–2s (Shot 1): @Bin keeps talking rapidly, spinning back toward @Khang with his arms flung wide.
- 2–3s (Shot 1): @Bin keeps going, jabbing a finger at the empty chest harness, his glasses slipping down his nose.
- 3–4s (Shot 1): @Bin keeps talking fast, pulling his phone from his pocket and waving its blank glowing screen.
- 4–5s (Shot 1): @Bin finishes, pockets the phone and closes his mouth, staring down at @Khang.
- 5–6s (CUT to Shot 2): @Khang lifts both calloused, blistered hands in front of his face and answers in an even voice.
- 6–7s (Shot 2): @Khang keeps speaking, turning his palms over slowly in the dusty light.
- 7–8s (Shot 2): @Khang goes on, closing his fingers into loose fists, a quiet certainty in his eyes.
- 8–9s (Shot 2): @Khang finishes and closes his mouth, still looking at his hands, as @Bin's pacing slows to a stop.
- 9–10s (CUT to Shot 3): @Bin stops pacing, his face crumpling, and starts speaking slowly in a thick, quiet voice.
- 10–11s (Shot 3): @Bin keeps speaking, pulling off his round glasses and pressing his wrist to his eyes.
- 11–12s (Shot 3): @Bin goes on softly, his shoulders dropping as the tension drains out of him.
- 12–13s (CUT to Shot 4): @Bin sits down heavily beside @Khang against the wall, still speaking, his voice cracking.
- 13–14s (Shot 4): @Bin finishes the last words and closes his mouth, leaning his shoulder against @Khang's.
- 14–15s (Shot 4): @Khang puts one arm around @Bin's shoulders, both silent with their mouths closed, beneath the wall of faded red hands. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, exasperated, rapid, half hysterical): "Seven days, the whole country watching, and you come back empty-handed? Subscribers are exploding!"
- Turn 2, 5.4–8.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, calm, quietly proud): "Not empty-handed. These hands can make fire now."
- Turn 3, 9.2–13.6s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking slowly and softly, unhurried, with a short natural pause between phrases, voice thick, finally letting go): "Forget it. You're back, that's enough. I thought I'd lost you."
- Pacing: @Bin speaks quickly, then @Khang answers at an even everyday pace, then @Bin answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.6s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: sneakers scuffing on the dusty floor, a radio hissing static, water dripping, birdsong outside the cave mouth, a shaky exhale. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 22 - Clip 4 (`canh-22/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Early morning inside the same large limestone cave today after the storm: the elephant-shaped stalactite, the wall of hundreds of faded red-ochre hand stencils with one bigger hand in the middle and a slightly smaller hand right beside it, rescue ropes on the floor, flashlight beams in the dusty air.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; torn mud-stained olive-green tactical shirt, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera, a necklace of small stream-snail shells.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot against the wall, holding the previous framing, tilting up as the survivalist rises.
- Shot 2, 5–10s: 85mm close-up of the cameraman aiming his flashlight, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the cameraman onto the survivalist at the wall of faded red hands.
- Shot 4, 13–15s: 85mm close-up of the survivalist in profile, his open hand hovering near the big faded hand, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang rises to his feet beside @Bin and is already speaking, his eyes fixed on the wall of faded red hands.
- 1–2s (Shot 1): @Khang keeps talking, stepping slowly toward the wall, one hand trailing along the cool stone.
- 2–3s (Shot 1): @Khang keeps speaking, stopping in front of the big faded hand in the middle of the wall.
- 3–4s (Shot 1): @Khang goes on, his gaze moving to the slightly smaller faded hand right beside it.
- 4–5s (Shot 1): @Khang finishes his question and closes his mouth, still facing the wall, while @Bin follows with his flashlight.
- 5–6s (CUT to Shot 2): @Bin answers in a dry deadpan, swinging his flashlight beam across the wall of hands.
- 6–7s (Shot 2): @Bin keeps talking, one eyebrow raised above his round glasses, the flashlight beam wobbling on the rock.
- 7–8s (Shot 2): @Bin keeps going, tapping his own temple with the end of the flashlight.
- 8–9s (Shot 2): @Bin keeps speaking, squinting at @Khang's back with a crooked half-smile and a small shake of the head.
- 9–10s (Shot 2): @Bin finishes and closes his mouth, the flashlight beam resting on the big faded hand.
- 10–11s (CUT to Shot 3): @Khang answers slowly over his shoulder, a soft smile in his beard.
- 11–12s (Shot 3): @Khang keeps speaking quietly, raising his open hand toward the big faded hand.
- 12–13s (Shot 3): @Khang goes on, his fingers hovering a breath away from the rock without touching it.
- 13–14s (CUT to Shot 4): @Khang keeps speaking softly, his eyes clear and calm in the flashlight glow.
- 14–15s (Shot 4): @Khang finishes the last words and closes his mouth, his hand still hovering just short of the faded red hand. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.1s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, quiet and wondering): "Bin, do you believe someone once spent their whole life by this wall?"
- Turn 2, 5.6–9.9s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking at a natural, even conversational pace, deadpan and teasing): "Cave people lived in caves, sure. Did the lightning fry your brain?"
- Turn 3, 10.4–14.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow, calm and clear-eyed): "Maybe. But for the first time, my head feels clear."
- Pacing: @Khang speaks at an even everyday pace, then @Bin answers at an even everyday pace, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: boots crunching on grit, water dripping from the stalactite, a flashlight click, birdsong at the cave mouth, a soft wind through the entrance. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 23 - Clip 1 (`canh-23/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 7s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
The wooden porch of a stilt-house guesthouse at the forest edge today in late afternoon: worn plank steps, potted plants, a smartphone on a small tripod, limestone peaks glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; plain grey cotton T-shirt, khaki cargo trousers, brown hiking boots, a necklace of small stream-snail shells.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the survivalist on the porch step facing a phone on a small tripod, locked off.
- Shot 2, 4–7s: 85mm close-up of the survivalist looking straight into the lens, slow push-in.
- Shot 3, 7–10s: 50mm over-the-shoulder shot from behind the survivalist onto the cameraman leaning out from behind the tripod.
- Shot 4, 10–15s: 85mm close-up of the survivalist turning back to the lens, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): On the sunlit porch step, @Khang sits facing a smartphone on a small tripod and is already speaking plainly into its lens.
- 1–2s (Shot 1): @Khang keeps speaking evenly, the shell necklace resting on his plain grey T-shirt, his hands loose on his knees.
- 2–3s (Shot 1): @Khang goes on, a wry twist at the corner of his mouth as he shakes his head once.
- 3–4s (Shot 1): @Khang keeps talking, looking straight into the lens without a showman's grin.
- 4–5s (CUT to Shot 2): @Khang keeps speaking steadily, rubbing the faint blister scars on one palm with his thumb.
- 5–6s (Shot 2): @Khang keeps going, his jaw set, holding the lens with his eyes.
- 6–7s (Shot 2): @Khang finishes and closes his mouth; behind the tripod, @Bin leans out sideways and starts asking softly.
- 7–8s (CUT to Shot 3): @Bin keeps speaking in a low voice, glancing at the blank glowing phone screen and back at @Khang.
- 8–9s (Shot 3): @Bin keeps going quietly, eyebrows lifted above his round glasses, one hand on the tripod leg.
- 9–10s (Shot 3): @Bin finishes and closes his mouth, waiting, his lips pressed together, his eyes flicking to the phone.
- 10–11s (CUT to Shot 4): @Khang turns back to the lens and answers slowly, without a trace of hesitation.
- 11–12s (Shot 4): @Khang keeps speaking, a small calm shrug lifting his shoulders, his eyes never leaving the lens.
- 12–13s (Shot 4): @Khang goes on, touching one shell of the necklace at his collar.
- 13–14s (Shot 4): @Khang finishes the last words and closes his mouth, his eyes steady on the lens.
- 14–15s (Shot 4): @Khang sits still on the porch step, mouth closed, the limestone peaks glowing behind him in the late sun. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–6.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, plain and honest, no showman): "Today, no old opening line. I can survive anywhere: I lied about that for three years."
- Turn 2, 6.7–10.0s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking at a natural, even conversational pace, quiet and worried): "You sure? Say that, and the last sponsors walk."
- Turn 3, 10.5–13.7s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and certain): "Sure. Let them. Faking it makes you starve."
- Pacing: @Khang speaks at an even everyday pace, then @Bin answers at an even everyday pace, then @Khang answers slowly and calmly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: cicadas at the forest edge, a rooster far off, wooden porch boards creaking, leaves rustling in a light breeze. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 23 - Clip 2 (`canh-23/clip-2.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 11s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
The wooden porch of a stilt-house guesthouse at the forest edge today in late afternoon: worn plank steps, potted plants, a smartphone on a small tripod, limestone peaks glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; plain grey cotton T-shirt, khaki cargo trousers, brown hiking boots, a necklace of small stream-snail shells.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 85mm close-up of the survivalist talking to the phone lens, holding the previous framing.
- Shot 2, 5–8s: 50mm medium shot of the survivalist lifting a green bamboo tube from the porch boards, locked off.
- Shot 3, 8–11s: 85mm close-up of the survivalist holding a notched bamboo strip beside his face, locked off.
- Shot 4, 11–13s: 50mm medium shot of the survivalist raising a small whistle, slow push-in.
- Shot 5, 13–15s: 100mm extreme close-up of the whistle resting on his scarred open palm, locked off.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang keeps his eyes on the phone lens and is already speaking, his voice low and steady, the shell necklace at his collar.
- 1–2s (Shot 1): @Khang keeps speaking honestly, his gaze dropping for a moment to his hands.
- 2–3s (Shot 1): @Khang goes on, lifting his eyes back to the lens, his jaw tight.
- 3–4s (Shot 1): @Khang keeps talking, pressing one palm flat against his chest in apology.
- 4–5s (Shot 1): @Khang says the last words of the apology, then takes one slow breath.
- 5–6s (CUT to Shot 2): @Khang closes his mouth briefly, picks up a fresh green bamboo tube from the porch boards and starts talking fast.
- 6–7s (Shot 2): @Khang keeps talking quickly, holding the green bamboo tube up to the lens and tapping its node.
- 7–8s (Shot 2): @Khang keeps going, setting the tube down and lifting a split bamboo strip with a notched groove.
- 8–9s (CUT to Shot 3): @Khang keeps talking fast, sawing his fingertip across the notch to show the motion.
- 9–10s (Shot 3): @Khang keeps speaking, showing the faint blister scars across his palm beside the bamboo.
- 10–11s (Shot 3): @Khang keeps going, setting the bamboo down and holding up a small plastic whistle.
- 11–12s (CUT to Shot 4): @Khang keeps talking quickly, raising three fingers beside the whistle and nodding firmly at the lens.
- 12–13s (Shot 4): @Khang finishes the last words and closes his mouth, the whistle still raised.
- 13–14s (CUT to Shot 5): @Khang lowers the whistle into his open palm, mouth closed, looking calmly at the lens.
- 14–15s (Shot 5): The whistle rests in @Khang's open palm, faint blister scars catching the late golden sun, all quiet but the cicadas. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, spoken on camera by @Khang alone in two parts in this order with a short breath between them, each said exactly once (no subtitles):
- Part 1, 0.4–5.1s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, quiet and sincere, an apology): "Most of my old videos were staged. You trusted me, and I'm sorry."
- Part 2, 5.6–12.8s (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking quickly in short lively phrases, every word still clear, brisk and practical, teaching for real): "Here's what's real, learned with blistered hands: boil your water, green bamboo can boil it, bamboo can make fire, three whistle blasts means help."
- Pacing: @Khang speaks at an even everyday pace, then @Khang continues quickly; the change of speed is clearly audible.
- Throughout, @Khang's face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word @Khang closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.8s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: porch boards creaking, bamboo knocking softly on wood, cicadas at the forest edge, a light breeze through the potted plants. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 23 - Clip 3 (`canh-23/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 8s, 12s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
The wooden porch of a stilt-house guesthouse at the forest edge today in late afternoon: worn plank steps, potted plants, a smartphone on a small tripod, limestone peaks glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; plain grey cotton T-shirt, khaki cargo trousers, brown hiking boots, a necklace of small stream-snail shells.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium shot following the cameraman out onto the porch with a glowing phone, handheld.
- Shot 2, 5–8s: 85mm close-up of the survivalist weaving thin bamboo strips, eyes down, locked off.
- Shot 3, 8–12s: 50mm over-the-shoulder shot from behind the survivalist onto the cameraman crouching beside him.
- Shot 4, 12–15s: 35mm medium two-shot of the two men on the porch step, the limestone peaks glowing behind, slow push-in.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Bin bursts out through the doorway onto the porch, holding up his phone with its blank screen glowing, and is already talking fast.
- 1–2s (Shot 1): @Bin keeps talking rapidly, his eyes huge behind his round glasses, his thumb scrolling the glowing screen.
- 2–3s (Shot 1): @Bin keeps going, thrusting the glowing phone toward @Khang, almost tripping on the porch step.
- 3–4s (Shot 1): @Bin keeps talking fast, half laughing, pressing one hand to the top of his bucket hat.
- 4–5s (Shot 1): @Bin finishes and closes his mouth, panting, holding the phone out at arm's length.
- 5–6s (CUT to Shot 2): @Khang, sitting on the step weaving a small fish trap from bamboo strips, answers without looking up.
- 6–7s (Shot 2): @Khang keeps speaking evenly, threading one thin strip through the woven rim.
- 7–8s (Shot 2): @Khang finishes and closes his mouth, a faint smile at one corner, his eyes on the trap.
- 8–9s (CUT to Shot 3): @Bin crouches beside him, lowers the phone and goes on, a curious grin spreading.
- 9–10s (Shot 3): @Bin keeps talking, pointing at the shell necklace on @Khang's chest, his eyes twinkling behind his glasses.
- 10–11s (Shot 3): @Bin keeps going, scrolling the glowing screen with his thumb, eyebrows high.
- 11–12s (Shot 3): @Bin keeps speaking, leaning in close to study the small shells, his nose almost touching them.
- 12–13s (CUT to Shot 4): @Bin finishes and closes his mouth, waiting with an expectant look, his phone dangling from one hand.
- 13–14s (Shot 4): @Khang's fingers stop on the bamboo strips, mouth closed, as he glances down at the necklace.
- 14–15s (Shot 4): @Khang and @Bin sit side by side on the porch step in the golden light, both silent, the limestone peaks glowing far behind. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–4.9s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, breathless and thrilled): "Khang, three hours, five million views! Nobody's hating on you. People are actually thanking you!"
- Turn 2, 5.4–7.9s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, mild, eyes on his weaving): "Huh. So people watch the truth too."
- Turn 3, 8.4–12.4s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking at a natural, even conversational pace, curious, a sly grin): "And half the comments ask where you bought that shell necklace."
- Pacing: @Bin speaks quickly, then @Khang answers at an even everyday pace, then @Bin answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 12.4s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a screen door banging, quick footsteps on porch boards, bamboo strips rustling, cicadas, a rooster far away. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 23 - Clip 4 (`canh-23/clip-4.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 10s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
The wooden porch of a stilt-house guesthouse at the forest edge today in late afternoon: worn plank steps, potted plants, a smartphone on a small tripod, limestone peaks glowing in the distance.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; plain grey cotton T-shirt, khaki cargo trousers, brown hiking boots, a necklace of small stream-snail shells.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium two-shot on the porch step, holding the previous framing.
- Shot 2, 3–6s: 85mm close-up of the survivalist holding a small shell up to the late sun, locked off.
- Shot 3, 6–10s: 50mm over-the-shoulder shot from behind the survivalist onto the cameraman, locked off.
- Shot 4, 10–15s: 85mm close-up of the survivalist smiling, the limestone peaks soft behind him, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang sets the half-woven trap aside, lifts the shell necklace off his chest and is already speaking slowly, his eyes on the shells.
- 1–2s (Shot 1): @Khang keeps speaking softly, turning one small stream-snail shell to the late golden light.
- 2–3s (Shot 1): @Khang goes on, a far-away look in his eyes, while @Bin watches him with his mouth closed.
- 3–4s (CUT to Shot 2): @Khang keeps speaking quietly, his thumb tracing the spiral of the shell.
- 4–5s (Shot 2): @Khang keeps talking slowly, glancing out toward the distant limestone peaks glowing in the late afternoon sun.
- 5–6s (Shot 2): @Khang finishes and closes his mouth, letting the shell fall back against his T-shirt.
- 6–7s (CUT to Shot 3): @Bin scoots closer beside him and starts talking fast, his eyes wide with curiosity.
- 7–8s (Shot 3): @Bin keeps talking rapidly, nudging @Khang's shoulder with his own, grinning from ear to ear.
- 8–9s (Shot 3): @Bin keeps going, wagging a finger at the necklace, his eyebrows bouncing above his glasses.
- 9–10s (Shot 3): @Bin finishes his demand and closes his mouth, leaning in with his chin propped on one fist, waiting.
- 10–11s (CUT to Shot 4): @Khang smiles to himself, shakes his head slowly and answers in a calm, unhurried voice.
- 11–12s (Shot 4): @Khang keeps speaking, picking up the half-woven fish trap again and threading one bamboo strip.
- 12–13s (Shot 4): @Khang goes on, turning to look at @Bin with a quiet, knowing smile.
- 13–14s (Shot 4): @Khang finishes the last words and closes his mouth, his smile lingering.
- 14–15s (Shot 4): @Khang goes back to weaving the bamboo strips, mouth closed, as the limestone peaks glow in the late sun. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.6s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and soft, far away): "You can't buy it. Someone put it on me, somewhere very far away."
- Turn 2, 6.1–10.0s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, nosy and eager, teasing): "Who? Seven days in the jungle and you got a girlfriend? Tell me!"
- Turn 3, 10.5–14.1s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, smiling, quietly mysterious): "You won't believe me. Take me to the cave tomorrow."
- Pacing: @Khang speaks slowly and calmly, then @Bin answers quickly, then @Khang answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.1s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: bamboo strips creaking, cicadas, a breeze through the potted plants, small shells clicking, a rooster far away. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 24 - Clip 1 (`canh-24/clip-1.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 3s, 6s, 11s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Morning inside the same large limestone cave today: sunlight slanting through the wide arched mouth onto the elephant-shaped stalactite and the wall of hundreds of faded red-ochre hand stencils, the bigger hand in the middle with a smaller hand beside it and a faint charcoal stick figure wearing a square box on its chest.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; plain grey cotton T-shirt, khaki cargo trousers, brown hiking boots, a necklace of small stream-snail shells.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–3s: 35mm medium shot of the cameraman sweeping his flashlight across the wall of faded red hands, handheld.
- Shot 2, 3–6s: 85mm close-up of the cameraman's face beside the faint charcoal stick figure in the flashlight beam, locked off.
- Shot 3, 6–11s: 50mm over-the-shoulder shot from behind the cameraman onto the survivalist, slow push-in.
- Shot 4, 11–15s: 35mm medium two-shot at the wall, the big red hand and the charcoal figure between them, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the shadowed back of the sunlit cave, @Bin sweeps his flashlight over the wall of faded red hands and is already talking fast, pointing.
- 1–2s (Shot 1): @Bin keeps talking excitedly, stepping closer to the big faded hand in the middle of the wall.
- 2–3s (Shot 1): @Bin keeps going, holding the beam on a faint charcoal stick figure right beside the big hand.
- 3–4s (CUT to Shot 2): @Bin keeps talking fast, tracing in the air the little square box with rays on the figure's chest.
- 4–5s (Shot 2): @Bin keeps going, tapping his own chest where a camera harness would sit, his eyes wide behind his glasses.
- 5–6s (Shot 2): @Bin finishes and closes his mouth, turning to @Khang with his eyebrows shooting up, lips pressed together.
- 6–7s (CUT to Shot 3): @Khang steps up beside him, gazing at the charcoal figure, and answers slowly with a soft smile.
- 7–8s (Shot 3): @Khang keeps speaking gently, touching the stream-snail shells at his collar, his eyes on the drawing.
- 8–9s (Shot 3): @Khang goes on, his eyes warm and wet in the slanting sunlight.
- 9–10s (Shot 3): @Khang keeps speaking softly, nodding at the little drawing as if greeting an old friend.
- 10–11s (Shot 3): @Khang finishes and closes his mouth, still smiling at the faint charcoal figure on the wall.
- 11–12s (CUT to Shot 4): @Bin swings the flashlight back to the drawing and blurts out fast, his eyes huge.
- 12–13s (Shot 4): @Bin keeps talking rapidly, glancing between the charcoal figure and @Khang's face.
- 13–14s (Shot 4): @Bin finishes and closes his mouth, his flashlight beam trembling on the rock.
- 14–15s (Shot 4): @Bin stares at the faint charcoal stick figure, mouth closed, while @Khang smiles beside him in silence. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.5s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, excited and rapid, pointing): "Look! By the big hand: a stick man with a box on his chest. Like your camera!"
- Turn 2, 6.0–10.8s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and soft, smiling): "A little boy drew it. So the seeing stone wouldn't be sad."
- Turn 3, 11.3–13.7s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, astonished, blurting it out): "Archaeologists say it's over ten thousand years old!"
- Pacing: @Bin speaks quickly, then @Khang answers slowly and calmly, then @Bin answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.7s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a flashlight click, sneakers scuffing on grit, water dripping, birdsong and cicadas outside the sunlit mouth. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 24 - Clip 2 (`canh-24/clip-2.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Morning inside the same large limestone cave today: sunlight slanting through the wide arched mouth onto the elephant-shaped stalactite and the wall of hundreds of faded red-ochre hand stencils, the bigger hand in the middle with a smaller hand beside it and a faint charcoal stick figure wearing a square box on its chest.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; plain grey cotton T-shirt, khaki cargo trousers, brown hiking boots, a necklace of small stream-snail shells.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot at the wall, holding the previous framing, slow push-in.
- Shot 2, 5–10s: 85mm close-up of the cameraman squinting behind his round glasses, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the cameraman onto the survivalist at the wall.
- Shot 4, 13–15s: 85mm close-up of the survivalist, his fingertips on the smaller faded hand, slow push-in.
- Continuity: continues the same moment, place and lighting as the previous shot; Shot 1 keeps the previous framing axis, no jump.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): @Khang reaches out and rests his fingertips on the smaller faded hand right beside the big one, and is already speaking slowly.
- 1–2s (Shot 1): @Khang keeps speaking softly, his fingertips tracing the faded red outline of the small fingers.
- 2–3s (Shot 1): @Khang goes on, a tender look in his eyes, while @Bin watches him with his mouth closed.
- 3–4s (Shot 1): @Khang keeps talking quietly, his other hand closing around the shells of his necklace.
- 4–5s (Shot 1): @Khang keeps speaking slowly, his voice dropping almost to a whisper, his fingertips still on the rock.
- 5–6s (CUT to Shot 2): @Khang finishes and closes his mouth; @Bin narrows his eyes behind his round glasses and starts answering.
- 6–7s (Shot 2): @Bin keeps talking in a dry, knowing voice, wagging the flashlight at @Khang.
- 7–8s (Shot 2): @Bin keeps going, squinting from the faded wall to @Khang and back, his head tilted skeptically.
- 8–9s (Shot 2): @Bin keeps speaking, folding his arms with a skeptical half-smile, the flashlight tucked under one elbow.
- 9–10s (Shot 2): @Bin finishes and closes his mouth, one eyebrow raised high above his round glasses, waiting.
- 10–11s (CUT to Shot 3): @Khang answers calmly over his shoulder, his fingertips still resting on the small red hand.
- 11–12s (Shot 3): @Khang keeps speaking, shaking his head gently, with no showman's grin, just a quiet calm.
- 12–13s (Shot 3): @Khang goes on, lifting his hand away from the rock and laying it on his chest.
- 13–14s (CUT to Shot 4): @Khang keeps speaking softly, his eyes steady and clear, a faint smile at the corners of his mouth.
- 14–15s (Shot 4): @Khang finishes the last words and closes his mouth, gazing at the two faded hands side by side. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow and tender, remembering): "And this smaller hand, right beside it. That's a girl named Stream."
- Turn 2, 5.7–9.7s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking at a natural, even conversational pace, dry, squinting, unconvinced): "You're acting again, right? Good script, but I'm not buying it."
- Turn 3, 10.2–14.2s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, calm and sure, at peace): "You don't have to. No filming, no posting. Remembering is enough."
- Pacing: @Khang speaks slowly and calmly, then @Bin answers at an even everyday pace, then @Khang answers at an even everyday pace; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 14.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: water dripping from the stalactite, distant birdsong outside, a flashlight buzzing faintly, small shells clicking. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 24 - Clip 3 (`canh-24/clip-3.md`)

```markdown
A 15-second live-action film sequence of 4 shots, 16:9 widescreen, 24 fps, with hard cuts only at 5s, 10s, 13s; one place and one moment, sound and action continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
Morning inside the same large limestone cave today: sunlight slanting through the wide arched mouth onto the elephant-shaped stalactite and the wall of hundreds of faded red-ochre hand stencils, the bigger hand in the middle with a smaller hand beside it and a faint charcoal stick figure wearing a square box on its chest.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Bin = Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; plain grey cotton T-shirt, khaki cargo trousers, brown hiking boots, a necklace of small stream-snail shells.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
Nobody else appears in the shot.

[SHOT LIST — 4 shots, hard cuts only at the marked seconds]
- Shot 1, 0–5s: 35mm medium two-shot at the wall, his palm inside the big red hand, handheld.
- Shot 2, 5–10s: 85mm close-up of the survivalist laughing, locked off.
- Shot 3, 10–13s: 50mm over-the-shoulder shot from behind the survivalist onto the cameraman.
- Shot 4, 13–15s: 24mm wide shot from deep in the cave toward the bright arched mouth, slow pull-back.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.
- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): Distant thunder rolls outside as @Khang rests his palm inside the big faded red hand, a perfect fit, and @Bin jolts and is already shouting.
- 1–2s (Shot 1): @Bin keeps shouting fast, flapping both hands at @Khang's arm, his flashlight beam swinging wildly.
- 2–3s (Shot 1): @Bin takes hold of @Khang's forearm with both hands, still talking fast, and tugs it away from the wall.
- 3–4s (Shot 1): @Bin keeps going breathlessly, his eyes darting to the bright cave mouth as the thunder rumbles again.
- 4–5s (Shot 1): @Bin keeps talking rapidly, pulling @Khang a step back from the wall of hands.
- 5–6s (CUT to Shot 2): @Bin finishes and closes his mouth, panting; @Khang bursts out laughing and starts answering.
- 6–7s (Shot 2): @Khang keeps talking through his laughter, his free hand on @Bin's shoulder.
- 7–8s (Shot 2): @Khang keeps speaking, his laugh settling into a warm grin as he glances at the wall.
- 8–9s (Shot 2): @Khang goes on, nodding toward the big red hand with quiet certainty.
- 9–10s (Shot 2): @Khang keeps speaking gently, the shell necklace swinging at his chest as he turns back to @Bin.
- 10–11s (CUT to Shot 3): @Khang finishes and closes his mouth, still smiling, while @Bin stares at him, blinking.
- 11–12s (Shot 3): @Bin flings both hands up and fires back fast, his glasses askew.
- 12–13s (Shot 3): @Bin keeps going, jabbing a finger at @Khang's chest, demanding an answer, his voice cracking high.
- 13–14s (CUT to Shot 4): @Bin finishes and closes his mouth, glaring at @Khang through his crooked glasses, his chest heaving.
- 14–15s (Shot 4): @Khang grins and walks toward the sunlit cave mouth, mouth closed, while @Bin hurries after him, both silent. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, three spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–5.2s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, panicking, rapid and shrill): "Whoa! Thunder! Take your hand off! Last time you touched that, you vanished for seven days!"
- Turn 2, 5.7–10.4s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking at a natural, even conversational pace, laughing, teasing, then gentle): "Scared I'll vanish? Over there, they have fire now. They don't need me."
- Turn 3, 10.9–13.3s, spoken on camera by @Bin (young man of 24, light dry voice, deadpan and teasing, speaking quickly in short lively phrases, every word still clear, fast, demanding answers): "Over where? Explain that to me right now!"
- Pacing: @Bin speaks quickly, then @Khang answers at an even everyday pace, then @Bin answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.3s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: a long low roll of distant thunder, sneakers scuffing on grit, a flashlight knocking against stone, birdsong falling quiet outside. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, a change of location, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```

---

## Cảnh 24 - Clip 4 (`canh-24/clip-4.md`)

```markdown
A 15-second live-action film sequence of 5 shots, 16:9 widescreen, 24 fps, with hard cuts only at 4s, 8s, 11s, 13s; it intercuts the two places or times named in the shot list, each shot keeping its own place and light, with sound continuous across the cuts.

[STYLE]
Photorealistic live-action survival adventure film with warm humor, set in the limestone jungles of northern Vietnam today and more than ten thousand years ago; lush natural greens, wet limestone greys, ember-orange firelight, natural skin texture with sweat and dirt, subtle 35mm film grain, shallow depth of field, grounded handheld energy.

[LIGHTING]
Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.

[LOCATION]
The same limestone cave mouth with the elephant-shaped stalactite in two times: today in bright morning sun with the wall of faded red hand stencils, and more than ten thousand years ago at night, lit by a hearth fire with the clan sitting around it and two fresh red hand stencils on the wall.

[CHARACTERS]
Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.
- @Khang = Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; plain grey cotton T-shirt, khaki cargo trousers, brown hiking boots, a necklace of small stream-snail shells.
- @Snail = Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.
- Wardrobe: in this shot @Khang wears the outfit written above, not the outfit in the reference image; face and hair stay identical.
- Extra: in the night shots long ago only, the Stone Age clan in bark-cloth tunics and hide wraps sits around the hearth watching the boy, in soft focus
Nobody else appears in the shot.

[SHOT LIST — 5 shots, hard cuts only at the marked seconds]
- Shot 1, 0–4s: 50mm medium shot of the survivalist standing in the sunlit cave mouth today, a phone held up in the foreground, slow push-in.
- Shot 2, 4–8s: 85mm close-up of the survivalist today in the morning sun, fingers on his shell necklace, locked off.
- Shot 3, 8–11s: 35mm medium shot of the boy by the hearth fire at night long ago, holding up his flat holed stone, handheld.
- Shot 4, 11–13s: 50mm over-the-shoulder shot long ago at night, from behind the seated clan onto the boy at the hearth, slow push-in.
- Shot 5, 13–15s: 100mm extreme close-up of the two red hand stencils on the rock wall, fresh in firelight long ago, then faded in sunlight today, locked off.
- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.
- Each shot keeps the lighting of its own place and time; faces, wardrobe and props stay consistent; whoever is speaking has the face clearly on screen in that shot.

[TIMELINE — second by second]
Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn.
- 0–1s (Shot 1): In the sunlit mouth of the cave today, @Khang faces a phone held up by an unseen hand and is already speaking slowly and plainly.
- 1–2s (Shot 1): @Khang keeps speaking, today's morning light on his face, the green limestone jungle bright behind him.
- 2–3s (Shot 1): @Khang goes on quietly, his eyes steady on the phone, with no showman's grin.
- 3–4s (Shot 1): @Khang keeps speaking, lifting one hand to rest his fingers on the stream-snail shells at his collar.
- 4–5s (CUT to Shot 2): @Khang keeps talking slowly, rolling one small shell between his fingers, his eyes shining.
- 5–6s (Shot 2): @Khang goes on, glancing back over his shoulder toward the faded wall of red hands deep in today's cave.
- 6–7s (Shot 2): @Khang keeps speaking, his voice catching slightly, a small grateful smile forming.
- 7–8s (Shot 2): @Khang finishes the last words and closes his mouth, breathing out, the sun warm on his face.
- 8–9s (CUT to Shot 3): More than ten thousand years ago at night, @Snail stands by the hearth fire, raises his flat stone with a hole to his face and starts shouting brightly.
- 9–10s (Shot 3): Long ago at night, @Snail keeps talking fast, beaming, pointing the flat stone at the clan seated around the fire.
- 10–11s (Shot 3): Long ago by the hearth, @Snail keeps going, lifting a split bamboo tube and a notched bamboo strip from the ground.
- 11–12s (CUT to Shot 4): Long ago at night, @Snail keeps shouting with joy, sawing the strip across the bamboo once to show the seated clan.
- 12–13s (Shot 4): Long ago by the firelight, @Snail keeps talking, thrusting the flat stone high, his snail-shell bracelet rattling on his wrist.
- 13–14s (CUT to Shot 5): Long ago at night, firelight flickers over the two fresh red hands side by side on the rock wall, one big and one smaller, as the boy falls silent.
- 14–15s (Shot 5): Today, soft morning sunlight replaces the firelight on the very same two hands, now faded with age, still side by side. The sequence settles on this as its final frame.

[AUDIO]
- Dialogue in English with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):
- Turn 1, 0.4–7.6s, spoken on camera by @Khang (man of 29, bright energetic tenor, a showman's voice that drops low and honest when serious, speaking slowly and softly, unhurried, with a short natural pause between phrases, slow, plain and grateful, no performance): "I can't survive anywhere. I survived because someone shared their snails with me, and someone held my rope."
- Turn 2, 8.1–13.2s, spoken on camera by @Snail (boy of 8, high bright child's voice, quick and excited, speaking quickly in short lively phrases, every word still clear, radiant, shouting with joy): "Hello everyone! Today I teach the cave bamboo fire, like Fire taught me! I can survive anywhere!"
- Pacing: @Khang speaks slowly and calmly, then @Snail answers quickly; the change of speed is clearly audible.
- Throughout, each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.
- Voices: everyone speaks clear, natural English with a neutral international accent, says each word once and clearly, and keeps one consistent voice that is clearly different from every other character in pitch, age and texture.
- All speech is over by 13.2s. From then until 15.0s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.
- Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.
- SFX: birdsong and a soft morning breeze at the cave mouth, then a crackling hearth fire at night, bamboo rasping on bamboo, small bare feet on stone. Ambience continues to 15.0s. No music.

[AVOID]
On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, background music, letterbox bars, cuts at any moment other than the planned shot changes, jump cuts, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, mumbled or swallowed words, an off-screen narrator or voice-over, garbled or invented words, words in any language other than English.
```
