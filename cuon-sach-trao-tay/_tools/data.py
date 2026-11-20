# -*- coding: utf-8 -*-
"""Dữ liệu phim Cuốn Sách Trao Tay: nhân vật theo bộ đồ, bối cảnh, 20 cảnh và bảng shot.
Sửa ở đây rồi chạy build.py để sinh NHAN_VAT_FLOW.md, kich-ban/, film/cXX/*.txt."""

# ---------------------------------------------------------------- người: khuôn mặt + giọng
PEOPLE = {
    "Khang": dict(name="Khang", role="the founder of a tech group",
        face="a composed 44-year-old Vietnamese man, medium build with a slightly full face, rectangular black-framed glasses, short neat black hair greying at the temples, clean-shaven, calm tired intelligent eyes",
        voice="man of 44, low calm baritone, few words, long pauses"),
    "KhangTre": dict(name="Khang lúc trẻ", role="young Khang",
        face="a slim young adult Vietnamese man, sun-tanned skin, high cheekbones, rimless glasses, neat side-parted short black hair, bright curious eyes, a shy smile",
        voice="young man of 19, light clear tenor, shy and polite"),
    "BaHanh": dict(name="Bà Hạnh", role="Khang's mother",
        face="a small, wiry 72-year-old Vietnamese countrywoman, sun-browned deeply lined face, sharp stubborn eyes, grey hair in a low bun, thin lips pressed tight",
        voice="woman of 72, dry low voice, short clipped sentences"),
    "BaHanhTre": dict(name="Bà Hạnh lúc trẻ", role="Khang's mother, 25 years earlier",
        face="a slim 47-year-old Vietnamese countrywoman, tired gentle face, black hair in a low bun, sharp eyes",
        voice="woman of 47, soft steady alto, few words"),
    "CoLan": dict(name="Cô Lan", role="the old bookseller",
        face="a sharp-tongued 62-year-old Vietnamese woman, round face, short permed grey hair, thick reading glasses on a beaded chain, quick amused eyes",
        voice="woman of 62, quick bright voice, teasing, a little raspy"),
    "CoLanTre": dict(name="Cô Lan lúc trẻ", role="the bookseller, 25 years earlier",
        face="a lively 37-year-old Vietnamese woman, round face, short permed black hair, reading glasses on a beaded chain, quick amused eyes",
        voice="woman of 37, quick bright voice, teasing"),
    "Mai": dict(name="Mai", role="a village girl who just got into university",
        face="a slim 19-year-old Vietnamese young woman, a university freshman from the countryside, sun-tanned skin, big dark eyes, long black hair in a ponytail, a stubborn chin, a quick sideways grin",
        voice="young woman of 19, clear fast mezzo, blunt, laughs through her nose"),
    "Tung": dict(name="Tùng", role="Khang's finance director",
        face="a sharp 38-year-old Vietnamese man, lean, slicked-back black hair, thin metal-framed glasses, a neatly trimmed short beard, alert eyes",
        voice="man of 38, crisp fast tenor, speaks like reading a report"),
    "Thang": dict(name="Anh Thắng", role="the bulldozer crew foreman",
        face="a stocky 45-year-old Vietnamese construction foreman, sunburnt face, short buzz cut, thick black moustache, kind eyes",
        voice="man of 45, gruff loud voice, countryside warmth"),
    "CoGai": dict(name="Cô gái lạ", role="a young woman from the village",
        face="a 19-year-old Vietnamese young woman, round face, short bob haircut, shy eyes",
        voice="young woman of 19, soft hopeful voice", text_only=True,
        outfit_text="a faded blue factory-worker shirt, black trousers, plastic sandals"),
}

# ---------------------------------------------------------------- bộ đồ = nhân vật trên Flow
# code: (person, tên trên Flow, mô tả bộ đồ, cảnh dùng, ghi chú, là bộ gốc?)
OUTFITS = {
    "KH1": ("Khang", "Khang · Sơ mi đêm", "a white dress shirt with the top two buttons undone and sleeves rolled to the forearms, dark charcoal trousers, black leather shoes, a silver wristwatch", "02", "Đã có trên Flow tên KhangMid", True),
    "KH2": ("Khang", "Khang · Vest họp", "a tailored navy-blue suit over a crisp white shirt, no tie, a silver wristwatch, polished black shoes", "01, 05, 19", "Phòng họp", False),
    "KH3": ("Khang", "Khang · Sơ mi về quê", "a plain white linen shirt with sleeves rolled up, beige chino trousers, brown leather loafers, a silver wristwatch", "06–18", "Về làng thứ Bảy, Chủ nhật", False),
    "KH4": ("Khang", "Khang · Polo khai trương", "a light-blue polo shirt, navy trousers, white canvas sneakers", "20", "Vài tuần sau", False),
    "KY1": ("KhangTre", "Khang trẻ · Sơ mi trắng cũ", "a slightly yellowed old white short-sleeved shirt, navy-black trousers frayed at the hem, brown sandals with heel straps, a faded canvas backpack", "03, 04", "19 tuổi. Đã có trên Flow tên KhangYoung", True),
    "KY2": ("KhangTre", "Khang trẻ · Đêm lũ", "a soaked grey T-shirt clinging to his body, a torn clear plastic raincoat, rolled-up dark trousers, bare feet, wet hair", "10", "24 tuổi, phòng thuê ngập nước", False),
    "BH1": ("BaHanh", "Bà Hạnh · Áo cánh nâu", "a faded brown traditional áo cánh blouse with cloth buttons, black satin trousers, plastic sandals, bare earlobes with old empty piercing holes", "02, 06, 10, 11, 17", "Ở nhà", True),
    "BH2": ("BaHanh", "Bà Hạnh · Áo dài nhung", "a deep-red velvet áo dài over black trousers, a pair of small old gold hoop earrings, hair neatly pinned", "20", "Đeo lại đôi bông tai", False),
    "BHT": ("BaHanhTre", "Bà Hạnh trẻ · Áo cánh hoa", "a pale floral cotton blouse, black cloth trousers, plastic sandals, a pair of small gold hoop earrings", "04, 10", "47 tuổi, hồi tưởng. Tạo từ ảnh BH1, trẻ hơn 25 tuổi", False),
    "CL1": ("CoLan", "Cô Lan · Áo len bán sách", "a pale-blue blouse under a thin grey knitted cardigan, cloth sleeve protectors on her forearms, dark trousers, reading glasses on a beaded chain", "01, 07, 08, 12, 14, 15", "Hiệu sách", True),
    "CL2": ("CoLan", "Cô Lan · Áo mới khai trương", "a new jade-green silk blouse, black trousers, new reading glasses on a beaded chain, a small brooch", "20", "Khai trương phòng máy", False),
    "CLT": ("CoLanTre", "Cô Lan trẻ · Áo blouse xanh", "a pale-blue blouse, cloth sleeve protectors on her forearms, dark trousers, a wooden ruler in her hand, reading glasses on a beaded chain", "03", "37 tuổi, hồi tưởng. Tạo từ ảnh CL1, trẻ hơn 25 tuổi", False),
    "MA1": ("Mai", "Mai · Sơ mi trắng ba lô", "an old oversized white shirt, navy-black trousers, plastic sandals with heel straps, a faded canvas backpack", "01, 08, 13, 15", "", True),
    "MA2": ("Mai", "Mai · Đồ nhặt ve chai", "a faded grey T-shirt, loose dark trousers rolled at the ankle, cotton work gloves, a conical nón lá hat pushed back", "09, 18", "Bãi ve chai", False),
    "MA3": ("Mai", "Mai · Đi nhập học", "a crisp new white shirt, black trousers, white canvas sneakers, a new navy backpack", "20", "Lên đường nhập học", False),
    "TU1": ("Tung", "Tùng · Vest xám", "a slim charcoal-grey suit, a white shirt, a dark-blue tie, a thin smartwatch", "01, 05, 19", "Phòng họp", True),
    "TU2": ("Tung", "Tùng · Áo khoác về làng", "a black zip-up windbreaker jacket thrown over a white shirt with loosened tie, grey trousers, black leather shoes", "11, 13–16", "Đuổi theo về làng", False),
    "TH1": ("Thang", "Anh Thắng · Áo bảo hộ", "a fluorescent orange safety vest over a faded navy work shirt, a yellow hard hat, dusty work trousers, rubber boots", "14, 15", "Đốc công máy ủi", True),
}

# ---------------------------------------------------------------- bối cảnh
PLACES = {
    "B1": "A top-floor glass meeting room in a modern city office tower: a long dark walnut table, black leather chairs, floor-to-ceiling windows over a hazy grey skyline, cool steel-blue daylight, everything minimal and expensive.",
    "B2": "A large dark executive office on a high floor at night: a brass desk lamp with a green glass shade on a walnut desk, a face-down black smartphone, a low wooden cabinet, floor-to-ceiling windows full of city lights.",
    "B3": "A small old bookshop on a countryside market street today: tall wooden shelves painted pale green and half emptied, stacks of books tied with string, taped cardboard boxes everywhere, a scratched glass display counter, an old ceiling fan, a yellowed scrap of paper pinned to the wall behind the counter, late golden sunlight through the open shopfront.",
    "B4": "The same small countryside bookshop twenty-five years ago, bright and full: tall wooden shelves freshly painted pale green and packed with books, a clean glass display counter, a slow ceiling fan, dusty sunbeams slanting in through the open shopfront, a village road with bicycles outside.",
    "B5": "An old three-room tile-roofed village house in the Northern Vietnamese countryside: a brick-paved yard with a jackfruit tree, a low brick gate, a porch with wooden pillars; inside, a dim central room with a wooden cabinet, a family altar and an old beige desktop computer with a bulky CRT monitor under a cloth cover.",
    "B6": "A dusty village scrap yard beside green rice fields: heaps of flattened cans, plastic bottles and cardboard, an old hanging scale on a wooden post, a bicycle loaded with sacks, warm late-afternoon light.",
    "B7": "A cramped rented room in a city alley twenty years ago, flooded knee-deep with muddy water at night: desks, beige computer towers and CRT monitors, tangled cables, a wooden ladder to a loft, the beam of a flashlight; later, a small street phone booth at grey dawn.",
    "B8": "The countryside market street in front of the bookshop on an overcast morning: a yellow bulldozer with its bucket stopped an arm's length from the bookshop door, a row of half-demolished shophouses, villagers gathered at a distance, grey sky, diesel smoke.",
    "B9": "A small gold shop at the head of a countryside market twenty-five years ago: a glass counter with a tiny brass scale, a red velvet tray, an old shopkeeper seen only from behind, warm morning light.",
    "B10": "The same small countryside bookshop reopened, bright and warm: one side still tall pale-green wooden shelves full of books, the other side a neat row of new desktop computers on wooden tables, young adult villagers working at them, warm sunlight, potted plants, a small framed scrap of yellowed paper on the wall.",
}

LOOK = ("Feature-film cinematography for a premium Vietnamese family drama with a gentle comic bite: shot on ARRI Alexa 35 with Cooke anamorphic/i lenses, 24 fps, 16:9 full frame without letterbox bars; deliberate cinematic blocking with foreground elements and layered depth, motivated natural light, soft haze in the air, rich true-to-life Vietnamese skin tones, gentle film halation and fine 35mm grain, shallow depth of field with creamy bokeh. Restrained, truthful acting with micro-expressions, like an award-winning Asian festival film; never CGI, never a video game, never an advertisement.")
LOOK_FLASH = " This is a memory from twenty-five years ago: warmer golden grade, slightly faded colours, thicker film grain."

AVOID = ("On-screen text, subtitles, captions, logos, watermarks, readable writing on paper, maps, contracts, screens, boxes or signs; any cut or second camera angle; the same person appearing twice, twins, clones or look-alike doubles; children or minors; extra people in focus; distorted hands or fused fingers; face, hair or costume changes; plastic or waxy skin; flashing or cutting to an attached reference portrait or a plain grey studio backdrop; repeated, echoed or stuttered words; an off-screen narrator; background music; Southern or Central Vietnamese accents.")

# ---------------------------------------------------------------- cảnh và shot
# shot: (tên, giây tối thiểu, [mã bộ đồ], camera, hành động, [(người, câu, sắc thái)], ghi chú)
# mã bộ đồ "CoGai" = người không gắn ảnh. Shot có "EXIST:<file>" là clip đã quay ở bản 1.
S = []
def scene(num, title, act, when, place, sound, shots, flash=False):
    S.append(dict(num=num, title=title, act=act, when=when, place=place, sound=sound, shots=shots, flash=flash))

scene("01", "Giá của một đời người", "Hồi 1 · Lời đề nghị", "mở đầu: chiều thứ Bảy ở hiệu sách; rồi chiều thứ Sáu ở phòng họp", "B1",
  "air-conditioning hum, faint city traffic far below, a pen tapping glass. No music.", [
  ("Câu mở đầu", 5, ["MA1", "CL1"], "50mm medium two-shot across the glass counter, warm late sunlight", "@Mai sets a small pile of crumpled small banknotes and coins on the glass counter and pushes a blue-covered book toward @CoLan, breathless and hopeful.", [("Mai", "Cô ơi, cô giữ cuốn này cho cháu mấy hôm được không ạ?", "hopeful, a little breathless")], "B3"),
  ("Hai mươi lăm năm trước", 4, ["CL1"], "85mm close-up over the counter, slow push-in", "@CoLan freezes, then slowly lifts her eyes past the girl toward the doorway.", [("CoLan", "Câu này… hai mươi lăm năm trước có đứa nói rồi.", "quiet, stunned")], "B3"),
  ("Khang ở cửa", 3, ["KH3"], "85mm close-up in the bookshop doorway, backlit by the street", "@Khang stands in the doorway, motionless; his eyes fill with something he cannot say.", [], "B3"),
  ("Ba ngày trước", 3, [], "macro close-up on a walnut desk", "A black smartphone lying face down vibrates on the dark wood, inching a few millimetres with each buzz.", [], "B2"),
  ("Phòng họp kính", 4, ["KH2", "TU1"], "wide shot down the long walnut table toward the windows", "@Tung slides a thick folder across the table to @Khang, who sits at the head of the table, back to the skyline.", [], ""),
  ("Giá cuối", 4, ["TU1"], "50mm medium shot", "@Tung taps the closed folder with two fingers, still half-disbelieving.", [("Tung", "Giá cuối của họ. Em đọc ba lần vẫn không tin.", "crisp, impressed")], ""),
  ("Không mở", 3, ["KH2"], "85mm close-up", "@Khang looks at the folder and does not open it.", [], ""),
  ("Một điều kiện", 5, ["TU1"], "50mm medium shot, slow push-in", "@Tung leans forward and lowers his voice.", [("Tung", "Một điều kiện: kho vận phía Bắc phải khởi công trước ngày ký.", "matter-of-fact")], ""),
  ("Ký thì được gì", 3, ["KH2"], "85mm close-up", "@Khang leans back in the leather chair.", [("Khang", "Ký thì tôi được gì?", "flat, tired")], ""),
  ("Được nghỉ", 5, ["TU1"], "50mm medium shot", "@Tung smiles for the first time.", [("Tung", "Anh được nghỉ. Hai mươi lăm năm anh chưa nghỉ ngày nào.", "warm, almost teasing")], ""),
  ("Nghỉ để làm gì", 3, ["KH2"], "85mm close-up", "@Khang gives a dry half-smile.", [("Khang", "Nghỉ để làm gì?", "dry, half amused")], ""),
  ("Úp điện thoại", 3, ["KH2"], "insert close-up on the table, his hand in frame", "@Khang's phone buzzes on the glass; without looking he turns it face down.", [], ""),
  ("Chín giờ thứ Hai", 5, ["TU1", "KH2"], "40mm medium two-shot, Tung standing by the door", "@Tung buttons his jacket at the door and looks back at @Khang.", [("Tung", "Chín giờ sáng thứ Hai. Anh ký là xong một đời.", "formal, final")], ""),
  ("Mười hai cuộc", 5, ["KH2"], "85mm close-up, city light on his glasses", "@Khang turns the phone over, looks at it for a long beat, then lays it face down again.", [("Khang", "Mẹ tôi gọi mười hai cuộc.", "quiet, to himself")], ""),
])

scene("02", "Mười hai cuộc gọi nhỡ", "Hồi 1 · Lời đề nghị", "đêm thứ Sáu", "B2",
  "office air-conditioning hum, faint city through glass; at the village house, crickets and a distant dog. No music.", [
  ("Đêm văn phòng", 15, ["KH1"], "", "", [], "EXIST:canh-01_clip-1.mp4"),
  ("Gọi lại", 4, ["KH1"], "85mm close-up, lamp light on one side of his face", "@Khang holds the phone to his ear.", [("Khang", "Mẹ ạ. Con đây.", "soft, guilty")], ""),
  ("Bà ở hiên", 5, ["BH1"], "50mm medium shot on the dark porch, a bare bulb behind her", "@BaHanh sits on the porch step holding an old mobile phone to her ear.", [("BaHanh", "Hiệu sách cô Lan sắp bị ủi rồi.", "flat, no greeting")], "B5"),
  ("Công ty kho", 5, ["BH1"], "85mm close-up", "@BaHanh looks out at the dark yard.", [("BaHanh", "Người ta bảo của công ty kho gì trên thành phố.", "dry")], "B5"),
  ("Vì thế ạ", 4, ["KH1"], "85mm close-up", "@Khang rubs his eyes under his glasses.", [("Khang", "Mẹ gọi con mười hai cuộc vì thế ạ?", "weary")], ""),
  ("Giữ một thứ", 5, ["BH1"], "85mm close-up, slow push-in", "@BaHanh hesitates before speaking.", [("BaHanh", "Cô Lan bảo… cô còn giữ một thứ của con.", "careful")], "B5"),
  ("Thứ gì", 3, ["KH1"], "85mm close-up", "@Khang sits up.", [("Khang", "Thứ gì ạ?", "alert")], ""),
  ("Về mà hỏi", 3, ["BH1"], "50mm medium shot", "@BaHanh lowers the phone and ends the call.", [("BaHanh", "Về mà hỏi.", "curt")], "B5"),
  ("Máy tắt", 3, ["KH1"], "85mm close-up", "@Khang slowly lowers the silent phone and stares at it.", [], ""),
  ("Chiếc hộp cũ", 15, ["KH1"], "", "", [], "EXIST:canh-01_clip-2.mp4"),
  ("Cuốn sách", 15, ["KH1"], "", "", [], "EXIST:canh-01_clip-3.mp4"),
  ("Tờ giấy rơi", 4, ["KH1"], "macro close-up on the desk under the lamp", "A small yellowed folded scrap of paper slips out from between the pages of an old blue book and lands on the walnut desk; @Khang's hand picks it up.", [], ""),
  ("Ba nghìn", 4, ["KH1"], "85mm close-up, warm lamp light", "@Khang unfolds the paper and smiles for the first time in the film.", [("Khang", "Ba nghìn…", "a whisper, almost a laugh")], ""),
])

scene("03", "Cuốn sách hai mươi lăm năm", "Hồi 1 · Lời đề nghị", "hồi tưởng: chiều hè, năm Khang 19 tuổi", "B4",
  "cicadas, a slow ceiling fan ticking, a bicycle bell outside, pages turning. No music.", [
  ("Đọc sách dưới nắng", 15, ["KY1"], "", "", [], "EXIST:canh-01_clip-4.mp4"),
  ("Đọc chùa", 4, ["CLT"], "50mm medium shot behind the glass counter", "@CoLanTre taps a wooden ruler on the counter, looking over her reading glasses.", [("CoLanTre", "Đọc chùa ba chiều rồi đấy. Mua không?", "teasing, sharp")], ""),
  ("Thiếu ba nghìn", 4, ["KY1"], "50mm medium shot, he sits cross-legged between shelves", "@KhangTre looks up, embarrassed, clutching the blue book.", [("KhangTre", "Cháu… thiếu ba nghìn ạ.", "embarrassed, small voice")], ""),
  ("Đọc nốt chương", 4, ["CLT"], "85mm close-up", "@CoLanTre goes back to her ledger without looking up.", [("CoLanTre", "Thế đọc nốt chương này rồi về.", "gruff but kind")], ""),
  ("Ôm sách đứng dậy", 3, ["KY1"], "medium shot, slow push-in", "@KhangTre stands up, hugging the book to his chest, gathering courage.", [], ""),
  ("Cô giữ cho cháu", 5, ["KY1", "CLT"], "40mm two-shot across the counter", "@KhangTre walks to the counter and sets the book down carefully.", [("KhangTre", "Cô ơi, cô giữ cuốn này cho cháu mấy hôm được không ạ?", "hopeful, polite")], ""),
  ("Giữ đến bao giờ", 3, ["CLT"], "85mm close-up", "@CoLanTre peers at him over her glasses.", [("CoLanTre", "Giữ đến bao giờ?", "dry")], ""),
  ("Đủ tiền", 3, ["KY1"], "85mm close-up", "@KhangTre swallows.", [("KhangTre", "Đến khi cháu đủ tiền.", "earnest")], ""),
  ("Viết giấy nợ", 4, ["CLT"], "50mm medium shot", "@CoLanTre pushes the book back to him, then a small slip of paper and a ballpoint pen.", [("CoLanTre", "Cầm về. Viết giấy nợ.", "brisk")], ""),
  ("Tay viết", 4, ["KY1"], "insert close-up on the counter", "@KhangTre's hand writes a few careful unreadable lines on the small slip of paper.", [], ""),
  ("Ghim lên tường", 5, ["CLT"], "50mm medium shot toward the wall behind the counter", "@CoLanTre pins the little slip of paper on the wall behind the counter with a drawing pin.", [("CoLanTre", "Bao giờ thành người thì trả.", "half joking, half serious")], ""),
  ("Chạy ra nắng", 4, ["KY1"], "wide shot from inside toward the sunlit street", "@KhangTre bows quickly and runs out into the sun with the book.", [("KhangTre", "Cháu cảm ơn cô ạ!", "bright, over his shoulder")], ""),
], flash=True)

scene("04", "Đôi bông tai", "Hồi 1 · Lời đề nghị", "hồi tưởng: tối hôm ấy, rồi sáng hôm sau", "B5",
  "crickets, a bare bulb buzzing, cans clinking on bricks. No music.", [
  ("Đổ ve chai", 4, ["KY1"], "high wide shot over the brick yard at dusk", "@KhangTre empties a sack of flattened cans and bottles onto the brick yard.", [], ""),
  ("Đếm tiền", 4, ["KY1"], "50mm medium shot under a bare bulb", "@KhangTre sits on the step counting small creased banknotes, lips moving.", [("KhangTre", "Hai trăm… hai trăm mốt…", "muttering")], ""),
  ("Bà ở cửa", 3, ["BHT"], "50mm medium shot in the doorway", "@BaHanhTre leans on the doorframe, drying her hands on a cloth.", [("BaHanhTre", "Đếm gì mà đếm mãi thế?", "tired, gentle")], ""),
  ("Học bơi trên cạn", 5, ["KY1"], "85mm close-up", "@KhangTre looks up at her, frustrated and hopeful.", [("KhangTre", "Mẹ ơi, học lập trình mà không có máy, như học bơi trên cạn.", "frustrated, pleading")], ""),
  ("Tay chạm tai", 4, ["BHT"], "85mm close-up", "@BaHanhTre says nothing; her fingers drift up and touch the small gold hoop in her ear.", [], ""),
  ("Đi ngủ đi", 3, ["BHT"], "50mm medium shot", "@BaHanhTre turns back inside.", [("BaHanhTre", "Đi ngủ đi.", "quiet")], ""),
  ("Nửa đêm", 5, ["BHT"], "50mm medium shot by an oil lamp, deep night", "@BaHanhTre sits alone on the bed and slowly unhooks the gold hoop earrings from her ears.", [], ""),
  ("Trên lòng bàn tay", 4, ["BHT"], "macro close-up", "Two small gold hoop earrings rest on @BaHanhTre's open, work-worn palm in the lamplight.", [], ""),
  ("Tiệm vàng", 4, ["BHT"], "50mm medium shot across a glass counter", "@BaHanhTre slides the two earrings across the glass counter toward an old shopkeeper seen only from behind.", [], "B9"),
  ("Máy tính về nhà", 4, ["KY1"], "wide shot of the yard in bright morning sun", "Two blurred porters carry a beige desktop computer and a bulky CRT monitor into the yard; @KhangTre stands frozen on the step.", [], ""),
  ("Tiền đâu ra", 4, ["KY1", "BHT"], "40mm two-shot in the yard", "@KhangTre turns to his mother, stunned.", [("KhangTre", "Mẹ lấy tiền đâu ra?", "stunned")], ""),
  ("Bán con lợn", 3, ["BHT"], "85mm close-up", "@BaHanhTre answers without meeting his eyes.", [("BaHanhTre", "Mẹ bán con lợn.", "too quick")], ""),
  ("Dái tai trống", 4, ["KY1"], "85mm close-up over her shoulder", "@KhangTre's eyes drop to his mother's bare earlobes.", [("KhangTre", "Mẹ… bông tai của mẹ đâu?", "slow, realizing")], ""),
  ("Ăn cơm đi", 3, ["BHT"], "50mm medium shot", "@BaHanhTre turns away toward the kitchen.", [("BaHanhTre", "Ăn cơm đi.", "firm, closing the subject")], ""),
], flash=True)

scene("05", "Kho của chính mình", "Hồi 1 · Lời đề nghị", "sáng thứ Bảy", "B1",
  "air-conditioning hum, a projector fan, faint city. No music.", [
  ("Sách trên bàn họp", 4, ["KH2"], "high angle over the long table", "@Khang sets an old dog-eared blue book down on the polished glass-and-walnut table.", [], ""),
  ("Sách gì cũ thế", 3, ["TU1"], "50mm medium shot", "@Tung raises an eyebrow at the book.", [("Tung", "Sách gì mà cũ thế anh?", "curious")], ""),
  ("Mở bản đồ", 4, ["KH2"], "85mm close-up", "@Khang does not explain.", [("Khang", "Mở cho tôi bản đồ kho phía Bắc.", "quiet, firm")], ""),
  ("Trừ một hộ", 5, ["TU1"], "40mm shot with a large wall screen glowing with an unreadable map", "@Tung points at the glowing screen with a pen.", [("Tung", "Đất rẻ, sát quốc lộ, đền bù xong hết. Trừ một hộ.", "efficient")], ""),
  ("Hộ nào", 3, ["KH2"], "85mm close-up", "@Khang's eyes narrow.", [("Khang", "Hộ nào?", "sharp")], ""),
  ("Bà bán sách", 5, ["TU1"], "50mm medium shot", "@Tung checks his tablet.", [("Tung", "Một bà bán sách. Không chịu ký. Chủ nhật bảy giờ máy vào.", "routine")], ""),
  ("Nhìn bản đồ", 4, ["KH2"], "slow push-in on his face lit by the screen", "@Khang stares at the glowing map for a long time without blinking.", [], ""),
  ("Làng tôi", 4, ["KH2"], "85mm close-up", "@Khang speaks very quietly.", [("Khang", "Cái kho này xây ở làng tôi.", "very quiet")], ""),
  ("Em không biết", 3, ["TU1"], "85mm close-up", "@Tung lowers the tablet.", [("Tung", "Em… không biết.", "caught off guard")], ""),
  ("Hoãn lịch", 4, ["KH2"], "50mm medium shot", "@Khang picks up the old book and his car keys.", [("Khang", "Hoãn hết lịch thứ Bảy.", "decisive")], ""),
  ("Anh đi đâu", 3, ["TU1"], "50mm medium shot", "@Tung half rises from his chair.", [("Tung", "Anh đi đâu?", "alarmed")], ""),
  ("Về nhà", 3, ["KH2"], "medium shot at the glass door, skyline behind", "@Khang stops at the glass door without turning around.", [("Khang", "Về nhà.", "simple")], ""),
])

scene("06", "Về làm gì", "Hồi 2 · Đường về", "trưa thứ Bảy", "B5",
  "a broom on bricks, chickens, a distant village loudspeaker hum, a car engine ticking. No music.", [
  ("Ô tô ngoài cổng", 4, [], "wide shot from inside the yard toward the low brick gate", "A shiny black sedan rolls to a stop outside the old brick gate, dust drifting.", [], ""),
  ("Quét sân", 4, ["BH1"], "50mm medium shot", "@BaHanh keeps sweeping the brick yard with a straw broom and does not look up.", [], ""),
  ("Mẹ", 4, ["KH3"], "medium shot at the gate", "@Khang steps through the gate carrying a small travel bag.", [("Khang", "Mẹ.", "careful")], ""),
  ("Về làm gì", 5, ["BH1"], "85mm close-up, she stops sweeping", "@BaHanh straightens up, broom in hand.", [("BaHanh", "Về làm gì? Về đuổi cô Lan à?", "cold, sharp")], ""),
  ("Không biết", 4, ["KH3"], "85mm close-up", "@Khang takes the hit.", [("Khang", "Con không biết đó là đất làng mình.", "low")], ""),
  ("Ai biết", 4, ["BH1"], "85mm close-up", "@BaHanh stares at him.", [("BaHanh", "Mày không biết thì ai biết?", "bitter")], ""),
  ("Gửi quà", 5, ["KH3", "BH1"], "40mm two-shot across the yard", "@Khang steps closer, trying.", [("Khang", "Năm nào con cũng gửi quà về…", "defensive, soft")], ""),
  ("Người thì không", 4, ["BH1"], "50mm medium shot", "@BaHanh leans the broom on the wall and walks inside.", [("BaHanh", "Ừ. Quà về. Người thì không.", "flat, wounded")], ""),
  ("Hàng hộp đỏ", 5, [], "slow dolly along the top of a dark wooden cabinet", "A neat row of small red velvet jewellery boxes, unopened, coated in dust, lined up on top of an old wooden cabinet.", [], ""),
  ("Khang đứng lặng", 4, ["KH3"], "85mm close-up in the dim central room", "@Khang stands in the doorway looking at the row of boxes.", [], ""),
  ("Bụi trên tay", 4, ["KH3"], "insert close-up", "@Khang lifts one red box; dust comes away on his fingertips; the box has never been opened.", [], ""),
  ("Rửa tay", 4, ["BH1"], "50mm medium shot in the kitchen doorway, her back half turned", "@BaHanh stands in the smoky kitchen doorway, not looking at him.", [("BaHanh", "Vào mà rửa tay. Cơm sắp chín.", "gruff, softening")], ""),
])

scene("07", "Hiệu sách cuối cùng", "Hồi 2 · Đường về", "chiều thứ Bảy", "B3",
  "packing tape screeching, a slow ceiling fan, the market outside. No music.", [
  ("Dán thùng", 5, ["CL1"], "50mm medium shot among cardboard boxes", "@CoLan tapes a cardboard box shut and does not look up.", [("CoLan", "Đóng cửa rồi. Ai cần sách thì cứ lấy, để máy ủi nó cũng phí.", "brisk, bitter")], ""),
  ("Cô Lan", 3, ["KH3"], "medium shot in the doorway", "@Khang stands in the doorway.", [("Khang", "Cô Lan.", "gentle")], ""),
  ("Thằng đọc chùa", 5, ["CL1"], "85mm close-up, she lifts her glasses", "@CoLan squints at him over her reading glasses, then her face changes.", [("CoLan", "Khang đấy à? Cái thằng đọc chùa.", "amazed, then teasing")], ""),
  ("Cháu đây", 3, ["KH3"], "85mm close-up", "@Khang laughs despite himself.", [("Khang", "Vâng. Cháu đây.", "warm")], ""),
  ("Trả nợ", 4, ["KH3", "CL1"], "40mm two-shot across the counter", "@Khang steps up to the counter.", [("Khang", "Cháu về trả nợ.", "half joking")], ""),
  ("Hất hàm", 3, ["CL1"], "50mm medium shot", "@CoLan jerks her chin toward the wall behind her.", [], ""),
  ("Giấy nợ trên tường", 4, [], "macro close-up", "A small yellowed scrap of paper with faded unreadable handwriting, pinned to a wall with a rusty drawing pin, curling at the corners.", [], ""),
  ("Lãi hai lăm năm", 5, ["CL1"], "85mm close-up", "@CoLan folds her arms.", [("CoLan", "Ba nghìn. Lãi hai lăm năm, cháu tự tính.", "deadpan")], ""),
  ("Chạm tờ giấy", 4, ["KH3"], "close-up", "@Khang reaches past the counter and touches the old paper with one finger.", [], ""),
  ("Máy ủi của công ty cháu", 5, ["CL1"], "85mm close-up, slow push-in", "@CoLan goes back to taping a box.", [("CoLan", "Mà về đúng lúc đấy. Sáng mai máy ủi của công ty cháu vào.", "casual, cutting")], ""),
  ("Cô biết", 3, ["KH3"], "85mm close-up", "@Khang turns to her, stricken.", [], ""),
  ("Cả làng biết", 5, ["CL1"], "85mm close-up", "@CoLan rips off another strip of tape.", [("CoLan", "Cả làng biết. Chỉ có ông chủ là không biết.", "dry, cutting")], ""),
])

scene("08", "Cô giữ cho cháu", "Hồi 2 · Đường về", "chiều thứ Bảy, tiếp liền cảnh 07", "B3",
  "flip-flops on tiles, the ceiling fan, a moped passing. No music.", [
  ("Mai bước vào", 4, ["MA1"], "wide shot from behind the counter toward the bright doorway", "@Mai hurries in from the street, sweaty, a sack slung on her shoulder.", [], ""),
  ("Cô giữ cho cháu", 5, ["MA1", "CL1"], "over-the-shoulder shot from behind Mai onto the counter", "@Mai sets a pile of crumpled small banknotes and coins on the glass counter.", [("Mai", "Cô ơi, cô giữ cuốn này cho cháu mấy hôm được không ạ?", "hopeful, breathless")], ""),
  ("Đóng cửa rồi", 3, ["CL1"], "85mm close-up", "@CoLan sighs.", [("CoLan", "Mai đóng cửa rồi cháu.", "gentle")], ""),
  ("Trả dần", 4, ["MA1"], "85mm close-up", "@Mai refuses to give up.", [("Mai", "Thế cô bán cho cháu, cháu trả dần.", "stubborn")], ""),
  ("Có đứa nói rồi", 5, ["CL1"], "85mm close-up, she glances past Mai", "@CoLan glances over the girl's shoulder at the man in the corner.", [("CoLan", "Câu này… hai mươi lăm năm trước có đứa nói rồi.", "quiet, meaningful")], ""),
  ("Khang nghe", 3, ["KH3"], "85mm close-up by the shelves", "@Khang stands very still by the shelves.", [], ""),
  ("Đếm lại", 4, ["MA1"], "insert close-up on her hands, then her face", "@Mai recounts her coins.", [("Mai", "Mười tám… mười chín… thiếu à?", "dismayed")], ""),
  ("Cuốn sách xanh", 3, ["MA1"], "close-up", "@Mai hugs a new blue-covered programming book to her chest.", [], ""),
  ("Chú nhường cháu", 5, ["MA1", "KH3"], "40mm two-shot", "@Mai turns to @Khang, not knowing who he is.", [("Mai", "Chú cũng mua sách à? Chú nhường cháu cuốn này nhé.", "cheeky")], ""),
  ("Cháu cầm đi", 3, ["KH3"], "85mm close-up", "@Khang nods slowly.", [("Khang", "Ừ. Cháu cầm đi.", "soft")], ""),
  ("Viết giấy nợ", 4, ["CL1"], "50mm medium shot", "@CoLan slides a slip of paper and a pen across the counter, eyes on Khang.", [("CoLan", "Cầm về. Viết giấy nợ.", "dry, knowing")], ""),
  ("Viết ngay", 3, ["MA1"], "medium shot", "@Mai grabs the pen with a grin.", [("Mai", "Cháu viết ngay!", "delighted")], ""),
])

scene("09", "Bãi ve chai", "Hồi 2 · Đường về", "chiều muộn thứ Bảy", "B6",
  "bicycle chain, cans clattering, frogs in the paddies, wind. No music.", [
  ("Đạp xe ve chai", 4, ["MA2"], "wide tracking shot along a village road between rice fields", "@Mai pedals an old bicycle loaded with sacks of cans.", [], ""),
  ("Đợi chú", 3, ["KH3"], "medium tracking shot", "@Khang walks fast behind her in his loafers.", [("Khang", "Cháu ơi, đợi chú với.", "slightly out of breath")], ""),
  ("Không bán", 4, ["MA2"], "50mm medium shot, she brakes", "@Mai stops and looks back suspiciously.", [("Mai", "Chú định mua lại sách à? Không bán đâu.", "suspicious, cheeky")], ""),
  ("Đỗ đại học", 5, ["MA2"], "50mm medium shot at the scrap yard scale", "@Mai hangs a sack of cans on the old scale, proud.", [("Mai", "Cháu đỗ đại học ngành máy tính. Thứ Hai nhập học.", "proud")], ""),
  ("Còn thiếu", 5, ["MA2"], "85mm close-up", "@Mai reads the scale and her face falls.", [("Mai", "Còn thiếu tiền vé với học phí kỳ đầu.", "matter-of-fact")], ""),
  ("Sao không vay", 3, ["KH3"], "85mm close-up", "@Khang leans on a post.", [("Khang", "Sao không vay?", "gentle")], ""),
  ("Ve chai thì không", 4, ["MA2"], "85mm close-up", "@Mai shrugs.", [("Mai", "Vay thì phải trả. Ve chai thì không.", "blunt")], ""),
  ("Khang bật cười", 3, ["KH3"], "85mm close-up", "@Khang laughs out loud for the first time.", [], ""),
  ("Chỗ đọc sách", 5, ["MA2"], "50mm medium shot, she ties a sack angrily", "@Mai yanks a sack tight.", [("Mai", "Cả làng có mỗi chỗ đọc sách không mất tiền, thế mà nó ủi.", "angry")], ""),
  ("Ông chủ chưa đọc", 5, ["MA2"], "85mm close-up", "@Mai spits the words.", [("Mai", "Ông chủ cái công ty kho ấy chắc cả đời chưa đọc quyển nào.", "contemptuous")], ""),
  ("Khang nhăn mặt", 3, ["KH3"], "85mm close-up", "@Khang winces and says nothing.", [], ""),
  ("Chú tên gì", 3, ["MA2", "KH3"], "40mm two-shot", "@Mai looks him up and down.", [("Mai", "Mà chú tên gì?", "curious")], ""),
  ("Khang", 3, ["KH3"], "85mm close-up", "@Khang hesitates.", [("Khang", "Khang.", "reluctant")], ""),
  ("Xui nhỉ", 4, ["MA2"], "50mm medium shot", "@Mai bursts out laughing and swings onto her bicycle.", [("Mai", "Trùng tên ông chủ công ty đấy. Xui nhỉ.", "laughing")], ""),
])

scene("10", "Đêm lũ", "Hồi 2 · Đường về", "tối thứ Bảy; hồi tưởng năm Khang 24 tuổi", "B5",
  "crickets, rain drumming in the memory, water sloshing, a dial tone. No music.", [
  ("Gỡ khăn phủ", 4, ["KH3"], "50mm medium shot in the dim central room", "@Khang lifts a dusty cloth off an old beige computer and CRT monitor; dust drifts in the bulb light.", [], ""),
  ("Năm lũ", 4, ["BH1"], "50mm medium shot", "@BaHanh sets a tray of rice and vegetables on the mat.", [("BaHanh", "Còn nhớ năm lũ không?", "quiet")], ""),
  ("Nước tràn", 4, ["KY2"], "wide shot, flashlight beams in muddy water", "Muddy water pours into the rented room; @KhangTre wades in, knee-deep.", [], "B7"),
  ("Ổ cứng trước", 4, ["KY2"], "handheld-feel medium shot, flashlight", "@KhangTre lifts a computer tower out of the water toward the loft ladder.", [("KhangTre", "Ổ cứng trước! Cứu ổ cứng trước!", "shouting, desperate")], "B7"),
  ("Lội nước", 4, ["KY2"], "medium shot", "@KhangTre hands a dripping computer tower up the ladder to a blurred figure above.", [], "B7"),
  ("Bốt điện thoại", 4, ["KY2"], "medium shot through the glass of a phone booth at grey dawn", "@KhangTre, still soaked, holds the receiver.", [("KhangTre", "Con mất hết rồi mẹ ạ.", "hoarse, broken")], "B7"),
  ("Còn người là còn", 5, ["BHT"], "85mm close-up, an old landline phone at the village house", "@BaHanhTre holds the receiver, calm.", [("BaHanhTre", "Mất máy thì mua máy. Còn người là còn.", "steady, firm")], ""),
  ("Khóc trong bốt", 3, ["KY2"], "85mm close-up through wet glass", "@KhangTre presses his forehead to the booth glass and cries silently.", [], "B7"),
  ("Mẹ nói lại", 4, ["BH1"], "50mm medium shot, present day", "@BaHanh sits down across from Khang.", [("BaHanh", "Mẹ nói câu đấy. Giờ mẹ nói lại.", "gentle for once")], ""),
  ("Đôi bông tai năm ấy", 5, ["KH3"], "85mm close-up", "@Khang finally asks.", [("Khang", "Mẹ… đôi bông tai năm ấy…", "hesitant")], ""),
  ("Ăn cơm đi", 3, ["BH1"], "85mm close-up", "@BaHanh cuts him off exactly as she did years ago.", [("BaHanh", "Ăn cơm đi.", "firm")], ""),
  ("Ăn cơm im lặng", 4, ["KH3", "BH1"], "wide shot of the mat, the old computer behind them", "@Khang and @BaHanh eat in silence; she drops a piece of fish into his bowl without looking.", [], ""),
])

scene("11", "Tùng về làng", "Hồi 2 · Đường về", "tối thứ Bảy", "B5",
  "crickets, a car engine idling, a dog barking far away. No music.", [
  ("Đèn pha", 3, [], "wide shot of the dark lane", "Car headlights sweep across the old brick gate and the jackfruit tree.", [], ""),
  ("Tùng xuống xe", 3, ["TU2"], "medium shot by the car", "@Tung climbs out of a car, windbreaker thrown on in a hurry.", [("Tung", "Anh.", "tense")], ""),
  ("Một câu", 5, ["TU2"], "50mm medium shot at the gate", "@Tung speaks low under the porch bulb.", [("Tung", "Bên kia biết anh về đây. Họ chỉ hỏi: sáng mai máy có vào không.", "urgent")], ""),
  ("Nếu không", 3, ["KH3"], "85mm close-up", "@Khang folds his arms.", [("Khang", "Nếu không?", "calm")], ""),
  ("Hạ giá", 4, ["TU2"], "85mm close-up", "@Tung spreads his hands.", [("Tung", "Họ hạ hai mươi phần trăm. Hoặc thôi.", "blunt")], ""),
  ("Mười hai năm", 5, ["TU2"], "85mm close-up, slow push-in", "@Tung drops his voice and his guard.", [("Tung", "Anh, em theo anh mười hai năm. Em có hai đứa con.", "personal, quiet")], ""),
  ("Chữ ký thứ Hai", 4, ["TU2"], "85mm close-up", "@Tung looks away.", [("Tung", "Quyền chọn của em nằm ở chữ ký thứ Hai.", "ashamed but honest")], ""),
  ("Đến sáng mai", 4, ["KH3"], "50mm medium shot", "@Khang looks off toward the dark market road.", [("Khang", "Cho tôi đến sáng mai.", "quiet")], ""),
  ("Bảy giờ máy nổ", 5, ["TU2"], "medium shot, he opens the car door", "@Tung pauses with one hand on the car door.", [("Tung", "Bảy giờ sáng máy nổ. Anh không nói gì là nó chạy.", "flat, final")], ""),
  ("Bà nghe", 3, ["BH1"], "85mm close-up behind a half-open wooden door", "@BaHanh stands behind the door in the dark, listening.", [], ""),
  ("Bánh mì", 4, ["TU2"], "medium shot by the open car door", "@Tung hesitates, then pulls a paper-wrapped bánh mì from his jacket pocket and holds it out.", [("Tung", "Anh ăn gì chưa? Em mua bánh mì đây.", "awkward, kind")], ""),
  ("Nhận bánh mì", 3, ["KH3"], "85mm close-up", "@Khang takes the bánh mì and almost laughs.", [], ""),
])

scene("12", "Cái ngăn kéo", "Hồi 2 · Đường về", "đêm thứ Bảy", "B3",
  "the ceiling fan, a distant karaoke, crickets. No music.", [
  ("Một mình", 4, ["CL1"], "wide shot, a single desk lamp among boxes", "@CoLan sits alone among taped boxes, the shop dark except for one warm desk lamp.", [], ""),
  ("Gõ cửa kính", 3, ["KH3"], "medium shot through the glass door at night", "@Khang knocks softly on the glass door.", [], ""),
  ("Biết cháu đến", 4, ["CL1"], "50mm medium shot", "@CoLan unlocks the door without surprise.", [("CoLan", "Biết thế nào cháu cũng đến.", "tired, knowing")], ""),
  ("Mở ngăn kéo", 4, ["CL1"], "close-up behind the counter", "@CoLan unlocks a small drawer under the counter with a tiny key.", [], ""),
  ("Túi vải", 3, [], "macro close-up on the glass counter", "A small faded cloth pouch tied with red thread is set down on the glass counter under the lamp.", [], ""),
  ("Đôi bông tai", 4, ["KH3"], "close-up on his hands, then his face", "@Khang unties the pouch; two small old gold hoop earrings tumble into his palm.", [], ""),
  ("Cái này là", 3, ["KH3"], "85mm close-up", "@Khang cannot finish.", [("Khang", "Cái này là…", "breaking")], ""),
  ("Cô chuộc lại", 5, ["CL1"], "85mm close-up", "@CoLan takes off her glasses.", [("CoLan", "Hai lăm năm trước mẹ cháu bán ở tiệm vàng đầu chợ. Hôm sau cô chuộc lại.", "plain, gentle")], ""),
  ("Sao không nói", 4, ["KH3"], "85mm close-up", "@Khang looks up, eyes wet.", [("Khang", "Sao cô không nói với cháu?", "hurt")], ""),
  ("Lời hứa", 5, ["CL1"], "85mm close-up, slow push-in", "@CoLan holds his gaze.", [("CoLan", "Mẹ cháu bắt cô hứa. Bao giờ thằng Khang về mà không phải về vì tiền thì trả.", "firm, moved")], ""),
  ("Nắm chặt", 3, ["KH3"], "insert close-up", "@Khang's fist closes tight around the earrings.", [], ""),
  ("Tự biết", 4, ["CL1"], "50mm medium shot", "@CoLan pushes the empty pouch toward him.", [("CoLan", "Cháu về vì gì, cháu tự biết.", "quiet")], ""),
])

scene("13", "Chú là ông chủ", "Hồi 2 · Đường về", "rạng sáng Chủ nhật", "B8",
  "roosters, a distant diesel engine, wind. No music.", [
  ("Trời xám", 4, ["MA1"], "wide shot of the grey market street at dawn", "@Mai wheels her bicycle up to the bookshop, the blue book in her basket.", [], ""),
  ("Chủ tịch", 4, ["TU2", "KH3"], "40mm two-shot in front of the bookshop", "@Tung walks up to @Khang, phone in hand.", [("Tung", "Chủ tịch, đội máy đến đầu chợ rồi.", "businesslike")], ""),
  ("Chủ tịch ư", 3, ["MA1"], "85mm close-up", "@Mai freezes beside her bicycle.", [("Mai", "Chủ… tịch?", "stunned")], ""),
  ("Chú nói đã", 3, ["KH3"], "85mm close-up", "@Khang turns toward her.", [("Khang", "Mai, chú nói…", "urgent")], ""),
  ("Không cần sách", 5, ["MA1"], "50mm medium shot", "@Mai sets the blue book on the bookshop step.", [("Mai", "Cháu không cần sách của người ủi hiệu sách.", "cold, hurt")], ""),
  ("Đạp xe đi", 3, ["MA1"], "wide shot", "@Mai rides away fast down the grey street.", [], ""),
  ("Sách trên bậc cửa", 3, [], "close-up", "A blue-covered book lies alone on a worn concrete step in the grey dawn.", [], ""),
  ("Nhặt sách", 3, ["KH3"], "medium shot", "@Khang crouches and picks up the book.", [], ""),
  ("Con bé nào", 4, ["TU2"], "50mm medium shot", "@Tung watches the girl ride away.", [("Tung", "Con bé nào thế anh?", "puzzled")], ""),
  ("Dám mắng tôi", 4, ["KH3"], "85mm close-up, he dusts off the book", "@Khang dusts off the book with his sleeve.", [("Khang", "Người duy nhất dám mắng tôi tuần này.", "wry")], ""),
  ("Khói đen", 4, [], "wide shot down the street", "At the end of the market street a yellow bulldozer roars to life, black diesel smoke rising into the grey sky.", [], ""),
])

scene("14", "Bảy giờ sáng", "Hồi 3 · Trao tay", "7 giờ sáng Chủ nhật", "B8",
  "diesel engine idling, murmuring villagers, a page turning. No music.", [
  ("Gầu máy ủi", 4, [], "low wide shot", "A yellow bulldozer bucket stops with a jolt an arm's length from the bookshop door.", [], ""),
  ("Ngồi đọc sách", 4, ["CL1"], "50mm medium shot", "@CoLan sits on a low plastic stool right in the doorway, reading glasses on, calmly reading a book.", [], ""),
  ("Cô tránh ra", 4, ["TH1"], "medium shot", "@Thang jumps down from the bulldozer and walks over, scratching his neck.", [("Thang", "Cô ơi, cô tránh ra cho cháu làm.", "polite, awkward")], ""),
  ("Đọc nốt chương", 4, ["CL1"], "85mm close-up", "@CoLan turns a page without looking up.", [("CoLan", "Cháu cứ làm. Cô đọc nốt chương này.", "serene")], ""),
  ("Mua truyện ở đây", 4, ["TH1"], "85mm close-up", "@Thang takes off his hard hat and scratches his head.", [("Thang", "Hồi bé cháu cũng mua truyện ở đây đấy cô.", "sheepish")], ""),
  ("Đọc chùa nhiều", 3, ["CL1"], "85mm close-up", "@CoLan peers at him over her glasses.", [("CoLan", "Mua ít, đọc chùa nhiều.", "deadpan")], ""),
  ("Người làng", 4, [], "wide shot", "Villagers in work clothes gather at a distance, murmuring, some holding bicycles.", [], ""),
  ("Một câu", 4, ["TU2", "KH3"], "40mm two-shot at the edge of the crowd", "@Tung speaks into @Khang's ear.", [("Tung", "Anh nói một câu, máy chạy.", "low")], ""),
  ("Khang nhìn", 3, ["KH3"], "85mm close-up", "@Khang watches the old woman reading in the doorway.", [], ""),
  ("Ghế thứ hai", 4, ["KH3"], "medium shot", "@Khang picks up a second low plastic stool from a neighbour's porch.", [], ""),
  ("Ngồi cạnh", 4, ["KH3", "CL1"], "50mm two-shot in the doorway", "@Khang sets the stool beside @CoLan and sits down next to her; she glances at him and almost smiles.", [], ""),
])

scene("15", "Hai cái ghế", "Hồi 3 · Trao tay", "tiếp liền cảnh 14", "B8",
  "the bulldozer engine, then silence, birds returning. No music.", [
  ("Hai cái ghế", 3, ["KH3", "CL1"], "low close-up on two plastic stools side by side, the bulldozer bucket behind", "@Khang and @CoLan sit side by side on two stools.", [], ""),
  ("Tắt máy", 3, ["KH3"], "85mm close-up", "@Khang looks up at the foreman.", [("Khang", "Anh Thắng, tắt máy.", "calm")], ""),
  ("Ai trả tiền", 4, ["TH1"], "50mm medium shot", "@Thang blinks.", [("Thang", "Thế ai trả tiền ca máy hôm nay?", "confused")], ""),
  ("Tôi", 3, ["KH3"], "85mm close-up", "@Khang does not hesitate.", [("Khang", "Tôi.", "simple")], ""),
  ("Máy tắt", 3, [], "wide shot", "The bulldozer engine coughs and dies; the black smoke thins in the grey air.", [], ""),
  ("Đi ăn sáng", 4, ["TH1"], "50mm medium shot", "@Thang takes off his hard hat and grins at the old woman.", [("Thang", "Thế thì cháu đi ăn sáng đã cô nhé.", "relieved, cheerful")], ""),
  ("Người làng xì xào", 4, [], "wide shot of the crowd", "Villagers murmur and smile; a few clap awkwardly; an old man laughs.", [], ""),
  ("Anh biết không", 4, ["TU2"], "85mm close-up", "@Tung stares at Khang.", [("Tung", "Anh biết anh vừa làm gì không?", "shaken")], ""),
  ("Lần đầu", 4, ["KH3"], "85mm close-up", "@Khang nods.", [("Khang", "Biết. Lần đầu sau mười năm.", "quiet, certain")], ""),
  ("Mai trong đám đông", 4, ["MA1"], "85mm close-up among blurred villagers", "@Mai stands in the crowd holding her bicycle, watching, her anger cracking.", [], ""),
  ("Chương này hay", 4, ["CL1"], "50mm medium shot", "@CoLan closes her book.", [("CoLan", "Chương này hay đấy.", "dry, pleased")], ""),
  ("Bên kia", 3, ["TU2"], "medium shot", "@Tung's phone rings; he looks at the screen.", [("Tung", "Bên kia.", "tense")], ""),
])

scene("16", "Cuộc gọi", "Hồi 3 · Trao tay", "tiếp liền cảnh 15", "B8",
  "distant market sounds, birds, a phone ringtone. No music.", [
  ("Áp điện thoại vào ngực", 4, ["TU2"], "50mm medium shot at a quiet corner of the market", "@Tung presses the ringing phone against his chest.", [("Tung", "Họ hỏi máy đã vào chưa.", "tense")], ""),
  ("Không xây ở đây", 5, ["KH3"], "85mm close-up", "@Khang speaks evenly.", [("Khang", "Nói với họ: kho phía Bắc không xây ở đây. Giá thế nào thì thế.", "calm, decided")], ""),
  ("Họ sẽ rút", 3, ["TU2"], "85mm close-up", "@Tung shakes his head.", [("Tung", "Họ sẽ rút.", "grim")], ""),
  ("Để họ rút", 3, ["KH3"], "85mm close-up", "@Khang shrugs.", [("Khang", "Thì để họ rút.", "light")], ""),
  ("Im lặng", 3, ["TU2"], "85mm close-up, slow push-in", "@Tung is silent for a long beat.", [], ""),
  ("Em tính rồi", 5, ["TU2"], "85mm close-up", "@Tung breaks into a tired grin.", [("Tung", "Anh biết không, em tính rồi. Bỏ kho này đi, mình vẫn lãi.", "relieved")], ""),
  ("Chưa ai dám", 4, ["TU2"], "85mm close-up", "@Tung shakes his head at himself.", [("Tung", "Chỉ là chưa ai dám nói với anh.", "rueful")], ""),
  ("Cậu", 3, ["KH3"], "85mm close-up", "@Khang stares at him, then laughs.", [("Khang", "Cậu…", "laughing")], ""),
  ("Gọi về nhà", 5, ["TU2"], "50mm medium shot, he steps aside with a second phone", "@Tung calls home on a second phone, turning away, softer.", [("Tung", "Bố về muộn tí. Ừ, chủ nhật bố đi xem con đá bóng.", "tender")], ""),
  ("Chín giờ mai", 5, ["TU2"], "50mm medium shot", "@Tung lifts the phone to his ear, formal again.", [("Tung", "Vâng, chín giờ sáng mai. Chủ tịch sẽ có mặt.", "formal")], ""),
  ("Tự nói", 4, ["TU2", "KH3"], "40mm two-shot", "@Tung lowers the phone and looks at @Khang.", [("Tung", "Ký hay không, mai anh tự nói.", "warm")], ""),
])

scene("17", "Mẹ đeo lại bông tai", "Hồi 3 · Trao tay", "trưa Chủ nhật", "B5",
  "chopsticks on bowls, chickens outside, a fan whirring. No music.", [
  ("Túi vải trên mâm", 4, ["KH3", "BH1"], "high wide shot over the rice tray on the mat", "@Khang sets the small faded cloth pouch on the rice tray between them.", [], ""),
  ("Cô Lan nói rồi", 4, ["BH1"], "85mm close-up", "@BaHanh stares at the pouch, her hands trembling.", [("BaHanh", "Cô Lan nói rồi à?", "shaky")], ""),
  ("Bán con lợn", 4, ["KH3"], "85mm close-up", "@Khang half smiles.", [("Khang", "Mẹ bảo mẹ bán con lợn.", "gentle teasing")], ""),
  ("Lợn nào", 4, ["BH1"], "85mm close-up", "@BaHanh's mouth twitches.", [("BaHanh", "Nhà mình có nuôi con lợn nào đâu.", "dry, caught")], ""),
  ("Bật cười", 3, ["KH3", "BH1"], "40mm two-shot", "@Khang and @BaHanh burst out laughing together.", [], ""),
  ("Bà khóc", 3, ["BH1"], "85mm close-up", "@BaHanh's laugh turns into tears; she covers her mouth.", [], ""),
  ("Đeo bông tai", 5, ["KH3", "BH1"], "50mm two-shot", "@Khang gently hooks the small gold earrings into his mother's ears.", [], ""),
  ("Bông tai", 3, ["BH1"], "macro close-up", "A small old gold hoop earring catches the light on @BaHanh's ear.", [], ""),
  ("Không vì tiền", 4, ["BH1"], "85mm close-up", "@BaHanh touches the earring.", [("BaHanh", "Con về… không phải vì tiền nhỉ?", "hopeful, fragile")], ""),
  ("Một cuốn sách", 4, ["KH3"], "85mm close-up", "@Khang shakes his head.", [("Khang", "Con về vì một cuốn sách, mẹ ạ.", "soft")], ""),
  ("Đi tìm con bé", 5, ["BH1"], "50mm medium shot", "@BaHanh wipes her eyes and waves him off.", [("BaHanh", "Thế thì đi tìm con bé kia đi. Mai nó lên xe rồi.", "brisk again")], ""),
])

scene("18", "Giấy nợ", "Hồi 3 · Trao tay", "chiều Chủ nhật", "B6",
  "cans clinking, wind over the paddies, a distant bus horn. No music.", [
  ("Đếm tiền", 4, ["MA2"], "50mm medium shot", "@Mai sits on a bulging sack of cans counting small banknotes, again.", [("Mai", "Thiếu. Vẫn thiếu.", "tired")], ""),
  ("Đặt sách", 4, ["KH3", "MA2"], "40mm two-shot", "@Khang sets the blue book down on the sack beside her.", [], ""),
  ("Không nhận", 4, ["MA2"], "85mm close-up", "@Mai does not look at him.", [("Mai", "Cháu bảo rồi, cháu không nhận.", "stubborn")], ""),
  ("Cho mượn", 4, ["KH3"], "85mm close-up", "@Khang crouches to her eye level.", [("Khang", "Chú không cho. Chú cho mượn. Viết giấy nợ.", "gentle")], ""),
  ("Tờ giấy ố vàng", 3, ["KH3"], "insert close-up", "@Khang holds out a small yellowed folded scrap of paper.", [], ""),
  ("Đọc to", 5, ["MA2"], "85mm close-up", "@Mai unfolds the paper and reads aloud, frowning.", [("Mai", "Cháu Khang nợ cô Lan ba nghìn đồng.", "reading slowly")], ""),
  ("Ba nghìn", 3, ["MA2"], "85mm close-up", "@Mai snorts with laughter.", [("Mai", "Ba nghìn?", "laughing")], ""),
  ("Trả cho đứa khác", 5, ["KH3"], "85mm close-up", "@Khang nods.", [("Khang", "Bao giờ thành người thì trả. Không phải trả chú. Trả cho một đứa khác.", "earnest")], ""),
  ("Nhìn sách", 3, ["MA2"], "85mm close-up", "@Mai looks down at the book for a long moment.", [], ""),
  ("Chú trả chưa", 3, ["MA2"], "85mm close-up", "@Mai looks up at him.", [("Mai", "Thế chú đã trả chưa?", "pointed")], ""),
  ("Sáng mai", 3, ["KH3"], "85mm close-up", "@Khang smiles.", [("Khang", "Sáng mai chú trả.", "sure")], ""),
  ("Lãi cao", 4, ["MA2"], "50mm medium shot", "@Mai takes the book and a pen, grinning.", [("Mai", "Cháu viết giấy nợ đây. Ghi lãi cao vào.", "cheeky")], ""),
  ("Mai viết", 4, ["MA2"], "insert close-up on her knee", "@Mai writes a few unreadable lines on a small scrap of paper, tongue between her teeth.", [], ""),
  ("Chú giữ đi", 5, ["MA2", "KH3"], "40mm two-shot", "@Mai holds the scrap of paper out to @Khang.", [("Mai", "Chú giữ đi. Bao giờ cháu thành người thì cháu trả.", "serious, proud")], ""),
])

scene("19", "Chín giờ sáng thứ Hai", "Hồi 3 · Trao tay", "9 giờ sáng thứ Hai", "B1",
  "air-conditioning hum, pages turning, a pen uncapped. No music.", [
  ("Điện thoại nằm ngửa", 3, [], "macro close-up on the walnut table", "A black smartphone lies face up on the polished table, screen dark.", [], ""),
  ("Phòng họp", 4, ["KH2", "TU1"], "wide shot down the table; two dark-suited figures seen only from behind on the near side", "@Khang and @Tung sit across from two foreign businessmen seen only from behind, out of focus.", [], ""),
  ("Bản cuối", 3, ["TU1"], "50mm medium shot", "@Tung slides a contract across the table.", [("Tung", "Bản cuối, anh.", "neutral")], ""),
  ("Bỏ kho", 5, ["KH2"], "85mm close-up", "@Khang uncaps a pen.", [("Khang", "Ký. Bỏ kho phía Bắc ra khỏi hợp đồng.", "steady")], ""),
  ("Phần của tôi", 4, ["KH2"], "85mm close-up", "@Khang taps the contract.", [("Khang", "Phần chênh lệch trừ vào phần của tôi.", "simple")], ""),
  ("In sẵn", 4, ["TU1"], "50mm medium shot", "@Tung flips open a second, ready-made contract and smiles.", [("Tung", "Em in sẵn bản này từ hôm qua rồi.", "smug, fond")], ""),
  ("Họ hỏi vì sao", 5, ["TU1"], "50mm medium shot, leaning toward Khang", "@Tung listens to a murmur from across the table, then leans to @Khang.", [("Tung", "Họ hỏi vì sao anh bỏ kho. Em trả lời thế nào?", "curious")], ""),
  ("Vì một hiệu sách", 4, ["KH2"], "85mm close-up", "@Khang does not look up from the contract.", [("Khang", "Bảo họ: vì tôi còn nợ một hiệu sách.", "simple")], ""),
  ("Ký", 4, ["KH2"], "insert close-up on the pen and paper", "@Khang signs an unreadable signature on the last page.", [], ""),
  ("Hẹn trả nợ", 4, ["KH2"], "50mm medium shot, he stands", "@Khang stands, buttons his jacket and picks up the old blue book.", [("Khang", "Tôi xin phép. Tôi có hẹn trả nợ.", "light")], ""),
  ("Tùng nhìn theo", 3, ["TU1"], "85mm close-up", "@Tung watches him go, smiling.", [], ""),
])

scene("20", "Phòng máy ở hiệu sách", "Hồi 3 · Trao tay", "vài tuần sau", "B10",
  "keyboards clicking, soft laughter, the ceiling fan, a bicycle bell outside. No music.", [
  ("Hiệu sách mới", 5, [], "slow wide dolly through the open shopfront", "The old bookshop reopened: pale-green shelves full of books on one side, a row of new computers on the other, warm sunlight.", [], ""),
  ("Thanh niên ngồi máy", 4, [], "medium shot along the computer tables", "Young adult villagers in work clothes type at the computers, faces lit by the screens.", [], ""),
  ("Lãi cao quá", 5, ["CL2", "BH2"], "40mm two-shot behind the counter", "@CoLan and @BaHanh sit side by side behind the glass counter; @BaHanh wears small gold earrings.", [("CoLan", "Ba nghìn, trả bằng cả cái phòng máy. Lãi cao quá.", "delighted")], ""),
  ("Học ai", 3, ["BH2"], "85mm close-up", "@BaHanh touches her earring and sniffs.", [("BaHanh", "Nó học ai mà hào phóng thế.", "proud, gruff")], ""),
  ("Giấy nợ đóng khung", 3, [], "macro close-up", "A small yellowed scrap of paper with unreadable faded handwriting, now framed behind glass on the wall.", [], ""),
  ("Cháu đi đây", 4, ["MA3"], "medium shot by the door", "@Mai shoulders a new backpack, ready to leave.", [("Mai", "Cháu đi đây ạ.", "excited, nervous")], ""),
  ("Của cháu đây", 4, ["KH4", "MA3"], "40mm two-shot", "@Khang holds out the old dog-eared blue book.", [("Khang", "Của cháu đây.", "warm")], ""),
  ("Giữ cho ai", 3, ["MA3"], "85mm close-up", "@Mai takes the book in both hands.", [("Mai", "Cháu giữ cho ai ạ?", "curious")], ""),
  ("Đứa nói câu ấy", 4, ["KH4"], "85mm close-up", "@Khang smiles.", [("Khang", "Cho đứa nào nói câu ấy với cháu.", "gentle")], ""),
  ("Anh Thắng đăng ký", 4, ["TH1"], "medium shot in the doorway", "@Thang leans in the doorway, hard hat under his arm.", [("Thang", "Cô ơi, cho cháu đăng ký học máy tính với!", "eager")], ""),
  ("Miễn phí", 4, ["CL2"], "85mm close-up", "@CoLan waves him in.", [("CoLan", "Đăng ký thì miễn phí. Đọc chùa cũng miễn phí.", "teasing")], ""),
  ("Cô gái lạ", 5, ["CoGai"], "over-the-shoulder shot toward the counter", "A young woman of 19 sets a few crumpled small banknotes on the counter and holds up a blue book, toward a young woman behind the counter.", [("CoGai", "Chị ơi, chị giữ cuốn này cho em mấy hôm được không ạ?", "hopeful, shy")], ""),
  ("Mai quay lại", 4, ["MA3"], "85mm close-up", "@Mai turns around, looks back at Khang, and breaks into a grin.", [], ""),
  ("Khang cười", 3, ["KH4"], "85mm close-up", "@Khang laughs quietly.", [], ""),
  ("Hoàng hôn", 5, [], "wide shot from the village road at sunset", "The little bookshop glows warm in the dusk; a bicycle rings its bell as it passes.", [], ""),
])
