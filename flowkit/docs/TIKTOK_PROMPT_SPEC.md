# TikTok episode prompt spec (Google Flow, Gemini Omni Flash, 10 s clips, 9:16)

Repo: /Users/iseul-a/Documents/TikTokSeries. The user is a Vietnamese TikTok creator; each episode = 6 clip files
`clip-1.md … clip-6.md`, each the full prompt sent to Flow for one 10-second clip. The runner renders EVERY clip
independently in Ingredients mode (character reference images, no start frame), so the prompt text is the only
continuity between clips. Do not change that.

## What was measured (why we rewrite)
- Dialogue is far too dense: many clips cram 45–70 Vietnamese syllables into 10 s (6–8.7 syllables/s inside a
  segment). Omni then rushes, slurs or cuts lines and the lip-sync drifts. Comfortable is ≤ 4.2 syllables/s.
- Clock digits in the text ("Time: 06:31 PM", "09:45") make Omni paint clocks/numbers on screen.
- Voice descriptions vary from line to line, so the same character changes voice between clips.
- Characters are declared in clips where they do not appear, so the model adds them.
- (365ngayvietnam) the file starts with a markdown title line, carries a research/verification section, and repeats
  every dialogue line twice (body + table) — the model may speak lines twice or read Vietnamese directions aloud.

## Hard rules for every rewritten clip
1. Keep the series' look and rules: copy the series' current `[FORMAT]` block verbatim from the episode you are
   fixing (or the series' newest good episode), only removing clock digits/markdown. Make sure it contains the
   clean-frame sentence: "Clean frame: no channel or station logo, no corner bug, no lower-third, no timestamp,
   no REC or LIVE badge, no news ticker." (add it if missing).
2. `[CHARACTERS — match the attached reference images @A @B]`: list ONLY the characters who are visible in this
   clip. Each named lead on its own line starting `@Tag = …` (exact tag spelling used by the series, e.g. `@Mit`,
   `@Đú`, `@Nở`, `@Pheo`, `@No`, `@Thay`, `@DaiCa`, `@HeoLuoi`, `@UtKho`, `@Ngoc`, `@Gao`, `@Bong`, `@Vy`, `@Joi`).
   Copy the series' anchor text verbatim. Each character has ONE fixed `Voice:` string — identical in every clip of
   the episode. Untagged supporting characters (e.g. HÙNG, LA SÁT) get one line without `@` and only in clips where
   they appear. Never mention an absent tagged character anywhere in the prompt (not even in AVOID) — the runner
   attaches a reference image for every tag it finds.
3. Location lock: one `[SET LOCK — Tập NN, identical in all clips at this location]` block per location, pasted
   word-for-word in every clip at that location: the place, time of day IN WORDS (no digits), light direction,
   which side the camera stands, a left/centre/right/foreground layout, seat/standing positions. If the episode
   changes location, each location gets its own block, reused verbatim.
4. `[CHARACTER STATE IN THIS CLIP]` (outfit/hair/feet/what is on the head, injuries) and
   `[PROPS IN THIS CLIP — exact list, nothing else]` — short; each prop has one description string reused word for
   word across clips.
5. `[SHOT LIST]` — keep the series' convention (Mít & Đú / Phèo / Mẹ & Bé / 365: ONE CONTINUOUS SHOT;
   Tây Du Ký: may cut only where the shot list says). 2–3 timed segments `00:00–00:04.0 | …`.
   Dialogue rules (the core fix):
   - at most 2 speaking turns per clip (3 only if each ≤ 8 syllables);
   - each turn sits in its own segment, one speaker per segment, written in the series' format
     `@Nở says (<that character's exact Voice string>; <emotion>): <Vietnamese line>` — the line is NOT in quotes
     (series convention: spoken only, never shown as text);
   - syllables of the turn ÷ segment duration ≤ 4.2 (hard limit 4.4); total spoken syllables per clip ≤ 36;
   - the speaker's face is visible while speaking; everyone else keeps their mouth closed;
   - accent (user rule 07/11/2026): Mít & Đú keeps natural Southern Mekong speech; Phèo, Mẹ & Bé, Tây Du Ký and
     365 Ngày speak "giọng Bắc thanh thoát" — FORMAT says "a soft, clear, elegant standard Northern Vietnamese
     (Hà Nội) accent", every Voice string ends with "elegant standard Hà Nội Northern Vietnamese accent", AVOID lists
     "Southern or Central Vietnamese accents", and the wording is Northern (này/đây, nhé, không, vào, thật, quá/thế,
     thìa, bát, cốc, lợn, đắt — never nè, nghen, hông, vô, thiệt, ghê, muỗng, chén, ly, heo, mắc);
   - correct grammar and meaning, same story beat — shorten, do not change the plot. Babies (Mẹ & Bé) never speak words.
   - Mít & Đú: each episode is one countryside story; food is at most a side detail, not every episode a recipe.
   - Fewer actions per clip: what is shown must physically fit its segment.
6. No clock digits or "AM/PM", no hex colour codes, no markdown (`#`, `**`, tables), no research/verification
   notes, no product prices; each dialogue line appears exactly once in the prompt. Product codes the series uses in
   backticks (`SP_TAP`, `SP_BUTMAU`, `SP_DIU_VAI`, …) stay as they are.
7. Safety: no contact violence (no slapping, grabbing, shoving, pinning, dragging, fighting, weapons pointed at
   people); avoid fight words even in camera notes ("action shot", "kinetic"). Keep the series' child/baby safety
   rules (no child near fire, baby head/neck supported, face uncovered).
8. Section order: [FORMAT] [CHARACTERS…] [SET LOCK…] [CHARACTER STATE IN THIS CLIP] [PROPS IN THIS CLIP…]
   [BLOCKING] (optional) [SHOT LIST…] [SOUND] [END FRAME] [AVOID]. `[AVOID]` MUST be the last section (the runner's
   retry sanitizer replaces everything from [AVOID] to the end). Keep AVOID in the series' style; drop items that
   name absent tagged characters.
9. Length: aim 4,000–9,000 characters per clip (SET LOCK episodes may reach ~10,500); cut repetition, keep the anchors.
10. If you change dialogue, update the same lines wherever the episode README.md/caption.md quote them, so docs and
    prompts agree. Do not touch other episodes, runners, the database, git, or files outside your episode folder(s).

## Natural speech (user, 10/11/2026: "còn nhiều tình tiết với giọng bị lặp lại… mọi thứ phải tự nhiên hơn")
- Each clip moves the story on; never restate what the previous clip already said, and cap any content phrase at two uses per episode (a running gag word may appear once more as the punchline).
- People do not say their own name ("Ngày nào cũng Heo Lười giữ lửa" → "Ngày nào cũng em giữ lửa"); a series catchphrase that uses a nickname ("Để Đại Ca!") at most once per episode.
- Speak like people, not like a recipe card: Phèo says one or two quantities per turn in a casual sentence ("Một thìa dầu hào, chút đường, ướp mười lăm phút là thấm"); the full list stays in the README and caption. Never chop one turn into a string of bare fragments.
- Vary the emotion/speed slot: the same character never gets the same tag ("steady medium pace") in two clips in a row; fast for gags and panic, slow for the warm or sad beat.
- 10-second clips: keep 18–34 syllables. Renders on 10/11 showed lines spoken exactly once at this density, while 15-second film clips with only about 30 syllables made Omni repeat the line to fill the time.

## Self-check (run before you finish)
`python3 flowkit/scripts/check_tiktok_episode.py <episode dir>`
It must print OK for all 6 clips (no ERROR lines). Then reread each clip once as the model would: one coherent
10-second shot, every line timed, nothing contradictory between clips.

Report back (concise): per clip the old → new dialogue (syllables and seconds), what else you changed and why, any
story problems you found and how you fixed them, and anything you were unsure about.
