#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tự động sinh toàn bộ hệ thống 45 thư mục cảnh (canh-01 đến canh-45)
cho series phim điện ảnh 45 phút Biệt Đội Gara (Fast & Furious style).
Mỗi thư mục có:
- README.md: Kịch bản điện ảnh chi tiết 60 giây (6 clip x 10s)
- caption.md: Caption TikTok / Shorts
- clip-1.md đến clip-6.md: Prompt Google Flow / Gemini Omni định dạng Widescreen 16:9
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
    "BACBAY": """BÁC BẢY (HOLOGRAM): kind elderly Vietnamese mechanic in late 60s, crew cut, warm smile lines, blue work shirt, glowing soft-blue hologram; warm elderly Southern male voice."""
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
        # Tách mô tả và thoại
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
        
    # 3. TẠO CLIP-1.MD ĐẾN CLIP-6.MD
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
        # Check if armor or civilian
        if f"{cp}_G" in keys_str and f"{cp}_G" in CHAR_FULL_MAP:
            char_blocks_full.append(CHAR_FULL_MAP[f"{cp}_G"])
        elif f"{cp}_R" in keys_str and f"{cp}_R" in CHAR_FULL_MAP:
            char_blocks_full.append(CHAR_FULL_MAP[f"{cp}_R"])
        elif cp in CHAR_FULL_MAP:
            char_blocks_full.append(CHAR_FULL_MAP[cp])
    char_full_text = "\n".join(char_blocks_full)
    
    c1 = clips_data[0]
    clip1_prompt = f"""[FORMAT]
Widescreen 16:9, 10-second clip, photorealistic live-action superhero action film look, cinematic anamorphic lens flares: real Vietnamese people with natural skin textures; sleek practical armor with composite plates and glowing colored LED lines; energy powers are pure clean light (no fire damage, no blood). High-contrast Saigon cinematic color grade, 24fps. No guns or firearms anywhere. Dialogue in Vietnamese with natural Southern accent and lip-sync through clear helmet visors. No subtitles or on-screen text.

[CHARACTERS — match attached reference images]
{char_full_text}

[SETTING]
{setting_text}
Time: Scene {scene_num}/45, timecode {time_range}. Atmosphere: high-adrenaline action, tension, emotional bond.

[CAMERA & LIGHT]
Cinematic anamorphic 35mm wide angle for action beats, 50mm and 85mm for emotional character close-ups; dynamic camera tracking and stable gimbal movements; neon and sodium reflections.

[SHOT LIST]
00:00–00:03 | Establishing shot, 35mm — {c1['desc']}
00:03–00:07 | Medium shot, 50mm — Action intensifies. Character speaking: {c1['dialogue']}
00:07–00:10 | Dynamic close-up, 85mm — Reaction shot and movement towards the next beat. Hold final action for seamless frame extend.

[SOUND]
Engine roar, tire screech on pavement, mechanical armor hum, deep cinematic percussion and bass pulses.

[END FRAME]
Clean freeze on the final frame of the action beat for seamless continuation into clip 2.

[AVOID]
guns, firearms, knives, blood, gore, visible wounds, deaths, real brand logos, readable license plates, watermarks, text overlays, extra fingers, cartoon or anime look.
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
        
        clip_fr_prompt = f"""Continue the scene seamlessly from the final frame of clip {prev_idx}, which is the first frame of this clip. Same characters, outfits, vehicles, lighting, and 16:9 cinematic widescreen framing. Flawless continuity with zero jump cut.
Widescreen 16:9, 10-second clip, photorealistic live-action superhero film style. Spoken dialogue in natural Southern Vietnamese with lip-sync. Cut only where the shot list says. No subtitles or on-screen text.

[CHARACTERS — unchanged]
{char_short_text}

[CAMERA & LIGHT]
Same lighting and cinematic 16:9 widescreen composition. 85mm close-up for speech and 35mm wide for vehicular stunts and combat.

[SHOT LIST]
00:00–00:03.5 | Continuing seamlessly from the last frame — {c_item['desc']}
00:03.5–00:07 | Dynamic action progression. Character line: {c_item['dialogue']}
00:07–00:10 | Culmination of this beat, setting up the next action transition.

[SOUND]
Immersive sound design: roaring engine turbos, mechanical armor servos, whoosh of wind and cinematic orchestral score.

[END FRAME]
Hold final frame still for 0.5s for seamless extension to clip {cur_idx + 1 if cur_idx < 6 else 'next scene'}.

[AVOID]
guns, blood, visible injuries, brand logos, watermarks, jump cuts, distorted hands, subtitles, text.
"""
        with open(os.path.join(dir_path, f"clip-{cur_idx}.md"), "w", encoding="utf-8") as f:
            f.write(clip_fr_prompt)

print("Đã tạo thành công toàn bộ 45 thư mục cảnh (canh-01 đến canh-45) với đầy đủ README, caption, và 6 clip prompts 16:9!")
