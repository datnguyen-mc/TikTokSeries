#!/usr/bin/env python3
"""Dữ liệu gốc phim "Ai Là Vợ Bệnh Nhân?": nhân vật, bộ đồ (= nhân vật trên Flow), bối cảnh, âm thanh,
khối prompt chung và hàm dựng prompt cho từng shot. Bảng shot nằm ở canh_a.py, canh_b.py, canh_c.py.
Sửa dữ liệu ở đây rồi chạy: python3 ai-la-vo-benh-nhan/_tools/build.py"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEN_PHIM = "Ai Là Vợ Bệnh Nhân?"

# ---------------------------------------------------------------- nhân vật gốc
# rate = số âm tiết mỗi giây khi tính thời lượng thoại
PEOPLE = {
    "Hanh": dict(
        vn="Hạnh", role="the legal wife, a chief accountant", short="a composed 38-year-old Vietnamese woman",
        face="a composed, elegant 38-year-old Vietnamese woman, slim, oval face with high cheekbones, calm intelligent "
             "almond eyes, straight black hair pulled into a neat low bun, minimal makeup, a small mole under the left eye",
        voice="woman of 38, low calm alto, dry and precise, unhurried, never raises her voice", rate=3.8),
    "Mai": dict(
        vn="Mai", role="the second 'wife' who had a village wedding", short="a petite 29-year-old Vietnamese woman",
        face="a warm, pretty 29-year-old Vietnamese woman, petite with a round girlish face, big expressive eyes that tear "
             "up easily, full cheeks, long dark-brown hair twisted up in a big plastic claw clip with loose strands",
        voice="woman of 29, bright warm soprano, fast and emotional, voice cracking when upset", rate=4.3),
    "Ly": dict(
        vn="Ly", role="the young girlfriend, a bank credit officer", short="a tall slender 23-year-old Vietnamese woman",
        face="a strikingly pretty 23-year-old Vietnamese woman, tall and slender, heart-shaped face, large doe eyes, long "
             "glossy black hair in soft waves, light glam makeup",
        voice="woman of 23, soft sweet light voice, polite and a little breathless", rate=4.3),
    "Dung": dict(
        vn="Dũng", role="the husband", short="a smooth, handsome 40-year-old Vietnamese man",
        face="a handsome, smooth 40-year-old Vietnamese man, medium build, charming boyish smile with dimples, neatly "
             "side-parted black hair with a touch of grey at the temples, clean-shaven, soft persuasive eyes",
        voice="man of 40, smooth warm baritone, persuasive and a little oily, hoarse when weak", rate=4.3),
    "Thom": dict(
        vn="Chị Thơm", role="the night-shift head nurse", short="a sturdy 48-year-old Vietnamese nurse",
        face="a no-nonsense 48-year-old Vietnamese head nurse, sturdy, square tired face, deadpan heavy-lidded eyes, short "
             "black bob tucked behind the ears, reading glasses hanging on a cord",
        voice="woman of 48, flat deadpan mezzo, brisk and tired, no-nonsense", rate=4.3),
    "BaVuong": dict(
        vn="Bà Vượng", role="the husband's mother", short="a small wiry 68-year-old Vietnamese village woman",
        face="a sharp-tongued 68-year-old Vietnamese village woman, small and wiry, sun-browned lined face, thin lips, "
             "quick darting eyes, grey hair in a tight bun",
        voice="woman of 68, raspy strong village voice, quick and sharp", rate=3.4),
    "OngLoc": dict(
        vn="Ông Lộc", role="an old man waiting on the next bench", short="a thin, twinkly 74-year-old Vietnamese grandfather",
        face="a gentle, twinkly 74-year-old Vietnamese grandfather, thin, kind wrinkled face, wispy white hair, a small "
             "white goatee, amused crinkled eyes",
        voice="man of 74, gentle slow gravelly voice, amused", rate=3.4),
}

# ---------------------------------------------------------------- bộ đồ = nhân vật trên Flow
# (mã, người, tên trên Flow, trang phục tiếng Anh, ghi chú tiếng Việt)
LOOKS = [
    ("HA1", "Hanh", "Hạnh · Vest xám",
     "a tailored charcoal-grey blazer over an ivory silk blouse, black cigarette trousers, low black heels, a structured "
     "tan leather tote bag, a plain gold wedding band",
     "Đồ công sở, từ văn phòng chạy thẳng đến viện"),
    ("HA2", "Hanh", "Hạnh · Sơ mi ngà",
     "an ivory silk blouse with the sleeves rolled to the elbow and no blazer, black cigarette trousers, low black heels, "
     "a structured tan leather tote bag, a plain gold wedding band",
     "Sau khi khoác vest cho Mai (từ cuối cảnh 10)"),
    ("HA3", "Hanh", "Hạnh · Cô dâu áo dài đỏ",
     "twelve years younger, about 26: a red silk bridal áo dài with gold embroidery over white trousers, hair in an elegant "
     "bridal updo with a small red headpiece, soft bridal makeup",
     "Hồi tưởng đám cưới 12 năm trước"),
    ("HA4", "Hanh", "Hạnh · Ở nhà",
     "a soft beige knitted cardigan over a white T-shirt, grey lounge trousers, a plain apron, hair in a low bun",
     "Hồi tưởng bữa cơm nhà"),
    ("MA1", "Mai", "Mai · Đồ ngủ hồng",
     "pale-pink floral cotton pyjamas with a mustard-yellow knitted cardigan thrown on top, plastic slippers, a motorbike "
     "helmet hooked on one arm, a plain gold wedding band",
     "Chạy đến viện giữa đêm"),
    ("MA2", "Mai", "Mai · Khoác vest xám",
     "the same pale-pink floral cotton pyjamas with an oversized charcoal-grey tailored blazer draped over her shoulders, "
     "plastic slippers, a plain gold wedding band",
     "Mặc áo vest của Hạnh (từ cuối cảnh 10)"),
    ("MA3", "Mai", "Mai · Cô dâu váy trắng",
     "four years younger: a simple white lace wedding dress with a short veil, a small bouquet, light bridal makeup",
     "Hồi tưởng đám cưới quê 4 năm trước"),
    ("MA4", "Mai", "Mai · Ở nhà",
     "a lilac home T-shirt and floral lounge trousers, hair in a claw clip",
     "Hồi tưởng bữa cơm phòng trọ"),
    ("LY1", "Ly", "Ly · Váy xanh lam",
     "a sapphire-blue satin slip evening dress, sapphire-blue high heels, a small silver clutch, delicate silver earrings",
     "Đi ăn sinh nhật rồi chạy đến viện"),
    ("DU1", "Dung", "Dũng · Áo bệnh nhân",
     "a pale-blue hospital patient gown, messy hair, his lower right leg in a clean white plaster cast",
     "Trên giường bệnh"),
    ("DU2", "Dung", "Dũng · Sơ mi trắng",
     "a crisp white dress shirt with the sleeves rolled once, navy suit trousers, a brown leather belt, a slim leather briefcase",
     "Hồi tưởng: 'giám đốc dự án'"),
    ("DU3", "Dung", "Dũng · Vest xám chú rể",
     "a light-grey three-piece wedding suit with a red rose boutonniere, a white shirt and a burgundy tie",
     "Hồi tưởng: cùng một bộ vest cho cả hai đám cưới"),
    ("TH1", "Thom", "Chị Thơm · Điều dưỡng",
     "a white nurse's tunic with dark-blue trim and matching trousers, a dark-blue cardigan, white clogs, a clipboard under "
     "one arm, reading glasses on a cord",
     "Ca đêm"),
    ("BV1", "BaVuong", "Bà Vượng · Áo bông nâu",
     "a brown quilted cotton jacket, a dark velvet headscarf, black trousers, cloth shoes, carrying a stainless-steel tiffin "
     "food carrier",
     "Lên viện bằng chuyến xe đầu tiên"),
    ("BV2", "BaVuong", "Bà Vượng · Áo dài nhung",
     "four years younger: a maroon velvet áo dài over black trousers, a string of pearls, hair neatly pinned",
     "Hồi tưởng: trao vàng ở đám cưới quê"),
    ("OL1", "OngLoc", "Ông Lộc · Gi-lê len",
     "a grey knitted wool vest over a checked shirt, dark trousers, a brown flat cap, a thermos flask and a bag of mandarins "
     "beside him",
     "Ngồi ghế bên cả đêm"),
]
LOOK = {c: dict(person=p, flow=f, outfit=o, note=n) for c, p, f, o, n in LOOKS}
BASE = {"Hanh": "HA1", "Mai": "MA1", "Ly": "LY1", "Dung": "DU2", "Thom": "TH1", "BaVuong": "BV1", "OngLoc": "OL1"}
# mô tả ngắn riêng cho bản hồi tưởng
SHORT_LOOK = {"HA3": "the same woman twelve years younger, about 26", "MA3": "the same woman four years younger, about 25",
              "BV2": "the same woman four years younger"}

# ---------------------------------------------------------------- bối cảnh
_GHE = ("The waiting area outside an operating theatre in a Vietnamese city hospital {when}: two rows of blue plastic bench "
        "seats facing wide double doors with a lamp above them, a plain round wall clock with tick marks only, a humming "
        "drinks vending machine in the corner, {light}.")
PLACES = {
    "GHE": _GHE.format(when="late at night", light="the lamp above the doors glowing red, pale fluorescent light, a rain-streaked window"),
    "GHE_SANG": _GHE.format(when="in the early morning", light="the lamp above the doors switched off, golden sunlight slanting through the window across the blue seats"),
    "VP_DEM": "A small accounting office late at night: rows of dark empty desks, one desk lit by a warm lamp, tall stacks of "
              "paper invoices and binders with no readable writing, a desktop calculator, rain streaking the window, city lights beyond.",
    "NHA_MAI_DEM": "A small rented one-room flat at night: a double bed beside a child's cot holding a small blanket-covered bundle "
                   "(the child is never visible), plastic toys on the floor, a night-light glowing soft pink.",
    "QUAY": "A hospital nurses' station at night: a long white counter, stacked patient folders, a desk lamp, pale blue-green "
            "fluorescent light, a quiet corridor behind.",
    "DUONGMUA": "A rainy city junction at night in front of a hospital gate: wet asphalt reflecting red and amber lights, heavy rain, no people.",
    "SANH_MUA": "The covered entrance porch of a city hospital at night in heavy rain: sliding glass doors, wet tiles, a glowing "
                "red-cross lamp with no lettering, rain pouring off the canopy.",
    "HL": "A long hospital corridor at night: glossy pale-green floor reflecting fluorescent tubes, closed doors, an empty gurney, "
          "a rain-streaked window at the far end.",
    "HL_SANG": "A long hospital corridor in the early morning: golden sunlight streaming through the far window, glossy pale-green floor, long shadows.",
    "CUASO": "A quiet end of a hospital corridor at night beside a tall rain-streaked window, city lights blurred beyond, a single wall lamp.",
    "MAYBAN": "A dim alcove off a hospital corridor at night with a single glowing drinks vending machine, its cold light spilling "
              "onto the floor, a rain-streaked window.",
    "CANTIN": "An almost empty hospital canteen in the small hours: stainless-steel tables, plastic stools, a big steaming stock pot "
              "at the serving counter, one table under a warm hanging lamp.",
    "BANCONG": "An open-air connecting walkway on the third floor of a hospital at night: a metal railing, rain falling just beyond "
               "the roof edge, blurred city lights and wet rooftops, a single warm wall lamp.",
    "PHONGBENH": "A hospital recovery room at dawn: three beds separated by pale-green privacy curtains, an over-bed table, a drip "
                 "stand, soft grey-pink dawn light through window blinds.",
    "PHONGBENH_CUA": "The corridor just outside a hospital recovery room at dawn: a door with a frosted-glass panel, a hand-sanitiser "
                     "dispenser on the wall, first grey daylight.",
    "CONG_SANG": "The gate of a city hospital at sunrise after a night of rain: the wet street shining gold, motorbikes passing, a "
                 "steaming street noodle stall under a tarp across the road.",
    "PHO": "A street-side noodle stall at sunrise: low plastic tables and stools on the wet pavement, a big steaming pot, jars of "
           "chilli and lime wedges, warm golden light.",
    "NHA_HANH": "A tidy middle-class apartment dining room in the evening: a wooden table set with a home-cooked family meal, a warm "
                "pendant light, a glass sliding door to a small balcony.",
    "NHA_HANH_BC": "A small apartment balcony at night seen through a glass sliding door from the dining room: potted plants, a "
                   "drying rack, city lights beyond.",
    "NHA_MAI": "A small rented flat in the evening: a low folding table with a modest home-cooked meal for two, plastic toys in a "
               "corner, a warm bare bulb.",
    "CUOI_QUE": "A festive countryside wedding tent in daytime: pink and white drapes, round tables, a small stage with flowers and "
                "balloons and no lettering, villagers clapping in soft focus, bright soft daylight.",
    "CUOI_12": "An old-fashioned hotel wedding hall twelve years ago: red and gold drapes, a tiered champagne tower, round banquet "
               "tables, warm tungsten light, slightly faded colours like an old wedding video.",
    "NHAHANG": "An elegant restaurant near closing time: a candle-lit table for two by the window, rain on the glass, waiters "
               "stacking chairs in the soft-focus background.",
    "TIEMVANG": "A bright jewellery shop counter: glass display cases of rings, mirrored walls, crisp white spotlights.",
}
SOUND = {
    "GHE": "the low hum of a vending machine, a wall clock ticking, rain on the window, a distant trolley",
    "GHE_SANG": "morning birds outside, a wall clock ticking, distant footsteps and a trolley",
    "VP_DEM": "rain on the window, the hum of an air conditioner, calculator keys clicking",
    "NHA_MAI_DEM": "a small fan whirring, rain on a tin awning, a soft lullaby hum",
    "QUAY": "a quiet hospital at night, a keyboard clacking far off, a monitor beeping faintly",
    "DUONGMUA": "heavy rain, a hazard indicator ticking, a distant ambulance far away",
    "SANH_MUA": "heavy rain on the canopy, a taxi engine idling, sliding doors hissing open",
    "HL": "footsteps echoing, fluorescent tubes buzzing, rain far off",
    "HL_SANG": "morning birds, footsteps echoing, a distant trolley",
    "CUASO": "rain against the glass, fluorescent tubes buzzing",
    "MAYBAN": "the vending machine humming and clunking, rain on the window",
    "CANTIN": "a stock pot bubbling, a ladle against metal, a fridge humming",
    "BANCONG": "steady rain, water dripping from the roof edge, distant traffic",
    "PHONGBENH": "a heart monitor beeping slowly, a curtain ring sliding, birds waking outside",
    "PHONGBENH_CUA": "a heart monitor beeping faintly through the door, soft footsteps",
    "CONG_SANG": "motorbikes passing on a wet street, morning birds, a street vendor's ladle",
    "PHO": "a bubbling broth pot, chopsticks on bowls, motorbikes passing, morning birds",
    "NHA_HANH": "chopsticks on bowls, a television murmuring in another room",
    "NHA_HANH_BC": "city hum, a wind chime, muffled dinner sounds behind glass",
    "NHA_MAI": "a small fan whirring, a neighbour's radio through the wall",
    "CUOI_QUE": "a cheerful village wedding crowd, applause, a microphone's slight echo",
    "CUOI_12": "a banquet hall crowd, applause, a microphone's slight echo",
    "NHAHANG": "rain on the window, chairs being stacked, soft cutlery sounds",
    "TIEMVANG": "a quiet shop, a glass case sliding open, banknotes being counted",
}

CINE = ("Feature-film cinematography for a premium Vietnamese family drama-comedy set over one night in a city hospital: shot on "
        "ARRI Alexa 35 with Cooke anamorphic/i lenses, 24 fps, 16:9 full frame, the picture filling the frame edge to edge "
        "with no black borders, no letterbox bars and no rounded corners; deliberate cinematic "
        "blocking with foreground elements and layered depth, motivated light (cool fluorescent hospital light, rain on glass, "
        "warm practical lamps, dawn sun), rich true-to-life Vietnamese skin tones, gentle film halation and fine 35mm grain, "
        "shallow depth of field with creamy bokeh. Restrained, truthful acting with micro-expressions and dry comic timing, like "
        "an award-winning Asian festival film; never CGI, never a video game, never an advertisement.")

AVOID = ("On-screen text, TV channel logos or broadcaster bugs in any corner, character tags or names written on screen, subtitles, "
         "captions, logos, watermarks, readable writing on paper, screens, signs, badges or clock faces; any cut or second camera "
         "angle; the same person appearing twice, twins, clones or look-alike doubles; extra people in focus; distorted hands or "
         "fused fingers; face, hair or costume changes; plastic or waxy skin; blood, wounds, needles, syringes, surgical "
         "instruments or anything graphic; flashing or cutting to an attached reference portrait or a plain grey studio backdrop; "
         "repeated, echoed or stuttered words; an off-screen narrator; background music; Southern or Central Vietnamese accents.")

# ---------------------------------------------------------------- máy quay (viết tắt dùng trong bảng shot)
CU = "85mm close-up, locked off"
CUP = "85mm close-up, very slow push-in"
MCU = "65mm medium close-up, locked off"
MS = "50mm medium shot, locked off"
MSH = "50mm medium shot, slight handheld"
TWO = "50mm two-shot, locked off"
TWOP = "50mm two-shot, slow push-in"
WIDE = "35mm wide shot, locked off"
WIDEP = "35mm wide shot, slow push-in"
INS = "macro insert, shallow depth of field, locked off"
X = "X"     # người ngoài không gắn nhân vật
PH = "PH"   # giọng qua loa điện thoại (Ly, cảnh 06)


def syl(t):
    return len(re.findall(r"\w+", t))


def speaker_rate(c):
    if c in (X, PH):
        return 4.3
    return PEOPLE[LOOK[c]["person"]]["rate"]


def timings(lines, dur, warn=None):
    """Chia mốc giây cho từng câu thoại; cảnh báo nếu thoại dài hơn shot."""
    out, t = [], 0.4
    for ln in lines:
        c, text = ln[0], ln[1]
        if len(ln) > 2:          # (người nói, câu, giây bắt đầu): thoại vào muộn, sau hành động
            t = max(t, ln[2])
        d = max(1.0, syl(text) / speaker_rate(c))
        out.append((c, text, round(t, 1), round(t + d, 1)))
        t += d + 0.4
    if out and out[-1][3] > dur - 0.3 and warn is not None:
        warn.append(f"thoại dài hơn shot ({out[-1][3]}s > {dur}s): {lines[-1][1][:50]}")
    return out


def prompt(s, warn=None):
    code, name, dur, place, looks, cam, action, lines, extra = s
    out = [f"A single continuous {dur}-second shot, 16:9, one camera angle, no cuts.", "",
           f"[LOOK] {CINE}", "", f"[PLACE] {PLACES[place]}", ""]
    if looks:
        out.append("[CHARACTERS] Use the attached character image for each person: same face, same hair, same outfit, exactly.")
        for c in looks:
            lk = LOOK[c]
            per = lk["person"]
            p = PEOPLE[per]
            desc = SHORT_LOOK.get(c, p["short"])
            out.append(f"- {per} = {p['vn']}, {p['role']} ({desc}); wears {lk['outfit']}. Attached image: \"{lk['flow']}\".")
        out.append("Each named person appears exactly once. Background people stay distant, blurred and clearly different from them.")
    else:
        out.append("[CHARACTERS] No named characters; any people in frame are distant, blurred, or seen only from behind or below the shoulders.")
    out += ["", f"[CAMERA] {cam}.", "", f"[ACTION] {action}.", ""]
    if lines:
        out.append("[DIALOGUE] In Vietnamese with exact lip-sync, standard Northern Vietnamese accent; each line spoken exactly once; "
                   "only the speaker moves the lips:")
        for c, t, a, b in timings(lines, dur, warn):
            if c == X:
                out.append(f"- {a:.1f}s–{b:.1f}s, an unnamed bystander whose face is out of focus (ordinary adult voice): {t}")
            elif c == PH:
                out.append(f"- {a:.1f}s–{b:.1f}s, a young woman's soft voice heard only through the phone's small loudspeaker, thin and "
                           f"tinny; nobody on screen moves their lips during this line: {t}")
            else:
                per = LOOK[c]["person"]
                out.append(f"- {a:.1f}s–{b:.1f}s, {per} ({PEOPLE[per]['voice']}): {t}")
        out.append(f"After the last word nobody speaks until {dur:.1f}s. Never read these directions aloud.")
    else:
        out.append("[DIALOGUE] None. Every mouth stays closed; no voices at all.")
    snd = SOUND[place] + (f"; {extra}" if extra else "")
    out += ["", f"[SOUND] {snd}. No music.", "", f"[AVOID] {AVOID}", ""]
    return "\n".join(out)


def ref_prompt(c):
    lk = LOOK[c]
    p = PEOPLE[lk["person"]]
    return (f"Full-body photorealistic character reference of {p['face']}, wearing {lk['outfit']}; plain light-grey studio "
            "background, soft even daylight, natural skin texture with pores and fine lines, realistic proportions, 8K. "
            "Not resembling any real person.")


def edit_prompt(c):
    return (f"Same person, same face and hair, exactly. Now wearing {LOOK[c]['outfit']}. Full body, plain light-grey studio background.")


def write(path, text):
    path = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def speaker_vn(c):
    if c == X:
        return "Người ngoài"
    if c == PH:
        return "Ly (qua loa điện thoại)"
    return PEOPLE[LOOK[c]["person"]]["vn"]
