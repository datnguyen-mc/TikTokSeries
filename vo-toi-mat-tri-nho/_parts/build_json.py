#!/usr/bin/env python3
"""Sinh PHAN_CANH_OMNI.json cho "Vợ Tôi Mất Trí Nhớ Có Chọn Lọc" từ dàn ý thoại + hành động trong _parts/scenes_act*.py.

    python3 vo-toi-mat-tri-nho/_parts/build_json.py
    python3 flowkit/scripts/build_omni_horror_prompts.py vo-toi-mat-tri-nho

Mỗi clip trong scenes_act*.py chỉ cần: nhân vật (c), lượt thoại (t: speaker, pace, tone, line),
hành động theo từng lượt (a) và vài câu hành động im lặng cuối clip (tail). Script này tự tính khung thoại
theo đúng công thức của build_omni_horror_prompts.py rồi chia 15 bước (mỗi giây một bước) và 3–5 cảnh quay.
"""
import json
import os
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

D = 15
ADV = {"fast": "quickly", "normal": "at an easy conversational pace", "slow": "slowly and softly"}
FILL = ["holding {lis}'s gaze", "one hand moving lightly with the words", "leaning a little toward {lis}",
        "taking a quick breath between phrases", "eyebrows lifting on the key word", "never looking away from {lis}"]
MOVES = ["slow push-in", "locked off", "gentle handheld drift", "slow dolly-in", "subtle rack focus", "slow arc"]


def header() -> dict:
    return {"series": H.SERIES, "title": H.TITLE, "clip_seconds": D, "style": H.STYLE, "lighting": H.LIGHTING,
            "voice_common": H.VOICE_COMMON, "characters": H.CHARACTERS}


def owners(plan):
    """Which turn (or 'tail') owns each second 0..14."""
    out = []
    end = plan[-1][3]
    for k in range(D):
        mid = k + 0.5
        if mid > end + 0.2:
            out.append("tail")
            continue
        idx = 0
        for i, (_, _, a, _) in enumerate(plan):
            if a <= mid or i == 0:
                idx = i
        out.append(idx)
    return out


def build_steps(clip, plan, own):
    chars = clip["c"]
    steps = []
    seen = {}
    for k, o in enumerate(own):
        if o == "tail":
            continue
        seen.setdefault(o, []).append(k)
    for o, secs in seen.items():
        sp, _, _, _ = plan[o]
        tr = clip["t"][o]
        pace, tone = tr[1], tr[2]
        lis = next((c for c in chars if c != sp), None)
        acts = list(clip["a"][o])
        for j, k in enumerate(secs):
            if j == 0:
                g = acts.pop(0) if acts else "facing " + (lis or "the camera")
                if o == 0:
                    s = f"{sp} is {g} and is already speaking {ADV[pace]} ({tone})."
                else:
                    s = f"{sp} starts speaking {ADV[pace]} ({tone}), {g}" + (f", while {lis} listens with the mouth closed." if lis else ".")
            elif j == len(secs) - 1 and len(secs) > 1:
                g = acts.pop(0) if acts else None
                s = f"{sp} finishes the line and closes the mouth" + (f", {g}." if g else ".")
            else:
                g = acts.pop(0) if acts else FILL[(k + o) % len(FILL)].format(lis=lis or "the camera")
                s = f"{sp} keeps talking, {g}."
            steps.append((k, s))
    tail_secs = [k for k, o in enumerate(own) if o == "tail"]
    tails = list(clip["tail"])
    for j, k in enumerate(tail_secs):
        if j < len(tails):
            s = tails[j]
        else:
            s = ("Everyone holds still in silence, mouths closed, the moment hanging in the air."
                 if j < len(tail_secs) - 1 else
                 f"{' and '.join(chars)} stay silent, mouths closed, as the moment settles.")
        steps.append((k, s))
    steps.sort()
    assert [k for k, _ in steps] == list(range(D)), steps
    return [s for _, s in steps]


def segments(own):
    segs = []
    for k, o in enumerate(own):
        if segs and segs[-1][0] == o:
            segs[-1][2] = k + 1
        else:
            segs.append([o, k, k + 1])
    # merge segments shorter than 2s into the previous one (or the next one for the first)
    changed = True
    while changed:
        changed = False
        for i, (o, a, b) in enumerate(segs):
            if b - a < 2 and len(segs) > 1:
                if i > 0:
                    segs[i - 1][2] = b
                else:
                    segs[1][1] = a
                segs.pop(i)
                changed = True
                break
    while len(segs) < 3:  # split the longest segment
        i = max(range(len(segs)), key=lambda n: segs[n][2] - segs[n][1])
        o, a, b = segs[i]
        m = (a + b) // 2
        segs[i:i + 1] = [[o, a, m], [o, m, b]]
    while len(segs) > 5:
        segs[-2][2] = segs[-1][2]
        segs.pop()
    return segs


def camera(kind, sp, lis, room, move):
    n = H.NOUN
    if kind == "close":
        return f"85mm close-up of {n[sp]}, {move}"
    if kind == "ots" and lis:
        return f"50mm over-the-shoulder shot from behind {n[lis]} onto {n[sp]}, {move}"
    if kind == "medium":
        return f"50mm medium shot of {n[sp]} with {room} softly behind, {move}"
    if kind == "two" and lis:
        return f"35mm medium two-shot of {n[sp]} and {n[lis]}, {move}"
    if kind == "wide":
        return f"24mm wide shot of {room} with " + (f"{n[sp]} and {n[lis]}" if lis else n[sp]) + f", {move}"
    return f"40mm medium shot of {n[sp]}, {move}"


SCALE = {"close": "close-up", "ots": "over-the-shoulder", "medium": "medium", "two": "medium", "wide": "wide"}


def build_shots(clip, plan, own, room, seed):
    segs = segments(own)
    shots = []
    prev = None
    order = [["medium", "close", "ots"], ["close", "ots", "medium"], ["ots", "close", "medium"], ["two", "close", "ots"]][seed % 4]
    pi = 0
    chars = clip["c"]
    for j, (o, a, b) in enumerate(segs):
        last = j == len(segs) - 1
        if o == "tail":
            sp = plan[-1][0]
            kind = "wide" if SCALE.get(prev) != "wide" else "two"
        else:
            sp = plan[o][0]
            kind = None
            for _ in range(3):
                cand = order[pi % 3]
                pi += 1
                if SCALE[cand] != SCALE.get(prev):
                    kind = cand
                    break
            if kind is None:
                kind = "close" if SCALE.get(prev) != "close-up" else "medium"
            if last and b == D and own[-1] == "tail" and SCALE.get(prev) != "medium":
                kind = "two"  # last speaking shot that also holds the silent reaction
        lis = next((c for c in chars if c != sp), None)
        if kind in ("ots", "two") and not lis:
            kind = "close" if SCALE.get(prev) != "close-up" else "medium"
        move = MOVES[(seed + j) % len(MOVES)]
        shots.append({"until": b, "camera": camera(kind, sp, lis, room, move)})
        prev = kind
    return shots


def main() -> int:
    data = header()
    scenes = []
    seed = 0
    for sc in A1 + A2 + A3:
        setting = H.S[sc["setting"]]
        clips = []
        prev = None
        for i, cl in enumerate(sc["clips"]):
            seed += 1
            cid = f"{sc['num']:02d}.{i + 1}"
            csetting = H.S[cl["set"]] if cl.get("set") else setting
            turns = [{"speaker": s, "line": ln, "pace": p, "tone": tone} for s, p, tone, ln in cl["t"]]
            c = {"id": cid, "chars": cl["c"], "turns": turns}
            if csetting != setting:
                c["setting"] = csetting
            if prev and set(cl["c"]) <= set(prev["chars"]) and csetting == prev.get("setting", setting):
                c["continuity"] = "continuous"
            else:
                c["continuity"] = "cut"
            c["sfx"] = cl.get("sfx", sc["sfx"])
            ward = dict(sc.get("wardrobe") or {})
            ward.update(cl.get("wardrobe") or {})
            ward = {t: H.W[w] for t, w in ward.items() if w and t in cl["c"]}
            if ward:
                c["wardrobe"] = ward
            tmp = dict(c, _dialogue_only=True, steps=[""] * D)  # steps → talks_from_start: speech from 0.4s
            cont = "continuous" if c["continuity"] == "continuous" else "cut"
            plan = B.speech_plan(data, tmp, cont, D, clamp=False)
            own = owners(plan)
            c["shots"] = build_shots(cl, plan, own, sc["room"], seed)
            c["steps"] = build_steps(cl, plan, own)
            clips.append(c)
            prev = c
        scenes.append({k: sc[k] for k in ("num", "title", "time_label", "location", "axis", "props")} | {"setting": setting, "clips": clips})
    data["scenes"] = scenes
    out = os.path.join(SDIR, "PHAN_CANH_OMNI.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(os.path.join(HERE, "header.json"), "w", encoding="utf-8") as f:
        json.dump(header(), f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"wrote {out}: {len(scenes)} scenes, {sum(len(s['clips']) for s in scenes)} clips")
    return 0


if __name__ == "__main__":
    sys.exit(main())
