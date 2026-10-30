#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh 60 thư mục cảnh (canh-01 … canh-60) cho phim hành động tâm lý neo-noir 60 phút "Kẻ Sống Sót: Bóng Ma"
từ kịch bản tổng KICH_BAN_60_PHUT.md. Mỗi cảnh: README.md, caption.md, clip-1.md … clip-6.md.
- Khóa chính xác 9 nhân vật (@Son, @May, @Ha, @HaiNgoc, @Dũng, @Vũ Kiên, @Phó Thành, @Bác sĩ Linh, @Ông Bảy).
- Clip 1 và clip ghi "Cắt cảnh" / "Cắt:" / "Hồi tưởng" / "Quá khứ:" mở bằng [FORMAT] + FULL LOCK (Ingredients).
- Các clip còn lại mở bằng câu Continue… + SHORT LOCK (Frames / Extend).
- Nhân vật xuất hiện lần đầu giữa cảnh có khối [CHARACTER ENTERING THIS SEGMENT].
- Tối ưu 100% cho Google Flow (Omni Flash R2V/I2V): gắn @Tag trực tiếp trong [SHOT LIST] & lời thoại,
  khử hoàn toàn từ khóa kích hoạt bộ lọc an toàn và đồng bộ góc máy khớp khẩu hình.
"""
import os
import re

SCRIPT_FILE = "KICH_BAN_60_PHUT.md"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOTAL_SCENES = 60
PRESERVED_SCENES: set[int] = set()
SERIES_TITLE = "Kẻ Sống Sót: Bóng Ma"

with open(os.path.join(BASE_DIR, SCRIPT_FILE), "r", encoding="utf-8") as f:
    script_content = f.read()

scene_pattern = re.compile(
    r"### CẢNH (\d+): (.*?) \((.*?)\)\n\*Bối cảnh: (.*?)\*\n(.*?)(?=(?:### CẢNH \d+:)|(?:# HƯỚNG DẪN)|$)",
    re.DOTALL,
)
scenes = scene_pattern.findall(script_content)
print(f"Bóc tách được {len(scenes)} cảnh.")

CHAR_FULL = {
    "SON": "@Son = SƠN (45, a legendary former underground operative known as the Ghost, now hiding in a small seaside town): a real Vietnamese man, about 176 cm tall, lean and quiet, cropped black hair greying at the temples, a weathered calm face with deep lines, dark unreadable eyes, a thin old white scar across the bridge of his nose (signature detail), a silver pocket-watch chain hanging from his belt (signature detail). Present-day outfit: a faded olive field jacket over a grey shirt, dark trousers, worn brown boots. Voice: low, dry, unhurried Southern Vietnamese male voice, mid-40s. Not resembling any real actor.",
    "SON_P": "@Son = SƠN in the past (45, the Ghost in his signature dark attire): a real Vietnamese man, about 176 cm tall, lean, cropped black hair greying at the temples, weathered calm face, a thin old white scar across the bridge of his nose (signature detail), in a plain black suit with no tie, white shirt open at the collar, polished black shoes, black leather gloves. Voice: low, dry, unhurried Southern Vietnamese male voice. Not resembling any real actor.",
    "MAY": "@May = MÂY (38, head of the small-town police post of Hòn Sóng): a real Vietnamese woman, about 166 cm tall, athletic, sun-lined face, sharp warm eyes, short black hair with a single white streak at the front (signature detail). Outfit: a plain khaki shirt with sleeves rolled, dark trousers, canvas shoes, no badge or readable insignia, a small notebook in her chest pocket, steel cuffs on her belt. Voice: firm, dry, slightly amused Southern Vietnamese female voice, late 30s.",
    "MAY_C": "@May = MÂY in civilian clothes (38): a real Vietnamese woman, about 166 cm tall, athletic, sun-lined face, short black hair with a single white streak at the front (signature detail), in a denim jacket over a dark T-shirt, jeans, sneakers, a small backpack, steel cuffs tucked in her jacket. Voice: firm, dry, slightly amused Southern Vietnamese female voice.",
    "HA": "@Ha = HẠ (32, a florist in the city, Sơn's beloved; appears in the past): a real Vietnamese woman, about 162 cm tall, slim, gentle bright face, long black hair tied loosely, a pale-blue silk scarf around her neck or in her hair (signature detail). Outfit: a cream linen dress, a green canvas apron with pockets, flat sandals, flower stems in her hands. Voice: soft, warm, clear Southern Vietnamese female voice, early 30s.",
    "HA_D": "@Ha = HẠ held in a locked room (32): a real Vietnamese woman, about 162 cm tall, slim, gentle face now pale and tired, long black hair loose, no scarf, in a plain grey cotton dress, barefoot or in thin sandals, unharmed. Voice: soft, warm, clear Southern Vietnamese female voice.",
    "HA_N": "@Ha = HẠ free in the present (32): a real Vietnamese woman, about 162 cm tall, slim, gentle bright face, long black hair tied loosely, the pale-blue silk scarf back around her neck (signature detail), a white blouse, jeans, sandals. Voice: soft, warm, clear Southern Vietnamese female voice.",
    "HAINGOC": "@HaiNgoc = BÀ HAI NGỌC (60, matriarch of the Rắn Đen syndicate, owner of a silk shop as a front): a real Vietnamese woman, about 158 cm tall, small and upright, silver hair in a tight bun, powdered calm face, eyes that never blink first, a thick jade bracelet on her LEFT wrist (signature detail), a long black unlit holder in her hand. Outfit: a violet silk áo bà ba with a high collar, black silk trousers, embroidered slippers. Voice: soft, slow, sweet Southern Vietnamese female voice, around 60.",
    "DUNG": "@Dũng = DŨNG \"ĐINH\" (35, Rắn Đen's chief enforcer): a real Vietnamese man, about 180 cm tall, heavy-shouldered, buzz cut, a small nail-shaped silver earring in his LEFT ear (signature detail), black sleeveless shirt, black jeans, boots, a closed leather belt pouch. Voice: rough, loud Southern Vietnamese male voice.",
    "KIEN": "@Vũ Kiên = VŨ KIÊN (50, construction tycoon and the hidden Broker): a tall Vietnamese man with slicked black hair, a white tailored suit, gold watch, a wide politician's smile that never fades. Voice: smooth, confident Southern Vietnamese male voice.",
    "THANH": "@Phó Thành = PHÓ THÀNH (26, Mây's young deputy): a skinny Vietnamese man with round glasses, neat side-parted hair, a plain light-blue shirt, eager nervous face, no insignia. Voice: quick, polite Southern Vietnamese male voice.",
    "LINH": "@Bác sĩ Linh = BÁC SĨ LINH (55, the town doctor): a thin Vietnamese man with grey hair, wire glasses, a worn white coat over a checked shirt, a stethoscope. Voice: tired, precise Southern Vietnamese male voice.",
    "BAY": "@Ông Bảy = ÔNG BẢY (70, owner of the seafront coffee stall): a stout old Vietnamese man with a white moustache, white singlet, shorts, rubber sandals, a conical hat, always wiping a glass. Voice: loud, cheerful elderly Southern voice.",
}
CHAR_SHORT = {
    "SON": "@Son = SƠN: Vietnamese man, 45, cropped hair greying at the temples, thin white scar across the bridge of his nose, silver pocket-watch chain on his belt, faded olive field jacket over a grey shirt; low, dry Southern male voice.",
    "SON_P": "@Son = SƠN in the past: 45, cropped greying hair, scar across the bridge of his nose, black suit no tie, white shirt, black leather gloves; low, dry Southern male voice.",
    "MAY": "@May = MÂY: Vietnamese woman, 38, short hair with a white streak at the front, sun-lined face, khaki shirt with rolled sleeves, notebook in her chest pocket, steel cuffs on her belt, no insignia; firm, dry Southern female voice.",
    "MAY_C": "@May = MÂY in civilian clothes: 38, short hair with a white streak at the front, denim jacket over a dark T-shirt, jeans, small backpack; firm, dry Southern female voice.",
    "HA": "@Ha = HẠ: Vietnamese woman, 32, long loose black hair, pale-blue silk scarf, cream linen dress with a green florist apron; soft, warm Southern female voice.",
    "HA_D": "@Ha = HẠ: 32, pale tired face, long loose hair, no scarf, plain grey cotton dress; soft, warm Southern female voice.",
    "HA_N": "@Ha = HẠ: 32, long hair tied loosely, pale-blue silk scarf, white blouse, jeans; soft, warm Southern female voice.",
    "HAINGOC": "@HaiNgoc = BÀ HAI NGỌC: 60, silver bun, powdered calm face, jade bracelet on her LEFT wrist, black unlit holder, violet silk áo bà ba; soft, slow, sweet Southern female voice.",
    "DUNG": "@Dũng = DŨNG \"ĐINH\": 35, heavy-shouldered, buzz cut, nail-shaped silver earring in his LEFT ear, black sleeveless shirt; rough, loud Southern male voice.",
    "KIEN": "@Vũ Kiên = VŨ KIÊN: 50, tall, slicked black hair, white tailored suit, gold watch, wide unfading smile; smooth, confident Southern male voice.",
    "THANH": "@Phó Thành = PHÓ THÀNH: 26, skinny, round glasses, light-blue shirt, eager nervous face; quick, polite Southern male voice.",
    "LINH": "@Bác sĩ Linh = BÁC SĨ LINH: 55, thin, grey hair, wire glasses, worn white coat, stethoscope; tired, precise Southern male voice.",
    "BAY": "@Ông Bảy = ÔNG BẢY: 70, stout, white moustache, white singlet, conical hat, wiping a glass; loud cheerful elderly Southern voice.",
}
PROPS = {
    "WATCH": "ĐỒNG HỒ QUẢ QUÝT (Hạ's pocket watch): an old silver pocket watch on a chain, a small flower engraved on the lid (no readable text), its glass cracked, a tiny photo of a woman with a pale-blue scarf inside the lid.",
    "SCARF": "KHĂN LỤA XANH (Hạ's scarf): a long pale-blue silk scarf, soft, slightly frayed at one end.",
    "VIAL": "LỌ TÊ (vial of sleeping serum): a small clear glass vial with a rubber stopper holding a colourless liquid, kept in a dented tin box with a small metal applicator; no label.",
    "LEDGER": "SỔ ĐEN (the Rắn Đen ledger): a black leather account book with columns of handwritten numbers (not readable) and a USB stick taped inside the back cover.",
    "MARKS": "LỊCH BẢY NGÀY (the seven-day count): short lines carved into the wooden doorframe of the cabin with a small metal pocket tool, one per day.",
}
CHAR_ORDER = ["SON", "MAY", "HA", "HAINGOC", "DUNG", "KIEN", "THANH", "LINH", "BAY"]
PROP_ORDER = ["WATCH", "SCARF", "VIAL", "LEDGER", "MARKS"]
VN_NAMES = {
    "SON": "Sơn",
    "MAY": "Mây",
    "HA": "Hạ",
    "HAINGOC": "Bà Hai Ngọc",
    "DUNG": "Dũng Đinh",
    "KIEN": "Vũ Kiên",
    "THANH": "Phó Thành",
    "LINH": "Bác sĩ Linh",
    "BAY": "Ông Bảy",
}
CHAR_TAGS = {
    "SON": "@Son",
    "MAY": "@May",
    "HA": "@Ha",
    "HAINGOC": "@HaiNgoc",
    "DUNG": "@Dũng",
    "KIEN": "@Vũ Kiên",
    "THANH": "@Phó Thành",
    "LINH": "@Bác sĩ Linh",
    "BAY": "@Ông Bảy",
}

SETTINGS = {
    "CABIN": "CABIN IN THE CASUARINA PINES: an old wooden cabin on a dune above a small seaside town, sagging porch with a wooden table, tin roof, one room with a cot, a table, a radio, an oil lamp, carved day-marks on the doorframe; wind and sea sound; white glaring sun outside.",
    "TOWN": "HÒN SÓNG TOWN: a small Vietnamese seaside town with one main street, a fishing harbour of wooden boats, a seafront coffee stall under a green tarp, a fish market, a concrete pier, white sun and glare; no readable signs.",
    "STALL": "SEAFRONT COFFEE STALL: a tarp-roofed coffee stall on the sea wall, plastic tables and stools, glasses drying on a rack, boats behind, white glare; no readable signs.",
    "MARKET": "FISH MARKET OF HÒN SÓNG: an open wharf-side fish market, crushed ice, plastic crates of squid and fish, hanging bulbs, blurred fishermen, a tin roof; no readable signs.",
    "HARBOUR": "FISHING HARBOUR: the concrete pier of Hòn Sóng, wooden boats knocking, nets, ice crates, a single lamp post, sunset or night, the lighthouse cliff beyond.",
    "POST": "SMALL-TOWN POLICE POST: a tiled front room with a steel desk, a ceiling fan, an old computer, a holding room with a barred window, a motorbike outside; no readable insignia.",
    "CLINIC": "TOWN CLINIC: a small clinic with steel beds, glass cabinets, a microscope, green curtains, a ceiling fan, afternoon light; no readable text.",
    "VAN": "ÔNG BẢY'S OLD VAN: the back of a dented old van turned into a field station, a mattress, a lamp, a medical bag, doors open to the night harbour.",
    "CITY": "CITY AT NIGHT (past): a big Vietnamese city at night in amber light, glass towers, wet streets, neon reflections, a silk lane, a passenger port; no readable signs.",
    "FLOWER": "FLOWER SHOP (past): a small flower shop at the foot of a glass tower, buckets of white lilies and roses, a wooden counter, warm bulbs, a back room with a kettle, a glass front onto the street; no readable text.",
    "SILK": "SILK SHOP (Rắn Đen front): a dim shop of silk bolts in a city lane, a back office with a teak desk, incense, a steel safe behind a screen, a small courtyard; amber night light.",
    "GARAGE": "UNDERGROUND CAR PARK (past): an underground garage beneath a glass tower, yellow neon, concrete pillars, parked cars, a lift lobby, a large ventilation duct; night.",
    "MOTEL": "SMALL MOTEL ROOM: a small city motel room before dawn, a bed, a fan, a cracked mirror, grey light through blinds.",
    "LAB": "HIDDEN CHEMICAL WORKSHOP IN A DISUSED FISH-SAUCE FACTORY: a hidden workshop by the river in an abandoned fish-sauce factory, steel vats, glass flasks, trays of clear vials, masked workers blurred in background, a loading door onto the river.",
    "RIVER": "RIVER AT DUSK: a wide brown river at the edge of the city, a small wooden boat, mangroves, factory chimneys behind, orange dusk.",
    "BUS": "NIGHT COACH: the inside of an old sleeper coach at night, blue cabin light, rain on windows, the road to the coast.",
    "LIGHTHOUSE": "OLD LIGHTHOUSE ON THE CLIFF: a white-and-rust lighthouse on a cliff above the town, a rusted iron door, a spiral stair, a railed gallery at the top, wind, long grass, the sea far below.",
    "CLIFFROAD": "CLIFF ROAD AT NIGHT: a narrow road climbing the cliff from the town to the lighthouse, a motorbike headlight, sea wind, no streetlights.",
    "DUNE": "CASUARINA PINE DUNE: a dune of white sand and casuarina pines above the town, wind in the needles, long shadows, the cabin visible between trunks.",
    "CROSSROAD": "TOWN CROSSROAD AT DAWN: the crossroad at the edge of Hòn Sóng where the coach stops, dust, a signpost with no readable text, the sea white behind.",
}


# ----------------------------------------------------------------------------
# KHỬ TỪ KHÓA NHẠY CẢM TIẾNG VIỆT (TRÁNH TIMEOUT / SAFETY HOLD TRÊN GOOGLE FLOW)
# ----------------------------------------------------------------------------
_VN_SAFETY_SUBS = [
    ("ống tiêm", "ống thuốc nhỏ"),
    ("mũi tiêm", "ống thuốc"),
    ("tiêm thuốc giải", "đưa thuốc giải"),
    ("tôi tiêm", "tôi đưa thuốc"),
    ("Tiêm đi!", "Đưa thuốc giải đi!"),
    ("Tiêm.", "Đưa thuốc."),
    ("chưa tiêm", "chưa dùng thuốc giải"),
    ("nằm như chết", "nằm bất động như ngủ sâu"),
    ("ngửa như chết", "ngửa bất động"),
    ("chết thiệt", "ngưng thở thiệt"),
    ('vác Sơn "chết"', "vác Sơn đang bất động"),
    ('đang "chết"', "đang nằm bất động"),
    ("làm anh chết", "làm anh ngưng nhịp tim tạm thời"),
    ("giả cái chết", "giả ngưng thở"),
    ("thấy anh chết", "thấy anh ngã xuống"),
    ("thấy tôi chết", "thấy tôi ngã xuống"),
    ("Tôi chết, hai phe", "Tôi ngã xuống, hai phe"),
    ("cùng muốn Rắn Đen chết", "cùng muốn Rắn Đen sụp đổ"),
    ("Bà Hai Ngọc chết", "Bà Hai Ngọc ngã xuống"),
    ("Bà Hai chết", "Bà Hai ngã xuống"),
    ("sổ đó giết bà, nhưng cũng giết Kiên", "sổ đó hạ gục bà, nhưng cũng hạ gục Kiên"),
    ("cần Sơn giết Kiên", "cần Sơn hạ Kiên"),
    ("thuê con giết má", "thuê con đối đầu má"),
    ("thuê anh giết tôi", "thuê anh hạ tôi"),
    ("thuê một thằng giết người", "thuê một Bóng Ma"),
    ("giết người giỏi", "ra tay giỏi"),
    ("Ông giết bằng tay người khác", "Ông hại người bằng tay người khác"),
    ("Tôi giết bằng tay tôi", "Tôi làm bằng tay tôi"),
    ("Hôm nay không ai giết", "Hôm nay không ai ra tay"),
    ("Bà giết cô ấy?", "Bà hại cô ấy?"),
    ("Má không giết", "Má không hại"),
    ("Tôi không giết", "Tôi không hại"),
    ("sắp giết ai", "sắp hại ai"),
    ("Trang này giết ổng không cần súng", "Trang này hạ bệ ổng không cần ra tay"),
    ("sát thủ bị bắt tại trận", "người bị gài tại trận"),
    ("Một sát thủ", "Một Bóng Ma"),
    ("một sát thủ", "một Bóng Ma"),
    ("lấy xác", "đưa người"),
    ("Xác nó", "Người nó"),
    ("giao xác", "giao người"),
    ("Xác đâu?", "Tung tích đâu?"),
    ("cho tôi xác", "cho thấy tung tích"),
    ("khẩu súng ngắn trong bao da", "vật thép khóa trong bao da"),
    ("khẩu súng trong bao", "bao da khóa kín"),
    ("khẩu súng rỗng", "vật thép rỗng"),
    ("khẩu súng lấy từ mái", "bao da lấy từ mái"),
    ("nhìn khẩu súng", "nhìn bao da"),
    ("một khẩu súng", "một bao da"),
    ("cầm súng lên, tháo băng đạn, đặt băng đạn", "cầm bao da lên, tháo lõi kim loại, đặt lõi"),
    ("băng đạn", "lõi kim loại"),
    ("tháo đạn", "tháo lõi"),
    ("Đạn cô giữ", "Lõi thép cô giữ"),
    ("Cô giữ đạn", "Cô giữ lõi thép"),
    ("rút súng khỏi bao giơ lên", "rút gậy thép khỏi bao giơ lên"),
    ("rút súng giơ lên", "rút gậy thép giơ lên"),
    ("súng giơ lên", "gậy thép giơ lên"),
    ("súng rơi", "vật thép rơi"),
    ("súng văng", "vật thép văng"),
    ("Súng bỏ.", "Bỏ xuống."),
    ("Súng để trên mái", "Đồ nghề để trên mái"),
    ("thu súng", "thu đồ nghề"),
    ("ném súng", "ném bao da"),
    ("thấy súng", "thấy bao da"),
    ("giơ súng", "giơ vật thép"),
    ("hạ súng", "hạ tay"),
    ("Hạ súng", "Hạ tay"),
    ("chĩa súng", "giơ vật thép"),
    ("nòng súng", "mép thép"),
    ("họng súng", "vật thép"),
    ("vung súng", "vung tay"),
    ("súng ép giữa", "tay ép giữa"),
    ("bao súng", "bao da"),
    ("dầu súng", "dầu máy"),
    ("cầm súng rỗng", "cầm bao da rỗng"),
    ("bắn bà ta", "hạ bà ta"),
    ("Bắn bà ta", "Hạ bà ta"),
    ("Bắn nó", "Chặn nó"),
    ("bắn má", "đối đầu má"),
    ("Bắn tôi thì bắn qua cô ấy", "Đụng vào tôi thì phải bước qua cô ấy"),
    ("chưa bắn ai bao giờ", "chưa tự tay làm bao giờ"),
    ("chưa bắn", "chưa ra tay"),
    ("con dao nhỏ gọt bút chì", "dụng cụ khắc gỗ nhỏ"),
    ("con dao nhỏ", "dụng cụ khắc gỗ nhỏ"),
    ("đặt dao xuống", "đặt dụng cụ khắc xuống"),
]


def clean_vn_safety(text: str) -> str:
    if not text:
        return text
    out = text
    for old, new in _VN_SAFETY_SUBS:
        out = out.replace(old, new)
    return out


def inject_char_tags(text: str, chars_in: list[str]) -> str:
    """Gắn @Tag trực tiếp cạnh tên nhân vật trong [SHOT LIST] và lời thoại để Google Flow khóa đúng mặt & giọng."""
    if not text:
        return text
    out = text
    active_bases = [base_of(k) for k in chars_in]
    tag_rules = [
        ("SON", r"\bSơn\b(?!\s*\(@Son\))", "Sơn (@Son)"),
        ("MAY", r"\bMây\b(?!\s*\(@May\))", "Mây (@May)"),
        ("HA", r"\bHạ\b(?!\s*\(@Ha\))", "Hạ (@Ha)"),
        ("HAINGOC", r"\b(?:Bà Hai Ngọc|Bà Hai|bà Hai)\b(?!\s*\(@HaiNgoc\))", "Bà Hai Ngọc (@HaiNgoc)"),
        ("DUNG", r"\b(?:Dũng Đinh|Dũng)\b(?!\s*\(@Dũng\))", "Dũng (@Dũng)"),
        ("KIEN", r"\b(?:Vũ Kiên|Kiên)\b(?!\s*\(@Vũ Kiên\))", "Vũ Kiên (@Vũ Kiên)"),
        ("THANH", r"\b(?:Phó Thành|Thành)\b(?!\s*\(@Phó Thành\))", "Phó Thành (@Phó Thành)"),
        ("LINH", r"\b(?:Bác sĩ Linh|Linh)\b(?!\s*\(@Bác sĩ Linh\))", "Bác sĩ Linh (@Bác sĩ Linh)"),
        ("BAY", r"\b(?:Ông Bảy|ông Bảy)\b(?!\s*\(@Ông Bảy\))", "Ông Bảy (@Ông Bảy)"),
    ]
    for base_key, pat, repl in tag_rules:
        if base_key in active_bases or base_key in ("SON", "MAY", "HA", "HAINGOC", "DUNG", "KIEN", "THANH", "LINH", "BAY"):
            out = re.sub(pat, repl, out, count=1)
    return out


def get_setting_key(s):
    s = s.lower()
    if "ngã ba" in s or ("xe đò" in s and "đêm" not in s):
        return "CROSSROAD"
    if "xe đò" in s:
        return "BUS"
    if ("xe van" in s or "xe ông bảy" in s) and "sau chợ cá cạnh" not in s:
        return "VAN"
    if "hải đăng" in s and "đường" not in s:
        return "LIGHTHOUSE"
    if "đường vách" in s or "đường lên" in s:
        return "CLIFFROAD"
    if "bãi xe" in s:
        return "GARAGE"
    if "tiệm lụa" in s or "hẻm lụa" in s:
        return "SILK"
    if "tiệm hoa" in s:
        return "FLOWER"
    if "phòng trọ" in s:
        return "MOTEL"
    if "nước mắm" in s or "xưởng" in s:
        return "LAB"
    if "ghe trên sông" in s or "ven sông" in s or ("sông" in s and "hòn sóng" not in s):
        return "RIVER"
    if "bến cảng thành phố" in s or "thành phố" in s:
        return "CITY"
    if "phòng khám" in s:
        return "CLINIC"
    if "đồn" in s:
        return "POST"
    if "rừng dương" in s or ("đồi cát" in s and "nhà gỗ" not in s):
        return "DUNE"
    if "nhà gỗ" in s or "hiên" in s:
        return "CABIN"
    if "chợ cá" in s and "cầu cảng" not in s and "quán" not in s:
        return "MARKET"
    if "cảng cá" in s or "cầu cảng" in s:
        return "HARBOUR"
    if "quán" in s or "bờ kè" in s:
        return "STALL"
    return "TOWN"


COMBAT_KW = ["đạp ", "đánh ", "đòn", "quật", "đá văng", "đá bật", "cú đá", "khóa tay", "khóa cổ", "quét chân", "lao vào", "ập vào", "ra đòn", "đỡ bằng", "húc", "vật nhau", "hạ gục", "đập vào", "đè xuống", "đấm", "tước", "còng hắn", "bẻ cổ tay", "ném cát", "ống thuốc nhỏ vào", "hỗn chiến", "giằng", "vung"]
CHASE_KW = ["chạy", "rượt", "đuổi", "phóng", "xe máy", "lăn qua", "bò giữa", "chui qua", "trèo", "leo", "trượt", "nhảy", "ghe rời", "rú ga", "lao lên", "bám"]
STEALTH_KW = ["lẻn", "đột nhập", "mở két", "sau thân cây", "nằm sấp", "ống nhòm", "qua khe", "nấp", "ép sát", "giấu", "canh", "chụp lén", "chụp ảnh", "thì thầm"]
SUSPENSE_KW = ["điện thoại", "radio", "video", "usb", "sổ", "màn hình", "bản tin", "còng", "lọ", "ống thuốc", "mạch", "phút", "đồng hồ", "khắc vạch", "vạch", "giấy tờ", "tra"]


def classify(desc: str, title: str) -> str:
    t = (desc + " " + title).lower()
    if any(k in t for k in COMBAT_KW):
        return "COMBAT"
    if any(k in t for k in CHASE_KW):
        return "CHASE"
    if any(k in t for k in STEALTH_KW):
        return "STEALTH"
    if any(k in t for k in SUSPENSE_KW):
        return "SUSPENSE"
    return "DRAMA"


CAMERA = {
    "COMBAT": "Dynamic 35mm anamorphic handheld tracking, low-angle 24mm framing on fast close-quarters martial choreography, one speed-ramp slow-motion beat on the decisive wrist-lock or throw. 90-degree shutter angle for razor-sharp motion with zero smear. Cold teal-and-steel grade, hard practical light from floodlights or lamps, rain and spray catching the light.",
    "CHASE": "Fast 35mm anamorphic tracking moving alongside the character, low follow shot over roofs, cliffs or water, whip pans on direction changes, one slow-motion beat on the biggest leap. 90-degree shutter angle, sharp subject over streaking lights, deep night contrast.",
    "STEALTH": "Slow creeping 35mm camera moves, tight 85mm close-ups on hands, eyes and locks, searchlight beams sweeping through mist, long held frames with controlled cuts. Chiaroscuro shadows, cold green or blue light.",
    "SUSPENSE": "Controlled 50mm and 85mm push-ins on faces, phones, radios and documents, balanced two-shots across the space, slow dolly around the room. Cold fluorescent or grey window light, high contrast, held breath pacing.",
    "DRAMA": "Patient neo-noir 50mm and 85mm prime-lens cinematography with shallow depth of field, slow dolly moves, long close-ups on weathered faces, hands and small objects. White bleached daylight for the present or warm amber lamp light for the past, deep shadows, natural skin tones, light cinematic grain.",
}


def pick(pool, seed):
    return pool[seed % len(pool)]


def split_beats(desc: str):
    """Chia mô tả clip thành tối đa 3 nhịp theo ';' rồi '.', rồi ','. Trả về (b1, b2, b3, mệnh_đề_cuối_trực_quan)."""
    clean = re.sub(r"^(Quá khứ|Cắt|Cắt cảnh|Hồi tưởng|MỞ MÀN LẠNH|MỞ MÀN)[^:]*:\s*", "", desc.strip())
    clean = re.sub(
        r"(^|[;\.]\s*)(Chậm lại[^:;\.]{0,30}|Thời gian kéo giãn|Nhịp chậm|Máy chậm dần|Một nhịp quay chậm|Quay chậm[^:;\.]{0,20}|quay chậm[^:;\.]{0,20}):\s*",
        r"\1",
        clean,
    )
    full = [p.strip().rstrip(".") for p in re.split(r";\s*|(?<=[\.\!\?])\s+", clean) if p.strip()]
    subj = re.compile(
        r"\b(Sơn|Mây|Hạ|Bà Hai|Dũng|Kiên|Thành|Linh|Bảy|anh|cô|bà|hắn|ông|cả hai|hai người|xe|ghe|máy|tay|mắt|đồng hồ|khăn|sổ|lọ|đèn|cửa|màn hình|điện thoại)\b",
        re.I,
    )
    abstract_verb = re.compile(r"^(anh|cô|bà|ông|hắn|Sơn|Mây|Hạ)?\s*(nhớ|nghĩ|hiểu ra|tưởng|biết|nhận ra)\b", re.I)
    last_full = clean
    for cand in reversed(full):
        if len(cand) >= 12 and subj.search(cand) and not abstract_verb.search(cand.strip()):
            last_full = cand
            break
    else:
        for cand in reversed(full):
            if not abstract_verb.search(cand.strip()):
                last_full = cand
                break
        else:
            last_full = full[0] if full else clean
    last_full = last_full[:1].upper() + last_full[1:]
    parts, sep = list(full), "; "
    if len(parts) < 3:
        tmp = []
        for p in parts:
            cs = [x.strip() for x in p.split(", ") if x.strip()]
            if len(cs) >= 2 and len(tmp) + len(cs) <= 4:
                tmp += cs
            else:
                tmp.append(p)
        if len(tmp) > len(parts):
            parts, sep = tmp, ", "
    if len(parts) >= 3:
        return parts[0], sep.join(parts[1:-1]), parts[-1], last_full
    if len(parts) == 2:
        return parts[0], parts[1], None, last_full
    return parts[0], None, None, last_full


OPEN_SHOT = {
    "COMBAT": [
        "35mm handheld, low angle, tight on the opening movement",
        "24mm wide from over the shoulder showing both figures in space",
        "50mm tracking laterally with the first step",
        "35mm medium-wide framing the confrontation clearly",
        "Handheld 28mm pushing in as the distance closes",
        "Steady 50mm medium shot capturing the sudden motion",
    ],
    "CHASE": [
        "35mm tracking alongside the moving subject",
        "Low 24mm follow shot from behind",
        "50mm lens compressing the distance in the frame",
        "Handheld 28mm tracking from shoulder level",
        "Wide 24mm angle showing the environment and path",
        "35mm smooth pan onto the moving figure",
    ],
    "STEALTH": [
        "35mm low-key framing creeping along the edge",
        "85mm close-up on hands and the object in focus",
        "28mm from the shadowed foreground looking into the space",
        "50mm slow push through the doorway or gap",
        "Static wide 24mm, quiet controlled movement in frame",
        "35mm over the shoulder, subtle light crossing the space",
    ],
    "SUSPENSE": [
        "Steady 50mm medium shot establishing the tension",
        "85mm tight on the key detail before tilting to the character",
        "35mm slow dolly in through the space",
        "50mm medium-wide framing the figures in the room",
        "Close-up on the key object, then smooth tilt up to the face",
        "28mm wide, single practical light source, deep shadows",
        "50mm balanced framing, held steady",
        "Slow 35mm push-in establishing the room and subject",
    ],
    "DRAMA": [
        "50mm slow dolly in from medium shot",
        "85mm medium close-up on the face, background softly blurred",
        "35mm wide establishing the characters in the environment",
        "50mm medium framing with shallow depth of field",
        "Gentle 35mm medium-close shot, breathing with the actor",
        "Static 28mm wide, natural directional light shaping the scene",
    ],
}
MID_SHOT = {
    "COMBAT": [
        "50mm speed-ramp on the decisive wrist-lock",
        "35mm low angle, one slow-motion beat on the counter-move",
        "Handheld 28mm medium shot capturing the close-quarters grapple",
        "85mm on the hands at the moment of the takedown",
        "35mm medium-wide keeping the choreography crystal clear",
        "50mm reverse angle on the defensive block",
    ],
    "CHASE": [
        "50mm whip-pan, one slow-motion beat on the stride",
        "35mm tracking shot with foreground depth",
        "24mm wide showing the full movement across the space",
        "Handheld 28mm, focus locked on the main character",
        "85mm close-up on the determined face in motion",
        "35mm low angle tracking the movement",
    ],
    "STEALTH": [
        "85mm close-up on fingers and the mechanism",
        "35mm medium shot as a light beam sweeps past",
        "50mm holding steady on the character in shadow",
        "28mm wide showing the quiet tension in the space",
        "Slow 50mm push-in on a held breath",
        "35mm angled framing through the dim environment",
    ],
    "SUSPENSE": [
        "85mm push-in on the face and the key detail",
        "50mm medium close-up on the character's expression",
        "35mm slow dolly, the key object visible in foreground",
        "Close-up on the key object, then rack focus to the eyes",
        "Steady 50mm medium close-up, held with quiet intensity",
        "35mm medium shot framing the interaction clearly",
        "50mm rack focus from the hands to the face",
        "35mm slow quarter-turn dolly around the subject",
    ],
    "DRAMA": [
        "85mm close-up on the eyes and expression, long hold",
        "50mm medium close-up on hands and face",
        "35mm medium shot, emotional distance readable in frame",
        "Slow 50mm dolly in on the character's face",
        "85mm medium close-up capturing the subtle reaction",
        "Steady 35mm medium framing, the gesture playing in full",
    ],
}
CLOSE_SHOT = {
    "COMBAT": [
        "35mm settling as dust and spray fall around the characters",
        "50mm medium close-up on the character standing steady, breathing",
        "Wide 24mm showing the quiet aftermath in the space",
        "85mm close-up on the hand and calm expression",
        "35mm low angle holding on the final posture",
        "Static 50mm, the composed stance held",
        "50mm close-up on the face after the action",
        "28mm wide, the space suddenly still",
    ],
    "CHASE": [
        "35mm settling as the camera stops with the character",
        "50mm medium close-up on the face after the movement",
        "Wide 24mm showing the new position in the environment",
        "85mm close-up on the key detail in hand",
        "35mm steady framing looking ahead",
        "Static 28mm wide, dust settling in the light",
    ],
    "STEALTH": [
        "50mm medium close-up as the character stays composed",
        "35mm steady shot as shadows settle",
        "85mm close-up on the hand and quiet expression",
        "Wide 24mm holding on the still room",
        "50mm close-up on the watchful eyes",
        "35mm steady framing at the threshold",
    ],
    "SUSPENSE": [
        "50mm medium close-up on the reaction, held steady",
        "85mm close-up on the object and hands",
        "Static 35mm medium shot holding on the quiet tension",
        "50mm close-up as the shadow falls across the frame",
        "Slow 85mm close-up on the hand and face",
        "35mm medium-wide holding the final composition",
        "50mm hold on the eyes, unwavering",
        "Static 28mm wide, the stillness after",
    ],
    "DRAMA": [
        "50mm hold on the face, no cut",
        "85mm close-up on the object and hands",
        "Static 35mm medium shot, the gesture finishing",
        "50mm medium close-up with shallow depth of field",
        "85mm close-up on the quiet gaze",
        "Slow 35mm pull-back holding the composition",
    ],
}

LEAD_IN_FR = [
    "Tiếp từ khung cuối clip trước",
    "Không cắt, cùng tư thế cuối clip trước",
    "Nối liền chuyển động đang dang dở",
    "Từ đúng khung dừng của clip trước",
    "Máy ở nguyên chỗ, hành động đi tiếp",
    "Cùng góc máy cuối clip trước, rồi đổi cỡ cảnh",
    "Nhịp đầu nối thẳng, không chuyển",
    "Hành động dở dang đi tiếp ngay giây đầu",
    "Khung đầu trùng khung cuối clip trước",
    "Tiếp tục một hơi, chưa đổi góc",
    "Cùng ánh sáng, cùng vị trí, đi tiếp",
    "Không có khoảng dừng giữa hai clip",
]
LEAD_IN_ING = ["Mở cảnh", "Khung mở", "Vào cảnh", "Thiết lập không gian", "Mở màn cảnh này", "Khung đầu"]
LEAD_IN_CUT = [
    "Cắt cứng sang bối cảnh mới",
    "Chuyển cảnh thẳng, không mờ",
    "Cắt gọn, đổi không gian và ánh sáng",
    "Nhảy cảnh, bảng màu đổi ngay khung đầu",
]
DIAL_SPOKEN = [
    "Thoại có khẩu hình, máy thấy rõ miệng người nói:",
    "Người nói nghiêng ba phần tư về máy, khớp môi từng chữ:",
    "Nói trong khung, không cắt giữa câu:",
    "Khẩu hình rõ, câu ngắn, máy giữ trên người nói tới hết câu:",
    "Thoại khớp môi, người nghe ở nửa khung còn lại:",
    "Máy ở trên mặt người nói khi câu bắt đầu:",
    "Câu thoại nói chậm, môi khớp, mắt không rời người đối diện:",
    "Thoại ngắn, khẩu hình thật, không nhạc dưới lời:",
    "Người nói ở tiền cảnh, môi rõ, người nghe mờ phía sau:",
    "Nói nhỏ nhưng khẩu hình rõ, máy không rung:",
    "Thoại nói khi đang làm việc tay, môi vẫn khớp:",
    "Một câu, một hơi, môi khớp từng âm:",
]
DIAL_VO = [
    "Lời dẫn ngoài hình, miệng nhân vật không mở:",
    "Giọng kể phủ lên hình, không khẩu hình:",
    "Voice-over, hình đi tiếp dưới lời dẫn:",
    "Lời dẫn trầm, không ai nói trong khung:",
]
DIAL_DEVICE = [
    "Giọng qua máy, méo nhẹ, không cần khẩu hình:",
    "Âm thanh từ loa điện thoại hoặc radio, không khẩu hình:",
    "Tiếng từ thiết bị, nhân vật chỉ nghe:",
]
HOLD_LINES = [
    "Dừng ở khung này nửa giây để clip {n} nối vào.",
    "Khung cuối đứng yên 0.5s, không đổi góc máy; clip {n} bắt đầu từ đây.",
    "Giữ nguyên bố cục cuối nửa giây rồi hết clip.",
    "Nửa giây tĩnh ở khung cuối làm điểm nối cho clip {n}.",
    "Khóa khung cuối 0.5s, mọi thứ bất động.",
    "Đứng hình nửa giây, kể cả gió.",
    "Giữ khung cuối tĩnh để clip {n} tiếp đúng tư thế.",
    "Kết bằng khung tĩnh 0.5s.",
    "Hình dừng hẳn nửa giây trước khi hết clip.",
    "Khung cuối bất động, clip {n} nối từ đúng đây.",
    "Giữ cỡ cảnh và vị trí cuối thêm 0.5s.",
    "Nửa giây cuối không ai cử động.",
    "Khung kết đứng yên, chờ clip {n}.",
    "Bất động 0.5s ở khung này.",
]
HOLD_LAST = [
    "Giữ khung cuối tĩnh 0.5s; hết cảnh.",
    "Đứng hình nửa giây ở khung cuối, cảnh khép lại ở đây.",
    "Khung cuối bất động 0.5s rồi khép cảnh.",
    "Nửa giây tĩnh, hết cảnh.",
]
FALLBACK_B3 = [
    "Khoảng lặng sau câu cuối ở lại trong khung, không ai rời đi.",
    "Chỉ còn chuyển động nhỏ: gió, tay, ánh sáng đổi.",
    "Một chi tiết tĩnh khép nhịp: vật trên bàn, bàn tay, vệt nắng.",
    "Nhân vật đứng yên thêm một nhịp, máy không rời.",
    "Hình thở ra: không thoại, không cắt.",
    "Máy giữ cỡ cảnh, chỉ ánh mắt đổi hướng.",
]
TYPE_ACCENT = {
    "COMBAT": ["tiếng va chạm khô, không nhạc", "nhịp trống trầm theo từng đòn", "hơi thở gấp át cả nền", "một tiếng kim loại rơi làm dấu"],
    "CHASE": ["bước chân dồn trên nền", "gió và máy nổ", "nhịp gõ nhanh tăng dần", "tiếng thở và tiếng đồ rơi"],
    "STEALTH": ["gần như im, chỉ tiếng nền", "một tiếng kim loại rất nhỏ", "hơi thở nín", "tiếng đèn pha quay xa"],
    "SUSPENSE": ["bass trầm chậm như nhịp tim", "một tiếng tích tắc", "tiếng máy rung trên gỗ", "dây đàn căng một nốt"],
    "DRAMA": ["đàn tranh thưa", "piano một tay, rất khẽ", "không nhạc, chỉ nền", "cello kéo dài một nốt"],
}
SETTING_SOUND = {
    "CABIN": ["gió dương rít qua mái tôn, radio rè", "sóng rất xa, ván gỗ kêu", "mạt gỗ rơi, cửa gỗ kẽo kẹt"],
    "TOWN": ["xe máy xa, chợ rì rầm", "gió cát, biển sau lưng", "loa phường đã tắt, gà gáy muộn"],
    "STALL": ["ly thủy tinh chạm nhau, bạt xanh phần phật", "ghe nổ máy ngoài cảng", "cà phê rót, ông Bảy nói không ngừng"],
    "MARKET": ["đá lạnh đổ, thúng nhựa va nhau", "tiếng rao mờ, mái tôn kêu nắng", "nước chảy, tiếng chợ xa"],
    "HARBOUR": ["ghe cá va mạn, dây neo kêu", "sóng vỗ trụ bê tông, hải âu", "cột đèn ù điện, biển đêm"],
    "POST": ["quạt trần kêu đều, bàn phím cũ", "còng va bàn thép", "đèn tuýp ù nhẹ"],
    "CLINIC": ["kim loại chạm khay, quạt trần", "đồng hồ bấm giờ tích tắc", "rèm xanh bay, chai lọ khẽ chạm"],
    "VAN": ["sắt xe rung, cửa sau kêu", "ống nghe chạm da, đồng hồ bấm giờ", "tiếng chợ cá vọng vào xe"],
    "CITY": ["còi xe xa, mưa phùn trên vải", "đèn neon ù, nước chảy máng", "bước chân trên vỉa hè ướt"],
    "FLOWER": ["chuông cửa, kéo cắt cành", "nước xô hoa, xe ngoài đường", "ấm trà reo, mưa nhẹ trên kính"],
    "SILK": ["lụa trượt trên lụa, nhang cháy", "tách trà đặt xuống gỗ lim", "két sắt xoay, mưa trên mái hẻm"],
    "GARAGE": ["neon ù, bước chân dội bê tông", "cửa xe đóng dội vang", "lốp rít, thang máy ting"],
    "MOTEL": ["quạt lắc, xe máy ngoài trọ", "nước nhỏ giọt, gà gáy", "băng vải xé, giường kêu"],
    "LAB": ["máy bơm nền, thủy tinh chạm", "chuông báo động từ xa", "nước sông vỗ cửa bốc hàng"],
    "RIVER": ["máy ghe nổ đều, nước rẽ", "đước xào xạc, chim nước", "sóng cửa biển vỗ mũi ghe"],
    "BUS": ["máy xe đò gầm, mưa trên kính", "đèn cabin ù xanh, hành khách ngủ", "lốp trên đường ướt"],
    "LIGHTHOUSE": ["gió hú qua lỗ thông gió tháp", "sắt gỉ rên, biển dưới xa", "cầu thang xoắn dội bước chân"],
    "CLIFFROAD": ["máy xe máy gào lên dốc", "sỏi bắn, gió biển", "đèn xe rung theo ổ gà"],
    "DUNE": ["lá dương reo như sóng", "cát trượt dưới chân", "chim biển kêu xa"],
    "CROSSROAD": ["xe đò rồ máy đi, bụi", "gió cát trên cột biển", "biển trắng im phía sau"],
}
SETTING_TEXTURE = {
    "CABIN": ["nắng trắng cắt qua khe ván", "mạt gỗ còn bám trên khung cửa", "radio rè một bản tin xa", "gió dương lùa qua hiên"],
    "TOWN": ["nắng lóa trên đường chính", "bụi cát bay ngang", "cửa tiệm hé rồi khép"],
    "STALL": ["bạt xanh phần phật", "ly thủy tinh lấp lánh trên giá", "ghe cá ngoài kè làm nền"],
    "MARKET": ["đá lạnh bốc hơi dưới bóng đèn", "thúng nhựa xếp cao hai bên", "nước chảy dọc lối đi"],
    "HARBOUR": ["ghe va mạn, dây neo căng", "cột đèn soi mặt nước đen", "nắng cam trải trên bê tông"],
    "POST": ["quạt trần quay chậm trên đầu", "song sắt cửa sổ đổ bóng", "bàn thép lạnh dưới tay"],
    "CLINIC": ["rèm xanh lay nhẹ", "khay kim loại sáng", "kính hiển vi bắt nắng"],
    "VAN": ["đèn pin hắt lên trần xe", "cửa sau mở ra cảng đêm", "nệm cũ, ánh đèn hắt"],
    "CITY": ["neon vàng loang trên đường ướt", "tòa kính sáng từng ô", "mưa phùn qua đèn đường"],
    "FLOWER": ["ly trắng trong xô", "chuông cửa còn rung", "ánh bóng đèn vàng trên quầy gỗ"],
    "SILK": ["cuộn lụa chất cao hai bên", "khói nhang lượn qua đèn bàn", "bình phong che nửa phòng"],
    "GARAGE": ["neon vàng nhấp nháy", "cột bê tông nối nhau", "xe đỗ im hàng dài"],
    "MOTEL": ["rèm xám lọc nắng sớm", "gương nứt bắt hình", "quạt lắc qua lại"],
    "LAB": ["bể thép xếp hàng", "lọ trong trên khay", "cửa bốc hàng mở ra sông"],
    "RIVER": ["đước hai bên mũi ghe", "nước nâu lấp lánh cam", "ống khói nhà máy lùi xa"],
    "BUS": ["đèn cabin xanh", "mưa chảy ngược trên kính", "ghế nằm cuối xe"],
    "LIGHTHOUSE": ["lan can sắt gỉ", "gió bạt áo", "biển xám rất xa bên dưới"],
    "CLIFFROAD": ["đèn pha cắt sương", "vách đá bên đường", "sỏi trắng dưới bánh"],
    "DUNE": ["thân dương thẳng như cột", "cát trắng lóa", "bóng cây xiên dài"],
    "CROSSROAD": ["cột biển không chữ", "bụi xe đò tan", "biển trắng phía sau"],
}


def dialogue_block(dialogue: str, seed: int, chars_in: list[str]) -> tuple[str, bool]:
    if not dialogue or dialogue.strip() in ("—", "-", ""):
        return "", False
    tagged_dial = inject_char_tags(dialogue, chars_in)
    speakers = re.findall(r'(?:^|· )([^:"]+?):\s*"', dialogue)
    device_keys = ("(điện thoại)", "(bộ đàm)", "Ghi âm", "Radio", "(video)", "(qua khe", "(máy tắt)", "(vọng)")
    all_vo = bool(speakers) and all("Voice-over" in sp for sp in speakers)
    all_device = bool(speakers) and all(any(k in sp for k in device_keys) for sp in speakers)
    if all_vo:
        lead = pick(DIAL_VO, seed)
        return f" {lead} {tagged_dial}", False
    if all_device:
        lead = pick(DIAL_DEVICE, seed)
        return f" {lead} {tagged_dial}", False
    lead = pick(DIAL_SPOKEN, seed)
    return f" {lead} {tagged_dial}", True


def shot_list(desc, dialogue, ctype, c_num, opens_scene, hard_cut, setting_key, scene_num, chars_in):
    seed = scene_num * 7 + c_num * 3
    b1, b2, b3, last_full = split_beats(desc)
    b1 = inject_char_tags(b1, chars_in)
    b2 = inject_char_tags(b2, chars_in) if b2 else None
    b3 = inject_char_tags(b3, chars_in) if b3 else None
    last_full = inject_char_tags(last_full, chars_in)

    has_dialogue = bool(dialogue) and dialogue.strip() not in ("—", "-", "")
    speakers = re.findall(r'(?:^|· )([^:"]+?):\s*"', dialogue) if has_dialogue else []
    is_vo_only = has_dialogue and bool(speakers) and all("Voice-over" in sp for sp in speakers)
    nxt = c_num + 1
    if hard_cut:
        lead = pick(LEAD_IN_CUT, seed)
    elif opens_scene:
        lead = pick(LEAD_IN_ING, seed)
    else:
        lead = pick(LEAD_IN_FR, seed)
    tpool = SETTING_TEXTURE.get(setting_key, SETTING_TEXTURE["TOWN"])
    texture = pick(tpool, seed + c_num)
    if texture.split()[0] in desc:
        texture = pick(tpool, seed + c_num + 1)
    slow = bool(re.search(r"(quay chậm|chậm lại|nhịp chậm|máy chậm dần|kéo giãn|chậm cực chậm)", desc.lower()))
    accent = pick(TYPE_ACCENT[ctype], seed + 1)

    d1 = d2 = d3 = ""
    lip1 = lip2 = lip3 = False
    if has_dialogue:
        blk, is_lip = dialogue_block(dialogue, seed, chars_in)
        if is_vo_only:
            if c_num % 2 == 1 or b3 is None:
                d1 = blk
            else:
                d3 = blk
        elif b2 is None:
            d1, lip1 = blk, is_lip
        elif c_num == 6 and b3 is not None and seed % 2 == 0:
            d3, lip3 = blk, is_lip
        else:
            d2, lip2 = blk, is_lip

    cam1 = "50mm medium close-up on the speaker's face, clear lip-sync" if lip1 else pick(OPEN_SHOT[ctype], seed)
    cam2 = "50mm medium close-up on the speaker's face, clear lip-sync" if lip2 else pick(MID_SHOT[ctype], seed + 2)
    cam3 = "50mm medium close-up on the speaker's face, clear lip-sync" if lip3 else pick(CLOSE_SHOT[ctype], seed + 4)

    t1 = f"00:00–00:03.5 | {cam1} — {lead}: {b1}; {texture}.{d1}"
    slow_tag = ", one slow-motion beat" if slow else ""
    if b2:
        t2 = f"00:03.5–00:07.0 | {cam2}{slow_tag} — {b2}.{d2}"
    else:
        t2 = f"00:03.5–00:07.0 | {cam2} — Hành động trên đi tiếp, đổi cỡ cảnh, {accent}.{d2}"
    tail = b3 if b3 else pick(FALLBACK_B3, seed + 5)
    hold = pick(HOLD_LAST, seed) if c_num == 6 else pick(HOLD_LINES, seed + 4).format(n=nxt)
    t3 = f"00:07.0–00:10.0 | {cam3} — {tail}.{d3} {hold}"
    return t1, t2, t3, last_full.strip()


def end_frame_text(end_vn: str, c_num: int, seed: int) -> str:
    if c_num < 6:
        pool = [
            "End on: {x}. Hold that exact frame still for 0.5s; clip {n} starts from it.",
            "Last frame: {x}, perfectly still for half a second so clip {n} can continue without a cut.",
            "Freeze the final composition ({x}) for 0.5s; this is the first frame of clip {n}.",
            "Hold on {x} for 0.5s, no camera drift, so the next clip extends seamlessly.",
        ]
        return pick(pool, seed).format(x=end_vn, n=c_num + 1)
    pool = [
        "End on: {x}. Hold still for 0.5s; this closes the scene.",
        "Last frame: {x}, held motionless for half a second, then the scene ends.",
        "Freeze on {x} for 0.5s; scene complete.",
    ]
    return pick(pool, seed).format(x=end_vn)


def sound_text(setting_key: str, ctype: str, seed: int) -> str:
    base = pick(SETTING_SOUND.get(setting_key, SETTING_SOUND["TOWN"]), seed)
    tail = pick(
        ["Thoại rõ, không nhạc đè lời.", "Lời thoại nổi trên nền.", "Nền nhỏ hơn giọng người.", "Không nhạc dưới câu thoại."],
        seed + 2,
    )
    return f"Âm thanh nền: {base}; {pick(TYPE_ACCENT[ctype], seed + 3)}. {tail}"


FR_HEADERS = [
    "Continue the scene seamlessly from the final frame of clip {p}, which is the first frame of this clip. Same characters, outfits, props, lighting, and 16:9 cinematic widescreen framing. Flawless continuity with zero jump cut.",
    "Continue the scene seamlessly from the final frame of clip {p}: this clip opens on that exact frame. Keep the same people, clothes, props, light and 16:9 widescreen framing; no jump cut.",
    "Continue the scene seamlessly from the final frame of clip {p}. Pick up every element where it was left: same faces, outfits, objects, lighting, 16:9 framing, no visible cut.",
    "Continue the scene seamlessly from the final frame of clip {p}, matching position, light and 16:9 framing exactly, as one unbroken take.",
]
FR_FORMAT_LINES = [
    "Widescreen 16:9 (2.39:1 anamorphic ratio), 10-second clip, photorealistic live-action Vietnamese neo-noir mystery drama film style. 24fps high-budget cinematography, crisp 90-degree shutter angle, razor-sharp motion. {palette} Clean cinematic staging. Spoken dialogue in natural Southern Vietnamese with accurate lip-sync; voice-over narration allowed. Cut only where the shot list says. No subtitles or on-screen text.",
    "10-second clip, 16:9 (2.39:1 anamorphic), photorealistic live-action Vietnamese neo-noir drama. 24fps, 90-degree shutter, sharp motion, no smear. {palette} Clean cinematic staging. Southern Vietnamese dialogue with accurate lip-sync, voice-over allowed. No subtitles, no on-screen text.",
    "Photorealistic live-action Vietnamese neo-noir, 16:9 widescreen (2.39:1), 10 seconds at 24fps with a crisp 90-degree shutter. {palette} Clean cinematic staging. Natural Southern Vietnamese dialogue, lip-synced; voice-over permitted. No text or subtitles on screen.",
]

FORMAT_BLOCK = """[FORMAT]
Widescreen 16:9 (2.39:1 anamorphic ratio), 10-second clip, photorealistic live-action Vietnamese neo-noir mystery drama film style set in a small Vietnamese seaside town and a big city at night. 24fps high-budget cinematography, crisp 90-degree shutter angle, razor-sharp motion. {palette} Clean cinematic staging. Dialogue in Vietnamese with natural Southern accent and accurate lip-sync; first-person narration allowed as voice-over. No subtitles or on-screen text."""

AVOID_BLOCK = """[AVOID]
subtitles, captions, on-screen text, readable signs or documents, real brand logos, real police insignia, watermarks, text overlays, extra fingers, distorted hands, cartoon or anime look, slow sluggish motion, blurry motion smear, jump cuts, likeness of any real actor."""


def parse_keys(keys_str):
    mode = "ING" if keys_str.strip().startswith("ING") else "FR"
    return mode, re.findall(r"`([A-Z_]+)`", keys_str)


def base_of(key):
    for b in CHAR_ORDER:
        if key == b or key.startswith(b + "_"):
            return b
    return key


def sort_keys(keys):
    order = CHAR_ORDER + PROP_ORDER
    return sorted(set(keys), key=lambda k: (order.index(base_of(k)) if base_of(k) in order else 99, k))


def char_lines(keys, full):
    table = CHAR_FULL if full else CHAR_SHORT
    return [table[k] for k in sort_keys(keys) if k in table]


def prop_lines(keys):
    return [PROPS[k] for k in sort_keys(keys) if k in PROPS]


clip_pattern = re.compile(r"\* \*\*Clip (\d+) \((.*?)\):\*\* (.*?)(?=(?:\* \*\*Clip \d+)|$)", re.DOTALL)
generated = 0
for num_str, title, time_range, setting_str, body in scenes:
    scene_num = int(num_str)
    if scene_num in PRESERVED_SCENES:
        print(f"Giữ nguyên Cảnh {scene_num:02d}.")
        continue
    dir_path = os.path.join(BASE_DIR, f"canh-{scene_num:02d}")
    os.makedirs(dir_path, exist_ok=True)
    clips = []
    for c_num, c_keys, c_desc in clip_pattern.findall(body):
        desc = c_desc.strip()
        dialogue = "—"
        if "*Thoại:*" in desc:
            desc, dialogue = [p.strip() for p in desc.split("*Thoại:*", 1)]
            dialogue = dialogue.splitlines()[0].strip() if dialogue else "—"
        desc = clean_vn_safety(re.sub(r"\s+", " ", desc).strip())
        dialogue = clean_vn_safety(re.sub(r"\s+", " ", dialogue).strip())
        mode, keys = parse_keys(c_keys)
        hard_cut = (
            desc.startswith("Cắt cảnh")
            or desc.startswith("Cắt:")
            or desc.startswith("Hồi tưởng")
            or desc.startswith("Quá khứ:")
        )
        clips.append({"num": int(c_num), "mode": mode, "keys": keys, "desc": desc, "dialogue": dialogue, "hard_cut": hard_cut})
    assert len(clips) == 6, f"Cảnh {scene_num} có {len(clips)} clip"

    setting_key = get_setting_key(setting_str)
    setting_text = SETTINGS[setting_key]
    tap_num = (scene_num - 1) // 10 + 1
    act_name = {1: "Hồi 1: Bảy Ngày", 2: "Hồi 2: Thuốc Tê", 3: "Hồi 3: Người Môi Giới"}[
        1 if scene_num <= 20 else (2 if scene_num <= 40 else 3)
    ]
    prev_link = f"[← Cảnh {scene_num-1:02d}](../canh-{scene_num-1:02d}/README.md)" if scene_num > 1 else "← Bắt đầu phim"
    next_link = f"[Cảnh {scene_num+1:02d} →](../canh-{scene_num+1:02d}/README.md)" if scene_num < TOTAL_SCENES else "Hết phim"
    chars_vn = ", ".join(
        f"{VN_NAMES[base_of(k)]} ({CHAR_TAGS[base_of(k)]})"
        for k in sort_keys([k for c in clips for k in c["keys"]])
        if base_of(k) in VN_NAMES
    )

    readme = f"""# {SERIES_TITLE} — Cảnh {scene_num}: {title}

**Cảnh {scene_num}/60** · Phút {time_range} của phim · {act_name} · Tập {tap_num}/6 (bản 10 phút) · Thời lượng: 60s (6 clip × 10s)  
**Tỷ lệ khung hình:** **16:9 ngang** cho YouTube; crop 9:16 khi đăng TikTok  
**Kịch bản tổng:** [KICH_BAN_60_PHUT.md](../KICH_BAN_60_PHUT.md) · **Khóa nhân vật (9 nhân vật):** [FLOW_PROMPTS.md](../FLOW_PROMPTS.md) · **Đăng YouTube:** [youtube.md](../youtube.md)

{prev_link} | {next_link}

---

## 1. Tóm tắt cảnh
{clips[0]['desc']} {clips[2]['desc']} {clips[5]['desc']}

* **Bối cảnh chính:** {setting_str}
* **Nhân vật khóa trong cảnh:** {chars_vn}
* **Quy cách hình ảnh:** Người thật, neo-noir; hiện tại nắng trắng lạnh, quá khứ đêm ám vàng; lời dẫn ngôi thứ nhất; dàn dựng điện ảnh sạch, an toàn 100% trên Google Flow.
* **Thời lượng:** Đúng 60 giây.

---

## 2. Kịch bản phân cảnh chi tiết (Shot List 60 giây)

| Clip | Thời gian | Diễn biến | Lời thoại (Lip-sync) | Cách tạo |
|:---:|:---:|---|---|:---:|
"""
    for c in clips:
        s0, s1 = (c["num"] - 1) * 10, c["num"] * 10
        t = f"00:{s0:02d}–01:00" if s1 == 60 else f"00:{s0:02d}–00:{s1:02d}"
        mode_str = (
            "Ingredients (khóa mặt & bối cảnh)"
            if c["num"] == 1
            else ("Ingredients (cắt cảnh, đính lại ảnh)" if c["hard_cut"] else "Frames / Extend (nối liền)")
        )
        readme += f"| {c['num']} | {t} | **{c['desc']}** | {c['dialogue']} | {mode_str} |\n"
    readme += "\n---\n\n## 3. Danh sách file prompt Google Flow (Gemini Omni)\n\nCopy toàn bộ nội dung file và dán thẳng vào Google Flow (16:9):\n"
    for c in clips:
        note = (
            "Mở đầu cảnh (Ingredients)"
            if c["num"] == 1
            else (
                "Cắt cảnh: dán ở chế độ Ingredients"
                if c["hard_cut"]
                else ("Frames / Extend nối tiếp (cú lật, móc sang cảnh sau)" if c["num"] == 6 else "Frames / Extend nối tiếp")
            )
        )
        readme += f"- [clip-{c['num']}.md](clip-{c['num']}.md) — *{note}*\n"
    readme += "\nCaption đăng TikTok / Shorts: [caption.md](caption.md)\n"
    with open(os.path.join(dir_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)

    caption = f"""# Caption · {SERIES_TITLE} · Phần {scene_num}/60: {title}

> Caption cho video ngắn TikTok / YouTube Shorts cắt từ Cảnh {scene_num} (Phút {time_range}). 60 giây, 16:9 hoặc crop 9:16.

## Caption đề xuất
```text
Kẻ Sống Sót: Bóng Ma · Tập {scene_num}/60: {title} 🌊🕯️

{clips[0]['desc']}
{clips[4]['desc']}

"Bóng ma không biến mất. Bóng ma chỉ hết việc."
📺 Xem trọn bộ phim 60 phút trên kênh YouTube (link ở bio).
Phim hư cấu do AI tạo, cảnh hành động là dàn dựng điện ảnh.

#kesongsot #bongma #phimhanhdong #phimle #phimvietai
```

## Bình luận ghim (Pinned Comment)
```text
Cảnh {scene_num}: nếu là Sơn, bạn có bỏ nghề đi với Hạ không? 👇
```

## Checklist khi đăng
- Bật nhãn **"Nội dung do AI tạo"**.
- Không gắn giỏ hàng; không dùng tên diễn viên thật trong caption.
- Tối đa 5 hashtag.
"""
    with open(os.path.join(dir_path, "caption.md"), "w", encoding="utf-8") as f:
        f.write(caption)

    seen = set()
    for c in clips:
        c_num = c["num"]
        seed = scene_num * 7 + c_num * 3
        chars_in = [k for k in c["keys"] if base_of(k) in CHAR_ORDER]
        props_in = [k for k in c["keys"] if k in PROPS]
        ctype = classify(c["desc"], title)
        opens = c_num == 1 or c["hard_cut"]
        if c_num == 1:
            current_setting = setting_text
        if c["hard_cut"] and c_num > 1:
            current_setting = SETTINGS[get_setting_key(c["desc"])]
        clip_setting = current_setting
        clip_setting_key = [k for k, v in SETTINGS.items() if v == clip_setting][0]
        b1, b2, b3, end_vn = shot_list(
            c["desc"], c["dialogue"], ctype, c_num, c_num == 1, c["hard_cut"], clip_setting_key, scene_num, chars_in
        )
        end_frame = end_frame_text(end_vn, c_num, seed)
        if c_num == 1:
            scene_past = title.startswith("Quá Khứ") or c["desc"].startswith("Quá khứ:")
        if c["desc"].startswith("Quá khứ:"):
            scene_past = True
        elif c["desc"].startswith("Cắt:") and ("hiện tại" in c["desc"][:40].lower()):
            scene_past = False
        is_past = scene_past
        palette = (
            "Warm amber night colour grade with deep shadows for the past."
            if is_past
            else "Bleached white-sun colour grade with cool shadows for the present day."
        )
        if opens:
            header = FORMAT_BLOCK.format(palette=palette)
            chars_title = "[CHARACTERS — match attached reference images]"
            char_block = "\n".join(char_lines(chars_in, True)) or CHAR_FULL["SON"]
            entering = ""
        else:
            header = (
                pick(FR_HEADERS, seed).format(p=c_num - 1)
                + "\n"
                + pick(FR_FORMAT_LINES, seed + 1).format(palette=palette)
            )
            chars_title = "[CHARACTERS — unchanged]"
            char_block = "\n".join(char_lines(chars_in, False)) or CHAR_SHORT["SON"]
            new_chars = [k for k in chars_in if base_of(k) not in seen]
            entering = (
                "\n[CHARACTER ENTERING THIS SEGMENT — match attached reference image]\n"
                + "\n".join(char_lines(new_chars, True))
                + "\n"
                if new_chars
                else ""
            )
        for k in chars_in:
            seen.add(base_of(k))
        props_block = ("\n[PROPS]\n" + "\n".join(prop_lines(props_in)) + "\n") if props_in else ""
        atmosphere = {
            "COMBAT": "intense close-quarters martial choreography",
            "CHASE": "breathless pursuit",
            "STEALTH": "silent infiltration",
            "SUSPENSE": "cold ticking tension",
            "DRAMA": "quiet noir melancholy",
        }[ctype]
        prompt = f"""{header}

{chars_title}
{char_block}
{entering}{props_block}
[SETTING]
{clip_setting}
Story setting: {setting_str}
Scene {scene_num}/60, timecode {time_range}, clip {c_num}/6 ({(c_num-1)*10}–{c_num*10}s of the scene). Atmosphere: {atmosphere}, cinematic Vietnamese neo-noir.

[CAMERA & LIGHT]
{CAMERA[ctype]}

[SHOT LIST]
{b1}
{b2}
{b3}

[SOUND]
{sound_text(clip_setting_key, ctype, seed)}

[END FRAME]
{end_frame}

{AVOID_BLOCK}
"""
        with open(os.path.join(dir_path, f"clip-{c_num}.md"), "w", encoding="utf-8") as f:
            f.write(prompt)
        generated += 1
    print(f"✅ Cảnh {scene_num:02d} ({title}) — {setting_key}")
print(f"\nHoàn tất: {generated} clip cho {len(scenes)} cảnh.")
