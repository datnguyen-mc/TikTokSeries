# -*- coding: utf-8 -*-
"""Dữ liệu phim Chị Ơi, Đến Rồi: nhân vật theo bộ đồ, bối cảnh, 20 cảnh và bảng shot.
Sửa ở đây rồi chạy build.py để sinh NHAN_VAT_FLOW.md, SHOTS.md, kich-ban/, film/cXX/*.txt."""

TITLE = "Chị Ơi, Đến Rồi"

# ---------------------------------------------------------------- người: khuôn mặt + giọng
PEOPLE = {
    "Hung": dict(name="Hưng", role="the driver of the last night bus",
        face="a lean 32-year-old Vietnamese man, warm tan skin, gentle narrow eyes with faint laugh lines, short slightly untidy black hair, light stubble, a shy lopsided smile",
        voice="man of 32, soft warm baritone, talks quietly as if to himself, gentle humour"),
    "An": dict(name="An", role="a hospital nurse who rides the last bus home",
        face="a slender 28-year-old Vietnamese woman, pale tired oval face, delicate features, dark eyes with faint shadows under them, shoulder-length straight black hair tucked behind her ears, a small mole under her left eye",
        voice="woman of 28, soft low alto, few words, warm"),
    "OngThu": dict(name="Ông Thư", role="an old retired tram driver who rides the night bus",
        face="a thin, upright 78-year-old Vietnamese man, sharp clean-shaven face with deep lines, neatly combed thin white hair, bushy white eyebrows, clear wry eyes",
        voice="man of 78, dry slow voice with a slight tremor, wry"),
    "OngThuTre": dict(name="Ông Thư lúc trẻ", role="young Thư, a night tram driver fifty years ago",
        face="a lean 28-year-old Vietnamese man, sharp clean-shaven face, thick black hair combed back, bushy black eyebrows, earnest shy eyes",
        voice="man of 28, warm shy tenor"),
    "BaNguyetTre": dict(name="Bà Nguyệt lúc trẻ", role="young Nguyệt, a nurse fifty years ago",
        face="a slender 24-year-old Vietnamese woman, soft oval face, long black hair in a low braid, gentle sleepy eyes, a dimple in her left cheek when she smiles",
        voice="woman of 24, soft clear voice, sleepy and teasing"),
    "BaNguyet": dict(name="Bà Nguyệt", role="Thư's wife, in a coma, one year ago",
        face="a frail 74-year-old Vietnamese woman, soft oval face with fine wrinkles, thin white hair, a dimple in her left cheek",
        voice="woman of 74, never speaks"),
    "Tu": dict(name="Anh Tú", role="the night dispatcher at the bus depot",
        face="a plump, round-faced 46-year-old Vietnamese man, thinning black hair, thick black-rimmed glasses, a cheerful double chin, rosy cheeks",
        voice="man of 46, loud jovial voice, talks fast, laughs a lot"),
    "BaLua": dict(name="Bà Lụa", role="Hưng's mother",
        face="a small, plump 63-year-old Vietnamese woman, round cheerful face, short curly greying hair, sharp lively eyes, laugh lines",
        voice="woman of 63, high quick voice, nagging but loving"),
    "Thao": dict(name="Thảo", role="An's roommate and fellow nurse",
        face="a sturdy 28-year-old Vietnamese woman, round face, short bob haircut with straight bangs, big expressive eyes, a wide grin",
        voice="woman of 28, fast loud bright voice, blunt and funny"),
    "BaCu": dict(name="Bà cụ giường bên", role="an elderly patient",
        face="a frail 85-year-old Vietnamese woman, thin white hair, a kind deeply wrinkled face",
        voice="woman of 85, thin warm shaky voice", text_only=True,
        outfit_text="a blue-and-white striped hospital gown and a knitted shawl, sitting up in bed"),
}

# ---------------------------------------------------------------- bộ đồ = nhân vật trên Flow
# code: (người, tên trên Flow, mô tả bộ đồ, cảnh dùng, ghi chú, True = bộ gốc / mã bộ gốc để sửa từ đó)
OUTFITS = {
    "HU1": ("Hung", "Hưng · Đồng phục lái xe", "a navy-blue padded winter bus-driver uniform jacket with no logo or badge, a light-blue collared shirt underneath, dark-navy trousers, black work shoes", "01, 02, 04, 07–09, 11, 13–19", "Tuyến đêm; cả hồi tưởng hai năm trước", True),
    "HU2": ("Hung", "Hưng · Áo phao thường", "an open dark-grey padded jacket over a grey hoodie, faded jeans, white sneakers", "05, 10", "Ở nhà, đi tìm An", "HU1"),
    "HU3": ("Hung", "Hưng · Năm năm sau", "the same navy-blue padded bus-driver uniform jacket with no logo, a hand-knitted grey wool scarf, a light-blue collared shirt, dark-navy trousers, black work shoes", "20", "Năm năm sau", "HU1"),
    "AN1": ("An", "An · Áo dạ về ca", "a long camel wool coat over light-blue hospital scrubs, a cream knitted scarf, white nurse's sneakers, a beige canvas tote bag", "01–03, 06–09, 13–17", "Về chuyến xe cuối; cả hồi tưởng hai năm trước", True),
    "AN2": ("An", "An · Đồ trực", "light-blue hospital scrubs, a short white cardigan, hair tied in a low ponytail, a stethoscope around her neck, white nurse's sneakers", "12", "Trong khoa", "AN1"),
    "AN3": ("An", "An · Đồ ở nhà", "an oversized oatmeal knitted sweater, soft grey pyjama trousers, thick wool socks, hair loose", "09", "Phòng trọ", "AN1"),
    "AN4": ("An", "An · Đi xa", "a dark-navy puffer coat, a faded red hand-knitted scarf, grey hand-knitted wool gloves, black jeans, white sneakers", "18, 19", "Ra sân bay, quàng khăn ông Thư, đeo găng bà Lụa đan", "AN1"),
    "AN5": ("An", "An · Năm năm sau", "an elegant charcoal-grey wool coat, a faded red hand-knitted scarf, worn grey hand-knitted wool gloves, black trousers, ankle boots", "20", "Năm năm sau", "AN1"),
    "OT1": ("OngThu", "Ông Thư · Áo dạ khăn đỏ", "an old dark-brown wool overcoat, a grey wool flat cap, a faded red hand-knitted women's scarf, dark trousers, old polished leather shoes, holding a battered aluminium thermos", "01, 02, 06, 07, 11–15", "Cả hồi tưởng đêm Noel năm ngoái", True),
    "OT2": ("OngThu", "Ông Thư · Năm năm sau", "the same old dark-brown wool overcoat, a grey wool flat cap, a plain grey wool scarf, dark trousers, leaning on a wooden walking cane", "20", "Năm năm sau, chống gậy", "OT1"),
    "OTT": ("OngThuTre", "Ông Thư trẻ · Áo lái tàu điện", "a faded khaki tram-driver's uniform jacket with brass buttons, a matching peaked cap, dark trousers, worn leather shoes", "07, 14", "28 tuổi, hồi tưởng. Tạo từ ảnh OT1, trẻ hơn 50 tuổi", "OT1"),
    "BNT": ("BaNguyetTre", "Bà Nguyệt trẻ · Áo y tá xưa", "an old-fashioned white cotton nurse's uniform dress, a white nurse's cap, a thin dark-blue knitted cardigan, a cloth shoulder bag", "07, 14", "24 tuổi, hồi tưởng năm mươi năm trước", True),
    "BN1": ("BaNguyet", "Bà Nguyệt · Áo bệnh viện", "a blue-and-white striped hospital gown", "12", "74 tuổi, hôn mê. Tạo từ ảnh BNT, già hơn 50 tuổi", "BNT"),
    "TU1": ("Tu", "Anh Tú · Áo phao bến xe", "a puffy olive-green padded jacket over a maroon hand-knitted sweater, a black wool beanie, fingerless gloves, dark trousers", "04, 13, 16, 18", "Chòi điều độ, bộ đàm", True),
    "BL1": ("BaLua", "Bà Lụa · Áo bông ở nhà", "a quilted floral cotton jacket, dark cotton trousers, wool socks with plastic slippers, a cloth apron, hair held in a clip", "05", "Ở nhà", True),
    "BL2": ("BaLua", "Bà Lụa · Áo dài đi lễ", "a dark-red velvet áo dài under an open black wool coat, a white lace veil over her hair, a small rosary in her hand", "14", "Đi lễ nửa đêm", "BL1"),
    "TH1": ("Thao", "Thảo · Đồ trực", "light-blue hospital scrubs, a short white cardigan, hair clipped up, a stethoscope around her neck", "10, 12", "Trong khoa", True),
    "TH2": ("Thao", "Thảo · Đồ ngủ", "a pink fleece pyjama set, fluffy socks, hair in a messy bun", "03, 09, 18", "Phòng trọ", "TH1"),
}

AGE_EDIT = {
    "OTT": "Same man as the attached image, same face shape, bushy eyebrows and features, shown fifty years younger: {face}, wearing {outfit}. Full body, plain light-grey studio background.",
    "BN1": "Same woman as the attached image, same face shape, dimple and features, shown fifty years older: {face}, wearing {outfit}. Full body, plain light-grey studio background.",
}

# ---------------------------------------------------------------- bối cảnh
PLACES = {
    "P1": "Inside an empty mid-size city bus at night in a Northern Vietnamese city in December: worn blue fabric seats in pairs, yellow steel grab poles, a folding front door, warm yellowish ceiling strip lights, windows fogged at the edges with streaks of drizzle, the city sliding past outside in blurred amber streetlights and strings of coloured Christmas fairy lights; a large rectangular rear-view mirror above the windscreen; the driver's seat on the left with a big steering wheel and a small black two-way radio handset on a curly cord clipped to the dashboard; no route numbers or signs anywhere.",
    "P1F": "Inside the same empty city bus at night two years ago: worn blue fabric seats in pairs, yellow grab poles, warm yellowish ceiling lights, rain streaming down the fogged windows, a large rear-view mirror above the windscreen, the driver's seat on the left with a small radio on the dashboard; no Christmas lights outside, only dark wet streets; no signs.",
    "P2": "A covered bus stop in front of the tall wrought-iron gate of a large old city hospital at night: cold drizzle, wet pavement mirroring the lights, bare trees wrapped in tiny white Christmas fairy lights, a worn stone bench beside the gate, a sidewalk tea vendor's low stools under a lamp, the hospital building behind with rows of lit windows; no readable signs.",
    "P2D": "The stone bench beside the tall wrought-iron gate of a large old city hospital at dusk: the sky deep cobalt blue, streetlights and tiny white fairy lights on the bare trees just coming on, dry pavement, the hospital building behind with its first lit windows, a covered bus stop nearby; no readable signs.",
    "P3": "A hospital ward corridor at night: pale green walls, a long nurse station counter with a small decorated Christmas tree and paper snowflakes taped to the glass, patient rooms with half-open doors, soft fluorescent light, a tall corridor window looking down onto the hospital gate and its stone bench far below; no readable signs or charts.",
    "P3F": "A quiet hospital room at night lit by a single warm bedside lamp: an old iron hospital bed with white sheets, a drip stand, a wooden chair pulled close to the bed, a window with blurred Christmas lights far outside, the door half open to the corridor.",
    "P4": "A city bus depot after midnight: rows of parked buses under orange sodium lights, puddles, a small glass dispatcher's booth with a cluttered desk, an electric kettle, instant noodle cups, a tiny plastic Christmas tree with blinking coloured lights, a two-way radio base station with a handset; outside the booth, a cardboard box lined with an old blanket where a brown stray dog nurses four puppies.",
    "P5": "A narrow old tube house in a city alley on a winter morning: a small front room with a low wooden table and plastic stools, a home altar on the wall with a crucifix, a small statue of the Virgin Mary and a framed photo of a man in a driver's uniform (no readable text), a handmade nativity crib of straw and coloured paper on a cabinet, a big pot of sticky rice steaming on a gas stove, grey morning light from the alley.",
    "P6": "A tiny rented room on the top floor of an old alley building at night: a mattress on the floor with a floral blanket, a clothes rack, an open overstuffed suitcase, a desk lamp, a small electric heater glowing orange, a window over wet tin rooftops with distant Christmas lights blinking.",
    "P7": "A quiet bus stop at the mouth of a narrow residential alley at night: a single old street lamp, a closed metal shutter, a sidewalk tea stall packing up its low plastic stools, wet tarmac reflecting the light, a string of coloured Christmas lights across the alley entrance.",
    "P8": "A packed old-city street in front of a large grey stone neo-Gothic cathedral with twin square bell towers on Christmas Eve: thousands of adults in winter coats and red Santa hats, balloon sellers, street vendors, strings of warm lights across the street, jammed motorbikes, the cathedral facade lit warm gold; everyone distant and blurred; no readable signs.",
    "P9": "Inside an old wooden city tram fifty years ago at night: wooden slat benches along the sides, brass handrails, dim yellow bulbs, open windows with wooden frames, the driver's brass controls at the front, a quiet old city outside with few lights and bare trees; no readable signs or numbers.",
    "P9B": "Fifty years ago on Christmas Eve: an old wooden city tram stopped in a dense crowd of adults in old-fashioned wool coats with bicycles, in front of a large grey stone neo-Gothic cathedral with twin bell towers, simple warm lights, old low houses; no readable signs.",
    "P10": "An airport departures drop-off lane just before dawn: a wide glowing glass facade, an empty curb, a few distant taxis, cold blue twilight, the sky just turning pale at the horizon; every sign blurred and unreadable.",
    "P11": "Inside a modern low-floor tram in a snowy European city at dusk: big windows with heavy snow falling outside over old stone buildings and warm street lights, warm interior light, a few passengers blurred in the background; no readable signs or screens.",
    "PS": "A wide city boulevard at night in December, lined with tall bare trees wrapped in white fairy lights, wet asphalt reflecting amber streetlights, old low buildings with a few lit windows, almost no traffic; no readable signs.",
    "PB": "A long empty bridge over a wide dark river at night, a row of streetlamps and strings of Christmas lights reflected in the black water, the far shore a line of soft city lights.",
}

FLASH50 = "This is a memory from fifty years ago: warm sepia-golden grade, faded colours, thicker film grain, softer edges; a period-correct old city, no modern objects."
FLASH_NEAR = "This is a memory: slightly cooler, softer, gently desaturated grade."
PLACE_FLASH = {"P9": FLASH50, "P9B": FLASH50, "P1F": FLASH_NEAR + " Two years ago.", "P3F": FLASH_NEAR + " One year ago."}

BUS_SOUND = "the bus diesel engine humming, windows rattling softly, wipers squeaking now and then, drizzle on the glass, distant motorbike horns. No music."
PLACE_SOUND = {
    "P1": BUS_SOUND,
    "P1F": "the bus engine, heavy rain on the windows, a young woman's muffled sobbing. No music.",
    "P2": "drizzle, distant traffic, a tea vendor's kettle, faint church bells far away. No music.",
    "P2D": "evening traffic, wind in bare branches, faint church bells far away. No music.",
    "P3": "hospital corridor hum, a trolley wheel squeaking, a distant monitor beeping, soft footsteps. No music.",
    "P3F": "a monitor beeping softly, quiet breathing, church bells very far away. No music.",
    "P4": "the crackle of a two-way radio, an electric kettle, rain dripping from bus roofs, a puppy whimpering. No music.",
    "P7": "a quiet alley at night, drizzle, a distant motorbike, the bus engine idling. No music.",
    "P8": "a huge Christmas Eve crowd, cathedral bells pealing, motorbike horns, vendors calling. No music.",
    "P9": "an old tram's iron wheels clacking and creaking, a small bell ding, a quiet night city. No music.",
    "P9B": "crowd murmur, old bicycle bells, cathedral bells, a tram bell. No music.",
    "P10": "wind, a distant jet engine, an idling bus engine. No music.",
    "P11": "a modern tram humming, the hush of falling snow, a soft door chime. No music.",
    "PS": "the bus engine humming, tyres hissing on wet asphalt, a distant city hush. No music.",
    "PB": "the bus engine humming over a bridge, wind, the hush of the river. No music.",
}

LOOK = ("Feature-film cinematography for a premium Vietnamese romantic drama on cold December nights: shot on ARRI Alexa 35 with Cooke anamorphic/i lenses, 24 fps, 16:9 full frame without letterbox bars; deliberate cinematic blocking with foreground elements and layered depth; motivated practical light (warm bus ceiling lights, streetlamps, Christmas fairy lights) against cool blue night; soft haze in the cold damp air, rich true-to-life Vietnamese skin tones, gentle film halation and fine 35mm grain, shallow depth of field with creamy bokeh of Christmas lights. Restrained, truthful acting with micro-expressions, like an award-winning Asian festival film; never CGI, never a video game, never an advertisement.")

AVOID = ("On-screen text, burned-in subtitles or captions, a TV channel logo or broadcaster bug in any corner of the frame, logos, watermarks, readable writing on paper, tickets, passports, signs, bus route numbers, shop signs, screens or phones; any cut or second camera angle; the same person appearing twice, twins, clones or look-alike doubles (a person seen in a mirror counts as their only appearance); children or minors anywhere, including in crowds; extra people in focus; Santa Claus characters or mascots; distorted hands or fused fingers; face, hair or costume changes; plastic or waxy skin; flashing or cutting to an attached reference portrait or a plain grey studio backdrop; repeated, echoed or stuttered words; an off-screen narrator; background music or singing; snow, except where the place says it is snowing; Southern or Central Vietnamese accents.")

# ---------------------------------------------------------------- cảnh và shot
# shot: (tên, giây tối thiểu, [mã bộ đồ], camera, hành động, [(người, câu, sắc thái)], bối cảnh khác cảnh hoặc "")
S = []
def scene(num, title, act, when, place, sound, shots):
    S.append(dict(num=num, title=title, act=act, when=when, place=place, sound=sound, shots=shots))

A1, A2, A3 = "Hồi 1 · Chuyến đêm", "Hồi 2 · Câu nói lúc ngủ", "Hồi 3 · Chuyến cuối"

# ================================================================ HỒI 1
scene("01", "Chị ơi, đến rồi", A1, "mở đầu: đêm 23 trên xe; rồi đêm 22, trạm bệnh viện", "P1", BUS_SOUND, [
  ("Câu mở đầu", 5, ["HU1"], "50mm medium close-up from the front passenger side on the driver, his eyes lifted to the big rear-view mirror", "@Hung drives the empty night bus, eyes on the rear-view mirror, speaking very softly as if to himself; coloured Christmas lights slide across the windscreen and his face.", [("Hung", "Chị ngủ thì em mới dám nói.", "soft, trembling")], ""),
  ("Em thích chị", 4, ["HU1"], "85mm close-up on the driver, very slow push-in", "@Hung swallows, still looking into the mirror, both hands tight on the wheel.", [("Hung", "Em thích chị.", "barely a whisper")], ""),
  ("Giọt nước mắt", 5, ["AN1"], "100mm extreme close-up on her face against the fogged window at the back of the bus", "@An sits with her eyes closed, head against the cold glass, as if asleep; her eyelids tremble and a single tear slides from her closed eye down her cheek while city lights drift across her face.", [], ""),
  ("Hai đêm trước", 4, [], "wide static shot at street level", "An almost empty city bus with warm lit windows pulls slowly along a drizzly night street strung with Christmas lights; the bus has no readable number or sign.", [], "PS"),
  ("Ông Thư lên xe", 4, ["OT1"], "medium wide shot from inside the bus through the open folding door onto the hospital bus stop", "The folding door opens; @OngThu, in a dark overcoat and a faded red women's scarf, climbs the steps slowly, holding a battered aluminium thermos.", [("OngThu", "Chào cậu lái.", "dry, friendly")], ""),
  ("Bà thế nào", 4, ["HU1"], "50mm medium shot on the driver from the aisle", "@Hung turns to the old man with a warm smile.", [("Hung", "Hôm nay bà thế nào hả ông?", "warm")], ""),
  ("Bà nhìn tôi lâu lắm", 5, ["OT1"], "85mm close-up", "@OngThu settles into the first seat right behind the driver, straightens the red scarf and smiles to himself.", [("OngThu", "Khá hơn. Hôm nay bà nhìn tôi lâu lắm.", "gentle, a little too bright")], ""),
  ("Cô gái chạy tới", 4, ["AN1"], "medium wide shot from inside the bus through the windscreen toward the stop", "@An runs through the drizzle toward the bus, a camel coat thrown over light-blue nurse scrubs, a canvas tote bag on her shoulder, hair damp.", [], ""),
  ("Ghế cuối", 5, ["AN1"], "wide shot down the aisle from the driver's position toward the back", "@An walks down the empty aisle without looking at anyone, sits in the last row by the right-hand window, hugs her tote bag, leans her head on the glass and closes her eyes.", [], ""),
  ("Lại ngủ", 4, ["OT1", "HU1"], "50mm two-shot from the front: the driver in the foreground, the old man in the first seat behind him", "@OngThu leans forward toward the driver and nods toward the back of the bus.", [("OngThu", "Cô ấy lại ngủ rồi.", "amused"), ("Hung", "Ca chiều mệt mà ông.", "quiet")], ""),
  ("Vặn nhỏ đài", 4, ["HU1"], "insert close-up on the dashboard and the mirror", "@Hung's hand turns the volume knob of the small dashboard radio all the way down, then reaches up and tilts the big rear-view mirror a few degrees.", [], ""),
  ("Cái gương", 4, ["HU1", "AN1"], "close-up over the driver's shoulder onto the rear-view mirror", "Over @Hung's shoulder, the rear-view mirror holds the small distant reflection of @An asleep against the window in the last row; @An is seen only in the mirror.", [], ""),
  ("Hai năm rồi", 4, ["OT1"], "85mm close-up", "@OngThu watches the driver with a sly sideways look.", [("OngThu", "Cái gương ấy, cậu chỉnh hai năm rồi đấy.", "sly, dry")], ""),
  ("Giả điếc", 4, ["HU1"], "85mm close-up", "@Hung keeps his eyes on the road, pretending not to hear, the corner of his mouth twitching.", [], ""),
])

scene("02", "Ngủ Gật", A1, "đêm 22, tiếp liền", "P1", BUS_SOUND, [
  ("Ông xuống xe", 4, ["OT1", "HU1"], "medium shot at the open folding door", "@OngThu stands on the step at the open door and lifts his thermos slightly in farewell; @Hung nods from the driver's seat.", [("OngThu", "Mai tôi lại đi.", "dry"), ("Hung", "Ông về cẩn thận.", "warm")], ""),
  ("Chỉ còn hai người", 4, ["HU1", "AN1"], "wide shot from the very back of the bus toward the driver", "The bus is empty except for @An asleep in the last row in the foreground and @Hung driving far ahead in the warm cabin light.", [], ""),
  ("Bắt đầu kể", 5, ["HU1"], "50mm medium side shot on the driver", "@Hung clears his throat and starts talking softly toward the mirror, the way one talks to a sleeping friend.", [("Hung", "Hôm nay phố nhà thờ treo đèn kín rồi chị ạ.", "soft, chatty")], ""),
  ("Nghe", 4, ["AN1"], "100mm close-up at the back window", "@An, eyes closed, head on the glass; the faintest smile at the corner of her lips.", [], ""),
  ("Chó đẻ", 4, ["HU1"], "50mm medium shot", "@Hung lowers his voice as if sharing big news.", [("Hung", "Con chó ở bến cuối đẻ rồi. Bốn con.", "pleased, conspiratorial")], ""),
  ("Ngủ Gật", 4, ["HU1"], "85mm close-up", "@Hung glances up at the mirror.", [("Hung", "Em đặt tên một con là Ngủ Gật.", "deadpan")], ""),
  ("Không phải theo chị", 4, ["HU1"], "85mm close-up", "@Hung looks away from the mirror quickly.", [("Hung", "Không phải theo chị đâu.", "quick, embarrassed")], ""),
  ("Cắn môi", 4, ["AN1"], "100mm close-up", "@An presses her lips together hard to keep from laughing, eyes still shut.", [], ""),
  ("Định kể", 4, ["HU1"], "50mm medium shot", "@Hung opens his mouth, hesitates, and shakes his head.", [("Hung", "Em còn định… thôi, mai em kể.", "hesitant")], ""),
  ("Đến trạm", 4, ["HU1"], "medium shot from the aisle; the folding door hisses open onto a quiet alley stop", "@Hung brings the bus to a stop and looks up into the mirror.", [("Hung", "Chị ơi, đến rồi.", "gentle, a nightly ritual")], ""),
  ("Dậy ngay", 4, ["AN1"], "medium shot at the back of the bus", "@An opens her eyes instantly at the very first call, picks up her bag and walks up the aisle.", [], ""),
  ("Em cảm ơn", 4, ["AN1", "HU1"], "50mm two-shot at the front door", "@An passes the driver's seat without looking at him; @Hung keeps his eyes ahead.", [("An", "Em cảm ơn anh.", "quiet"), ("Hung", "Chị về cẩn thận.", "quiet")], ""),
  ("Đèn hậu", 4, ["AN1"], "wide shot from the alley mouth", "@An stands under the single streetlamp as the bus pulls away, its red tail-lights fading in the drizzle.", [], "P7"),
  ("Ngủ Gật à", 5, ["AN1"], "85mm close-up under the streetlamp", "@An looks after the bus and smiles, wide awake.", [("An", "Ngủ Gật à…", "whisper, amused, tender")], "P7"),
])

scene("03", "Mở mắt thì anh ấy thôi nói", A1, "đêm 22, phòng trọ của An", "P6",
  "a small electric heater ticking, drizzle on the tin roof, distant motorbikes, a zipper straining. No music.", [
  ("Vali không đóng", 5, ["TH2"], "medium wide shot", "@Thao sits on top of an overstuffed open suitcase, bouncing on it, tugging at the zipper.", [("Thao", "Sáng hai lăm bay rồi mà vali vẫn chưa đóng nổi.", "exasperated, comic")], ""),
  ("An về", 4, ["AN1"], "medium shot by the door", "@An comes in, hangs her damp camel coat on a hook and sits on the mattress, still smiling to herself.", [], ""),
  ("Hôm nay kể gì", 4, ["TH2"], "50mm medium shot", "@Thao stops bouncing and narrows her eyes at her.", [("Thao", "Hôm nay anh lái xe kể gì?", "nosy")], ""),
  ("Bốn con", 4, ["AN1"], "85mm close-up", "@An hugs a pillow, dreamy.", [("An", "Chó ở bến cuối đẻ bốn con.", "dreamy")], ""),
  ("Lịch đẻ", 4, ["TH2"], "50mm medium shot", "@Thao stares at her flatly.", [("Thao", "Hai năm, mày thuộc cả lịch đẻ của chó bến xe.", "deadpan")], ""),
  ("Nói chưa", 4, ["TH2"], "85mm close-up", "@Thao turns serious.", [("Thao", "Thế mày đã nói với người ta là mày đi chưa?", "serious")], ""),
  ("Đang ngủ mà", 4, ["AN1"], "85mm close-up", "@An shrugs with a wry little smile.", [("An", "Nói thế nào? Tao đang ngủ mà.", "wry")], ""),
  ("Mở mắt ra", 4, ["TH2"], "50mm medium shot", "@Thao throws up her hands.", [("Thao", "Thì mở mắt ra mà nói!", "loud, exasperated")], ""),
  ("Thôi nói", 5, ["AN1"], "85mm close-up, slow push-in", "@An's smile fades; she looks down at her hands.", [("An", "Tao mở mắt thì anh ấy thôi nói.", "quiet, the plain truth")], ""),
  ("Tấm vé", 4, ["AN1"], "insert close-up on the mattress", "@An's fingers turn over a plain folded paper ticket and a dark booklet with blank covers; nothing on them is readable.", [], ""),
  ("Kém bốn tuổi", 5, ["TH2"], "50mm medium shot", "@Thao nudges her with a foot, trying to cheer her up.", [("Thao", "Hai năm người ta gọi mày bằng chị. Mày kém người ta bốn tuổi đấy.", "teasing")], ""),
  ("Lần cuối", 4, ["AN1"], "85mm close-up", "@An's laugh fades into something quieter.", [("An", "Đêm hai tư là lần cuối tao đi xe anh ấy.", "quiet")], ""),
  ("Nhìn một lần", 4, ["TH2"], "85mm close-up", "@Thao looks at her friend softly.", [("Thao", "Thế thì mở mắt ra, nhìn người ta một lần.", "soft")], ""),
])

scene("04", "Tuyến đêm bị cắt", A1, "đêm 22, sau nửa đêm, bến xe", "P4", PLACE_SOUND["P4"], [
  ("Bến xe", 4, [], "wide establishing shot", "Rows of parked city buses under orange sodium lights after midnight, puddles reflecting a tiny blinking plastic Christmas tree in the window of a glass dispatcher's booth.", [], ""),
  ("Mì tôm", 5, ["TU1"], "medium shot through the booth window", "@Tu slurps instant noodles at his desk in the booth, beanie and fingerless gloves on; he sees someone coming and points with his chopsticks.", [("Tu", "Có tin vui với tin buồn, nghe cái nào trước?", "jovial, mouth full")], ""),
  ("Trả chìa khóa", 4, ["HU1"], "medium shot at the booth counter", "@Hung puts the bus keys on the counter.", [("Hung", "Tin vui.", "tired")], ""),
  ("Ca ngày", 4, ["TU1"], "50mm medium shot", "@Tu spreads his hands grandly.", [("Tu", "Mày được lên ca ngày. Lương gấp rưỡi.", "grand")], ""),
  ("Thế tin buồn", 4, ["HU1"], "85mm close-up", "@Hung waits, wary.", [("Hung", "Thế tin buồn?", "wary")], ""),
  ("Cắt tuyến", 4, ["TU1"], "85mm close-up", "@Tu puts down the noodle cup.", [("Tu", "Tuyến đêm cắt. Đêm hai tư là chuyến cuối.", "blunt")], ""),
  ("Sững", 4, ["HU1"], "85mm close-up", "@Hung freezes, his hand still on the counter.", [], ""),
  ("Ba khách", 5, ["TU1"], "50mm medium shot", "@Tu counts on his gloved fingers.", [("Tu", "Cả tuyến có ba khách. Một ông già, một cô ngủ, với mày.", "counting, comic")], ""),
  ("Hai năm xếp ca", 5, ["TU1"], "50mm medium shot", "@Tu wags a finger at him.", [("Tu", "Hai năm tao xếp mày ca ngày, mày không đi. Lần này hết đường từ chối nhé.", "wagging, teasing")], ""),
  ("Vì cô ngủ gật", 5, ["TU1"], "85mm close-up", "@Tu leans in across the counter, grinning.", [("Tu", "Nói thật đi, mày ở lại tuyến đêm vì cô ngủ gật chứ gì?", "grinning")], ""),
  ("Dễ lái", 4, ["HU1"], "85mm close-up", "@Hung looks away.", [("Hung", "Tuyến đêm vắng. Dễ lái.", "evasive")], ""),
  ("Như lính", 4, ["TU1"], "50mm medium shot", "@Tu snorts and picks up his noodles again.", [("Tu", "Mày bảo gọi một tiếng là cô ấy dậy, như lính. Ngủ gì kiểu ấy?", "scoffing")], ""),
  ("Cười một mình", 4, ["HU1"], "85mm close-up", "@Hung looks down and smiles a small private smile, saying nothing.", [], ""),
  ("Ngủ Gật", 6, ["HU1"], "medium low-angle shot beside the cardboard box", "@Hung crouches by the cardboard box next to the booth where a brown stray dog nurses four puppies, and lifts one sleepy puppy gently in his palm.", [("Hung", "Còn hai đêm nữa thôi, Ngủ Gật ạ.", "soft")], ""),
])

scene("05", "Hai năm, một câu", A1, "sáng 23, nhà Hưng", "P5",
  "sticky rice steaming, a quiet morning alley, a moped passing, scissors cutting paper, a rooster far away. No music.", [
  ("Hang đá", 5, ["BL1"], "medium shot across the low table", "@BaLua sits gluing straw onto a small handmade nativity crib, the sticky-rice pot steaming behind her, and glares at someone off-screen.", [("BaLua", "Ba mươi hai tuổi đầu, mày định lấy cái vô lăng làm vợ à?", "nagging, loud")], ""),
  ("Tuyến cắt rồi", 4, ["HU2"], "medium shot", "@Hung, messy-haired in a grey hoodie, sits down opposite and steals a pinch of sticky rice.", [("Hung", "Tuyến đêm cắt rồi mẹ ạ.", "flat")], ""),
  ("Tốt", 4, ["BL1"], "50mm medium shot", "@BaLua slaps the table, delighted.", [("BaLua", "Tốt! Từ giờ mày ngủ đêm như người.", "pleased")], ""),
  ("Cô ngủ gật", 4, ["BL1"], "85mm close-up", "@BaLua stops gluing and peers at him slyly.", [("BaLua", "Thế còn cái cô ngủ gật?", "sly")], ""),
  ("Sao mẹ biết", 4, ["HU2"], "85mm close-up", "@Hung chokes on the rice.", [("Hung", "Sao mẹ biết?", "startled")], ""),
  ("Cả bến xe", 4, ["BL1"], "50mm medium shot", "@BaLua goes back to her straw.", [("BaLua", "Thằng Tú bảo. Cả bến xe biết.", "matter-of-fact")], ""),
  ("Gục đầu", 4, ["HU2"], "medium shot", "@Hung drops his forehead onto the table with a soft thud.", [], ""),
  ("Tặng gì", 4, ["BL1"], "50mm medium shot", "@BaLua pokes his head with the glue brush handle.", [("BaLua", "Noel rồi, mày định tặng người ta cái gì?", "brisk")], ""),
  ("Một câu", 4, ["HU2"], "85mm close-up, his cheek still on the table", "@Hung answers without lifting his head.", [("Hung", "Hai năm, con mới nói với người ta đúng một câu.", "sheepish")], ""),
  ("Câu gì", 4, ["BL1"], "85mm close-up", "@BaLua leans in.", [("BaLua", "Câu gì?", "curious")], ""),
  ("Đến rồi", 4, ["HU2"], "85mm close-up", "@Hung sits up, embarrassed.", [("Hung", "Chị ơi, đến rồi.", "embarrassed")], ""),
  ("Câu khác", 5, ["BL1"], "50mm medium shot", "@BaLua stares at him, then shakes her head slowly.", [("BaLua", "Hai năm tặng người ta một câu. Năm nay tặng câu khác đi.", "dry")], ""),
  ("Đôi găng", 5, ["BL1"], "medium shot", "@BaLua pulls a pair of hand-knitted grey wool gloves from her apron pocket and slaps them on the table in front of him.", [("BaLua", "Mẹ đan đấy. Con gái đi đêm, tay lạnh.", "gruff, tender")], ""),
  ("Tên gì", 4, ["BL1"], "85mm close-up", "@BaLua picks up her glue brush again, casually.", [("BaLua", "Mà con bé ấy tên gì?", "casual")], ""),
  ("Không biết", 4, ["HU2"], "85mm close-up", "@Hung holds the gloves and goes very still.", [("Hung", "…Con không biết.", "tiny voice")], ""),
  ("Hai năm!", 4, ["BL1"], "50mm medium shot", "@BaLua drops the glue brush onto the crib.", [("BaLua", "Hai năm!", "outraged")], ""),
])

# ================================================================ HỒI 2
scene("06", "Người ngồi cổng viện", A2, "tối 23, ghế đá cổng bệnh viện", "P2", PLACE_SOUND["P2"], [
  ("Ghế đá", 5, ["OT1"], "wide shot", "@OngThu sits alone on the stone bench beside the tall iron hospital gate, thermos on his knees, red scarf around his neck, gazing at the gate.", [], ""),
  ("Ổ bánh mì", 5, ["AN1", "OT1"], "medium two-shot on the bench", "@An comes out through the gate, sits down beside the old man and hands him a warm paper-wrapped bread roll.", [("An", "Ông ăn đi cho ấm.", "gentle")], ""),
  ("Vào thăm chưa", 4, ["AN1"], "85mm close-up", "@An watches him carefully.", [("An", "Hôm nay ông vào thăm bà chưa?", "careful")], ""),
  ("Vào rồi", 4, ["OT1"], "85mm close-up", "@OngThu unwraps the bread without looking at her.", [("OngThu", "Vào rồi.", "too quick")], ""),
  ("Ánh mắt", 4, ["AN1"], "85mm close-up", "@An looks at him with sad, knowing eyes, and lets it go.", [], ""),
  ("Đi xa", 4, ["AN1"], "50mm medium shot", "@An pulls her coat tighter.", [("An", "Ông ơi, sáng hai lăm cháu đi xa rồi. Năm năm ạ.", "quiet")], ""),
  ("Cậu lái xe", 4, ["OT1"], "50mm medium shot", "@OngThu turns his head sharply toward her.", [("OngThu", "Cậu lái xe biết chưa?", "sharp")], ""),
  ("Đang ngủ", 4, ["AN1"], "85mm close-up", "@An gives a wry little smile.", [("An", "Cháu đang ngủ mà ông.", "wry")], ""),
  ("Thở dài", 4, ["OT1"], "85mm close-up", "@OngThu sighs and shakes his head slowly.", [("OngThu", "Ngày xưa bà nhà tôi cũng ngủ.", "wistful")], ""),
  ("Đèn pha", 4, ["OT1", "AN1"], "wide shot", "Headlights sweep across the wet pavement as the night bus pulls into the stop; the old man and the nurse both stand up from the bench.", [], ""),
  ("Vào mà ngủ", 4, ["OT1"], "50mm medium shot", "@OngThu tucks the bread into his coat and nods at the bus.", [("OngThu", "Xe đến rồi. Cô vào mà ngủ.", "dry joke")], ""),
])

scene("07", "Tàu điện năm mươi năm trước", A2, "đêm 23 trên xe; hồi tưởng: tàu điện đêm năm mươi năm trước", "P1", BUS_SOUND, [
  ("Ông tán bà", 4, ["HU1"], "50mm medium shot", "@Hung glances at the old man behind him; far back in the mirror the nurse is already asleep.", [("Hung", "Ông ơi, ngày xưa ông tán bà thế nào?", "shy, curious")], ""),
  ("Tàu điện", 4, ["OT1"], "85mm close-up", "@OngThu points at the road ahead with his thermos.", [("OngThu", "Ngày xưa tôi lái tàu điện. Tuyến này đây.", "proud")], ""),
  ("Đường ray", 4, ["OT1"], "50mm medium shot over his shoulder toward the windscreen", "@OngThu taps the window toward the asphalt.", [("OngThu", "Đường ray còn chôn dưới lớp nhựa này này.", "fond")], ""),
  ("Tàu đêm", 4, ["OTT"], "medium shot from behind the young driver", "Fifty years ago: @OngThuTre drives an old wooden city tram through the quiet night, brass controls under a dim yellow bulb.", [], "P9"),
  ("Cô y tá", 4, ["BNT"], "medium shot", "@BaNguyetTre, a young nurse in a white uniform and cap, sleeps on a wooden slat bench, her cloth bag on her lap, head against the window frame.", [], "P9"),
  ("Ba năm", 4, ["OT1"], "85mm close-up", "@OngThu smiles at the memory.", [("OngThu", "Ba năm, đêm nào bà ấy cũng ngủ trên tàu tôi.", "tender")], ""),
  ("Liếc gương", 4, ["HU1"], "85mm close-up", "@Hung's eyes flick to the rear-view mirror, then back to the road.", [], ""),
  ("Cô ơi", 4, ["OTT"], "medium shot inside the tram", "@OngThuTre stops the tram and turns toward the sleeping nurse, his cap in his hands.", [("OngThuTre", "Cô ơi, đến rồi.", "shy")], "P9"),
  ("Y như cháu", 4, ["HU1"], "85mm close-up", "@Hung lets out a stunned half-laugh.", [("Hung", "Y như cháu.", "half-laugh, stunned")], ""),
  ("Chữ thương", 5, ["OT1"], "85mm close-up", "@OngThu looks down at his thermos.", [("OngThu", "Năm mươi năm, tôi chưa nói chữ thương nào lúc bà ấy thức.", "low")], ""),
  ("Không nghe được", 5, ["OT1"], "100mm close-up", "@OngThu's jaw trembles.", [("OngThu", "Đến lúc nói được thì bà ấy không nghe được nữa.", "barely audible")], ""),
  ("Vẫn nằm viện", 4, ["HU1"], "50mm medium shot", "@Hung frowns toward the mirror at the old man.", [("Hung", "Bà… vẫn đang nằm viện mà ông?", "confused")], ""),
  ("Đến rồi", 4, ["OT1"], "medium shot", "The bus stops; @OngThu stands up without answering and moves to the door.", [("OngThu", "Đến rồi.", "deflecting")], ""),
  ("Mắt mở", 5, ["AN1"], "100mm close-up in the dark at the back", "@An's eyes are open and wet, fixed on the old man walking to the door.", [], ""),
])

scene("08", "Em thích chị", A2, "đêm 23, tiếp liền", "P1", BUS_SOUND, [
  ("Đèn đỏ", 4, ["HU1"], "50mm medium side shot", "The bus stops at a red light; Christmas lights blink on a bare tree outside; @Hung looks up into the mirror.", [], ""),
  ("Tuyến cắt", 5, ["HU1"], "85mm close-up", "@Hung speaks softly to the mirror.", [("Hung", "Chị ơi, tuyến đêm cắt rồi. Đêm mai là chuyến cuối.", "soft")], ""),
  ("An toàn", 5, ["HU1"], "85mm close-up", "@Hung swallows.", [("Hung", "Từ ngày kia, em không biết chị về có an toàn không.", "worried")], ""),
  ("Chưa biết tên", 4, ["HU1"], "50mm medium shot", "@Hung gives a small rueful laugh.", [("Hung", "Hai năm rồi, em còn chưa biết tên chị.", "rueful")], ""),
  ("Mai em kể", 4, ["HU1"], "85mm close-up", "@Hung takes a breath, both hands tight on the wheel.", [("Hung", "Hôm qua em bảo mai em kể.", "nervous")], ""),
  ("Dám nói", 4, ["HU1"], "50mm medium close-up from the passenger side, a different angle from the opening", "@Hung looks into the mirror as the light turns green.", [("Hung", "Chị ngủ thì em mới dám nói.", "soft, trembling")], ""),
  ("Em thích chị", 4, ["HU1"], "85mm close-up", "@Hung barely moves his lips.", [("Hung", "Em thích chị.", "whisper")], ""),
  ("Giọt nước mắt", 5, ["AN1"], "100mm close-up from a lower angle than the opening", "A single tear slides from @An's closed eye down to her chin; she does not wipe it.", [], ""),
  ("Đến trạm", 4, ["HU1"], "medium shot; the bus pulls up at the alley stop and the door hisses open", "@Hung looks up into the mirror.", [("Hung", "Chị ơi, đến rồi.", "gentle")], ""),
  ("Không dậy", 5, ["AN1"], "wide shot down the aisle", "@An does not move. For the first time she does not wake at the first call.", [], ""),
  ("Gọi lần hai", 4, ["HU1"], "85mm close-up", "@Hung waits, then calls again, very softly.", [("Hung", "Chị ơi.", "very soft")], ""),
  ("Không nhìn", 4, ["AN1", "HU1"], "medium two-shot at the door", "@An gets up and walks to the door with her head down, not looking at him; @Hung keeps his eyes on the wheel.", [("An", "Em cảm ơn.", "thin voice")], ""),
  ("Đèn khẩn cấp", 6, ["AN1"], "wide shot from the alley mouth", "On the pavement @An presses her hand over her mouth and cries; behind her the bus stays at the stop, its amber hazard lights blinking, before it finally pulls away.", [], "P7"),
])

scene("09", "Đêm đầu tiên", A2, "đêm 23, phòng trọ; hồi tưởng: hai năm trước", "P6",
  "a small electric heater ticking, rain on the tin roof, a stifled sob. No music.", [
  ("Mắt đỏ", 5, ["AN3", "TH2"], "medium two-shot", "@An sits on the floor against the suitcase in an oversized sweater, red-eyed; @Thao kneels in front of her.", [("Thao", "Anh ấy nói rồi à?", "gentle")], ""),
  ("Trả lời gì", 4, ["TH2"], "85mm close-up", "@Thao leans closer.", [("Thao", "Thế mày trả lời gì?", "urgent")], ""),
  ("Tao ngủ", 4, ["AN3"], "85mm close-up", "@An whispers.", [("An", "Tao ngủ.", "tiny")], ""),
  ("Phang gối", 5, ["TH2", "AN3"], "medium two-shot", "@Thao grabs a pillow, smacks An with it, then pulls her into a tight hug.", [("Thao", "Con điên!", "half-laughing, half-crying")], ""),
  ("Bắt chờ", 5, ["AN3"], "85mm close-up over Thao's shoulder", "@An speaks into her friend's shoulder.", [("An", "Ngày kia tao bay. Năm năm. Bắt người ta chờ à?", "bitter")], ""),
  ("Hỏi chưa", 5, ["TH2"], "85mm close-up", "@Thao holds her at arm's length.", [("Thao", "Mày hỏi người ta chưa mà biết người ta không chờ?", "firm")], ""),
  ("Đêm đầu tiên", 5, ["AN3"], "85mm close-up lit by the heater's orange glow", "@An stares at the glowing heater.", [("An", "Đêm đầu tiên, tao vừa mất bệnh nhân đầu tiên.", "distant")], ""),
  ("Khóc trên xe", 5, ["AN1"], "100mm close-up at the back of the bus", "Two years ago: @An sits in the last row of the night bus in her coat over scrubs, crying silently, trying to hide it against the rainy window.", [], "P1F"),
  ("Cứ ngủ đi", 5, ["HU1"], "50mm close-up on the driver, eyes in the mirror", "Two years ago: @Hung glances in the mirror and quietly switches the radio off.", [("Hung", "Chị cứ ngủ đi. Đến nơi em gọi.", "gentle")], "P1F"),
  ("Nhắm mắt", 4, ["AN1"], "100mm close-up", "Two years ago: @An closes her eyes; tears still run, but her breathing slows.", [], "P1F"),
  ("Hai năm", 6, ["AN3"], "85mm close-up", "@An smiles faintly through tears.", [("An", "Anh ấy kể chuyện linh tinh suốt đường. Tao nhắm mắt nghe. Hai năm.", "soft")], ""),
  ("Đến bao giờ", 4, ["TH2"], "85mm close-up", "@Thao wipes her friend's cheek with her sleeve.", [("Thao", "Thế mày định ngủ đến bao giờ?", "soft")], ""),
  ("Tấm vé", 5, ["AN3"], "medium shot", "@An looks at the plain folded ticket on the mattress and does not answer.", [], ""),
])

scene("10", "Tên cô ấy là An", A2, "sáng 24, hành lang khoa", "P3", PLACE_SOUND["P3"], [
  ("Hành lang", 4, ["HU2"], "wide shot down the corridor", "@Hung walks hesitantly down the ward corridor holding a plastic bag of mandarins, peering into doorways.", [], ""),
  ("Anh tìm ai", 4, ["TH1"], "medium shot at the nurse station", "@Thao, writing on a blank chart at the counter, looks up.", [("Thao", "Anh tìm ai?", "brisk")], ""),
  ("Bà Nguyệt", 4, ["HU2"], "50mm medium shot", "@Hung bows his head politely.", [("Hung", "Dạ, em tìm bà Nguyệt, vợ ông Thư.", "polite")], ""),
  ("Mất rồi", 5, ["TH1"], "85mm close-up", "@Thao's face softens.", [("Thao", "Bà Nguyệt mất năm ngoái rồi anh ạ. Đúng đêm Noel.", "gentle")], ""),
  ("Sững", 4, ["HU2"], "85mm close-up", "@Hung stands frozen, the bag of mandarins hanging from his fingers.", [], ""),
  ("Ngồi cổng", 6, ["TH1"], "50mm medium shot", "@Thao lowers her voice.", [("Thao", "Đêm nào ông cũng ra ngồi cổng viện. Không vào. Đợi xe cuối thì về.", "quiet")], ""),
  ("Nhìn xuống", 5, ["HU2"], "medium shot from behind at the corridor window", "@Hung turns to the window and looks down at the empty stone bench by the gate far below.", [], ""),
  ("Nhận ra", 4, ["TH1"], "85mm close-up", "@Thao narrows her eyes, recognising something.", [("Thao", "Khoan. Anh là anh lái xe tuyến đêm à?", "suspicious")], ""),
  ("Biết tên chưa", 5, ["TH1"], "50mm medium shot", "@Thao crosses her arms.", [("Thao", "Hai năm lái xe, anh biết tên người ta chưa?", "arms crossed")], ""),
  ("Chưa", 4, ["HU2"], "85mm close-up", "@Hung shakes his head.", [("Hung", "Chưa ạ.", "sheepish")], ""),
  ("An", 4, ["TH1"], "85mm close-up", "@Thao relents.", [("Thao", "An. Tên nó là An.", "softening")], ""),
  ("Thì thầm", 4, ["HU2"], "100mm close-up", "@Hung says the name to himself, as if tasting it.", [("Hung", "An…", "whisper")], ""),
  ("Sáu giờ", 5, ["TH1"], "85mm close-up", "@Thao looks him straight in the eye.", [("Thao", "Sáng mai nó bay. Sáu giờ. Năm năm.", "blunt")], ""),
  ("Quýt lăn", 4, ["HU2"], "low-angle insert at floor level", "The plastic bag slips from @Hung's fingers; bright mandarins roll across the pale corridor floor around his sneakers.", [], ""),
  ("Chuyến cuối", 6, ["TH1"], "85mm close-up", "@Thao picks up one mandarin and holds it out to him.", [("Thao", "Đêm nay nó trực ca cuối. Chuyến cuối của anh cũng là chuyến cuối của nó.", "meaningful")], ""),
])

scene("11", "Chiếc khăn đỏ", A2, "chập tối 24, ghế đá cổng bệnh viện", "P2D", PLACE_SOUND["P2D"], [
  ("Ngồi xuống", 5, ["OT1", "HU1"], "wide shot", "Dusk. @OngThu sits on the stone bench by the hospital gate; @Hung, in his driver's uniform, comes and sits down beside him without a word.", [], ""),
  ("Cháu biết rồi", 4, ["HU1"], "85mm close-up", "@Hung looks at the old man's profile.", [("Hung", "Ông ơi. Cháu biết rồi. Bà mất từ năm ngoái.", "gentle, quiet")], ""),
  ("Im", 4, ["OT1"], "100mm close-up", "@OngThu keeps looking at the gate; his jaw trembles, then steadies.", [], ""),
  ("Đứng cổng", 5, ["OT1"], "85mm close-up", "@OngThu nods at the iron gate.", [("OngThu", "Bốn mươi năm bà ấy đi trực, tôi đứng cổng này đón.", "low")], ""),
  ("Chân quen đường", 6, ["OT1"], "100mm close-up, very slow push-in", "@OngThu's eyes glisten.", [("OngThu", "Giờ bà ấy không tan ca nữa, mà chân tôi vẫn quen đường.", "cracking")], ""),
  ("Nói dối", 5, ["OT1"], "50mm medium shot", "@OngThu gives a small guilty smile.", [("OngThu", "Nói dối cậu bà còn nằm đấy, tôi nghe cũng thấy đỡ.", "guilty, wry")], ""),
  ("Bàn tay", 4, ["HU1", "OT1"], "insert close-up on their hands", "@Hung places his hand over the old man's trembling hand on the thermos.", [], ""),
  ("Cái khăn", 5, ["OT1"], "85mm close-up", "@OngThu touches the faded red scarf at his neck.", [("OngThu", "Cái khăn này, đêm Noel năm mươi năm trước tôi quàng cho bà ấy.", "tender")], ""),
  ("Lúc ngủ", 4, ["OT1"], "85mm close-up", "@OngThu smiles faintly.", [("OngThu", "Lúc bà ấy đang ngủ trên tàu.", "small smile")], ""),
  ("Cháu cũng nói", 5, ["HU1"], "85mm close-up", "@Hung looks down at his shoes.", [("Hung", "Cháu cũng nói rồi ông ạ. Lúc cô ấy ngủ.", "ashamed")], ""),
  ("Như tôi", 4, ["OT1"], "50mm medium shot", "@OngThu turns and looks at him for the first time.", [("OngThu", "Thế thì như tôi.", "flat")], ""),
  ("Lúc thức", 5, ["OT1"], "85mm close-up", "@OngThu grips Hung's wrist.", [("OngThu", "Cậu hỏi lại đi. Lần này, hỏi lúc người ta thức.", "firm")], ""),
])

scene("12", "Ca trực cuối", A2, "tối 24, khoa bệnh viện; hồi tưởng: đêm Noel năm ngoái", "P3", PLACE_SOUND["P3"], [
  ("Mũ Noel", 4, ["AN2", "TH1"], "wide shot down the corridor", "Christmas Eve on the ward: @An and @Thao, red Santa hats over their scrubs, walk past the small decorated tree at the nurse station.", [], ""),
  ("Quả quýt", 5, ["AN2", "BaCu"], "medium shot in a patient room", "@BaCu, an old patient sitting up in bed, presses a mandarin into @An's hands; @An bows her head, moved.", [("BaCu", "Đi đâu cũng nhớ ăn cho no nhé cháu.", "motherly, shaky")], ""),
  ("Cửa sổ", 5, ["AN2"], "medium shot from behind at the corridor window", "@An looks down from the window: at the gate far below, two tiny anonymous figures sit side by side on the stone bench, one with a red scarf.", [], ""),
  ("Ngồi với ông", 4, ["TH1"], "50mm medium shot", "@Thao comes beside her and looks down too.", [("Thao", "Anh ấy đến từ chiều. Ngồi với ông.", "soft")], ""),
  ("Đêm ấy", 5, ["AN2"], "85mm close-up", "@An keeps looking down.", [("An", "Đêm Noel năm ngoái, ông nói với bà một câu.", "distant")], ""),
  ("Phòng bệnh", 5, ["OT1", "BN1"], "medium shot", "One year ago: @OngThu sits by a hospital bed holding the hand of @BaNguyet, who lies unconscious with her eyes closed, the red scarf folded on her pillow.", [], "P3F"),
  ("Anh thương em", 5, ["OT1"], "85mm close-up, @OngThu leaning close to her ear", "One year ago: @OngThu whispers into his wife's ear.", [("OngThu", "Anh thương em.", "whisper, breaking")], "P3F"),
  ("Giọt nước mắt", 4, ["BN1"], "100mm close-up on her face on the pillow", "One year ago: a single tear slides from @BaNguyet's closed eye.", [], "P3F"),
  ("Ở cửa", 4, ["AN2"], "medium shot at the half-open door", "One year ago: @An, standing at the half-open door, sees it and covers her mouth.", [], "P3F"),
  ("Kể chưa", 4, ["TH1"], "85mm close-up", "@Thao looks at her.", [("Thao", "Mày kể với ông chưa?", "soft")], ""),
  ("Sợ ông đau", 4, ["AN2"], "85mm close-up", "@An shakes her head.", [("An", "Chưa. Tao sợ ông đau thêm.", "quiet")], ""),
  ("Người nằm im", 7, ["TH1"], "50mm medium shot", "@Thao takes her friend's hand.", [("Thao", "Người nằm im còn nghe được. Mày nhắm mắt hai năm, mày nghe được những gì?", "gentle push")], ""),
  ("Nghe hết", 5, ["AN2"], "85mm close-up", "@An slowly takes off her Santa hat.", [("An", "Nghe hết.", "quiet resolve")], ""),
])

# ================================================================ HỒI 3
scene("13", "Chuyến cuối", A3, "đêm Noel, 22 giờ 50, trạm bệnh viện", "P2",
  "a dense holiday crowd, motorbike horns, balloon vendors, cathedral bells far away. No music.", [
  ("Phố đông", 4, [], "wide shot", "Christmas Eve: the street outside the hospital is jammed with motorbikes and adults in Santa hats heading toward the cathedral; the night bus inches into the stop.", [], ""),
  ("Ông lên xe", 4, ["OT1", "HU1"], "medium shot at the door from inside the bus", "@OngThu climbs aboard; @Hung nods to him, then looks past him at the empty stop.", [], "P1"),
  ("Bộ đàm", 5, ["TU1"], "medium shot in the booth", "@Tu, a red Santa hat on top of his beanie, speaks into the two-way radio handset.", [("Tu", "Hưng ơi, chuyến cuối mà mày chậm năm phút rồi đấy.", "loud, cheerful")], "P4"),
  ("Chờ một khách", 4, ["HU1"], "50mm medium shot", "@Hung lifts the dashboard radio handset.", [("Hung", "Em chờ một khách.", "steady")], "P1"),
  ("Chạy đi", 4, ["TU1"], "85mm close-up", "@Tu rolls his eyes.", [("Tu", "Cô ngủ gật chứ gì? Hết giờ rồi, chạy đi!", "impatient, fond")], "P4"),
  ("Không lên xe nữa", 5, ["OT1"], "85mm close-up", "@OngThu, in the first seat, speaks gently, thinking of someone else.", [("OngThu", "Đi thôi cậu. Có những người không lên xe nữa đâu.", "sad")], "P1"),
  ("Đóng cửa", 4, ["HU1"], "medium shot", "@Hung closes the folding door and slowly pulls away from the kerb.", [], "P1"),
  ("Gương bên hông", 4, ["AN1"], "close-up on the bus's side mirror", "In the side mirror: @An running through the holiday crowd, bag flying, waving her arm.", [], ""),
  ("Phanh", 4, ["HU1"], "50mm medium shot", "@Hung slams on the brakes and hits the door button.", [], "P1"),
  ("Lên xe", 4, ["AN1"], "medium shot at the door from inside", "@An climbs the steps, breathless, cheeks flushed from the cold.", [], "P1"),
  ("Nhìn nhau", 5, ["AN1", "HU1"], "50mm two-shot at the door", "For the first time in two years they look straight at each other; a long, frozen second.", [], "P1"),
  ("Nhắm mắt", 5, ["AN1"], "wide shot down the aisle", "@An breaks the look, walks to the last row, sits by the window and closes her eyes.", [], "P1"),
  ("Mặt Hưng", 4, ["HU1"], "85mm close-up", "@Hung's face falls; he looks down, then puts the bus in gear.", [], "P1"),
])

scene("14", "Đêm Noel năm ấy", A3, "đêm Noel, phố nhà thờ; hồi tưởng: đêm Noel năm mươi năm trước", "P8", PLACE_SOUND["P8"], [
  ("Kẹt giữa biển người", 5, [], "wide high-angle shot", "The night bus is stuck in a sea of adults in Santa hats and winter coats in front of a huge lit stone cathedral with twin bell towers.", [], ""),
  ("Cũng tắc thế này", 5, ["OT1"], "85mm close-up through the bus window", "@OngThu looks out at the crowd and the glowing cathedral.", [("OngThu", "Năm mươi năm trước cũng tắc thế này.", "fond")], "P1"),
  ("Mẹ gõ cửa", 4, ["BL2"], "medium shot from inside, through the driver's side window", "@BaLua, dressed for midnight mass, pushes through the crowd, recognises the bus and knocks on the driver's window.", [("BaLua", "Nói chưa con?", "loud, hopeful")], ""),
  ("Mẹ đi lễ đi", 4, ["HU1"], "85mm close-up", "@Hung waves her away through the glass, mortified.", [("Hung", "Mẹ đi lễ đi!", "mortified hiss")], "P1"),
  ("Tàu đứng", 4, [], "wide shot", "Fifty years ago on Christmas Eve: the old wooden tram is stuck in a crowd in front of the same stone cathedral; bells ring.", [], "P9B"),
  ("Ngủ trên tàu", 4, ["BNT"], "medium shot inside the tram", "@BaNguyetTre sleeps on the wooden bench, shivering a little in the cold.", [], "P9"),
  ("Quàng khăn", 5, ["OTT", "BNT"], "medium two-shot inside the tram", "@OngThuTre takes a new red knitted scarf from his jacket and, with trembling hands, wraps it around the sleeping nurse's neck.", [], "P9"),
  ("Mở mắt", 4, ["BNT"], "85mm close-up", "@BaNguyetTre opens her eyes and looks up at him; out of frame his hands are still on the scarf.", [], "P9"),
  ("Cho chặt vào", 4, ["BNT", "OTT"], "50mm two-shot", "@BaNguyetTre looks at the frozen young driver with a sleepy smile.", [("BaNguyetTre", "Anh quàng thì quàng cho chặt vào.", "teasing, sleepy")], "P9"),
  ("Toét miệng cười", 4, ["OTT"], "85mm close-up", "@OngThuTre bursts into a huge, disbelieving grin.", [], "P9"),
  ("Tháo khăn", 4, ["OT1"], "85mm close-up", "In the present, @OngThu slowly unwinds the faded red scarf from his neck.", [], "P1"),
  ("Đứng dậy", 5, ["OT1", "HU1"], "wide shot down the aisle of the motionless bus", "@OngThu stands up and walks down the aisle toward the young woman in the last row; @Hung watches him in the mirror.", [], "P1"),
])

scene("15", "Bà nghe thấy đấy", A3, "đêm Noel, ghế cuối, tiếp liền", "P1", PLACE_SOUND["P8"], [
  ("Ngồi cạnh", 5, ["OT1", "AN1"], "medium two-shot in the last row", "@OngThu sits down beside @An, who has her eyes closed.", [("OngThu", "Cô An. Tôi biết cô không ngủ.", "gentle")], ""),
  ("Mở mắt", 4, ["AN1"], "85mm close-up", "@An opens her eyes.", [], ""),
  ("Cửa phòng", 5, ["AN1"], "85mm close-up", "@An turns to him, trembling.", [("An", "Ông ơi. Đêm Noel năm ngoái, cháu đứng ở cửa phòng.", "trembling")], ""),
  ("Bà khóc", 5, ["AN1"], "85mm close-up", "@An's eyes fill.", [("An", "Lúc ông nói với bà… bà khóc. Cháu thấy.", "soft")], ""),
  ("Bà nghe thấy", 4, ["AN1"], "100mm close-up", "@An smiles through her tears.", [("An", "Bà nghe thấy đấy ông ạ.", "tender")], ""),
  ("Bà nghe thấy à", 5, ["OT1"], "100mm close-up", "@OngThu's face crumples; he grips the scarf in both hands.", [("OngThu", "Bà nghe thấy à?", "breaking")], ""),
  ("Nắm tay", 4, ["AN1", "OT1"], "insert close-up", "@An nods, crying, and takes the old man's hand in both of hers.", [], ""),
  ("Chuông", 4, [], "wide shot", "The cathedral's bell towers ring out over the crowd; people look up.", [], "P8"),
  ("Quàng cho cô", 6, ["OT1", "AN1"], "medium two-shot", "@OngThu wraps the faded red scarf around @An's neck with trembling hands.", [("OngThu", "Bà ấy không lạnh nữa. Cô đi xa, cô quàng.", "gentle")], ""),
  ("Đừng để", 5, ["OT1"], "85mm close-up", "@OngThu pats her hand.", [("OngThu", "Đừng để người ta nói thương với người đang ngủ nữa.", "firm, kind")], ""),
  ("Đi lễ", 4, ["OT1", "HU1"], "medium shot at the open door", "@OngThu stands at the open door, looking out at the cathedral.", [("OngThu", "Tôi xuống đây. Đi lễ với bà ấy.", "peaceful")], ""),
  ("Đi chậm", 4, ["OT1"], "85mm close-up", "@OngThu turns back to the driver with a wry smile.", [("OngThu", "Cậu lái xe. Chuyến cuối thì đi chậm thôi.", "wry")], ""),
  ("Vào đám đông", 5, ["OT1"], "wide shot", "@OngThu walks slowly into the bright crowd toward the cathedral, a small upright figure with no scarf.", [], "P8"),
])

scene("16", "Bộ đàm", A3, "đêm Noel, đại lộ vắng", "P1", BUS_SOUND, [
  ("Đường vắng", 4, [], "wide shot", "The night bus glides along a now-empty boulevard of bare trees wrapped in white fairy lights.", [], "PS"),
  ("Hai người", 5, ["HU1", "AN1"], "wide shot from behind An toward the front", "@An sits in the last row, eyes open, the red scarf around her neck, watching the back of the driver's head; @Hung drives, eyes fixed on the road.", [], ""),
  ("Tú gọi", 5, ["TU1"], "medium shot in the booth", "@Tu, feet up on the desk with a cup of tea, speaks cheerfully into the radio.", [("Tu", "Hưng ơi, xong chuyến về đây anh em khui chai.", "cheerful")], "P4"),
  ("Mai ca ngày", 5, ["TU1"], "85mm close-up", "@Tu wags a finger at the radio.", [("Tu", "À, mai mày lên ca ngày nhé, đừng từ chối như hai năm nay nữa.", "teasing")], "P4"),
  ("Lái đêm", 5, ["TU1"], "50mm medium shot", "@Tu laughs into the handset.", [("Tu", "Hai năm lương gấp rưỡi không lấy, cứ đòi lái đêm. Lái đêm có cái gì!", "laughing")], "P4"),
  ("Tắt", 4, ["HU1"], "insert close-up on the dashboard", "@Hung clicks the radio off; silence.", [], ""),
  ("Nghe thấy", 4, ["AN1"], "85mm close-up", "@An, at the back, stares at him, stunned.", [], ""),
  ("Hai năm à", 4, ["AN1"], "85mm close-up", "@An speaks up, clear in the empty bus.", [("An", "Anh từ chối ca ngày hai năm à?", "clear, stunned")], ""),
  ("Tai đỏ", 4, ["HU1"], "85mm close-up from behind and to the side", "@Hung says nothing; his ears turn red.", [], ""),
  ("Đến trạm", 4, ["HU1"], "medium shot; the bus pulls up at the alley stop and the door hisses open on the cold", "@Hung keeps his eyes on the wheel.", [("Hung", "Chị ơi, đến rồi.", "careful, flat")], ""),
  ("Không đứng dậy", 5, ["AN1"], "wide shot down the aisle", "@An stays seated, hands folded on her bag, eyes open, looking straight at the mirror.", [], ""),
])

scene("17", "Em biết chị không ngủ", A3, "đêm Noel, trạm đầu ngõ, tiếp liền", "P1",
  "the bus engine idling, the open door letting in the hush of the alley, a far-off bell. No music.", [
  ("Chưa trả lời", 5, ["AN1"], "85mm close-up", "@An speaks toward the front of the bus.", [("An", "Đêm qua anh nói một câu. Em chưa trả lời.", "steady")], ""),
  ("Không cần", 4, ["HU1"], "50mm medium shot, @Hung speaking to the mirror without turning", "@Hung looks into the mirror.", [("Hung", "Chị không cần trả lời.", "gentle")], ""),
  ("Em biết", 4, ["HU1"], "85mm close-up", "@Hung smiles slightly at the mirror.", [("Hung", "Em biết chị không ngủ.", "quiet")], ""),
  ("Từ bao giờ", 4, ["AN1"], "85mm close-up", "@An stares, lips parted.", [("An", "Từ… bao giờ?", "stunned")], ""),
  ("Đêm đầu tiên", 4, ["HU1"], "85mm close-up", "@Hung answers simply.", [("Hung", "Từ đêm đầu tiên.", "simple")], ""),
  ("Lần thứ hai", 5, ["HU1"], "85mm close-up", "@Hung's smile widens a little.", [("Hung", "Hai năm, chưa đêm nào em phải gọi đến lần thứ hai.", "small smile")], ""),
  ("Trừ đêm qua", 4, ["HU1"], "100mm close-up", "@Hung's smile fades.", [("Hung", "Trừ đêm qua.", "soft")], ""),
  ("Sao vẫn nói", 4, ["AN1"], "85mm close-up", "@An laughs and cries at once.", [("An", "Thế sao anh vẫn nói?", "crying, laughing")], ""),
  ("Thôi nghe", 5, ["HU1"], "85mm close-up", "@Hung looks into the mirror.", [("Hung", "Vì chị mở mắt ra thì chị sẽ thôi nghe.", "honest")], ""),
  ("Thôi nói", 5, ["AN1"], "85mm close-up", "@An covers her mouth, laughing through tears.", [("An", "Em cứ sợ em mở mắt thì anh thôi nói.", "laughing through tears")], ""),
  ("Đi lên", 4, ["AN1"], "wide shot down the aisle", "@An stands and walks up the aisle to the front, the red scarf around her neck.", [], ""),
  ("Năm năm", 6, ["AN1", "HU1"], "50mm two-shot, she stands beside the driver's seat", "@An stands beside the driver's seat, holding a grab pole; @Hung still looks ahead.", [("An", "Sáng mai em bay. Năm năm.", "quiet"), ("Hung", "Em biết. Bạn chị bảo rồi.", "gentle")], ""),
  ("Em tên An", 4, ["AN1"], "85mm close-up", "@An looks down at him.", [("An", "Em tên An.", "soft")], ""),
  ("Em biết", 4, ["HU1"], "85mm close-up", "@Hung smiles at the wheel.", [("Hung", "Em biết.", "smiling")], ""),
  ("Muốn nghe", 4, ["AN1"], "85mm close-up", "@An leans a little closer.", [("An", "Em muốn nghe anh nói tên anh.", "tender")], ""),
  ("Hưng", 4, ["HU1"], "85mm close-up as he turns his head", "@Hung turns and looks straight at her for the first time.", [("Hung", "Hưng.", "simple, warm")], ""),
  ("Đừng gọi chị", 5, ["AN1"], "85mm close-up", "@An wipes her eyes, teasing.", [("An", "Em kém anh bốn tuổi. Đừng gọi em là chị nữa.", "teasing, wet eyes")], ""),
  ("Tự nghĩ", 5, ["HU1", "AN1"], "50mm two-shot", "@Hung blinks up at her; @An smiles.", [("Hung", "Thế gọi là gì?", "flustered"), ("An", "Anh tự nghĩ.", "smiling")], ""),
  ("Đôi găng", 5, ["HU1", "AN1"], "medium two-shot", "@Hung takes the grey hand-knitted gloves from his jacket and puts them into her hands.", [("Hung", "Mẹ em đan. Bên ấy rét.", "shy")], ""),
])

scene("18", "Chuyến ngoài luồng", A3, "rạng sáng 25: đầu ngõ lúc 2 giờ 30, rồi đường ra sân bay", "P7", PLACE_SOUND["P7"], [
  ("Xe vẫn chờ", 5, ["HU1"], "wide shot", "2:30 a.m. The night bus still idles at the alley mouth with its interior lights on; @Hung stands by the open door in the cold.", [], ""),
  ("Vali", 6, ["AN4", "TH2"], "medium two-shot", "@An comes out of the alley pulling a suitcase, in a navy puffer coat, the red scarf and grey knitted gloves; @Thao, a coat thrown over her pink pyjamas, hugs her tight.", [("Thao", "Mở mắt mà đi đấy!", "crying, joking")], ""),
  ("Bộ đàm gắt", 5, ["TU1"], "medium shot in the booth", "@Tu, half asleep in his chair, jolts upright and shouts into the radio.", [("Tu", "Hưng! Hai giờ sáng rồi, xe mày đang ở đâu?", "shouting")], "P4"),
  ("Cho em đi nốt", 5, ["HU1"], "50mm medium shot in the driver's seat", "@Hung holds the radio handset, calm.", [("Hung", "Anh Tú. Chuyến cuối. Cho em đi nốt.", "calm")], "P1"),
  ("Đi chậm thôi", 4, ["TU1"], "85mm close-up", "@Tu sighs, glances at the little blinking Christmas tree on his desk and presses the handset button.", [("Tu", "…Đổ dầu cho đầy. Đi chậm thôi.", "gruff, soft")], "P4"),
  ("Ghế đầu", 6, ["AN4", "HU1"], "50mm two-shot from the aisle", "@An sits in the first seat right behind the driver, eyes open, chatting; @Hung drives, listening.", [("An", "Mẹ em ở quê nuôi ba con bò. Con nào cũng tên là Vàng.", "chatty, amused")], "P1"),
  ("Bệnh nhân đầu", 5, ["AN4"], "85mm close-up", "@An, still laughing at her own story, smiles more softly and looks out at the lights.", [("An", "Bệnh nhân đầu tiên của em, ông ấy cũng thích nghe kể chuyện.", "soft")], "P1"),
  ("Cây cầu", 5, [], "wide shot", "The lit bus crosses a long empty bridge over a dark river, Christmas lights shimmering in the water.", [], "PB"),
  ("Ngủ thật", 5, ["AN4"], "100mm close-up", "@An has fallen asleep for real against the window by the first seat, mouth slightly open, gloves on, breathing deeply.", [], "P1"),
  ("Đi chậm lại", 5, ["HU1"], "85mm close-up", "@Hung looks in the mirror and smiles; he says nothing and eases off the accelerator.", [], "P1"),
])

scene("19", "Gọi hai lần", A3, "rạng sáng 25, sân bay", "P1", PLACE_SOUND["P10"], [
  ("Sân bay", 4, [], "wide shot", "Before dawn, the night bus pulls up at an empty airport departures curb, the glass facade glowing, every sign blurred.", [], "P10"),
  ("Chị ơi", 4, ["HU1"], "50mm medium shot", "@Hung turns slightly toward the first seat.", [("Hung", "Chị ơi, đến rồi.", "gentle")], ""),
  ("An ơi", 4, ["HU1"], "85mm close-up", "@Hung glances back at the passenger still sound asleep just behind him, smiles and tries again, softer, using her name for the first time.", [("Hung", "An ơi. Đến rồi.", "soft, tender")], ""),
  ("Giật mình", 4, ["AN4"], "85mm close-up", "@An jolts awake, blinking.", [("An", "Em ngủ thật à?", "embarrassed")], ""),
  ("Hai lần", 4, ["HU1"], "85mm close-up", "@Hung grins.", [("Hung", "Ngủ thật. Gọi hai lần.", "grinning")], ""),
  ("Lề đường", 5, ["AN4", "HU1"], "medium two-shot on the curb", "@Hung lifts her suitcase down onto the curb; they stand facing each other in the cold blue light.", [], "P10"),
  ("Câu khác", 5, ["HU1"], "85mm close-up", "@Hung takes a breath.", [("Hung", "Hai năm em tặng chị một câu. Hôm nay tặng câu khác.", "nervous")], "P10"),
  ("Anh đón em", 5, ["HU1"], "85mm close-up, very slow push-in", "@Hung looks straight into her eyes.", [("Hung", "Năm năm nữa, anh đón em.", "steady")], "P10"),
  ("Gọi em là gì", 4, ["AN4"], "85mm close-up", "@An hears the change of words; her eyes fill and she smiles.", [("An", "Anh vừa gọi em là gì?", "whisper, smiling")], "P10"),
  ("Em", 4, ["HU1"], "85mm close-up", "@Hung smiles, shy but sure.", [("Hung", "Em. Anh đón em.", "shy, sure")], "P10"),
  ("Sửa cổ áo", 5, ["AN4", "HU1"], "close two-shot", "@An reaches up with gloved hands and straightens his uniform collar, then rests her forehead against his chest for one breath.", [], "P10"),
  ("Cửa kính", 5, ["AN4"], "wide shot", "@An walks toward the glowing glass doors pulling her suitcase, the red scarf trailing; at the door she turns, opens her eyes theatrically wide and waves.", [], "P10"),
  ("Gương trống", 5, ["HU1"], "close-up over the driver's shoulder onto the rear-view mirror", "Back in the driver's seat, @Hung looks in the mirror: the last row is empty. Pale dawn light creeps into the bus.", [], ""),
])

scene("20", "Em chưa muốn xuống", A3, "năm năm sau, đêm Noel", "P1", BUS_SOUND, [
  ("Tuyến mở lại", 5, ["HU3"], "50mm medium shot in the driver's seat", "@Hung drives the night bus with a phone on a dashboard mount, its screen a soft unreadable glow, talking to it softly as he always did.", [("Hung", "Người ta mở lại tuyến đêm cho người làm ca đêm. Anh xin lái.", "soft, chatty")], ""),
  ("Ngủ Gật đẻ", 4, ["HU3"], "85mm close-up", "@Hung grins at the phone.", [("Hung", "Con Ngủ Gật đẻ rồi em ạ. Bốn con.", "pleased")], ""),
  ("Tàu điện xứ tuyết", 5, ["AN5"], "medium shot inside the tram", "In a snowy faraway city at dusk, @An rides a modern tram with earphones in, eyes open, smiling at the falling snow as she listens.", [], "P11"),
  ("Năm năm sau", 4, [], "wide shot", "Christmas Eve again: the hospital bus stop glittering with fairy lights, crowds heading toward the cathedral; the night bus pulls in.", [], "P2"),
  ("Ông lên xe", 5, ["OT2", "HU3"], "medium shot at the door from inside", "@OngThu, leaning on a cane, climbs aboard slowly; @Hung reaches out and gives him a hand.", [("OngThu", "Năm năm rồi đấy nhé.", "dry")], ""),
  ("Thiếu một đêm", 4, ["HU3"], "85mm close-up", "@Hung smiles toward the stop outside.", [("Hung", "Năm năm, thiếu một đêm.", "smiling")], ""),
  ("Người phụ nữ", 5, ["AN5"], "medium wide shot through the windscreen toward the stop", "A woman in a charcoal wool coat, a faded red scarf and worn grey knitted gloves walks to the stop pulling a small suitcase: @An.", [], "P2"),
  ("Ghế cuối", 5, ["AN5"], "wide shot down the aisle", "@An walks down the aisle, sits in the last row by the window, and keeps her eyes wide open, looking at the mirror.", [], ""),
  ("Trong gương", 5, ["HU3", "AN5"], "close-up over the driver's shoulder onto the rear-view mirror", "In the rear-view mirror, @An is looking straight back at @Hung; @An is seen only in the mirror.", [], ""),
  ("Gõ gậy", 5, ["OT2"], "85mm close-up", "@OngThu, in the first seat, looks from one to the other and taps his cane on the floor.", [("OngThu", "Lần này nói nhanh lên. Tôi già rồi, không chờ được.", "wry")], ""),
  ("Em ơi", 4, ["HU3"], "85mm close-up; the bus pulls up at the alley stop and the door hisses open", "@Hung looks into the mirror, warm.", [("Hung", "Em ơi, đến rồi.", "warm, tender")], ""),
  ("Không xuống", 5, ["AN5"], "medium shot", "@An stands, walks to the front and sits down in the seat beside the driver instead of getting off.", [], ""),
  ("Chưa muốn xuống", 5, ["AN5"], "85mm close-up", "@An smiles at him, sure.", [("An", "Anh lái tiếp đi. Em chưa muốn xuống.", "smiling, sure")], ""),
  ("Cửa đóng", 6, [], "wide shot from the street", "The folding door closes; the warm lit bus pulls away past the alley stop and drives on into the Christmas lights.", [], "PS"),
])
