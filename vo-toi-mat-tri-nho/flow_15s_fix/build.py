#!/usr/bin/env python3
"""Sinh lại câu lệnh đã sửa cho các clip cần render lại + 7 cảnh mới (18/11/2026).
Chạy: python3 flow_15s_fix/build.py  → flow_15s_fix/<id>.txt + queue.json  ([id, [tên ảnh nhân vật], prompt])"""
import os, re, glob, json
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(os.path.dirname(HERE), "flow_15s")
REDO = ("04-2 04-3 05-1 05-2 05-3 05-4 06-1 06-2 07-1 07-4 08-1 09-4 10-1 10-2 11-2 12-1 12-2 12-3 13-1 14-1 14-2 14-3 "
        "15-1 15-2 15-3 16-3 17-2 17-3 17-4 19-2 19-3 20-1 20-2 21-1 22-1 22-3 23-1 23-2 23-3 23-4 24-1 24-2 24-3 25-3 25-5").split()
AVOID_ADD = ("Visible film cameras, tripods, light stands, boom microphones, film crew or any filmmaking equipment anywhere in the frame, "
             "camera viewfinder or recording overlays, phone camera interfaces, the same character appearing twice in one shot, ")
def src(i): return open(os.path.join(SRC, "p" + i[:2], i + ".txt")).read()
def generic(t):
    t = t.replace("shot on ARRI Alexa 35 with anamorphic lenses", "with the look of an ARRI Alexa 35 anamorphic feature film")
    t = t.replace("locked off on a tripod, perfectly still", "a completely static frame")
    t = t.replace("spoken on camera by", "spoken in frame by")
    t = t.replace("recorded close on set with a little room tone", "close, natural dialogue sound with a little room tone")
    t = t.replace("[AVOID]\n", "[AVOID]\n" + AVOID_ADD) if AVOID_ADD not in t else t
    return t
# ---- khối dùng chung lấy từ file gốc
ALL = {os.path.basename(f)[:-4]: open(f).read() for f in glob.glob(os.path.join(SRC, "p*", "*.txt"))}
CH = {}; VOICE = {}
for t in ALL.values():
    for m in re.finditer(r'^- (@\w+ = .*?Attached image: "([^"]+)"\.)$', t, re.M): CH.setdefault(m.group(2), m.group(1))
    for m in re.finditer(r'spoken on camera by (@\w+) \((.*?), speaking ', t): VOICE.setdefault(m.group(1), m.group(2))
T0 = generic(ALL["06-3"])
STYLE = re.search(r"\[STYLE\]\n(.*?)\n", T0).group(1)
CHHEAD = re.search(r"\[CHARACTERS\]\n(.*?)\n", T0).group(1)
SLTAIL = "- Whoever is speaking has the face clearly on screen in that shot; the camera keeps one side of the line so eyelines match across the cuts."
TLHEAD = re.search(r"\[TIMELINE[^\n]*\n(.*?)\n", T0).group(1)
THR = [l for l in T0.split("\n") if l.startswith("- Throughout")][0]
VOI = [l for l in T0.split("\n") if l.startswith("- Voices")][0]
SPK = [l for l in T0.split("\n") if l.startswith("- Speak only")][0]
AVOID = T0.split("[AVOID]\n")[1].strip()
PACE = {"slow": "speaking slowly and softly with small natural pauses", "mid": "speaking at a natural conversational pace",
        "fast": "speaking quickly in short lively phrases, every word clear"}
def make(cuts, loc, chars, shots, beats, turns, sfx, extra_avoid=""):
    n = len(shots); cs = ", ".join(f"{c:g}s" for c in cuts)
    out = [f"A 15-second live-action film sequence of {n} shots, 16:9 widescreen, 24 fps, with hard cuts only at {cs}; one place and one moment, sound and action continuous across the cuts.",
           "", "[STYLE]", STYLE, "", "[LOCATION]", loc, "", "[CHARACTERS]", CHHEAD] + ["- " + CH[c] for c in chars] + ["Nobody else appears in focus.", "",
           "[SHOT LIST — hard cuts only at the marked seconds]"]
    b = [0] + list(cuts) + [15]
    for k, s in enumerate(shots): out.append(f"- Shot {k+1}, {b[k]:g}–{b[k+1]:g}s: {s}.")
    out += [SLTAIL, "", "[TIMELINE — second by second]", TLHEAD]
    for k, s in enumerate(beats):
        head = f"- {b[k]:g}–{b[k+1]:g}s (Shot 1)" if k == 0 else f"- {b[k]:g}–{b[k+1]:g}s (CUT to Shot {k+1})"
        out.append(f"{head}: {s}" + (" The sequence settles on this as its final frame." if k == n - 1 else ""))
    out += ["", "[AUDIO]"]
    if turns:
        out.append(f"- Dialogue in Vietnamese with exact lip-sync, {len(turns)} spoken turn{'s' if len(turns)>1 else ''} in this order, each said exactly once (no subtitles):")
        for k, (a, z, who, pace, mood, line) in enumerate(turns):
            out.append(f'- Turn {k+1}, {a:g}–{z:g}s, spoken in frame by {who} ({VOICE[who]}, {PACE[pace]}, {mood}): "{line}"')
        out += [THR, VOI, f"- All speech is over by {turns[-1][1]:g}s; outside the turns above nobody says a word, and no line is ever repeated to fill the time.", SPK]
    else:
        out.append("- No dialogue at all: nobody speaks, mouths stay closed; only the sound effects below.")
    out += [f"- SFX: {sfx}", "", "[AVOID]", extra_avoid + AVOID]
    return "\n".join(out)
SPEAK = lambda w: f"{w} speaks, face clearly on screen."
Q = {}
# ---------- clip làm lại: sửa chung + sửa riêng
for i in REDO:
    t = generic(src(i))
    if i == "05-1":
        t = t.replace("Bong runs across the living room straight into Linh's open arms", "Bong runs across the living room and stops in front of Linh, beaming up at her")
        t = t.replace("Linh kneels and holds her daughter close, touching her nose", "Linh crouches to her daughter's eye level and gently tucks a strand of hair behind her ear")
        t = t.replace("ngủ phải ôm thỏ", "mê truyện cổ tích")
        t = t.replace("Shot 4, 12–15s: 85mm close-up on the little girl, eyes in sharp focus, background melting into bokeh,", "Shot 4, 12–15s: 50mm medium shot of the little girl beside her mother,")
    if i == "13-1":
        t = t.replace("two women's silhouettes in the back seat", "exactly two women in the back seat, one on each side")
        t = t.replace("Nobody else appears in focus.", "Exactly two people are inside the car: Linh on the left, Mai Anh on the right. Nobody else appears in focus.")
    if i in ("17-2", "17-3", "17-4"):
        t = t.replace("The entrance hall of a modern villa: tall wooden double door, stone floor, a console with white orchids, a staircase; morning sun through the door.",
                      "The entrance hall of a modern villa late at night in a heavy rainstorm: tall wooden double door, wet stone floor by the door, a console with white orchids, a dark staircase; dim warm wall sconces, rain lashing the tall window beside the door, black night outside.")
        t = t.replace("SFX: birdsong outside, a heavy door, footsteps on stone.", "SFX: heavy rain outside, a low roll of distant thunder, a heavy door, footsteps on stone.")
    if i == "19-3":
        t = t.replace("Match: a woman's hands button a tailored white suit jacket before a mirror;", "Match: clearly visible, a woman's hands fasten the button of a tailored white suit jacket before a mirror, the button closing in frame;")
    if i == "25-5":
        t = t.replace("Shot 1, 0–5.5s: 85mm close-up on the little girl, eyes in sharp focus, background melting into bokeh, a slow, steady push-in",
                      "Shot 1, 0–5.5s: 35mm medium two-shot of the little girl and her mother at the table, both faces readable, a completely static frame")
        t = t.replace("Bong points her cake fork at him;", "Beside her smiling mother, Bong points her cake fork across the table at Tuan;")
    if i == "10-1":
        for a, b in [("hard cuts only at 4s, 9.5s", "hard cuts only at 4s, 8.5s"), ("Shot 2, 4–9.5s", "Shot 2, 4–8.5s"), ("Shot 3, 9.5–15s", "Shot 3, 8.5–15s"),
                     ("- 4–9.5s (CUT to Shot 2)", "- 4–8.5s (CUT to Shot 2)"), ("- 9.5–15s (CUT to Shot 3)", "- 8.5–15s (CUT to Shot 3)")]: t = t.replace(a, b)
        t = re.sub(r"Turn 2, [\d.]+–[\d.]+s", "Turn 2, 8.8–12.6s", t); t = re.sub(r"All speech is over by [\d.]+s", "All speech is over by 12.6s", t)
    if i == "12-2":
        t = re.sub(r'(Turn 1, [^"]*)"[^"]*"', r'\1"Em nợ anh Hưng một khoản rất lớn."', t)
        t = re.sub(r'(Turn 2, [^"]*)"[^"]*"', r'\1"Anh ta bảo làm xong việc này thì xoá nợ cho em."', t)
    Q[i] = (re.findall(r'Attached image: "([^"]+)"', t), t)
# ---------- 7 cảnh mới
CAR = "The back seat of a black luxury car parked on a dark street at night, heavy rain streaming down the windows, street lights sliding across black leather; moody blue with passing amber light."
Q["06-5"] = (["Hưng · Vest đen", "Mai Anh · Thường ngày"], make([4, 7, 10.5], CAR, ["Hưng · Vest đen", "Mai Anh · Thường ngày"],
   ["35mm medium two-shot of the vice president and the young woman side by side in the back seat, both faces readable, a completely static frame",
    "100mm macro insert shot, a completely static frame", "85mm close-up on the young woman, eyes in sharp focus, background melting into bokeh, a completely static frame",
    "85mm close-up on the vice president, eyes in sharp focus, background melting into bokeh, a slow, steady push-in"],
   ["Hung slides a small white name card across the leather seat toward Mai Anh; " + SPEAK("@Hung"),
    "The plain white card on the black leather, rain shadows rippling over it; no readable text. No one speaks.",
    "Mai Anh holds the card, uneasy; " + SPEAK("@MaiAnh"), "Hung smiles thinly, eyes cold; " + SPEAK("@Hung")],
   [(0.3, 3.6, "@Hung", "slow", "silky", "Mai Anh. Từ mai em là huấn luyện viên phục hồi của vợ hắn."),
    (7.3, 9.6, "@MaiAnh", "mid", "uneasy", "Lỡ chị ấy nhận ra em thì sao?"),
    (10.8, 14.6, "@Hung", "slow", "amused, then cold", "Người mất trí thì nhận ra ai? Lần này, phải có ảnh.")],
   "heavy rain drumming on the car roof, a distant car passing on a wet road. No music."))
OFFICE = "A glass-walled CEO office high above the city by day: a long walnut desk, a tall standing mirror by the bookshelf, the skyline through floor-to-ceiling windows; clean cool daylight."
Q["08-5"] = (["Tuấn · Vest be", "Quân · Vest navy"], make([4.5, 9, 12.5], OFFICE, ["Tuấn · Vest be", "Quân · Vest navy"],
   ["35mm medium two-shot of the assistant and the husband in front of the tall mirror, both faces readable, a completely static frame",
    "50mm medium shot of the husband facing the mirror, his reflection visible, a completely static frame",
    "85mm close-up on the assistant, eyes in sharp focus, background melting into bokeh, a completely static frame",
    "85mm close-up on the husband, eyes in sharp focus, background melting into bokeh, a completely static frame"],
   ["Tuan stands beside Quan at the mirror, coaching him with both hands like a director; " + SPEAK("@Tuan"),
    "Quan tries a stiff smile at his reflection, then a wider one; " + SPEAK("@Quan"),
    "Tuan winces and covers his eyes; " + SPEAK("@Tuan"), "Quan drops the smile and sighs, defeated. No one speaks."],
   [(0.3, 3.9, "@Tuan", "fast", "coaching", "Anh cười tự nhiên lên! Đừng như đi họp cổ đông!"),
    (4.8, 8.2, "@Quan", "mid", "trying hard", "Thế này… được chưa? Hay thế này?"),
    (9.3, 12, "@Tuan", "fast", "horrified, comic", "Trời ơi, nhìn như đòi nợ ấy anh ạ!")],
   "a quiet office hum, the city far below. No music."))
LIV = re.search(r"\[LOCATION\]\n(.*?)\n", src("05-1")).group(1).replace("in the evening", "late at night").replace("warm amber lamplight", "a single warm floor lamp, the rest in soft shadow")
Q["10-5"] = (["Linh · Lụa ngà", "Quân · Vest navy"], make([5, 8.5, 12], LIV, ["Linh · Lụa ngà", "Quân · Vest navy"],
   ["50mm medium shot of the wife on the sofa, a completely static frame", "85mm close-up on the husband, eyes in sharp focus, background melting into bokeh, a slow, steady push-in",
    "85mm close-up on the wife, eyes in sharp focus, background melting into bokeh, a completely static frame", "50mm medium shot of the wife, a completely static frame"],
   ["Linh, alone on the cream sofa, softly hums a gentle wordless tune to herself, eyes half closed, smiling. No one speaks.",
    "Quan has stopped in the doorway, frozen, moved; " + SPEAK("@Quan"), "Linh snaps her eyes open and sits up straight; " + SPEAK("@Linh"),
    "Linh stands and walks briskly out of frame, not looking back. No one speaks."],
   [(5.3, 8.2, "@Quan", "slow", "stunned, tender", "Bài hát đám cưới mình… sao em còn nhớ?"),
    (8.8, 11.6, "@Linh", "fast", "caught out, brisk", "Nghe trên mạng thôi! Tôi đi ngủ đây.")],
   "soft wordless humming at the start, a clock ticking, wind in the garden trees. No music besides the humming."))
Q["15-4"] = (["Quân · Đồ ngủ"], make([4, 8.5, 12], LIV.replace("a single warm floor lamp", "a single warm table lamp"), ["Quân · Đồ ngủ"],
   ["24mm wide shot of the dark living room, a completely static frame", "100mm macro insert shot, a completely static frame",
    "85mm close-up on the husband, eyes in sharp focus, background melting into bokeh, a slow, steady push-in", "100mm macro insert shot, a completely static frame"],
   ["Past midnight, Quan sits alone on the cream sofa in a rumpled T-shirt, a thick white wedding album open on his knees. No one speaks.",
    "His hand turns a page: wedding photos of a young couple laughing under white flowers, no writing. No one speaks.",
    "Quan's eyes fill; " + SPEAK("@Quan"), "His thumb rests on a photo of the bride's smile. No one speaks."],
   [(8.8, 11.8, "@Quan", "slow", "broken whisper", "Mười năm… anh đánh rơi em ở chỗ nào thế?")],
   "a clock ticking, a page turning, quiet night. No music."))
STUDY = "A dark home study in a villa at night: a walnut desk, bookshelves, a laptop glowing, a brass desk lamp, rain-dark window; cool laptop light on the face, warm lamp behind."
Q["19-4"] = (["Linh · Lụa ngà"], make([4, 8.5, 12], STUDY, ["Linh · Lụa ngà"],
   ["24mm wide shot of the dark study, a completely static frame", "85mm close-up on the wife, eyes in sharp focus, background melting into bokeh, a slow, steady push-in",
    "100mm macro insert shot, a completely static frame", "85mm close-up on the wife, eyes in sharp focus, background melting into bokeh, a completely static frame"],
   ["Linh sits alone at the desk, phone to her ear, the laptop glow on her face; no one else in the room. No one speaks.",
    "Linh, calm and commanding, no trace of confusion; " + SPEAK("@Linh"),
    "Her hand closes the laptop; a cherry-blossom hairpin lies beside it. No one speaks.",
    "Linh lowers the phone and looks straight ahead, a small sure smile; " + SPEAK("@Linh")],
   [(4.3, 8.2, "@Linh", "slow", "quiet authority", "Mười giờ sáng mai. Chuẩn bị đủ hồ sơ."), (12.3, 13.8, "@Linh", "slow", "decided", "Tôi sẽ tự đến.")],
   "rain on the window, a soft laptop click. No music."))
ELEV = re.search(r"\[LOCATION\]\n(.*?)\n", src("06-4")).group(1)
Q["21-5"] = (["Hưng · Vest đen"], make([4, 8.5, 12], ELEV, ["Hưng · Vest đen"],
   ["24mm wide shot of the glass elevator, a completely static frame", "85mm close-up on the vice president, eyes in sharp focus, background melting into bokeh, a completely static frame",
    "100mm macro insert shot, a completely static frame", "50mm medium shot of the vice president, a slow pull-back"],
   ["Night: the glass elevator slides down the outside of the tower, Hung alone inside. No one speaks.",
    "Hung pulls his tie loose with a shaking hand, the polite mask gone, jaw tight. No one speaks.",
    "His phone buzzes again and again in his palm, screen lit with no readable writing; his thumb hovers and does not answer. No one speaks.",
    "Hung sags back against the glass as the city lights slide upward past him. No one speaks."],
   [], "the low hum of a moving elevator, a phone buzzing repeatedly. No music."))
STALL = "A busy sidewalk food stall beside a lake at night: low plastic stools, a small steel table, grilled pork smoking on a charcoal brazier, warm yellow bulbs strung overhead; warm, lively light."
Q["23-5"] = (["Khang · Tiệc", "Mai Anh · Thường ngày"], make([5, 9, 12.5], STALL, ["Khang · Tiệc", "Mai Anh · Thường ngày"],
   ["35mm medium two-shot of the doctor and the young woman on low stools at the table, both faces readable, a completely static frame",
    "85mm close-up on the doctor, eyes in sharp focus, background melting into bokeh, a completely static frame",
    "85mm close-up on the young woman, eyes in sharp focus, background melting into bokeh, a completely static frame",
    "35mm medium two-shot of the doctor and the young woman, both faces readable, a completely static frame"],
   ["Khang and Mai Anh sit on low plastic stools over two steaming bowls; Mai Anh grins at him; " + SPEAK("@MaiAnh"),
    "Khang, deadpan, picks up a piece of grilled pork with chopsticks; " + SPEAK("@Khang"),
    "Mai Anh bursts out laughing; " + SPEAK("@MaiAnh"), "Both laugh together over the bowls. No one speaks."],
   [(0.3, 2, "@MaiAnh", "mid", "teasing", "Cả năm thật à anh?"), (5.3, 6.8, "@Khang", "slow", "deadpan", "Tôi nói là làm."),
    (9.3, 11.4, "@MaiAnh", "fast", "playful", "Thế mai mình ăn phở nhé!")],
   "sizzling charcoal, chatter of the street, a motorbike passing. No music."))
os.makedirs(HERE, exist_ok=True); order = REDO + ["06-5", "08-5", "10-5", "15-4", "19-4", "21-5", "23-5"]
for i in order:
    open(os.path.join(HERE, i + ".txt"), "w").write(Q[i][1])
json.dump([[i, Q[i][0], Q[i][1]] for i in order], open(os.path.join(HERE, "queue.json"), "w"), ensure_ascii=False)
bad = [i for i in order if re.search(r"tripod|on camera|on set|ARRI Alexa 35 with", Q[i][1].split("[AVOID]")[0])]
print(len(order), "câu lệnh; còn từ dễ gây lỗi:", bad or "không")
