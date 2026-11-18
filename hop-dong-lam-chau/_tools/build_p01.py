#!/usr/bin/env python3
"""Sinh prompt Flow cho 2 phút đầu phim (bản 2): câu mở đầu + cảnh 01 + cảnh 02.
Chạy: python3 hop-dong-lam-chau/_tools/build_p01.py  →  film/p01/*.txt và film/PHAN_01.md
Dùng chung nhân vật, bộ đồ, bối cảnh và khuôn prompt của build_flow_files.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_flow_files as B

B.SOUND["BENXE_PHANH"] = "a coach's air brakes hissing loudly, then a door folding open"
B.PLACES["BENXE_PHANH"] = B.PLACES["BENXE"]

# (mã, tên trên Flow, giây, bối cảnh, [bộ đồ], máy quay, hành động, thoại (bộ đồ, câu, t0, t1) | None)
SHOTS = [
    # ---- Câu mở đầu (flash-forward, sáng 29 Tết)
    ("00-01", "Hai thằng Minh ở cổng", 4, "CONG", ["MI2", "DA3"],
     "35mm wide shot through the gate, slow push-in",
     "Dat stands on a short bamboo ladder hanging a red lantern; the gate creaks open and Minh stands in it with a backpack; Dat freezes with the lantern in mid-air; they stare at each other", None),
    ("00-02", "Đứa nào cháu thật", 3, "SAN", ["BT1"],
     "50mm medium close-up, quick push-in",
     "BaThoa pops up over the low brick wall, phone raised high on the selfie stick, mouth dropping open",
     ("BT1", "Thế đứa nào là cháu thật?", 0.3, 2.3)),
    ("00-03", "Minh vào ăn sáng", 4, "HIEN", ["OT2"],
     "50mm medium shot, locked off",
     "OngThinh steps out onto the veranda leaning on his walking stick, looks from one young man to the other off-screen, then turns warmly toward camera-left",
     ("OT2", "Minh, vào ăn sáng con.", 1.4, 3.4)),
    ("00-04", "Minh chết lặng", 3, "CONG", ["MI2"],
     "85mm close-up, locked off",
     "Minh stands frozen in the gateway, stunned and silent, his breath misting in the cold air", None),
    ("00-05", "Xe khách phanh", 3, "BENXE_PHANH", [],
     "low shot at wheel level, locked off",
     "An old coach rolls in and stops hard in front of camera, dust swirling around its front wheel; the folding door opens", None),
    # ---- Cảnh 01 · Đơn hàng cháu đích tôn (bến xe huyện, 26 Tết)
    ("01-01", "Đạt xuống xe", 4, "BENXE", ["DA1"],
     "35mm medium-wide shot, slow pan following him",
     "Dat hops down from the coach step in his try-hard outfit, straightens his collar, and looks around the crowd with an eager showman's grin", None),
    ("01-02", "Bà dúi phong bì", 6, "BENXE", ["BM1", "DA1"],
     "50mm medium two-shot behind a concrete pillar, slow push-in",
     "BaMan glances around nervously, then presses a thick red envelope into Dat's hands and folds his fingers over it; Dat blinks, surprised",
     ("BM1", "Năm ngày thôi. Cháu làm cháu nội tôi, đừng để ông biết.", 0.4, 4.6)),
    ("01-03", "Đọc hợp đồng như văn khấn", 7, "BENXE", ["BM1"],
     "50mm medium close-up, locked off",
     "BaMan holds a folded sheet of paper close to her face (its writing never readable) and recites from it in a solemn sing-song like a temple prayer, eyes half closed",
     ("BM1", "Một, không để ông biết. Hai, không lên gác mở cái tủ gỗ. Ba, phải đi trước giao thừa.", 0.4, 6.2)),
    ("01-04", "Điều năm", 5, "BENXE", ["BM1"],
     "50mm medium close-up, locked off",
     "BaMan lowers the paper and looks up over it, suddenly very matter-of-fact",
     ("BM1", "Điều năm là của công ty cậu: lộ thì đền gấp đôi.", 0.4, 3.8)),
    ("01-05", "Đạt nuốt khan", 3, "BENXE", ["DA1"],
     "85mm close-up, locked off",
     "Dat's grin freezes; he swallows hard, then nods too quickly", None),
    ("01-06", "Ông hay lẫn", 7, "BENXE", ["BM1"],
     "85mm close-up, very slow push-in",
     "BaMan speaks quietly, her eyes wet and worried, twisting the strap of her cloth bag",
     ("BM1", "Từ hôm tai biến ông hay lẫn. Nhưng chuyện thằng Minh thì ông nhớ từng tí.", 0.5, 5.8)),
    ("01-07", "Nó hiền ít nói", 3, "BENXE", ["BM1"],
     "50mm medium close-up, locked off",
     "BaMan gives a small proud smile",
     ("BM1", "Nó hiền, ít nói.", 0.4, 1.9)),
    ("01-08", "Ít nói thì diễn được", 3, "BENXE", ["DA1"],
     "50mm medium close-up, locked off",
     "Dat flashes a confident thumbs-up and a wink",
     ("DA1", "Ít nói thì cháu diễn được.", 0.3, 2.1)),
    ("01-09", "Gọi về mái ấm", 7, "BENXE", ["DA1"],
     "50mm medium shot by the side of the coach, slight handheld",
     "Alone by the coach, Dat holds an old phone to his ear (screen never visible), speaking softly with a tender smile, glancing back toward where BaMan stands off-screen",
     ("DA1", "Cô ơi, cháu chuyển tiền rồi. Cô mua bánh chưng cho các em nhé. Năm nay các em có Tết rồi.", 0.4, 6.0)),
    ("01-10", "Lộ là đuổi ra đường", 5, "BENXE", ["BM1", "DA1"],
     "50mm two-shot, slow push-in",
     "BaMan suddenly grabs Dat's hand with both of hers and grips it hard, looking up at him with fierce, frightened eyes",
     ("BM1", "Lộ ra là ông đuổi cả hai bà cháu ra đường đấy.", 0.4, 3.9)),
    ("01-11", "Không còn đường lùi", 3, "BENXE", ["DA1"],
     "85mm close-up, locked off",
     "Dat's smile fades; he looks down at the envelope in his hand, then up toward the road out of town", None),
    # ---- Cảnh 02 · Mười năm mà mày lùn đi à? (sân nhà, chiều 26 Tết)
    ("02-01", "Ông sơn ghế bé", 5, "SAN", ["OT1"],
     "35mm medium-wide shot, slow push-in",
     "OngThinh sits on a low stool in the middle of the courtyard, carefully repainting a tiny child-sized wooden chair with a thin brush, totally absorbed", None),
    ("02-02", "Ông ơi cháu về rồi", 4, "CONG", ["DA1"],
     "35mm medium-wide shot from inside the courtyard looking at the gate, locked off",
     "Dat bursts through the brick gate with his arms flung wide and a huge over-acted grin, backpack bouncing",
     ("DA1", "Ông ơi! Cháu về rồi!", 0.3, 2.0)),
    ("02-03", "Cái ôm cứng đơ", 4, "SAN", ["OT1", "DA1"],
     "50mm two-shot, locked off",
     "Dat throws his arms around OngThinh from the side; the old man goes stiff as a plank, the paintbrush frozen in mid-air, dripping", None),
    ("02-04", "Mày là", 5, "SAN", ["OT1"],
     "85mm close-up, very slow push-in",
     "OngThinh looks up at the young man for a long, unreadable moment, eyes narrowing",
     ("OT1", "Mày là…", 1.8, 2.8)),
    ("02-05", "Bà nín thở", 3, "CONG", ["BM1"],
     "85mm close-up, locked off",
     "BaMan stands just inside the gate clutching her bag, holding her breath, eyes wide", None),
    ("02-06", "Mười năm lùn đi", 5, "SAN", ["OT1"],
     "85mm close-up, locked off",
     "OngThinh squints, completely unimpressed, and goes back to painting",
     ("OT1", "…thằng Minh. Mười năm mà mày lùn đi à?", 0.5, 4.2)),
    ("02-07", "Ăn uống kham khổ", 4, "CONG", ["BM1"],
     "50mm medium close-up, locked off",
     "BaMan forces a too-bright laugh, flapping one hand",
     ("BM1", "Thành phố người ta ăn uống kham khổ.", 0.3, 3.0)),
    ("02-08", "Ghế của ai", 4, "SAN", ["OT1", "DA1"],
     "50mm two-shot, locked off",
     "Dat crouches beside the tiny chair, pointing at it with a curious grin; OngThinh keeps painting",
     ("DA1", "Ghế của ai mà bé thế hả ông?", 0.3, 2.4)),
    ("02-09", "Một thằng không ngồi nữa", 5, "SAN", ["OT1"],
     "85mm close-up, locked off",
     "OngThinh puts down the brush, speaks without looking up, then slowly stands with a hand on his knee",
     ("OT1", "Của một thằng không ngồi nữa.", 0.6, 3.2)),
    ("02-10", "Ông liếc cằm", 3, "SAN", ["OT1"],
     "extreme close-up on his eyes, locked off",
     "As he turns away, OngThinh's sharp eyes flick down for a split second toward the young man's chin off-screen, then away", None),
    ("02-11", "Đạt ngơ ngác", 3, "SAN", ["DA1"],
     "50mm medium shot, locked off",
     "Dat is left crouching beside the tiny wet chair, grin slowly fading, watching the old man walk into the house", None),
]

LOOK = B.LOOK; PEOPLE = B.PEOPLE
lines = ["# Phần 01 — 2 phút đầu (bản 2): câu mở đầu + cảnh 01 + cảnh 02", "",
         "*Sinh bởi `_tools/build_p01.py`.* Mỗi shot tạo một lần trên Flow: **Video → Ingredients**, đính đúng nhân vật ở cột *Đính*, "
         "dán nguyên `film/p01/<shot>.txt`, đặt tên clip `P01-<shot> · <tên>`. Shot 00-05 không có nhân vật: Text-to-Video.", "",
         "| Shot | Tên trên Flow | Giây | Đính | Thoại |", "|---|---|---|---|---|"]
total = 0
for s in SHOTS:
    code, name, dur, place, looks, cam, action, line = s
    total += dur
    B.write(f"film/p01/{code}.txt", B.shot_prompt((code, name, dur, place, looks, cam, action, line)))
    lines.append(f"| {code} | P01-{code} · {name} | {dur} | {', '.join(LOOK[c]['flow'] for c in looks) or '— (Text-to-Video)'} | "
                 f"{(PEOPLE[LOOK[line[0]]['person']]['vn'] + ': ' + line[1]) if line else '—'} |")
need = sorted({c for s in SHOTS for c in s[4]})
lines += ["", f"**Tổng: {len(SHOTS)} shot, {total} giây.** Nhân vật Flow cần có: " + ", ".join(f"{c} ({LOOK[c]['flow']})" for c in need), ""]
B.write("film/PHAN_01.md", "\n".join(lines))
print(len(SHOTS), "shot,", total, "giây; cần:", ", ".join(LOOK[c]['flow'] for c in need))
