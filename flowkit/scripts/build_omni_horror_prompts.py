#!/usr/bin/env python3
"""Compile a 15-scene horror series' PHAN_CANH_OMNI.json into Google Flow Omni prompts.

Used by can-nha-am-duong and tieng-go-dem-ba-gio.

    python3 flowkit/scripts/build_omni_horror_prompts.py can-nha-am-duong          # validate + write
    python3 flowkit/scripts/build_omni_horror_prompts.py tieng-go-dem-ba-gio --check # validate only

The JSON is the single source of truth. This script writes canh-NN/clip-N.md,
canh-NN/README.md, KICH_BAN_15_PHUT.md, FLOW_PROMPTS.md and the clip table of
README.md. After writing, sync flow_agent.db (cms_clip.prompt) or the CMS UI
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


def syllables(text: str) -> int:
    return len([w for w in re.split(r"\s+", re.sub(r"[^\wÀ-ỹ\s]", " ", text)) if w])


def speech_window(line: str, rate: float) -> tuple[float, float]:
    end = SPEECH_START + syllables(line) / rate
    return SPEECH_START, round(min(end, 8.6) + 0.049, 1)


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
    lines = [f"{data['style']} One continuous 10-second shot, 16:9 widescreen, 24 fps.", ""]

    lines.append("[CHARACTERS]")
    if c["chars"]:
        lines.append("Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, furniture or signboards.")
        for t in c["chars"]:
            lines.append(f"- {t} = {chars[t]['anchor']}")
        if c.get("extras"):
            lines.append(f"- Extra: {c['extras']}")
        lines.append("Nobody else appears in the shot.")
    else:
        if c.get("extras"):
            lines.append(f"- Extra: {c['extras']}")
        lines.append("No named characters and no other people appear in this shot.")
    lines.append("")

    lines += ["[SETTING]", setting, ""]

    lines.append("[SHOT]")
    lines.append(f"- Camera: {c['camera']}; one smooth camera move from start to end, no cuts.")
    if cont == "continuous":
        lines.append(f"- {CONTINUOUS_MARK}; same framing axis, no jump.")
    else:
        lines.append("- Continuity: new camera setup; establish the place and light cleanly from the first frame.")
    lines.append("")

    b1, b2, b3 = c["beats"]
    lines += ["[TIMELINE]", f"- 0.0–3.0s: {b1}", f"- 3.0–7.0s: {b2}", f"- 7.0–10.0s: {b3} The shot settles on this as its final frame.", ""]

    lines.append("[AUDIO]")
    if c["speaker"] == "NARRATOR":
        a, b = speech_window(c["line"], data["narrator"]["rate"])
        lines.append(f"- Narration {a:.1f}–{b:.1f}s by an off-screen male narrator ({data['narrator']['voice']}), in Vietnamese: \"{c['line']}\"")
        lines.append("- Nobody on screen speaks; every mouth on screen stays closed.")
    else:
        sp = c["speaker"]
        a, b = speech_window(c["line"], chars[sp]["rate"])
        lines.append(f"- Dialogue {a:.1f}–{b:.1f}s, spoken on camera by {sp} ({chars[sp]['voice']}), in Vietnamese with exact lip-sync: \"{c['line']}\"")
        lines.append(f"- {sp}'s face and lips stay clearly visible while speaking. No narrator and no other voices.")
    lines.append("- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.")
    music = any(k in c["sfx"] for k in ("melody", "flute", "music"))
    lines.append(f"- Sound effects: {c['sfx']}. Ambience continues to 10.0s." + ("" if music else " No music."))
    lines.append("")

    lines.append("[AVOID]")
    lines.append("On-screen text of any kind (subtitles, captions, titles, credits, watermarks, logos, TV graphics, digital clock readouts), letterbox bars, jump cuts or scene changes, extra people, extra or fused fingers, face or costume changes, slurred or sped-up speech, Southern or Central Vietnamese accents.")
    return "\n".join(lines) + "\n"


def validate(data: dict) -> tuple[list[str], list[str]]:
    errors, warns = [], []
    chars = data["characters"]
    for sc in data["scenes"]:
        for i, c in enumerate(sc["clips"]):
            cid = c["id"]
            if len(c["beats"]) != 3:
                errors.append(f"{cid}: needs exactly 3 beats")
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
            rate = data["narrator"]["rate"] if c["speaker"] == "NARRATOR" else chars[c["speaker"]]["rate"]
            if speech_window(c["line"], rate)[1] > 8.5:
                warns.append(f"{cid}: line runs past 8.5s")
    return errors, warns


def scene_table(data: dict, sc: dict, conts: list[str]) -> list[str]:
    rows = ["| Clip | Nhân Vật | Giọng | Âm tiết | Khung thoại | Lời Dẫn / Thoại | Camera | Cách tạo trên Flow |",
            "|---|---|---|---|---|---|---|---|"]
    for c, cont in zip(sc["clips"], conts):
        n = int(c["id"].split(".")[1])
        rate = data["narrator"]["rate"] if c["speaker"] == "NARRATOR" else data["characters"][c["speaker"]]["rate"]
        a, b = speech_window(c["line"], rate)
        mode = "VO" if c["speaker"] == "NARRATOR" else f"LIPSYNC:{c['speaker']}"
        who = ", ".join(f"`{t}`" for t in c["chars"]) or "—"
        rows.append(f"| [**Clip {n}**](clip-{n}.md) | {who} | `{mode}` | **{syllables(c['line'])}** | `{a:.1f}–{b:.1f}s` | \"{c['line']}\" | {c['camera']} | {flow_mode(c, cont)} |")
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
    vo = sum(1 for sc in data["scenes"] for c in sc["clips"] if c["speaker"] == "NARRATOR")
    modes = [flow_mode(c, all_conts[sc["num"]][i]) for sc in data["scenes"] for i, c in enumerate(sc["clips"])]
    print(f"{series}: {len(prompts)} clips, {vo} VO + {len(prompts) - vo} lip-sync; prompt length {min(lens)}–{max(lens)} chars (avg {sum(lens)//len(lens)})")
    for m in sorted(set(modes)):
        print(f"  {modes.count(m):3d} × {m}")
    if check_only:
        return 0

    total = len(prompts)
    n_frames = sum(1 for m in modes if m.startswith("Frames"))
    n_ingr = sum(1 for m in modes if m.startswith("Ingredients"))
    n_t2v = total - n_frames - n_ingr
    voice_bullets = [
        f"- **Giọng Người Dẫn Chuyện (cố định cả {total} clip):** {data['narrator']['voice']}. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; nhịp ~{data['narrator']['rate']:.0f} âm tiết/giây.",
        "- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.",
        f"- **Mật độ:** {total} clips × 10s — {vo} clip VO + {total - vo} clip thoại; lời nói nằm trong khung riêng bắt đầu từ {SPEECH_START:.1f}s (xem cột *Khung thoại*).",
        f"- **Cách tạo trên Flow (runner tự chọn):** {n_frames} clip nối khung cuối (Frames), {n_ingr} clip ảnh nhân vật (Ingredients), {n_t2v} clip chỉ text.",
        "- **Hậu kỳ runner:** `atempo` tăng tốc giọng chỉ áp dụng cho clip VO; clip lip-sync giữ nguyên tốc độ để khớp khẩu hình.",
        f"- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py {series}` sinh lại toàn bộ clip, README, kịch bản.",
    ]

    for sc in data["scenes"]:
        d = os.path.join(sdir, f"canh-{sc['num']:02d}")
        for c in sc["clips"]:
            n = int(c["id"].split(".")[1])
            with open(os.path.join(d, f"clip-{n}.md"), "w", encoding="utf-8") as f:
                f.write(prompts[c["id"]])
        readme = [f"# Cảnh {sc['num']:02d}: {sc['title']} (6 Clips × 10s = 60s)", "",
                  f"- **Thời gian:** {sc['time_label']}",
                  f"- **Bối cảnh:** {sc['location']}",
                  f"- **Trục không gian cố định:** {sc['axis']}",
                  f"- **Đạo cụ chính:** {sc['props']}", ""]
        readme += scene_table(data, sc, all_conts[sc["num"]])
        with open(os.path.join(d, "README.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(readme) + "\n")

    kb = [f"# KỊCH BẢN CHI TIẾT 15 PHÚT: {data['title'].upper()}", ""] + voice_bullets[:1] + [""]
    for sc in data["scenes"]:
        kb += [f"## Cảnh {sc['num']:02d}: {sc['title']} ({sc['time_label']})", f"- **Bối cảnh:** {sc['location']}", ""]
        for c in sc["clips"]:
            n = int(c["id"].split(".")[1])
            mode = "VO" if c["speaker"] == "NARRATOR" else f"LIPSYNC:{c['speaker']}"
            kb.append(f"- **[Clip {c['id']}](canh-{sc['num']:02d}/clip-{n}.md)** (`{mode}` | `{syllables(c['line'])} âm tiết`): \"{c['line']}\"")
        kb.append("")
    with open(os.path.join(sdir, "KICH_BAN_15_PHUT.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(kb))

    rd = [f"# {data['title']} (15 Cảnh × 6 Clips × 10s = 15 Phút)", ""] + voice_bullets + ["", "## Danh Sách 15 Cảnh (90 Clips × 10s)", "",
          "| Cảnh | Tiêu Đề | Thời Gian | Đường Dẫn |", "|---|---|---|---|"]
    for sc in data["scenes"]:
        rd.append(f"| **Cảnh {sc['num']:02d}** | {sc['title']} | {sc['time_label']} | [`canh-{sc['num']:02d}/`](canh-{sc['num']:02d}/README.md) |")
    with open(os.path.join(sdir, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(rd) + "\n")

    fp = [f"# {data['title']} — Bộ {total} Prompt Google Flow Omni (15 Cảnh × 6 Clips × 10s)", ""] + voice_bullets + [""]
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
