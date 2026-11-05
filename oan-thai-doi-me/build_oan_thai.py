#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build complete production package for 'Oán Thai Đòi Mẹ: Búp Bê Đất Nung' (oan-thai-doi-me)
14 Scenes x 6 Clips x 10s = 84 Clips (14 minutes)
80% Off-screen Narrator Voice-Over (67 clips) + 20% Shock/Climax Character Lip-Sync (17 clips)
100% Standard Northern Vietnamese accent (giọng chuẩn miền Bắc) — ZERO real-world geographic names.
Gritty, visceral horror visual staging and bespoke multi-layered diegetic horror sound design.
"""

import os
from shot_data_gritty import SCENE_META, SCENE_SPATIAL_LOCKS, ALL_SHOTS

BASE_DIR = "/Users/iseul-a/Documents/TikTokSeries/oan-thai-doi-me"

CHARACTER_SPECS = {
    "@Bach": {
        "name": "Bách (Trần Nguyên Bách)",
        "age": 30,
        "voice_lock": "VOICE_LOCK_BACH_OANTHAI",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Bach, a 30-year-old Vietnamese male 3D spatial scanning engineer, "
            "175 cm, lean build, angular face with tired attentive dark eyes behind thin metal-frame glasses, short natural parted black hair, "
            "wearing a charcoal-grey windbreaker jacket over a plain black crew-neck T-shirt, dark cargo trousers, and dusty hiking boots, "
            "carrying a compact handheld 3D LiDAR scanner; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
        ),
        "block": (
            "@Bach = Trần Nguyên Bách: same approved identity, age 30; Vietnamese male 3D LiDAR spatial engineer, 175 cm, lean build, "
            "angular face with expressive dark eyes behind thin metal-rimmed glasses, short natural black hair. Wardrobe: charcoal-grey windbreaker "
            "jacket over a black cotton T-shirt, dark slate trousers. Voice profile: [VOICE_LOCK_BACH_OANTHAI — Cố định giọng Bách chuẩn miền Bắc "
            "xuyên suốt 84 clips]: Fixed 30-year-old native Standard Northern Vietnamese male voice, warm mid-baritone register, natural "
            "Standard Northern Vietnamese cadence that tightens with breathless urgency, raw terror, and paternal anguish in horror climax moments. Strictly lock this exact "
            "Standard Northern Vietnamese vocal identity across every clip; never use Southern or Mekong Delta accent/slang."
        ),
    },
    "@Ha": {
        "name": "Hà (Lê Thanh Hà)",
        "age": 28,
        "voice_lock": "VOICE_LOCK_HA_OANTHAI",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Ha, a 28-year-old pregnant Vietnamese female antique ceramic conservator "
            "(7 months pregnant), 162 cm, gentle oval face with pale complexion and expressive sorrowful dark eyes, long black hair pinned in a low "
            "bun with a wooden hairpin, wearing a loose cream-beige linen maternity dress with a brown canvas studio apron smudged with dried terracotta "
            "clay over her visible 7-month pregnant belly, flat indoor cloth slippers; plain grey studio background, soft side light, 8K. Not resembling any real actor."
        ),
        "block": (
            "@Ha = Lê Thanh Hà: same approved identity, age 28; Vietnamese female antique ceramic conservator, 7 months pregnant, 162 cm, "
            "delicate oval face, pale skin, expressive dark eyes, long black hair fastened in a low bun with a carved wooden hairpin. "
            "Wardrobe: soft cream-beige linen maternity dress with a visible 7-month pregnant belly and a brown canvas potter apron lightly dusted "
            "with terracotta clay. Voice profile: [VOICE_LOCK_HA_OANTHAI — Cố định giọng Hà chuẩn miền Bắc xuyên suốt 84 clips]: Fixed 28-year-old "
            "native Standard Northern Vietnamese female voice, soft lyrical mezzo-soprano register, gentle maternal warmth that shifts to a "
            "bone-chilling trance-like Northern whisper when singing the clay-doll nursery rhyme or pleading in raw terror. Strictly lock this exact Standard Northern "
            "Vietnamese vocal identity across every clip; never use Southern or Mekong Delta accent/slang."
        ),
    },
    "@ThayPhong": {
        "name": "Thầy Phong",
        "age": 36,
        "voice_lock": "VOICE_LOCK_THAYPHONG_OANTHAI",
        "ref_prompt": (
            "Full-body photorealistic character reference of @ThayPhong, a 36-year-old Vietnamese folklore scholar and Taoist ritual master, "
            "174 cm, composed athletic build, sharp cheekbones, calm piercing dark eyes, neat short black hair, wearing a dark indigo-black stand-collar "
            "linen shirt (áo sơ mi cổ tàu tối màu), dark trousers, a 108-bead black ebony prayer mala around his left wrist, holding an antique brass "
            "geomancy compass (la bàn đồng); plain grey studio background, soft side light, 8K. Not resembling any real actor."
        ),
        "block": (
            "@ThayPhong = Thầy Phong: same approved identity, age 36; Vietnamese ancient-script researcher and ritual master, 174 cm, composed lean build, "
            "sharp observant dark eyes, neat short black hair. Wardrobe: dark indigo-black stand-collar linen shirt, charcoal trousers, 108-bead black "
            "ebony prayer bracelet on his left wrist, carrying an antique brass feng-shui compass and cinnabar brush. Voice profile: "
            "[VOICE_LOCK_THAYPHONG_OANTHAI — Cố định giọng Thầy Phong chuẩn miền Bắc xuyên suốt 84 clips]: Fixed 36-year-old native Standard Northern "
            "Vietnamese male voice, resonant authoritative low baritone, crisp articulation, calm and commanding spiritual gravitas. Strictly lock "
            "this exact Standard Northern Vietnamese vocal identity across every clip; never use Southern or Mekong Delta accent/slang."
        ),
    },
    "@BaLua": {
        "name": "Bà Lụa (Oán Linh Người Thợ Gốm Năm Xưa)",
        "age": 32,
        "voice_lock": "VOICE_LOCK_BALUA_OANTHAI",
        "ref_prompt": (
            "Full-body photorealistic character reference of @BaLua, a 32-year-old traditional Vietnamese female potter from the 1990s, "
            "158 cm, gaunt sorrowful face dusted with pale grey kiln ash, tearful dark eyes, long disheveled black hair partly covering one cheek, "
            "wearing a weathered dark-brown traditional Vietnamese cotton blouse (áo cánh nâu sồng) and black trousers stained with dried grey clay, "
            "calloused clay-crusted hands, barefoot; plain grey studio background, cool moonlit side light, 8K. Clean cinematic ghost appearance, no gore."
        ),
        "block": (
            "@BaLua = Bà Lụa (Vong hồn người thợ gốm năm 1996): same approved identity, age 32; sorrowful Vietnamese female potter apparition, "
            "158 cm, pale ash-dusted complexion with natural skin texture (no gore, no facial distortion), tearful pleading dark eyes, long "
            "black hair falling past her cheeks. Wardrobe: traditional weathered dark-brown cotton blouse (áo cánh nâu sồng) and black trousers smudged "
            "with grey kiln ash and dried clay, barefoot, calloused hands. Always silent on screen (mouth remains closed), communicating through tragic "
            "maternal gestures."
        ),
    },
}

NARRATOR_VOICE_BLOCK = (
    "Narrator (Người Dẫn Chuyện) = Off-screen 40-year-old native Standard Northern Vietnamese male horror storyteller. "
    "Voice profile: [VOICE_LOCK_NARRATOR_OANTHAI — Cố định giọng Nam Người Dẫn Chuyện chuẩn miền Bắc xuyên suốt 84 clips]: "
    "Deep, bone-chilling 40-year-old native Standard Northern Vietnamese male baritone voice (giọng nam chuẩn miền Bắc trầm lạnh, gai góc kể chuyện ma đêm khuya, "
    "classic Northern Vietnamese ghost-storyteller cadence with crisp consonant distinction, dark gravelly resonance, and authentic Northern tones). "
    "Strictly lock this exact Standard Northern Vietnamese male narrator voice across all 84 clips; NEVER use a Southern Vietnamese (Saigon/Mekong Delta) or Central accent, "
    "and never sound like a cheerful announcer or robotic TTS engine."
)

LOCATIONS = {
    "ABANDONED_KILN_HOUSE": (
        "Abandoned ancient brick pottery kiln house at the edge of a desolate riverbank graveyard (xưởng lò bầu gốm cổ bỏ hoang cuối bãi tha ma ven sông vắng): "
        "towering moss-covered dome of soot-blackened wood-fired red-grey bricks, kiln mouth bricked shut and crisscrossed with rotting blood-red threads, "
        "jagged terracotta shards and cold grey bone-ash covering the damp earthen floor, cobwebbed wooden roof beams, eerie blood-red twilight or stormy midnight rain."
    ),
    "RESTORATION_STUDIO_HOME": (
        "Dimly lit antique ceramic restoration studio inside an old two-story wooden house (gian phòng phục chế gốm cổ âm u trong căn nhà gỗ hai tầng tĩnh mịch): "
        "dark ironwood worktable with a manual wooden potter's wheel, flickering tungsten lamp and blood-red nightlight casting deep shadows against damp peeling walls, "
        "wooden shelves lined with cracked antique ceramic jars, a tarnished round brass-rimmed wall mirror, bowls of wet blood-red terracotta clay, sharp steel carving tools, "
        "and an adjacent workroom with a 3D point-cloud monitor and a white rattan baby crib."
    ),
}

SHOT_TYPES = [
    ("ESTABLISHING_WIDE", "24mm", "24mm stabilized gimbal slow creeping push-in establishing claustrophobic spatial geometry and suffocating folk-horror dread"),
    ("MEDIUM_SHOT", "35mm", "35mm controlled dolly-in tracking character upper-body tension, trembling hands, and unsettling micro-expressions"),
    ("CLOSE_UP", "50mm", "50mm intimate shallow-depth close-up isolating visceral hand/prop interaction, cold sweat, and raw psychological terror"),
    ("OVER_SHOULDER", "50mm", "50mm over-the-shoulder framing connecting foreground subject with midground supernatural apparition or cursed clay effigy"),
    ("MEDIUM_CLOSEUP", "50mm", "50mm slow creeping push-in on character face and upper torso during peak horror revelation"),
    ("INSERT_CLOSEUP", "85mm", "85mm macro-style cinematic horror insert with sharp rack focus locking the spine-chilling cliffhanger detail"),
]


def build_scenes_data():
    scenes = []
    for s_num in range(1, 15):
        meta = SCENE_META[s_num]
        clips = []
        for c_num in range(1, 7):
            sh = ALL_SHOTS[(s_num, c_num)]
            clips.append({
                "scene_num": s_num,
                "clip_num": c_num,
                "timerange": sh["timerange"],
                "is_vo": sh["is_vo"],
                "speaker_tag": sh["speaker_tag"],
                "speed": sh["speed"],
                "meta": "VO - NGƯỜI DẪN CHUYỆN" if sh["is_vo"] else "THOẠI TRỰC TIẾP - LIP-SYNC",
                "beat1": sh["beat1"],
                "beat2": sh["beat2"],
                "beat3": sh["beat3"],
                "eng_action": sh["eng_action"],
                "dialogue": sh["dialogue"],
                "sound": sh["sound"],
                "chars": sh["chars"],
            })
        scenes.append({
            "scene_num": s_num,
            "act": meta.get("act"),
            "title": meta["title"],
            "story_time": meta["story_time"],
            "time_span": meta["time_span"],
            "loc_id": meta["loc_id"],
            "loc_desc_vi": meta["loc_desc_vi"],
            "clips": clips,
        })
    return scenes


def build_clip_markdown(scene, clip):
    s_num = scene["scene_num"]
    c_num = clip["clip_num"]
    shot_type, lens, cam_plan = SHOT_TYPES[(c_num - 1) % 6]
    eng_action = clip["eng_action"]
    loc_id = scene["loc_id"]
    loc_en = LOCATIONS[loc_id]
    spatial_lock, props_lock = SCENE_SPATIAL_LOCKS[s_num]

    chars = clip["chars"]
    char_tags_str = ", ".join(chars)
    char_blocks = "\n".join(CHARACTER_SPECS[c]["block"] for c in chars)

    word_count = len(clip["dialogue"].split())
    if clip["is_vo"]:
        eng_action_full = (
            eng_action
            + f" Throughout 0.8–9.2s, an off-screen 40-year-old Standard Northern Vietnamese male horror narrator (VOICE_LOCK_NARRATOR_OANTHAI) "
            f"speaks the Vietnamese voice-over in a deep, bone-chilling Standard Northern Vietnamese baritone accent (giọng nam chuẩn miền Bắc trầm lạnh, gai góc kể chuyện ma đêm khuya, speed {clip['speed']}, strictly NO Southern/Saigon accent) while all on-screen characters keep their mouths closed."
        )
        mouth_map = (
            "0.0–10.0s: Off-screen Standard Northern Vietnamese male horror narrator voice-over ONLY (VOICE_LOCK_NARRATOR_OANTHAI — giọng nam chuẩn miền Bắc trầm lạnh); "
            "all on-screen characters keep their mouths naturally closed throughout 0.0–10.0s and perform purely through unblinking eye tension, trembling breath, cold sweat, and visceral physical action."
        )
        dialogue_line = (
            f'- Turn 1 [0.8–9.2s] Off-Screen Male Narrator (Người Dẫn Chuyện — VOICE_LOCK_NARRATOR_OANTHAI | '
            f'speaking off-screen in a deep, bone-chilling 40-year-old Standard Northern Vietnamese male baritone accent — '
            f'giọng nam chuẩn miền Bắc trầm lạnh, gai góc kể chuyện ma đêm khuya at {clip["speed"]} speed; '
            f'strictly NO Southern/Saigon accent; all on-screen mouths remain closed): "{clip["dialogue"]}"'
        )
    else:
        eng_action_full = eng_action
        sp = clip["speaker_tag"]
        v_lock = CHARACTER_SPECS[sp]["voice_lock"]
        sp_name = CHARACTER_SPECS[sp]["name"]
        mouth_map = (
            f"0.0–3.0s: mouth closed during tense setup beat; 3.0–7.0s: ONLY {sp_name} ({sp}) moves their lips on screen with accurate syllable-level "
            f"Standard Northern Vietnamese lip-sync ({v_lock}); 7.0–10.0s: mouth closed during horror reaction beat, reacting through eyes and heavy breathing; "
            f"every other character in frame keeps their mouth naturally closed throughout 0.0–10.0s."
        )
        dialogue_line = (
            f'- Turn 1 [3.0–7.0s] {sp_name} ({sp}) '
            f'[thoại trực tiếp trên hình | {v_lock} | giọng chuẩn miền Bắc {clip["speed"]}, '
            f'cảm xúc kinh dị gai góc chân thực, khớp khẩu hình]: "{clip["dialogue"]}"'
        )

    md = f"""[FORMAT]
10 seconds (0.0s–10.0s), full-frame 16:9 widescreen, 24 fps, photorealistic live-action Vietnamese supernatural folk-horror film. Model: `omni_flash` (Google Flow Omni 10s Ingredients Reference-to-Video). Shutter: 180-degree cinema shutter (24 fps) for gritty motion cadence, visceral psychological dread, realistic skin pores, cold sweat texture, and raw cinema sensor grain. Scene category: SUPERNATURAL_FOLK_HORROR | Dialect: Standard Northern Vietnamese accent (giọng chuẩn miền Bắc). Color grade: Gritty Vietnamese folk-horror palette — dried blood-terracotta reds, deep kiln-ash charcoal blacks, flickering candle/nightlight crimson contrasted with cold cyan-green LiDAR and corpse-pale moonlight shadows, realistic Vietnamese skin tones. In a single continuous shot from 0.0s to 10.0s (Google Flow Omni 10s (`omni_flash`, 10.0s Ingredients Reference-to-Video locking {char_tags_str}), shot type: {shot_type}): ONE camera setup and ONE real story location throughout the entire 10-second clip. Full-bleed 16:9 widescreen image filling 100% of the canvas edge-to-edge: strictly NO black letterbox bars at top or bottom, NO camera viewfinder/HUD metadata overlays, NO burned-in titles/captions/subtitles, NO film-strip borders, and NO split-screen panels. No scene cuts, no hard cuts, no whip-pan, no teleportation, and never flash or cut to an attached character reference portrait or plain grey studio backdrop at any point in the clip.

[CHARACTERS — approved identities, wardrobe, carried props and locked Standard Northern Vietnamese voice profiles]
Use the attached reference images strictly for facial identity, hair, and wardrobe design inside the live story environment. Only the listed characters appear in frame.
{char_blocks}
{NARRATOR_VOICE_BLOCK}

[TIMELINE AND LOCATION]
Scene {s_num:02d}/14, clip {c_num}/6; shot {s_num:02d}.{c_num} (10.0s | Model: `omni_flash` 10s). Story time: {scene["story_time"]} ({clip["timerange"]}).
{loc_en}
[FIXED SCENE SPATIAL LOCK — Cố định không gian xuyên suốt Cảnh {s_num:02d} (Clip 1–6)]
{spatial_lock}
Strict spatial rule: Lock this exact spatial geometry, compass axis and architectural boundary across all 6 clips (Clip 1–6, 6 × 10s = 60s) of Scene {s_num:02d}.

[DRAMATIC INTENT — show through visceral horror behaviour, never narrate this note]
{clip["beat2"]}

[ACTION — 0.0s–10.0s, one continuous evolving take]
- English Visual Choreography (0.0–10.0s): {eng_action_full}
- Beat 1 (0.0–3.0s — Thiết lập không gian rùng rợn & khởi phát hành động): {clip["beat1"]}
- Beat 2 (3.0–7.0s — Cao trào kinh dị & tương tác gai góc): {clip["beat2"]}
- Beat 3 (7.0–10.0s — Dư chấn tâm lý & điểm dừng rợn gáy): {clip["beat3"]}
Single continuous motion rule: Play Beat 1 (0.0–3.0s) -> Beat 2 (3.0–7.0s) -> Beat 3 (7.0–10.0s) once in contiguous order from 0.0s to 10.0s as one seamless, fluid physical motion curve; characters never freeze physical movement, gestures never repeat, and all horror tension is raw, grounded, and visceral.

[BLOCKING AND PERFORMANCE]
- Spatial Blocking: Characters ({char_tags_str}) maintain consistent screen positions within {loc_id} matching the continuous 0.0s -> 3.0s -> 7.0s -> 10.0s action flow.
- Acting & Micro-Expressions: Gritty, spine-chilling Vietnamese live-action horror performance; trembling fingers, cold sweat, dilated pupils, heavy ragged breathing, visceral physical interaction with unglazed terracotta clay and ritual props.

[CAMERA — Shot Size, Lens, Movement & Continuity]
- Lens & Shot Type: {lens}, 24 fps, 180-degree shutter, {shot_type}.
- Camera Movement Plan (0.0–10.0s): {cam_plan}. Smooth acceleration and deceleration, level horizon, natural 3D parallax between foreground, midground and background. Never cut or jump axis inside the 10-second shot.

[PROPS & VISIBLE TEXTURE]
[FIXED SCENE OBJECT INVENTORY — Chỉ xoay quanh các vật thể cố định của Cảnh {s_num:02d}]
{props_lock}
- Visible Material & Lighting Texture: Raw porous unglazed terracotta clay grain, dried blood-crimson cinnabar paste, soot-blackened kiln ash, damp rotting wood, flickering red/amber shadows against deep abyssal darkness.
Strict prop rule: Hands grip props with realistic weight and 5 natural fingers; objects never float, morph or vanish.

[BODY, MOUTH AND FACE CONSISTENCY]
Lock character facial identity, hair, age, body proportions and wardrobe strictly to the approved references throughout the 10-second shot. No facial distortion or morphing during head turns. Natural blinks, matched eyelines, subtle breathing and micro-expressions.
Mouth & Lip-Sync Map: {mouth_map}

[VOICE & DIALOGUE LOCK — STANDARD NORTHERN VIETNAMESE (GIỌNG CHUẨN MIỀN BẮC)]
Mandatory Dialect & Voice Lock: 100% Standard Northern Vietnamese accent (Giọng chuẩn miền Bắc).
- Off-Screen Narrator (`VOICE_LOCK_NARRATOR_OANTHAI`): Deep, bone-chilling 40-year-old native Standard Northern Vietnamese male horror storyteller baritone voice (giọng nam chuẩn miền Bắc trầm lạnh, gai góc kể chuyện ma đêm khuya).
- On-Screen Characters (`VOICE_LOCK_BACH_OANTHAI`, `VOICE_LOCK_HA_OANTHAI`, `VOICE_LOCK_THAYPHONG_OANTHAI`): Native Standard Northern Vietnamese voices matching each character's locked register.
Voice direction: "Authentic native Standard Northern Vietnamese speech and late-night horror storytelling, crisp Northern phonology and tonal cadence, deep resonant chest baritone for the off-screen male narrator, organic breath control, and raw live-action Vietnamese horror cinema delivery. Strictly forbid Southern Vietnamese (Saigon) or Mekong Delta accent, and never use a robotic TTS monotone."

[DIALOGUE — Timed to Action (1 turn(s), {word_count} Vietnamese words)]
{dialogue_line}
Spoken Audio Rule: Only the Vietnamese words inside the quotation marks ("...") are spoken aloud. Never read speaker names, @tags, timestamps, voice-lock IDs, or bracketed stage notes. No on-screen captions, subtitles, or watermarks.

[SOUND — Bespoke Gritty Horror Soundscape (0.0s–10.0s)]
- Foreground & Ambience Horror SFX (0.0–10.0s): {clip["sound"]}
- Audio Discipline: Clean forward Standard Northern Vietnamese voice layered over raw, visceral, cause-driven diegetic horror sound effects (scraping unglazed clay, cracking joints/wood, sub-bass kiln resonance, ragged breathing, wet mud squelches, and eerie silence) synchronized to visible actions from 0.0s to 10.0s. No cheerful or generic stock music.

[EDIT IN — do not render the previous shot again]
Cut directly into Shot {s_num:02d}.{c_num} at 0.0s inside the locked Scene {s_num:02d} environment ({clip["timerange"]}) via Google Flow Omni 10s (`omni_flash`). Never flash or display any studio reference portrait or grey backdrop.

[START FRAME — state only, not an action to repeat]
{clip["beat1"]}

[END FRAME — lock position, props, eyeline & movement axis]
{clip["beat3"]}
"""
    return md


def build_kich_ban_markdown(scenes):
    lines = [
        "# Kịch Bản Phân Cảnh Chi Tiết — Oán Thai Đòi Mẹ: Búp Bê Đất Nung (v2.0 Gritty Folk-Horror — 14 Cảnh × 6 Clips × 10s = 84 Clips / 14 Phút)",
        "",
        "- **Tổng thời lượng:** **14 Cảnh × 6 Clips × 10 giây = 84 Clips (840 giây / 14 phút)** | Model: **`omni_flash` (Google Flow Omni 10s Ingredients R2V)** | Ngôn ngữ: **Tiếng Việt giọng chuẩn miền Bắc** (tuyệt đối không dùng địa danh thực tế).",
        "- **Phong cách Hình ảnh & Âm thanh (`Gai Góc – Rùng Rợn – Đậm Chất Phim Ma Cổ Thuật`):**",
        "  - **Bối cảnh hư cấu ám ảnh:** Xưởng lò bầu gốm cổ bỏ hoang cuối bãi tha ma ven sông vắng & căn nhà gỗ hai tầng tĩnh mịch ngập bóng tối và ánh đèn ngủ đỏ quạch.",
        "  - **Âm thanh kinh dị thiết kế riêng cho từng clip (`84 bespoke soundscapes`):** Tiếng móng tay cào ken két lên sành đất nung khô, tiếng đất khát máu hút giọt máu tươi kêu *'xèo... sụp!'*, tiếng bay gỗ miết xóa bùa kèm lửa nến nổ xanh lè, tiếng dao thép rạch miệng tượng trào tro đen, tiếng hát đồng dao lúc 2 giờ sáng, tiếng khóc nghẹt trong rương gỗ khóa kín và tiếng da thịt hóa sành rạn nứt *'răng rắc'*.",
        "- **Công thức Âm thanh & Thoại (`80% Người Dẫn Chuyện VO Giọng Nam Chuẩn Miền Bắc + 20% Thoại Nhân Vật Bất Ngờ Lip-Sync`):**",
        "  - **80% Clips (`67/84 clips` — `[VO - NGƯỜI DẪN CHUYỆN]`):** Giọng nam chuẩn miền Bắc trầm lạnh, gai góc (`VOICE_LOCK_NARRATOR_OANTHAI`, `0.90x–1.00x`, phong cách kể chuyện ma đêm khuya lạnh sống lưng); nhân vật trên màn hình **khép miệng hoàn toàn (`mouth remains closed 0.0–10.0s`)**, diễn xuất 100% bằng ánh mắt thất thần, gân máu, mồ hôi lạnh và hành động.",
        "  - **20% Clips (`17/84 clips` — `[THOẠI TRỰC TIẾP - LIP-SYNC]`):** Nhân vật mở miệng nói trực tiếp trên hình bằng giọng chuẩn miền Bắc ở đúng 17 khoảnh khắc giật mình, hát đồng dao điểm nhãn lúc 2 giờ sáng, quát hỏi trừ tà và gào khóc sinh tử.",
        "",
        "---",
    ]

    for scene in scenes:
        s_num = scene["scene_num"]
        if scene["act"]:
            lines.extend(["", f"## {scene['act']}", ""])
        spatial_lock, props_lock = SCENE_SPATIAL_LOCKS[s_num]
        lines.extend([
            f"### Cảnh {s_num:02d}: {scene['title']} (`6 × 10s = 60s` | `{scene['story_time']}` | `{scene['time_span']}`)",
            f"- **Bối cảnh:** `{scene['loc_id']}` — {scene['loc_desc_vi']}",
            f"- **Khóa Không Gian:** {spatial_lock}",
            f"- **Khóa Đạo Cụ:** {props_lock}",
            "",
        ])
        for clip in scene["clips"]:
            c_num = clip["clip_num"]
            shot_type, lens, cam_plan = SHOT_TYPES[(c_num - 1) % 6]
            chars_str = ", ".join(clip["chars"])
            if clip["is_vo"]:
                eng_full = (
                    clip["eng_action"]
                    + f" Throughout 0.8–9.2s, an off-screen 40-year-old Standard Northern Vietnamese male horror narrator (VOICE_LOCK_NARRATOR_OANTHAI) "
                    f"speaks the Vietnamese voice-over in a deep, bone-chilling Standard Northern Vietnamese baritone accent (giọng nam chuẩn miền Bắc trầm lạnh, gai góc kể chuyện ma đêm khuya, speed {clip['speed']}, strictly NO Southern/Saigon accent) while all on-screen characters keep their mouths closed."
                )
                cam_mouth = f"`{lens} {shot_type}` — {cam_plan}. Toàn bộ nhân vật trên hình khép miệng (`mouth closed 0.0–10.0s`), chỉ có giọng Nam Người Dẫn Chuyện chuẩn miền Bắc ngoài khung hình."
                diag_line = f"- **Lời dẫn chuyện (`VOICE_LOCK_NARRATOR_OANTHAI` | `0.8–9.2s`, `{clip['speed']}`, giọng nam chuẩn miền Bắc trầm lạnh, gai góc kể chuyện ma đêm khuya):** *\"{clip['dialogue']}\"*"
            else:
                eng_full = clip["eng_action"]
                sp = clip["speaker_tag"]
                v_lock = CHARACTER_SPECS[sp]["voice_lock"]
                cam_mouth = f"`{lens} {shot_type}` — {cam_plan}. `0.0–3.0s`: khép miệng; `3.0–7.0s`: chỉ duy nhất **{sp}** mở miệng nói khớp khẩu hình tiếng Việt chuẩn miền Bắc; `7.0–10.0s`: khép miệng phản ứng bằng ánh mắt."
                diag_line = f"- **Thoại nhân vật trực tiếp (`{v_lock}` | **{sp}** `3.0–7.0s`, `{clip['speed']}`, giọng chuẩn miền Bắc khớp khẩu hình):** *\"{clip['dialogue']}\"*"

            lines.extend([
                f"#### Shot {s_num:02d}.{c_num} ([`canh-{s_num:02d}/clip-{c_num}.md`](canh-{s_num:02d}/clip-{c_num}.md)) — `{shot_type}` ({lens}) | `{clip['timerange']}` | `[{clip['meta']}]`",
                f"- **Nhân vật khóa Reference:** {chars_str}",
                f"- **English Visual Choreography (0.0–10.0s):** {eng_full}",
                "- **Hành động chi tiết 3 nhịp nối tiếp (`0.0s → 3.0s → 7.0s → 10.0s`):**",
                f"  - *Beat 1 (`0.0–3.0s`):* {clip['beat1']}",
                f"  - *Beat 2 (`3.0–7.0s`):* {clip['beat2']}",
                f"  - *Beat 3 (`7.0–10.0s`):* {clip['beat3']}",
                f"- **Camera & Khẩu hình (0.0–10.0s):** {cam_mouth}",
                diag_line,
                f"- **Âm thanh kinh dị & tiếng động hiện trường (0.0–10.0s):** {clip['sound']}",
                "",
            ])

    lines.extend([
        "---",
        "",
        "## TỔNG KẾT TỶ LỆ THOẠI TRONG KỊCH BẢN (`84 CLIPS / 14 PHÚT`)",
        "- **Tổng số Clips:** `84 clips × 10 giây = 840 giây (14 phút)`",
        "- **Số Clips Người Dẫn Chuyện (`[VO - NGƯỜI DẪN CHUYỆN]`):** **`67 / 84 clips` (`79.8%` ~ `80%`)** — Toàn bộ 67 clips này nhân vật trên hình **khép miệng (`mouth remains closed`)**, giọng Nam Người Dẫn Chuyện chuẩn miền Bắc (`VOICE_LOCK_NARRATOR_OANTHAI`) trầm lạnh, gai góc kể chuyện ma đêm khuya.",
        "- **Số Clips Thoại Nhân Vật Bất Ngờ (`[THOẠI TRỰC TIẾP - LIP-SYNC]`):** **`17 / 84 clips` (`20.2%` ~ `20%`)** — Rải đều ở đúng 17 điểm cao trào/giật mình từ Cảnh 01 đến Cảnh 14 (`@Bach`: 6 câu, `@Ha`: 6 câu, `@ThayPhong`: 5 câu).",
        "",
    ])
    return "\n".join(lines)


def main():
    scenes = build_scenes_data()
    total_clips = sum(len(s["clips"]) for s in scenes)
    vo_clips = sum(1 for s in scenes for c in s["clips"] if c["is_vo"])
    lip_clips = total_clips - vo_clips
    print(f"Built {len(scenes)} scenes, {total_clips} clips ({vo_clips} VO = {vo_clips/total_clips*100:.1f}%, {lip_clips} Lip-Sync = {lip_clips/total_clips*100:.1f}%)")

    # 1. Write KICH_BAN_14_PHUT.md
    kb_md = build_kich_ban_markdown(scenes)
    with open(os.path.join(BASE_DIR, "KICH_BAN_14_PHUT.md"), "w", encoding="utf-8") as f:
        f.write(kb_md)

    # 2. Create canh-01 .. canh-14 directories, clip-1..6.md, and scene README.md
    for scene in scenes:
        s_num = scene["scene_num"]
        s_dir = os.path.join(BASE_DIR, f"canh-{s_num:02d}")
        os.makedirs(s_dir, exist_ok=True)
        spatial_lock, props_lock = SCENE_SPATIAL_LOCKS[s_num]

        rows = []
        for clip in scene["clips"]:
            c_num = clip["clip_num"]
            clip_md = build_clip_markdown(scene, clip)
            clip_path = os.path.join(s_dir, f"clip-{c_num}.md")
            with open(clip_path, "w", encoding="utf-8") as f:
                f.write(clip_md)

            shot_type, lens, _ = SHOT_TYPES[(c_num - 1) % 6]
            chars_str = ", ".join(clip["chars"])
            mode_label = "**[VO - Người Dẫn Chuyện]**" if clip["is_vo"] else f"**[THOẠI - {clip['speaker_tag']}]**"
            rows.append(
                f"| `clip-{c_num}.md` | `{shot_type}` ({lens}) | Omni 10s R2V ({len(clip['chars'])} refs) | {chars_str} | {clip['beat2']} | {mode_label} ({clip['speed']}): *\"{clip['dialogue']}\"* | {clip['sound']} |"
            )

        s_readme = f"""# Cảnh {s_num:02d}: {scene['title']} ({scene['time_span']})

- **Thời gian trong truyện:** `{scene['story_time']}`
- **Model & Chế độ Render:** `omni_flash` (Google Flow Omni — **10 giây/clip**, Ingredients Reference-to-Video, chuẩn **80% Người dẫn chuyện VO + 20% Thoại nhân vật bất ngờ**, giọng chuẩn miền Bắc)
- **Bối cảnh khóa cố định:** `{scene['loc_id']}` — {scene['loc_desc_vi']}

## Khóa Không Gian & Đạo Cụ
- **Spatial Lock:** {spatial_lock}
- **Props Lock:** {props_lock}

## Danh Sách 6 Clips (6 × 10s = 60s — Google Flow Omni 10s)

| File | Cỡ Cảnh & Ống Kính | Chế Độ Omni (10s) | Nhân Vật | Hành Động Kinh Dị Trọng Tâm | Thoại Chuẩn Miền Bắc (`80% VO / 20% Lip-Sync`) | Thiết Kế Âm Thanh Gai Góc (`0.0–10.0s`) |
|---|---|---|---|---|---|---|
""" + "\n".join(rows) + "\n"
        with open(os.path.join(s_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write(s_readme)

    # 3. Build FLOW_PROMPTS.md
    flow_md = """# Khóa Nhân Vật, Giọng Đọc, Bối Cảnh & Đạo Cụ — Oán Thai Đòi Mẹ: Búp Bê Đất Nung (Google Flow Omni 10s — 80% VO + 20% Lip-Sync)

## 1. Khóa Giọng Người Dẫn Chuyện (`VOICE_LOCK_NARRATOR_OANTHAI` — 80% Thời Lượng Phim)
```text
[VOICE_LOCK_NARRATOR_OANTHAI — Cố định giọng Nam Người Dẫn Chuyện chuẩn miền Bắc xuyên suốt 84 clips]: Fixed 40-year-old native Standard Northern Vietnamese male late-night horror storyteller voice, deep resonant chest baritone, measured atmospheric pacing (0.90x–1.00x), organic breath pauses, dark gravelly timbre, evoking classic Vietnamese supernatural folklore storytelling. Never sound like a commercial announcer or robotic TTS engine; never use Southern or Mekong Delta accent/slang.
```

## 2. Khóa 4 Nhân Vật Chính (`CHARACTER_SPECS`)
"""
    for tag, spec in CHARACTER_SPECS.items():
        flow_md += f"""
### {tag} — {spec['name']} ({spec['age']} tuổi)
- **Prompt tạo ảnh Reference trên Google Flow (`IMAGE_ASPECT_RATIO_LANDSCAPE`):**
```text
{spec['ref_prompt']}
```
- **Block khóa trong Clip Prompt (`CHARACTER_LOCK` & `VOICE_LOCK`):**
```text
{spec['block']}
```
"""

    flow_md += "\n## 3. Khóa Bối Cảnh Cố Định (`LOCATIONS`)\n"
    for loc_id, loc_desc in LOCATIONS.items():
        flow_md += f"\n### `{loc_id}`\n```text\n{loc_desc}\n```\n"

    flow_md += """
## 4. Danh Mục 84 Clips (14 Cảnh × 6 Clips × 10s = 14 Phút — Google Flow Omni 10s)

| Cảnh | Thời Lượng | Clip 1 (10s) | Clip 2 (10s) | Clip 3 (10s) | Clip 4 (10s) | Clip 5 (10s) | Clip 6 (10s) |
|---|---|---|---|---|---|---|---|
"""
    for s in scenes:
        sn = s["scene_num"]
        flow_md += (
            f"| [Cảnh {sn:02d}](canh-{sn:02d}/README.md) | `6 × 10s (60s)` | "
            + " | ".join(f"[Clip {c}](canh-{sn:02d}/clip-{c}.md)" for c in range(1, 7))
            + " |\n"
        )

    with open(os.path.join(BASE_DIR, "FLOW_PROMPTS.md"), "w", encoding="utf-8") as f:
        f.write(flow_md)

    print("Successfully built KICH_BAN_14_PHUT.md, all 84 clips, 14 scene READMEs, and FLOW_PROMPTS.md!")


if __name__ == "__main__":
    main()
