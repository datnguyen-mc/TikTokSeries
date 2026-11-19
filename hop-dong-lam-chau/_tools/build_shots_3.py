#!/usr/bin/env python3
"""Bản V3.1 · phần 3: hai phân cảnh thêm + các shot làm lại sau rà soát khung hình (18/11).
- 01b  Học làm cháu trên xe buýt về làng (giữa cảnh 01 và 02) — hài, gài sẵn "sẹo ở cằm" và "dị ứng lạc".
- 18b  Những đêm đóng ghế (sau 18-13, trước 19) — ông biết từ đầu, đêm đêm đóng chiếc ghế mới
       mà bà Thoa mang ra bến xe ở 19-07.
- REDO: shot cũ làm lại vì lỗi hình (giữ nguyên mã shot).
Chạy: python3 build_shots_3.py  → film/v3/c01b, c18b, redo/*.txt + film/v3/shots_3.json"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_shots as S1
import build_shots_2 as S2

ROOT = os.path.dirname(HERE)
LOOK = S2.LOOK
# Bà Thoa giờ cầm điện thoại bằng tay (bỏ gậy selfie trông như máy quay)
LOOK["BT1"]["outfit"] = ("a loud magenta floral-print velvet jacket, a patterned silk scarf, black trousers; she holds exactly "
                         "one ordinary smartphone directly in her bare hand (no selfie stick, no gimbal, no tripod)")
LOOK["BT1"]["flow"] = "Bà Thoa · Cầm điện thoại"

S2.PLACES.update({
    "XEBUYT": "The inside of an old rattling rural bus driving through the Northern Vietnamese countryside a few days before "
              "Lunar New Year: worn vinyl seats, sacks of rice and peach-blossom branches in the aisle, a bamboo cage with a "
              "rooster on the floor, other passengers soft and out of focus; hazy winter afternoon light flickering through the windows",
    "XEBUYT_NGOAI": "A narrow country road between harvested rice fields in Northern Vietnam a few days before Lunar New Year, "
                    "an old cream-and-blue rural bus rattling along it toward a distant village gate with red lanterns; hazy golden afternoon",
    "XUONG_DEM": "A corner of the old village house courtyard at night turned into a small carpentry space: a low wooden workbench, "
                 "hand planes and chisels, curls of fresh pale wood shavings, one bare bulb hanging from the eave, deep blue night beyond",
    "SAN_DEM_PHAN": "The dark brick courtyard of the old village house at night: a low bamboo daybed under the eave, a thin floral "
                    "blanket, a small oil lamp glowing on a stool, potted kumquat trees in shadow, deep blue night",
    "TUONG_DEM": "The low brick wall between two village courtyards late at night, a banana tree on the far side, one porch light "
                 "glowing behind, deep blue night",
})
S2.SOUND.update({
    "XEBUYT": "the bus engine rattling, loose windows buzzing, a horn outside, a rooster clucking in its cage",
    "XEBUYT_NGOAI": "a rattling bus engine passing, wind over the fields, birds",
    "XUONG_DEM": "crickets, the soft scrape of a hand plane, a dog barking far away",
    "SAN_DEM_PHAN": "crickets, a young man's slow sleeping breath, the oil lamp hissing faintly",
    "TUONG_DEM": "crickets, banana leaves rustling, a dog far away",
})
X = S2.X
OT3, BM1, BM2, DA1, DA2, MI2, MI3, BT1 = "OT3", "BM1", "BM2", "DA1", "DA2", "MI2", "MI3", "BT1"
OT2, DA3 = "OT2", "DA3"

SCENES = {
    "01b": ("Học làm cháu · xe buýt về làng, chiều 26 Tết", [
        ("01b-01", "Bài học trên xe", 6, "XEBUYT", [BM1, DA1], "35mm two-shot across the aisle, gentle bus sway",
         "BaMan and Dat sit squeezed side by side on a worn bus seat; BaMan unfolds a creased sheet of paper (writing never readable) and pushes it at him",
         [(BM1, "Học thuộc đi. Mười năm của nó, cháu có năm ngày.")], "paper rustling"),
        ("01b-02", "Câu hỏi đầu tiên", 4, "XEBUYT", [BM1], "65mm close-up, bus sway",
         "BaMan quizzes him like a strict teacher, eyes narrowed",
         [(BM1, "Thằng Minh có cái sẹo ở đâu?")], ""),
        ("01b-03", "Cằm nhẵn", 5, "XEBUYT", [DA1], "65mm close-up, bus sway",
         "Dat rubs his own smooth, scar-free chin with two fingers, suddenly worried",
         [(DA1, "Nhưng cằm cháu làm gì có sẹo hả bà?")], ""),
        ("01b-04", "Ông mắt kém", 4, "XEBUYT", [BM1], "65mm close-up, bus sway",
         "BaMan waves the worry away with one hand, not quite convinced herself",
         [(BM1, "Ông mắt kém rồi, không nhìn ra đâu.")], ""),
        ("01b-05", "Dị ứng gì", 4, "XEBUYT", [BM1, DA1], "50mm two-shot, bus sway",
         "BaMan fires the next question; Dat answers instantly like a quiz-show contestant, raising a finger",
         [(BM1, "Nó dị ứng gì?"), (DA1, "Lạc ạ!")], ""),
        ("01b-06", "Tập gọi ông", 6, "XEBUYT", [DA1], "50mm medium close-up, bus sway",
         "Dat clears his throat, spreads his arms wide and calls out in a huge sugary over-acted voice; the caged rooster at his feet flaps and squawks",
         [(DA1, "Ông ơi! Cháu về rồi đây ông ơi!")], "the rooster squawking loudly after the line"),
        ("01b-07", "Cả xe quay lại", 4, "XEBUYT", [], "35mm wide down the aisle, bus sway",
         "Several passengers turn around in their seats to stare; one elderly woman across the aisle, face soft and out of focus, chuckles",
         [(X, "Tập đóng phim à cháu?")], "passengers laughing softly"),
        ("01b-08", "Ít nói thôi", 6, "XEBUYT", [BM1, DA1], "50mm two-shot, bus sway",
         "BaMan pinches Dat's arm and hisses at him; he winces, nods and mimes zipping his lips shut",
         [(BM1, "Nhỏ thôi! Ông nó ít nói, cháu cũng phải ít nói.")], ""),
        ("01b-09", "Xe về làng", 4, "XEBUYT_NGOAI", [], "wide aerial-height shot, slow pan following the bus",
         "The old bus rattles along the road between the fields toward the village gate hung with red lanterns", [], ""),
    ]),
    "18b": ("Những đêm đóng ghế · đêm 26 → 30 Tết", [
        ("18b-01", "Bào gỗ trong đêm", 5, "XUONG_DEM", [OT3], "50mm medium shot, locked off",
         "Alone under the single bulb, OngThinh pushes a hand plane along a fresh pale plank; long curls of wood shavings fall to the bricks",
         [], ""),
        ("18b-02", "Cuốn sổ", 6, "XUONG_DEM", [OT3], "85mm close-up on his hands and face, shallow focus",
         "OngThinh licks the tip of his carpenter's pencil and writes slowly in a small worn notebook (writing never readable), murmuring each word to himself",
         [(OT3, "Thằng bé tên Đạt. Mồ côi. Ăn được lạc.")], "pencil scratching on paper"),
        ("18b-03", "Đắp chăn", 6, "SAN_DEM_PHAN", [OT3, DA2], "50mm, Dat asleep in the foreground, OngThinh stepping in behind",
         "Dat sleeps curled on the bamboo daybed; OngThinh comes over quietly with the oil lamp, looks at him for a long moment and pulls the thin blanket up over the young man's shoulders",
         [], ""),
        ("18b-04", "Ghép chân ghế", 4, "XUONG_DEM", [OT3], "macro insert on hands, shallow focus",
         "OngThinh's knotted hands tap the last leg into a small new wooden chair with a mallet, then press down on the seat to test it; it holds firm",
         [], "two soft mallet taps"),
        ("18b-05", "Bà hỏi", 4, "XUONG_DEM", [BM2], "65mm close-up in the doorway, locked off",
         "BaMan, a shawl over her shoulders, stands in the dark doorway watching him and whispers",
         [(BM2, "Ông đóng ghế cho ai thế?")], ""),
        ("18b-06", "Cho đứa nào cần", 5, "XUONG_DEM", [OT3], "85mm close-up, locked off",
         "OngThinh keeps sanding the chair without looking up; the corner of his mouth lifts into the smallest smile",
         [(OT3, "Cho đứa nào cần ghế.")], "sandpaper on wood"),
        ("18b-07", "Gửi qua tường", 6, "TUONG_DEM", [OT3, BT1], "50mm two-shot over the low wall, locked off",
         "OngThinh lifts a cardboard box tied with string over the low wall into BaThoa's arms; she tucks her phone away, startled, and takes it",
         [(OT3, "Tối ba mươi, mang ra bến xe hộ tôi.")], ""),
    ]),
}

REDO = [
    ("18-05", "Minh đứng sau lưng", 3, "NGHIATRANG_HH", [OT3, MI2], "85mm, OngThinh's beanie and shoulder soft in the foreground, Minh sharp a few steps behind",
     "OngThinh sits on the ground in the soft foreground facing the tomb, seen from behind; Minh stands sharp a few steps behind him, having heard everything", [], ""),
    ("18-08", "Ông chạm vào sẹo", 4, "NGHIATRANG_HH", [OT3, MI2], "50mm two-shot, both sitting on the ground, locked off",
     "Sitting side by side on the ground before the tomb, Minh tilts his chin toward his grandfather; OngThinh's knotted fingers reach over and touch the small scar", [], ""),
    ("18-10", "Ông xin lỗi", 5, "NGHIATRANG_HH", [OT3, MI2], "50mm two-shot, both sitting on the ground, locked off",
     "Sitting side by side on the ground before the tomb, OngThinh finally says it without looking at him; Minh answers gently",
     [(OT3, "Ông xin lỗi."), (MI2, "Con về rồi mà ông.")], ""),
    ("20-02", "Xe dừng đầu ngõ", 3, "CONG_GIAOTHUA", [MI3, DA3], "35mm wide down the lane, locked off",
     "A motorbike stops at the end of the lane just as the fireworks peak: Minh in his cream sweater is driving, Dat in his red puffer jacket sits behind him, both in helmets", [], ""),
    ("17-01", "Chìa khóa", 5, "GACXEP_NGAY", ["BM2", DA3], "50mm two-shot, locked off",
     "BaMan presses an old iron key into Dat's palm and closes his fingers over it",
     [("BM2", "Cháu mở đi. Điều thứ hai bà bỏ.")], ""),
    ("13-01", "Bao nhiêu tiền", 4, "AO", [MI2, DA3], "50mm two-shot, locked off",
     "Minh grabs Dat by the collar of his red jacket, then lets go immediately; no blows. Minh asks clearly and coldly",
     [(MI2, "Bao nhiêu tiền?")], ""),
    ("19-05", "Ông chỉ có cháu", 8, "BENXE_DEM", [MI3], "65mm close-up, slow push-in",
     "Minh delivers his grandfather's message slowly, pausing between sentences; the last sentence is said softly, looking straight at Dat",
     [(MI3, "Ông bảo hợp đồng hết hạn rồi."), (MI3, "Nhưng ông chưa ký hợp đồng nào cả."), (MI3, "Ông chỉ có cháu.")], ""),
    ("20-10", "Nhớ đường về", 5, "MAM_GIAOTHUA", ["OT4"], "85mm close-up, very slow push-in",
     "OngThinh looks at Minh, eyes wet, voice firm; he says the line once and then stays silent",
     [("OT4", "Đi đâu thì đi. Nhớ đường về.")], ""),
]

FIX = ("16:9 full frame edge to edge: no black letterbox bars, no rounded corners, no border, no picture-in-picture frame. "
       "No film cameras, tripods, gimbals, selfie sticks, boom microphones or any filming equipment anywhere in frame.")


def full(s):
    p = S2.prompt(s).replace("envelopes or signs;", "envelopes or signs; black letterbox bars, rounded frame corners or any border; "
                             "film cameras, tripods, gimbals, selfie sticks or any filming equipment;", 1)
    return p.replace("no cuts.", "no cuts. " + FIX, 1)


def main():
    out = []
    for sc, (title, shots) in SCENES.items():
        for s in shots:
            out.append({"code": s[0], "scene": sc, "name": s[1], "dur": s[2], "refs": [LOOK[c]["flow"] for c in s[4]], "prompt": full(s)})
    for s in REDO:
        out.append({"code": s[0], "scene": "redo", "name": s[1], "dur": s[2], "refs": [LOOK[c]["flow"] for c in s[4]], "prompt": full(s)})
    for x in out:
        d = os.path.join(ROOT, "film", "v3", "c" + x["scene"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, x["code"] + ".txt"), "w", encoding="utf-8").write(x["prompt"])
    json.dump(out, open(os.path.join(ROOT, "film", "v3", "shots_3.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(out), "shot,", sum(x["dur"] for x in out), "giây")


if __name__ == "__main__":
    main()
