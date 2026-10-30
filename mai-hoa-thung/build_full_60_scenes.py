#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh toàn bộ 60 thư mục cảnh (canh-01 … canh-60) cho phim điện ảnh 60 phút
"Mai Hoa Thung — Lân Chợ Lớn" từ kịch bản tổng KICH_BAN_60_PHUT.md.

Mỗi cảnh: README.md (shot list 60 s), caption.md (TikTok), clip-1.md … clip-6.md (prompt Gemini Omni 16:9).
- Clip 1 (và clip ghi "Cắt cảnh") mở bằng [FORMAT] + FULL LOCK → dán ở chế độ Ingredients.
- Các clip còn lại mở bằng câu Continue… + SHORT LOCK → dán ở chế độ Frames / Extend.
- Nhân vật xuất hiện lần đầu giữa cảnh được thêm khối [CHARACTER ENTERING THIS SEGMENT] với FULL LOCK.
- Khóa theo clip: chỉ liệt kê nhân vật có trong clip đó (hậu tố _C = thường phục; HAN_T / HAN_N = đồ của Hân theo giai đoạn).
Cảnh đã sửa tay: thêm số cảnh vào PRESERVED_SCENES để không bị ghi đè.
"""

import os
import re

SCRIPT_FILE = "KICH_BAN_60_PHUT.md"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOTAL_SCENES = 60
PRESERVED_SCENES: set[int] = set()

with open(os.path.join(BASE_DIR, SCRIPT_FILE), "r", encoding="utf-8") as f:
    script_content = f.read()

scene_pattern = re.compile(
    r"### CẢNH (\d+): (.*?) \((.*?)\)\n\*Bối cảnh: (.*?)\*\n(.*?)(?=(?:### CẢNH \d+:)|(?:# HƯỚNG DẪN)|$)",
    re.DOTALL,
)
scenes = scene_pattern.findall(script_content)
print(f"Bóc tách được {len(scenes)} cảnh từ kịch bản tổng.")

# ----------------------------------------------------------------------------
# KHÓA NHÂN VẬT (đồng bộ với FLOW_PROMPTS.md)
# ----------------------------------------------------------------------------
CHAR_FULL = {
    "LONG": "@Long = LONG (28, head of the lion and new leader of the Nghĩa Hòa troupe): a real Vietnamese man, about 175 cm tall, lean wiry acrobatic build, sharp focused dark eyes, calm face, black hair in an undercut with a small top knot, a small jade pendant shaped like a lion's tooth on a red cord around his neck (signature detail). Troupe outfit: a crimson silk kung-fu jacket with gold frog buttons and gold trim, loose black trousers, a red silk sash, white cloth kung-fu shoes. Voice: low, steady, warm Southern Vietnamese male voice, late 20s.",
    "LONG_C": "@Long = LONG in civilian clothes: the same man (28, undercut with a small top knot, jade lion-tooth pendant on a red cord) in a plain grey T-shirt, black jeans and white sneakers. Voice: low, steady, warm Southern Vietnamese male voice.",
    "MAI": "@Mai = MAI (24, tail of the lion and acrobat of the troupe): a real Vietnamese woman, about 160 cm tall, petite gymnast build, bright playful eyes, light freckles across her nose, black hair in two braids tied with red thread (signature detail). Troupe outfit: a crimson silk kung-fu jacket with gold trim, loose black trousers, a red silk sash, white cloth shoes, a long red silk ribbon wound around her LEFT wrist that she uses as a whip-like ribbon. Voice: quick, bright, teasing Southern Vietnamese female voice, mid-20s.",
    "MAI_C": "@Mai = MAI in civilian clothes: the same woman (24, two braids tied with red thread, freckles) in a white T-shirt, a denim jacket, black leggings and sneakers. Voice: quick, bright, teasing Southern Vietnamese female voice.",
    "PHUC": "@Phuc = PHÚC (30, the troupe's drummer, cook and former boxer): a real Vietnamese man, about 185 cm tall, big broad-shouldered and barrel-chested, completely shaved head (signature detail), thick black eyebrows, warm wide grin. Troupe outfit: a sleeveless crimson silk kung-fu vest with gold trim showing thick arms, loose black trousers, a red silk sash with two wooden drum sticks tucked into it, white cloth shoes. Voice: big, booming, warm Southern Vietnamese male voice, early 30s.",
    "PHUC_C": "@Phuc = PHÚC in civilian clothes: the same big shaved-headed man (30) in a black polo shirt, grey trousers and sandals. Voice: big, booming, warm Southern Vietnamese male voice.",
    "TI": "@Ti = TÍ (19, the youngest of the troupe, who plays the laughing Ông Địa character): a real Vietnamese young man, about 168 cm tall, skinny and springy, copper-dyed fringe over black hair (signature detail), a gap-toothed cheeky grin. Troupe outfit: a crimson silk kung-fu jacket with gold trim, loose black trousers, a red sash, sneakers, a round paper fan always in his hand; a round pink smiling Ông Địa mask pushed up on top of his head so his face stays fully visible. Voice: high, fast, cheeky Southern Vietnamese male voice, late teens.",
    "TI_C": "@Ti = TÍ in civilian clothes: the same skinny young man (19, copper-dyed fringe, gap-toothed grin) in an oversized black hoodie, shorts and sneakers, paper fan in his hand. Voice: high, fast, cheeky Southern Vietnamese male voice.",
    "HAN": "@Han = HÂN (27, a fighter of the Hắc Hổ troupe): a real Vietnamese woman, about 168 cm tall, athletic, serious almond eyes, short black hair with a single shaved line above her LEFT ear (signature detail). Hắc Hổ outfit: a black kung-fu jacket with gold tiger stripes on the sleeves, black trousers, a black sash, black cloth shoes, two short rattan sticks in her sash. Voice: low, cool, clipped Southern Vietnamese female voice, late 20s.",
    "HAN_T": "@Han = HÂN (27) in borrowed troupe clothes: a real Vietnamese woman, about 168 cm tall, athletic, serious almond eyes, short black hair with a single shaved line above her LEFT ear (signature detail), in a plain black kung-fu jacket with no stripes, black trousers, a red bandana tied around her neck, two short rattan sticks in a black sash. Voice: low, cool, clipped Southern Vietnamese female voice.",
    "HAN_N": "@Han = HÂN (27) in the Nghĩa Hòa troupe outfit: a real Vietnamese woman, about 168 cm tall, athletic, serious almond eyes, short black hair with a single shaved line above her LEFT ear (signature detail), in a crimson silk kung-fu jacket with gold trim, black trousers, a red sash, two short rattan sticks in her sash, a soft proud smile. Voice: low, cool, clipped Southern Vietnamese female voice.",
    "SUPHU": "SƯ PHỤ TƯ LÂN (70, master of the Nghĩa Hòa troupe): a slim elderly Vietnamese man with cropped white hair, a short white goatee, kind deeply lined face, in a dark-blue Chinese-style long jacket with cloth buttons, black trousers, cloth shoes, leaning on a wooden cane with a carved lion-head handle. Voice: warm, slow, elderly Southern Vietnamese male voice.",
    "LYHO": "LÝ HỔ (45, boss of the Hắc Hổ troupe, the master's expelled first disciple): a tall Vietnamese man with slicked-back black hair greying at the temples, cold narrow eyes, a scar cutting through his LEFT eyebrow (signature detail), in a black silk kung-fu jacket with gold tiger stripes, black trousers, gold rings, a black lacquered tiger-face mask pushed up on his forehead. Voice: deep, cold, unhurried Southern Vietnamese male voice.",
    "GOONS": "HẮC HỔ HENCHMEN: men in identical black kung-fu outfits with gold tiger stripes, black tiger-face masks covering their whole faces, wooden staffs; they never speak.",
    "BATAM": "BÀ TÁM (62, lantern maker and lion-head artisan): a plump elderly Vietnamese woman with a grey bun, reading glasses on a beaded chain, a floral apron over a brown blouse, hands stained with paint and glue. Voice: warm, chatty, elderly Southern Vietnamese female voice.",
}

CHAR_SHORT = {
    "LONG": "@Long = LONG: Vietnamese man, 28, undercut with a small top knot, jade lion-tooth pendant on a red cord, crimson silk kung-fu jacket with gold trim, red sash; low, steady Southern male voice.",
    "LONG_C": "@Long = LONG in civilian clothes: 28, top knot, jade lion-tooth pendant, grey T-shirt, black jeans; low, steady Southern male voice.",
    "MAI": "@Mai = MAI: Vietnamese woman, 24, two braids tied with red thread, freckles, crimson kung-fu jacket, red silk ribbon on her LEFT wrist; quick, bright Southern female voice.",
    "MAI_C": "@Mai = MAI in civilian clothes: 24, two braids with red thread, denim jacket over a white T-shirt; quick, bright Southern female voice.",
    "PHUC": "@Phuc = PHÚC: very big Vietnamese man, 30, shaved head, thick eyebrows, sleeveless crimson vest, two drum sticks in his red sash; booming, warm Southern male voice.",
    "PHUC_C": "@Phuc = PHÚC in civilian clothes: 30, very big, shaved head, black polo shirt; booming, warm Southern male voice.",
    "TI": "@Ti = TÍ: skinny Vietnamese young man, 19, copper-dyed fringe, gap-toothed grin, crimson kung-fu jacket, paper fan in hand, pink Ông Địa mask pushed up on his head; high, fast, cheeky Southern male voice.",
    "TI_C": "@Ti = TÍ in civilian clothes: 19, copper fringe, oversized black hoodie, paper fan; high, fast, cheeky Southern male voice.",
    "HAN": "@Han = HÂN: Vietnamese woman, 27, short hair with a shaved line above her LEFT ear, black kung-fu jacket with gold tiger stripes, two rattan sticks in her sash; low, cool Southern female voice.",
    "HAN_T": "@Han = HÂN: 27, shaved line above her LEFT ear, plain black kung-fu jacket, red bandana around her neck, two rattan sticks; low, cool Southern female voice.",
    "HAN_N": "@Han = HÂN: 27, shaved line above her LEFT ear, crimson kung-fu jacket with gold trim, two rattan sticks in her red sash; low, cool Southern female voice.",
    "SUPHU": "SƯ PHỤ TƯ LÂN: 70, cropped white hair, white goatee, dark-blue long jacket, lion-head cane; warm elderly Southern voice.",
    "LYHO": "LÝ HỔ: 45, slicked-back greying hair, scar through his LEFT eyebrow, black silk jacket with gold tiger stripes, tiger mask on his forehead; deep, cold Southern voice.",
    "GOONS": "HẮC HỔ HENCHMEN: black outfits with gold tiger stripes, full black tiger masks, wooden staffs, silent.",
    "BATAM": "BÀ TÁM: 62, grey bun, reading glasses on a chain, floral apron; warm chatty elderly Southern voice.",
}

PROPS = {
    "LION_TO": "LÂN TỔ (the ancestral lion head, 100 years old): a classic Southern lion-dance head, faded crimson and antique gold, long white fur beard and eyebrows, big mirrored eyes that blink, a black-lacquered horn with a red ribbon, one jade tooth missing from its upper jaw; a red-gold scaled cloth body with white fur trim. Long holds the head, Mai holds the tail.",
    "LION_MOI": "LÂN MỚI (the new lion head the troupe built): a bright crimson-and-gold lion-dance head with white fur beard, green mirrored eyes, a gold horn with a red ribbon, fresh hand-painted gold swirls; a red-gold scaled cloth body. Long holds the head, Mai holds the tail unless the shot list says otherwise.",
    "LION_HH": "LÂN HẮC HỔ (the Hắc Hổ lion): a black lion-dance head with silver stripes, red mirrored eyes, a black fur beard; a black-and-silver cloth body.",
    "TRONG": "TRỐNG TỔ (the ancestral drum): a big red lacquered lion-dance drum with brass studs and a worn hide, on a wooden stand, with a faded gold lion painted on its side.",
    "THUNG": "MAI HOA THUNG (the plum-blossom poles): red-painted steel poles of different heights from one to three metres, each topped with a round steel pad, arranged in a plum-blossom pattern, with safety mats below.",
}

CHAR_ORDER = ["LONG", "MAI", "PHUC", "TI", "HAN", "SUPHU", "LYHO", "GOONS", "BATAM"]
PROP_ORDER = ["LION_TO", "LION_MOI", "LION_HH", "TRONG", "THUNG"]
VN_NAMES = {"LONG": "Long", "MAI": "Mai", "PHUC": "Phúc", "TI": "Tí", "HAN": "Hân", "SUPHU": "Sư phụ", "LYHO": "Lý Hổ", "GOONS": "Hắc Hổ", "BATAM": "Bà Tám"}

# ----------------------------------------------------------------------------
# BỐI CẢNH
# ----------------------------------------------------------------------------
SETTINGS = {
    "TEMPLE": "TEMPLE SQUARE IN CHỢ LỚN: a small old temple with a curved tile roof, hanging coils of incense, a red-brick courtyard with an old apricot-blossom tree, red lanterns, a wooden rack holding lion heads and a big drum, Chợ Lớn alley houses around it; no readable text.",
    "LOFT": "TROUPE LOFT: a wooden loft above a Chợ Lớn alley hung with lion heads, drums and cymbals, a long wooden dining table, a small kitchen with a steaming noodle pot, warm tungsten bulbs, a small altar with a black-and-white photo; no readable text.",
    "ALLEY": "LANTERN ALLEY: a long narrow Chợ Lớn alley roofed with hundreds of red lanterns, shop fronts, old tiled houses, blurred neighbours; no readable signs.",
    "WORKSHOP": "LANTERN WORKSHOP: a cluttered lantern-maker's workshop at the end of the lantern alley, bamboo frames, red paper, glue pots, paint, half-finished lion heads, warm bulbs; no readable text.",
    "HERB": "HERBAL MEDICINE SHOP: a narrow old shop in the alley with tall wooden drawers of herbs, jars, scales, incense, a counter, morning light; no readable text.",
    "ROOFS": "CHỢ LỚN ROOFTOPS AT NIGHT: old tile roofs, water tanks, tangled wires, strings of red lanterns across the gaps, the night city glowing beyond.",
    "HOSPITAL": "HOSPITAL ROOM: a simple hospital room, white sheets, a window with daylight, a bedside stool with a bowl of soup, a corridor outside; no readable text.",
    "ICE": "ICE FACTORY AT NIGHT: a cold industrial ice factory with fog, huge ice blocks, chains and hooks, a glass office above, wet slippery concrete, green fluorescent light; no readable text.",
    "MARKET": "OLD MARKET AT DAWN (fictional): a huge old market with tiled roofs, aisles of fabric, candied fruit and lantern stalls, Tết crowds blurred in the background; no readable signs.",
    "CANAL": "TÀU HỦ CANAL: a dark city canal with small wooden boats, an old iron bridge, lantern reflections on the water, life jackets hanging on the boats.",
    "KILN": "ABANDONED KILN YARD AT NIGHT: rows of tall clay jars like a maze, dust, a round brick kiln with its door open and no fire, crossed floodlights.",
    "HALL": "HẮC HỔ HALL AT NIGHT: a dim martial-arts hall with black-and-gold banners without text, a black lion head on an altar, a wooden desk piled with folders, a ventilation grille in the roof.",
    "BUS": "BUS STATION AT NIGHT: a provincial bus station, sleeper buses, plastic chairs, fluorescent light, a vendor cart, a motorbike at the gate; no readable text.",
    "FESTIVAL": "FESTIVAL SQUARE ON THE THIRD DAY OF TẾT: the square in front of the temple, twenty-one red Mai Hoa Thung poles in the centre with safety mats, bamboo stands full of blurred spectators, red flags, a big drum, the organisers' wooden table, afternoon sun turning to dusk.",
}

def get_setting_key(setting_str: str, scene_num: int) -> str:
    s = setting_str.lower()
    if "quảng trường" in s or "dàn cột" in s or "cột lộc" in s or "trên cao dàn" in s or "giữa hai cột" in s or "đỉnh cột" in s or "chân dàn cột" in s:
        return "FESTIVAL"
    if "bến xe" in s:
        return "BUS"
    if "hắc hổ đường" in s:
        return "HALL"
    if "lò gốm" in s:
        return "KILN"
    if "chợ bình tây" in s:
        return "MARKET"
    if "kênh" in s:
        return "CANAL"
    if "nước đá" in s:
        return "ICE"
    if "bệnh viện" in s:
        return "HOSPITAL"
    if "mái" in s or "nóc" in s:
        return "ROOFS"
    if "thuốc bắc" in s:
        return "HERB"
    if "xưởng lồng đèn" in s:
        return "WORKSHOP"
    if "hẻm" in s:
        return "ALLEY"
    if "gác" in s:
        return "LOFT"
    return "TEMPLE"

# ----------------------------------------------------------------------------
# PHÂN LOẠI CLIP → camera, âm thanh, nhịp
# ----------------------------------------------------------------------------
COMBAT_KW = ["đánh ", "đánh lui", "đánh ba", "đánh hai", "đánh trên", "đánh giữa", "đánh tay", "đòn", "quật", "đá bật", "đá quét", "đá bay", "đá trả", "đá liên hoàn", "đá tung", "đá văng", "đá rơi", "đá rụng", "đá trụ", "cú đá", "côn gõ", "vung côn", "vung song côn", "hổ trảo", "hỗn chiến", "phục kích", "vật nhau", "vật tên", "vật lộn", "đấm", "khóa tay", "khóa cổ tay", "quét chân", "lao vào", "xông vào", "ập vào", "ra đòn", "đỡ đòn", "đỡ côn", "đỡ bằng", "đỡ hổ", "né lách", "né hai", "né bảy", "người né", "né đúng", "chặn côn", "húc đầu", "húc vào", "hất văng", "ngã chồng", "trượt dài"]
LION_KW = ["múa", "lân nhảy", "nhảy cột", "nhảy lên cột", "hái lộc", "chui vào", "lân đứng", "lân cúi", "lân ngậm", "lân chớp", "lân bật", "lên cột", "nhảy khỏi cột", "trên cột", "trống bảy", "nhịp bảy", "giáng dùi", "đánh trống", "chập chõa", "điểm nhãn"]
CHASE_KW = ["rượt", "đuổi", "chạy trên", "chạy xuyên", "phóng xe", "xe máy", "ghe", "trượt trên", "nhảy qua khe", "leo giàn", "trèo", "đu người", "đu qua", "lộn người", "parkour"]
SUSPENSE_KW = ["lẻn", "đột nhập", "nghe lén", "do thám", "chụp từng", "bằng chứng", "trói", "bị bắt", "lồng sắt", "đèn pin", "nhìn qua ống nhòm", "bóng đen", "khựng lại", "rạch nát", "móng hổ", "tin nhắn", "điện thoại rung", "loa"]

def classify_clip(desc: str, title: str) -> str:
    t = (desc + " " + title).lower()
    if any(k in t for k in COMBAT_KW):
        return "COMBAT"
    if any(k in t for k in LION_KW):
        return "LION"
    if any(k in t for k in CHASE_KW):
        return "CHASE"
    if any(k in t for k in SUSPENSE_KW):
        return "SUSPENSE"
    return "DRAMA"

CAMERA = {
    "COMBAT": "Aggressive 35mm anamorphic tracking, low-angle 24mm heroic perspective, dynamic handheld martial-arts camera with subtle micro-shake on impact, one speed-ramp slow-motion beat on the key strike. 90-degree shutter angle for razor-sharp kicks and staff work without motion smear. Gritty high-contrast lighting, red lantern rim light, dust in volumetric shafts, horizontal anamorphic flares.",
    "LION": "Sweeping 35mm anamorphic wide shots of the whole lion and the poles, cut with 50mm low-angle hero shots from below the pole tops, one extreme slow-motion beat on the jump. 90-degree shutter angle keeping the lion's fur, ribbons and mirrored eyes razor sharp. Warm golden Tết light, red-and-gold colour, lantern bokeh, drum-beat rhythm in the cutting.",
    "CHASE": "Fast 35mm anamorphic tracking shots running alongside the characters, low drone-style follow over roofs or water, whip pans on direction changes, one slow-motion beat on the big leap. 90-degree shutter angle, sharp subjects over streaking lantern lights, deep night contrast with red and amber practicals.",
    "SUSPENSE": "Tense 35mm Dutch-tilt moves through narrow spaces, tight 85mm close-ups on eyes, hands and small objects, slow push-ins. Chiaroscuro high-contrast shadows, cold green or pale fluorescent light against warm lantern glow, held breath pacing.",
    "DRAMA": "Warm, atmospheric 50mm and 85mm prime-lens cinematography with shallow depth of field, slow dolly moves, patient close-ups on faces. Soft golden tungsten light blending with red lantern glow through windows, natural skin tones, light cinematic film grain.",
}

SOUND = {
    "COMBAT": "Visceral martial-arts sound design: sharp wooden staff cracks, cloth snapping on fast kicks, deep sub-bass body impacts, quick air whooshes, lion-dance drum and cymbal hits punctuating the strikes, crowd gasps.",
    "LION": "Thunderous lion-dance drum in a seven-beat pattern, crashing cymbals and gong, the creak of steel poles, fur and ribbons rustling, a roaring crowd, rising orchestral strings on the jump.",
    "CHASE": "Breathless chase soundscape: running feet on tiles, cracking roof tiles, lanterns swinging and snapping, boat engines and water spray or motorbike engines, fast percussion, wind.",
    "SUSPENSE": "Edge-of-the-seat sound design: low ominous drone, slow heartbeat bass pulse, distant drum, small creaks and clicks, a phone vibrating on wood, rising string dissonance.",
    "DRAMA": "Subtle emotional sound design: a noodle pot simmering, chopsticks on bowls, distant alley sounds and crickets, a soft Southern folk melody on đàn tranh and guitar, natural room reverb.",
}

def split_desc(desc: str):
    sentences = [s.strip() for s in re.split(r"(?<=[\.\!\?;])\s+", desc) if s.strip()]
    if len(sentences) >= 2:
        return sentences[0], " ".join(sentences[1:])
    parts = [p.strip() for p in desc.split(",") if p.strip()]
    if len(parts) >= 3:
        return ", ".join(parts[:2]), ", ".join(parts[2:])
    if len(parts) == 2:
        return parts[0], parts[1]
    return desc, desc

def shot_list(desc: str, dialogue: str, ctype: str, c_num: int, opens_scene: bool, hard_cut: bool):
    part1, part2 = split_desc(desc)
    has_dialogue = bool(dialogue) and dialogue.strip() not in ("—", "-", "")
    next_target = f"clip {c_num + 1}" if c_num < 6 else "cảnh sau"
    if hard_cut:
        lead = "Hard cut to a new location and time, same outfits as described"
    elif opens_scene:
        lead = "Establishing shot and scene ignition"
    else:
        lead = "Continuing seamlessly from the last frame"
    if has_dialogue and ("Voice-over" in dialogue or "(loa" in dialogue or "Loa (" in dialogue or "điện thoại)" in dialogue):
        dial = f" Lời thoại nghe ngoài hình (voice-over, loa hoặc điện thoại), không cần khẩu hình: {dialogue}"
    elif has_dialogue:
        dial = f" Nhân vật nói với khẩu hình khớp từng âm tiết, máy quay thấy rõ mặt người nói: {dialogue}"
    else:
        dial = ""

    if ctype == "COMBAT":
        b1 = f"00:00–00:03.5 | Kinetic initiation, 35mm low-angle tracking — {lead}: {part1} Một động tác dứt khoát mở đầu, camera trượt góc thấp theo đà chuyển động."
        b2 = f"00:03.5–00:07.0 | Decisive impact with speed-ramp, 50mm dynamic cam — {part2} Mỗi nhịp một đòn: một cú né, một cú đỡ, một cú quật; nhịp quay chậm đúng cú ra đòn quyết định.{dial}"
        b3 = f"00:07.0–00:10.0 | Settle and stance lock, 35mm — Bụi và lồng đèn còn rung, đối thủ ngã hoặc lùi, nhân vật thu thế tấn vững, ánh mắt khóa mục tiêu. Khóa tĩnh khung hình cuối 0.5s để nối {next_target}."
    elif ctype == "LION":
        b1 = f"00:00–00:03.5 | Lion-dance wide and drum cue, 35mm anamorphic — {lead}: {part1} Trống nổi nhịp bảy, đầu lân chớp mắt gương, râu trắng bay."
        b2 = f"00:03.5–00:07.0 | The jump, 50mm low-angle hero shot with extreme slow motion — {part2} Mỗi nhịp một cú nhảy hoặc một thế lân; nhịp quay chậm đúng khoảnh khắc chân lân rời cột hoặc chạm cột.{dial}"
        b3 = f"00:07.0–00:10.0 | Landing and crowd reaction, 35mm — Lân đứng vững, ruy băng và lông bờm lắng xuống, chập chõa dứt, phản ứng của người xem hoặc đồng đội. Khóa tĩnh khung hình cuối 0.5s để nối {next_target}."
    elif ctype == "CHASE":
        b1 = f"00:00–00:03.5 | Pursuit tracking, 35mm anamorphic follow — {lead}: {part1} Camera chạy sát theo nhân vật, lồng đèn và mái ngói lướt qua."
        b2 = f"00:03.5–00:07.0 | The leap, 50mm whip-pan with one slow-motion beat — {part2} Mỗi nhịp một động tác: một cú nhảy, một cú bám, một cú né; nhịp quay chậm ở cú nhảy xa nhất.{dial}"
        b3 = f"00:07.0–00:10.0 | Landing and new gap, 35mm — Nhân vật tiếp đất, khoảng cách với mục tiêu thay đổi, một chi tiết rơi (ngói, lồng đèn, nước bắn). Khóa tĩnh khung hình cuối 0.5s để nối {next_target}."
    elif ctype == "SUSPENSE":
        b1 = f"00:00–00:03.5 | Tense approach, 35mm Dutch tilt — {lead}: {part1} Chuyển động chậm, thận trọng, tiếng thở và tiếng nền nhỏ."
        b2 = f"00:03.5–00:07.0 | The reveal, 85mm push-in — {part2} Cận vào vật chứng, bàn tay hoặc ánh mắt; một chi tiết lật tình thế.{dial}"
        b3 = f"00:07.0–00:10.0 | Hold on the turn, 50mm — Nhân vật phản ứng với điều vừa thấy, camera giữ chặt khoảnh khắc. Khóa tĩnh khung hình cuối 0.5s để nối {next_target}."
    else:
        b1 = f"00:00–00:03.5 | Atmospheric establishing, 50mm medium shot — {lead}: {part1} Ánh sáng ấm, camera lia chậm qua không gian và các nhân vật."
        b2 = f"00:03.5–00:07.0 | Intimate close-up, 85mm prime — {part2} Cận gương mặt, bàn tay, vật nhỏ; cảm xúc chân thật, không kịch.{dial}"
        b3 = f"00:07.0–00:10.0 | Emotional hold, 50mm — Nhịp phim lắng lại, các nhân vật trao nhau ánh nhìn hoặc một cử chỉ nhỏ; camera dừng ở góc máy điện ảnh. Khóa tĩnh khung hình cuối 0.5s để nối {next_target}."
    return b1, b2, b3

FORMAT_BLOCK = """[FORMAT]
Widescreen 16:9 (2.39:1 anamorphic ratio), 10-second clip, photorealistic live-action martial-arts blockbuster film style set in Saigon's Chợ Lớn at Tết. 24fps high-budget cinematography, crisp 90-degree shutter angle capturing razor-sharp kinetic motion with zero blurry artifacts. Rich red-and-gold Tết colour grade with warm lantern light. No guns, no blades anywhere. Dialogue in Vietnamese with natural Southern accent and lip-sync. No subtitles or on-screen text."""

AVOID_BLOCK = """[AVOID]
guns, firearms, knives, blades, blood, gore, visible wounds, deaths, large fire, real brand logos, readable signs or documents, watermarks, text overlays, extra fingers, cartoon or anime look, slow sluggish motion, blurry motion smear, awkward wind-up."""

def parse_keys(keys_str: str):
    """'ING · `LONG`, `MAI_C`' → ('ING', ['LONG', 'MAI_C'])"""
    mode = "ING" if keys_str.strip().startswith("ING") else "FR"
    keys = re.findall(r"`([A-Z_]+)`", keys_str)
    return mode, keys

def base_of(key: str) -> str:
    for b in CHAR_ORDER:
        if key == b or key.startswith(b + "_"):
            return b
    return key

def sort_keys(keys):
    order = CHAR_ORDER + PROP_ORDER
    return sorted(set(keys), key=lambda k: (order.index(base_of(k)) if base_of(k) in order else 99, k))

def char_lines(keys, full: bool):
    table = CHAR_FULL if full else CHAR_SHORT
    return [table[k] for k in sort_keys(keys) if k in table]

def prop_lines(keys):
    return [PROPS[k] for k in sort_keys(keys) if k in PROPS]

# ----------------------------------------------------------------------------
# SINH FILE
# ----------------------------------------------------------------------------
clip_pattern = re.compile(r"\* \*\*Clip (\d+) \((.*?)\):\*\* (.*?)(?=(?:\* \*\*Clip \d+)|$)", re.DOTALL)
generated = 0

for num_str, title, time_range, setting_str, body in scenes:
    scene_num = int(num_str)
    if scene_num in PRESERVED_SCENES:
        print(f"Giữ nguyên Cảnh {scene_num:02d} (đã sửa tay).")
        continue

    dir_name = f"canh-{scene_num:02d}"
    dir_path = os.path.join(BASE_DIR, dir_name)
    os.makedirs(dir_path, exist_ok=True)

    clips = []
    for c_num, c_keys, c_desc in clip_pattern.findall(body):
        desc = c_desc.strip()
        dialogue = "—"
        if "*Thoại:*" in desc:
            desc, dialogue = [p.strip() for p in desc.split("*Thoại:*", 1)]
        desc = re.sub(r"\s+", " ", desc).strip()
        dialogue = re.sub(r"\s+", " ", dialogue).strip()
        mode, keys = parse_keys(c_keys)
        hard_cut = desc.startswith("Cắt cảnh") or desc.startswith("Hồi tưởng")
        clips.append({"num": int(c_num), "mode": mode, "keys": keys, "desc": desc, "dialogue": dialogue, "hard_cut": hard_cut})
    assert len(clips) == 6, f"Cảnh {scene_num} có {len(clips)} clip, cần đúng 6"

    setting_key = get_setting_key(setting_str, scene_num)
    setting_text = SETTINGS[setting_key]
    tap_num = (scene_num - 1) // 10 + 1
    act = 1 if scene_num <= 20 else (2 if scene_num <= 40 else 3)
    act_name = {1: "Hồi 1: Trống Khai Xuân", 2: "Hồi 2: Đầu Lân Mới", 3: "Hồi 3: Mai Hoa Thung"}[act]

    # ---------- README ----------
    prev_link = f"[← Cảnh {scene_num-1:02d}](../canh-{scene_num-1:02d}/README.md)" if scene_num > 1 else "← Bắt đầu phim"
    next_link = f"[Cảnh {scene_num+1:02d} →](../canh-{scene_num+1:02d}/README.md)" if scene_num < TOTAL_SCENES else "Hết phim"
    readme = f"""# Mai Hoa Thung — Cảnh {scene_num}: {title}

**Cảnh {scene_num}/60** · Phút {time_range} của phim · {act_name} · Tập {tap_num}/6 (bản 10 phút) · Thời lượng: 60s (6 clip × 10s)  
**Tỷ lệ khung hình:** **16:9 ngang (Cinematic Widescreen)** cho YouTube; crop 9:16 khi đăng TikTok  
**Kịch bản tổng:** [KICH_BAN_60_PHUT.md](../KICH_BAN_60_PHUT.md) · **Khóa nhân vật:** [FLOW_PROMPTS.md](../FLOW_PROMPTS.md) · **Đăng YouTube:** [youtube.md](../youtube.md)

{prev_link} | {next_link}

---

## 1. Tóm tắt cảnh
{clips[0]['desc']} {clips[2]['desc']} {clips[5]['desc']}

* **Bối cảnh chính:** {setting_str}
* **Nhân vật trong cảnh:** {", ".join(VN_NAMES[base_of(k)] for k in sort_keys([k for c in clips for k in c['keys']]) if base_of(k) in VN_NAMES)}
* **Quy cách hình ảnh:** Người thật, phim võ thuật điện ảnh, đồ đoàn lân lụa đỏ viền vàng, đầu lân và trống thật; thoại ngắn giọng miền Nam; không súng, không dao, không máu.
* **Thời lượng:** Đúng 60 giây, khớp 1 phút trên timeline YouTube.

---

## 2. Kịch bản phân cảnh chi tiết (Shot List 60 giây)

| Clip | Thời gian | Diễn biến | Lời thoại (Lip-sync) | Cách tạo |
|:---:|:---:|---|---|:---:|
"""
    for c in clips:
        start_sec = (c["num"] - 1) * 10
        end_sec = c["num"] * 10
        time_str = f"00:{start_sec:02d}–01:00" if end_sec == 60 else f"00:{start_sec:02d}–00:{end_sec:02d}"
        if c["num"] == 1:
            mode_str = "Ingredients (khóa mặt, đầu lân, bối cảnh)"
        elif c["hard_cut"]:
            mode_str = "Ingredients (cắt cảnh, đính lại ảnh)"
        else:
            mode_str = "Frames / Extend (nối liền)"
        readme += f"| {c['num']} | {time_str} | **{c['desc']}** | {c['dialogue']} | {mode_str} |\n"

    readme += """
---

## 3. Danh sách file prompt Google Flow (Gemini Omni)

Mỗi file đã chuẩn hóa **16:9 Cinematic**; copy toàn bộ nội dung file và dán thẳng vào Google Flow:
"""
    for c in clips:
        if c["num"] == 1:
            note = "Mở đầu cảnh (Ingredients: đính ảnh nhân vật và đầu lân có trong cảnh)"
        elif c["hard_cut"]:
            note = "Cắt cảnh: dán ở chế độ Ingredients, đính lại ảnh nhân vật"
        elif c["num"] == 6:
            note = "Frames / Extend nối tiếp (cú lật, móc sang cảnh sau)"
        else:
            note = "Frames / Extend nối tiếp"
        readme += f"- [clip-{c['num']}.md](clip-{c['num']}.md) — *{note}*\n"
    readme += "\nCaption đăng TikTok / Shorts độc lập: [caption.md](caption.md)\n"
    with open(os.path.join(dir_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)

    # ---------- CAPTION ----------
    caption = f"""# Caption · Mai Hoa Thung · Phần {scene_num}/60: {title}

> Caption cho video ngắn TikTok / YouTube Shorts cắt từ Cảnh {scene_num} (Phút {time_range}).  
> Thời lượng: 60 giây. Khung hình: 16:9 hoặc crop 9:16.

## Caption đề xuất
```text
Mai Hoa Thung — Lân Chợ Lớn · Tập {scene_num}/60: {title} 🦁🥁

{clips[0]['desc']}
{clips[4]['desc']}

"Lân nằm ở tim!" ❤️
📺 Xem trọn bộ phim điện ảnh 60 phút trên kênh YouTube (link ở bio).
Phim hư cấu do AI tạo, cảnh võ thuật không thực hiện ngoài đời.

#maihoathung #lanchonlon #phimhanhdong #vothuat #tet
```

## Bình luận ghim (Pinned Comment)
```text
Cảnh {scene_num}: theo bạn ai ngầu nhất, Long, Mai, Phúc, Tí hay Hân? 👇
```

## Checklist khi đăng
- Bật nhãn **"Nội dung do AI tạo"** (AI-generated content).
- Không gắn giỏ hàng thương mại.
- Tối đa 5 hashtag; trả lời bình luận theo tinh thần đoàn Nghĩa Hòa.
"""
    with open(os.path.join(dir_path, "caption.md"), "w", encoding="utf-8") as f:
        f.write(caption)

    # ---------- CLIP PROMPTS ----------
    seen_chars: set[str] = set()
    for idx, c in enumerate(clips):
        c_num = c["num"]
        chars_in_clip = [k for k in c["keys"] if base_of(k) in CHAR_ORDER]
        props_in_clip = [k for k in c["keys"] if k in PROPS]
        ctype = classify_clip(c["desc"], title)
        opens = (c_num == 1) or c["hard_cut"]
        b1, b2, b3 = shot_list(c["desc"], c["dialogue"], ctype, c_num, opens_scene=(c_num == 1), hard_cut=c["hard_cut"])

        if opens:
            char_block = "\n".join(char_lines(chars_in_clip, full=True)) or "(no main character in frame)"
            header = FORMAT_BLOCK
            chars_title = "[CHARACTERS — match attached reference images]"
            end_frame = f"Clean freeze on the final frame for seamless continuation into clip {c_num + 1}." if c_num < 6 else "Clean freeze on the final frame; this ends the scene."
            entering_block = ""
        else:
            char_block = "\n".join(char_lines(chars_in_clip, full=False)) or "(no main character in frame)"
            header = (
                f"Continue the scene seamlessly from the final frame of clip {c_num - 1}, which is the first frame of this clip. Same characters, outfits, props, lighting, and 16:9 cinematic widescreen framing. Flawless continuity with zero jump cut.\n"
                "Widescreen 16:9 (2.39:1 anamorphic ratio), 10-second clip, photorealistic live-action martial-arts blockbuster film style set in Saigon's Chợ Lớn at Tết. 24fps high-budget cinematography, crisp 90-degree shutter angle, razor-sharp motion. Spoken dialogue in natural Southern Vietnamese with lip-sync. Cut only where the shot list says. No subtitles or on-screen text."
            )
            chars_title = "[CHARACTERS — unchanged]"
            new_chars = [k for k in chars_in_clip if base_of(k) not in seen_chars]
            entering_block = ""
            if new_chars:
                entering_block = "\n[CHARACTER ENTERING THIS SEGMENT — match attached reference image]\n" + "\n".join(char_lines(new_chars, full=True)) + "\n"
            end_frame = f"Hold final frame still for 0.5s for seamless extension to clip {c_num + 1}." if c_num < 6 else "Hold final frame still for 0.5s; this ends the scene."

        for k in chars_in_clip:
            seen_chars.add(base_of(k))

        props_block = ("\n[PROPS]\n" + "\n".join(prop_lines(props_in_clip)) + "\n") if props_in_clip else ""
        if c["hard_cut"] and c_num > 1:
            clip_setting_text = SETTINGS[get_setting_key(c["desc"], scene_num)]
        else:
            clip_setting_text = setting_text
        elapsed = f"Scene {scene_num}/60, timecode {time_range}, clip {c_num}/6 ({(c_num-1)*10}–{c_num*10}s of the scene)."

        prompt = f"""{header}

{chars_title}
{char_block}
{entering_block}{props_block}
[SETTING]
{clip_setting_text}
Story setting: {setting_str}
{elapsed} Atmosphere: {'high-adrenaline martial-arts action' if ctype in ('COMBAT','CHASE') else ('festive lion-dance spectacle' if ctype == 'LION' else ('tense suspense' if ctype == 'SUSPENSE' else 'warm family drama'))}, cinematic Tết in Chợ Lớn.

[CAMERA & LIGHT]
{CAMERA[ctype]}

[SHOT LIST]
{b1}
{b2}
{b3}

[SOUND]
{SOUND[ctype]}

[END FRAME]
{end_frame}

{AVOID_BLOCK}
"""
        with open(os.path.join(dir_path, f"clip-{c_num}.md"), "w", encoding="utf-8") as f:
            f.write(prompt)
        generated += 1

    print(f"✅ Cảnh {scene_num:02d} ({title}) — bối cảnh {setting_key} — 6 clip.")

print(f"\nHoàn tất: {generated} file clip prompt cho {len(scenes)} cảnh.")
