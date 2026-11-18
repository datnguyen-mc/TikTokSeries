#!/usr/bin/env python3
"""Bản điện ảnh: shot 3–5 giây, cắt dựng nhiều, thoại nhiều. Cảnh 00 (mở đầu), 01, 02, 03 theo CAU_CHUYEN_v2.md.
Chạy: python3 hop-dong-lam-chau/_tools/build_shots.py [00 01 ...] → film/v3/cNN/NN-SS.txt + film/v3/SHOTS.md"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_flow_files as B

LOOK, PEOPLE = B.LOOK, B.PEOPLE
# Bà Thoa chỉ có MỘT điện thoại
LOOK["BT1"]["outfit"] = ("a loud magenta floral-print velvet jacket, a patterned silk scarf, black trousers; she carries exactly one "
                         "smartphone, clipped to a short selfie stick in one hand, and never holds a second phone")

CINE = ("Feature-film cinematography for a premium Vietnamese family drama-comedy: shot on ARRI Alexa 35 with Cooke anamorphic/i "
        "lenses, 24 fps, 16:9 full frame without letterbox bars; deliberate cinematic blocking with foreground elements and "
        "layered depth, motivated natural light (low winter sun, practical lamps, firelight), soft haze in the air, rich true-to-life "
        "Vietnamese skin tones, gentle film halation and fine 35mm grain, shallow depth of field with creamy bokeh. Restrained, "
        "truthful acting with micro-expressions, like an award-winning Asian festival film; never CGI, never a video game, never an advertisement.")

PLACES = dict(B.PLACES)
PLACES["SAN_BAO"] = PLACES["SAN"][:-1] + "; under the eaves a worn carpenter's workbench with a hand plane and curls of fresh wood shavings."
PLACES["SAN_THOA"] = PLACES["SAN"][:-1] + "; beyond the low wall, the neighbour's garden."
SOUND = dict(B.SOUND)
SOUND["SAN_BAO"] = SOUND["SAN"] + ", the soft rasp of a hand plane on wood"
SOUND["SAN_THOA"] = SOUND["SAN"]
SOUND["BENXE_PHANH"] = "a coach's air brakes hissing loudly, then its door folding open"
PLACES["BENXE_PHANH"] = PLACES["BENXE"]


PLACES["BEP"] = ("A dim traditional Northern Vietnamese village kitchen: a blackened wood-fired clay stove, hanging soot-dark pots, a stack of "
                 "firewood, a small window letting in late-afternoon light through drifting smoke; warm smoky light.")
PLACES["GACXEP"] = ("A low wooden attic loft under the tile roof at night: rough beams, stacked old bamboo baskets, a reed mat on the floor, a tiny "
                    "window with cold moonlight, an old dark-wood cabinet closed with a rusty padlock; warm glow from a small oil lamp.")
PLACES["CAUTHANG"] = "The bottom of a steep narrow wooden staircase leading up to the attic, at night, almost dark, a sliver of oil-lamp light falling from above."
PLACES["CHOHOA"] = ("A crowded district flower market on a hazy winter morning a few days before Lunar New Year: rows of pink peach-blossom "
                    "branches and potted kumquat trees, red paper decorations, vendors' stalls under tarps, soft low sunlight through the haze.")
PLACES["SAN_BANH"] = PLACES["SAN"][:-1] + ("; on a woven mat in the courtyard: a pile of glossy green dong leaves, a basin of soaked sticky rice, "
                    "mung beans, pork belly, bamboo strings and square wooden moulds.")
SOUND["BEP"] = "crackling firewood, a pot lid rattling softly"
SOUND["GACXEP"] = "night crickets, wind on the roof tiles, the oil lamp hissing faintly"
SOUND["CAUTHANG"] = "night crickets, a creaking stair board"
SOUND["CHOHOA"] = "a busy market murmur, vendors calling in the distance, rustling plastic, a motorbike horn far off"
SOUND["SAN_BANH"] = SOUND["SAN"] + ", leaves rustling and bamboo strings snapping tight"

AVOID = ("On-screen text, TV channel logos or broadcaster bugs in any corner, character tags or @names written on screen, subtitles, captions, logos, watermarks, readable writing on paper, screens, envelopes or signs; "
         "any cut or second camera angle; the same person appearing twice, twins, clones or look-alike doubles; a second phone; "
         "extra people in focus; distorted hands or fused fingers; face, hair or costume changes; plastic or waxy skin; flashing or "
         "cutting to an attached reference portrait or a plain grey studio backdrop; repeated, echoed or stuttered words; an off-screen "
         "narrator; background music; Southern or Central Vietnamese accents.")

BM, BM2, DA, DA3, OT, OT2, MI, BT = "BM1", "BM2", "DA1", "DA3", "OT1", "OT2", "MI2", "BT1"
DA2, OT3 = "DA2", "OT3"
# (mã, tên, giây, bối cảnh, [bộ đồ], máy quay, hành động, [(bộ đồ, câu, t0, t1)], âm thanh thêm)
SCENES = {
"00": ("Mở đầu · sáng 29 Tết", [
 ("00-01", "Cổng mở", 4, "CONG", [MI, DA3], "35mm wide, low angle from inside the courtyard through the arched gate, slow push-in, morning haze backlit by the sun",
  "Dat stands on a short bamboo ladder hanging a red lantern; the old gate creaks open and Minh stands in it, backpack on one shoulder; Dat freezes with the lantern in mid-air", [], "the gate hinge creaks"),
 ("00-02", "Đứa nào cháu thật", 3, "SAN_THOA", [BT], "50mm medium close-up over the low brick wall, quick push-in, phone screen glow on her face",
  "BaThoa pops up over the low brick wall, her single phone raised high on its selfie stick, mouth dropping open", [(BT, "Thế đứa nào là cháu thật?", 0.3, 2.3)], ""),
 ("00-03", "Hai người nhìn nhau", 3, "CONG", [MI, DA3], "over-the-shoulder from behind Minh, 50mm, Minh soft and dark in the foreground, Dat sharp on the ladder beyond",
  "Dat stares back down at Minh, the red lantern swaying gently in his hand", [], ""),
 ("00-04", "Minh vào ăn sáng", 4, "HIEN", [OT2], "50mm medium shot, locked off, warm side light from the open doors",
  "OngThinh steps out onto the veranda leaning on his walking stick, looks from one young man to the other off-screen, then turns warmly toward camera-left", [(OT2, "Minh, vào ăn sáng con.", 1.4, 3.4)], ""),
 ("00-05", "Minh chết lặng", 3, "CONG", [MI], "85mm close-up, locked off, breath misting in the cold air", "Minh stands frozen in the gateway, stunned and silent", [], ""),
 ("00-06", "Xe khách phanh", 3, "BENXE_PHANH", [], "low shot at wheel level, locked off", "An old coach rolls in and stops hard in front of camera, dust swirling around its front wheel; the folding door opens", [], ""),
]),
"01": ("Đơn hàng cháu đích tôn · bến xe huyện, 26 Tết", [
 ("01-01", "Đạt xuống xe", 4, "BENXE", [DA], "35mm medium-wide, slow pan following him through the crowd, backlit morning haze",
  "Dat hops down from the coach step in his try-hard outfit and looks around the crowd", [], ""),
 ("01-02", "Tập câu chào", 3, "BENXE", [DA], "50mm medium close-up, slight handheld",
  "Dat practises an exaggerated warm grin to himself, mouthing the words under his breath", [(DA, "Ông ơi, cháu về rồi… Ông ơi!", 0.3, 2.6)], ""),
 ("01-03", "Bà túm tay áo", 4, "BENXE", [BM, DA], "50mm medium two-shot, handheld, crowd passing in the foreground",
  "BaMan pushes through the crowd, grabs Dat's sleeve and tugs him toward a concrete pillar", [(BM, "Cậu Đạt phải không? Ra đây, ra đây!", 0.4, 2.8)], ""),
 ("01-04", "Bà dúi phong bì", 5, "BENXE", [BM, DA], "50mm two-shot half hidden behind a concrete pillar, slow push-in",
  "BaMan glances around, then presses a thick red envelope into Dat's hands and folds his fingers over it", [(BM, "Năm ngày thôi. Cháu làm cháu nội tôi, đừng để ông biết.", 0.4, 4.4)], ""),
 ("01-05", "Phong bì dày", 3, "BENXE", [DA], "macro insert of hands, shallow focus",
  "Dat's thumb flicks the edge of the thick red envelope, feeling its weight", [], ""),
 ("01-06", "Đọc hợp đồng", 5, "BENXE", [BM], "50mm medium close-up, locked off",
  "BaMan holds a folded sheet of paper close to her face (writing never readable) and recites it in a solemn sing-song like a temple prayer", [(BM, "Một, không để ông biết. Hai, không lên gác mở cái tủ gỗ.", 0.4, 4.5)], ""),
 ("01-07", "Phải đi trước giao thừa", 4, "BENXE", [BM], "65mm close-up, locked off", "BaMan keeps reciting, eyes half closed", [(BM, "Ba, phải đi trước giao thừa.", 0.4, 2.6)], ""),
 ("01-08", "Điều năm", 4, "BENXE", [BM], "65mm close-up, locked off", "BaMan lowers the paper and looks up over it, suddenly very matter-of-fact",
  [(BM, "Điều năm, công ty cậu ghi: lộ thì đền gấp đôi.", 0.3, 3.6)], ""),
 ("01-09", "Gấp đôi ạ", 3, "BENXE", [DA], "85mm close-up, locked off", "Dat's grin freezes; he swallows hard", [(DA, "Gấp… đôi ạ?", 0.8, 2.2)], ""),
 ("01-10", "Ông hay lẫn", 5, "BENXE", [BM], "85mm close-up, very slow push-in", "BaMan speaks quietly, eyes wet and worried, twisting the strap of her cloth bag",
  [(BM, "Từ hôm tai biến ông hay lẫn. Hôm trước còn gọi tôi bằng tên thằng con.", 0.4, 4.6)], ""),
 ("01-11", "Ông nhớ từng tí", 4, "BENXE", [BM], "85mm close-up, locked off", "BaMan looks straight at Dat, very serious",
  [(BM, "Nhưng chuyện thằng Minh thì ông nhớ từng tí.", 0.4, 3.2)], ""),
 ("01-12", "Anh Minh thế nào", 4, "BENXE", [DA, BM], "over-the-shoulder from behind BaMan onto Dat, 50mm", "Dat leans in, eager, notebook-style attentive",
  [(DA, "Thế anh Minh là người thế nào hả bà?", 0.3, 2.6)], ""),
 ("01-13", "Nó hiền ít nói", 3, "BENXE", [BM, DA], "reverse over-the-shoulder from behind Dat onto BaMan, 50mm", "BaMan gives a small proud smile",
  [(BM, "Nó hiền, ít nói.", 0.4, 1.9)], ""),
 ("01-14", "Ít nói thì diễn được", 3, "BENXE", [DA], "50mm medium close-up, locked off", "Dat flashes a confident thumbs-up and a wink",
  [(DA, "Ít nói thì cháu diễn được.", 0.3, 2.1)], ""),
 ("01-15", "Gọi về mái ấm", 5, "BENXE", [DA], "50mm medium shot beside the coach, slight handheld, soft backlight",
  "Alone by the coach, Dat holds an old phone to his ear (screen never visible), speaking softly with a tender smile",
  [(DA, "Cô ơi, cháu chuyển tiền rồi. Cô mua bánh chưng cho các em nhé.", 0.4, 4.5)], ""),
 ("01-16", "Các em có Tết", 4, "BENXE", [DA], "85mm close-up, slow push-in", "Dat's voice softens, his eyes glistening a little",
  [(DA, "Năm nay các em có Tết rồi cô ạ.", 0.4, 2.8)], ""),
 ("01-17", "Lộ là đuổi ra đường", 5, "BENXE", [BM, DA], "50mm two-shot, slow push-in",
  "BaMan suddenly grabs Dat's hand with both of hers and grips it hard, looking up at him with fierce, frightened eyes",
  [(BM, "Lộ ra là ông đuổi cả hai bà cháu ra đường đấy.", 0.4, 3.9)], ""),
 ("01-18", "Không còn đường lùi", 3, "BENXE", [DA], "85mm close-up, locked off", "Dat's smile fades; he looks toward the road out of town", [], ""),
]),
"02": ("Mười năm mà mày lùn đi à? · sân nhà, chiều 26 Tết", [
 ("02-01", "Ông sơn ghế bé", 5, "SAN", [OT], "35mm wide, slow push-in, low golden afternoon sun raking across the bricks",
  "OngThinh sits on a low stool in the middle of the courtyard, carefully repainting a tiny child-sized wooden chair, totally absorbed", [], ""),
 ("02-02", "Nét cọ", 3, "SAN", [OT], "macro insert, shallow focus", "OngThinh's knotted carpenter's hand draws a slow stroke of paint along the tiny chair's backrest", [], ""),
 ("02-03", "Ông ơi cháu về rồi", 4, "CONG", [DA], "35mm medium-wide from inside the courtyard looking at the gate, locked off",
  "Dat bursts through the brick gate with his arms flung wide and a huge over-acted grin, backpack bouncing", [(DA, "Ông ơi! Cháu về rồi!", 0.3, 2.0)], ""),
 ("02-04", "Cọ dừng lại", 3, "SAN", [OT], "85mm close-up in profile, locked off", "OngThinh's brush stops mid-stroke; he does not turn around", [], ""),
 ("02-05", "Cái ôm cứng đơ", 4, "SAN", [OT, DA], "50mm two-shot, locked off", "Dat throws his arms around OngThinh from the side; the old man goes stiff as a plank, the brush frozen in mid-air", [], ""),
 ("02-06", "Mày là", 5, "SAN", [OT], "85mm close-up, very slow push-in", "OngThinh slowly looks up at the young man for a long, unreadable moment",
  [(OT, "Mày là…", 2.0, 3.0)], ""),
 ("02-07", "Bà nín thở", 3, "CONG", [BM], "85mm close-up, locked off", "BaMan stands just inside the gate clutching her bag, holding her breath", [], ""),
 ("02-08", "Mười năm lùn đi", 5, "SAN", [OT], "85mm close-up, locked off", "OngThinh squints, completely unimpressed, and goes back to painting",
  [(OT, "…thằng Minh. Mười năm mà mày lùn đi à?", 0.5, 4.2)], ""),
 ("02-09", "Ăn uống kham khổ", 4, "CONG", [BM], "50mm medium close-up, locked off", "BaMan forces a too-bright laugh, flapping one hand",
  [(BM, "Thành phố người ta ăn uống kham khổ.", 0.3, 3.0)], ""),
 ("02-10", "Kham khổ lắm ạ", 3, "SAN", [DA], "50mm medium close-up, locked off", "Dat laughs along a beat too late, nodding hard",
  [(DA, "Dạ… kham khổ lắm ông ạ.", 0.3, 2.3)], ""),
 ("02-11", "Ghế của ai", 4, "SAN", [OT, DA], "50mm two-shot at low height, locked off", "Dat crouches beside the tiny chair, pointing at it with a curious grin; OngThinh keeps painting",
  [(DA, "Ghế của ai mà bé thế hả ông?", 0.3, 2.4)], ""),
 ("02-12", "Một thằng không ngồi nữa", 5, "SAN", [OT], "85mm close-up, locked off", "OngThinh puts down the brush and speaks without looking up, then slowly stands with a hand on his knee",
  [(OT, "Của một thằng không ngồi nữa.", 0.6, 3.2)], ""),
 ("02-13", "Ông liếc cằm", 3, "SAN", [OT], "extreme close-up on his eyes, locked off", "As he turns away, OngThinh's sharp eyes flick down for a split second toward the young man's chin off-screen", [], ""),
 ("02-14", "Đạt ngơ ngác", 3, "SAN", [DA], "50mm medium shot, locked off", "Dat is left crouching alone beside the tiny wet chair, grin slowly fading", [], ""),
]),
"03": ("Thi kiến thức cháu đích tôn · sân nhà, 27 Tết", [
 ("03-01", "Bà Thoa lên live", 4, "SAN_THOA", [BT], "50mm medium shot over the low brick wall, slow push-in",
  "BaThoa pops up over the wall, her one phone on its selfie stick held high, talking brightly into it like a TV host", [(BT, "Các cháu ơi, xem live với bà nhé!", 0.3, 2.6)], ""),
 ("03-02", "Mười năm mới về", 5, "SAN_THOA", [BT], "65mm close-up, phone glow on her face, locked off",
  "BaThoa turns the selfie stick to show the courtyard behind her, eyebrows dancing", [(BT, "Cháu đích tôn nhà ông Thịnh mười năm mới về này!", 0.4, 3.8)], ""),
 ("03-03", "Đạt vẫy máy", 3, "SAN", [DA], "50mm medium shot, locked off", "Dat spots the phone, straightens his collar and waves at it with a stiff, over-eager grin",
  [(DA, "Dạ… cháu chào cả nhà ạ!", 0.4, 2.3)], ""),
 ("03-04", "Bà hỏi tí", 4, "SAN", [BT, DA], "35mm medium-wide two-shot, locked off",
  "BaThoa squeezes through a gap in the wall into the courtyard and marches toward Dat, her one phone held out in front", [(BT, "Đứng đấy! Bà hỏi tí!", 0.4, 2.2)], ""),
 ("03-05", "Mẹ mày tên gì", 3, "SAN", [BT, DA], "over-the-shoulder from behind Dat onto BaThoa, 50mm", "BaThoa thrusts the phone toward Dat's face",
  [(BT, "Mẹ mày tên gì?", 0.3, 1.5)], ""),
 ("03-06", "Mẹ ạ", 4, "SAN", [DA, BT], "reverse over-the-shoulder from behind BaThoa onto Dat, 50mm", "Dat blinks, thinking hard, then answers with a hopeful smile",
  [(DA, "Dạ… mẹ cháu tên là… Mẹ ạ!", 0.5, 3.4)], ""),
 ("03-07", "Bà Mận sặc", 3, "SAN", [BM2], "50mm medium shot in the doorway, locked off", "BaMan, holding a tea tray in the doorway, chokes and coughs into her hand, cups rattling", [], "a sharp non-verbal cough, no words"),
 ("03-08", "Đái dầm", 4, "SAN", [BT, DA], "over-the-shoulder from behind Dat onto BaThoa, 50mm", "BaThoa narrows her eyes and fires the next question, grinning",
  [(BT, "Năm lớp mấy mày đái dầm ở nhà bà?", 0.3, 2.8)], ""),
 ("03-09", "Mồ hôi", 3, "SAN", [DA], "85mm close-up, locked off", "Dat stands frozen, a bead of sweat sliding down his temple, smile stuck in place", [], ""),
 ("03-10", "Ngã cây gì", 3, "SAN", [BT], "65mm close-up, locked off", "BaThoa leans in with a sly grin", [(BT, "Thế hồi bé mày ngã cây gì?", 0.3, 2.3)], ""),
 ("03-11", "Đạt cứng họng", 3, "SAN", [DA], "85mm close-up, slow push-in", "Dat opens his mouth but nothing comes out; his eyes dart around the courtyard in panic", [], ""),
 ("03-12", "Cây bưởi", 4, "SAN_BAO", [OT], "50mm medium shot, OngThinh at his workbench in the foreground, locked off",
  "OngThinh keeps pushing his hand plane along a plank, never looking up, and answers flatly", [(OT, "Cây bưởi. Nó ngã cây bưởi.", 0.6, 3.2)], ""),
 ("03-13", "Ông vẫn nhớ", 4, "SAN", [BM2], "85mm close-up in the doorway, locked off", "BaMan whispers to herself in quiet surprise, eyes softening",
  [(BM2, "Ông vẫn nhớ cái đấy cơ à…", 0.5, 2.9)], ""),
 ("03-14", "Nhai kẹo lạc", 3, "SAN", [DA], "50mm medium shot by a low table with a plate of peanut brittle, locked off",
  "Dat relaxes, grabs a piece of peanut brittle and chews happily", [], ""),
 ("03-15", "Dị ứng lạc", 5, "SAN", [BT], "65mm close-up, slow push-in", "BaThoa slowly lowers her phone, eyes narrowing at something off-screen, and speaks with relish",
  [(BT, "Lạ nhỉ. Thằng Minh hồi bé dị ứng lạc cơ mà?", 0.6, 4.0)], ""),
 ("03-16", "Đạt đơ người", 3, "SAN", [DA], "85mm close-up, locked off", "Dat freezes mid-chew, cheeks full, eyes wide", [], ""),
]),
"04": ("Dị ứng theo yêu cầu · sân, bếp, gác xép, 27 Tết", [
 ("04-01", "Phun kẹo lạc", 4, "SAN", [DA], "50mm medium shot, slight handheld",
  "Dat spits the peanut brittle into his palm and clutches his throat, wildly over-acting", [(DA, "Ối! Ngứa! Ngứa quá!", 0.4, 2.2)], ""),
 ("04-02", "Lăn ra phản", 5, "SAN", [DA], "35mm medium-wide, locked off",
  "Dat flops onto a bamboo daybed, scratching his neck furiously, legs kicking like a stage actor", [], "exaggerated non-verbal groans, no words"),
 ("04-03", "Dị ứng thật à", 4, "SAN", [BT], "50mm medium close-up, locked off",
  "BaThoa takes a step back, lowering her single phone on its selfie stick, suddenly unsure", [(BT, "Ơ… dị ứng thật à?", 0.4, 2.2)], ""),
 ("04-04", "Bà về đây", 4, "SAN_THOA", [BT], "35mm medium-wide, locked off",
  "BaThoa backs out through the gap in the low wall, waving her free hand, muttering", [(BT, "Thôi bà về, bà về…", 0.5, 2.4)], ""),
 ("04-05", "Hé một mắt", 3, "SAN", [DA], "85mm close-up, locked off", "Dat, still lying on the daybed, cracks open one eye to check she has gone", [], ""),
 ("04-06", "Ăn đi khỏi rồi", 5, "SAN_BAO", [OT, DA], "50mm two-shot across the workbench, locked off",
  "Without looking up, OngThinh slides a plate of peanut brittle across the bench toward Dat, then goes back to his plane",
  [(OT, "Ăn đi.", 1.2, 1.9), (OT, "Khỏi rồi.", 3.0, 3.8)], ""),
 ("04-07", "Đạt nhìn đĩa lạc", 3, "SAN", [DA], "85mm close-up, locked off", "Dat stares at the plate, totally confused", [], ""),
 ("04-08", "Ông lẫn thật rồi", 6, "BEP", [BM2], "65mm close-up by the stove, slow push-in, firelight on her face",
  "BaMan stirs a pot, then wipes her eye with the corner of her apron", [(BM2, "Ông lẫn thật rồi. Đến cả chuyện thằng cháu dị ứng cũng quên.", 0.6, 5.2)], ""),
 ("04-09", "Lên gác xép", 4, "GACXEP", [DA2], "35mm wide from inside the attic, locked off",
  "Dat climbs up into the attic with a small oil lamp, ducking under the beams, and notices the padlocked wooden cabinet", [], ""),
 ("04-10", "Ổ khoá", 3, "GACXEP", [DA2], "macro insert, shallow focus",
  "Dat's hand reaches toward the rusty padlock on the cabinet, hesitates, then pulls back", [], ""),
 ("04-11", "Gọi cho sếp", 12, "GACXEP", [DA2], "one continuous take: 50mm, very slow push-in from medium to close-up, moonlight from the tiny window and lamplight on his face",
  "Dat sits on the reed mat with his back to the cabinet, an old phone pressed to his ear (screen never visible), speaking quietly, the over-acting gone",
  [(DA2, "Ba mươi triệu… em biết rồi anh.", 0.5, 3.0), (DA2, "Tiền cọc em gửi về mái ấm rồi. Em nhận vụ này vì tiền.", 4.2, 7.6),
   (DA2, "Với lại… em muốn biết Tết có ông bà nó thế nào.", 8.6, 11.6)], ""),
 ("04-12", "Ông đứng dưới cầu thang", 5, "CAUTHANG", [OT3], "50mm medium shot from above, locked off, face half in shadow",
  "OngThinh stands silently at the bottom of the attic stairs in the dark, a hand plane in his hand, listening; he coughs softly once", [], "one soft non-verbal cough at 3.5s, no words"),
 ("04-13", "Đạt sững lại", 3, "GACXEP", [DA2], "85mm close-up, locked off", "Dat freezes, phone still at his ear, eyes turning toward the stairs", [], ""),
]),
"05": ("Cành đào xấu nhất chợ · chợ hoa huyện, 27 Tết", [
 ("05-01", "Chợ hoa", 5, "CHOHOA", [], "high wide establishing shot, slow drift", "The flower market bustles, a sea of pink peach blossoms and kumquat trees", [], ""),
 ("05-02", "Hai ông cháu đi chợ", 8, "CHOHOA", [OT2, DA2], "one continuous take: 35mm tracking shot moving backward ahead of them",
  "OngThinh walks slowly with his stick through the market lane, Dat beside him gawking at the blossoms; neither speaks", [], ""),
 ("05-03", "Mày chọn đi", 4, "CHOHOA", [OT2], "65mm close-up, locked off", "OngThinh stops and speaks without looking at Dat",
  [(OT2, "Mày chọn đi. Như mọi năm.", 0.5, 3.2)], ""),
 ("05-04", "Như mọi năm", 3, "CHOHOA", [DA2], "85mm close-up, locked off", "Dat's eyes dart around in panic", [], ""),
 ("05-05", "Cành đào khẳng khiu", 5, "CHOHOA", [DA2], "50mm medium shot, slow push-in",
  "Dat drifts past lush full branches and stops at one scrawny, crooked peach branch leaning alone against a wall", [], ""),
 ("05-06", "Không ai mua thì buồn", 5, "CHOHOA", [DA2], "65mm close-up, locked off", "Dat lifts the crooked branch gently and smiles at it",
  [(DA2, "Cành này không ai mua thì nó buồn.", 0.6, 3.6)], ""),
 ("05-07", "Ông khựng lại", 5, "CHOHOA", [OT2], "85mm close-up, very slow push-in", "OngThinh freezes; his eyes widen, then slowly fill with tears", [], ""),
 ("05-08", "Trả tiền không mặc cả", 4, "CHOHOA", [OT2], "50mm medium shot, locked off",
  "OngThinh silently hands folded notes to a vendor whose face is out of frame, without bargaining", [], ""),
 ("05-09", "Về thôi cháu", 6, "CHOHOA", [OT2, DA2], "50mm two-shot, locked off",
  "OngThinh turns to Dat with red eyes and speaks low; Dat, holding the branch, is stunned", [(OT2, "Về thôi, cháu.", 2.0, 3.6)], ""),
 ("05-10", "Đi về giữa chợ", 8, "CHOHOA", [OT2, DA2], "one continuous take: 35mm from behind, slow follow",
  "They walk away down the market lane, Dat carrying the crooked branch over his shoulder, OngThinh a step ahead", [], ""),
]),
"06": ("Gói bánh chưng · sân nhà, sáng 28 Tết", [
 ("06-01", "Tay ông gói bánh", 8, "SAN_BANH", [OT], "one continuous take: 50mm macro-ish close on the hands, slow slide",
  "OngThinh's knotted hands fold dong leaves into a square wooden mould, add sticky rice, mung beans and pork, then tie bamboo strings into a perfectly square cake", [], ""),
 ("06-02", "Bánh méo như gối", 4, "SAN_BANH", [DA2], "50mm medium shot, locked off", "Dat proudly holds up his own cake: lumpy and pillow-shaped", [], ""),
 ("06-03", "Các cụ tưởng nghèo", 5, "SAN_BANH", [OT], "65mm close-up, locked off", "OngThinh glances at it, deadpan",
  [(OT, "Bánh này mà đặt lên bàn thờ, các cụ tưởng nhà mình nghèo.", 0.5, 4.6)], ""),
 ("06-04", "Bà cười", 3, "SAN_BANH", [BM2], "50mm medium close-up, locked off", "BaMan laughs behind her hand", [], "a soft non-verbal laugh"),
 ("06-05", "Méo nhưng chắc", 3, "SAN_BANH", [DA2], "50mm medium close-up, locked off", "Dat pats his lumpy cake, grinning",
  [(DA2, "Méo nhưng mà chắc ạ!", 0.4, 2.0)], ""),
 ("06-06", "Bố thằng Minh gói vuông nhất", 6, "SAN_BANH", [OT], "85mm close-up, slow push-in", "OngThinh ties a string, his voice softening",
  [(OT, "Ngày xưa bố thằng Minh gói vuông nhất làng.", 0.8, 4.2)], ""),
 ("06-07", "Bố cháu mất thế nào", 4, "SAN_BANH", [DA2], "65mm close-up, locked off", "Dat, absorbed, blurts out the question",
  [(DA2, "Bố cháu… mất thế nào hả ông?", 0.6, 3.0)], ""),
 ("06-08", "Bà đánh rơi lạt", 3, "SAN_BANH", [BM2], "macro insert, shallow focus", "Bamboo strings slip from BaMan's fingers onto the leaves; her hands freeze", [], ""),
 ("06-09", "Hỏi như người ngoài", 5, "SAN_BANH", [OT], "85mm close-up, locked off", "OngThinh keeps tying, never looking up",
  [(OT, "Mày hỏi như người ngoài ấy.", 1.0, 3.6)], ""),
 ("06-10", "Đạt cúi đầu", 4, "SAN_BANH", [DA2], "85mm close-up, locked off", "Dat's face falls; he looks down at his lumpy cake", [], ""),
 ("06-11", "Ba người im lặng", 10, "SAN_BANH", [OT, DA2, BM2], "one continuous take: 35mm, slow crane back and up from the mat",
  "The three of them keep wrapping in silence around the pile of leaves; only the strings and leaves make sound", [], ""),
 ("06-12", "Ngón tay trên nút lạt", 4, "SAN_BANH", [OT], "macro insert, shallow focus", "OngThinh's thumb rests on the knot of a square cake; his hand stops, lost in memory", [], ""),
]),
}


def prompt(s):
    code, name, dur, place, looks, cam, action, lines, extra = s
    out = [f"A single continuous {dur}-second shot, 16:9, one camera angle, no cuts.", "", f"[LOOK] {CINE}", "", f"[PLACE] {PLACES[place]}", ""]
    if looks:
        out.append("[CHARACTERS] Use the attached character image for each person: same face, same hair, same outfit, exactly.")
        for c in looks:
            lk = LOOK[c]; p = PEOPLE[lk["person"]]
            out.append(f"- @{lk['person']} = {p['vn']}, {p['role']} ({p['face'].split(',')[0]}); wears {lk['outfit']}. Attached image: \"{lk['flow']}\".")
        out.append("Each named person appears exactly once. Background people stay distant, blurred and clearly different from them.")
    else:
        out.append("[CHARACTERS] No named characters; any people in frame are distant, blurred, seen only from behind or below the waist.")
    out += ["", f"[CAMERA] {cam}.", "", f"[ACTION] {action}.", ""]
    if lines:
        out.append("[DIALOGUE] In Vietnamese with exact lip-sync, standard Northern Vietnamese accent; each line spoken exactly once, on camera; only the speaker moves the lips:")
        for c, t, a, b in lines:
            per = LOOK[c]["person"]
            out.append(f"- {a:.1f}s–{b:.1f}s, @{per} ({PEOPLE[per]['voice']}): {t}")
        out.append(f"After the last word nobody speaks until {dur:.1f}s. Never read these directions aloud.")
    else:
        out.append("[DIALOGUE] None. Every mouth stays closed; no voices at all.")
    snd = SOUND[place] + (f"; {extra}" if extra else "")
    out += ["", f"[SOUND] {snd}. No music.", "", f"[AVOID] {AVOID}", ""]
    return "\n".join(out)


def main():
    only = sys.argv[1:] or list(SCENES)
    md = ["# Bản điện ảnh v3 — shot 3–5 giây", "", "*Sinh bởi `_tools/build_shots.py`.* Flow: Video → Thành phần, Omni 1.2 Flash, 720p, x1. "
          "Tên trên Flow: `V3-<shot> · <tên>`. Sau khi tạo, thêm vào mục **Cảnh** của Flow theo từng cảnh.", ""]
    tot = 0
    for sc in SCENES:
        title, shots = SCENES[sc]
        md += [f"## Cảnh {sc} · {title}", "", "| Shot | Giây | Đính | Thoại |", "|---|---|---|---|"]
        for s in shots:
            if sc in only:
                B.write(f"film/v3/c{sc}/{s[0]}.txt", prompt(s))
            tot += s[2]
            md.append(f"| {s[0]} · {s[1]} | {s[2]} | {', '.join(LOOK[c]['flow'] for c in s[4]) or 'Text-to-Video'} | "
                      + " / ".join(f"{PEOPLE[LOOK[l[0]]['person']]['vn']}: {l[1]}" for l in s[7]) + " |")
        md.append("")
    md.append(f"**Tổng {sum(len(v[1]) for v in SCENES.values())} shot, {tot} giây.**")
    B.write("film/v3/SHOTS.md", "\n".join(md) + "\n")
    print(sum(len(v[1]) for v in SCENES.values()), "shot", tot, "giây")


if __name__ == "__main__":
    main()
