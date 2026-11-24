# -*- coding: utf-8 -*-
# Bản sửa v2 sau buổi duyệt "biên tập viên": ghi đè từng shot theo mã. Được data.py exec sau canh_a/b/c.
_IDX = dict(title=0, secs=1, attach=2, cam=3, act=4, lines=5, place=6, note=7)
def _fix(sid, **kw):
    num, k = sid.split("-")
    for _sc in S:
        if _sc["num"] == num:
            _sh = list(_sc["shots"][int(k) - 1])
            for _k, _v in kw.items():
                _sh[_IDX[_k]] = _v
            _sc["shots"][int(k) - 1] = tuple(_sh)
            return
    raise KeyError(sid)

FG_TEAPOT = "the soft foreground on the LEFT is the edge of the clay teapot on the low tea table"
FG_PLANT_L = "the soft foreground on the LEFT is the leaves of a potted plant"

_fix("01-07", act="The phone buzzes on the desk; @Ngan turns it over (the screen faces away from camera, only a soft glow), looks at it for a beat, then answers and lifts it to her left ear. Her face is cold and closed the whole time: no smile at any moment, lips flat, eyes hard and tired; she has just heard her husband laughing with another woman through the wall.",
     lines=[("Ngan", "Em nghe.", "flat, cold, controlled|đều, lạnh, nén")])
_fix("01-09", cam=CAM_WALL_N + "; her phone at her LEFT ear; the studio desk soft behind her",
     act="From the first frame to the last, the right side of @Ngan's head is pressed flat against the bare wall, her right ear and cheek touching the wall surface; she never moves away from the wall. Her phone is at her left ear and she asks softly into the phone. Her eyes are wet and shining but her voice stays very calm; she does not smile.")
_fix("01-14", act="At the very first frame three sharp knocks sound from the wall right behind @Hung's head; he jerks forward out of his lazy slouch in fright, eyes wide, and twists round to stare at the wall; @Diem spins round on the vanity stool, startled. He is visibly scared, not relaxed. He forces himself to answer too quickly while " + RING + ".")
_fix("02-01", act="The front door opens; @Hung, in yesterday's crumpled white shirt, steps in, pushes the door shut behind him and bends to take off his shoes by the shoe cabinet. @Ngan keeps pouring and does not look up. His hands stay away from his wrists and cuffs; his wrists are bare, with no wristwatch.")
_fix("02-02", act="@Hung hangs his keys on a hook; then " + RING + ". The ring is already on his finger when the shot begins and is still fully on it at the end.")
_fix("02-10", title="Sửa bóng đèn", secs=7,
     act="@Hung leans out past her, sees the slippers, and answers toward the boy off-screen RIGHT a little too quickly, avoiding his wife's eyes, while " + RING + ".",
     lines=[("Hung", "À… hôm trước nhà bên mới chuyển đến, nhờ bố sang sửa cái bóng đèn. Bố để quên.", "light, a little too quick|nhẹ, hơi nhanh quá")],
     note="Hưng (đã thay com-lê) ló ra sau vai vợ, bịa chuyện sang sửa bóng đèn (khớp lời Diễm ở 04-12), tay xoay nhẫn.")
_fix("04-03", cam="85mm close-up of @Ngan in the armchair, three-quarter, looking RIGHT of camera, the teacup in her hands; " + FG_TEAPOT,
     act="@Ngan turns the teacup slowly in her fingers. Her face is calm and pleasant, a hostess making small talk; only her eyes are sharp. No frown.")
_fix("04-07", cam="85mm close-up of @Ngan in the armchair, three-quarter, looking RIGHT of camera; " + FG_PLANT_L,
     act="@Ngan holds her gaze calmly; a faint sadness passes through her eyes; she does not smile.")
_fix("04-09", cam="85mm close-up of @Diem on the sofa, three-quarter, looking LEFT of camera; the soft foreground on the RIGHT is the arm of the sofa with a cushion",
     act="@Diem turns her head toward the door off-screen LEFT, then back to her host, puzzled, and asks the question clearly.")
_fix("04-10", cam="85mm close-up of @Ngan in the armchair, three-quarter, looking RIGHT of camera; " + FG_TEAPOT,
     act="@Ngan answers smoothly, without hurry, with a small easy smile.")
_fix("05-13", cam="85mm close-up of @Ngan at the head of the dinner table, three-quarter, looking LEFT of camera; the soft foreground is the rim of a soup bowl and a pair of chopsticks on the table",
     act="@Ngan says it gently, looking straight at her husband off-screen LEFT; a soft polite smile that does not reach her eyes.")
_fix("06-05", cam="85mm close-up of @Ngan as she turns off the tap and turns to face him, three-quarter, looking LEFT of camera; the soft foreground on the RIGHT is the chrome kitchen tap and the dish rack",
     act="@Ngan dries her hands slowly on a kitchen towel; her face is calm and dry, no anger.")
_fix("06-06", cam="50mm medium shot of @Hung by the dining table; the soft foreground on the RIGHT is the back of a wooden dining chair",
     act="@Hung grabs his car keys from the table, avoids her eyes, and walks out of frame to the LEFT toward the front door. His wrists are bare.")
_fix("06-09", cam="50mm two-shot: @Hung stands by the bare wall on the LEFT of frame, his jacket already off and his shirt sleeves already rolled up; @Diem sits on the edge of the bed on the RIGHT brushing her hair",
     act="@Diem asks lightly; @Hung undoes the top button of his collar with one hand and sits down on the edge of the bed beside her. He never touches his wrists or sleeves; his wrists are bare.")
_fix("07-10", cam="85mm close-up of @BaLua at her steel desk, three-quarter, looking LEFT of camera; the soft foreground on the RIGHT is the blue-and-white teapot on the desk")
_fix("07-11", cam="85mm close-up of @Ngan seated across the desk, three-quarter, looking RIGHT of camera; the soft foreground on the LEFT is a stack of paper folders on the desk")
_fix("10-06", cam="85mm close-up of @Diem on her balcony holding the fluffy snow-white cat against her chest, three-quarter, looking LEFT of camera, the partition soft on the LEFT",
     act="@Diem, cradling the fluffy snow-white cat (pure white fur, no stripes, no patches, red collar) in her left arm, notices the look and lifts her right wrist proudly, showing an old thin gold bracelet with a single small green jade bead.")
_fix("10-08", cam="85mm close-up of @Diem on her balcony, three-quarter, holding the fluffy snow-white cat",
     act="@Diem laughs and carries the fluffy snow-white cat (pure white fur, no stripes, no patches, red collar) out of frame to the RIGHT into her apartment.")
_fix("10-10", cam="85mm close-up of @Ngan sitting on the floor beside the TV cabinet, the open lacquer box in her lap; the soft foreground on the LEFT is the corner of the open cabinet drawer",
     act="@Ngan closes the box slowly; her lips press together; her eyes are wet but no tears fall.")
_fix("11-02", cam="85mm close-up of @Ngan at the dining table, three-quarter, looking LEFT of camera; the soft foreground is the edge of the stack of papers and the pen lying on the table")
_fix("11-11", act="@Bin, in a yellow T-shirt, peeks from behind the half-open door, half hidden, eyes wide with fear, holding his breath, lips pressed tight; he does not smile at any moment; at the end he slowly pulls back behind the door.")
_fix("12-05", cam="50mm medium shot of @Hung alone by the glass balcony door, his phone buzzing in his hand",
     act="@Hung glances at the phone (screen facing away), says the line in his own low male voice, slides the balcony door open and steps out of frame to the RIGHT onto the balcony. He is the only person who speaks in this shot.")
_fix("13-06", cam="85mm close-up of @BaLua at her steel desk, three-quarter, looking LEFT of camera, the blue notebook in her hands; the soft foreground on the RIGHT is the blue-and-white teapot on the desk")
_fix("13-07", cam="85mm close-up of @Ngan seated across the desk, three-quarter, looking RIGHT of camera; the soft foreground on the LEFT is a stack of paper folders on the desk")
_fix("15-06", cam="85mm close-up of @Ngan standing in her living room, three-quarter, looking RIGHT of camera; " + FG_PLANT_L + "; the dining table and the balcony door soft behind her")
_fix("15-08", cam="85mm close-up of @Ngan standing in her living room, three-quarter, looking RIGHT of camera; " + FG_PLANT_L + "; the dining table and the balcony door soft behind her",
     act="@Ngan speaks slowly, without anger, almost with pity.")
_fix("17-05", cam="85mm close-up of @Ngan in her studio, holding her phone to her LEFT ear",
     act="@Ngan, still on the phone call, keeps the phone pressed to her left ear the whole time, nods to herself and speaks into the phone.")
_fix("17-06", cam="85mm close-up of @ChiMai at her office desk, holding her phone to her ear with one hand",
     act="@ChiMai, still on the phone call, keeps the phone at her ear with one hand the whole time, closes the folder on the desk with her other hand, then speaks into the phone.")
_fix("18-10", act="@Diem slowly pulls the black face mask down off her face and lays it on the desk; she keeps the black bucket hat on her head, pulled low. Her face is pale, her jaw set. She does not speak yet.")
_fix("19-08", cam="50mm two-shot from inside the office: @BaLua on the LEFT and @Ngan on the RIGHT stand side by side at the glass front door, both in profile, looking out through the glass at the street",
     act="Both women watch the street through the glass: out on the sidewalk, small and soft in the distance, a man in a navy suit stands alone with his head down. The shop fronts across the street have plain blank signboards.")
_fix("21-11", lines=[("ChiMai", "Tiền đã đóng cho căn ấy, công ty sẽ hoàn về đúng tài khoản đã chuyển.", "businesslike|công việc")])
_fix("25-05", cam="85mm close-up of @Ngan at the studio desk, three-quarter, looking LEFT of camera toward her son; the plain black unbranded mesh pop filter soft in the RIGHT foreground",
     act="@Ngan glances at the bare wall on the RIGHT, then back at her son, with a soft, wise smile.")
_fix("25-07", cam="50mm two-shot at the bare wall on the RIGHT of frame, same framing as the previous shot: @Bin and @Ngan standing side by side right at the wall",
     act="@Bin and @Ngan stay standing side by side at the bare wall, exactly where they were. A beat of silence; then three soft knocks come back from the other side of the wall; mother and son turn to look at each other and burst out laughing. Nobody sits down.")

# v2b: 18-01 lần 2 — kính mờ phía sau vẫn hiện chữ "HÀ NỘI": đổi phông nền sau lưng thành tường trơn
_c = [_s for _sc in S if _sc["num"] == "18" for _s in [_sc["shots"][0]]][0][3]
assert "the glass door behind them" in _c
_fix("18-01", cam=_c.replace("the glass door behind them", "behind them only a plain bare pale-grey painted wall and one potted plant, no glass, no partition, nothing written anywhere"))

# v2c: 03-03 — bản cũ tự thêm một người đàn ông áo đen ở tiền cảnh: đổi sang qua vai Ngân (có ảnh sau lưng)
_fix("03-03", attach=["NG1B", "DI2"],
     cam="over-the-shoulder from just inside the family's open door: @Ngan seen only from behind (her low hair knot and charcoal knitted cardigan soft in the LEFT foreground), onto @Diem standing in the corridor in a medium close shot, the fruit basket at her chest; she looks slightly LEFT of camera at @Ngan; nobody else is in the frame")

# v2d: 04-11 lần 5 — 4 lần trước hỏng ở khâu âm thanh khi quay chính diện Bin: đổi sang qua vai Bin nhìn về Diễm
_fix("04-11", attach=["BI2B", "DI2"],
     cam="over-the-shoulder from behind @Bin (seen only from behind: his short black hair, white school shirt collar, red neckerchief knot and backpack straps soft in the LEFT foreground) onto @Diem sitting on the sofa, three-quarter, looking at the boy",
     act="@Bin, seen only from behind, tilts his head and says it innocently in his clear child's voice; @Diem's bright smile freezes for a moment and her eyes flick toward the front door.")

# ===================== v3 (duyệt lần 3: user + biên tập) =====================
AVOID = AVOID.replace("letterbox bars;", "letterbox bars; cartoon or comic graphics drawn over the picture such as motion lines, shock marks, exclamation marks or emoji; extra rings or jewellery that are not described;")
for _k in ("HU1", "HU2", "HU3"):
    _o = list(OUTFITS[_k]); _o[2] = _o[2].replace("a plain gold wedding band on his left ring finger", "exactly one ring: a single plain gold wedding band on his left ring finger, no other ring on any finger of either hand"); OUTFITS[_k] = tuple(_o)
RING1 = "with his right thumb and forefinger he twists the single plain gold wedding band round and round on his left ring finger; it is the only ring on either hand, it stays seated at the base of the finger the whole time, and his right hand wears no ring at all"

_fix("01-04", act="@Ngan stops reading mid-breath. Keeping the headphones on her head the whole time, she lifts only the right ear cup a little away from her right ear with her right hand and slowly turns her head toward the RIGHT of frame, toward the bare wall, listening. The headband stays on top of her head until the end of the shot; the headphones never go down to her neck. She does not speak.")
_fix("01-10", cam="85mm close-up of @Hung lounging in the white velvet armchair in the cream-and-pink bedroom, the back of his head resting against the bare pale-cream wall on the LEFT of frame, phone at his right ear; the soft background is the bed and the vanity mirror with its bulbs; there is no microphone, no stand and no studio equipment anywhere in this bedroom")
_fix("01-14", act="At the very first frame three sharp knocks sound from the wall right behind @Hung's head; he jerks forward out of his lazy slouch in fright, eyes wide, and twists round to stare at the wall; @Diem spins round on the vanity stool, startled. He is visibly scared, not relaxed. He forces himself to answer too quickly while " + RING1 + ". A clean photographic image: nothing is drawn over the picture.")
_fix("02-02", act="@Hung hangs his keys on a hook; then " + RING1 + ". From the first frame to the last there is exactly one ring in the shot.")
_fix("02-10", attach=["HU1", "NG1"],
     cam="over-the-shoulder from behind their 8-year-old son Bin standing in the corridor in front of the neighbour's door (seen only from behind: short black hair, white school shirt, red neckerchief knot and small navy backpack soft in the RIGHT foreground), looking LEFT toward the family's open doorway, where @Ngan stands holding the door and @Hung in his navy suit leans out behind her shoulder",
     act="@Hung leans out past his wife, glances at the slippers by the boy's feet, and answers the boy a little too quickly, avoiding his wife's eyes, while " + RING1 + ". @Ngan keeps her eyes on the slippers. The boy stays still with his back to camera; his face is never seen.")
_fix("03-06", attach=["DI2B", "NG1"],
     cam="over-the-shoulder from behind @Diem standing in the corridor (seen only from behind: her long wavy chestnut hair, short white tweed jacket and the wicker fruit basket soft in the RIGHT foreground) onto @Ngan in the family's open doorway, medium shot",
     act="@Ngan steps back and opens the door wide with one hand, inviting her in, with a polite smile that stops at her eyes.")
_fix("04-08", act="The front door opens and @Bin in his school uniform comes in with his small navy backpack on both shoulders, pushes the door shut behind him and calls out happily. The backpack stays on his back for the whole shot; he does not take it off or put it down.")
_fix("04-14", act="@Bin, his backpack still on both shoulders, walks away from camera toward a bedroom door on the LEFT, and out of frame.")
_fix("06-06", cam="50mm medium shot of @Hung standing by the dining table, the front door off-screen LEFT; the soft foreground on the RIGHT is the back of a wooden dining chair",
     act="A single set of car keys lies on the table. @Hung snatches up the car keys, avoids her eyes, says the line and walks straight out of frame to the LEFT toward the front door. After he picks the keys up there are no keys left on the table. He never walks toward the back of the room.")
_fix("07-10", cam="85mm close-up of @BaLua at her steel desk, three-quarter, looking LEFT of camera, her gold-rimmed glasses hanging on the beaded chain against her chest; the soft foreground on the RIGHT is the blue-and-white teapot on the desk",
     act="@BaLua, her glasses off and hanging on the beaded chain on her chest the whole shot (she does not put them on), speaks slowly, remembering, looking straight at her guest.")
_fix("07-12", secs=5, cam="85mm medium close-up of @BaLua at her steel desk, three-quarter, looking down at the open blue notebook; the writing is only unreadable scribble",
     act="@BaLua lifts her gold-rimmed glasses from the chain back onto her nose, opens the blue notebook and writes in it with a pen, muttering.",
     lines=[("BaLua", "Tài sản riêng của cô. Để tôi ghi vào sổ.", "determined, matter-of-fact|quyết, rành mạch")])
_fix("16-06", act="Close on his hands: " + RING1 + ". From the first frame to the last there is exactly one ring in the shot.")
_fix("19-04", act=RING1[0].upper() + RING1[1:] + ". From the first frame to the last there is exactly one ring in the shot.")

# v3b: 21-08 tháo nhẫn — bản cũ: 2 nhẫn lúc đầu, tháo xong vẫn còn nhẫn trên ngón. Dàn lại: kết thúc trên chiếc nhẫn một mình.
_fix("21-08", secs=6, cam="close shot at table height on the teal tablecloth: only @Hung's two hands, his navy suit cuffs and the pink booklet are in frame",
     act="His left hand rests on the tablecloth; the single plain gold wedding band on his left ring finger is the only ring on either hand. With his right thumb and forefinger he slowly works that one band up over the knuckle and off the fingertip, and lays it down on the tablecloth beside the pink booklet. Then he slowly draws both hands back toward himself and out of the bottom of the frame, and the shot ends on the lone ring lying on the cloth beside the booklet. There is only ever one ring in the shot.")

# v3c: 24-05 — bản cũ vẫn đeo nhẫn khi nhìn ngón tay trần
_fix("24-05", act="@Hung irons a white shirt alone. He wears no ring at all: every finger of both hands is bare, with only a faint pale band of skin at the base of the left ring finger. He stops, lifts his left hand and looks at that bare ring finger for a moment, then goes back to ironing.")

# v3d: tiếng gõ cửa gần cuối
_fix("23-01", secs=5, cam="50mm medium shot in the corridor at night: the family's closed dark-wood front door on the LEFT of frame, @Hung standing close in front of it, seen in three-quarter profile facing the door",
     act="@Hung, in a crumpled white shirt, raises his right hand and knocks his knuckles on the wooden door three times, slowly and evenly, with a clear pause between each knock: knock... knock... knock. His knuckles touch the door each time. Then he lowers his hand and waits, still facing the door, head bowed. He never turns away from the door and never looks down the corridor.")
_fix("25-02", cam="35mm from inside the studio: @Ngan at the desk on the RIGHT with the headphones on her head; the open studio doorway with its wooden door frame on the LEFT",
     act="@Bin steps into the open doorway on the LEFT, faces into the room and knocks his knuckles on the wooden door frame beside him three times, knock, knock, knock; his knuckles touch the frame each time. @Ngan hears it, slides the headphones off her head down to her neck once, and they stay around her neck until the end of the shot; she turns her chair toward him with a warm smile.")

# v3e: 22-10 — bản cũ thành vòng kiềng trơn, mất hạt ngọc
_fix("22-10", act="@Ngan holds the old thin gold chain bracelet with a single small green jade bead, the same delicate bracelet Diem just gave back (not a bangle, not a plain ring of gold), slips it onto her own left wrist, fastens the tiny clasp and looks down at it; the small green jade bead rests on top of her wrist.")

# v3f: đổi cách dàn cảnh cho các đạo cụ "tháo ra" mà mô hình hay làm sai
_fix("06-06", cam="50mm medium shot of @Hung standing beside the dining table, the front door off-screen LEFT; the soft foreground on the RIGHT is the back of a wooden dining chair",
     act="@Hung already holds his car keys in his right hand. Avoiding her eyes, he says the line, then turns to his left and walks straight out of the LEFT edge of the frame toward the front door. Nothing lies on the table. He never walks toward the back of the room or the balcony.")
_fix("07-09", act="@BaLua slowly lowers her gold-rimmed glasses to the tip of her nose and stares at her guest over the top of them for a long beat, then pushes them back up into place with one finger. The glasses stay on her face the whole time.")
_fix("16-06", cam="macro close-up of only @Hung's LEFT hand resting on his knee, the single plain gold wedding band on its ring finger; his right hand stays out of frame except the tips of the right thumb and forefinger",
     act="The tips of his right thumb and forefinger come in from the edge of frame and twist the single band round and round on the left ring finger. There is exactly one ring in the shot; no other finger wears a ring.")
_fix("21-08", secs=5, cam="50mm medium shot of @Hung sitting alone at the front table covered with the teal cloth, three-quarter from his left, head bowed, the blurred residents behind him; the pink booklet lies on the table in front of him",
     act="@Hung looks down at his left hand, slowly works the single gold wedding band off his ring finger and lays it on the tablecloth beside the pink booklet, then lowers both hands below the edge of the table and stays still, head bowed, not looking up.")

# v3g: 01-10 bản mới chỉ nói đến "em ạ" rồi cúp máy -> phụ đề khớp tiếng
_fix("01-10", lines=[("Hung", "Đông lắm. Ồn lắm em ạ.", "fake weary sigh|thở dài mệt giả")])

# ===================== v4 (duyệt liền mạch từng mốc) =====================
# 02-11: Bin đang đứng ở hành lang (02-10) thì biến mất -> cho Bin chạy qua bà Lụa ra thang máy trước khi bà nói
_fix("02-11", attach=["LU1", "BI2"],
     cam="50mm medium shot in the corridor, the neighbour's door on the LEFT edge of frame, the lift lobby off-screen RIGHT",
     act="In the first two seconds @Bin, in his school uniform with his small navy backpack on both shoulders, hurries across the frame from the LEFT toward the lift and out of the RIGHT edge of frame, giving a quick little bow as he passes; @BaLua, coming the other way from the lift with her glasses on her nose and her blue notebook open, glances after him, stops by the neighbour's shoe rack and looks toward the family's door off-screen LEFT. @Bin does not speak and does not come back; only @BaLua speaks.")
# 06-09: Hưng ngồi xuống giường rồi 06-10/06-12 lại đứng tựa tường -> đứng tựa tường suốt
_fix("06-09", act="@Diem, sitting on the edge of the bed on the RIGHT and brushing her hair, asks lightly. @Hung stays standing by the bare wall on the LEFT for the whole shot: he undoes the top button of his collar with one hand, then leans one shoulder against the wall with a pleased little smile. He never sits down and never walks to the bed. He never touches his wrists or sleeves; his wrists are bare.")
# 07-10: bản v3 có 2 cặp kính (trên mặt + treo trước ngực) -> chỉ 1 cặp, đeo trên mặt (khớp 07-09 và 07-12)
_fix("07-10", cam="85mm close-up of @BaLua at her steel desk, three-quarter, looking LEFT of camera, her one pair of gold-rimmed glasses on her nose; the soft foreground on the RIGHT is the blue-and-white teapot on the desk",
     act="@BaLua wears her one pair of gold-rimmed glasses on her nose the whole shot, the thin beaded chain hanging from the arms of those glasses behind her ears; she speaks slowly, remembering, looking straight at her guest. There is exactly one pair of glasses in the shot: nothing else hangs on her chest, no second pair of glasses anywhere.")
# 19-09: 19-08 hai người đứng ở cửa kính, 19-09 lại ngồi ghế -> đứng nguyên chỗ
_fix("19-09", cam="50mm two-shot from inside the office at the glass front door, same framing as the previous shot: @BaLua on the LEFT and @Ngan on the RIGHT standing side by side at the glass, the street soft and bright behind the glass",
     act="Both women stay standing side by side at the glass door exactly where they were; nobody sits down and there are no chairs near them. @Ngan turns her head toward @BaLua and speaks quietly; @BaLua hugs her blue notebook to her chest and answers proudly.")
# 08-01/08-02: nồi canh — 08-01 nồi men trắng hoa, 08-02 tay không, 08-03 nồi men nâu sẫm -> cả 3 shot cùng một nồi nâu sẫm, cầm suốt
POT = "a dark brown enamel cooking pot with a domed lid and two small side handles"
_fix("08-01", act="@Ngan stands in front of the neighbour's door on the RIGHT, holding " + POT + " against her left hip in the crook of her left arm, and presses the doorbell with one finger of her right hand. She keeps holding the pot for the whole shot; it is the only thing in her hands.")
_fix("08-02", act="@Diem has just opened the door and stands inside the doorway on the RIGHT, surprised. @Ngan stands in the corridor on the LEFT holding " + POT + " in front of her with both hands by its two side handles; she holds the pot the whole shot and never puts it down; @Diem glances at the pot.")
# 03-05/03-07: giỏ hoa quả — 03-02/03-03/03-06 Diễm cầm giỏ, 03-05 và 03-07 tay không -> cầm giỏ suốt
BASKET = "the wicker fruit basket tied with a pink ribbon"
_fix("03-05", act="The two women face each other across the threshold. @Diem holds " + BASKET + " in front of her with both hands for the whole shot; it never leaves her hands.")
_fix("03-07", act="@Diem, still holding " + BASKET + " in her left hand the whole shot, slips off her heels, steps into a pair of guest slippers and looks around the room with delight. The basket stays in her hand; she does not put it down.")
# 13-02: Ngân đứng trong khi 13-01/13-05/13-07 ngồi; bảng sau lưng có chữ -> ngồi ghế khách, tường trơn
_fix("13-02", cam="85mm close-up of @Ngan sitting in the visitor's chair across the steel desk, three-quarter, looking RIGHT of camera, her phone in her hand with its screen facing away from camera; behind her only a plain pale wall and the soft edge of a window",
     act="@Ngan stays seated for the whole shot; she glances down at the phone in her hand and speaks evenly. Nothing behind her has any writing, labels or signs.")
# 22-09: vali hồng ở 22-01 thành vali màu be, và có 2 lồng mèo (bỏ lại 1 cái) -> đúng 1 vali hồng + 1 lồng mèo xám, mang đi hết
_fix("22-09", act="@Diem, seen only from behind, picks up her one grey plastic cat carrier in her left hand and pulls her one pink hard-shell suitcase with her right hand, and walks away from camera down the corridor toward the lift and out of frame. There is exactly one suitcase, and it is pink, and exactly one cat carrier, and it is grey; she takes both with her and nothing is left on the corridor floor.")
