#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tự động sinh toàn bộ hệ thống 45 thư mục cảnh (canh-01 đến canh-45)
cho series phim điện ảnh 45 phút Biệt Đội Gara (Fast & Furious style).
ĐƯỢC NÂNG CẤP CHUẨN BOM TẤN HÀNH ĐỘNG ĐIỆN ẢNH (BLOCKBUSTER ACTION GRADE):
- Khung hình 16:9 ngang (Anamorphic 2.39:1 widescreen aesthetic)
- Shutter angle 90° bắt trọn đòn thế võ thuật và rượt đuổi siêu tốc, loại bỏ triệt để motion blur nhòe bệt của AI
- Shot list phân rã 3 nhịp chi tiết (00:00-03.5s; 03.5-07.0s; 07.0-10.0s) không có placeholder
- Đòn thế võ thuật Vovinam, stunt cận chiến, drifting uy lực, bộc phá năng lượng
- Thiết kế âm thanh Dolby Atmos đa tầng (sub-bass impact, metallic clangs, mechanical servos)
"""

import os
import re

SCRIPT_FILE = "KICH_BAN_45_PHUT_FAST_FURIOUS.md"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Đọc kịch bản 45 phút
with open(os.path.join(BASE_DIR, SCRIPT_FILE), "r", encoding="utf-8") as f:
    script_content = f.read()

# Regex bóc tách 45 cảnh
scene_pattern = re.compile(
    r"### CẢNH (\d+): (.*?) \((.*?)\)\n\*Bối cảnh: (.*?)\*\n(.*?)(?=(?:### CẢNH \d+:)|(?:# HƯỚNG DẪN)|$)",
    re.DOTALL
)

scenes = scene_pattern.findall(script_content)
print(f"Bóc tách được {len(scenes)} cảnh từ kịch bản tổng.")

# Định nghĩa các khối nhân vật và xe cộ
CHAR_FULL_MAP = {
    "THANG": """@Thang = THẮNG (36, the eldest, owner of Gara Bảy): a real Vietnamese man, about 178 cm tall, lean and strong, square jaw, calm dark eyes, light stubble, short black hair with a single silver streak at his LEFT temple (signature detail), a faded burn scar on his LEFT forearm. Civilian outfit: an olive-green mechanic's work jacket with the sleeves pushed up over a black T-shirt, dark work trousers, black boots, a red shop rag hanging from his back pocket. Voice: deep, calm, steady Southern Vietnamese male voice, mid-30s.""",
    "THANG_G": """@Thang = THẮNG in his armor GIÁP GIÓ: the same man inside a sleek red-and-black armored suit of matte composite plates with angular wind-vent fins on the shoulders and calves and glowing red light lines; an open-face armored helmet with a clear amber visor, so his whole face, the silver streak at his LEFT temple and his lips stay visible; a glowing red hexagonal core on his LEFT wrist. Power: short dashes of speed that leave red wind streaks. Voice: deep, calm, steady Southern Vietnamese male voice.""",
    "THANG_R": """@Thang = THẮNG in racing suit: Vietnamese man, 36, silver streak at his LEFT temple, plain red-and-black racing suit with no logos, black racing helmet with red stripe and clear visor raised showing his face; deep, calm Southern male voice.""",
    
    "LAN": """@Lan = LAN (29, the best driver of the family): a real Vietnamese woman, about 162 cm tall, petite and athletic, sharp bright eyes, a confident half smile, a short black bob with one ice-blue streak on the RIGHT side (signature detail). Civilian outfit: a white leather moto jacket over a grey top, black jeans, white sneakers. Voice: quick, bright, confident Southern Vietnamese female voice, late 20s.""",
    "LAN_G": """@Lan = LAN in her armor GIÁP CÁO: the same woman inside a slim white armored suit with ice-blue light lines and a small fox-ear crest on the helmet; an open-face armored helmet with a clear ice-blue visor, so her whole face and the ice-blue streak in her hair stay visible; a glowing white-blue hexagonal core on her LEFT wrist. Power: blinding speed and agility that leaves white-blue afterimages. Voice: quick, bright, confident Southern Vietnamese female voice.""",
    
    "HAI": """@Hai = HẢI (32, the family's mechanic, cook and Vovinam fighter): a real Vietnamese man, about 188 cm tall, big and broad-shouldered, warm brown eyes, a short full black beard, hair shaved short on the sides with a short top (signature detail: the tallest and biggest of the family). Civilian outfit: a grey tank top under a brown leather work apron, dark cargo trousers, boots, a big steel wrench usually in his hand or apron. Voice: big, warm, booming Southern Vietnamese male voice, early 30s, gentle.""",
    "HAI_G": """@Hai = HẢI in his armor GIÁP BÚA: the same big man inside heavy orange-and-gunmetal armor with thick shoulder plates and a short buffalo-horn crest on the helmet; an open-face armored helmet with a clear orange visor, so his bearded face stays visible; a glowing orange hexagonal core on his LEFT wrist. His steel wrench turns into a glowing orange energy hammer that knocks enemies back with harmless shockwaves of light. Voice: big, warm, booming Southern Vietnamese male voice.""",
    
    "KHOI": """@Khoi = KHÔI (24, the family's tech genius and joker): a real Vietnamese young man, about 170 cm tall, slim, round tortoiseshell glasses (signature detail), messy black hair, an expressive nervous face. Civilian outfit: a mustard-yellow hoodie, black joggers, sneakers, headphones around his neck, a laptop in his hands or a small backpack. Voice: fast, nervous, funny Southern Vietnamese male voice, mid-20s.""",
    "KHOI_G": """@Khoi = KHÔI in his armor GIÁP BIT: the same young man inside a slim yellow-and-black armored suit with circuit-like light lines and two palm-sized drones docked on his shoulders; an open-face armored helmet with a clear yellow visor, so his face and his round glasses stay visible; a glowing yellow hexagonal core on his LEFT wrist. Power: his drones fire rings of yellow light that switch off enemy gauntlets. Voice: fast, nervous, funny Southern Vietnamese male voice.""",
    
    "MINH": """@Minh = MINH (31, a police detective captain): a real Vietnamese woman, about 168 cm tall, athletic, sharp straight eyebrows, serious dark eyes, a thin pale scar on her chin (signature detail), black hair in a tight low bun. Civilian outfit: a black plain-clothes jacket over a white shirt, dark trousers, low black boots, no badges or readable text. Voice: firm, low, clear Southern Vietnamese female voice, mid-30s.""",
    "MINH_G": """@Minh = MINH in her armor GIÁP KHIÊN: the same woman inside navy-and-silver armor with clean straight lines and a round energy shield of navy light on her left forearm; an open-face armored helmet with a clear navy visor, so her face and the scar on her chin stay visible; a glowing navy hexagonal core on her LEFT wrist. Power: an energy shield and navy light cuffs that lock enemy gauntlets for arrest. Voice: firm, low, clear Southern Vietnamese female voice.""",
    
    "TU": """@Tu = TÚ: a Vietnamese young man of 22, thin, dyed-brown hair, silver ear stud, nervous boyish face, in a grey racing suit; young, hoarse Southern male voice.""",
    "SOI": """SÓI XÁM (the villain): a Vietnamese man of 45, salt-and-pepper slicked hair, cold eyes, dark gunmetal armor with glowing red wolf helmet that splits open when speaking, grey gloves; deep, menacing Southern male voice.""",
    "SOI_C": """SÓI XÁM (HÙNG) WITHOUT ARMOR: the same man of 45, armor shattered, torn black under-suit, face tired and broken, crying in remorse; low, broken Southern male voice.""",
    "GOONS": """GĂNG XÁM HENCHMEN: men in identical grey tactical armor with full helmets and glowing grey power gauntlets; they never speak.""",
    "BACBAY": """BÁC BẢY (HOLOGRAM): kind elderly Vietnamese mechanic in late 60s, crew cut, warm smile lines, blue work shirt, glowing soft-blue hologram; warm elderly Southern voice."""
}

CHAR_SHORT_MAP = {
    "THANG": """@Thang = THẮNG: Vietnamese man, 36, silver streak at LEFT temple, olive work jacket, red rag; deep, calm Southern voice.""",
    "THANG_G": """@Thang = THẮNG in GIÁP GIÓ: red-and-black armor with wind fins, amber visor showing face, red wrist core; deep, calm Southern voice.""",
    "THANG_R": """@Thang = THẮNG in racing suit: 36, red-black suit, open helmet with red stripe; deep, calm Southern voice.""",
    "LAN": """@Lan = LAN: Vietnamese woman, 29, short bob with ice-blue streak, white leather moto jacket; quick, bright Southern voice.""",
    "LAN_G": """@Lan = LAN in GIÁP CÁO: slim white armor with ice-blue lines and fox-ear crest, ice-blue visor showing face; quick, bright Southern voice.""",
    "HAI": """@Hai = HẢI: big Vietnamese man, 32, full beard, shaved sides, grey tank top, leather apron, big steel wrench; booming Southern voice.""",
    "HAI_G": """@Hai = HẢI in GIÁP BÚA: heavy orange-and-gunmetal armor, buffalo horn crest, orange visor showing face, glowing energy hammer; booming Southern voice.""",
    "KHOI": """@Khoi = KHÔI: slim Vietnamese young man, 25, round glasses, messy hair, yellow hoodie, laptop; fast, nervous Southern voice.""",
    "KHOI_G": """@Khoi = KHÔI in GIÁP BIT: slim yellow-black armor, two shoulder drones, yellow visor showing glasses and face; nervous, fast Southern voice.""",
    "MINH": """@Minh = MINH: Vietnamese woman, 31, chin scar, low hair bun, black jacket; firm, clear Southern voice.""",
    "MINH_G": """@Minh = MINH in GIÁP KHIÊN: navy-and-silver armor, round energy shield on left arm, navy visor showing face; firm Southern voice.""",
    "TU": """@Tu = TÚ: 22, thin, brown hair, grey racing suit; hoarse nervous Southern voice.""",
    "SOI": """SÓI XÁM: 45, salt-and-pepper hair, dark gunmetal wolf armor with red glowing eyes, grey gloves; low sinister Southern voice.""",
    "SOI_C": """SÓI XÁM (HÙNG): 45, armor shattered, torn under-suit, face broken with tears; low, broken voice.""",
    "GOONS": """GĂNG XÁM HENCHMEN: men in grey tactical armor and glowing power gauntlets, silent.""",
    "BACBAY": """BÁC BẢY (HOLOGRAM): kind elderly Vietnamese mechanic in soft-blue hologram; warm elderly Southern voice."""
}

SETTING_DESCS = {
    "GARA_NIGHT": "GARA BẢY AT NIGHT: two-story mechanic garage beside a canal in Saigon, oil-stained concrete floor, teal neon and warm work lamps, walls of hanging tools, hydraulic lift, mezzanine with wooden table; no readable text.",
    "GARA_DAY": "GARA BẢY BY DAY: two-story garage workshop beside a canal in bright daylight, open front shutter, tire stacks, hydraulic lift, tools on walls, backyard by the canal edge; no readable text.",
    "TRACK": "CLOSED RACING TRACK: asphalt circuit in Saigon outskirts under harsh midday sun, concrete barriers, tire walls, red dirt shoulders, pit lane; no brand logos or readable signs.",
    "WAREHOUSE": "CONTAINER WAREHOUSE AT NIGHT: cavernous abandoned dockside warehouse, skylights, rows of covered stolen cars, high steel catwalks, industrial floodlights; no logos.",
    "ROOFS_RAIN": "SAIGON ROOFTOPS IN HEAVY RAIN: corrugated metal roofs beside a canal, dark stormy night with heavy rain and wind, reflections of city lights in puddles, wet slick surfaces.",
    "HIGHWAY": "SEALED PORT HIGHWAY: wide 8-lane asphalt coastal highway leading to the seaport at midnight, police barricades, flashing lights, empty road cleared for tactical pursuit.",
    "SHIP": "CONTAINER CARGO SHIP DECK: open steel deck of a massive cargo ship at sea, towering stacks of plain shipping containers, ocean spray, night storm with wind and rising dawn."
}

def get_setting_key(setting_str, scene_num):
    s = setting_str.lower()
    if "đường đua" in s:
        return "TRACK"
    elif "kho" in s:
        return "WAREHOUSE"
    elif "mưa" in s or "nóc" in s or "mái" in s:
        return "ROOFS_RAIN"
    elif "đại lộ" in s or "đường cảng" in s:
        return "HIGHWAY"
    elif "tàu" in s or "boong" in s or "cầu tàu" in s:
        return "SHIP"
    elif "ngày" in s or "sáng" in s or "chiều" in s:
        return "GARA_DAY"
    else:
        return "GARA_NIGHT"

def classify_clip(desc, dialogue, title):
    text = (desc + " " + title).lower()
    
    # 1. ARMOR TRANSFORMATION
    if any(k in text for k in ["lõi", "khởi động", "biến hình", "bọc lấy", "áo giáp", "phát sáng 5 màu", "ngũ sắc"]):
        if any(k in text for k in ["khởi động", "bay thẳng tới", "ghim vào", "khoác giáp", "bọc kín", "mở bung", "thu hồi"]):
            return "ARMOR"
            
    # 2. COMBAT & MARTIAL ARTS
    if any(k in text for k in ["đấm", "đá", "cước", "cờ lê", "búa", "găng", "tập kích", "hỗn chiến", "quật", "tước", "xà beng", "sóng áp suất", "sóng chấn động", "nện", "quét trụ", "kẹp cổ", "chiến binh", "sói xám", "chiến đấu", "vung", "đỡ đòn", "vật ngã", "quật văng"]):
        return "COMBAT"
        
    # 3. RACING & VEHICULAR
    if any(k in text for k in ["đua", "drift", "vô lăng", "bẻ lái", "chân ga", "khúc cua", "húc", "xe tải", "xe bán tải", "hắc phong", "phanh", "bốc đầu", "vượt xe", "pit-stop", "nitro"]):
        return "RACING"
        
    # 4. SUSPENSE & TACTICAL
    if any(k in text for k in ["kíp nổ", "bom", "gỡ", "gián điệp", "đột nhập", "mái tôn", "giếng trời", "rượt đuổi"]):
        return "SUSPENSE"
        
    return "DRAMA"

def split_desc(desc):
    sentences = [s.strip() for s in re.split(r'[\.\!\?]', desc) if s.strip()]
    if len(sentences) >= 2:
        return sentences[0], ' '.join(sentences[1:])
    subparts = [p.strip() for p in desc.split(',') if p.strip()]
    if len(subparts) >= 3:
        return ', '.join(subparts[:2]), ', '.join(subparts[2:])
    elif len(subparts) == 2:
        return subparts[0], subparts[1]
    return desc, desc

def generate_blockbuster_shotlist(desc, dialogue, clip_type, c_num, is_clip1=False):
    part1, part2 = split_desc(desc)
    has_dialogue = dialogue and dialogue.strip() != "—" and dialogue.strip() != ""
    next_target = f"clip {c_num+1}" if c_num < 6 else "sang cảnh sau"
    lead_in = "Establishing scene & action ignition" if is_clip1 else "Continuing seamlessly from the last frame"

    if clip_type == "COMBAT":
        b1 = f"00:00–00:03.5 | Explosive kinetic initiation, 35mm low-angle tracking — {lead_in}: {part1}. Đòn thế khai cuộc thần tốc, gia tốc bộc phát tức thì, camera trượt theo góc thấp bắt trọn đà chuyển động dứt khoát của nhân vật."
        if has_dialogue:
            b2 = f"00:03.5–00:07.0 | Decisive martial arts impact & speed-ramp execution, 50mm dynamic combat cam — Cú ra đòn và phản xạ dứt khoát: {part2}. Va chạm đanh thép tạo xung lực dội ngược làm chấn động không khí, tia lửa cơ khí lóe sáng; nhân vật giữ thế dứt khoát, cất giọng Nam dõng dạc với khẩu hình khớp từng âm tiết: {dialogue}. Ánh mắt kiên định sắc lạnh qua kính mũ."
        else:
            b2 = f"00:03.5–00:07.0 | Decisive martial arts impact & speed-ramp execution, 50mm dynamic combat cam — Cú ra đòn và phản xạ dứt khoát: {part2}. Va chạm đanh thép tạo xung lực dội ngược làm chấn động không khí, tia lửa cơ khí lóe sáng; nhân vật dậm trụ dứt khoát, ánh mắt kiên định sắc lạnh qua kính mũ, không chút do dự."
        b3 = f"00:07.0–00:10.0 | Kinetic shockwave dissipation & combat stance lock, 35mm low-angle — Sóng xung kích quét tròn làm bụi đất và mảnh vỡ dạt ra ngoài, đối thủ bị chấn động lùi lại hoặc dính đòn; nhân vật thu thế tấn vững như bàn thạch, cơ bắp căng tràn, ánh mắt khóa chặt mục tiêu. Khóa tĩnh khung hình cuối 0.5s để nối tiếp {next_target} mượt mà không lỗi giật."

    elif clip_type == "RACING":
        b1 = f"00:00–00:03.5 | High-speed kinetic vehicular tracking, 35mm wide anamorphic — {lead_in}: {part1}. Tiếng gầm rú của động cơ Twin-Turbo, lốp xe cày xé mặt đường tạo khói trắng cuồn cuộn, camera tracking sát sườn xe ở góc cực thấp với độ nét sắc sảo."
        if has_dialogue:
            b2 = f"00:03.5–00:07.0 | Precision high-speed stunt & decisive counter, 50mm dynamic cam — Cú bẻ lái hoặc va chạm nảy lửa: {part2}. Thân xe trượt ngang ngoạn mục, tia lửa ma sát bắn tung tóe từ rào chắn; nhân vật ghì chặt vô lăng, nét mặt căng thẳng cao độ, cất giọng qua bộ đàm với khẩu hình chuẩn xác: {dialogue}."
        else:
            b2 = f"00:03.5–00:07.0 | Precision high-speed stunt & decisive counter, 50mm dynamic cam — Cú bẻ lái hoặc va chạm nảy lửa: {part2}. Thân xe trượt ngang ngoạn mục, tia lửa ma sát bắn tung tóe từ rào chắn; nhân vật ghì chặt vô lăng bẻ góc cua sắc lẹm, kiểm soát quỹ đạo hoàn hảo."
        b3 = f"00:07.0–00:10.0 | Drift recovery & relentless forward momentum, 35mm tracking — Chiếc xe lấy lại độ bám đường sau cú drift nghẹt thở, vệt bánh xe đen bóng in hằn trên mặt đường bốc khói; camera lia mượt về góc sau xe, khóa tĩnh khung hình cuối 0.5s để làm gốc nối liền cho {next_target}."

    elif clip_type == "ARMOR":
        b1 = f"00:00–00:03.5 | Epic power surge & core resonance, 35mm anamorphic wide — {lead_in}: {part1}. Luồng ánh sáng năng lượng thuần khiết bùng nổ, các vi mạch nano kích hoạt phát quang rực rỡ, gió xoáy năng lượng thổi tung tàn bụi xung quanh."
        if has_dialogue:
            b2 = f"00:03.5–00:07.0 | Sleek armor morphing & heroic declaration, 50mm hero shot — {part2}. Các mảnh giáp cơ khí nano ôm khít cơ thể trong nháy mắt, kính mũ trong suốt trượt xuống bảo vệ khuôn mặt. Nhân vật bộc lộ hào khí dũng mãnh, hô vang câu khẩu lệnh dõng dạc: {dialogue}. Khẩu hình khớp hoàn hảo qua kính mũ."
        else:
            b2 = f"00:03.5–00:07.0 | Sleek armor morphing & heroic declaration, 50mm hero shot — {part2}. Các mảnh giáp cơ khí nano ôm khít cơ thể trong nháy mắt, kính mũ trong suốt trượt xuống bảo vệ khuôn mặt. Nhân vật đứng thẳng uy nghiêm trong luồng sáng vi mạch."
        b3 = f"00:07.0–00:10.0 | Radiant aura stabilization & battle-ready lock, 35mm low-angle — Hào quang năng lượng từ lõi cổ tay trái lan tỏa dọc theo các đường viền LED của bộ giáp, các vây khí động học khẽ rung lên vào vị trí sẵn sàng chiến đấu. Khóa tĩnh khung hình cuối 0.5s làm gốc cho {next_target}."

    elif clip_type == "SUSPENSE":
        b1 = f"00:00–00:03.5 | High-tension tactical tracking, 35mm Dutch tilt — {lead_in}: {part1}. Chuyển động thận trọng, camera lướt theo nhịp thở gấp gáp, bắt trọn từng tích tắc đếm ngược của hiểm họa cận kề."
        if has_dialogue:
            b2 = f"00:03.5–00:07.0 | Critical decisive maneuver & tense dialogue, 50mm to 85mm push-in — Thao tác kỹ thuật chuẩn xác và dứt khoát: {part2}. Bàn tay vững vàng xử lý trong giây phút sinh tử, trán ướt đẫm mồ hôi nhưng ánh mắt không hề dao động, nhân vật bật ra câu nói then chốt: {dialogue}."
        else:
            b2 = f"00:03.5–00:07.0 | Critical decisive maneuver, 50mm to 85mm push-in — Thao tác kỹ thuật chuẩn xác và dứt khoát: {part2}. Bàn tay vững vàng xử lý trong giây phút sinh tử, trán ướt đẫm mồ hôi nhưng ánh mắt tập trung tột độ không hề dao động."
        b3 = f"00:07.0–00:10.0 | High-stakes stabilization & cliffhanger lock, 35mm — Hiểm nguy tạm thời được kìm hãm hoặc bộc lộ bước ngoặt nghẹt thở; camera khóa chặt vào khoảnh khắc quyết định, giữ tĩnh 0.5s ở khung hình cuối cùng để chuyển tiếp {next_target}."

    else: # DRAMA
        b1 = f"00:00–00:03.5 | Cinematic atmospheric tracking, 50mm medium shot — {lead_in}: {part1}. Ánh sáng ấm áp lan tỏa, camera lia chậm rãi ghi lại không gian xưởng gara và mối dây liên kết ruột thịt giữa các nhân vật."
        if has_dialogue:
            b2 = f"00:03.5–00:07.0 | Warm intimate close-up & sincere dialogue, 85mm prime lens — Chuyển biến cảm xúc chân thành: {part2}. Ánh mắt chất phác, nụ cười tin tưởng hoặc sự trầm tư của nhân vật, giọng nói miền Nam truyền cảm với khẩu hình khớp tự nhiên: {dialogue}."
        else:
            b2 = f"00:03.5–00:07.0 | Warm intimate close-up & emotion, 85mm prime lens — Chuyển biến cảm xúc chân thành: {part2}. Ánh mắt chất phác, nụ cười tin tưởng hoặc sự trầm tư của nhân vật thể hiện tình thương gia đình sâu sắc."
        b3 = f"00:07.0–00:10.0 | Emotional resonance & peaceful hold, 50mm — Nhịp phim lắng đọng, các thành viên trao nhau ánh nhìn động viên vững chắc. Camera dừng tĩnh ở góc máy điện ảnh chuẩn xác, giữ nguyên 0.5s ở khung hình cuối cùng để chuyển tiếp {next_target}."

    return b1, b2, b3

def get_blockbuster_camera_light(clip_type):
    if clip_type == "COMBAT":
        return "Aggressive 35mm anamorphic wide tracking, low-angle 24mm heroic perspective, dynamic handheld combat camera with subtle micro-shake on kinetic impact. 90-degree shutter angle for razor-sharp martial arts without blurry motion artifacts. Gritty high-contrast cinematic lighting, volumetric rim light through dust/smoke, vibrant neon reflections on armor plates, and horizontal anamorphic flares."
    elif clip_type == "RACING":
        return "High-speed 35mm anamorphic tracking shot mounted low on vehicle chassis, dynamic whip pans tracking drift arcs, intense motion blur on background with razor-sharp vehicle focus. Anamorphic horizontal lens flare streaks from headlights, reflections of streetlights and neon on glossy car bodies."
    elif clip_type == "ARMOR":
        return "Heroic 35mm anamorphic wide framing orbiting slightly around the character, 50mm chest-up hero shot capturing the helmet visor snap. Radiant volumetric light shafts radiating from the wrist core, high dynamic range reflections on polished armor composite plating."
    elif clip_type == "SUSPENSE":
        return "Tense 35mm Dutch tilt moving through narrow spaces, tight 85mm close-ups focusing on sweating brows and trembling hands. Chiaroscuro high-contrast shadows, cold fluorescent or emergency red rotating beacons piercing the darkness."
    else:
        return "Warm, atmospheric 50mm and 85mm prime lens cinematography with shallow depth of field. Soft golden rim lighting from overhead lamps blending with teal neon through windows, natural skin tones with cinematic film grain."

def get_blockbuster_sound(clip_type):
    if clip_type == "COMBAT":
        return "Visceral blockbuster sound design: thunderous sub-bass impact thump, sharp metallic clangs, rapid whoosh of displaced air, mechanical armor servo hum, screaming turbocharged engine, and soaring brass orchestral percussion."
    elif clip_type == "RACING":
        return "High-octane soundscape: deafening roar of high-revving Twin-Turbo engines, screeching tire burnouts, explosive nitrous purge hisses, rattling chassis vibration, and relentless action percussion."
    elif clip_type == "ARMOR":
        return "Epic transformation sound design: high-frequency alien power hum, metallic latching of mechanized armor plates, celestial energy shockwave whoosh, and an inspiring orchestral brass crescendo."
    elif clip_type == "SUSPENSE":
        return "Edge-of-the-seat sound design: ominous low drone, rapid heartbeat bass pulse, ticking countdown audio cue, sharp metallic clicks of tools, and rising string dissonance."
    else:
        return "Subtle emotional sound design: gentle idling engine purr in the background, distant sound of canal water and night crickets, warm acoustic guitar melodies, and natural room reverberation."

for num_str, title, time_range, setting_str, body in scenes:
    scene_num = int(num_str)
    dir_name = f"canh-{scene_num:02d}"
    dir_path = os.path.join(BASE_DIR, dir_name)
    os.makedirs(dir_path, exist_ok=True)
    
    # Bóc tách 6 clip
    clip_pattern = re.compile(r"\* \*\*Clip (\d+) \((.*?)\):\*\* (.*?)(?=(?:\* \*\*Clip \d+)|$)", re.DOTALL)
    raw_clips = clip_pattern.findall(body)
    
    clips_data = []
    for c_num, c_keys, c_desc in raw_clips:
        dialogue = "—"
        desc = c_desc.strip()
        if "*Thoại:*" in desc:
            parts = desc.split("*Thoại:*")
            desc = parts[0].strip()
            dialogue = parts[1].strip()
        clips_data.append({
            "num": int(c_num),
            "keys": c_keys.strip(),
            "desc": desc,
            "dialogue": dialogue
        })
    
    setting_key = get_setting_key(setting_str, scene_num)
    setting_text = SETTING_DESCS[setting_key]
    
    # 1. TẠO README.MD CHO CẢNH
    prev_link = f"[← Cảnh {scene_num-1:02d}](../canh-{scene_num-1:02d}/README.md)" if scene_num > 1 else "← Bắt đầu phim"
    next_link = f"[Cảnh {scene_num+1:02d} →](../canh-{scene_num+1:02d}/README.md)" if scene_num < 45 else "Hết phim (Bữa cơm khải hoàn)"
    
    readme_content = f"""# Biệt Đội Gara — Cảnh {scene_num}: {title}

**Cảnh {scene_num}/45** · Phút {time_range} của phim · Thời lượng: 60s (6 clip × 10s)  
**Tỷ lệ khung hình:** **16:9 ngang (Cinematic Widescreen)** chuẩn màn ảnh rộng YouTube điện ảnh  
**Kịch bản tổng:** [KICH_BAN_45_PHUT_FAST_FURIOUS.md](../KICH_BAN_45_PHUT_FAST_FURIOUS.md) · **Đăng YouTube:** [youtube.md](../youtube.md)

{prev_link} | {next_link}

---

## 1. Tóm tắt cảnh
{clips_data[0]['desc']} Sau đó, {clips_data[2]['desc']} Cuối cùng, {clips_data[5]['desc']}

* **Bối cảnh chính:** {setting_str}
* **Quy cách hình ảnh:** Người thật, giáp cơ khí viền LED sạch, xe độ cơ bắp & JDM Việt hóa. Thoại ngắn gọn, khẩu hình tiếng Việt miền Nam rõ ràng qua kính mũ trong suốt.
* **Thời lượng:** Đúng 60 giây, khớp hoàn hảo 1 phút trên timeline YouTube.

---

## 2. Kịch bản phân cảnh chi tiết (Shot List 60 giây)

| Clip | Thời gian | Cỡ cảnh & Diễn biến | Lời thoại (Lip-sync) | Cách tạo |
|:---:|:---:|---|---|:---:|
"""
    for c in clips_data:
        start_sec = (c['num'] - 1) * 10
        end_sec = c['num'] * 10
        time_str = f"00:{start_sec:02d}–01:00" if end_sec == 60 else f"00:{start_sec:02d}–00:{end_sec:02d}"
        clean_desc = c['desc'].replace("\n", " ").replace("---", "").strip()
        clean_dial = c['dialogue'].replace("\n", " ").replace("---", "").strip()
        mode_str = "Ingredients (Khóa mặt & cảnh)" if c['num'] == 1 else "Frames / Extend (Nối liền)"
        readme_content += f"| {c['num']} | {time_str} | **{clean_desc}** | {clean_dial} | {mode_str} |\n"
    
    readme_content += f"""
---

## 3. Danh sách file prompt Google Flow (Gemini Omni)

Mỗi file đã được chuẩn hóa tỷ lệ **16:9 Cinematic**, copy toàn bộ nội dung file và dán thẳng vào Google Flow:
- [clip-1.md](clip-1.md) — *Mở đầu cảnh (Ingredients, neo giữ mặt nhân vật & xe)*
- [clip-2.md](clip-2.md) — *Frames / Extend nối tiếp*
- [clip-3.md](clip-3.md) — *Frames / Extend nối tiếp*
- [clip-4.md](clip-4.md) — *Frames / Extend nối tiếp*
- [clip-5.md](clip-5.md) — *Frames / Extend nối tiếp*
- [clip-6.md](clip-6.md) — *Frames / Extend nối tiếp (Cú lật / Hook sang cảnh sau)*

Caption đăng TikTok / Shorts độc lập: [caption.md](caption.md)
"""
    with open(os.path.join(dir_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)
        
    # 2. TẠO CAPTION.MD
    caption_content = f"""# Caption · Biệt Đội Gara · Phần {scene_num}/45: {title}

> Caption cho video ngắn TikTok / YouTube Shorts cắt từ Cảnh {scene_num} (Phút {time_range}).  
> Thời lượng: 60 giây. Khung hình: 16:9 hoặc crop 9:16.

## Caption đề xuất
```text
Biệt Đội Gara · Tập {scene_num}/45: {title} 🏎️🔥

{clips_data[0]['desc']}
{clips_data[4]['desc']}

"Muốn đua thì lên đường đua. Ra đường là chở người mình thương!" ❤️
📺 Xem trọn bộ phim điện ảnh 45 phút trên kênh YouTube Biệt Đội Gara (Link ở bio).

#bietdoigara #phimhanhdong #fastandfurious #sieuanhhung #phimvietnam
```

## Bình luận ghim (Pinned Comment)
```text
Theo bạn tình huống ở Cảnh {scene_num} này ai xử lý ngầu nhất? Bình luận bên dưới nhé! 👇
```

## Checklist khi đăng
- Bật nhãn **"Nội dung do AI tạo"** (AI-generated content).
- Không gắn giỏ hàng thương mại.
- Tương tác với khán giả theo tinh thần gia đình Gara Bảy.
"""
    with open(os.path.join(dir_path, "caption.md"), "w", encoding="utf-8") as f:
        f.write(caption_content)
        
    # 3. TẠO CLIP-1.MD ĐẾN CLIP-6.MD (Giữ lại Cảnh 02 thủ công tinh xảo)
    if scene_num == 2:
        print(f"Bảo tồn Cảnh 02 đã tối ưu thủ công tinh xảo.")
        continue

    # Xác định các nhân vật xuất hiện
    chars_present = []
    keys_str = " ".join([c['keys'] for c in clips_data])
    for k in ["THANG", "LAN", "HAI", "KHOI", "MINH", "TU", "SOI", "GOONS", "BACBAY"]:
        if k in keys_str:
            chars_present.append(k)
    if not chars_present:
        chars_present = ["THANG", "LAN", "HAI", "KHOI"]
        
    # Clip 1 (ING - Full prompt)
    char_blocks_full = []
    for cp in chars_present:
        if f"{cp}_G" in keys_str and f"{cp}_G" in CHAR_FULL_MAP:
            char_blocks_full.append(CHAR_FULL_MAP[f"{cp}_G"])
        elif f"{cp}_R" in keys_str and f"{cp}_R" in CHAR_FULL_MAP:
            char_blocks_full.append(CHAR_FULL_MAP[f"{cp}_R"])
        elif cp in CHAR_FULL_MAP:
            char_blocks_full.append(CHAR_FULL_MAP[cp])
    char_full_text = "\n".join(char_blocks_full)
    
    c1 = clips_data[0]
    c1_type = classify_clip(c1['desc'], c1['dialogue'], title)
    b1_1, b1_2, b1_3 = generate_blockbuster_shotlist(c1['desc'], c1['dialogue'], c1_type, 1, is_clip1=True)
    c1_cam_light = get_blockbuster_camera_light(c1_type)
    c1_sound = get_blockbuster_sound(c1_type)

    clip1_prompt = f"""[FORMAT]
Widescreen 16:9 (2.39:1 anamorphic ratio), 10-second clip, photorealistic live-action superhero blockbuster action film style. 24fps high-budget Hollywood cinematography, crisp 90-degree shutter angle capturing razor-sharp kinetic motion with zero blurry artifacts. High-contrast Saigon cinematic color grade, 24fps. No guns or firearms anywhere. Dialogue in Vietnamese with natural Southern accent and lip-sync through clear helmet visors. No subtitles or on-screen text.

[CHARACTERS — match attached reference images]
{char_full_text}

[SETTING]
{setting_text}
Time: Scene {scene_num}/45, timecode {time_range}. Atmosphere: high-adrenaline blockbuster action, cinematic tension, emotional bond.

[CAMERA & LIGHT]
{c1_cam_light}

[SHOT LIST]
{b1_1}
{b1_2}
{b1_3}

[SOUND]
{c1_sound}

[END FRAME]
Clean freeze on the final frame of the action beat for seamless continuation into clip 2.

[AVOID]
guns, firearms, knives, blood, gore, visible wounds, deaths, real brand logos, readable license plates, watermarks, text overlays, extra fingers, cartoon or anime look, slow sluggish motion, blurry motion smear, awkward wind-up.
"""
    with open(os.path.join(dir_path, "clip-1.md"), "w", encoding="utf-8") as f:
        f.write(clip1_prompt)
        
    # Clip 2 đến Clip 6 (FR - Frame Extend)
    for c_idx in range(1, 6):
        c_item = clips_data[c_idx]
        prev_idx = c_idx
        cur_idx = c_idx + 1
        
        char_blocks_short = []
        for cp in chars_present:
            if f"{cp}_G" in keys_str and f"{cp}_G" in CHAR_SHORT_MAP:
                char_blocks_short.append(CHAR_SHORT_MAP[f"{cp}_G"])
            elif cp in CHAR_SHORT_MAP:
                char_blocks_short.append(CHAR_SHORT_MAP[cp])
        char_short_text = "\n".join(char_blocks_short)
        
        c_type = classify_clip(c_item['desc'], c_item['dialogue'], title)
        b_1, b_2, b_3 = generate_blockbuster_shotlist(c_item['desc'], c_item['dialogue'], c_type, cur_idx, is_clip1=False)
        cam_light = get_blockbuster_camera_light(c_type)
        sound_desc = get_blockbuster_sound(c_type)
        
        clip_fr_prompt = f"""Continue the scene seamlessly from the final frame of clip {prev_idx}, which is the first frame of this clip. Same characters, outfits, vehicles, lighting, and 16:9 cinematic widescreen framing. Flawless continuity with zero jump cut.
Widescreen 16:9 (2.39:1 anamorphic ratio), 10-second clip, photorealistic live-action superhero blockbuster action film style. 24fps high-octane cinema, crisp 90-degree shutter angle capturing razor-sharp kinetic martial arts and stunts with zero blurry artifacts. Spoken dialogue in natural Southern Vietnamese with lip-sync. Cut only where the shot list says. No subtitles or on-screen text.

[CHARACTERS — unchanged]
{char_short_text}

[CAMERA & LIGHT]
{cam_light}

[SHOT LIST]
{b_1}
{b_2}
{b_3}

[SOUND]
{sound_desc}

[END FRAME]
Hold final frame still for 0.5s for seamless extension to clip {cur_idx + 1 if cur_idx < 6 else 'next scene'}.

[AVOID]
guns, blood, visible injuries, brand logos, watermarks, jump cuts, distorted hands, subtitles, text, cartoon or anime look, slow sluggish motion, blurry motion smear, awkward wind-up.
"""
        with open(os.path.join(dir_path, f"clip-{cur_idx}.md"), "w", encoding="utf-8") as f:
            f.write(clip_fr_prompt)

print("Đã tái tạo và tối ưu thành công toàn bộ 45 thư mục cảnh (canh-01 đến canh-45) chuẩn bom tấn hành động điện ảnh!")
