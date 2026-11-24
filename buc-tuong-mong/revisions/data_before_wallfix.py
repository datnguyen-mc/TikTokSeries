# -*- coding: utf-8 -*-
"""Dữ liệu phim Bức Tường Mỏng — BẢN 1: nhân vật theo bộ đồ, bối cảnh, 25 cảnh và bảng shot.
Sửa ở đây (và canh_a.py / canh_b.py / canh_c.py) rồi chạy build.py để sinh KICH_BAN_CHI_TIET.md,
NHAN_VAT_FLOW.md, SHOTS.md, kich-ban/, film/cXX/*.txt."""
import os

TITLE = "Bức Tường Mỏng"

# ---------------------------------------------------------------- người: khuôn mặt + giọng
PEOPLE = {
    "Ngan": dict(name="Ngân", role="the wife, a sound engineer who records audiobooks in her home studio",
        face="a slender, quietly beautiful 35-year-old Vietnamese woman with an elegant oval face, high cheekbones, straight dark eyebrows, calm intelligent dark almond eyes, clear smooth skin, shoulder-length glossy black hair gathered in a low loose knot with a few soft strands framing her face, small pearl stud earrings, natural light makeup",
        voice="woman of 35, low calm alto, slow and precise, every word clear"),
    "Hung": dict(name="Hưng", role="the husband, a sales director at a real-estate sales company",
        face="a well-groomed 38-year-old Vietnamese man, square jaw, smooth light skin, thick black hair neatly side-parted and gelled, clean-shaven, a quick charming salesman's smile",
        voice="man of 38, smooth warm baritone, fluent like a salesman, speeds up when he lies"),
    "Diem": dict(name="Diễm", role="the new next-door neighbour, a 26-year-old online cosmetics seller who livestreams",
        face="a pretty 26-year-old Vietnamese woman, small heart-shaped face, big round eyes with long lashes, glossy long wavy chestnut-brown hair past her shoulders, pink glossy lips, carefully done makeup",
        voice="woman of 26, bright sweet fast voice, a little sing-song, turns sharp when upset"),
    "Bin": dict(name="Bin", role="Ngân and Hưng's 8-year-old son", child=True,
        face="an 8-year-old Vietnamese boy, round face, bright curious eyes, short thick black hair with a cowlick at the crown, a shy wide smile",
        voice="boy of 8, clear high child's voice, earnest"),
    "BaLua": dict(name="Bà Lụa", role="the head of the residents' committee of the apartment block",
        face="a small brisk 66-year-old Vietnamese woman, round face with sharp lively eyes, short tightly permed grey hair, fine wrinkles, gold-rimmed reading glasses",
        voice="woman of 66, quick sharp old-Hanoi voice, nosy but kind, dry humour"),
    "ChiMai": dict(name="Chị Mai", role="the director of the real-estate sales company, Hưng's boss",
        face="a composed 45-year-old Vietnamese woman, sharp straight eyebrows, a sleek chin-length black bob, minimal makeup, small gold earrings",
        voice="woman of 45, low firm businesslike voice, few words"),
    "CongChung": dict(name="Công chứng viên", role="a notary public",
        face="a 50-year-old Vietnamese man with thin steel-rimmed glasses and neatly combed greying hair",
        voice="man of 50, dry formal voice"),
    "Tuan": dict(name="Tuấn", role="Bà Lụa's grandson, the new neighbour months later",
        face="a 30-year-old Vietnamese man with a friendly round face and short black hair",
        voice="man of 30, cheerful polite voice"),
}

# ---------------------------------------------------------------- bộ đồ = nhân vật trên Flow
# code: (người, tên trên Flow, mô tả bộ đồ, cảnh dùng, ghi chú, True = bộ gốc / mã bộ gốc để sửa từ đó)
PHONES = "large black over-ear studio headphones with no logo resting around her neck"
OUTFITS = {
    "NG1": ("Ngan", "Ngân · Áo len ở nhà", "a long oversized charcoal-grey knitted cardigan over a plain cream T-shirt, loose black trousers, grey house socks, " + PHONES, "01–17, 22, 23", "Ở nhà, trong tòa nhà. Tai nghe luôn quàng cổ", True),
    "NG2": ("Ngan", "Ngân · Áo trench ra ngoài", "a camel wool trench coat over a plain white silk blouse, black straight trousers, low black heels, a small black leather handbag with no logo, hair in a neat low knot, no headphones", "18–21", "Phòng công chứng, họp cư dân", "NG1"),
    "NG3": ("Ngan", "Ngân · Áo len xanh mùa xuân", "a soft sage-green knitted sweater, light-grey loose trousers, grey house socks, hair loose to the shoulders, " + PHONES, "24, 25", "Mấy tháng sau", "NG1"),
    "HU1": ("Hung", "Hưng · Com-lê xanh", "a fitted navy-blue suit with no tie, a white dress shirt open at the collar, a brown leather belt, polished brown shoes, a plain gold wedding band on his left ring finger", "02, 05, 06, 11, 18–21", "Đi làm. Nhẫn cưới là đạo cụ: nói dối thì xoay nhẫn", True),
    "HU2": ("Hung", "Hưng · Sơ mi xắn tay", "a white dress shirt with the sleeves rolled up to the elbows and the collar open, navy suit trousers, a brown leather belt, black socks, a plain gold wedding band on his left ring finger", "01, 02, 06, 16", "Buổi tối ở căn bên (cởi áo vest)", "HU1"),
    "HU3": ("Hung", "Hưng · Polo cuối tuần", "a dark-green polo shirt, beige chinos, white sneakers, a plain gold wedding band on his left ring finger", "12", "Cuối tuần", "HU1"),
    "HU4": ("Hung", "Hưng · Sơ mi nhàu không nhẫn", "a crumpled white dress shirt untucked with the collar open, navy suit trousers, black socks, no ring on either hand, bare fingers", "23, 24", "Sau khi tháo nhẫn", "HU2"),
    "DI1": ("Diem", "Diễm · Áo lụa hồng ở nhà", "a soft blush-pink satin long-sleeved blouse, loose white wide-leg trousers, fluffy white house slippers, hair down", "01, 06, 08–10, 12, 14, 16, 17, 24", "Ở nhà, livestream", True),
    "DI2": ("Diem", "Diễm · Váy len kem", "a fitted cream knitted midi dress, a short white tweed jacket with plain buttons, small pearl earrings, beige low heels, hair down", "03–05, 15, 20–22", "Sang chơi, đi họp", "DI1"),
    "DI3": ("Diem", "Diễm · Áo trench cải trang", "an oversized beige trench coat buttoned to the neck, black trousers, flat black shoes, a black bucket hat pulled low with all her long hair tucked up under it", "18, 19", "Cải trang ở phòng công chứng. Khẩu trang đen ghi trong hành động, không vẽ vào ảnh", "DI1"),
    "BI1": ("Bin", "Bin · Áo vàng ở nhà", "a plain mustard-yellow T-shirt with no print, navy shorts, white socks", "11, 12, 25", "Ở nhà", True),
    "BI2": ("Bin", "Bin · Đồng phục đi học", "a white short-sleeved school shirt with no badge, navy shorts, a red pioneer neckerchief knotted at the collar, a small navy backpack with no logo, white socks", "02, 04", "Đi học", "BI1"),
    "BI3": ("Bin", "Bin · Đồ ngủ", "light-blue cotton pyjamas with a pattern of small white clouds, bare feet", "01, 23", "Ban đêm", "BI1"),
    "LU1": ("BaLua", "Bà Lụa · Áo len đỏ mận", "a maroon knitted cardigan over a cream blouse with tiny flowers, dark-grey trousers, black cloth shoes, gold-rimmed reading glasses on a beaded chain, holding a small blue cloth-covered notebook", "02, 07, 13, 14, 18–21, 24", "Cuốn sổ bìa xanh luôn trong tay", True),
    "CC1": ("CongChung", "Công chứng viên · Sơ mi cà vạt", "a white long-sleeved shirt and a plain dark-blue tie, dark trousers", "18", "Vai phụ 3 shot: gắn ảnh để mặt không đổi", True),
    "TU1": ("Tuan", "Tuấn · Áo hoodie xám", "a plain grey hoodie and jeans, carrying a plain brown cardboard moving box with no writing", "24", "Cháu bà Lụa, vai phụ 2 shot", True),
    "MA1": ("ChiMai", "Chị Mai · Vest đen", "a black tailored blazer over an ivory silk blouse, black trousers, black pumps, a slim black leather folder in hand", "17, 20, 21", "Giám đốc sàn", True),
}
BACK = "; seen from directly behind, back of the head and hair, shoulders and the back of the outfit clearly visible, face not visible"
for _c in [c for c in list(OUTFITS) if not c.endswith("B")]:  # mọi bộ đồ đều có ảnh trước + sau lưng
    _p, _flow, _desc, _sc, _note, _base = OUTFITS[_c]
    OUTFITS[_c + "B"] = (_p, _flow + " · Sau lưng", _desc + BACK, _sc, "Ảnh sau lưng cho góc qua vai / quay lưng", _c)

AGE_EDIT = {}

# ---------------------------------------------------------------- bối cảnh
_STUDIO = ("A small home recording studio in a converted bedroom of a mid-range Hanoi apartment: a wooden desk against the back wall, a large silver condenser microphone on a black boom arm with a round black pop filter, an audio interface with small glowing amber knobs, two small black monitor speakers, a laptop whose screen shows only a soft abstract waveform glow, a warm desk lamp, an office chair; the back wall behind the desk covered in dark-grey acoustic foam panels. "
           "Layout, always exactly the same: the wall shared with the next-door apartment is on the RIGHT side of the room as seen from the doorway, a bare plain pale-cream painted wall with nothing on it except three children's crayon drawings (a house, a cat, three dots) taped low, with no letters or writing; the door and a narrow window are always on the LEFT of frame. No readable text anywhere.")
_LIVING = ("The living-dining room of a warm, lived-in mid-range Hanoi apartment: a light-oak dining table with four chairs under a pendant lamp, a beige fabric sofa with cushions and an armchair, a low wooden TV cabinet with a switched-off dark TV and a small framed photo standing on it seen edge-on (its picture never visible), an open kitchen counter with a sink, a rice cooker and a kettle, a glass sliding door to a narrow balcony with potted plants, the front door with a wooden shoe cabinet beside it, a child's school things on a chair. No readable text anywhere.")
_BEDROOM = ("A brand-new bedroom in the next-door apartment, decorated in white and blush pink: a white double bed with fluffy pillows, a white velvet armchair, a white vanity table crowded with cosmetic bottles and boxes with blank unreadable labels, a large ring light and a phone on a tripod, warm fairy lights, a white cat bed. "
            "Layout, always exactly the same: the wall shared with the apartment next door is on the LEFT side of the room as seen from the doorway, a bare plain pale-cream painted wall with nothing on it; the bedroom door is always on the RIGHT of frame. No readable text anywhere.")
_NEWLIVING = ("The living room of the brand-new next-door apartment, showy and half unpacked: glossy white floor tiles, a white leather sofa with clear plastic film still on its arms, three unopened plain brown moving boxes with no writing, a tall white cat tree, a big vase of pink lilies, a white marble-look dining table, a sliding glass door to the balcony, an open door to the bedroom; cold bright ceiling light. No readable text anywhere.")
PLACES = {
    "PAN": _STUDIO + " Night: the black window shows distant city lights; only the desk lamp and the amber gear lights are on.",
    "PAD": _STUDIO + " Daytime: soft grey daylight from the narrow window, the desk lamp off.",
    "PBM": _LIVING + " Early morning: soft cool daylight through the balcony door.",
    "PBD": _LIVING + " Afternoon: warm low sunlight slanting through the balcony door.",
    "PBN": _LIVING + " Evening: the pendant lamp and a floor lamp on, the balcony door black with city lights.",
    "PCN": _BEDROOM + " Night: fairy lights and the ring light on, the curtains drawn.",
    "PCD": _BEDROOM + " Daytime: bright daylight through sheer white curtains.",
    "PDD": _NEWLIVING + " Daytime.",
    "PE": ("A clean, quiet 12th-floor corridor of a mid-range Hanoi apartment block: grey stone-look floor tiles, cream walls, recessed ceiling lights, two dark-wood front doors side by side with black digital keypad locks and small plain metal plates with no readable numbers, a narrow shoe rack beside each door. "
           "Layout, always exactly the same: facing the doors from the corridor, the family's door is on the LEFT and the new neighbour's door is on the RIGHT; the lift lobby is off-screen at the RIGHT end of the corridor. No readable text anywhere."),
    "PFM": ("Two narrow side-by-side balconies on the 12th floor of a Hanoi apartment block on a soft morning: waist-high steel railings, a frosted-glass privacy partition taller than a person between the two balconies with a hand-wide gap at its foot, potted green plants and a small drying rack on the family's balcony; below, Hanoi rooftops, trees and traffic in morning haze. "
            "Layout, always exactly the same: seen from the family's balcony the partition and the neighbour's balcony are on the RIGHT; seen from the neighbour's balcony they are on the LEFT."),
    "PFN": ("Two narrow side-by-side balconies on the 12th floor of a Hanoi apartment block at night: waist-high steel railings, a frosted-glass privacy partition taller than a person between them with a hand-wide gap at its foot, potted plants on the family's balcony, warm light glowing through the frosted glass from the neighbour's side; below, the city lights of Hanoi. "
            "Layout, always exactly the same: seen from the family's balcony the partition and the neighbour's balcony are on the RIGHT."),
    "PG": ("The small building-management office on the ground floor of the apartment block by day: a grey steel desk with stacks of plain folders, an old ceramic teapot and small cups on a tray, a wall board of key hooks with blank tags, an old desk fan, a window onto the lobby, fluorescent light mixed with daylight. No readable papers, signs or screens."),
    "PH": ("A modern notary office in Hanoi by day: a long pale-wood desk with a desk lamp and neat plain folders, two client chairs in front of it, a glass door and glass partitions, a row of waiting chairs, potted plants, soft daylight through blinds. No readable signs, nameplates, logos, flags or documents."),
    "PI": ("A busy Hanoi sidewalk by day outside a glass office front: rows of parked motorbikes, a big old tree with peeling bark, a street café's low plastic stools, motorbikes passing in the street; traffic drives on the right. No readable signs or number plates."),
    "PJ": ("The residents' community room on the ground floor of the apartment block on a Saturday morning: rows of grey plastic chairs with about twenty adult residents in casual clothes, all blurred and anonymous in the background, a long table at the front covered with a teal cloth, bottles of water and plain paper cups, a small table microphone, a blank white projector screen, daylight from tall windows. No banners, slogans or readable writing."),
    "PK": ("A glass-walled director's office in a real-estate sales company by day: a dark wooden desk, a city skyline of towers behind the glass, a desk lamp, plain blank folders, a closed laptop. No logos, models with labels or readable screens."),
    "PL": ("A cramped rented room at night: bare off-white walls, a narrow single bed, a plastic wardrobe, an ironing board with an iron, a single bare bulb, a small barred window. No readable text."),
    "PM": ("A small cosy rented room by day: a ring light and a phone on a tripod, a low wooden table with a few unbranded cosmetic boxes with blank labels, a white cat curled on a cushion, a window with green plants. No readable text."),
    "PN": ("The facade of a mid-range Hanoi apartment block at night seen from across the street, rows of small balconies, most windows dark; on the 12th floor two adjacent windows side by side, the LEFT one glowing warm amber, the RIGHT one glowing pink; the city hum of Hanoi below. No readable signs."),
    "PN2": ("The facade of a mid-range Hanoi apartment block at night seen from across the street, rows of small balconies; on the 12th floor two adjacent windows side by side both glowing the same warm amber. No readable signs."),
}
PLACE_VI = {
    "PAN": "NỘI · Phòng thu nhà Ngân (1205), đêm", "PAD": "NỘI · Phòng thu nhà Ngân (1205), ngày",
    "PBM": "NỘI · Phòng khách nhà Ngân, sáng sớm", "PBD": "NỘI · Phòng khách nhà Ngân, chiều", "PBN": "NỘI · Phòng khách nhà Ngân, tối",
    "PCN": "NỘI · Phòng ngủ nhà Diễm (1206), đêm", "PCD": "NỘI · Phòng ngủ nhà Diễm (1206), ngày",
    "PDD": "NỘI · Phòng khách nhà Diễm (1206), ngày", "PE": "NỘI · Hành lang tầng 12",
    "PFM": "NGOẠI · Hai ban công cạnh nhau, sáng", "PFN": "NGOẠI · Ban công, đêm",
    "PG": "NỘI · Phòng ban quản trị tầng trệt", "PH": "NỘI · Phòng công chứng", "PI": "NGOẠI · Vỉa hè trước phòng công chứng",
    "PJ": "NỘI · Phòng sinh hoạt cộng đồng (họp cư dân)", "PK": "NỘI · Văn phòng chị Mai",
    "PL": "NỘI · Phòng trọ của Hưng", "PM": "NỘI · Phòng trọ của Diễm",
    "PN": "NGOẠI · Mặt tiền chung cư, đêm (hai ô cửa vàng – hồng)", "PN2": "NGOẠI · Mặt tiền chung cư, đêm (hai ô cửa cùng vàng)",
}
PLACE_FLASH = {}

STUDIO_SOUND = "a quiet room: the soft hiss of a fan, the hum of the city far below, the faint creak of the office chair. No music."
BED_SOUND = "a quiet new bedroom: a faint air-conditioner hum, the city far below, a cat's bell now and then. No music."
PLACE_SOUND = {
    "PAN": STUDIO_SOUND, "PAD": "a quiet room by day: the city hum, a distant motorbike horn, a bird outside. No music.",
    "PBM": "a morning kitchen: a kettle ticking, a spoon on a cup, the city waking up outside. No music.",
    "PBD": "a quiet afternoon apartment: a wall clock ticking, distant traffic. No music.",
    "PBN": "an evening apartment: a rice cooker clicking, chopsticks on bowls, distant traffic. No music.",
    "PCN": BED_SOUND, "PCD": "a bright new bedroom by day: city hum, a cat's bell. No music.",
    "PDD": "a half-empty new apartment: echoing footsteps on tiles, a cat's bell, distant traffic. No music.",
    "PE": "a quiet apartment corridor: a soft ventilation hum, the distant ding of the lift. No music.",
    "PFM": "a morning breeze, distant traffic and motorbike horns far below, birds. No music.",
    "PFN": "a night breeze, the city hum far below. No music.",
    "PG": "a slow desk fan, a lobby door opening and closing, tea being poured. No music.",
    "PH": "a quiet office: air conditioning, a printer far away, pages turning. No music.",
    "PI": "a busy Hanoi street: motorbikes, horns, café chatter. No music.",
    "PJ": "a room of murmuring residents, plastic chairs creaking, a cough. No music.",
    "PK": "a quiet glass office: air conditioning, a phone line's faint hum. No music.",
    "PL": "a cramped room: the hiss of a steam iron, a neighbour's TV through the wall. No music.",
    "PM": "a small sunny room: birds outside, a cat purring. No music.",
    "PN": "the night hum of Hanoi traffic far below. No music.", "PN2": "the night hum of Hanoi, quieter. No music.",
}

LOOK = ("Feature-film cinematography for a premium Vietnamese family drama set in a Hanoi apartment block in late autumn: shot on ARRI Alexa 35 with Cooke anamorphic/i lenses, 24 fps, 16:9 full frame without letterbox bars; deliberate blocking with foreground elements and layered depth (door frames, shelves, the edge of a wall, a microphone in soft focus); "
        "motivated practical light (warm table lamps, the cool glow of city windows, small amber studio-gear lights, cold ceiling light in the new apartment); rich true-to-life Vietnamese skin tones, gentle film halation and fine 35mm grain, shallow depth of field. "
        "Restrained, truthful acting with micro-expressions, like an award-winning Asian festival film; never CGI, never a soap opera, never an advertisement. Classic film coverage: over-the-shoulder reverses, profiles and three-quarter angles, locked-off frames or a slow dolly, small natural movements; never a flat frontal news-interview framing.")

AVOID = ("Flat frontal TV-interview framing with the camera staring straight at a face; on-screen text, burned-in subtitles or captions, a lower-third title showing a character's name or age, @-handles written on screen, a TV channel logo or broadcaster bug in any corner of the frame, logos, watermarks, brand names, readable writing on paper, documents, notebooks, door plates, signs, labels, phones, laptops or screens; "
         "any cut or second camera angle; the same person appearing twice, twins, clones or look-alike doubles (a person seen in a mirror counts as their only appearance); any child other than the named boy; extra people in focus; kissing, lying in bed together, undressing or underwear; slapping, hitting, pushing, grabbing or any violence; "
         "distorted hands or fused fingers; face, hair or costume changes; plastic or waxy skin; flashing or cutting to an attached reference portrait or a plain grey studio backdrop; repeated, echoed or stuttered words; an off-screen narrator or voice-over; background music or singing with words; gliding or sliding movement, floating feet; letterbox bars; morphing faces or hands; Southern or Central Vietnamese accents.")

PLACE_AVOID = {
    "PAN": "acoustic foam on the right-hand wall; a door or window in the right-hand wall; readable text on the laptop or gear",
    "PAD": "acoustic foam on the right-hand wall; a door or window in the right-hand wall; readable text on the laptop or gear",
    "PCN": "the bare shared wall on the right of the room; readable labels; text on the phone",
    "PCD": "the bare shared wall on the right of the room; readable labels; text on the phone",
    "PE": "readable door numbers; more than two front doors in focus; a hotel corridor",
    "PJ": "banners, slogans or readable writing; children in the room",
    "PH": "readable nameplates, documents, ID cards or signs; a national flag",
    "PI": "readable shop signs or number plates; traffic driving on the left",
    "PN": "readable signs; the two lit windows far apart", "PN2": "readable signs",
}
SHOT_AVOID = {}

# ---------------------------------------------------------------- góc máy chuẩn (giữ trục: phía nhà Ngân luôn bên TRÁI bức tường, phía nhà Diễm luôn bên PHẢI)
CAM_STU = "from the studio doorway, 35mm medium-wide, locked-off: the desk and the microphone against the foam-panelled back wall in the centre, the bare pale-cream shared wall on the RIGHT of frame"
CAM_MIC = "85mm close-up of @Ngan at the desk from slightly left of the microphone, the round pop filter soft in the RIGHT foreground, the foam panels dark behind her"
CAM_WALL_N = "85mm close-up along the bare shared wall: the pale-cream wall plane recedes along the RIGHT side of the frame; @Ngan's right ear and cheek pressed flat against it, her face turned toward the camera in three-quarter, eyes lowered, listening"
CAM_WALL_D = "85mm close-up along the bare shared wall: the pale-cream wall plane recedes along the LEFT side of the frame; @Diem's left ear and cheek pressed flat against it, her face turned toward the camera in three-quarter, eyes lowered, listening"
CAM_BED = "from the bedroom doorway, 35mm medium-wide, locked-off: the bed, the vanity and the ring light, the bare pale-cream shared wall on the LEFT of frame with a white velvet armchair standing against it"
CAM_CORR = "35mm wide shot in the corridor facing the two front doors, locked-off: the family's door on the LEFT, the new neighbour's door on the RIGHT"

# ---------------------------------------------------------------- cảnh và shot
# shot: (tên, giây tối thiểu, [mã bộ đồ], camera EN, hành động EN, [(người, câu, "sắc thái EN|sắc thái VI")], bối cảnh khác cảnh hoặc "", mô tả tiếng Việt)
S = []
def scene(num, title, act, when, place, sound, shots, goal="", mood="", music="", trans=""):
    S.append(dict(num=num, title=title, act=act, when=when, place=place, sound=sound, shots=shots,
                  goal=goal, mood=mood, music=music, trans=trans))

A1, A2, A3 = "Hồi 1 · Hàng xóm mới", "Hồi 2 · Bà chị chồng", "Hồi 3 · Họp cư dân"
RING = "with his right thumb and forefinger he twists the plain gold wedding band round and round on his left ring finger"

_HERE = os.path.dirname(os.path.abspath(__file__))
for _f in ("canh_a.py", "canh_b.py", "canh_c.py"):
    _p = os.path.join(_HERE, _f)
    if os.path.exists(_p):
        exec(compile(open(_p, encoding="utf-8").read(), _p, "exec"))
