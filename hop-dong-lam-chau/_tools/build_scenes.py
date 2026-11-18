#!/usr/bin/env python3
"""Sinh prompt Flow cho phim đầy đủ: mỗi cảnh 4 clip × 15 giây, một cú máy liền, Omni 1.2 Flash.
Chạy: python3 hop-dong-lam-chau/_tools/build_scenes.py  →  film/canh-XX/clip-N.txt + film/canh-XX/README.md
Dữ liệu cảnh nằm trong SCENES bên dưới (theo CAU_CHUYEN_v2.md)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_flow_files as B

LOOK, PEOPLE = B.LOOK, B.PEOPLE
B.PLACES["SAN_BAO"] = (B.PLACES["SAN"][:-1] + "; under the eaves a worn carpenter's workbench with a hand plane, "
                       "curls of fresh wood shavings and a half-finished small wooden chair frame.")
B.SOUND["SAN_BAO"] = B.SOUND["SAN"] + ", the soft rasp of a hand plane on wood"

AVOID15 = B.AVOID.replace("any cut or second camera angle", "any cut, jump or change to a second camera angle; the same person appearing twice, twins, clones or look-alike doubles of a named character")

# Mỗi clip: (tên, bối cảnh, [bộ đồ], máy quay, hành động theo mốc giây, [(bộ đồ, câu, t0, t1)], ghi chú âm thanh thêm)
SCENES = {
    "03": dict(title="Thi kiến thức cháu đích tôn", clips=[
        ("Bà Thoa lên live", "SAN", ["BT1", "DA1"],
         "One continuous 15-second take: 35mm medium-wide two-shot, locked off with a very slow push-in; BaThoa at the low brick wall on the left of frame and Dat standing alone in the courtyard on the right of frame are both visible from the first frame to the last",
         "0–5s: BaThoa pops up over the low brick wall from the neighbour's garden, holding her phone high on a selfie stick and talking brightly into it like a TV host. "
         "5–9s: on the right, Dat spots the phone, straightens his collar and waves at it with a stiff, over-eager grin. "
         "9–15s: BaThoa beckons with her free hand and squeezes through a gap in the wall into the courtyard, phone still raised; Dat's grin wobbles",
         [("BT1", "Các cháu đang xem live ơi, cháu đích tôn nhà ông Thịnh về rồi này!", 0.4, 4.6),
          ("DA1", "Dạ… cháu chào cả nhà ạ!", 6.0, 8.0),
          ("BT1", "Đứng đấy! Sang đây bà hỏi tí!", 9.6, 11.8)], ""),
        ("Mẹ mày tên gì", "SAN", ["BT1", "DA1", "BM2"],
         "One continuous 15-second take: 50mm medium two-shot of BaThoa and Dat face to face in the courtyard, BaMan visible in soft focus behind them in the doorway holding a tea tray, very slow push-in",
         "0–2s: BaThoa thrusts the phone toward Dat's face. "
         "2–6s: Dat blinks, thinking hard, then answers with a hopeful smile. "
         "6–9s: BaThoa narrows her eyes and fires the next question. "
         "9–11s: in the background BaMan chokes and coughs loudly into her hand, the tea cups rattling on the tray. "
         "11–15s: Dat stands frozen, a bead of sweat on his temple, smile stuck in place; BaThoa waits, delighted",
         [("BT1", "Mẹ mày tên gì?", 0.5, 1.8),
          ("DA1", "Dạ… mẹ cháu tên là… Mẹ ạ!", 2.6, 5.4),
          ("BT1", "Thế năm lớp mấy mày đái dầm ở nhà bà?", 6.4, 9.0)],
         "BaMan's cough at 9.3s–10.5s is a non-verbal sound, no words"),
        ("Cây bưởi", "SAN_BAO", ["BT1", "DA1", "OT1"],
         "One continuous 15-second take: 35mm medium-wide shot with OngThinh at his workbench in the foreground left, Dat and BaThoa standing behind in the courtyard, slow rack focus from them to OngThinh and back",
         "0–3s: BaThoa leans toward Dat with a sly grin and asks. "
         "3–7s: Dat opens his mouth, nothing comes out; his eyes dart around the courtyard in panic. "
         "7–10s: in the foreground OngThinh keeps pushing his hand plane along a plank, never looking up, and answers flatly. "
         "10–15s: BaThoa straightens up, a little disappointed; Dat lets out a huge silent breath and nods too many times",
         [("BT1", "Thế hồi bé mày ngã cây gì?", 0.5, 2.6),
          ("OT1", "Cây bưởi. Nó ngã cây bưởi.", 7.2, 9.8)], ""),
        ("Dị ứng lạc", "SAN", ["BM2", "DA1", "BT1"],
         "One continuous 15-second take: starts as an 85mm close-up on BaMan in the doorway, then slowly pulls back and pans to a 50mm two-shot of Dat and BaThoa by a low table with a plate of peanut brittle",
         "0–4s: BaMan, holding the tea tray, whispers to herself in quiet surprise, eyes soft. "
         "4–8s: the camera drifts to Dat, who relaxes, grabs a piece of peanut brittle from the plate and chews happily. "
         "8–12s: BaThoa slowly turns from her phone, eyes narrowing at the peanut brittle in his hand, and speaks with relish. "
         "12–15s: Dat freezes mid-chew, cheeks full, eyes wide",
         [("BM2", "Ông vẫn nhớ cái đấy cơ à…", 0.6, 3.2),
          ("BT1", "Lạ nhỉ. Thằng Minh hồi bé dị ứng lạc cơ mà?", 8.4, 11.8)], ""),
    ]),
}


def clip_prompt(c):
    name, place, looks, cam, action, lines, extra = c
    out = ["A single continuous 15-second shot, 16:9, one camera take with no cuts.", "",
           f"[LOOK] {B.LOOKBLOCK}", "", f"[PLACE] {B.PLACES[place]}", "",
           "[CHARACTERS] Use the attached character image for each person: same face, same hair, same outfit, exactly."]
    for code in looks:
        lk = LOOK[code]; p = PEOPLE[lk["person"]]
        out.append(f"- @{lk['person']} = {p['vn']}, {p['role']} ({p['face'].split(',')[0]}); wears {lk['outfit']}. Attached image: \"{lk['flow']}\".")
    out += ["Each named person appears exactly once in the frame for the whole take, as one single continuous person; no duplicates, twins or look-alikes. "
            "Background villagers, if any, stay distant, blurred and clearly different from the named characters.", "", f"[CAMERA] {cam}.", "", f"[ACTION] {action}.", ""]
    if lines:
        out.append("[DIALOGUE] In Vietnamese with exact lip-sync, standard Northern Vietnamese accent. Each line is spoken exactly once, on camera, at its time; only the speaker moves the lips:")
        for code, text, t0, t1 in lines:
            person = LOOK[code]["person"]
            out.append(f"- {t0:.1f}s–{t1:.1f}s, @{person} ({PEOPLE[person]['voice']}): {text}")
        out.append("No other words are spoken. Never read these directions aloud.")
    else:
        out.append("[DIALOGUE] None. Every mouth stays closed; no voices at all.")
    snd = B.SOUND[place] + (f"; {extra}" if extra else "")
    out += ["", f"[SOUND] {snd}. No music.", "", f"[AVOID] {AVOID15}", ""]
    return "\n".join(out)


def main():
    only = sys.argv[1:] or list(SCENES)
    for sc in only:
        s = SCENES[sc]
        md = [f"# Cảnh {sc} · {s['title']}", "", "*Sinh bởi `_tools/build_scenes.py`.* Mỗi clip 15 giây, một cú máy liền, "
              "Flow: **Video → Thành phần**, Omni 1.2 Flash, 720p, 16:9, x1. Tên trên Flow: `C" + sc + "-N · <tên>`.", "",
              "| Clip | Tên trên Flow | Đính | Thoại |", "|---|---|---|---|"]
        for i, c in enumerate(s["clips"], 1):
            B.write(f"film/canh-{sc}/clip-{i}.txt", clip_prompt(c))
            md.append(f"| {i} | C{sc}-{i} · {c[0]} | {', '.join(LOOK[x]['flow'] for x in c[2])} | "
                      + " / ".join(f"{PEOPLE[LOOK[l[0]]['person']]['vn']}: {l[1]}" for l in c[5]) + " |")
        B.write(f"film/canh-{sc}/README.md", "\n".join(md) + "\n")
        print(f"canh-{sc}: {len(s['clips'])} clip")


if __name__ == "__main__":
    main()
