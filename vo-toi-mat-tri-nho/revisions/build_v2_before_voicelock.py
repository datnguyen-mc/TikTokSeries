#!/usr/bin/env python3
"""Bản 2 — sinh prompt từng shot (3–5s) cho Flow "Cảnh", kịch bản đọc được, danh sách shot và danh sách nhân vật theo bộ đồ.

    python3 vo-toi-mat-tri-nho/_v2/build_v2.py

Ra (trong vo-toi-mat-tri-nho/):
  flow_v2/pNN/NN-SS.txt   prompt dán vào Flow cho từng shot
  KICH_BAN_V2.md          kịch bản 25 phần: móc, câu treo, chuyển cảnh, từng shot (máy quay, hành động, thoại)
  SHOT_LIST_V2.md         bảng shot: mốc thời gian, độ dài, nhân vật cần gắn trên Flow
  NHAN_VAT_FLOW.md        36 nhân vật theo bộ đồ cần tạo trên Flow + prompt ảnh mẫu
"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SDIR = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from looks import FACE, NAME, ROLE, VOICE, RATE, LOOKS, PLACE  # noqa: E402
from parts1 import PARTS as A  # noqa: E402
from parts2 import PARTS as B  # noqa: E402
from parts3 import PARTS as C  # noqa: E402

PARTS = A + B + C
TAG = {k: "@" + k for k in NAME}
PACE = {"fast": (1.2, "speaking quickly in short lively phrases, every word clear"),
        "normal": (1.0, "speaking at a natural conversational pace"),
        "slow": (0.9, "speaking slowly and softly with small natural pauses")}
LOOK = ("Cinematic live-action film shot on ARRI Alexa 35 with vintage anamorphic lenses, 24 fps, 16:9; real actors with natural skin texture, "
        "pores and micro-expressions, believable understated performances, motivated practical lighting, soft contrast, rich teal-and-amber grade, "
        "gentle halation, subtle 35mm film grain, shallow depth of field with creamy oval bokeh. A premium Vietnamese theatrical romantic comedy-drama, "
        "never CGI, never a video game, never an advertisement.")
AVOID = ("On-screen text, subtitles, captions, logos, watermarks, readable writing on paper, screens or signs; any cut or second camera angle; extra people "
         "in focus; distorted hands or fused fingers; face, hair or costume changes; plastic or waxy skin; repeated, echoed or stuttered words; "
         "an off-screen narrator; background music; Southern or Central Vietnamese accents.")
SFX = {
    "B1": "a soft city hum far below, a light night breeze, candle flames fluttering, faint glassware",
    "B2": "the hush of a grand lobby, heels on marble, a distant elevator chime, a fountain trickling",
    "B3": "a soft monitor beep, quiet air conditioning, birds outside",
    "B4": "distant hospital footsteps, a soft announcement chime with no words, air conditioning",
    "B5": "a quiet big house, wind in the garden trees, a clock ticking",
    "B6": "fine rain on an umbrella, dripping iron, a distant car passing on wet road",
    "B7": "a quiet office hum, the city far below, a pen scratching",
    "B8": "the low hum of a moving elevator, muffled city wind",
    "B9": "birdsong outside, a heavy door, footsteps on stone",
    "B10": "birdsong, leaves rustling, slow breathing",
    "B11": "a quiet night house, a lamp switch, crickets outside",
    "B12": "charcoal sizzling, motorbikes passing slowly, water lapping, distant laughter",
    "B13": "birdsong from the garden, a clock ticking, pages turning",
    "B14": "bare feet on wood, slow breathing, faint city noise",
    "B15": "soft café murmur far away, cups on saucers, a milk steamer hissing",
    "B16": "heavy rain drumming on the car roof, wipers off, a distant passing car",
    "B17": "a quiet studio at night, faint city hum, paper rustling",
    "B18": "soft rain on a window, the rustle of a blanket, a faint ticking clock",
    "B19": "rain hammering glass, porridge bubbling, distant thunder",
    "B20": "a heavy silence, a ticking clock, paper sliding on stone",
    "B21": "a pan sizzling, birdsong, a spoon against a cup",
    "B22": "air conditioning hum, a projector fan, chairs creaking",
    "B23": "sharp heel clicks echoing down glass and stone",
    "B24": "crickets, a soft breeze in fairy lights, distant laughter, the pool lapping",
    "B25": "scissors through fabric, a sewing machine far off, street noise through tall windows",
}
SIZE = {
    "ECU": "100mm extreme close-up on {a}",
    "CU": "85mm close-up on {a}, eyes in sharp focus, background melting into bokeh",
    "MCU": "65mm medium close-up on {a}",
    "MS": "50mm medium shot of {a}",
    "OTS": "50mm over-the-shoulder shot from behind {b}'s soft-focus shoulder onto {a}",
    "2S": "35mm medium two-shot of {a} and {b}, both faces readable",
    "WS": "24mm wide shot of {place}",
    "INS": "100mm macro insert shot",
    "POV": "point-of-view shot",
    "LOW": "low-angle 35mm shot looking up at {a}",
    "TOP": "overhead top-down shot of {a}",
}
MOVE = {
    "push": "a slow, steady push-in", "pull": "a slow pull-back", "dolly": "a slow lateral dolly", "arc": "a slow arc around the subject",
    "track": "a smooth tracking move that follows the action", "crane": "a slow crane-down", "handheld": "a subtle restless handheld float",
    "static": "locked off on a tripod, perfectly still", "tilt": "a slow tilt down", "rack": "a deliberate rack focus as described",
    "whip": "ending in a fast whip-pan blur", "orbit": "a slow orbit",
}
CAM_VI = {"ECU": "Đặc tả", "CU": "Cận", "MCU": "Cận trung", "MS": "Trung", "OTS": "Qua vai", "2S": "Hai người", "WS": "Toàn",
          "INS": "Chèn chi tiết", "POV": "Góc nhìn", "LOW": "Góc thấp", "TOP": "Từ trên xuống"}
MOVE_VI = {"push": "đẩy vào chậm", "pull": "kéo ra chậm", "dolly": "lia ngang", "arc": "vòng cung", "track": "bám theo", "crane": "cẩu hạ",
           "handheld": "cầm tay", "static": "đứng yên", "tilt": "nghiêng xuống", "rack": "chuyển nét", "whip": "lia gắt", "orbit": "xoay quanh"}
RISKY = re.compile(r"\b(slap|punch|strik(e|es|ing)|kick|strangl|chok(e|es|ing)|grab|seiz|lunge|attack|fight|sword|weapon|gun|knife|blade|blood|gore|"
                   r"violent|blast|thrown|throat|kiss|in bed|undress|naked|nude|lingerie|bikini|cleavage|shirtless|crash|smash|hit(s|ting)?|shoot|"
                   r"explo\w*|fist|shov\w*|drag(?!on)|tied|bound|threaten\w*|hostage|push(es|ed|ing)?(?!-in))\b", re.I)


def syllables(text: str) -> int:
    return len([w for w in re.split(r"\s+", re.sub(r"[^\w'À-ỹ\s]", " ", text)) if w.strip("'")])


def speech_secs(name: str, pace: str, line: str) -> float:
    return syllables(line) / (RATE.get(name, 4.0) * PACE[pace][0])


def look_of(part, shot, name):
    return shot["look"].get(name) or part["looks"][name]


def subj(name):
    return f"{TAG[name]} ({ROLE[name]})"


def render(part, shot, d):
    loc = shot["loc"] or part["loc"]
    place_short, place = PLACE[loc]
    size, move = (shot["cam"].split() + ["static"])[:2]
    who = shot["who"]
    say = shot["say"]
    a = say[0] if say else (who[0] if who else None)
    b = next((w for w in who if w != a), None)
    cam = SIZE[size].format(a=subj(a) if a else "", b=subj(b) if b else "", place=place_short)
    lines = [f"A single continuous {d}-second shot, 16:9, one camera angle, no cuts.", "",
             "[LOOK] " + LOOK, "", "[PLACE] " + place[0].upper() + place[1:] + ".", ""]
    if who:
        lines.append("[CHARACTERS] Use the attached character image for each person: same face, same hair, same outfit, exactly.")
        for w in who:
            code = look_of(part, shot, w)
            lines.append(f"- {TAG[w]} = {NAME[w]}, {ROLE[w]} ({FACE[w].split(',')[0]}); wears {LOOKS[code][2]}. Attached image: \"{LOOKS[code][1]}\".")
        lines.append("Nobody else is in focus.")
    else:
        lines.append("[CHARACTERS] No named characters; any people in frame are distant, blurred and unidentifiable.")
    lines += ["", f"[CAMERA] {cam}; {MOVE[move]}.", "", f"[ACTION] {shot['act'].rstrip('.')}.", ""]
    if say:
        n, pace, tone, line = say
        end = round(0.3 + speech_secs(n, pace, line), 1)
        lines += [f"[DIALOGUE] In Vietnamese with exact lip-sync, spoken on camera by {TAG[n]} ({VOICE[n]}, {PACE[pace][1]}, {tone}), "
                  f"said exactly once from 0.3s to {end}s: \"{line}\"",
                  f"Only {TAG[n]} moves the lips" + (f"; {TAG[b]} listens with the mouth closed" if b else "")
                  + f". After the last word nobody speaks again until {d}.0s. Standard Northern Vietnamese accent; never read these directions aloud.", ""]
    else:
        lines += ["[DIALOGUE] None. Every mouth stays closed; no voices at all.", ""]
    lines += [f"[SOUND] {SFX[loc]}. No music.", "", "[AVOID] " + AVOID]
    return "\n".join(lines) + "\n"


def main() -> int:
    out = os.path.join(SDIR, "flow_v2")
    os.makedirs(out, exist_ok=True)
    errors, warns = [], []
    kb = ["# KỊCH BẢN BẢN 2 — " + "VỢ TÔI MẤT TRÍ NHỚ CÓ CHỌN LỌC", "",
          "Mỗi phần ~1 phút, ghép từ các shot 3–5 giây trên tính năng \"Cảnh\" của Flow. Mỗi shot: một góc máy, một chuyển động máy, tối đa một người nói. "
          "Ký hiệu nhân vật theo bộ đồ (L1, Q4…) xem `NHAN_VAT_FLOW.md`; cốt truyện, gài – trả xem `CAU_CHUYEN.md`.", ""]
    sl = ["# Danh sách shot bản 2", "", "| Mốc | Shot | Dài | Máy quay | Gắn nhân vật trên Flow | Thoại |", "|---|---|---|---|---|---|"]
    used = {}
    total = 0
    n_shots = 0
    for part in PARTS:
        pdir = os.path.join(out, f"p{part['num']:02d}")
        os.makedirs(pdir, exist_ok=True)
        for f in os.listdir(pdir):
            os.remove(os.path.join(pdir, f))
        ptotal = sum(s["d"] for s in part["shots"])
        kb += [f"## Phần {part['num']:02d} · {part['title']}", "",
               f"- **Móc 3 giây đầu:** {part['hook']}", f"- **Câu treo:** {part['cliff']}", f"- **Chuyển sang phần sau:** {part['tr']}", "",
               "| # | Dài | Bối cảnh | Máy quay | Ai trong khung | Hành động | Thoại |", "|---|---|---|---|---|---|---|"]
        for k, s in enumerate(part["shots"], 1):
            sid = f"{part['num']:02d}-{k:02d}"
            who, say = s["who"], s["say"]
            if len(who) > 2:
                errors.append(f"{sid}: {len(who)} người trong khung (tối đa 2)")
            if say and say[0] not in who:
                errors.append(f"{sid}: người nói {say[0]} không có trong khung")
            for w in who:
                if w not in part["looks"] and w not in s["look"]:
                    errors.append(f"{sid}: chưa khai báo bộ đồ cho {w}")
            size, move = (s["cam"].split() + ["static"])[:2]
            if size not in SIZE or move not in MOVE:
                errors.append(f"{sid}: máy quay lạ '{s['cam']}'")
            d = s["d"]
            if say:
                need = math.ceil(0.3 + speech_secs(say[0], say[1], say[3]) + 0.4)
                if need > d:
                    warns.append(f"{sid}: câu cần {need}s, tăng từ {d}s")
                    d = need
                if '"' in say[3]:
                    errors.append(f"{sid}: dấu ngoặc kép trong câu thoại")
            if d > 5:
                warns.append(f"{sid}: {d}s (> 5s)")
            m = RISKY.search(s["act"])
            if m:
                warns.append(f"{sid}: từ rủi ro '{m.group(0)}'")
            txt = render(part, s, d)
            with open(os.path.join(pdir, f"{sid}.txt"), "w", encoding="utf-8") as f:
                f.write(txt)
            codes = [look_of(part, s, w) for w in who]
            for c in codes:
                used.setdefault(c, []).append(part["num"])
            loc = s["loc"] or part["loc"]
            cam_vi = f"{CAM_VI[size]}, {MOVE_VI[move]}"
            whos = ", ".join(f"{NAME[w]} ({c})" for w, c in zip(who, codes)) or "—"
            line = f"**{NAME[say[0]]}:** {say[3]}" if say else "*(im lặng)*"
            kb.append(f"| {k} | {d}s | {loc} | {cam_vi} | {whos} | {s['act'].rstrip('.')} | {line} |")
            mm, ss = divmod(total, 60)
            sl.append(f"| {mm:02d}:{ss:02d} | `{sid}` | {d}s | {cam_vi} | {', '.join(LOOKS[c][1] for c in codes) or '— (chỉ text)'} | "
                      + (f"{NAME[say[0]]}: {say[3]}" if say else "—") + " |")
            total += d
            n_shots += 1
        kb += ["", f"*Tổng phần {part['num']:02d}: {len(part['shots'])} shot, ~{ptotal}s.*", ""]
    kb.insert(3, f"**Tổng:** {len(PARTS)} phần, {n_shots} shot, {total // 60} phút {total % 60} giây.\n")
    with open(os.path.join(SDIR, "KICH_BAN_V2.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(kb) + "\n")
    with open(os.path.join(SDIR, "SHOT_LIST_V2.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(sl[:2]) + f"\n{n_shots} shot, {total // 60} phút {total % 60} giây. Tạo trên Flow: Video · Thành phần · 16:9 · Omni 1.2 Flash · độ dài theo cột *Dài*; "
                "gắn đúng nhân vật theo bộ đồ ở cột *Gắn*. Shot không có nhân vật thì tạo chỉ bằng text.\n\n" + "\n".join(sl[2:]) + "\n")
    nv = ["# Nhân vật theo bộ đồ cần tạo trên Flow", "",
          "Mỗi bộ đồ là một nhân vật riêng trên Flow, đặt đúng tên ở cột *Tên trên Flow*. Cách tạo giữ nguyên khuôn mặt: mở nhân vật gốc (Linh, Quân…), "
          "dùng ô \"Bạn muốn thay đổi điều gì?\" với câu *same person, same face and hair, now wearing …*; hoặc tạo mới bằng prompt ở cột cuối "
          "và gắn ảnh nhân vật gốc làm tham chiếu.", "",
          "| Mã | Tên trên Flow | Dùng ở phần | Prompt ảnh mẫu |", "|---|---|---|---|"]
    for code, (who, flow_name, outfit) in LOOKS.items():
        parts_used = sorted(set(used.get(code, [])))
        if not parts_used:
            warns.append(f"bộ đồ {code} không dùng ở phần nào")
        prompt = (f"Full-body photorealistic character reference of {FACE[who]}, wearing {outfit}; plain light-grey studio background, "
                  "soft flattering beauty light, natural skin texture, 8K. Not resembling any real person.")
        nv.append(f"| {code} | {flow_name} | {', '.join(f'P{p}' for p in parts_used) or '—'} | {prompt} |")
    with open(os.path.join(SDIR, "NHAN_VAT_FLOW.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(nv) + "\n")
    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"{len(PARTS)} phần, {n_shots} shot, {total // 60}:{total % 60:02d} → {out}; {len(errors)} lỗi, {len(warns)} cảnh báo")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
