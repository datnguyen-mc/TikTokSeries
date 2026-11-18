#!/usr/bin/env python3
"""Bản điện ảnh V3 phần 2: cảnh 07–20 (theo kich-ban/canh-XX.md). Shot 2–8 giây, Omni 1.2 Flash, 720p.
Chạy từ gốc repo: python3 hop-dong-lam-chau/_tools/build_shots_2.py [07 08 ...]
→ film/v3/cNN/NN-SS.txt + film/v3/SHOTS_2.md + film/v3/shots_2.json (cho bước render)."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_shots as S

B, LOOK, PEOPLE, CINE, AVOID = S.B, S.LOOK, S.PEOPLE, S.CINE, S.AVOID
PLACES, SOUND = S.PLACES, S.SOUND
SHORT = {"OngThinh": "a 76-year-old Vietnamese grandfather", "BaMan": "a 72-year-old Vietnamese grandmother",
         "Dat": "a 25-year-old Vietnamese man with a smooth, scar-free chin",
         "Minh": "a 28-year-old Vietnamese man with a small pale scar on the left of his chin",
         "BaThoa": "a 70-year-old Vietnamese woman", "BoMinh": "a 45-year-old Vietnamese man"}
# OT5, MI0 là bản hồi tưởng: mô tả riêng
LOOK["OT5"]["outfit"] = "a white cotton singlet under an open khaki shirt, trousers rolled to the knee, bare feet; about 56 years old, hair still mostly black"
LOOK["MI0"]["outfit"] = "a faded blue T-shirt and shorts, bare feet, a small white gauze patch on the left of his chin; he is 8 years old"

P = PLACES
P["SAN_DEM_RAO"] = ("The low brick wall between two village courtyards at night: on the near side the warm glow of a wood fire under a big pot, "
                    "beyond the wall the neighbour's dark garden and a banana tree; deep blue night.")
P["BEPNH_CUA"] = ("The back door of a big city restaurant kitchen late at night: a narrow service alley, crates of vegetables, a steel door propped open "
                  "spilling cold fluorescent light, steam drifting out; cold steely light.")
P["NGHIATRANG"] = ("A small village cemetery in the middle of harvested rice fields in the Northern Vietnamese countryside: weathered whitewashed tombs "
                   "with ceramic incense bowls, joss sticks smoking, winter rice stubble, a pale grey-gold afternoon sky.")
P["NGHIATRANG_HH"] = P["NGHIATRANG"].replace("a pale grey-gold afternoon sky", "the low orange sun of the last sunset of the lunar year, long shadows")
P["BORUONG_HH"] = ("A narrow raised earthen path between harvested rice fields at sunset on New Year's Eve, a distant village of tile roofs and bamboo, "
                   "a deep orange sky.")
P["RUONG_XUA"] = ("The same narrow earthen path between rice fields twenty years ago in summer: lush green rice, a pomelo tree near a village, "
                  "warm golden nostalgic light, slightly faded colours like an old memory.")
P["MAM"] = ("The central room of the old village house: a low wooden table set for a family meal (rice, boiled chicken, pickled onions, a plate of "
            "peanut brittle), a dark wooden ancestral altar in the background, a tiny child-sized wooden chair standing empty beside the table, "
            "soft morning light through open wooden doors.")
P["AO"] = ("Behind the village house: a small fish pond with water spinach, a banana tree, a brick path, a low brick wall to the neighbour's "
           "garden; hazy midday winter light.")
P["SAN_XOM"] = P["SAN"][:-1] + "; a crowd of village neighbours bunched at the gate and along the wall, all soft and out of focus."
P["GIANTHO"] = ("The ancestral altar room of the old house: a dark lacquered altar with a framed portrait photo of a kind 45-year-old man, "
                "incense smoke rising straight up, a tray of five fruits, red candles; dim warm late-afternoon light.")
P["GACXEP_NGAY"] = P["GACXEP"].replace("at night", "in the late afternoon").replace("a tiny window with cold moonlight", "a dusty beam of afternoon light from a tiny window").replace("; warm glow from a small oil lamp", "")
P["CONG_CHIEU"] = ("The old arched brick gate of the village house in the late afternoon of New Year's Eve, red paper lanterns, and just inside the gate "
                   "a small worn wooden chair where someone sits every night, a walking stick leaning against it.")
P["BENXE_DEM"] = ("A small district bus station late on New Year's Eve: almost empty, one dark parked coach, a single fluorescent tube, red lanterns "
                  "swaying, scraps of red paper on the ground; cold blue night.")
P["CONG_GIAOTHUA"] = ("The narrow brick lane and arched gate of the village house at midnight on New Year's Eve: red lanterns glowing, distant "
                      "fireworks blooming in the sky, light smoke in the air.")
P["HIEN_DEM"] = P["HIEN"].replace("soft hazy morning sunlight", "midnight, warm lamp light from inside, distant fireworks lighting the sky")
P["MAM_GIAOTHUA"] = ("The central room at midnight on New Year's Eve: a low table with perfectly square sticky-rice cakes, boiled chicken, sticky rice, "
                     "a crooked scrawny peach-blossom branch in a vase, two wooden chairs at the table (one tiny child-sized, one brand-new), red "
                     "candles on the altar, fireworks flickering through the open doors.")
P["CONG_MUNG1"] = ("The arched brick gate of the village house on the bright morning of Lunar New Year's Day: red lanterns, red festive scrolls with "
                   "no readable writing, pink peach blossoms, firecracker paper on the bricks, soft golden sunlight.")
SD = SOUND
SD["SAN_DEM_RAO"] = "crackling wood fire, crickets, a dog far away"
SD["BEPNH_CUA"] = "an extractor fan humming, distant pans clattering, city traffic far off"
SD["NGHIATRANG"] = "wind over the fields, a bird calling, joss sticks hissing faintly"
SD["NGHIATRANG_HH"] = SD["NGHIATRANG"]
SD["BORUONG_HH"] = "wind over the fields, footsteps on dry earth, distant firecrackers"
SD["RUONG_XUA"] = "summer cicadas, a child's sniffle, hurried footsteps"
SD["MAM"] = "chopsticks on bowls, a rooster outside, a kettle"
SD["AO"] = "ducks on the pond, banana leaves rustling"
SD["SAN_XOM"] = "a murmuring crowd of neighbours, a baby crying far off"
SD["GIANTHO"] = "near silence, incense crackling, a clock ticking"
SD["GACXEP_NGAY"] = "roof tiles creaking, dust settling, a distant rooster"
SD["CONG_CHIEU"] = "wind chimes, a distant loudspeaker playing festive announcements"
SD["BENXE_DEM"] = "the fluorescent tube buzzing, distant firecrackers, cold wind"
SD["CONG_GIAOTHUA"] = "distant fireworks popping, a motorbike engine idling"
SD["HIEN_DEM"] = SD["CONG_GIAOTHUA"]
SD["MAM_GIAOTHUA"] = "distant fireworks, laughter, chopsticks"
SD["CONG_MUNG1"] = "birds, distant festive drums, children laughing far away"

OT, OT2, OT3, OT4, OT5 = "OT1", "OT2", "OT3", "OT4", "OT5"
BM2, BM3, DA2, DA3, DA4 = "BM2", "BM3", "DA2", "DA3", "DA4"
MI0, MI1, MI2, MI3, BT, BT2, BOM = "MI0", "MI1", "MI2", "MI3", "BT1", "BT2", "BOM"
X = "X"   # người không gắn nhân vật (đồng nghiệp, hàng xóm)

# (mã, tên, giây, bối cảnh, [bộ đồ], máy quay, hành động, [(bộ đồ hoặc X, câu)], âm thanh thêm)
SCENES = {
"07": ("Đêm canh nồi bánh · bếp lửa ngoài sân, đêm 27 Tết", [
 ("07-01", "Lửa củi, nồi bánh sôi", 4, "BEPLUA", [], "low macro insert at the fire, locked off", "Flames lick the blackened pot; water bubbles over the lid edge; sparks drift up into the dark", [], ""),
 ("07-02", "Hai ông cháu bên lửa", 5, "BEPLUA", [OT3, DA2], "35mm wide two-shot across the fire, slow push-in", "OngThinh and Dat sit on two low stools by the fire, firelight on their faces, silent", [], ""),
 ("07-03", "Mười năm trước", 6, "BEPLUA", [OT3], "85mm close-up, firelight, locked off", "OngThinh stares into the fire and speaks slowly", [(OT3, "Mười năm trước, đám ma bố nó. Ông cãi nhau với mẹ nó.")], ""),
 ("07-04", "Đi rồi thì đừng về", 5, "BEPLUA", [OT3], "85mm close-up, very slow push-in", "OngThinh's jaw tightens as he repeats his own old words", [(OT3, "Ông bảo nó: đi rồi thì đừng về.")], ""),
 ("07-05", "Nó nghe thật", 5, "BEPLUA", [OT3], "85mm close-up, locked off", "OngThinh pokes the fire with a stick; his voice cracks slightly", [(OT3, "Ông nói câu đấy. Nó nghe thật.")], ""),
 ("07-06", "Đạt nhìn ông", 3, "BEPLUA", [DA2], "85mm close-up, locked off", "Dat watches the old man, his playful mask slipping", [], ""),
 ("07-07", "Ông có giận cháu không", 4, "BEPLUA", [DA2], "65mm close-up, locked off", "Dat asks quietly, half in role, half himself", [(DA2, "Ông… ông có giận cháu không?")], ""),
 ("07-08", "Ông giận ông", 5, "BEPLUA", [OT3, DA2], "50mm two-shot across the fire, locked off", "OngThinh keeps his eyes on the fire as he answers; Dat turns toward him", [(OT3, "Ông không giận cháu. Ông giận ông.")], ""),
 ("07-09", "Đạt khóc thật", 4, "BEPLUA", [DA2], "85mm close-up, locked off", "Tears run down Dat's face; he wipes them roughly with his oversized sleeve and looks away", [], ""),
 ("07-10", "Màn hình sáng sau rào", 3, "SAN_DEM_RAO", [BT], "long-lens 100mm shot through dark banana leaves beyond the wall, locked off", "In the dark garden behind the wall, BaThoa's face is lit only by her phone screen, silently filming", [], ""),
]),
"08": ("Hai triệu người xem · bếp nhà hàng, rạng sáng 28 Tết", [
 ("08-01", "Chảo lửa bùng", 4, "BEPNH", [MI1], "50mm medium shot, slight handheld", "A wok flares with a burst of flame; Minh tosses it with a flat, expressionless face", [], "a wok flame roars"),
 ("08-02", "Mùng hai bay rồi", 5, "BEPNH", [MI1], "50mm medium shot, an unnamed coworker in chef whites soft in the foreground, back to camera", "A coworker leans in and jokes; Minh answers without looking up from the wok", [(X, "Mùng hai bay rồi mà vẫn đứng bếp à?"), (MI1, "Không có ai để chào.")], ""),
 ("08-03", "Giờ nghỉ cửa sau", 4, "BEPNH_CUA", [MI1], "35mm medium-wide, locked off", "Minh sits on an upturned crate at the back door, cap off, drinking water, exhausted", [], ""),
 ("08-04", "Hai triệu view", 6, "BEPNH_CUA", [MI1], "50mm two-shot, an unnamed coworker beside him seen only from behind, holding out a phone", "The coworker shows Minh a phone with a glowing screen; Minh glances at it", [(X, "Ông cụ khóc bên nồi bánh chưng với cháu đích tôn, hai triệu view rồi. Sao giống ông mày kể thế?")], ""),
 ("08-05", "Ánh màn hình trên mặt", 4, "BEPNH_CUA", [MI1], "85mm close-up, slow push-in", "Minh takes the phone; the screen glow lights his face; his eyes harden", [], ""),
 ("08-06", "Thằng đấy là ai", 4, "BEPNH_CUA", [MI1], "85mm close-up, locked off", "Minh stares at the screen and speaks very quietly", [(MI1, "Thằng đấy… là ai?")], ""),
 ("08-07", "Cởi tạp dề", 3, "BEPNH_CUA", [MI1], "50mm medium shot, locked off", "Minh stands, pulls off his apron in one motion and tosses it on the crate", [], ""),
]),
"09": ("Tảo mộ · nghĩa trang giữa đồng, chiều 28 Tết", [
 ("09-01", "Khói hương ngang ruộng", 4, "NGHIATRANG", [], "wide establishing shot, slow drift", "Thin incense smoke drifts sideways across the stubble fields between the tombs", [], ""),
 ("09-02", "Đạt trước mộ", 4, "NGHIATRANG", [DA2], "35mm medium-wide from behind, locked off", "Dat stands alone before a whitewashed tomb with a small oval portrait photo of a man, holding three lit incense sticks", [], ""),
 ("09-03", "Cháu mượn tên", 7, "NGHIATRANG", [DA2], "65mm close-up, locked off", "Dat bows his head over the incense and whispers sincerely to the grave", [(DA2, "Cháu xin lỗi chú. Mấy hôm nay cháu ở nhà chú. Cháu sẽ tử tế.")], ""),
 ("09-04", "Ông đứng sau lưng", 4, "NGHIATRANG", [OT2], "85mm, Dat soft in the foreground, OngThinh sharp a few steps behind, locked off", "OngThinh stands behind Dat with his stick, having heard everything, face unreadable", [], ""),
 ("09-05", "Bàn tay trên vai", 4, "NGHIATRANG", [OT2, DA2], "50mm two-shot, locked off", "OngThinh steps forward and silently rests his hand on Dat's shoulder", [], ""),
 ("09-06", "Đạt quay lại", 3, "NGHIATRANG", [DA2], "85mm close-up, locked off", "Dat turns his head, startled, searching the old man's face", [], ""),
]),
"10": ("Lý do thật của bà · bếp tối 28 Tết; đầu làng đêm", [
 ("10-01", "Đạt xách ba lô", 6, "BEP", [DA3], "50mm medium shot, locked off", "Dat stands in the kitchen doorway with his backpack on, voice tight", [(DA3, "Bà ơi, cháu không giấu được nữa. Cháu xin lỗi bà, cháu sẽ làm lụng trả lại.")], ""),
 ("10-02", "Bà giữ tay", 4, "BEP", [BM2, DA3], "50mm two-shot, locked off", "BaMan drops her ladle and grabs Dat's wrist with both hands", [], ""),
 ("10-03", "Đêm nào ông cũng ra cổng", 7, "BEP", [BM2], "85mm close-up, locked off", "BaMan speaks through tears, still holding his wrist", [(BM2, "Năm ngoái ông tai biến. Bác sĩ dặn đừng để ông buồn. Mà đêm nào ông cũng ra cổng ngồi.")], ""),
 ("10-04", "Mười năm không hồi âm", 6, "BEP", [BM2], "85mm close-up, slow push-in", "BaMan lifts her old phone and looks at it", [(BM2, "Bà nhắn cho thằng Minh mười năm, không một lần nó trả lời.")], ""),
 ("10-05", "Tết cuối", 4, "BEP", [BM2], "85mm close-up, locked off", "BaMan's voice drops to a whisper", [(BM2, "Bà sợ Tết này là Tết cuối của ông.")], ""),
 ("10-06", "Đặt ba lô xuống", 3, "BEP", [DA3], "50mm medium shot, locked off", "Dat slowly slips the backpack off his shoulder and sets it on the floor", [], ""),
 ("10-07", "Xe khách đầu làng", 4, "DAULANG", [], "wide shot, locked off", "A coach pulls up under the banyan tree at the village entrance in the dark, headlights cutting the mist", [], "air brakes hiss"),
 ("10-08", "Đôi giày bước xuống", 3, "DAULANG", [MI2], "low shot at road level, locked off", "Black leather boots step down onto the road; a backpack strap swings; his face is never seen", [], ""),
]),
"11": ("Hai thằng Minh · cổng nhà, sáng 29 Tết (góc khác cảnh 00)", [
 ("11-01", "Treo đèn lồng", 4, "CONG", [DA3], "35mm medium shot from inside the courtyard, locked off", "Dat stands on tiptoe on a bamboo ladder, humming, hanging a red lantern over the gate", [], ""),
 ("11-02", "Cổng mở", 4, "CONG", [MI2, DA3], "35mm wide from inside the courtyard, slow push-in", "The gate swings open; Minh stands in it with his backpack; Dat freezes on the ladder", [], "the gate hinge creaks"),
 ("11-03", "Đứa nào cháu thật", 3, "SAN_THOA", [BT], "50mm medium close-up over the wall, quick push-in", "BaThoa pops up over the wall with her phone raised, gasping", [(BT, "Thế đứa nào là cháu thật?")], ""),
 ("11-04", "Anh shipper", 4, "CONG", [DA3], "65mm close-up, locked off", "Dat forces a bright smile down at the stranger", [(DA3, "Anh… anh là shipper giao đào phải không ạ?")], ""),
 ("11-05", "Tôi là cháu nhà này", 3, "CONG", [MI2], "85mm close-up, locked off", "Minh answers flatly, eyes on Dat", [(MI2, "Tôi là cháu nhà này.")], ""),
 ("11-06", "Rơi rổ bánh", 3, "SAN", [BM2], "50mm medium shot, locked off", "BaMan, coming out with a basket of cakes, drops it; cakes tumble onto the bricks", [], "a basket thuds"),
 ("11-07", "Vết sẹo", 2, "CONG", [MI2], "macro insert on Minh's chin, shallow focus", "A small pale scar on the left of Minh's chin, catching the morning light", [], ""),
 ("11-08", "Minh vào ăn sáng", 4, "HIEN", [OT2], "50mm medium shot, locked off", "OngThinh steps onto the veranda with his stick, looks from one young man to the other, then turns warmly toward camera-left", [(OT2, "Minh, vào ăn sáng con.")], ""),
 ("11-09", "Minh chết lặng", 3, "CONG", [MI2], "85mm close-up, locked off", "Minh stands frozen in the gateway, breath misting", [], ""),
]),
"12": ("Bữa sáng của anh shipper · mâm cơm, bếp, sáng 29 Tết", [
 ("12-01", "Mâm cơm bốn người", 5, "MAM", [OT2, DA3], "35mm wide, slow push-in, a third guest's shoulder soft at the edge of frame", "OngThinh eats calmly; Dat sits stiffly beside him; awkward silence", [], ""),
 ("12-02", "Ghế bé để trống", 3, "MAM", [], "macro insert, shallow focus", "The tiny empty child-sized wooden chair beside the table", [], ""),
 ("12-03", "Cháu nội dị ứng lạc", 4, "MAM", [MI2], "65mm close-up, locked off", "Minh puts down his chopsticks and asks evenly", [(MI2, "Cháu nghe nói cháu nội ông dị ứng lạc?")], ""),
 ("12-04", "Khỏi rồi", 3, "MAM", [OT2], "85mm close-up, locked off", "OngThinh answers without looking up", [(OT2, "Ừ. Khỏi rồi.")], ""),
 ("12-05", "Minh ăn lạc", 4, "MAM", [MI2], "50mm medium close-up, locked off", "Minh deliberately takes a piece of peanut brittle and eats it, staring at the old man", [], ""),
 ("12-06", "Cổ tay nổi mẩn", 3, "MAM", [MI2], "macro insert, shallow focus", "Small red blotches rise on Minh's wrist", [], ""),
 ("12-07", "Ông quay đi", 3, "MAM", [OT2], "85mm close-up, locked off", "OngThinh's eyes flick to the wrist, then he turns his face away", [], ""),
 ("12-08", "Bà ôm cháu trong bếp", 5, "BEP", [BM2, MI2], "50mm two-shot, locked off", "In the smoky kitchen BaMan hugs Minh tightly, crying without a sound", [], ""),
 ("12-09", "Đổi số năm thứ hai", 4, "BEP", [MI2], "65mm close-up, locked off", "Minh speaks softly over her shoulder", [(MI2, "Con đổi số từ năm thứ hai, bà ạ.")], ""),
 ("12-10", "Mười năm tin nhắn", 4, "BEP", [BM2], "85mm close-up, locked off", "BaMan looks down at her old phone, its glowing screen unreadable, realisation dawning", [], ""),
 ("12-11", "Không muốn nhận", 5, "BEP", [MI2], "85mm close-up, slow push-in", "Minh asks the question that hurts", [(MI2, "Ông không nhận ra con, hay ông không muốn nhận?")], ""),
 ("12-12", "Ông lẫn rồi", 3, "BEP", [BM2], "85mm close-up, locked off", "BaMan shakes her head sadly", [(BM2, "Ông lẫn rồi con ạ.")], ""),
]),
"13": ("Ba mươi triệu · sau nhà, bờ ao, trưa 29 Tết", [
 ("13-01", "Túm cổ áo", 4, "AO", [MI2, DA3], "50mm two-shot, slight handheld", "Minh grabs Dat by the collar of his red jacket, then lets go immediately; no blows", [(MI2, "Bao nhiêu tiền?")], ""),
 ("13-02", "Đền ba mươi", 4, "AO", [DA3], "65mm close-up, locked off", "Dat straightens his collar and answers honestly", [(DA3, "Mười lăm triệu. Hợp đồng ghi rõ.")], ""),
 ("13-03", "Tôi trả ba mươi", 5, "AO", [MI2], "65mm close-up, locked off", "Minh pulls out his phone and holds it out, screen glowing", [(MI2, "Tôi trả ba mươi. Đủ đền. Đi đi.")], ""),
 ("13-04", "Đạt nhìn màn hình", 4, "AO", [DA3], "85mm close-up, locked off", "Dat stares at the glowing phone for a long moment, tempted, then slowly puts his hands in his pockets", [], ""),
 ("13-05", "Thế anh khác gì em", 7, "AO", [DA3], "85mm close-up, slow push-in", "Dat looks up at Minh, quiet and steady", [(DA3, "Anh vắng mười năm, giờ trả tiền để ông có cháu à? Thế anh khác gì em?")], ""),
 ("13-06", "Hai người đứng thở", 4, "AO", [MI2, DA3], "35mm wide two-shot by the pond, locked off", "The two young men stand facing each other, breathing hard, neither moving", [], ""),
 ("13-07", "Cháu thuê", 3, "SAN_THOA", [BT], "long-lens shot over the wall through banana leaves, locked off", "BaThoa clutches her phone to her chest, eyes shining with gossip", [(BT, "Cháu thuê!")], ""),
]),
"14": ("Livestream bóc phốt · sân nhà, chiều 29 Tết", [
 ("14-01", "Bóc phốt giữa sân", 6, "SAN_XOM", [BT], "50mm medium shot, slow push-in", "BaThoa stands in the middle of the courtyard announcing into her phone on its selfie stick", [(BT, "Các cháu ơi, cháu đích tôn nhà ông Thịnh là cháu thuê!")], ""),
 ("14-02", "Xóm kéo đến", 4, "SAN_XOM", [], "wide shot from the veranda, locked off", "Neighbours crowd the gate and wall, whispering; one elderly neighbour shakes his head", [(X, "Tội ông, lẫn rồi nên bị lừa.")], ""),
 ("14-03", "Cháu lừa ông bà", 5, "SAN_XOM", [DA3], "65mm close-up, locked off", "Dat steps forward in front of everyone, head high", [(DA3, "Cháu lừa ông bà. Ông bà không biết gì.")], ""),
 ("14-04", "Minh im lặng", 3, "SAN_XOM", [MI2], "85mm close-up, locked off", "Minh stands to the side, jaw clenched, silent", [], ""),
 ("14-05", "Ông chống gậy ra sân", 4, "SAN_XOM", [OT2], "35mm medium-wide, slow push-in", "OngThinh walks slowly out to the middle of the courtyard with his stick; the crowd hushes", [], "the stick taps on bricks"),
 ("14-06", "Tôi quên tắt bếp", 6, "SAN_XOM", [OT2], "65mm close-up, locked off", "OngThinh speaks to the crowd, calm and dry", [(OT2, "Tôi quên tắt bếp. Tôi quên cả tên bà nhà tôi.")], ""),
 ("14-07", "Cái sẹo cây bưởi", 7, "SAN_XOM", [OT2], "85mm close-up, very slow push-in", "OngThinh's eyes go to Minh as he speaks", [(OT2, "Nhưng thằng cháu tôi có cái sẹo ở cằm, ngã cây bưởi năm tám tuổi, chính tôi cõng nó đi khâu.")], ""),
 ("14-08", "Cằm nhẵn thín", 3, "SAN_XOM", [OT2, DA3], "50mm two-shot, locked off", "OngThinh lifts his chin toward Dat", [(OT2, "Còn cậu này, cằm nhẵn thín.")], ""),
 ("14-09", "Biết từ lúc qua cổng", 5, "SAN_XOM", [OT2], "85mm close-up, locked off", "OngThinh says the last line slowly, looking straight ahead", [(OT2, "Tôi biết từ lúc nó bước qua cổng.")], ""),
]),
"15": ("Bà khoe cháu đi Nhật · sân nhà, tiếp liền", [
 ("15-01", "Cả xóm im lặng", 3, "SAN_XOM", [], "wide shot, locked off", "The whole crowd stands frozen in silence", [], "total silence except wind"),
 ("15-02", "Ông biết mà ông vẫn", 5, "SAN", [BM2], "65mm close-up, locked off", "BaMan sinks down onto the veranda step, staring at her husband", [(BM2, "Thế… ông biết mà ông vẫn…")], ""),
 ("15-03", "Cháu đi Nhật", 6, "SAN_XOM", [OT2], "65mm close-up, locked off", "OngThinh turns to BaThoa", [(OT2, "Bà khoe cháu đi Nhật năm năm nay, nó gọi về được mấy lần?")], ""),
 ("15-04", "Tay bà Thoa run", 3, "SAN_XOM", [BT], "macro insert, shallow focus", "BaThoa's hand trembles on the selfie stick; her thumb taps the phone screen off", [], ""),
 ("15-05", "Có người nghe tôi nói", 6, "SAN_XOM", [BT], "85mm close-up, locked off", "BaThoa speaks quietly for the first time, eyes lowered", [(BT, "Nó đổi số rồi. Tôi live… là để có người nghe tôi nói.")], ""),
 ("15-06", "Nó ngồi canh nồi bánh", 7, "SAN_XOM", [OT2], "85mm close-up, slow push-in", "OngThinh speaks softly, then his voice catches", [(OT2, "Tôi biết nó giả. Nhưng nó ngồi canh nồi bánh với tôi. Còn thằng thật thì mười năm…")], ""),
 ("15-07", "Ông nhìn Minh", 3, "SAN_XOM", [OT2, MI2], "over-the-shoulder 50mm from behind OngThinh onto Minh, locked off", "For the first time OngThinh looks straight at Minh", [], ""),
 ("15-08", "Ông bảo con đừng về", 4, "SAN_XOM", [MI2], "85mm close-up, slight handheld", "Minh explodes, voice breaking", [(MI2, "Ông bảo con đừng về cơ mà!")], ""),
]),
"16": ("Đêm hai mươi chín năm ấy · gian thờ, cổng, chiều 29 Tết", [
 ("16-01", "Di ảnh, khói hương", 4, "GIANTHO", [], "slow push-in on the altar", "The framed portrait of the kind 45-year-old man on the altar, incense smoke rising straight", [], ""),
 ("16-02", "Đám tang năm ấy", 6, "GIANTHO", [MI2], "65mm close-up, locked off", "Minh stands before the altar, speaking to the old man behind him without turning", [(MI2, "Con mười tám tuổi, đứng ở đám tang bố, nghe ông nói câu ấy.")], ""),
 ("16-03", "Con về một lần rồi", 7, "GIANTHO", [MI2], "85mm close-up, slow push-in", "Minh turns around, eyes wet", [(MI2, "Con về một lần rồi. Năm năm trước, đêm hai mươi chín. Con đứng ở cổng, thấy ông ngồi đấy.")], ""),
 ("16-04", "Ông đứng dậy đi vào", 5, "GIANTHO", [MI2], "85mm close-up, locked off", "Minh's voice drops", [(MI2, "Ông nhìn con… rồi ông đứng dậy đi vào.")], ""),
 ("16-05", "Ông sững người", 4, "GIANTHO", [OT2], "85mm close-up, very slow push-in", "OngThinh is stunned; his lips part but no words come", [], ""),
 ("16-06", "Mùng hai con bay", 5, "GIANTHO", [MI2], "65mm close-up, locked off", "Minh steadies himself", [(MI2, "Mùng hai con bay. Con về để chào ông.")], ""),
 ("16-07", "Thế thì chào đi", 4, "GIANTHO", [OT2], "50mm medium shot, locked off", "OngThinh turns his back to Minh, pride locking his throat", [(OT2, "Thế thì chào đi.")], ""),
 ("16-08", "Xách ba lô ra cổng", 4, "CONG", [MI2], "35mm from behind, slow follow", "Minh shoulders his backpack and strides toward the gate", [], ""),
 ("16-09", "Đạt chặn cổng", 6, "CONG", [DA3, MI2], "50mm two-shot, locked off", "Dat steps into the gateway, blocking Minh's way", [(DA3, "Anh có biết đêm nào ông cũng ngồi ở cái cổng này không?")], ""),
]),
"17": ("Cái tủ gỗ · gác xép, cổng, chiều 30 Tết", [
 ("17-01", "Chìa khóa", 5, "GACXEP_NGAY", [BM2, DA3], "50mm two-shot, locked off", "BaMan presses an old iron key into Dat's palm", [(BM2, "Cháu mở đi. Điều thứ ba bà bỏ.")], ""),
 ("17-02", "Ổ khóa bật", 3, "GACXEP_NGAY", [DA3], "macro insert, shallow focus", "The rusty padlock clicks open in Dat's hands; the cabinet doors creak", [], "a padlock clicks"),
 ("17-03", "Mười phong bao", 4, "GACXEP_NGAY", [], "macro insert, slow slide", "Inside the cabinet: ten red lucky-money envelopes stacked neatly, no readable writing", [], ""),
 ("17-04", "Mười tấm vé xe", 4, "GACXEP_NGAY", [], "macro insert, slow slide", "Beside them a bundle of ten old coach tickets tied with string, no readable writing", [], ""),
 ("17-05", "Năm nào cũng mua vé", 6, "GACXEP_NGAY", [BM2], "85mm close-up, locked off", "BaMan touches the tickets", [(BM2, "Năm nào ông cũng mua vé. Ra đến bến lại quay về.")], ""),
 ("17-06", "Đứng ngoài cửa kính", 8, "GACXEP_NGAY", [BM2], "85mm close-up, very slow push-in", "BaMan looks at Minh as she speaks", [(BM2, "Chỉ có một năm ông lên đến tận nơi. Đứng ngoài cửa kính nhìn con nấu bếp. Về bảo tôi: nó mặc áo trắng, đẹp như bố nó.")], ""),
 ("17-07", "Tấm vé bấm lỗ", 4, "GACXEP_NGAY", [MI2], "macro insert on Minh's hands, shallow focus", "Minh turns over one ticket: it has a punched hole; the others are untouched", [], ""),
 ("17-08", "Cùng năm ấy", 5, "GACXEP_NGAY", [MI2], "85mm close-up, locked off", "Minh whispers, realising", [(MI2, "Năm năm trước… Cùng năm ấy con cũng về.")], ""),
 ("17-09", "Minh vỡ òa", 4, "GACXEP_NGAY", [MI2], "50mm medium shot, locked off", "Minh clutches the bundle of tickets to his chest and breaks down crying", [], ""),
 ("17-10", "Ông đâu", 3, "SAN", [BM2], "35mm medium shot, slight handheld", "BaMan hurries down into the courtyard, looking around", [(BM2, "Ông đâu?")], ""),
 ("17-11", "Ghế ở cổng trống", 4, "CONG_CHIEU", [], "35mm wide, locked off", "The small worn chair by the gate stands empty, the walking stick leaning against it", [], ""),
]),
"18": ("Ông nói với con trai · nghĩa trang, bờ ruộng, hoàng hôn tất niên", [
 ("18-01", "Chạy dọc bờ ruộng", 5, "BORUONG_HH", [MI2], "35mm tracking shot beside him", "Minh runs along the earthen path between the fields, coat flapping", [], ""),
 ("18-02", "Ông ngồi trước mộ", 5, "NGHIATRANG_HH", [OT3], "wide shot, locked off", "In the distance OngThinh sits alone on the ground before his son's tomb, no walking stick", [], ""),
 ("18-03", "Tao không biết nói", 8, "NGHIATRANG_HH", [OT3], "85mm close-up, locked off", "OngThinh talks to the gravestone with the small portrait", [(OT3, "Thằng Minh về rồi. Tao không biết nói với nó thế nào.")], ""),
 ("18-04", "Mười năm tập một câu", 7, "NGHIATRANG_HH", [OT3], "85mm close-up, very slow push-in", "OngThinh's voice shakes", [(OT3, "Mười năm tao tập mỗi một câu mà đến lúc gặp thì không nói được.")], ""),
 ("18-05", "Minh đứng sau lưng", 3, "NGHIATRANG_HH", [MI2], "85mm, OngThinh's back soft in the foreground, Minh sharp behind, locked off", "Minh stands a few steps behind, having heard everything", [], ""),
 ("18-06", "Ngồi xuống cạnh ông", 4, "NGHIATRANG_HH", [MI2, OT3], "35mm two-shot, locked off", "Minh sits down on the ground beside his grandfather; neither looks at the other", [], ""),
 ("18-07", "Sẹo còn không", 4, "NGHIATRANG_HH", [OT3], "85mm close-up, locked off", "OngThinh asks without turning his head", [(OT3, "Sẹo còn không?")], ""),
 ("18-08", "Ông chạm vào sẹo", 4, "NGHIATRANG_HH", [OT3, MI2], "65mm two-shot, locked off", "Minh tilts his chin; OngThinh's knotted fingers touch the small scar", [], ""),
 ("18-09", "Chớp lui: cõng cháu", 5, "RUONG_XUA", [OT5, MI0], "35mm tracking shot, warm faded memory look", "Twenty years earlier, a younger OngThinh runs along the field path carrying a crying 8-year-old boy on his back, a gauze patch on the boy's chin", [], ""),
 ("18-10", "Ông xin lỗi", 5, "NGHIATRANG_HH", [OT3, MI2], "50mm two-shot, locked off", "OngThinh finally says it; Minh answers gently", [(OT3, "Ông xin lỗi."), (MI2, "Con về rồi mà ông.")], ""),
 ("18-11", "Cõng ông qua bờ ruộng", 6, "BORUONG_HH", [MI2, OT3], "wide shot from behind, slow follow", "Minh carries his grandfather on his back along the field path toward the village, against the orange sky", [], ""),
 ("18-12", "Áo len của bố", 4, "BEP", [BM2, MI3], "50mm two-shot, locked off", "BaMan hands Minh an old cream cable-knit sweater; Minh, now wearing it, holds the sleeve to his face", [], ""),
 ("18-13", "Đạt khép cổng", 4, "CONG_CHIEU", [DA3], "35mm from inside the courtyard, locked off", "At dusk Dat, backpack on, quietly pulls the gate closed behind him without a word", [], "the gate latch clicks"),
]),
"19": ("Phong bao thứ mười một · bến xe huyện, sát giao thừa", [
 ("19-01", "Bến xe vắng", 4, "BENXE_DEM", [DA3], "wide shot, locked off", "Dat sits alone on a bench in the empty station, backpack at his feet", [], ""),
 ("19-02", "Gọi về mái ấm", 5, "BENXE_DEM", [DA3], "65mm close-up, locked off", "Dat smiles bravely into his phone", [(DA3, "Các em ăn Tết vui không cô?")], ""),
 ("19-03", "Xe máy phóng đến", 4, "BENXE_DEM", [MI3], "35mm wide, locked off", "A motorbike swerves into the station; Minh in a helmet and the cream sweater brakes hard", [], "a motorbike engine"),
 ("19-04", "Phong bao thứ mười một", 5, "BENXE_DEM", [MI3, DA3], "50mm two-shot, locked off", "Minh holds out a brand-new red lucky-money envelope to Dat", [], ""),
 ("19-05", "Ông chỉ có cháu", 8, "BENXE_DEM", [MI3], "65mm close-up, slow push-in", "Minh delivers his grandfather's message", [(MI3, "Ông bảo hợp đồng hết hạn rồi. Nhưng ông chưa ký hợp đồng nào cả. Ông chỉ có cháu.")], ""),
 ("19-06", "Bà Thoa mở hộp", 4, "BENXE_DEM", [BT2], "50mm medium shot, locked off", "BaThoa, just off a motorbike taxi, opens a big cardboard box", [], ""),
 ("19-07", "Chiếc ghế thứ hai", 6, "BENXE_DEM", [BT2], "65mm close-up, locked off", "Inside the box a new small wooden chair, wood shavings still on it; BaThoa speaks warmly", [(BT2, "Ông đóng bốn đêm. Ông bảo đóng cho thằng cháu chưa từng có ghế.")], ""),
 ("19-08", "Còn mười phút", 4, "BENXE_DEM", [DA3], "85mm close-up, locked off", "Dat glances at the station clock with no readable numbers, tears in his eyes", [(DA3, "Không kịp đâu.")], ""),
 ("19-09", "Minh nổ máy", 3, "BENXE_DEM", [MI3, DA3], "50mm two-shot, locked off", "Minh revs the engine and tosses Dat a spare helmet; Dat catches it", [], "an engine revs"),
]),
"20": ("Xông đất · giao thừa → sáng mùng 1", [
 ("20-01", "Pháo hoa xa", 4, "HIEN_DEM", [OT4, BM3], "35mm two-shot, locked off", "OngThinh and BaMan stand on the veranda in their festive clothes, fireworks blooming far away", [], ""),
 ("20-02", "Xe dừng đầu ngõ", 3, "CONG_GIAOTHUA", [MI3, DA3], "wide shot down the lane, locked off", "A motorbike stops at the end of the lane just as the fireworks peak", [], ""),
 ("20-03", "Hai đứa xông đất", 5, "HIEN_DEM", [OT4], "65mm close-up, locked off", "OngThinh calls out across the courtyard", [(OT4, "Năm nay nhà này hai đứa xông đất.")], ""),
 ("20-04", "Bước qua cổng", 4, "CONG_GIAOTHUA", [MI3, DA3], "35mm from inside the courtyard, slow push-in", "Minh and Dat step through the gate together, side by side", [], ""),
 ("20-05", "Mâm cơm giao thừa", 5, "MAM_GIAOTHUA", [OT4, BM3], "35mm wide, slow crane down", "The New Year's Eve table: square cakes, the crooked peach branch, two chairs; the grandparents sit", [], ""),
 ("20-06", "Minh ngồi ghế bé", 4, "MAM_GIAOTHUA", [MI3], "50mm medium shot, locked off", "Minh, tall and broad, squeezes onto the tiny child-sized chair, knees up; he laughs", [], "family laughter"),
 ("20-07", "Đạt, ngồi đây con", 5, "MAM_GIAOTHUA", [OT4, DA3], "50mm two-shot, locked off", "OngThinh pats the brand-new chair and calls Dat by his real name for the first time", [(OT4, "Đạt. Ngồi đây con.")], ""),
 ("20-08", "Bà Thoa cuối mâm", 3, "MAM_GIAOTHUA", [BT2], "50mm medium shot, locked off", "BaThoa sits at the end of the table, smiling, no phone in her hands", [], ""),
 ("20-09", "Mười cái Tết", 6, "MAM_GIAOTHUA", [OT4, MI3], "65mm two-shot, locked off", "OngThinh places ten red envelopes into Minh's hands", [(OT4, "Mười cái Tết. Cầm lấy.")], ""),
 ("20-10", "Nhớ đường về", 5, "MAM_GIAOTHUA", [OT4], "85mm close-up, very slow push-in", "OngThinh looks at Minh, eyes wet, voice firm", [(OT4, "Đi đâu thì đi. Nhớ đường về.")], ""),
 ("20-11", "Ảnh mùng 1", 4, "CONG_MUNG1", [BT2], "50mm medium shot, locked off", "On New Year's morning BaThoa raises her phone to take a family photo, teasing", [(BT2, "Thế đứa nào là cháu thật?")], ""),
 ("20-12", "Cả hai", 4, "CONG_MUNG1", [OT4, DA4], "35mm wide family portrait framing, locked off", "OngThinh stands at the gate between his grandsons (Minh at the edge of frame, soft), smiles and answers", [(OT4, "Cả hai.")], ""),
]),
}


def syl(t):
    return len(re.findall(r"\w+", t))


def timings(lines, dur):
    out, t = [], 0.4
    for c, text in lines:
        rate = 3.2 if c in ("OT1", "OT2", "OT3", "OT4") else 4.3
        d = max(1.0, syl(text) / rate)
        out.append((c, text, round(t, 1), round(t + d, 1)))
        t += d + 0.4
    if out and out[-1][3] > dur - 0.3:
        print(f"  ! thoại dài hơn shot ({out[-1][3]}s > {dur}s): {lines[-1][1][:40]}")
    return out


def prompt(s):
    code, name, dur, place, looks, cam, action, lines, extra = s
    out = [f"A single continuous {dur}-second shot, 16:9, one camera angle, no cuts.", "", f"[LOOK] {CINE}", "", f"[PLACE] {PLACES[place]}", ""]
    if looks:
        out.append("[CHARACTERS] Use the attached character image for each person: same face, same hair, same outfit, exactly.")
        for c in looks:
            lk = LOOK[c]; per = lk["person"]; p = PEOPLE[per]
            desc = SHORT[per]
            if c == "OT5": desc = "the same grandfather twenty years younger"
            if c == "MI0": desc = "Minh as an 8-year-old boy"
            out.append(f"- {per} = {p['vn']}, {p['role']} ({desc}); wears {lk['outfit']}. Attached image: \"{lk['flow']}\".")
        out.append("Each named person appears exactly once. Background people stay distant, blurred and clearly different from them.")
    else:
        out.append("[CHARACTERS] No named characters; any people in frame are distant, blurred, seen only from behind or below the waist.")
    out += ["", f"[CAMERA] {cam}.", "", f"[ACTION] {action}.", ""]
    if lines:
        out.append("[DIALOGUE] In Vietnamese with exact lip-sync, standard Northern Vietnamese accent; each line spoken exactly once; only the speaker moves the lips:")
        for c, t, a, b in timings(lines, dur):
            if c == X:
                out.append(f"- {a:.1f}s–{b:.1f}s, an unnamed bystander whose face is out of focus (ordinary adult voice): {t}")
            else:
                per = LOOK[c]["person"]
                out.append(f"- {a:.1f}s–{b:.1f}s, {per} ({PEOPLE[per]['voice']}): {t}")
        out.append(f"After the last word nobody speaks until {dur:.1f}s. Never read these directions aloud.")
    else:
        out.append("[DIALOGUE] None. Every mouth stays closed; no voices at all.")
    snd = SOUND[place] + (f"; {extra}" if extra else "")
    out += ["", f"[SOUND] {snd}. No music.", "", f"[AVOID] {AVOID}", ""]
    return "\n".join(out).replace("@", "")


def main():
    only = sys.argv[1:] or list(SCENES)
    md = ["# Bản điện ảnh V3 · phần 2 (cảnh 07–20)", "",
          "*Sinh bởi `_tools/build_shots_2.py`.* Flow: Video → Thành phần, Omni 1.2 Flash, 720p, x1. Tên trên Flow: `V3-<shot> · <tên>`.", ""]
    js, tot = [], 0
    for sc, (title, shots) in SCENES.items():
        md += [f"## Cảnh {sc} · {title}", "", "| Shot | Giây | Đính | Thoại |", "|---|---|---|---|"]
        for s in shots:
            p = prompt(s)
            if sc in only:
                B.write(f"film/v3/c{sc}/{s[0]}.txt", p)
            tot += s[2]
            md.append(f"| {s[0]} · {s[1]} | {s[2]} | {', '.join(LOOK[c]['flow'] for c in s[4]) or 'Text-to-Video'} | "
                      + " / ".join(("Người ngoài" if c == X else PEOPLE[LOOK[c]['person']]['vn']) + ": " + t for c, t in s[7]) + " |")
            js.append(dict(code=s[0], name=s[1], dur=s[2], refs=[LOOK[c]["flow"] for c in s[4]], prompt=" ".join(p.split())))
        md.append("")
    n = sum(len(v[1]) for v in SCENES.values())
    md.append(f"**Tổng {n} shot, {tot} giây (~{tot * 3} credit ở 720p).**")
    B.write("film/v3/SHOTS_2.md", "\n".join(md) + "\n")
    B.write("film/v3/shots_2.json", json.dumps(js, ensure_ascii=False))
    print(n, "shot", tot, "giây")


if __name__ == "__main__":
    main()
