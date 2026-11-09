#!/usr/bin/env python3
"""Compile a series' PHAN_CANH_OMNI.json (N scenes × 6 clips × 10s) into Google Flow Omni prompts.

Used by can-nha-am-duong, tieng-go-dem-ba-gio, ma-da-dam-sen (15 scenes), gang-to-tai-xuat (27 scenes × 4 × 15s)
and cai-ket-cho-tieu-tam (25 scenes × 4 × 15s).

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
    return len([w for w in re.split(r"\s+", re.sub(r"[^\wÀ-ỹ\s]", " ", text)) if w])


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
    every other clip has the classic single "speaker" + "line"."""
    return c.get("turns") or [{"speaker": c["speaker"], "line": c["line"]}]


def is_vo(c: dict) -> bool:
    return turns(c)[0]["speaker"] == "NARRATOR"


def turn_rate(data: dict, speaker: str) -> float:
    return data["narrator"]["rate"] if speaker == "NARRATOR" else data["characters"][speaker]["rate"]


def speech_start_for(c: dict, cont: str) -> float:
    if is_vo(c):
        return SPEECH_START
    if cont != "continuous":
        return 3.0
    return float(c["speech_start"]) if c.get("speech_start") else SPEECH_START


def speech_plan(data: dict, c: dict, cont: str, D: int, clamp: bool = True) -> list[tuple[str, str, float, float]]:
    """(speaker, line, start, end) per turn, back to back with TURN_GAP between them."""
    t = speech_start_for(c, cont)
    late = (not is_vo(c)) and (cont != "continuous" or bool(c.get("speech_start")))
    limit = (hard_end(D) if late else soft_end(D)) if clamp else 99.0
    plan = []
    for tr in turns(c):
        a, b = speech_window(tr["line"], turn_rate(data, tr["speaker"]), start=t, max_end=limit)
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


def render_prompt(data: dict, scene: dict, c: dict, cont: str) -> str:
    chars = data["characters"]
    setting = c.get("setting", scene["setting"])
    # Thứ tự theo "Prompt Ingredients" của hướng dẫn Omni 1.2 (EvoLinkAI): Style → Lighting → Location →
    # Shot framing & motion → Action; lời nói trong ngoặc kép, phần cấm (negative) để cuối.
    D = clip_seconds(data)
    lines = [f"One continuous {D}-second live-action shot, 16:9 widescreen, 24 fps.", ""]
    lines += ["[STYLE]", data["style"], ""]
    if data.get("lighting"):
        lines += ["[LIGHTING]", data["lighting"], ""]
    lines += ["[LOCATION]", setting, ""]

    lines.append("[CHARACTERS]")
    if c["chars"]:
        if cont == "continuous":
            lines.append("Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.")
        else:
            lines.append("Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards, and never flash or display the studio reference portrait card in the opening frames; 0.0–3.0s establishes the empty environment first and characters appear only from 3.0s onward.")
        for t in c["chars"]:
            lines.append(f"- {t} = {chars[t]['anchor']}")
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

    lines.append("[AUDIO]")
    if is_vo(c):
        a, b = speech_window(c["line"], data["narrator"]["rate"], max_end=soft_end(D))
        gender = data["narrator"].get("gender", "male")  # cai-ket-cho-tieu-tam có khối giọng kể nữ (không dùng)
        lines.append(f"- Narration {a:.1f}–{b:.1f}s by an off-screen {gender} narrator ({data['narrator']['voice']}), in Vietnamese, said exactly once: \"{c['line']}\" (no subtitles)")
        lines.append("- After the last word the narrator stays silent until the end of the shot: no repeated words, no echo, no second reading of the line.")
        lines.append("- Nobody on screen speaks; every mouth on screen stays closed.")
    elif len(turns(c)) == 2:
        # Hai lượt thoại trong một clip 15s (09/11/2026): mỗi người một khung giờ riêng, người kia ngậm miệng nghe.
        plan = speech_plan(data, c, cont, D)
        lines.append("- Dialogue in Vietnamese with exact lip-sync, two spoken turns in this order, each said exactly once (no subtitles):")
        for k, (sp, ln, a, b) in enumerate(plan, 1):
            lines.append(f"- Turn {k}, {a:.1f}–{b:.1f}s, spoken on camera by {sp} ({chars[sp]['voice']}): \"{ln}\"")
        first = plan[0][2]
        opening = f"Both keep their mouths closed until {first:.1f}s; then" if first > SPEECH_START else "Throughout,"
        lines.append(f"- {opening} each speaker's face and lips stay clearly visible while speaking; only the person whose turn it is moves the lips while the other listens with the mouth closed; after the last word both close their mouths and say nothing more — no repeated words, no echo. No narrator and no other voices.")
    else:
        sp = c["speaker"]
        if cont == "continuous" and not c.get("speech_start"):
            a, b = speech_window(c["line"], chars[sp]["rate"], max_end=soft_end(D))
            lines.append(f"- Dialogue {a:.1f}–{b:.1f}s, spoken on camera by {sp} ({chars[sp]['voice']}), in Vietnamese with exact lip-sync, said exactly once: \"{c['line']}\" (no subtitles)")
            lines.append(f"- {sp}'s face and lips stay clearly visible while speaking; after the last word {sp} closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.")
        elif cont == "continuous":
            # speech_start (08/11/2026): beats cho nhân vật mở miệng từ beat 2 → lời thoại cũng bắt đầu đúng lúc đó, khẩu hình không trễ tiếng.
            st = float(c["speech_start"])
            a, b = speech_window(c["line"], chars[sp]["rate"], start=st, max_end=hard_end(D))
            lines.append(f"- Dialogue {a:.1f}–{b:.1f}s, spoken on camera by {sp} ({chars[sp]['voice']}), in Vietnamese with exact lip-sync, said exactly once: \"{c['line']}\" (no subtitles)")
            lines.append(f"- {sp} keeps the mouth closed until {a:.1f}s, then the face and lips stay clearly visible while speaking; after the last word {sp} closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.")
        else:
            a, b = speech_window(c["line"], chars[sp]["rate"], start=3.0, max_end=hard_end(D))
            lines.append(f"- Dialogue {a:.1f}–{b:.1f}s, spoken on camera by {sp} ({chars[sp]['voice']}), in Vietnamese with exact lip-sync, said exactly once: \"{c['line']}\" (no subtitles)")
            lines.append(f"- From 3.0s onward, {sp}'s face and lips stay clearly visible while speaking; after the last word {sp} closes the mouth and says nothing more — no repeated words, no echo. No narrator and no other voices.")
    lines.append("- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.")
    music = any(k in c["sfx"] for k in ("melody", "flute", "music"))
    lines.append(f"- SFX: {c['sfx']}. Ambience continues to {D:.1f}s." + ("" if music else " No music."))
    lines.append("")

    lines.append("[AVOID]")
    lines.append("On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), readable writing on signs, labels, name tags, paper or phone screens, blurry faces, distorted hands, " + ("" if music else "background music, ") + "letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred speech, repeated, stuttered or echoed words, the line spoken twice, slow drawn-out narration or long pauses inside a sentence, Southern or Central Vietnamese accents.")
    return "\n".join(lines) + "\n"


def validate_turns(data: dict, sc: dict, i: int, cont: str, D: int, errors: list[str], warns: list[str]) -> None:
    """15s-only checks: one VO line or 1–2 character turns that really fit inside the clip."""
    c = sc["clips"][i]
    cid = c["id"]
    ts = turns(c)
    if "turns" in c and ("speaker" in c or "line" in c):
        errors.append(f"{cid}: use either speaker+line or turns, not both")
    if not 1 <= len(ts) <= 2:
        errors.append(f"{cid}: 1 or 2 spoken turns per clip, got {len(ts)}")
        return
    speakers = [t["speaker"] for t in ts]
    if "NARRATOR" in speakers and len(ts) > 1:
        errors.append(f"{cid}: the narrator never shares a clip with a character turn")
    if len(ts) == 2 and speakers[0] == speakers[1]:
        errors.append(f"{cid}: two turns by the same speaker — merge them into one line")
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
        if not 22 <= n <= 46:
            warns.append(f"{cid}: {n} syllables (15s single turn: 22–46)")
    else:
        for t in ts:
            if not 8 <= syllables(t["line"]) <= 28:
                warns.append(f"{cid}: turn by {t['speaker']} has {syllables(t['line'])} syllables (8–28)")
    plan = speech_plan(data, c, cont, D, clamp=False)
    late = (not is_vo(c)) and (cont != "continuous" or bool(c.get("speech_start")))
    limit = hard_end(D) if late else soft_end(D)
    if plan[-1][3] > limit:
        errors.append(f"{cid}: speech ends at {plan[-1][3]:.1f}s, past {limit:.1f}s — shorten the line(s)")
    elif plan[-1][3] < D - 4.0:
        warns.append(f"{cid}: speech ends at {plan[-1][3]:.1f}s — over 4s of silence at the end of a {D}s clip; lengthen the line(s) or add a second turn")


def validate(data: dict) -> tuple[list[str], list[str]]:
    errors, warns = [], []
    chars = data["characters"]
    D = clip_seconds(data)
    n_beats = len(BEAT_WINDOWS[D])
    for sc in data["scenes"]:
        for i, c in enumerate(sc["clips"]):
            cid = c["id"]
            cont = effective_continuity(sc["clips"], i, sc["setting"])
            if D != 10:
                validate_turns(data, sc, i, cont, D, errors, warns)
            if len(c["beats"]) != n_beats:
                errors.append(f"{cid}: needs exactly {n_beats} beats")
            elif cont == "cut" and c["chars"] and TAG.search(c["beats"][0]):
                errors.append(f"{cid}: cut clip without previous last frame must NOT specify @character in beat 1 (0.0–3.0s): {c['beats'][0]}")
            for t in c["chars"]:
                if t not in chars:
                    errors.append(f"{cid}: unknown character {t}")
            visual = " ".join(c["beats"] + [c["camera"], c.get("setting", sc["setting"]), c.get("extras", "")])
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
            abstract = ABSTRACT_EMOTION.findall(" ".join(c["beats"]))
            if abstract:
                warns.append(f"{cid}: abstract emotion words {sorted(set(w.lower() for w in abstract))} — prefer physical cues")
            if i > 0 and shot_scale(c["camera"]) and shot_scale(c["camera"]) == shot_scale(sc["clips"][i - 1]["camera"]):
                warns.append(f"{cid}: same shot scale as previous clip ({shot_scale(c['camera'])})")
            first_sp = turns(c)[0]["speaker"]
            if D == 10:
                rate = data["narrator"]["rate"] if c["speaker"] == "NARRATOR" else chars[c["speaker"]]["rate"]
                if speech_window(c["line"], rate)[1] > 8.6:
                    warns.append(f"{cid}: line runs past 8.6s")
                if c["speaker"] != "NARRATOR" and cont == "continuous" and len(c["beats"]) == 3:
                    if c.get("speech_start"):
                        if speech_window(c["line"], rate, start=float(c["speech_start"]), max_end=99)[1] > 9.4:
                            errors.append(f"{cid}: line does not fit after speech_start {c['speech_start']}s — shorten it")
                    elif not SPEAKING.search(c["beats"][0]):
                        warns.append(f"{cid}: dialogue starts at 0.4s but beat 1 shows no speaking — lips will lag; set \"speech_start\": 3.0 or let {c['speaker']} talk in beat 1")
            elif not is_vo(c) and cont == "continuous" and len(c["beats"]) == n_beats:
                if not c.get("speech_start") and not SPEAKING.search(c["beats"][0]):
                    warns.append(f"{cid}: dialogue starts at 0.4s but beat 1 shows no speaking — lips will lag; set \"speech_start\": 3.0 or let {first_sp} talk in beat 1")
    return errors, warns


def scene_table(data: dict, sc: dict, conts: list[str]) -> list[str]:
    rows = ["| Clip | Nhân Vật | Giọng | Âm tiết | Khung thoại | Lời Dẫn / Thoại | Camera | Cách tạo trên Flow |",
            "|---|---|---|---|---|---|---|---|"]
    D = clip_seconds(data)
    for c, cont in zip(sc["clips"], conts):
        n = int(c["id"].split(".")[1])
        plan = speech_plan(data, c, cont, D)
        a, b = plan[0][2], plan[-1][3]
        who = ", ".join(f"`{t}`" for t in c["chars"]) or "—"
        n_syl = sum(syllables(t["line"]) for t in turns(c))
        rows.append(f"| [**Clip {n}**](clip-{n}.md) | {who} | `{mode_label(c)}` | **{n_syl}** | `{a:.1f}–{b:.1f}s` | \"{line_text(c)}\" | {c['camera']} | {flow_mode(c, cont)} |")
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
    voice_bullets = [
        f"- **Giọng Người Dẫn Chuyện (cố định cả {total} clip):** {data['narrator']['voice']}. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; đọc nhanh liên thanh như oan-thai-doi-me, ~{data['narrator']['rate']:.1f} âm tiết/giây, liền một hơi, không ngắt giữa câu.",
        "- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.",
        f"- **Mật độ:** {total} clips × {D}s — {vo} clip VO + {total - vo} clip thoại"
        + (f" ({two_turn} clip có hai lượt thoại)" if two_turn else "")
        + f"; lời nói nằm trong khung riêng bắt đầu từ {SPEECH_START:.1f}s (xem cột *Khung thoại*).",
        f"- **Cách tạo trên Flow (runner tự chọn):** {n_frames} clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), {n_ingr} clip ảnh nhân vật (Ingredients), {n_t2v} clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.",
        f"- **Hậu kỳ runner:** clip VO được tăng tốc giọng thêm 1.18x khi tải về (`FLOWKIT_VOICE_TEMPO` mặc định 1.18, đặt 1.0 để tắt), giữ nguyên khung hình {D}s; clip lip-sync không bao giờ bị tăng tốc để khớp khẩu hình.",
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

    kb = [f"# KỊCH BẢN CHI TIẾT {minutes} PHÚT: {data['title'].upper()}", ""] + voice_bullets[:1] + [""]
    for sc in data["scenes"]:
        kb += [f"## Cảnh {sc['num']:02d}: {sc['title']} ({sc['time_label']})", f"- **Bối cảnh:** {sc['location']}", ""]
        for c in sc["clips"]:
            n = int(c["id"].split(".")[1])
            n_syl = sum(syllables(t["line"]) for t in turns(c))
            kb.append(f"- **[Clip {c['id']}](canh-{sc['num']:02d}/clip-{n}.md)** (`{mode_label(c)}` | `{n_syl} âm tiết`): \"{line_text(c)}\"")
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
