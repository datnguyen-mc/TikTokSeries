# Spec: filling a skeleton part into a shot-by-shot part (Seven Days in the Stone Age)

Input: `_parts/skeleton_pK.json` (list of scenes). Output: `_parts/part_pK.json`, same structure, every clip completed.
Story and characters: `../CAU_CHUYEN.md`. Director's notes per clip (Vietnamese): the `_hinh` field, copied from `_parts/DAN_Y.md`.
The builder that turns this into Flow Omni prompts: `flowkit/scripts/build_omni_horror_prompts.py` (read `render_prompt`, `validate`, `validate_shots`).
A finished example of the format (Vietnamese film, same builder): clips 01.1 and 01.2 in `cai-ket-cho-tieu-tam/PHAN_CANH_OMNI.json`.

## Keep verbatim from the skeleton
`id`, `chars`, every turn's `speaker` / `line` / `pace`, the scene `setting` and any clip `setting`, `wardrobe`, scene `num` / `title` / `time_label` / `location`. Underscore keys (`_plan`, `_hinh`, `_tone_vi`, `_setting_key`) may stay; they are stripped at merge.

## Add to every scene
- `axis`: one Vietnamese sentence fixing camera geography (where the camera stands, what is left/right/far).
- `props`: one Vietnamese sentence listing the key props.

## Add to every clip
- `tone` on each turn: short English delivery note, at most 60 characters, no digits, no quotes, no @tags (translate/adapt `_tone_vi`).
- `continuity`: `"cut"`, or `"continuous"` only when the previous clip of the same scene has the same setting, this clip's chars are a subset of the previous clip's chars, and the moment continues directly. The first clip of a scene is always `"cut"`.
- `sfx`: concrete diegetic sound and ambience in English, no @tags, never the words music, melody or flute.
- `shots`: 3–5 objects `{"until": <int second>, "camera": "<lens> <shot size> of <subject>, <one move>"}`; cuts on whole seconds, each shot at least 2 s, last `until` is 15. Every camera text names a shot size (extreme close-up, close-up, medium, over-the-shoulder, wide, aerial); two shots in a row must not share the same size. Put cuts at turn changes where possible; the speaker's face must be on screen in the shot covering their words.
- `steps`: exactly 15 English sentences, step k describes second k–k+1. One concrete physical action per second, present tense.
  - Follow `_plan` (speech windows the builder will print). Speech starts at 0.4 s: **step 0 must contain the first speaker's @tag and a speaking verb** (e.g. "is already speaking", "says", "asks", "answers", "whispers", "shouts").
  - During a turn, steps show that speaker talking (face visible). The listener keeps the mouth closed. When a turn ends write that the speaker finishes and closes the mouth. After the last turn ends, the remaining seconds are silent reactions ("mouth closed").
  - Only tags listed in `chars` may appear anywhere in steps, cameras, setting or extras. A non-speaking named character can only appear untagged and unidentifiable (a hand, a back in soft focus) or not at all.
- `extras` (optional): crowd of untagged people, e.g. "a few clan members in bark-cloth tunics and hide wraps sit around the hearth in soft focus". Use only where the crowd matters (the builder warns ">2 people", which is accepted for those clips).

## Hard content rules (Flow blocks or the builder rejects)
- Banned words anywhere in steps / cameras / extras: slap, punch, strike, kick, strangle, choke, pinned, grab, seize, lunge, attack, fight, sword, weapon, gun, knife, blade, blood, gore, gouge, violent, blast, thrown, throat, convulse, kinetic, action. Use "multitool" not knife, "takes hold of" not grab, "tossed" not thrown, "whistle blows" not blasts.
- No abstract emotion words in steps (terrified, scared, afraid, frightened, horrified, petrified, shocked, startled, sad, anxious, nervous, guilty, angry, happy): show breathing, eyes, jaw, hands, posture.
- No digits in visual text (no clock times, no "4 meters").
- No readable text anywhere: phone and camera screens only glow.
- Stone Age people are always covered from shoulders to knees (bark-cloth tunics, hide wraps); nobody is bare-chested, children included.
- No violence on screen: no animal is hurt or killed; the tiger stays on the far bank and walks away; the rhino only drinks and leaves; a spear is held upright or across the body, never pointed at a person; injuries are a swollen ankle and blistered palms, no wounds.
- Flood: water reaches at most Khang's thighs; Snail is always above the water (on a pillar ledge, on Khang's shoulders, on the boulder), head and shoulders dry; nobody is swept away — only branches and the camera drift off.
- Present-day scenes (01–03.3, 22–24) and Stone Age scenes never mix objects, except Khang's own gear in the past. Clips 17.2 and 24.4 are cross-cuts inside one clip: 17.2 alternates the flooded lower cave (Snail) and the cliff above (Khang roping down) in the same night; 24.4 alternates today's sunlit cave mouth (Khang) and the same cave by night long ago (Snail by the hearth), ending on the red hands.

## Style of the writing
Cinematic and specific: lens (24/35/50/85mm), size, one move (push-in, slow pan, handheld follow, locked off, tilt). Steps 12–30 words, active verbs, concrete props from the scene. Keep the comedy readable through physical business (Bin's deadpan, Khang's showman gestures, Snail's wide eyes). Keep each character's look consistent with `_parts/header.json` anchors and the clip's `wardrobe`.

## Check before finishing
`python3 bay-ngay-sinh-ton/_parts/check_part.py K` from the repo root must print 0 errors. Fix every warning except ">2 people" on crowd clips; mention any warning you keep and why.
