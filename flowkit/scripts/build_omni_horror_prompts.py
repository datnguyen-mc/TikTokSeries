#!/usr/bin/env python3
"""Compile a series' PHAN_CANH_OMNI.json (N scenes × 6 clips × 10s) into Google Flow Omni prompts.

Used by can-nha-am-duong, tieng-go-dem-ba-gio, ma-da-dam-sen (15 scenes), gang-to-tai-xuat (27 scenes × 4 × 15s)
cai-ket-cho-tieu-tam (25 scenes × 4 × 15s) and bay-ngay-sinh-ton (24 scenes × 4 × 15s, English).

    python3 flowkit/scripts/build_omni_horror_prompts.py can-nha-am-duong          # validate + write
    python3 flowkit/scripts/build_omni_horror_prompts.py tieng-go-dem-ba-gio --check # validate only

The JSON is the single source of truth. This script writes canh-NN/clip-N.md,
canh-NN/README.md, KICH_BAN_<N>_PHUT.md (N = clips × 10s / 60), FLOW_PROMPTS.md and
the clip table of README.md. After writing, sync flow_agent.db (cms_clip.prompt) or the CMS UI
will write its stale copy back over the clip files.

Prompt rules (Omni works best with short, concrete prompts):
- reference images carry identity, so characters get one short anchor line;
- one camera move, three timed beats, one spoken line with its own window;
- VO clips carry only the narrator voice, lip-sync clips only the speaker's voice;
- no meta text (model names, media ids, clip numbers, clock digits) that Omni
  could paint on screen; the AVOID block stays last because the runner's retry
  sanitizer replaces everything from [AVOID] to the end.

Optional per-series / per-clip fields (10/11/2026):
- no "narrator" block → dialogue-only film: a NARRATOR clip is an error;
- "pace" (fast / normal / slow) and "tone" on each turn (or on a speaker+line clip):
  the pace phrase follows the character's fixed voice and sets the syllable rate,
  so the speech window grows for slow lines; once one turn has a pace, all must;
- "wardrobe": {"@Tag": "outfit"} replaces the outfit part of that anchor for one clip.

Optional "language" (12/11/2026, user: phim nhắm khán giả toàn cầu, thoại tiếng Anh, YouTube lo phụ đề):
"vi" (default) or "en". With "en" the prompts ask for English dialogue, word counts replace syllable
counts, and each character's "rate" is in words per second (about 2.8 until measured with Whisper).
- One speaker may hold several turns in a row when the pace changes (a monologue that starts in a
  whisper and speeds up); the prompt then asks for one speaker in parts with a breath between them.
- "intercut": true on a multi-shot clip that cuts between two places or two times (named per shot);
  the prompt then drops "one place and one moment" and lets each shot keep its own light.
"""
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEECH_START = 0.4
CONTINUOUS_MARK = "Continuity: continues the same moment, place and lighting as the previous shot"

BANNED_VISUAL = [  # contact-violence / gore words that make Flow block or time out
    r"\bslap", r"\bpunch", r"\bstrik(e|es|ing)\b", r"\bkick", r"\bstrangl", r"\bchok(e|es|ing)\b",
    r"\bpinned\b", r"\bgrab", r"\bseiz", r"\blunge", r"\battack", r"\bfight", r"\bsword", r"\bweapon",
    r"\bgun\b", r"\bknife", r"\bblade", r"\bblood", r"\bgore", r"\bgoug", r"\bviolent", r"\bblast",
    r"\bthrown\b", r"\bthroat", r"\bconvuls", r"\bkinetic", r"\baction\b", r"\bsnapped sideways",
]
CLOCK_DIGITS = re.compile(r"\b\d{1,2}[:.]\d{2}\b|\b\d{1,2}\s?(AM|PM)\b")
TAG = re.compile(r"@[A-Za-z]\w*")


SPEAKING = re.compile(r"\b(speak|speaks|speaking|says|saying|asks|asking|tells|telling|whispers|whispering|shouts|shouting|calls out|answers|replies|mutters|muttering|talks|talking|lips move|mouth moves|voice)\b", re.I)
ABSTRACT_EMOTION = re.compile(r"\b(terrified|scared|afraid|frightened|horrified|petrified|shocked|startled|sad|anxious|nervous|guilty|angry|happy)\b", re.I)


def shot_scale(camera: str) -> str:
    cam = camera.lower()
    for k in ("extreme close-up", "macro", "close-up", "over-the-shoulder", "medium", "wide", "aerial"):
        if k in cam:
            return k
    return ""


def syllables(text: str) -> int:
    """Vietnamese syllables, or English words (an apostrophe keeps "don't" as one word)."""
    return len([w for w in re.split(r"\s+", re.sub(r"[^\w'À-ỹ\s]", " ", text)) if w.strip("'")])


def speech_window(line: str, rate: float, start: float = SPEECH_START, max_end: float = 8.6) -> tuple[float, float]:
    end = start + syllables(line) / rate
    return start, round(min(end, max_end) + 0.049, 1)


# Clip length (09/11/2026): Omni 1.2 Flash renders up to 15s. A series opts in with
# "clip_seconds": 15 in PHAN_CANH_OMNI.json; without it everything stays 10s / 3 beats.
BEAT_WINDOWS = {
    10: [(0.0, 3.0), (3.0, 7.0), (7.0, 10.0)],
    15: [(0.0, 3.0), (3.0, 7.0), (7.0, 11.0), (11.0, 15.0)],
}
TURN_GAP = 0.5  # pause between two speakers inside one clip

# Nhịp giọng theo cảnh (10/11/2026, user: "giọng phải nhanh chậm tuỳ cảnh"): pace → (hệ số rate, nhãn, câu mô tả).
# Câu mô tả nối sau giọng cố định của nhân vật; giọng gốc giữ nguyên văn để Omni không đổi người nói.
# Hệ số đo lại từ bản render 10/11/2026 (Whisper): câu "slow" thực tế ra 2,5–4 âm tiết/giây, không phải 2,9 → 0.8.
PACES = {
    "fast": (1.2, "nhanh", "speaking quickly in short lively phrases, every word still clear", "quickly"),
    "normal": (1.0, "vừa", "speaking at a natural, even conversational pace", "at an even everyday pace"),
    "slow": (0.9, "chậm", "speaking slowly and softly, unhurried, with a short natural pause between phrases", "slowly and calmly"),
}
MIN_SYLLABLES_15S = 46  # dialogue-only 15s clips: Omni talks from 0s at ~3.5–4.5 syll/s; fewer words leave dead air it fills by repeating a line
# Per-language wording and word budgets. "en" budgets are provisional (bay-ngay-thoi-do-da, 12/11/2026): ~2.8 words/s.
LANGS = {
    "vi": {"name": "Vietnamese", "unit": "âm tiết", "min_15s": MIN_SYLLABLES_15S, "single_15s": (36, 56),
           "speak": "Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.",
           "accent_avoid": "Southern or Central Vietnamese accents", "voice_note": "tuổi, chất giọng, giọng Hà Nội"},
    "en": {"name": "English", "unit": "từ", "min_15s": 32, "single_15s": (25, 38),
           "speak": "Speak only the English words inside the double quotes, once, in clear natural English; never read these directions, names or tags aloud.",
           "accent_avoid": "garbled or invented words, words in any language other than English", "voice_note": "tuổi, chất giọng"},
}


def lang(data: dict) -> dict:
    return LANGS[data.get("language", "vi")]
SPEECH_AVOID = {  # chỉ cấm kiểu đọc ngược với nhịp của clip
    "fast": "slow or drawn-out delivery, mumbled or swallowed words",
    "normal": "rushed delivery, slow drawn-out delivery or long pauses inside a sentence",
    "slow": "rushed or hurried delivery",
}


def clip_seconds(data: dict) -> int:
    d = int(data.get("clip_seconds", 10))
    if d not in BEAT_WINDOWS:
        raise SystemExit(f"clip_seconds must be one of {sorted(BEAT_WINDOWS)}, got {d}")
    return d


def soft_end(D: int) -> float:
    """VO and old-style continuous dialogue must finish by here (10s → 8.6s)."""
    return D - 1.4


def hard_end(D: int) -> float:
    """Lip-sync that starts late (cut clip / speech_start) may run to here (10s → 9.4s)."""
    return D - 0.6


def turns(c: dict) -> list[dict]:
    """Spoken turns of a clip. 15s clips may hold two character turns in "turns";
    every other clip has the classic single "speaker" + "line" (+ optional "pace"/"tone")."""
    if c.get("turns"):
        return c["turns"]
    t = {"speaker": c["speaker"], "line": c["line"]}
    for k in ("pace", "tone"):
        if c.get(k):
            t[k] = c[k]
    return [t]


def is_vo(c: dict) -> bool:
    return turns(c)[0]["speaker"] == "NARRATOR"


def turn_rate(data: dict, t: dict) -> float:
    if t["speaker"] == "NARRATOR":
        return data["narrator"]["rate"]
    rate = data["characters"][t["speaker"]]["rate"]
    return rate * PACES[t["pace"]][0] if t.get("pace") else rate


def turn_voice(data: dict, t: dict) -> str:
    """Fixed character voice, then this turn's pace phrase and tone."""
    v = data["characters"][t["speaker"]]["voice"]
    if t.get("pace"):
        v += ", " + PACES[t["pace"]][2]
    if t.get("tone"):
        v += ", " + t["tone"]
    return v


def pace_label(c: dict) -> str:
    """'chậm' or 'nhanh → chậm' for tables; '' when the clip has no pace."""
    labels = [PACES[t["pace"]][1] for t in turns(c) if t.get("pace")]
    return " → ".join(labels)


def has_paces(data: dict) -> bool:
    return any(t.get("pace") for sc in data["scenes"] for c in sc["clips"] for t in turns(c))


def speech_avoid(data: dict, c: dict) -> str:
    """Delivery faults for [AVOID]: legacy text without pace, otherwise only what fights this clip's pace."""
    paces = sorted({t["pace"] for t in turns(c) if t.get("pace")})
    if not paces:
        s = "slow drawn-out narration or long pauses inside a sentence"
    elif len(paces) == 1:
        s = SPEECH_AVOID[paces[0]]
    else:
        s = "mumbled or swallowed words"
    return s if "narrator" in data else s + ", an off-screen narrator or voice-over"


def talks_from_start(c: dict) -> bool:
    """Multi-shot dialogue clip (steps) without a narrator block in the series: speech starts at 0.4s.
    Render 10/11/2026 (Whisper word times): Omni starts talking at 0.0s even when told to wait for 3s,
    finishes early and repeats the last phrase, so the plan must match what Omni really does."""
    return bool(c.get("steps")) and c.get("_dialogue_only", False)


def speech_start_for(c: dict, cont: str) -> float:
    if is_vo(c) or talks_from_start(c):
        return SPEECH_START
    if cont != "continuous":
        return 3.0
    return float(c["speech_start"]) if c.get("speech_start") else SPEECH_START


def speech_plan(data: dict, c: dict, cont: str, D: int, clamp: bool = True) -> list[tuple[str, str, float, float]]:
    """(speaker, line, start, end) per turn, back to back with TURN_GAP between them."""
    t = speech_start_for(c, cont)
    late = (not is_vo(c)) and (cont != "continuous" or bool(c.get("speech_start")) or talks_from_start(c))
    limit = (hard_end(D) if late else soft_end(D)) if clamp else 99.0
    plan = []
    for tr in turns(c):
        a, b = speech_window(tr["line"], turn_rate(data, tr), start=t, max_end=limit)
        plan.append((tr["speaker"], tr["line"], a, b))
        t = round(b + TURN_GAP, 1)
    return plan


def line_text(c: dict) -> str:
    """Spoken text for tables: one line, or '@A: … / @B: …' for two turns."""
    ts = turns(c)
    if len(ts) == 1:
        return ts[0]["line"]
    return " / ".join(f"{t['speaker']}: {t['line']}" for t in ts)


def mode_label(c: dict) -> str:
    if is_vo(c):
        return "VO"
    return "LIPSYNC:" + "+".join(t["speaker"] for t in turns(c))


def effective_continuity(clips: list[dict], i: int, scene_setting: str) -> str:
    """Chain from the previous clip's last frame only when nothing new must be introduced."""
    c = clips[i]
    if i == 0 or c.get("continuity") != "continuous":
        return "cut"
    prev = clips[i - 1]
    if not c["chars"] or not prev["chars"]:
        return "cut"
    if not set(c["chars"]) <= set(prev["chars"]):
        return "cut"  # a newcomer needs its reference image (Ingredients mode)
    if c.get("setting", scene_setting) != prev.get("setting", scene_setting):
        return "cut"
    return "continuous"


def flow_mode(c: dict, cont: str) -> str:
    if cont == "continuous":
        return "Frames: nối khung cuối clip trước"
    if c["chars"]:
        return "Ingredients: ảnh nhân vật"
    return "Text-to-video"


# Clip nhiều cảnh quay (10/11/2026, user: "clip 15 s thì các cảnh phải nhiều hơn, quy định các step từ 1 tới 15 giây rõ ràng"):
# opt-in bằng "shots" (mỗi shot có "camera" và giây kết thúc "until") + "steps" (đúng một câu cho mỗi giây).
def shot_spans(c: dict) -> list[tuple[int, int, str]]:
    """(start, end, camera) of each shot in a multi-shot clip."""
    spans, t = [], 0
    for s in c["shots"]:
        spans.append((t, int(s["until"]), s["camera"]))
        t = int(s["until"])
    return spans


def visual_lines(c: dict) -> list[str]:
    return c.get("steps") or c["beats"]


def cameras(c: dict) -> list[str]:
    return [s["camera"] for s in c["shots"]] if c.get("shots") else [c["camera"]]


def render_prompt(data: dict, scene: dict, c: dict, cont: str) -> str:
    chars = data["characters"]
    setting = c.get("setting", scene["setting"])
    # Thứ tự theo "Prompt Ingredients" của hướng dẫn Omni 1.2 (EvoLinkAI): Style → Lighting → Location →
    # Shot framing & motion → Action; lời nói trong ngoặc kép, phần cấm (negative) để cuối.
    D = clip_seconds(data)
    spans = shot_spans(c) if c.get("steps") else []
    if spans:
        cuts = ", ".join(f"{a}s" for a, _, _ in spans[1:])
        if c.get("intercut"):
            lines = [f"A {D}-second live-action film sequence of {len(spans)} shots, 16:9 widescreen, 24 fps, with hard cuts only at {cuts}; it intercuts the two places or times named in the shot list, each shot keeping its own place and light, with sound continuous across the cuts.", ""]
        else:
            lines = [f"A {D}-second live-action film sequence of {len(spans)} shots, 16:9 widescreen, 24 fps, with hard cuts only at {cuts}; one place and one moment, sound and action continuous across the cuts.", ""]
    else:
        lines = [f"One continuous {D}-second live-action shot, 16:9 widescreen, 24 fps.", ""]
    lines += ["[STYLE]", data["style"], ""]
    if data.get("lighting"):
        lines += ["[LIGHTING]", data["lighting"], ""]
    lines += ["[LOCATION]", setting, ""]

    lines.append("[CHARACTERS]")
    wardrobe = c.get("wardrobe") or {}
    if c["chars"]:
        if cont == "continuous":
            lines.append("Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.")
        elif talks_from_start(c):
            lines.append("Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card; the characters are already in place in the very first frame.")
        else:
            lines.append("Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.")
        for t in c["chars"]:
            anchor = chars[t]["anchor"]
            if wardrobe.get(t):  # the outfit is the last "; " part of every anchor
                anchor = "; ".join(anchor.split("; ")[:-1] + [wardrobe[t].rstrip(".") + "."])
            lines.append(f"- {t} = {anchor}")
        changed = [t for t in c["chars"] if wardrobe.get(t)]
        if changed:
            one = len(changed) == 1
            lines.append(f"- Wardrobe: in this shot {' and '.join(changed)} {'wears the outfit' if one else 'wear the outfits'} written above, not the outfit in the reference image; {'face and hair stay' if one else 'faces and hair stay'} identical.")
        if c.get("extras"):
            lines.append(f"- Extra: {c['extras']}")
        lines.append("Nobody else appears in the shot.")
    else:
        if c.get("extras"):
            lines.append(f"- Extra: {c['extras']}")
            # Không ghi "no other people" khi có quần chúng — câu đó tự mâu thuẫn và khiến Omni xoá đám đông.
            lines.append("No named characters appear in this shot; the extras above are the only people in it.")
        else:
            lines.append("No named characters and no other people appear in this shot.")
    lines.append("")

    if spans:
        lines.append(f"[SHOT LIST — {len(spans)} shots, hard cuts only at the marked seconds]")
        for j, (a, b, cam) in enumerate(spans, 1):
            lines.append(f"- Shot {j}, {a}–{b}s: {cam}.")
        if cont == "continuous":
            lines.append(f"- {CONTINUOUS_MARK}; Shot 1 keeps the previous framing axis, no jump.")
        elif c["chars"] and talks_from_start(c):
            lines.append("- Continuity: new camera setup; the characters are already in place in the first frame and the first speaker starts talking within the first second.")
        elif c["chars"]:
            lines.append(f"- Continuity: new camera setup; Shot 1 opens on the empty location and light with no person in frame, and characters appear only from 3s.")
        else:
            lines.append("- Continuity: new camera setup; Shot 1 establishes the place and light cleanly from the first frame.")
        if c.get("intercut"):
            lines.append("- Each shot keeps the lighting of its own place and time; faces, wardrobe and props stay consistent; whoever is speaking has the face clearly on screen in that shot.")
        else:
            lines.append("- Every cut keeps the same lighting, wardrobe, props and screen direction; whoever is speaking has the face clearly on screen in that shot.")
        if len(c["chars"]) >= 2 and not c.get("intercut"):  # intercut characters are in different places or times
            lines.append("- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the cuts.")
        lines.append("")
        rule = "Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per second; clothing stays fully worn."
        if cont != "continuous" and c["chars"] and not talks_from_start(c):
            rule += " The first three seconds show the environment and props only; characters enter from 3s."
        lines += ["[TIMELINE — second by second]", rule]
        for k, step in enumerate(c["steps"]):
            j = next(n for n, (a, b, _) in enumerate(spans, 1) if a <= k < b)
            cut = "CUT to " if k == spans[j - 1][0] and j > 1 else ""
            tail = " The sequence settles on this as its final frame." if k == D - 1 else ""
            step = re.sub(r"^CUT\s*(to [^:]*)?:\s*", "", step)  # the label already says CUT
            lines.append(f"- {k}–{k + 1}s ({cut}Shot {j}): {step}{tail}")
        lines.append("")
        return render_audio(data, c, cont, D, lines)

    lines.append("[SHOT]")
    lines.append(f"- Framing & motion: {c['camera']}; one smooth camera move from start to end, no cuts.")
    if cont == "continuous":
        lines.append(f"- {CONTINUOUS_MARK}; same framing axis, no jump.")
    elif c["chars"]:
        lines.append("- Continuity: new camera setup; 0.0–3.0s establishes the empty location and light with no person in frame, then reveals the character naturally from 3.0s.")
    else:
        lines.append("- Continuity: new camera setup; establish the place and light cleanly from the first frame.")
    if not is_vo(c) and len(c["chars"]) >= 2:
        # fk-camera-guide: 180-degree rule — camera stays on one side of the line, eyelines meet.
        lines.append("- Eyelines: the camera stays on one side of the line between the characters (180-degree rule) so their eyes meet across the frame.")
    lines.append("")

    if cont == "continuous" or not c["chars"]:
        timeline_rule = "Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; clothing stays fully worn from the first frame."
    else:
        timeline_rule = "Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one main action per beat; 0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn."
    lines += ["[TIMELINE]", timeline_rule]
    windows = BEAT_WINDOWS[D]
    for k, ((w0, w1), beat) in enumerate(zip(windows, c["beats"])):
        tail = " The shot settles on this as its final frame." if k == len(windows) - 1 else ""
        lines.append(f"- {w0:.1f}–{w1:.1f}s: {beat}{tail}")
    lines.append("")
    return render_audio(data, c, cont, D, lines)


def render_audio(data: dict, c: dict, cont: str, D: int, lines: list[str]) -> str:
    """[AUDIO] and [AVOID] (always last: the runner's retry sanitizer replaces from [AVOID] on)."""
    lines.append("[AUDIO]")
    if is_vo(c):
        a, b = speech_window(c["line"], data["narrator"]["rate"], max_end=soft_end(D))
        gender = data["narrator"].get("gender", "male")  # cai-ket-cho-tieu-tam có khối giọng kể nữ (không dùng)
        lines.append(f"- Narration {a:.1f}–{b:.1f}s by an off-screen {gender} narrator ({data['narrator']['voice']}), in {lang(data)['name']}, said exactly once: \"{c['line']}\" (no subtitles)")
        lines.append("- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.")
        lines.append("- Nobody on screen speaks; every mouth on screen stays closed.")
    elif len(turns(c)) >= 2:
        # Hai lượt thoại trong một clip 15s (09/11/2026): mỗi người một khung giờ riêng, người kia ngậm miệng nghe.
        # Từ 10/11/2026 phim không người dẫn chuyện được ba lượt ngắn qua lại (A-B-A).
        plan = speech_plan(data, c, cont, D)
        ts = turns(c)
        count = {2: "two", 3: "three"}[len(ts)]
        solo = len({t["speaker"] for t in ts}) == 1  # one speaker in parts: a monologue whose pace changes
        if solo:
            sp = ts[0]["speaker"]
            lines.append(f"- Dialogue in {lang(data)['name']} with exact lip-sync, spoken on camera by {sp} alone in {count} parts in this order with a short breath between them, each said exactly once (no subtitles):")
            for k, ((_, ln, a, b), t) in enumerate(zip(plan, ts), 1):
                lines.append(f"- Part {k}, {a:.1f}–{b:.1f}s ({turn_voice(data, t)}): \"{ln}\"")
        else:
            lines.append(f"- Dialogue in {lang(data)['name']} with exact lip-sync, {count} spoken turns in this order, each said exactly once (no subtitles):")
            for k, ((sp, ln, a, b), t) in enumerate(zip(plan, ts), 1):
                lines.append(f"- Turn {k}, {a:.1f}–{b:.1f}s, spoken on camera by {sp} ({turn_voice(data, t)}): \"{ln}\"")
        if all(t.get("pace") for t in ts) and len({t["pace"] for t in ts}) > 1:
            verb = lambda k: "continues" if plan[k][0] == plan[k - 1][0] else "answers"
            steps = [f"{plan[0][0]} speaks {PACES[ts[0]['pace']][3]}"] + [f"{plan[k][0]} {verb(k)} {PACES[ts[k]['pace']][3]}" for k in range(1, len(ts))]
            lines.append(f"- Pacing: {', then '.join(steps)}; the change of speed is clearly audible.")
        first = plan[0][2]
        if solo:
            opening = f"{sp} keeps the mouth closed until {first:.1f}s; then" if first > SPEECH_START else "Throughout,"
            lines.append(f"- {opening} {sp}'s face and lips stay clearly visible while speaking, with a short breath between the parts; after the last word {sp} closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.")
        else:
            opening = f"Both keep their mouths closed until {first:.1f}s; then" if first > SPEECH_START else "Throughout,"
            lines.append(f"- {opening} each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.")
    else:
        t = turns(c)[0]
        sp, line, rate, voice = t["speaker"], t["line"], turn_rate(data, t), turn_voice(data, t)
        if talks_from_start(c):  # multi-shot dialogue clip: the speaker is on screen and talking from the first second
            a, b = speech_window(line, rate, max_end=hard_end(D))
            lines.append(f"- Dialogue {a:.1f}–{b:.1f}s, spoken on camera by {sp} ({voice}), in {lang(data)['name']} with exact lip-sync, said exactly once: \"{line}\" (no subtitles)")
            lines.append(f"- {sp} starts talking within the first second; whenever {sp} speaks, the face and lips are clearly visible in that shot; after the last word {sp} closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.")
        elif cont == "continuous" and not c.get("speech_start"):
            a, b = speech_window(line, rate, max_end=soft_end(D))
            lines.append(f"- Dialogue {a:.1f}–{b:.1f}s, spoken on camera by {sp} ({voice}), in {lang(data)['name']} with exact lip-sync, said exactly once: \"{line}\" (no subtitles)")
            lines.append(f"- {sp}'s face and lips stay clearly visible while speaking; after the last word {sp} closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.")
        elif cont == "continuous":
            # speech_start (08/11/2026): beats cho nhân vật mở miệng từ beat 2 → lời thoại cũng bắt đầu đúng lúc đó, khẩu hình không trễ tiếng.
            st = float(c["speech_start"])
            a, b = speech_window(line, rate, start=st, max_end=hard_end(D))
            lines.append(f"- Dialogue {a:.1f}–{b:.1f}s, spoken on camera by {sp} ({voice}), in {lang(data)['name']} with exact lip-sync, said exactly once: \"{line}\" (no subtitles)")
            lines.append(f"- {sp} keeps the mouth closed until {a:.1f}s, then the face and lips stay clearly visible while speaking; after the last word {sp} closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.")
        else:
            a, b = speech_window(line, rate, start=3.0, max_end=hard_end(D))
            lines.append(f"- Dialogue {a:.1f}–{b:.1f}s, spoken on camera by {sp} ({voice}), in {lang(data)['name']} with exact lip-sync, said exactly once: \"{line}\" (no subtitles)")
            lines.append(f"- From 3.0s onward, {sp}'s face and lips stay clearly visible while speaking; after the last word {sp} closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.")
    if not is_vo(c) and "narrator" not in data:
        # Bản render 10/11/2026: clip còn trống vài giây thì Omni nói lại nguyên câu cho kín clip.
        end = speech_plan(data, c, cont, D)[-1][3]
        if data.get("voice_common"):
            lines.append(f"- Voices: {data['voice_common']}")
        lines.append(f"- All speech is over by {end:.1f}s. From then until {D:.1f}s nobody says a single word: the last beat plays as a silent reaction over ambience and sound effects, and no line or part of a line is ever said again to fill the time.")
    lines.append("- " + lang(data)["speak"])
    music = any(k in c["sfx"] for k in ("melody", "flute", "music"))
    lines.append(f"- SFX: {c['sfx']}. Ambience continues to {D:.1f}s." + ("" if music else " No music."))
    lines.append("")

    if c.get("intercut"):
        cut_avoid = "cuts at any moment other than the planned shot changes, jump cuts"
    else:
        cut_avoid = "cuts at any moment other than the planned shot changes, jump cuts, a change of location" if c.get("steps") else "jump cuts or scene changes"
    lines.append("[AVOID]")
    lines.append("On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, " + ("" if music else "background music, ") + f"letterbox bars, {cut_avoid}, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, {speech_avoid(data, c)}, {lang(data)['accent_avoid']}.")
    return "\n".join(lines) + "\n"


def validate_turns(data: dict, sc: dict, i: int, cont: str, D: int, errors: list[str], warns: list[str]) -> None:
    """15s-only checks: one VO line or 1–2 character turns that really fit inside the clip."""
    c = sc["clips"][i]
    cid = c["id"]
    ts = turns(c)
    if "turns" in c and ("speaker" in c or "line" in c):
        errors.append(f"{cid}: use either speaker+line or turns, not both")
    max_turns = 2 if "narrator" in data else 3  # dialogue-only films may trade three short turns (A-B-A)
    if not 1 <= len(ts) <= max_turns:
        errors.append(f"{cid}: 1–{max_turns} spoken turns per clip, got {len(ts)}")
        return
    speakers = [t["speaker"] for t in ts]
    if "NARRATOR" in speakers and len(ts) > 1:
        errors.append(f"{cid}: the narrator never shares a clip with a character turn")
    for a, b in zip(ts, ts[1:]):
        if a["speaker"] == b["speaker"] and a.get("pace") == b.get("pace"):
            errors.append(f"{cid}: two turns in a row by the same speaker at the same pace — merge them into one line")
    for t in ts:
        if t["speaker"] != "NARRATOR" and t["speaker"] not in c["chars"]:
            errors.append(f"{cid}: speaker {t['speaker']} not on screen")
        if '"' in t["line"]:
            errors.append(f"{cid}: double quote inside the spoken line")
    n = sum(syllables(t["line"]) for t in ts)
    if is_vo(c):
        if not 28 <= n <= 52:
            warns.append(f"{cid}: {n} syllables (15s VO: 28–52)")
    elif len(ts) == 1:
        m = PACES[ts[0]["pace"]][0] if ts[0].get("pace") in PACES else 1.0  # slow lines need fewer words
        single = lang(data)["single_15s"]
        lo, hi = (round(22 * m), round(46 * m)) if "narrator" in data else (round(single[0] * m), round(single[1] * m))  # dialogue-only: speech from 0.4s
        if not lo <= n <= hi:
            warns.append(f"{cid}: {n} syllables (15s single turn{' ' + ts[0]['pace'] if ts[0].get('pace') else ''}: {lo}–{hi})")
    else:
        for t in ts:
            m = PACES[t["pace"]][0] if t.get("pace") in PACES else 1.0
            lo, hi = (round(8 * m), round(30 * m)) if len(ts) == 2 else (3, round(24 * m))
            if not lo <= syllables(t["line"]) <= hi:
                warns.append(f"{cid}: turn by {t['speaker']} has {syllables(t['line'])} syllables ({lo}–{hi})")
    plan = speech_plan(data, c, cont, D, clamp=False)
    late = (not is_vo(c)) and (cont != "continuous" or bool(c.get("speech_start")) or talks_from_start(c))
    limit = hard_end(D) if late else soft_end(D)
    if plan[-1][3] > limit:
        errors.append(f"{cid}: speech ends at {plan[-1][3]:.1f}s, past {limit:.1f}s — shorten the line(s)")
    elif "narrator" not in data and n < lang(data)["min_15s"]:
        # 10/11/2026 renders: Omni speaks ~3.7–4 syllables/s whatever the pace, and fills a half-empty clip by repeating a line
        warns.append(f"{cid}: only {n} {lang(data)['unit']} in a {D}s clip — Omni finishes early and repeats lines; write at least {lang(data)['min_15s']} (add a reply or a third turn)")
    elif plan[-1][3] < D - 4.0:
        warns.append(f"{cid}: speech ends at {plan[-1][3]:.1f}s — over 4s of silence at the end of a {D}s clip; lengthen the line(s) or add a second turn")


def validate_voice_fields(data: dict, c: dict, paced: bool, errors: list[str]) -> bool:
    """Narrator, pace, tone and wardrobe checks; False when timing must not be computed."""
    cid, ok = c["id"], True
    for t in turns(c):
        if t["speaker"] == "NARRATOR":
            if "narrator" not in data:
                errors.append(f"{cid}: narrator line in a dialogue-only film — give it to a character on screen")
                ok = False
            continue
        if t["speaker"] not in data["characters"]:
            errors.append(f"{cid}: unknown speaker {t['speaker']}")
            ok = False
        if t.get("pace") and t["pace"] not in PACES:
            errors.append(f"{cid}: pace must be one of {sorted(PACES)}, got {t['pace']}")
            ok = False
        elif paced and not t.get("pace"):
            errors.append(f"{cid}: turn by {t['speaker']} has no pace (the film uses per-turn pace)")
        tone = t.get("tone", "")
        if tone and (re.search(r'["@\d]', tone) or len(tone) > 60):
            errors.append(f"{cid}: tone must be a short phrase without quotes, tags or digits: {tone}")
    for tag, outfit in (c.get("wardrobe") or {}).items():
        if tag not in c["chars"]:
            errors.append(f"{cid}: wardrobe for {tag}, who is not in the shot")
        if '"' in outfit or TAG.search(outfit):
            errors.append(f"{cid}: wardrobe text for {tag} must not contain quotes or tags")
    return ok


def validate_shots(c: dict, cont: str, D: int, errors: list[str], warns: list[str]) -> None:
    """Multi-shot clip: one step per second, 3–5 shots of at least 2s ending exactly at D."""
    cid = c["id"]
    steps, shots = c.get("steps") or [], c.get("shots") or []
    if len(steps) != D:
        errors.append(f"{cid}: needs exactly {D} steps (one per second), got {len(steps)}")
        return
    if "beats" in c or "camera" in c:
        errors.append(f"{cid}: a multi-shot clip uses shots+steps instead of camera+beats")
    if not 3 <= len(shots) <= 5:
        errors.append(f"{cid}: 3–5 shots per {D}s clip, got {len(shots)}")
    t = 0
    for s in shots:
        u = s.get("until")
        if not isinstance(u, int) or u - t < 2:
            errors.append(f"{cid}: shot ending at {u} must be a whole second at least 2s after the previous cut ({t})")
            return
        t = u
    if t != D:
        errors.append(f"{cid}: last shot must end at {D}s, ends at {t}")
        return
    spans = shot_spans(c)
    if talks_from_start(c):
        if c.get("speech_start"):
            errors.append(f"{cid}: speech starts at 0.4s in every clip of this film — remove speech_start")
        first = turns(c)[0]["speaker"]
        if first not in steps[0] or not SPEAKING.search(steps[0]):
            errors.append(f"{cid}: second 0–1 must show {first} already speaking (Omni starts the dialogue at once)")
    elif cont == "cut" and c["chars"]:
        if spans[0][1] < 3:
            errors.append(f"{cid}: Shot 1 must last at least until 3s (empty establishing frames)")
        for k in range(3):
            if TAG.search(steps[k]):
                errors.append(f"{cid}: second {k}–{k + 1} names a character; the first 3s of a cut clip show the place only")
    for (_, _, a), (_, _, b) in zip(spans, spans[1:]):
        if shot_scale(a) and shot_scale(a) == shot_scale(b):
            warns.append(f"{cid}: two shots in a row are both {shot_scale(a)} — vary the shot size")


def mark_dialogue_only(data: dict) -> None:
    for sc in data["scenes"]:
        for c in sc["clips"]:
            c["_dialogue_only"] = "narrator" not in data


def validate(data: dict) -> tuple[list[str], list[str]]:
    mark_dialogue_only(data)
    errors, warns = [], []
    chars = data["characters"]
    D = clip_seconds(data)
    n_beats = len(BEAT_WINDOWS[D])
    paced = has_paces(data)
    for sc in data["scenes"]:
        for i, c in enumerate(sc["clips"]):
            cid = c["id"]
            cont = effective_continuity(sc["clips"], i, sc["setting"])
            if not validate_voice_fields(data, c, paced, errors):
                continue
            if D != 10:
                validate_turns(data, sc, i, cont, D, errors, warns)
            if c.get("steps") or c.get("shots"):
                validate_shots(c, cont, D, errors, warns)
            elif len(c["beats"]) != n_beats:
                errors.append(f"{cid}: needs exactly {n_beats} beats")
            elif cont == "cut" and c["chars"] and TAG.search(c["beats"][0]):
                errors.append(f"{cid}: cut clip without previous last frame must NOT specify @character in beat 1 (0.0–3.0s): {c['beats'][0]}")
            for t in c["chars"]:
                if t not in chars:
                    errors.append(f"{cid}: unknown character {t}")
            visual = " ".join(visual_lines(c) + cameras(c) + [c.get("setting", sc["setting"]), c.get("extras", "")])
            stray = set(TAG.findall(visual)) - set(c["chars"])
            if stray:
                errors.append(f"{cid}: tags used but not declared: {sorted(stray)}")
            if CLOCK_DIGITS.search(visual):
                errors.append(f"{cid}: clock digits in visual text (Omni paints them): {CLOCK_DIGITS.search(visual).group(0)}")
            for pat in BANNED_VISUAL:
                m = re.search(pat, visual, re.I)
                if m:
                    warns.append(f"{cid}: risky word '{m.group(0)}' in visuals")
            if D == 10:
                if c["speaker"] != "NARRATOR":
                    if c["speaker"] not in c["chars"]:
                        errors.append(f"{cid}: speaker {c['speaker']} not on screen")
                if '"' in c["line"]:
                    errors.append(f"{cid}: double quote inside the spoken line")
                n = syllables(c["line"])
                if not 16 <= n <= 28:
                    warns.append(f"{cid}: {n} syllables")
            if TAG.search(c["sfx"]):
                errors.append(f"{cid}: @tag inside sound effects")
            people = len(c["chars"]) + (1 if c.get("extras") else 0)
            if people > 2:
                warns.append(f"{cid}: {people} people in frame (fk-scriptwriter: max 2; can-nha 03.4 with 3 people rendered a duplicated face)")
            abstract = ABSTRACT_EMOTION.findall(" ".join(visual_lines(c)))
            if abstract:
                warns.append(f"{cid}: abstract emotion words {sorted(set(w.lower() for w in abstract))} — prefer physical cues")
            if i > 0 and not c.get("shots") and not sc["clips"][i - 1].get("shots") and shot_scale(c["camera"]) and shot_scale(c["camera"]) == shot_scale(sc["clips"][i - 1]["camera"]):
                warns.append(f"{cid}: same shot scale as previous clip ({shot_scale(c['camera'])})")
            first_sp = turns(c)[0]["speaker"]
            if D == 10:
                rate = turn_rate(data, turns(c)[0])
                if speech_window(c["line"], rate)[1] > 8.6:
                    warns.append(f"{cid}: line runs past 8.6s")
                if c["speaker"] != "NARRATOR" and cont == "continuous" and len(c["beats"]) == 3:
                    if c.get("speech_start"):
                        if speech_window(c["line"], rate, start=float(c["speech_start"]), max_end=99)[1] > 9.4:
                            errors.append(f"{cid}: line does not fit after speech_start {c['speech_start']}s — shorten it")
                    elif not SPEAKING.search(c["beats"][0]):
                        warns.append(f"{cid}: dialogue starts at 0.4s but beat 1 shows no speaking — lips will lag; set \"speech_start\": 3.0 or let {c['speaker']} talk in beat 1")
            elif not is_vo(c) and cont == "continuous" and (c.get("steps") or len(c["beats"]) == n_beats):
                if not c.get("speech_start") and not SPEAKING.search(visual_lines(c)[0]):
                    warns.append(f"{cid}: dialogue starts at 0.4s but beat 1 shows no speaking — lips will lag; set \"speech_start\": 3.0 or let {first_sp} talk in beat 1")
    return errors, warns


def camera_cell(c: dict) -> str:
    """Camera column: the one camera move, or 'N cảnh quay: lens/size → …' for a multi-shot clip."""
    if not c.get("shots"):
        return c["camera"]
    return f"{len(c['shots'])} cảnh quay: " + " → ".join(s["camera"].split(",")[0] for s in c["shots"])


def scene_table(data: dict, sc: dict, conts: list[str]) -> list[str]:
    paced = has_paces(data)
    said = "Lời Dẫn / Thoại" if "narrator" in data else "Lời Thoại"
    rows = [f"| Clip | Nhân Vật | Giọng |{' Nhịp |' if paced else ''} {lang(data)['unit'].capitalize()} | Khung thoại | {said} | Camera | Cách tạo trên Flow |",
            "|---|---|---|" + ("---|" if paced else "") + "---|---|---|---|---|"]
    D = clip_seconds(data)
    for c, cont in zip(sc["clips"], conts):
        n = int(c["id"].split(".")[1])
        plan = speech_plan(data, c, cont, D)
        a, b = plan[0][2], plan[-1][3]
        who = ", ".join(f"`{t}`" for t in c["chars"]) or "—"
        n_syl = sum(syllables(t["line"]) for t in turns(c))
        pace = f" {pace_label(c)} |" if paced else ""
        rows.append(f"| [**Clip {n}**](clip-{n}.md) | {who} | `{mode_label(c)}` |{pace} **{n_syl}** | `{a:.1f}–{b:.1f}s` | \"{line_text(c)}\" | {camera_cell(c)} | {flow_mode(c, cont)} |")
    return rows


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    series = sys.argv[1].rstrip("/")
    check_only = "--check" in sys.argv
    sdir = os.path.join(REPO, series)
    data = json.load(open(os.path.join(sdir, "PHAN_CANH_OMNI.json"), encoding="utf-8"))

    errors, warns = validate(data)
    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    if errors:
        print(f"{len(errors)} error(s); nothing written.")
        return 1

    all_conts, prompts = {}, {}
    for sc in data["scenes"]:
        conts = [effective_continuity(sc["clips"], i, sc["setting"]) for i in range(len(sc["clips"]))]
        all_conts[sc["num"]] = conts
        for c, cont in zip(sc["clips"], conts):
            prompts[c["id"]] = render_prompt(data, sc, c, cont)

    lens = [len(p) for p in prompts.values()]
    vo = sum(1 for sc in data["scenes"] for c in sc["clips"] if is_vo(c))
    modes = [flow_mode(c, all_conts[sc["num"]][i]) for sc in data["scenes"] for i, c in enumerate(sc["clips"])]
    print(f"{series}: {len(prompts)} clips, {vo} VO + {len(prompts) - vo} lip-sync; prompt length {min(lens)}–{max(lens)} chars (avg {sum(lens)//len(lens)})")
    for m in sorted(set(modes)):
        print(f"  {modes.count(m):3d} × {m}")
    if check_only:
        return 0

    total = len(prompts)
    n_scenes = len(data["scenes"])
    D = clip_seconds(data)
    per_scene = {len(sc["clips"]) for sc in data["scenes"]}
    cps = per_scene.pop() if len(per_scene) == 1 else None  # clips per scene, when uniform
    minutes = total * D // 60
    two_turn = sum(1 for sc in data["scenes"] for c in sc["clips"] if len(turns(c)) == 2)
    n_ingr = sum(1 for m in modes if m.startswith("Ingredients"))
    n_frames = sum(1 for m in modes if m.startswith("Frames"))
    n_t2v = total - n_frames - n_ingr
    narrated = "narrator" in data
    if narrated:
        voice_head = [f"- **Giọng Người Dẫn Chuyện (cố định cả {total} clip):** {data['narrator']['voice']}. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; đọc nhanh liên thanh như oan-thai-doi-me, ~{data['narrator']['rate']:.1f} âm tiết/giây, liền một hơi, không ngắt giữa câu."]
    else:
        voice_head = [f"- **Không có người dẫn chuyện:** 100% lời thoại do nhân vật nói trên hình — cả {total} clip là thoại khớp khẩu hình. Giọng gốc của mỗi nhân vật ({lang(data)['voice_note']}) giữ nguyên văn ở mọi clip để Omni không đổi người nói."]
    if has_paces(data):
        cnt = {k: 0 for k in PACES}
        for sc in data["scenes"]:
            for c in sc["clips"]:
                for t in turns(c):
                    cnt[t["pace"]] += 1
        voice_head.append(
            f"- **Nhịp giọng theo cảnh:** mỗi lượt thoại có nhịp riêng nối sau giọng gốc — **nhanh** (cãi vã, hoảng hốt, rượt đuổi, khoe khoang; tốc độ ×{PACES['fast'][0]:g}), "
            f"**vừa** (trò chuyện thường), **chậm** (xúc động, thú nhận, câu chốt lặng người; tốc độ ×{PACES['slow'][0]:g}). Khung thoại tính theo nhịp nên câu chậm ít chữ hơn. "
            f"Cả phim: {cnt['fast']} lượt nhanh, {cnt['normal']} lượt vừa, {cnt['slow']} lượt chậm.")
    voice_bullets = voice_head + [
        "- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.",
        (f"- **Mật độ:** {total} clips × {D}s — {vo} clip VO + {total - vo} clip thoại" if narrated else f"- **Mật độ:** {total} clips × {D}s, tất cả là clip thoại")
        + (f" ({two_turn} clip có hai lượt thoại)" if two_turn else "")
        + f"; lời nói nằm trong khung riêng bắt đầu từ {SPEECH_START:.1f}s (xem cột *Khung thoại*).",
        f"- **Cách tạo trên Flow (runner tự chọn):** {n_frames} clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), {n_ingr} clip ảnh nhân vật (Ingredients), {n_t2v} clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.",
        f"- **Hậu kỳ runner:** clip VO được tăng tốc giọng thêm 1.18x khi tải về (`FLOWKIT_VOICE_TEMPO` mặc định 1.18, đặt 1.0 để tắt), giữ nguyên khung hình {D}s; clip lip-sync không bao giờ bị tăng tốc để khớp khẩu hình."
        if vo else "- **Hậu kỳ runner:** không có clip VO nên runner không tăng tốc giọng clip nào; tốc độ nói nằm trong prompt (nhịp từng lượt) để khớp khẩu hình.",
        f"- **Màu phim & ánh sáng:** {data.get('lighting') or data['style']}",
        f"- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py {series}` sinh lại toàn bộ clip, README, kịch bản.",
    ]

    for sc in data["scenes"]:
        d = os.path.join(sdir, f"canh-{sc['num']:02d}")
        os.makedirs(d, exist_ok=True)
        keep = set()
        for c in sc["clips"]:
            n = int(c["id"].split(".")[1])
            keep.add(f"clip-{n}.md")
            with open(os.path.join(d, f"clip-{n}.md"), "w", encoding="utf-8") as f:
                f.write(prompts[c["id"]])
        for old in os.listdir(d):  # 6 clips × 10s → 4 clips × 15s leaves clip-5/6.md behind
            if re.fullmatch(r"clip-\d+\.md", old) and old not in keep:
                os.remove(os.path.join(d, old))
        n_cl = len(sc["clips"])
        readme = [f"# Cảnh {sc['num']:02d}: {sc['title']} ({n_cl} Clips × {D}s = {n_cl * D}s)", "",
                  f"- **Thời gian:** {sc['time_label']}",
                  f"- **Bối cảnh:** {sc['location']}",
                  f"- **Trục không gian cố định:** {sc['axis']}",
                  f"- **Đạo cụ chính:** {sc['props']}", ""]
        readme += scene_table(data, sc, all_conts[sc["num"]])
        with open(os.path.join(d, "README.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(readme) + "\n")

    kb = [f"# KỊCH BẢN CHI TIẾT {minutes} PHÚT: {data['title'].upper()}", ""] + voice_head + [""]
    for sc in data["scenes"]:
        kb += [f"## Cảnh {sc['num']:02d}: {sc['title']} ({sc['time_label']})", f"- **Bối cảnh:** {sc['location']}", ""]
        for c in sc["clips"]:
            n = int(c["id"].split(".")[1])
            n_syl = sum(syllables(t["line"]) for t in turns(c))
            pace = f" | `nhịp {pace_label(c)}`" if pace_label(c) else ""
            kb.append(f"- **[Clip {c['id']}](canh-{sc['num']:02d}/clip-{n}.md)** (`{mode_label(c)}` | `{n_syl} {lang(data)['unit']}`{pace}): \"{line_text(c)}\"")
        kb.append("")
    with open(os.path.join(sdir, f"KICH_BAN_{minutes}_PHUT.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(kb))

    shape = f"{n_scenes} Cảnh × {cps} Clips × {D}s" if cps else f"{n_scenes} Cảnh, {total} Clips × {D}s"
    rd = [f"# {data['title']} ({shape} = {minutes} Phút)", ""] + voice_bullets + ["", f"## Danh Sách {n_scenes} Cảnh ({total} Clips × {D}s)", "",
          "| Cảnh | Tiêu Đề | Thời Gian | Đường Dẫn |", "|---|---|---|---|"]
    for sc in data["scenes"]:
        rd.append(f"| **Cảnh {sc['num']:02d}** | {sc['title']} | {sc['time_label']} | [`canh-{sc['num']:02d}/`](canh-{sc['num']:02d}/README.md) |")
    with open(os.path.join(sdir, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(rd) + "\n")

    fp = [f"# {data['title']} — Bộ {total} Prompt Google Flow Omni ({shape})", ""] + voice_bullets + [""]
    for sc in data["scenes"]:
        for c in sc["clips"]:
            n = int(c["id"].split(".")[1])
            fp += ["---", "", f"## Cảnh {sc['num']:02d} - Clip {n} (`canh-{sc['num']:02d}/clip-{n}.md`)", "", "```markdown", prompts[c["id"]].rstrip("\n"), "```", ""]
    with open(os.path.join(sdir, "FLOW_PROMPTS.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(fp))
    print(f"wrote {total} clips + READMEs + KICH_BAN + FLOW_PROMPTS for {series}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
