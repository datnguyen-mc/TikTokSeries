#!/usr/bin/env python3
"""Bản 15 giây — gom các shot 3–5s của mỗi phần thành clip 15 giây nhiều shot (cắt cứng), giọng A có nhấn giọng Hà Nội.

    python3 _v2/build_15s.py

Ra: flow_15s/pNN/NN-C.txt (prompt dán vào Flow) và flow_15s/manifest.json (nhân vật cần gắn, shot gốc, thoại).
Mỗi phần chia thành ceil(tổng/15) clip, cắt ở ranh giới shot sao cho các clip đều nhau; độ dài shot co giãn cho đủ 15s,
shot có thoại luôn đủ thời gian nói."""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SDIR = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from build_v2 import PARTS, PACE, SFX, SIZE, MOVE, speech_secs, look_of  # noqa: E402
from looks import FACE, NAME, ROLE, VOICE, LOOKS, PLACE  # noqa: E402

DUR = 15
STYLE = ("Photorealistic live-action Vietnamese romantic comedy-drama with a thriller edge, shot on ARRI Alexa 35 with anamorphic lenses, "
         "24 fps; rich teal-and-amber grade, motivated practical light, natural skin texture with pores, subtle 35mm film grain, shallow depth of field "
         "with creamy oval bokeh, gentle halation. Real actors, believable understated performances, a premium theatrical feature — never CGI, never an advertisement.")
AVOID = ("On-screen text of any kind (subtitles, captions, titles, watermarks, logos), readable writing, blurry faces, distorted hands, background music, "
         "letterbox bars, cuts at any other moment, extra people in focus, face, hair or costume changes, robotic or text-to-speech sounding voices, "
         "flat monotone delivery, slurred speech, repeated, stuttered or echoed words, the line spoken twice, an off-screen narrator or voice-over, "
         "Southern or Central Vietnamese accents.")


def need(s):
    """Thời lượng tối thiểu của shot (giây)."""
    if s["say"]:
        n, pace, _, line = s["say"]
        return 0.3 + speech_secs(n, pace, line) + 0.5
    return 1.5


def key(part, s, w):
    return (w, look_of(part, s, w))


def partition(part):
    sh = part["shots"]
    n = len(sh)
    total = sum(s["d"] for s in sh)
    for k in range(math.ceil(total / DUR), n + 1):
        tgt = total / k
        INF = float("inf")
        best = [[INF] * (n + 1) for _ in range(k + 1)]
        prev = [[None] * (n + 1) for _ in range(k + 1)]
        best[0][0] = 0
        for g in range(1, k + 1):
            for j in range(1, n + 1):
                for i in range(j - 1, -1, -1):
                    grp = sh[i:j]
                    raw = sum(s["d"] for s in grp)
                    if raw > DUR + 1.5 or sum(need(s) for s in grp) > DUR:
                        break
                    if best[g - 1][i] == INF:
                        continue
                    looks = {}
                    clash = False
                    for s in grp:
                        for w in s["who"]:
                            lk = look_of(part, s, w)
                            if looks.setdefault(w, lk) != lk:
                                clash = True
                    if clash or len(looks) > 3:
                        continue
                    locs = len({s["loc"] or part["loc"] for s in grp})
                    c = best[g - 1][i] + (raw - tgt) ** 2 + 8 * (locs - 1)
                    if c < best[g][j]:
                        best[g][j] = c
                        prev[g][j] = i
        if best[k][n] < INF:
            cuts, j = [], n
            for g in range(k, 0, -1):
                i = prev[g][j]
                cuts.append((i, j))
                j = i
            return [sh[i:j] for i, j in reversed(cuts)]
    raise SystemExit(f"P{part['num']}: không chia được")


def timing(grp):
    raw = sum(s["d"] for s in grp)
    d = [max(s["d"] * DUR / raw, need(s)) for s in grp]
    # trả phần dư/thiếu về các shot còn dư thời gian
    for _ in range(50):
        diff = DUR - sum(d)
        if abs(diff) < 1e-6:
            break
        free = [i for i in range(len(d)) if diff > 0 or d[i] - need(grp[i]) > 0.01]
        for i in free:
            d[i] += diff / len(free)
            d[i] = max(d[i], need(grp[i]))
    # làm tròn mốc cắt về 0.5s
    t, edges = 0.0, [0.0]
    for x in d[:-1]:
        t += x
        edges.append(round(t * 2) / 2)
    edges.append(float(DUR))
    return edges


def fmt(x):
    return f"{x:g}"


def char_line(w, code):
    _, flow, outfit = LOOKS[code]
    return f"- @{w} = {NAME[w]}, {ROLE[w]}: {FACE[w]}; wears {outfit}. Attached image: \"{flow}\"."


def build(part, grp):
    edges = timing(grp)
    locs = []
    for s in grp:
        l = s["loc"] or part["loc"]
        if l not in locs:
            locs.append(l)
    main = max(locs, key=lambda l: sum(s["d"] for s in grp if (s["loc"] or part["loc"]) == l))
    chars = []
    for s in grp:
        order = ([s["say"][0]] if s["say"] else []) + s["who"]
        for w in order:
            if w in s["who"] and w not in [c[0] for c in chars]:
                chars.append((w, look_of(part, s, w)))
    n = len(grp)
    cuts = ", ".join(fmt(e) + "s" for e in edges[1:-1])
    one_place = len(locs) == 1
    L = [f"A {DUR}-second live-action film sequence of {n} shots, 16:9 widescreen, 24 fps, with hard cuts only at {cuts}; "
         + ("one place and one moment, sound and action continuous across the cuts." if one_place else "sound and action continuous across the cuts."), "",
         "[STYLE]", STYLE, "", "[LOCATION]"]
    for l in locs:
        desc = PLACE[l][1]
        L.append((desc[0].upper() + desc[1:] + ".") if one_place else f"- {PLACE[l][0][0].upper() + PLACE[l][0][1:]}: {desc}.")
    L += ["", "[CHARACTERS]"]
    if chars:
        L.append("Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, "
                 "and never flash the studio reference portrait; the characters are already in place in the very first frame.")
        L += [char_line(w, c) for w, c in chars]
        L.append("Nobody else appears in focus.")
    else:
        L.append("No named characters; any people in frame are distant, blurred and unidentifiable.")
    L += ["", "[SHOT LIST — hard cuts only at the marked seconds]"]
    turns, tl = [], []
    for i, s in enumerate(grp):
        a, b = edges[i], edges[i + 1]
        loc = s["loc"] or part["loc"]
        size, move = (s["cam"].split() + ["static"])[:2]
        say = s["say"]
        sa = say[0] if say else (s["who"][0] if s["who"] else None)
        sb = next((w for w in s["who"] if w != sa), None)
        cam = SIZE[size].format(a=ROLE[sa] if sa else "", b=ROLE[sb] if sb else "", place=PLACE[loc][0])
        where = "" if one_place else f" (in {PLACE[loc][0]})"
        L.append(f"- Shot {i + 1}, {fmt(a)}–{fmt(b)}s{where}: {cam}, {MOVE[move]}.")
        act = s["act"].rstrip(".")
        cut = "" if i == 0 else "CUT to "
        line = f"- {fmt(a)}–{fmt(b)}s ({cut}Shot {i + 1}): {act}"
        if say:
            w, pace, tone, txt = say
            st = round(a + 0.3, 1)
            en = round(st + speech_secs(w, pace, txt), 1)
            en = min(en, round(b - 0.2, 1))
            turns.append((w, st, en, f"{PACE[pace][1]}, {tone}", txt))
            line += f"; @{w} speaks, face clearly on screen."
        else:
            line += ". No one speaks."
        if i == n - 1:
            line += " The sequence settles on this as its final frame."
        tl.append(line)
    L.append("- Whoever is speaking has the face clearly on screen in that shot; the camera keeps one side of the line so eyelines match across the cuts.")
    L += ["", "[TIMELINE — second by second]", "Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per beat."] + tl
    L += ["", "[AUDIO]"]
    if turns:
        L.append(f"- Dialogue in Vietnamese with exact lip-sync, {len(turns)} spoken turn{'s' if len(turns) > 1 else ''} in this order, each said exactly once (no subtitles):")
        for k, (w, st, en, how, txt) in enumerate(turns, 1):
            L.append(f"- Turn {k}, {fmt(st)}–{fmt(en)}s, spoken on camera by @{w} ({VOICE[w]}, {how}): \"{txt}\"")
        end = max(t[2] for t in turns)
        L += ["- Throughout, only the person whose turn it is moves the lips while anyone else listens with the mouth closed; real breaths and tiny natural "
              "hesitations, recorded close on set with a little room tone — it sounds like real actors talking, never like a voice-over or text-to-speech.",
              "- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, "
              "and different characters sound clearly different in pitch, age and texture.",
              f"- All speech is over by {fmt(end)}s; outside the turns above nobody says a word, and no line is ever repeated to fill the time.",
              "- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud."]
    else:
        L.append("- No dialogue: every mouth stays closed, no voices at all.")
    sfx = "; ".join(SFX[l] for l in locs)
    L += [f"- SFX: {sfx}. No music.", "", "[AVOID]", AVOID]
    return "\n".join(L) + "\n", chars, turns, edges


def main():
    out = os.path.join(SDIR, "flow_15s")
    os.makedirs(out, exist_ok=True)
    man = []
    total = 0
    for part in PARTS:
        pdir = os.path.join(out, f"p{part['num']:02d}")
        os.makedirs(pdir, exist_ok=True)
        k0 = 0
        for c, grp in enumerate(partition(part), 1):
            txt, chars, turns, edges = build(part, grp)
            cid = f"{part['num']:02d}-{c}"
            with open(os.path.join(pdir, f"{cid}.txt"), "w", encoding="utf-8") as f:
                f.write(txt)
            ids = [f"{part['num']:02d}-{k0 + i + 1:02d}" for i in range(len(grp))]
            k0 += len(grp)
            man.append(dict(id=cid, part=part["num"], title=part["title"], dur=DUR, shots=ids, edges=edges,
                            chars=[LOOKS[code][1] for _, code in chars], chars_n=len(chars),
                            lines=[f"{NAME[w]}: {t}" for w, _, _, _, t in turns], prompt_chars=len(txt),
                            flow_name=f"P{part['num']:02d}-C{c} · {part['title']}"))
            total += 1
    with open(os.path.join(out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(man, f, ensure_ascii=False, indent=1)
    print(f"{total} clip × {DUR}s = {total * DUR / 60:.1f} phút, {total * 45} tín dụng")
    for m in man:
        print(m["id"], len(m["shots"]), "shot", m["chars_n"], "nv", m["prompt_chars"], "ký tự", "|", ", ".join(m["chars"]))


if __name__ == "__main__":
    main()
