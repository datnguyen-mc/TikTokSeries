#!/usr/bin/env python3
"""Bản 3 — 3 phút đầu (P1–P3): shot 3–5s, giọng A nhấn giọng Hà Nội, nhân vật & bối cảnh gắn ảnh tham chiếu bản điện ảnh.

    python3 _v2/build_v3.py
Ra: flow_v3/pNN/NN-SS.txt, flow_v3/manifest.json, KICH_BAN_V3_P1-3.md, ANH_THAM_CHIEU_V3.md"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SDIR = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from build_v2 import PACE, SFX, SIZE, MOVE, CAM_VI, MOVE_VI, TAG, speech_secs, look_of  # noqa
from looks import FACE, NAME, ROLE, VOICE, LOOKS, PLACE  # noqa
from parts_v3 import PARTS  # noqa

SUFFIX = ""  # làm lại ảnh ngay trên nhân vật gốc (Flow giữ lịch sử ảnh)
SET_NAME = {"B1": "Bối cảnh · Sân thượng", "B2": "Bối cảnh · Sảnh khách sạn", "B3": "Bối cảnh · Phòng bệnh VIP",
            "B4": "Bối cảnh · Hành lang bệnh viện", "B23": "Bối cảnh · Hành lang kính"}
LOOK = ("A frame from a premium Vietnamese theatrical feature film, shot on ARRI Alexa 35 with vintage anamorphic lenses, 24 fps, 16:9: "
        "real film actors with natural skin texture, pores and micro-expressions, subtle restrained performances, motivated practical key light with soft "
        "negative fill, deep shadows and glowing highlights, rich teal-and-amber grade, gentle halation, fine 35mm film grain, shallow depth of field with "
        "creamy oval bokeh. Romantic comedy-drama with a thriller edge — never CGI, never a video game, never an advertisement, never a TV soap look.")
AVOID = ("On-screen text, subtitles, captions, logos, watermarks, readable writing on paper, screens or signs; any cut or second camera angle; extra people "
         "in focus; distorted hands or fused fingers; face, hair or costume changes; plastic or waxy skin; flat TV lighting; robotic or text-to-speech "
         "sounding voices; flat monotone delivery; repeated, echoed or stuttered words; an off-screen narrator; background music; "
         "Southern or Central Vietnamese accents.")


def render(part, s, d):
    loc = s["loc"] or part["loc"]
    place_short, place = PLACE[loc]
    size, move = (s["cam"].split() + ["static"])[:2]
    who, say = s["who"], s["say"]
    a = say[0] if say else (who[0] if who else None)
    b = next((w for w in who if w != a), None)
    subj = lambda n: f"{TAG[n]} ({ROLE[n]})"
    cam = SIZE[size].format(a=subj(a) if a else "", b=subj(b) if b else "", place=place_short)
    L = [f"A single continuous {d}-second shot, 16:9, one camera angle, no cuts.", "", "[LOOK] " + LOOK, "",
         f"[PLACE] {place[0].upper() + place[1:]}. The attached image \"{SET_NAME[loc]}\" shows this exact set: match its architecture, furniture, "
         "colours and light, seen from this shot's camera angle; never show the reference image itself.", ""]
    if who:
        L.append("[CHARACTERS] Use the attached character image for each person: same face, same hair, same outfit, exactly; only face and clothes come from it, never its background.")
        for w in who:
            code = look_of(part, s, w)
            L.append(f"- {TAG[w]} = {NAME[w]}, {ROLE[w]}: {FACE[w]}; wears {LOOKS[code][2]}. Attached image: \"{LOOKS[code][1]}{SUFFIX}\".")
        L.append("Nobody else is in focus.")
    else:
        L.append("[CHARACTERS] No named characters; any people in frame are distant, blurred and unidentifiable.")
    L += ["", f"[CAMERA] {cam}; {MOVE[move]}.", "", f"[ACTION] {s['act'].rstrip('.')}.", ""]
    if say:
        n, pace, tone, line = say
        end = round(0.3 + speech_secs(n, pace, line), 1)
        L += [f"[DIALOGUE] In Vietnamese with exact lip-sync, spoken on camera by {TAG[n]} ({VOICE[n]}, {PACE[pace][1]}, {tone}), "
              f"said exactly once from 0.3s to {end}s: \"{line}\"",
              f"Only {TAG[n]} moves the lips" + (f"; {TAG[b]} listens with the mouth closed" if b else "") + f". After the last word nobody speaks again until {d}.0s.",
              "Voice: standard Hà Nội Northern Vietnamese with natural Northern tones (never Southern or Central accents); a real actor recorded close on set with a little "
              "room tone, real breaths and tiny natural hesitations — never a voice-over or text-to-speech. Speak only the Vietnamese words inside the double quotes, "
              "once; never read these directions, names or tags aloud.", ""]
    else:
        L += ["[DIALOGUE] None. Every mouth stays closed; no voices at all.", ""]
    L += [f"[SOUND] {SFX[loc]}. No music.", "", "[AVOID] " + AVOID]
    return "\n".join(L) + "\n"


def main():
    out = os.path.join(SDIR, "flow_v3"); os.makedirs(out, exist_ok=True)
    man, kb, total = [], ["# KỊCH BẢN BẢN 3 — 3 phút đầu (Phần 1–3)", "",
                         "Shot 3–5 giây, cắt nhanh, nhiều thoại hơn bản 2. Dòng **in đậm** trong cột Thoại là câu mới thêm ở bản 3.", ""], 0
    old = {}
    from parts1 import PARTS as OLD
    for p in OLD[:3]:
        old[p["num"]] = {x["say"][3] for x in p["shots"] if x["say"]}
    used_looks, used_sets = {}, {}
    for part in PARTS:
        pdir = os.path.join(out, f"p{part['num']:02d}"); os.makedirs(pdir, exist_ok=True)
        ptot = sum(x["d"] for x in part["shots"])
        kb += [f"## Phần {part['num']} · {part['title']} ({ptot} giây)", "", f"- **Móc:** {part['hook']}", f"- **Câu treo:** {part['cliff']}",
               f"- **Chuyển cảnh:** {part['tr']}", "", "| Mốc | Shot | Dài | Máy quay | Ai trong khung | Hành động | Thoại |", "|---|---|---|---|---|---|---|"]
        for k, s in enumerate(part["shots"], 1):
            sid = f"{part['num']:02d}-{k:02d}"; d = s["d"]
            if s["say"]:
                d = max(d, math.ceil(0.3 + speech_secs(s["say"][0], s["say"][1], s["say"][3]) + 0.4))
            txt = render(part, s, d)
            open(os.path.join(pdir, f"{sid}.txt"), "w", encoding="utf-8").write(txt)
            loc = s["loc"] or part["loc"]
            chars = [LOOKS[look_of(part, s, w)][1] + SUFFIX for w in s["who"]]
            for w in s["who"]:
                used_looks[look_of(part, s, w)] = 1
            used_sets[loc] = 1
            man.append(dict(id=sid, dur=d, set=SET_NAME[loc], chars=chars, ingredients=[SET_NAME[loc]] + chars,
                            line=(f"{NAME[s['say'][0]]}: {s['say'][3]}" if s["say"] else ""), n=len(txt)))
            size, move = (s["cam"].split() + ["static"])[:2]
            mm, ss = divmod(total, 60)
            line = "—"
            if s["say"]:
                t = s["say"][3]; line = f"{NAME[s['say'][0]]}: " + (t if t in old[part["num"]] else f"**{t}**")
            kb.append(f"| {mm}:{ss:02d} | `{sid}` | {d}s | {CAM_VI[size]}, {MOVE_VI[move]} | {', '.join(NAME[w] for w in s['who']) or '—'} | {s['act'].rstrip('.')} | {line} |")
            total += d
        kb.append("")
    kb.insert(2, f"Tổng: {len(man)} shot, {total // 60} phút {total % 60} giây.\n")
    json.dump(man, open(os.path.join(out, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(os.path.join(SDIR, "KICH_BAN_V3_P1-3.md"), "w", encoding="utf-8").write("\n".join(kb) + "\n")
    # ảnh tham chiếu
    R = ["# Ảnh tham chiếu bản 3 (điện ảnh)", "", "## Nhân vật — tạo lại từ nhân vật cũ (giữ mặt), tạo ảnh mới ngay trên nhân vật gốc (Flow giữ lịch sử, có thể quay lại ảnh cũ)", ""]
    for code in used_looks:
        w, flow, outfit = LOOKS[code]
        R += [f"### {flow}{SUFFIX}  ← từ \"{flow}\"", "```",
              f"Keep exactly the same person and face as the reference: {FACE[w]}. Re-shoot as a cinematic full-body character still for a premium feature film: "
              f"wearing {outfit}; natural relaxed actor pose, three-quarter angle, face clearly visible; soft motivated key light from one side with gentle falloff, "
              "subtle rim light, natural skin texture with pores, no retouching gloss; plain dark-grey studio backdrop with soft vignette; shot on ARRI Alexa with an "
              "85mm lens, shallow depth of field, fine film grain, teal-and-amber grade. No text, no logo.", "```", ""]
    R += ["## Bối cảnh — ảnh tạo mới (không người)", ""]
    for loc in used_sets:
        R += [f"### {SET_NAME[loc]}", "```",
              f"Cinematic establishing still of an empty film set, no people: {PLACE[loc][1]}. Wide 24mm view showing the whole layout, shot on ARRI Alexa with "
              "anamorphic lenses, motivated practical lighting, rich teal-and-amber grade, fine film grain, 16:9. No text, no logo, no people.", "```", ""]
    open(os.path.join(SDIR, "ANH_THAM_CHIEU_V3.md"), "w", encoding="utf-8").write("\n".join(R) + "\n")
    print(f"{len(man)} shot, {total}s; nhân vật mới: {len(used_looks)}, bối cảnh: {len(used_sets)}")


if __name__ == "__main__":
    main()
