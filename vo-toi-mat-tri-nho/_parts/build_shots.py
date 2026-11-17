#!/usr/bin/env python3
"""Tách phim thành CẢNH QUAY ĐIỆN ẢNH 3–5 giây cho tính năng "Cảnh" (Scene) của Flow web.

Mỗi clip 15s trong kịch bản (3 lượt thoại) thành 3–5 cảnh quay ngắn, mỗi cảnh quay một góc máy duy nhất,
một người nói (hoặc im lặng), rồi ghép lại trên timeline "Cảnh" của Flow:
  - cảnh đầu của mỗi cảnh phim có 1 shot toàn cảnh 3s (establishing, không thoại);
  - mỗi lượt thoại là 1 shot (câu dài hơn 5s được tách theo câu thành 2 shot đổi góc máy);
  - clip có nhịp im lặng cuối thì thêm 1 shot phản ứng 3s.

    python3 vo-toi-mat-tri-nho/_parts/build_shots.py            # cả phim
    python3 vo-toi-mat-tri-nho/_parts/build_shots.py 01.1 01.2  # khoảng clip

Ra: vo-toi-mat-tri-nho/flow_shots/<cảnh>/<clip>-<shot>.txt + SHOT_LIST.md (thời lượng, nhân vật cần gắn).
"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SDIR = os.path.dirname(HERE)
REPO = os.path.dirname(SDIR)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "flowkit", "scripts"))
import build_omni_horror_prompts as B  # noqa: E402
import header_data as H  # noqa: E402
from scenes_act1 import SCENES as A1  # noqa: E402
from scenes_act2 import SCENES as A2  # noqa: E402
from scenes_act3 import SCENES as A3  # noqa: E402

MIN_S, MAX_S = 3, 5
LOOK = ("Cinematic live-action film still in motion, shot on ARRI Alexa 35 with vintage anamorphic lenses, 24 fps, 16:9; "
        "real actors with natural skin texture, pores and micro-expressions, believable performances, motivated practical lighting, "
        "soft contrast, rich teal-and-amber grade, gentle halation, subtle 35mm film grain, shallow depth of field with creamy bokeh. "
        "Looks like a premium Vietnamese theatrical romantic comedy-drama, never like CGI, a video game or an advertisement.")
AVOID = ("On-screen text, subtitles, captions, logos, watermarks, readable writing on paper or screens; cuts or a second camera angle; "
         "extra people; distorted hands or fused fingers; face, hair or costume changes; plastic or waxy skin; "
         "repeated, echoed or stuttered words; an off-screen narrator; background music; Southern or Central Vietnamese accents.")

NOUN = H.NOUN


def secs(line: str, pace: str, tag: str) -> float:
    rate = H.CHARACTERS[tag]["rate"] * B.PACES[pace][0]
    return B.syllables(line) / rate


def split_sentences(line: str) -> list[str]:
    parts = [p.strip() for p in re.split(r"(?<=[.!?…])\s+", line) if p.strip()]
    return parts or [line]


def chunk_line(line: str, pace: str, tag: str) -> list[str]:
    """Câu nói vừa 1 shot (≤ MAX_S) thì giữ; dài hơn thì gom câu thành nhiều shot."""
    if secs(line, pace, tag) + 0.7 <= MAX_S:
        return [line]
    out, cur = [], ""
    for s in split_sentences(line):
        cand = (cur + " " + s).strip()
        if cur and secs(cand, pace, tag) + 0.8 > MAX_S:
            out.append(cur)
            cur = s
        else:
            cur = cand
    if cur:
        out.append(cur)
    final = []  # một câu vẫn quá dài thì tách tiếp ở dấu phẩy
    for piece in out:
        if secs(piece, pace, tag) + 0.8 <= MAX_S or "," not in piece:
            final.append(piece)
            continue
        cur = ""
        for c in [x.strip() for x in piece.split(",")]:
            cand = (cur + ", " + c) if cur else c
            if cur and secs(cand, pace, tag) + 0.8 > MAX_S:
                final.append(cur + ",")
                cur = c
            else:
                cur = cand
        final.append(cur)
    return final


CAMS = {
    "close": ("85mm close-up of {sp}, eyes in sharp focus, background melting into bokeh", "a slow, almost imperceptible push-in"),
    "ots": ("50mm over-the-shoulder shot from behind {li}'s blurred shoulder onto {sp}", "a gentle handheld float"),
    "two": ("35mm medium two-shot of {sp} and {li}, both faces readable", "a slow lateral dolly"),
    "medium": ("50mm medium shot of {sp}, waist up", "a slow dolly-in"),
    "react": ("50mm medium shot of {sp} in a silent beat", "locked off, a hint of breathing movement"),
    "wide": ("24mm wide establishing shot of {place}", "a slow crane-down drift"),
}
ROTATION = ["two", "close", "ots", "close", "medium", "ots"]


def outfit(sc: dict, cl: dict, tag: str) -> str:
    ward = dict(sc.get("wardrobe") or {})
    ward.update(cl.get("wardrobe") or {})
    if ward.get(tag):
        return H.W[ward[tag]]
    return H.CHARACTERS[tag]["anchor"].split("; ")[-1].rstrip(".")


def who_block(sc, cl, tags) -> str:
    lines = ["[CHARACTERS] Use the attached character images for faces and hair; keep them exactly the same."]
    for t in tags:
        lines.append(f"- {t} = {H.CHARACTERS[t]['name']}, {NOUN[t].replace('the ', '')}; wears {outfit(sc, cl, t)}.")
    lines.append("Nobody else is in frame.")
    return "\n".join(lines)


def shot_prompt(sc, cl, setting, d, kind, sp, li, action, react, line=None, pace=None, tone=None, sfx=""):
    tags = [t for t in (sp, li) if t] if kind in ("ots", "two") else [t for t in (sp,) if t]
    cam, move = CAMS[kind]
    cam = cam.format(sp=NOUN.get(sp, ""), li=NOUN.get(li, "") if li else "", place=sc["room"])
    parts = [f"A single continuous {d}-second shot, one camera angle, no cuts.", "", "[LOOK] " + LOOK, "",
             "[PLACE] " + setting, ""]
    if tags:
        parts += [who_block(sc, cl, tags), ""]
    else:
        parts += ["[CHARACTERS] No people in frame.", ""]
    parts += [f"[CAMERA] {cam}; {move}; framing holds steady for the whole shot.", ""]
    if line:
        end = round(0.3 + secs(line, pace, sp), 1)
        voice = f"{H.CHARACTERS[sp]['voice']}, {B.PACES[pace][2]}, {tone}"
        parts += [f"[ACTION] {sp} is {action}" + (f"; {react}" if react and li in tags else "") + ".", "",
                  f"[DIALOGUE] In Vietnamese with exact lip-sync, spoken on camera by {sp} ({voice}), said exactly once from 0.3s to {end}s: \"{line}\"",
                  f"After the last word {sp} closes the mouth; nobody speaks again until {d}.0s."
                  + (f" {li} listens with the mouth closed." if li and li in tags else ""),
                  "Standard Northern Vietnamese accent; never read these directions or names aloud.", ""]
    else:
        parts += [f"[ACTION] {(sp + ' ') if sp and '@' not in action else ''}{action.rstrip('.')}.", "", "[DIALOGUE] None. Every mouth stays closed; no voices at all.", ""]
    parts += [f"[SOUND] {sfx}. No music.", "", "[AVOID] " + AVOID]
    return "\n".join(parts) + "\n", tags


def build(lo="00.0", hi="99.9"):
    out_dir = os.path.join(SDIR, "flow_shots")
    os.makedirs(out_dir, exist_ok=True)
    table, total, n = [], 0.0, 0
    for sc in A1 + A2 + A3:
        sc_dir = os.path.join(out_dir, f"canh-{sc['num']:02d}")
        for i, cl in enumerate(sc["clips"]):
            cid = f"{sc['num']:02d}.{i + 1}"
            if not (lo <= cid <= hi):
                continue
            os.makedirs(sc_dir, exist_ok=True)
            setting = H.S[cl["set"]] if cl.get("set") else H.S[sc["setting"]]
            sfx = cl.get("sfx", sc["sfx"])
            shots = []
            if i == 0 or cl.get("set"):
                shots.append(dict(d=3, kind="wide", sp=None, li=None,
                                  action=f"The camera reveals {sc['room']} in its own light; the space is still and waiting, nobody in frame yet.", react=None))
            rot = (sc["num"] + i) % len(ROTATION)
            for k, (sp, pace, tone, line) in enumerate(cl["t"]):
                li = next((c for c in cl["c"] if c != sp), None)
                acts = cl["a"][k]
                for j, piece in enumerate(chunk_line(line, pace, sp)):
                    kind = ROTATION[rot % len(ROTATION)]
                    rot += 1
                    d = min(MAX_S + 1, max(MIN_S, math.ceil(0.3 + secs(piece, pace, sp) + 0.4)))
                    act = acts[min(j, len(acts) - 1)]
                    react = f"{li} watches, mouth closed" if li else None
                    shots.append(dict(d=d, kind=kind, sp=sp, li=li, action=act, react=react, line=piece, pace=pace, tone=tone))
            if cl.get("tail"):
                t0 = cl["tail"][0]
                who = re.findall(r"@[A-Za-z]\w*", t0)
                sp = who[0] if who else cl["c"][0]
                shots.append(dict(d=3, kind="react", sp=sp, li=None, action=t0.rstrip("."), react=None))
            for s_no, s in enumerate(shots, 1):
                text, tags = shot_prompt(sc, cl, setting, s["d"], s["kind"], s["sp"], s["li"], s["action"], s["react"],
                                         s.get("line"), s.get("pace"), s.get("tone"), sfx)
                if s["d"] > MAX_S:
                    print(f"WARN {cid}-{s_no}: {s['d']}s (> {MAX_S}s)")
                name = f"{cid}-{s_no}"
                with open(os.path.join(sc_dir, name + ".txt"), "w", encoding="utf-8") as f:
                    f.write(text)
                m, sec = divmod(total, 60)
                table.append(f"| {int(m):02d}:{sec:04.1f} | `{name}` | {s['d']}s | {s['kind']} | {', '.join(H.CHARACTERS[t]['name'] for t in tags) or '— (chỉ text)'} | "
                             + (f"{s['sp']}: {s['line']}" if s.get("line") else "*(im lặng)* " + s["action"][:80]) + " |")
                total += s["d"]
                n += 1
    with open(os.path.join(out_dir, "SHOT_LIST.md"), "w", encoding="utf-8") as f:
        f.write(f"# {H.TITLE} — danh sách cảnh quay {MIN_S}–{MAX_S}s cho Flow \"Cảnh\" ({n} shot, {total:.0f}s)\n\n"
                "Tạo từng shot trên Flow: Video · Thành phần (gắn đúng nhân vật ở cột *Gắn*) · 16:9 · Omni 1.2 Flash · độ dài như cột *Dài*; "
                "shot không có nhân vật thì tạo chỉ bằng text. Sau đó thả các shot theo thứ tự vào timeline của Cảnh.\n\n"
                "| Mốc | Shot | Dài | Góc máy | Gắn | Thoại / hành động |\n|---|---|---|---|---|---|\n" + "\n".join(table) + "\n")
    print(f"{n} shot, {total:.0f}s → {out_dir}")


if __name__ == "__main__":
    a = sys.argv[1:]
    build(*(a[:2] if len(a) >= 2 else []))
