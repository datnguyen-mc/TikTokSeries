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
