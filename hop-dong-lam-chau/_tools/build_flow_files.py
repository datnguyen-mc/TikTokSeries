#!/usr/bin/env python3
"""Sinh NHAN_VAT_FLOW.md, trailer/TRAILER.md và trailer/prompts/TR-XX.txt cho "Hợp Đồng Làm Cháu".
Chạy từ thư mục gốc repo: python3 hop-dong-lam-chau/_tools/build_flow_files.py
Sửa dữ liệu nhân vật, bộ đồ, bối cảnh, shot ngay trong file này rồi chạy lại."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- nhân vật gốc
PEOPLE = {
    "OngThinh": dict(
        vn="Ông Thịnh", role="the grandfather",
        face="a dignified 76-year-old Vietnamese grandfather from the Northern countryside, lean and slightly stooped, "
             "weathered sun-browned skin with deep laugh lines, short thinning white hair, a neat short white moustache, "
             "bushy white eyebrows over sharp watchful dark eyes, strong carpenter's hands with knotted knuckles",
        voice="man of 76, low gravelly baritone, slow and clipped, long pauses between phrases, dry and stubborn"),
    "BaMan": dict(
        vn="Bà Mận", role="the grandmother",
        face="a warm, anxious 72-year-old Vietnamese grandmother from the Northern countryside, small and plump, "
             "round kind face with soft wrinkles, grey-black hair pulled into a low bun, gentle worried eyes, a quick shy smile",
        voice="woman of 72, soft warm alto, a little breathless, speaking fast and low when nervous"),
    "Dat": dict(
        vn="Đạt", role="the hired fake grandson",
        face="an affable 25-year-old Vietnamese man, slim and of medium height, friendly expressive face with lively eyebrows, "
             "bright mischievous eyes, a wide easy grin, short tousled black hair, a smooth clean-shaven chin with no scar",
        voice="man of 25, bright light tenor, quick and over-eager, words tumbling out"),
    "Minh": dict(
        vn="Minh", role="the real grandson",
        face="a handsome, reserved 28-year-old Vietnamese man, tall and broad-shouldered, serious face with a strong jaw, "
             "tired guarded eyes, short neat black hair, light stubble, a small thin pale scar on the left side of his chin",
        voice="man of 28, deep quiet baritone, flat and restrained, few words"),
    "BaThoa": dict(
        vn="Bà Thoa", role="the nosy neighbour",
        face="a lively, nosy 70-year-old Vietnamese woman from the Northern countryside, short and energetic, round face with "
             "bright rouge, permed short curly black hair, sharp curious eyes, gold hoop earrings",
        voice="woman of 70, high sharp voice, loud and chatty like a TV host"),
    "BoMinh": dict(
        vn="Bố Minh", role="Minh's late father, seen only as an altar portrait",
        face="a kind 45-year-old Vietnamese man who clearly resembles Minh, strong jaw, gentle smile, short black hair",
        voice=""),
}

# ---------------------------------------------------------------- bộ đồ = nhân vật trên Flow
# (mã, người, tên trên Flow, cảnh dùng, trang phục tiếng Anh, ghi chú tiếng Việt)
LOOKS = [
    ("OT1", "OngThinh", "Ông Thịnh · Áo nâu ở nhà", "02, 03, 04, 06",
     "a faded brown cotton traditional shirt with cloth buttons, dark trousers rolled at the ankle, rubber sandals, a carpenter's pencil tucked behind one ear",
     "Đồ ở nhà, sơn ghế, gói bánh"),
    ("OT2", "OngThinh", "Ông Thịnh · Áo bông xanh", "05, 09, 11, 12, 14, 15, 16, 17",
     "a navy quilted cotton jacket over a grey shirt, dark trousers, a brown felt beret, holding a polished wooden walking stick",
     "Ra đường, chợ hoa, tảo mộ, sáng 29"),
    ("OT3", "OngThinh", "Ông Thịnh · Áo len đêm", "07, 18",
     "a moss-green knitted cardigan buttoned over a brown shirt, a grey wool scarf, a dark wool beanie",
     "Đêm canh bánh, nằm giường"),
    ("OT4", "OngThinh", "Ông Thịnh · Áo dài Tết", "20",
     "a traditional dark-blue men's silk áo dài tunic over loose white trousers, a black wrapped khăn xếp turban",
     "Giao thừa, mùng 1"),
    ("OT5", "OngThinh", "Ông Thịnh · 56 tuổi hồi tưởng", "18 (hồi tưởng)",
     "twenty years younger: about 56, hair still mostly black with some grey, a white cotton singlet under an open khaki shirt, trousers rolled to the knee, bare feet",
     "Chớp lui: cõng thằng bé ngã cây bưởi. Mặt trẻ hơn 20 tuổi"),
    ("BM1", "BaMan", "Bà Mận · Áo bông đi đường", "01",
     "a maroon quilted jacket, a dark-brown wool headscarf tied under the chin, black trousers, a cloth shoulder bag clutched tight",
     "Bến xe"),
    ("BM2", "BaMan", "Bà Mận · Áo cánh ở nhà", "02–04, 06, 10, 12, 14–17",
     "a light-brown traditional blouse (áo cánh) with cloth buttons under a beige knitted cardigan, black satin trousers, a faded floral apron",
     "Đồ ở nhà"),
    ("BM3", "BaMan", "Bà Mận · Áo dài nhung Tết", "20",
     "a deep-red velvet áo dài over black trousers, a small jade bracelet, hair neatly pinned",
     "Giao thừa, mùng 1"),
    ("DA1", "Dat", "Đạt · Bomber ra mắt", "01, 02, 03",
     "a trying-too-hard outfit: a shiny olive bomber jacket over a crisp white shirt buttoned to the top, brand-new stiff blue jeans, bright white sneakers, a big black backpack",
     "Ngày đầu 'diện' về ra mắt"),
    ("DA2", "Dat", "Đạt · Áo len mượn", "04, 05, 06, 07, 09",
     "an oversized old brown hand-knitted sweater that is far too big for him, sleeves rolled, grey track pants, rubber sandals",
     "Áo len cũ bà đưa mặc cho ấm"),
    ("DA3", "Dat", "Đạt · Áo phao đỏ", "10–19",
     "a red puffer jacket over a grey hoodie, blue jeans, white sneakers",
     "Từ tối 28 đến bến xe tối 30"),
    ("DA4", "Dat", "Đạt · Áo dạ mùng 1", "20",
     "a camel wool coat over a white shirt, dark trousers, polished brown shoes",
     "Sáng mùng 1, chụp ảnh gia đình"),
    ("MI1", "Minh", "Minh · Áo đầu bếp", "08",
     "a white double-breasted chef's jacket, a black waist apron, black trousers, a black chef's skull cap",
     "Bếp nhà hàng ca đêm"),
    ("MI2", "Minh", "Minh · Áo dạ đen", "10, 11–17",
     "a long black wool coat over a charcoal turtleneck, dark jeans, black leather boots, a black backpack",
     "Về làng sáng 29"),
    ("MI3", "Minh", "Minh · Áo len của bố", "18, 19, 20",
     "an old cream cable-knit wool sweater slightly out of fashion (his late father's), dark jeans, black boots",
     "Bà đưa áo len của bố; chiều 30 đến mùng 1"),
    ("MI0", "Minh", "Minh · 8 tuổi hồi tưởng", "18 (hồi tưởng)",
     "as an 8-year-old Vietnamese village boy with the same eyes and jaw, a shaved-short haircut, a faded blue T-shirt and shorts, bare feet, a small white gauze patch on the left side of his chin",
     "Chớp lui; chỉ băng gạc, không máu"),
    ("BT1", "BaThoa", "Bà Thoa · Áo nhung hoa", "03, 07, 11, 13, 14, 15",
     "a loud magenta floral-print velvet jacket, a patterned silk scarf, black trousers, a smartphone always held up on a short selfie stick",
     "Luôn cầm điện thoại livestream"),
    ("BT2", "BaThoa", "Bà Thoa · Áo dài gấm Tết", "19, 20",
     "a golden brocade áo dài over black trousers, a pearl necklace, a small red handbag",
     "Tối 30 và mùng 1; ngồi sau xe máy thì đội thêm mũ bảo hiểm"),
    ("BOM", "BoMinh", "Bố Minh · Di ảnh", "07, 09, 16, 20",
     "a formal head-and-shoulders studio portrait in a white shirt and dark jacket, framed for a family altar",
     "Ảnh thờ, đạo cụ"),
]
LOOK = {c: dict(person=p, flow=f, scenes=s, outfit=o, note=n) for c, p, f, s, o, n in LOOKS}

REF_TAIL = ("; plain light-grey studio background, soft even daylight, natural skin texture with pores and fine wrinkles, "
            "realistic proportions, 8K. Not resembling any real person.")


def ref_prompt(code):
    lk = LOOK[code]
    p = PEOPLE[lk["person"]]
    if code == "BOM":
        return f"Photorealistic framed altar portrait photograph of {p['face']}, {lk['outfit']}; neutral grey backdrop, soft studio light, natural skin texture, 8K. Not resembling any real person."
    if code in ("OT5", "MI0"):
        return f"Full-body photorealistic character reference of the same person as the attached image — {p['face']} — shown {lk['outfit']}{REF_TAIL}"
    return f"Full-body photorealistic character reference of {p['face']}, wearing {lk['outfit']}{REF_TAIL}"


def edit_prompt(code):
    lk = LOOK[code]
    if code in ("OT5", "MI0"):
        return f"Same person, same face shape and features, shown {lk['outfit']}. Full body, plain light-grey studio background."
    return f"Same person, same face and hair, exactly. Now wearing {lk['outfit']}. Full body, plain light-grey studio background."


# Bộ đồ gốc của mỗi người (tạo trước, dùng làm ảnh khóa mặt cho các bộ còn lại)
BASE = {"OngThinh": "OT1", "BaMan": "BM2", "Dat": "DA1", "Minh": "MI2", "BaThoa": "BT1", "BoMinh": "BOM"}

# ---------------------------------------------------------------- bối cảnh trailer
LOOKBLOCK = ("Cinematic live-action film shot on ARRI Alexa 35 with vintage spherical lenses, 24 fps, 16:9; real actors with "
             "natural skin texture, pores and micro-expressions, believable understated performances, motivated practical "
             "lighting, soft contrast, warm amber-and-jade grade, gentle halation, subtle 35mm film grain, shallow depth of "
             "field. A premium Vietnamese theatrical family comedy-drama set in a Northern Vietnamese village in the last days "
             "before Lunar New Year, never CGI, never a video game, never an advertisement.")

PLACES = {
    "BENXE": "A small rural district bus station in Northern Vietnam a few days before Lunar New Year: faded coaches, red "
             "lanterns strung under a tin awning, travellers carrying peach-blossom branches and gift boxes; hazy grey "
             "winter morning light.",
    "SAN": "The brick-paved courtyard of an old three-room tile-roofed village house in the Northern Vietnamese countryside: "
           "a pomelo tree in the corner, a betel-vine trellis, potted kumquat trees, a low brick wall to the neighbour's "
           "garden; pale golden winter sunlight.",
    "BEPLUA": "The same village courtyard at night: a big blackened pot of square sticky-rice cakes boiling over a wood "
              "fire, sparks drifting up, two low wooden stools; warm orange firelight against a deep blue night.",
    "BEPNH": "A busy professional restaurant kitchen in a big city late at night: stainless steel counters, blue-white "
             "fluorescent light, steam and flashes of wok flame; cold steely light.",
    "DAULANG": "A village entrance road at night: a huge old banyan tree, one weak yellow streetlight, rice fields "
               "fading into darkness, a coach's tail lights pulling away.",
    "CONG": "An old arched brick gate of the village house hung with red paper lanterns, opening onto a narrow "
            "brick-paved lane; the morning of the last day before Lunar New Year, soft hazy sunlight.",
    "HIEN": "The front veranda of the old village house: tall wooden doors folded open, red festive scrolls with no "
            "readable writing, a tray of kumquats; soft hazy morning sunlight.",
}

SOUND = {
    "BENXE": "coach engines idling, a conductor calling out far away, rustling plastic bags",
    "SAN": "chickens clucking softly, a broom on bricks next door, distant village loudspeaker hum",
    "BEPLUA": "crackling wood fire, the pot bubbling, crickets",
    "BEPNH": "clattering pans, a roaring wok burner, an extractor fan",
    "DAULANG": "a coach engine fading, cold wind in the banyan leaves, a distant dog",
    "CONG": "rustling paper lanterns, a rooster far off, a motorbike passing in the lane",
    "HIEN": "wind chimes, birds in the pomelo tree, a kettle whistling inside",
}

# ---------------------------------------------------------------- shot trailer
# (mã, tên ngắn trên Flow, giây, bối cảnh, [mã bộ đồ], máy quay, hành động, thoại: (mã người nói, câu, bắt đầu, kết thúc) hoặc None)
SHOTS = [
    ("TR-01", "Bà dúi phong bì", 5, "BENXE", ["BM1", "DA1"],
     "50mm medium two-shot, slow push-in",
     "BaMan glances around nervously, then presses a thick red envelope into Dat's hands and folds his fingers over it; Dat blinks, surprised",
     ("BM1", "Năm ngày thôi. Cháu làm cháu nội tôi, đừng để ông biết.", 0.3, 4.0)),
    ("TR-02", "Ông ơi cháu về rồi", 3, "CONG", ["DA1"],
     "35mm medium-wide shot from inside the courtyard looking at the gate, locked off",
     "Dat bursts through the brick gate with his arms flung wide and a huge over-acted grin, backpack bouncing",
     ("DA1", "Ông ơi! Cháu về rồi!", 0.3, 2.0)),
    ("TR-03", "Mười năm lùn đi", 4, "SAN", ["OT1"],
     "85mm close-up, locked off",
     "OngThinh sits on a low stool painting a tiny child-sized wooden chair; he stops the brush, slowly looks up and squints, unimpressed",
     ("OT1", "Mười năm… mà mày lùn đi à?", 1.0, 3.6)),
    ("TR-04", "Dị ứng lạc", 3, "SAN", ["DA1"],
     "50mm medium shot, slight handheld",
     "Dat is happily chewing a piece of peanut brittle, suddenly freezes, spits it into his palm and scratches his neck frantically with wide panicked eyes",
     ("DA1", "Ngứa! Ngứa quá!", 1.0, 2.6)),
    ("TR-05", "Bà Thoa qua rào", 4, "SAN", ["BT1"],
     "50mm medium shot over the low brick wall, slow push-in",
     "BaThoa leans over the low brick wall holding her phone up on a selfie stick, eyes narrowing with delighted suspicion",
     ("BT1", "Lạ nhỉ! Thằng Minh hồi bé dị ứng lạc cơ mà?", 0.3, 3.4)),
    ("TR-06", "Gói bánh chưng", 4, "SAN", ["OT1", "DA2"],
     "35mm two-shot from the side, gentle dolly",
     "OngThinh and Dat wrap square sticky-rice cakes in green dong leaves inside wooden moulds; Ong's cake is perfectly square, Dat's is lumpy and lopsided; Ong glances at it and his shoulders shake with a silent laugh",
     None),
    ("TR-07", "Ông giận ông", 5, "BEPLUA", ["OT3", "DA2"],
     "50mm two-shot across the fire, very slow push-in",
     "OngThinh stares into the fire while speaking; beside him Dat turns to look at him and his eyes fill with tears",
     ("OT3", "Ông không giận cháu. Ông giận ông.", 0.6, 3.6)),
    ("TR-08", "Thằng đấy là ai", 4, "BEPNH", ["MI1"],
     "85mm close-up, locked off",
     "On a break by the back door, Minh stares down at the glow of his phone screen; his jaw tightens and his eyes go cold",
     ("MI1", "Thằng đấy… là ai?", 1.2, 3.2)),
    ("TR-09", "Xe khách đêm", 3, "DAULANG", [],
     "low wide shot at road level, locked off",
     "A coach pulls away into the dark; a man's black leather boots step down onto the road and a backpack strap swings into frame; his face is never seen",
     None),
    ("TR-10", "Hai thằng Minh", 4, "CONG", ["MI2", "DA3"],
     "35mm wide shot through the gate, slow push-in",
     "Dat stands on a short bamboo ladder hanging a red lantern; the gate creaks open and Minh stands in it; Dat freezes with the lantern in mid-air; they stare at each other",
     None),
    ("TR-11", "Đứa nào cháu thật", 3, "SAN", ["BT1"],
     "50mm medium close-up, quick push-in",
     "BaThoa pops up over the brick wall, phone raised high on the selfie stick, mouth dropping open",
     ("BT1", "Thế đứa nào là cháu thật?", 0.3, 2.3)),
    ("TR-12", "Minh vào ăn sáng", 4, "HIEN", ["OT2"],
     "50mm medium shot, locked off",
     "OngThinh steps out onto the veranda leaning on his walking stick, looks from one young man to the other off-screen, then turns warmly toward camera-left",
     ("OT2", "Minh, vào ăn sáng con.", 1.4, 3.4)),
    ("TR-13", "Minh chết lặng", 3, "CONG", ["MI2"],
     "85mm close-up, locked off",
     "Minh stands frozen in the gateway, stunned and silent, his breath misting in the cold air",
     None),
]

AVOID = ("On-screen text, subtitles, captions, logos, watermarks, readable writing on paper, screens, envelopes or signs; "
         "any cut or second camera angle; extra people in focus; distorted hands or fused fingers; face, hair or costume "
         "changes; plastic or waxy skin; flashing or cutting to an attached reference portrait or a plain grey studio "
         "backdrop; repeated, echoed or stuttered words; an off-screen narrator; background music; Southern or Central "
         "Vietnamese accents.")


def shot_prompt(s):
    code, name, dur, place, looks, cam, action, line = s
    out = [f"A single continuous {dur}-second shot, 16:9, one camera angle, no cuts.", "",
           f"[LOOK] {LOOKBLOCK}", "", f"[PLACE] {PLACES[place]}", ""]
    if looks:
        out.append("[CHARACTERS] Use the attached character image for each person: same face, same hair, same outfit, exactly.")
        for c in looks:
            lk = LOOK[c]
            p = PEOPLE[lk["person"]]
            out.append(f"- @{lk['person']} = {p['vn']}, {p['role']} ({p['face'].split(',')[0]}); wears {lk['outfit']}. Attached image: \"{lk['flow']}\".")
        out.append("Nobody else is in focus.")
    else:
        out.append("[CHARACTERS] No named characters; any people in frame are distant, blurred, seen only from behind or below the waist.")
    out += ["", f"[CAMERA] {cam}.", "", f"[ACTION] {action}.", ""]
    if line:
        sp, text, t0, t1 = line
        person = LOOK[sp]["person"]
        p = PEOPLE[person]
        out.append(f"[DIALOGUE] In Vietnamese with exact lip-sync, spoken on camera by @{person} ({p['voice']}), "
                   f"said exactly once from {t0:.1f}s to {t1:.1f}s: {text}")
        out.append(f"Only @{person} moves the lips. After the last word nobody speaks again until {dur:.1f}s. "
                   "Standard Northern Vietnamese accent; never read these directions aloud.")
    else:
        out.append("[DIALOGUE] None. Every mouth stays closed; no voices at all.")
    out += ["", f"[SOUND] {SOUND[place]}. No music.", "", f"[AVOID] {AVOID}", ""]
    return "\n".join(out)


def write(path, text):
    path = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    # NHAN_VAT_FLOW.md
    L = ["# Hợp Đồng Làm Cháu — Nhân vật theo bộ đồ trên Flow", "",
         "*Sinh bởi `_tools/build_flow_files.py`. Sửa trong script rồi chạy lại, không sửa tay file này.*", "",
         "Mỗi bộ đồ là **một nhân vật riêng trên Flow**, đặt đúng tên ở cột *Tên trên Flow*. "
         "Thứ tự tạo: (1) tạo **bộ đồ gốc** của từng người bằng prompt đầy đủ (đánh dấu ★); "
         "(2) các bộ còn lại: đính ảnh bộ gốc làm tham chiếu và dùng *Prompt sửa* để giữ nguyên khuôn mặt. "
         "Riêng OT5 và MI0 (hồi tưởng) đính ảnh gốc rồi dùng prompt đầy đủ.", "",
         "## Khóa mặt và giọng", "", "| Tag | Nhân vật | Khuôn mặt | Giọng |", "|---|---|---|---|"]
    for k, p in PEOPLE.items():
        L.append(f"| `@{k}` | {p['vn']} | {p['face']} | {p['voice'] or '—'} |")
    L += ["", f"## {len(LOOKS)} nhân vật theo bộ đồ", "",
          "| Mã | Tên trên Flow | Cảnh dùng | Ghi chú | Prompt sửa (từ ảnh gốc) | Prompt đầy đủ |", "|---|---|---|---|---|---|"]
    for c, *_ in LOOKS:
        lk = LOOK[c]
        star = " ★" if BASE.get(lk["person"]) == c else ""
        L.append(f"| {c}{star} | {lk['flow']} | {lk['scenes']} | {lk['note']} | "
                 f"{'— (tạo bằng prompt đầy đủ)' if star else edit_prompt(c)} | {ref_prompt(c)} |")
    L += ["", "## Cảnh nào dùng bộ nào", "",
          "| Cảnh | Bộ đồ |", "|---|---|"]
    by_scene = {}
    for c, *_ in LOOKS:
        for part in LOOK[c]["scenes"].replace("–", "-").replace(" (hồi tưởng)", "").split(","):
            part = part.strip()
            rng = [part] if "-" not in part else [f"{i:02d}" for i in range(int(part.split('-')[0]), int(part.split('-')[1]) + 1)]
            for sc in rng:
                by_scene.setdefault(f"{int(sc):02d}", []).append(c)
    for sc in sorted(by_scene):
        L.append(f"| {sc} | {', '.join(by_scene[sc])} |")
    write("NHAN_VAT_FLOW.md", "\n".join(L) + "\n")

    # trailer
    T = ["# Trailer — Hợp Đồng Làm Cháu (~60 giây, 16:9)", "",
         "*Sinh bởi `_tools/build_flow_files.py`.* Trailer chỉ dùng nửa đầu phim, **không lộ cú lật** (ông biết từ đầu). "
         "Mỗi shot là một lần tạo trên Flow: **Video → Gemini Omni → Ingredients**, đính đúng các nhân vật ở cột *Đính*, "
         "dán nguyên file `prompts/TR-XX.txt`, đặt tên clip trên Flow là `TR-XX · <tên>` để `make_trailer.py` nhận ra. "
         "TR-09 không có nhân vật: dùng Text-to-Video.", "",
         "| Shot | Tên trên Flow | Giây | Đính | Thoại |", "|---|---|---|---|---|"]
    for s in SHOTS:
        code, name, dur, place, looks, cam, action, line = s
        T.append(f"| {code} | {code} · {name} | {dur} | {', '.join(LOOK[c]['flow'] for c in looks) or '— (Text-to-Video)'} | "
                 f"{(PEOPLE[LOOK[line[0]]['person']]['vn'] + ': ' + line[1]) if line else '—'} |")
        write(f"trailer/prompts/{code}.txt", shot_prompt(s))
    T += ["", "## Dựng", "",
          "Tải các clip về `trailer/clips/` rồi chạy `python3 hop-dong-lam-chau/trailer/make_trailer.py hop-dong-lam-chau/trailer/clips`. "
          "Script chèn thẻ chữ (26 THÁNG CHẠP · MỘT ĐỨA CHÁU THUÊ… · …MỘT ĐỨA CHÁU THẬT · tựa phim · RA MẮT TRƯỚC TẾT) giữa các shot. "
          "Nhạc nền thêm khi hậu kỳ."]
    write("trailer/TRAILER.md", "\n".join(T) + "\n")
    print(f"Xong: {len(LOOKS)} bộ đồ, {len(SHOTS)} shot trailer.")


if __name__ == "__main__":
    main()
