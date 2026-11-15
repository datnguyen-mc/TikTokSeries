import json
import math
import subprocess
from pathlib import Path

BASE = Path("/Users/iseul-a/Documents/TikTokSeries/ww2-ghost-army-b2")
META = json.loads((BASE / "art/sprites-meta.json").read_text(encoding="utf-8"))
VOICE_DUR = float(subprocess.check_output([
    "/opt/homebrew/bin/ffprobe", "-v", "error",
    "-show_entries", "format=duration",
    "-of", "default=noprint_wrappers=1:nokey=1",
    str(BASE / "narration.wav")
], text=True).strip())
LEAD = 0.25
TARGET_DUR = 29.80
TAIL = round(TARGET_DUR - VOICE_DUR - LEAD, 6)

SAFE_MIN_X = 82.0
SAFE_MAX_X = 1120.0
SAFE_MIN_Y = 190.0
SAFE_MAX_Y = 1662.0


def sprite_region(rid: str, role: str, layer: dict, intent: str, pad: float = 28.0) -> dict:
    fname = Path(layer["path"]).name
    sw, sh = META[fname]["w"], META[fname]["h"]
    states = [layer] + layer.get("keys", [])
    cur_x = layer["x"]
    cur_y = layer["y"]
    cur_w = layer["w"]
    cur_a = layer.get("angle", 0.0)

    pts = []
    for s in states:
        cur_x = s.get("x", cur_x)
        cur_y = s.get("y", cur_y)
        cur_w = s.get("w", cur_w)
        cur_a = s.get("angle", cur_a)
        cur_h = cur_w * sh / sw
        ca, sa = math.cos(cur_a), math.sin(cur_a)
        for cx, cy in [(0, 0), (cur_w, 0), (0, cur_h), (cur_w, cur_h)]:
            pts.append((cur_x + cx * ca - cy * sa, cur_y + cx * sa + cy * ca))

    min_x = min(p[0] for p in pts)
    max_r = max(p[0] for p in pts)
    min_y = min(p[1] for p in pts)
    max_b = max(p[1] for p in pts)

    rx0 = max(SAFE_MIN_X, math.floor(min_x - pad))
    ry0 = max(SAFE_MIN_Y, math.floor(min_y - pad))
    rx1 = min(SAFE_MAX_X, math.ceil(max_r + pad))
    ry1 = min(SAFE_MAX_Y, math.ceil(max_b + pad))
    return {
        "id": rid,
        "role": role,
        "layer_ids": [layer["id"]],
        "region": {"x": rx0, "y": ry0, "w": rx1 - rx0, "h": ry1 - ry0},
        "intent": intent,
    }


def build():
    # --- SHOT 1 (0.00 -> 6.30s): Unbroken palm-to-tread contact + centered badge ---
    s1_title = {
        "id": "s1_title",
        "type": "text",
        "text": "ANH QUỐC · MÙA XUÂN 1944",
        "x": 165, "y": 230, "w": 890, "size": 52, "bold": True, "color": "#26231f"
    }
    s1_soldiers = {
        "id": "s1_soldiers",
        "type": "image",
        "path": "art/s1_soldiers_lifting.png",
        "x": 265, "y": 865, "w": 680,
    }
    s1_tank = {
        "id": "s1_tank",
        "type": "image",
        "path": "art/s1_rubber_tank.png",
        "x": 205, "y": 532, "w": 810,
        "motion": {"role": "prop", "reason": "40-ton rubber tank flexes and rocks directly inside the four cupped palms of the two soldiers"},
        "keys": [
            {"t": 0.00, "y": 535, "angle": -0.006},
            {"t": 1.30, "y": 525, "angle": 0.007},
            {"t": 2.60, "y": 536, "angle": -0.007},
            {"t": 3.90, "y": 525, "angle": 0.007},
            {"t": 5.20, "y": 535, "angle": -0.006},
            {"t": 6.30, "y": 527, "angle": 0.005},
        ]
    }
    s1_badge = {
        "id": "s1_badge",
        "type": "image",
        "path": "art/s1_feather_badge.png",
        "from": 2.75,
        "x": 380, "y": 335, "w": 470,
        "motion": {"role": "information", "reason": "Centered callout questioning how a 40-ton tank feels feather-light"},
        "keys": [
            {"t": 2.75, "y": 344},
            {"t": 4.00, "y": 324},
            {"t": 5.20, "y": 342},
            {"t": 6.30, "y": 326},
        ]
    }

    # --- SHOT 2 (6.30 -> 9.60s): Grounded soldier & cylinder + separate moving plunger ---
    s2_title = {
        "id": "s2_title",
        "type": "text",
        "text": "BÍ MẬT: XE TĂNG BƠM HƠI!",
        "x": 195, "y": 240, "w": 850, "size": 54, "bold": True, "color": "#c6644c"
    }
    s2_plunger = {
        "id": "s2_plunger",
        "type": "image",
        "path": "art/s2_pump_plunger.png",
        "x": 207, "y": 1140, "w": 283,
        "motion": {"role": "prop", "reason": "Plunger rod and T-handle pumping down into the grounded red air-pump barrel"},
        "keys": [
            {"t": 0.00, "y": 1138},
            {"t": 0.85, "y": 1168},
            {"t": 1.70, "y": 1136},
            {"t": 2.55, "y": 1170},
            {"t": 3.30, "y": 1140},
        ]
    }
    s2_soldier = {
        "id": "s2_soldier",
        "type": "image",
        "path": "art/s2_pump_soldier.png",
        "x": 115, "y": 995, "w": 465,
    }
    s2_tank = {
        "id": "s2_tank",
        "type": "image",
        "path": "art/s2_floppy_tank.png",
        "x": 545, "y": 1175, "w": 540,
        "motion": {"role": "prop", "reason": "Grounded rubber Sherman tank swells outward along the tarp from its hose-connected valve"},
        "keys": [
            {"t": 0.00, "x": 548, "y": 1184, "w": 528},
            {"t": 1.10, "x": 544, "y": 1164, "w": 570},
            {"t": 2.20, "x": 547, "y": 1176, "w": 545},
            {"t": 3.30, "x": 542, "y": 1158, "w": 582},
        ]
    }
    s2_puffs = {
        "id": "s2_puffs",
        "type": "image",
        "path": "art/s2_air_puffs.png",
        "x": 425, "y": 975, "w": 280,
        "motion": {"role": "information", "reason": "Clean merged-contour air puff pulsing above the inflation nozzle"},
        "keys": [
            {"t": 0.00, "x": 432, "y": 982, "w": 270},
            {"t": 1.10, "x": 416, "y": 955, "w": 302},
            {"t": 2.20, "x": 428, "y": 978, "w": 276},
            {"t": 3.30, "x": 414, "y": 950, "w": 306},
        ]
    }

    # --- SHOT 3 (9.60 -> 14.40s): Grounded cast on wooden planks + shoulder-connected arm+hand+props ---
    s3_title = {
        "id": "s3_title",
        "type": "text",
        "text": "ĐẠO QUÂN MA · 1.100 NGHỆ SĨ",
        "x": 150, "y": 240, "w": 920, "size": 52, "bold": True, "color": "#26231f"
    }
    s3_brush = {
        "id": "s3_brush",
        "type": "image",
        "path": "art/s3_brush_prop.png",
        "x": 246, "y": 932, "w": 212,
        "motion": {"role": "prop", "reason": "Shoulder-connected right arm, hand, and olive paintbrush stroking cleanly"},
        "keys": [
            {"t": 0.00, "x": 245, "y": 936, "angle": -0.025},
            {"t": 1.20, "x": 251, "y": 924, "angle": 0.025},
            {"t": 2.40, "x": 245, "y": 936, "angle": -0.025},
            {"t": 3.60, "x": 251, "y": 924, "angle": 0.025},
            {"t": 4.80, "x": 247, "y": 932, "angle": -0.010},
        ]
    }
    s3_painter = {
        "id": "s3_painter",
        "type": "image",
        "path": "art/s3_painter.png",
        "x": 115, "y": 965, "w": 213,
    }
    s3_boom = {
        "id": "s3_boom",
        "type": "image",
        "path": "art/s3_boom_prop.png",
        "x": 572, "y": 930, "w": 211,
        "motion": {"role": "prop", "reason": "Shoulder-connected right arm, hand, and boom microphone angling cleanly below boards"},
        "keys": [
            {"t": 0.00, "x": 571, "y": 934, "angle": -0.025},
            {"t": 1.20, "x": 577, "y": 920, "angle": 0.025},
            {"t": 2.40, "x": 571, "y": 934, "angle": -0.025},
            {"t": 3.60, "x": 577, "y": 920, "angle": 0.025},
            {"t": 4.80, "x": 573, "y": 929, "angle": -0.010},
        ]
    }
    s3_sound = {
        "id": "s3_sound",
        "type": "image",
        "path": "art/s3_sound_eng.png",
        "x": 505, "y": 965, "w": 154,
    }
    s3_clapper = {
        "id": "s3_clapper",
        "type": "image",
        "path": "art/s3_clapper_prop.png",
        "x": 746, "y": 1042, "w": 217,
        "motion": {"role": "prop", "reason": "Shoulder-connected left arm, hand, and clapperboard snapping cleanly"},
        "keys": [
            {"t": 0.00, "y": 1048, "angle": 0.024},
            {"t": 1.20, "y": 1034, "angle": -0.024},
            {"t": 2.40, "y": 1048, "angle": 0.024},
            {"t": 3.60, "y": 1034, "angle": -0.024},
            {"t": 4.80, "y": 1043, "angle": 0.010},
        ]
    }
    s3_actor = {
        "id": "s3_actor",
        "type": "image",
        "path": "art/s3_actor.png",
        "x": 885, "y": 965, "w": 181,
    }

    # --- SHOT 4 (14.40 -> 20.50s): Grounded dummy tanks & mast + clear moon + level truck ---
    s4_dummy = {
        "id": "s4_dummy",
        "type": "image",
        "path": "art/s4_dummy_row.png",
        "x": 165, "y": 605, "w": 760,
    }
    s4_radio = {
        "id": "s4_radio",
        "type": "image",
        "path": "art/s4_radio_rings.png",
        "x": 740, "y": 405, "w": 270,
        "motion": {"role": "information", "reason": "Fake Morse radio transmissions pulsing above the mast clear of the moon"},
        "keys": [
            {"t": 0.00, "x": 746, "y": 414, "w": 262},
            {"t": 1.50, "x": 728, "y": 380, "w": 298},
            {"t": 3.00, "x": 744, "y": 412, "w": 266},
            {"t": 4.50, "x": 726, "y": 378, "w": 302},
            {"t": 6.10, "x": 738, "y": 402, "w": 278},
        ]
    }
    s4_truck = {
        "id": "s4_truck",
        "type": "image",
        "path": "art/s4_speaker_truck.png",
        "x": 115, "y": 1035, "w": 485,
        "motion": {"role": "prop", "reason": "Half-track speaker truck rolling level along the flat foreground ridge"},
        "keys": [
            {"t": 0.00, "x": 115},
            {"t": 2.00, "x": 142},
            {"t": 4.00, "x": 164},
            {"t": 6.10, "x": 185},
        ]
    }
    s4_waves = {
        "id": "s4_waves",
        "type": "image",
        "path": "art/s4_sound_waves.png",
        "x": 615, "y": 870, "w": 340,
        "motion": {"role": "information", "reason": "20-kilometer acoustic deception soundwaves booming outward from speaker horn"},
        "keys": [
            {"t": 0.00, "x": 612, "y": 878, "w": 335},
            {"t": 1.50, "x": 672, "y": 852, "w": 375},
            {"t": 3.00, "x": 642, "y": 874, "w": 345},
            {"t": 4.50, "x": 698, "y": 848, "w": 382},
            {"t": 6.10, "x": 685, "y": 864, "w": 368},
        ]
    }

    # --- SHOT 5 (20.50 -> 23.50s): Calais anchored on coast + decoy arrow with arrowhead ---
    s5_calais = {
        "id": "s5_calais",
        "type": "image",
        "path": "art/s5_calais_decoy.png",
        "x": 645, "y": 735, "w": 445,
    }
    s5_normandy = {
        "id": "s5_normandy",
        "type": "image",
        "path": "art/s5_normandy_target.png",
        "x": 125, "y": 1265, "w": 445,
    }
    s5_decoy_arrow = {
        "id": "s5_decoy_arrow",
        "type": "arrow",
        "x": 495, "y": 618, "w": 230,
        "angle": 0.48,
        "color": "#c6644c",
        "lineWidth": 8,
        "progress": 0.18,
        "motion": {"role": "information", "reason": "Directional decoy arrow showing German focus drawn from Dover straight to Calais"},
        "keys": [
            {"t": 0.00, "progress": 0.18},
            {"t": 1.15, "progress": 1.00},
            {"t": 3.00, "progress": 1.00},
        ]
    }
    s5_plane = {
        "id": "s5_plane",
        "type": "image",
        "path": "art/s5_recon_plane.png",
        "x": 155, "y": 445, "w": 275,
        "motion": {"role": "actor", "reason": "German reconnaissance plane flying across the Channel into the Calais decoy zone"},
        "keys": [
            {"t": 0.00, "x": 155, "y": 442, "angle": 0.05},
            {"t": 1.50, "x": 385, "y": 472, "angle": 0.02},
            {"t": 3.00, "x": 585, "y": 492, "angle": -0.02},
        ]
    }

    # --- SHOT 6 (23.50 -> 29.80s): Boats advancing beachward clear of soldier + flush waving flag ---
    s6_stamp = {
        "id": "s6_stamp",
        "type": "image",
        "path": "art/s6_dday_stamp.png",
        "x": 280, "y": 245, "w": 660,
    }
    s6_boats = {
        "id": "s6_boats",
        "type": "image",
        "path": "art/s6_landing_craft.png",
        "x": 75, "y": 815, "w": 420,
        "motion": {"role": "prop", "reason": "Allied Higgins landing craft advancing downward-right in open sea channel clear of bluff soldier"},
        "keys": [
            {"t": 0.00, "x": 75, "y": 815, "w": 420},
            {"t": 2.10, "x": 110, "y": 836, "w": 434},
            {"t": 4.20, "x": 140, "y": 855, "w": 445},
            {"t": 6.30, "x": 165, "y": 872, "w": 455},
        ]
    }
    s6_flag = {
        "id": "s6_flag",
        "type": "image",
        "path": "art/s6_allied_flag.png",
        "x": 856, "y": 996, "w": 228,
        "motion": {"role": "prop", "reason": "Allied Invasion Star flag cloth waving flush against the planted flagpole"},
        "keys": [
            {"t": 0.00, "w": 226, "angle": -0.020},
            {"t": 1.60, "w": 240, "angle": 0.020},
            {"t": 3.20, "w": 225, "angle": -0.020},
            {"t": 4.80, "w": 242, "angle": 0.020},
            {"t": 6.30, "w": 232, "angle": -0.008},
        ]
    }
    s6_soldiers = {
        "id": "s6_soldiers",
        "type": "image",
        "path": "art/s6_victory_soldiers.png",
        "x": 705, "y": 985, "w": 195,
    }

    shots = [
        {
            "id": "shot_1_lift",
            "start": 0.00,
            "end": 6.30,
            "layers": [
                {"id": "s1_bg", "type": "image", "path": "art/s1_bg.png", "x": 0, "y": 0, "w": 1280},
                s1_title,
                s1_soldiers,
                s1_tank,
                s1_badge,
            ],
            "portrait": {
                "intent": "Vertical stack framing two grounded soldiers holding a 40-ton rubber Sherman tank directly on their cupped palms",
                "background_ids": ["s1_bg"],
                "regions": [
                    {"id": "r1_title", "role": "information", "layer_ids": ["s1_title"], "region": {"x": 140, "y": 210, "w": 940, "h": 95}, "intent": "Location and year header at top of safe area"},
                    sprite_region("r1_soldiers", "actor", s1_soldiers, "Two US stickman soldiers planted on grass with raised cupped palms"),
                    sprite_region("r1_tank", "prop", s1_tank, "40-ton Sherman tank resting directly on the soldiers' palms"),
                    sprite_region("r1_badge", "information", s1_badge, "Centered feather-light callout badge above tank"),
                ],
            },
        },
        {
            "id": "shot_2_pump",
            "start": 6.30,
            "end": 9.60,
            "layers": [
                {"id": "s2_bg", "type": "image", "path": "art/s2_bg.png", "x": 0, "y": 0, "w": 1280},
                s2_title,
                s2_plunger,
                s2_soldier,
                s2_tank,
                s2_puffs,
            ],
            "portrait": {
                "intent": "Workshop close-up with grounded soldier pumping plunger into floor pump connected directly to expanding rubber tank",
                "background_ids": ["s2_bg"],
                "regions": [
                    {"id": "r2_title", "role": "information", "layer_ids": ["s2_title"], "region": {"x": 165, "y": 220, "w": 900, "h": 95}, "intent": "Reveal header above workshop blueprint"},
                    sprite_region("r2_plunger", "prop", s2_plunger, "Animated plunger handle sliding into red floor pump"),
                    sprite_region("r2_soldier", "actor", s2_soldier, "Grounded soldier, red pump cylinder, and hose feeding tank valve"),
                    sprite_region("r2_tank", "prop", s2_tank, "Grounded inflatable rubber tank expanding on tarp"),
                    sprite_region("r2_puffs", "information", s2_puffs, "Clean merged-contour air puff above inflation valve"),
                ],
            },
        },
        {
            "id": "shot_3_artists",
            "start": 9.60,
            "end": 14.40,
            "layers": [
                {"id": "s3_bg", "type": "image", "path": "art/s3_bg.png", "x": 0, "y": 0, "w": 1280},
                s3_title,
                s3_brush,
                s3_painter,
                s3_boom,
                s3_sound,
                s3_clapper,
                s3_actor,
            ],
            "portrait": {
                "intent": "Grounded three-artist lineup standing on wooden tent planks while waving brush, boom mic, and clapperboard",
                "background_ids": ["s3_bg"],
                "regions": [
                    {"id": "r3_title", "role": "information", "layer_ids": ["s3_title"], "region": {"x": 125, "y": 220, "w": 965, "h": 95}, "intent": "Ghost Army 1,100 artists unit banner"},
                    sprite_region("r3_painter", "actor", s3_painter, "Grounded camouflage painter holding palette on studio floor"),
                    sprite_region("r3_brush", "prop", s3_brush, "Giant olive paintbrush waving in painter's hand"),
                    sprite_region("r3_sound", "actor", s3_sound, "Grounded sound engineer wearing headphones on studio floor"),
                    sprite_region("r3_boom", "prop", s3_boom, "Boom microphone swaying cleanly below blueprint boards"),
                    sprite_region("r3_actor", "actor", s3_actor, "Grounded actor standing on studio floor"),
                    sprite_region("r3_clapper", "prop", s3_clapper, "Clapperboard snapping in actor's hand"),
                ],
            },
        },
        {
            "id": "shot_4_night",
            "start": 14.40,
            "end": 20.50,
            "layers": [
                {"id": "s4_bg", "type": "image", "path": "art/s4_bg.png", "x": 0, "y": 0, "w": 1280},
                s4_dummy,
                s4_radio,
                s4_truck,
                s4_waves,
            ],
            "portrait": {
                "intent": "Two-tier night ridges with grounded dummy tanks and radio mast above and level rolling 20km speaker truck below",
                "background_ids": ["s4_bg"],
                "regions": [
                    sprite_region("r4_dummy", "prop", s4_dummy, "Dummy tanks and radio mast planted on upper hill ridge"),
                    sprite_region("r4_radio", "information", s4_radio, "Fake Morse radio signal rings above mast clear of moon"),
                    sprite_region("r4_truck", "prop", s4_truck, "Half-track truck rolling level along lower ridge"),
                    sprite_region("r4_waves", "information", s4_waves, "20km sound-wave arcs blasting into night sky"),
                ],
            },
        },
        {
            "id": "shot_5_map",
            "start": 20.50,
            "end": 23.50,
            "layers": [
                {"id": "s5_bg", "type": "image", "path": "art/s5_bg.png", "x": 0, "y": 0, "w": 1280},
                s5_calais,
                s5_normandy,
                s5_decoy_arrow,
                s5_plane,
            ],
            "portrait": {
                "intent": "Person-free vertical Channel map showing German recon and decoy arrow converging on Calais coastline while Normandy awaits below",
                "background_ids": ["s5_bg"],
                "regions": [
                    sprite_region("r5_calais", "information", s5_calais, "Calais decoy zone anchored on the Pas-de-Calais French coast"),
                    sprite_region("r5_normandy", "information", s5_normandy, "Normandy beach landing target on lower-left French coast"),
                    {"id": "r5_decoy_arrow", "role": "information", "layer_ids": ["s5_decoy_arrow"], "region": {"x": 455, "y": 555, "w": 285, "h": 195}, "intent": "Curved decoy arrow with arrowhead from Dover to Calais"},
                    sprite_region("r5_plane", "actor", s5_plane, "German reconnaissance plane flying into Calais decoy trap"),
                ],
            },
        },
        {
            "id": "shot_6_dday",
            "start": 23.50,
            "end": 29.80,
            "layers": [
                {"id": "s6_bg", "type": "image", "path": "art/s6_bg.png", "x": 0, "y": 0, "w": 1280},
                s6_stamp,
                s6_boats,
                s6_flag,
                s6_soldiers,
            ],
            "portrait": {
                "intent": "Golden Normandy beach payoff with centered D-Day stamp, landing craft advancing beachward, and planted soldier waving Allied flag",
                "background_ids": ["s6_bg"],
                "regions": [
                    sprite_region("r6_stamp", "information", s6_stamp, "Centered D-Day 06/06/1944 historical card at top of frame"),
                    sprite_region("r6_boats", "prop", s6_boats, "Allied Higgins landing craft advancing downward-right onto beach surf"),
                    sprite_region("r6_soldiers", "actor", s6_soldiers, "Grounded soldier and planted flagpole standing on Normandy bluff"),
                    sprite_region("r6_flag", "prop", s6_flag, "Allied Invasion Star flag cloth waving from the planted flagpole"),
                ],
            },
        },
    ]

    captions = [
        {"start": 0.35, "end": 2.94, "text": "Năm 1944 ở bờ biển Anh,"},
        {"start": 3.02, "end": 3.89, "text": "hai người lính Mỹ"},
        {"start": 3.89, "end": 4.98, "text": "nhấc bổng chiếc xe tăng"},
        {"start": 4.98, "end": 6.20, "text": "nặng bốn mươi tấn!"},
        {"start": 6.74, "end": 7.78, "text": "Thực ra chiếc xe đó"},
        {"start": 7.78, "end": 9.35, "text": "chỉ là phao cao su!"},
        {"start": 9.80, "end": 11.04, "text": "Đó là Đạo quân Ma,"},
        {"start": 11.10, "end": 12.50, "text": "gồm một nghìn họa sĩ,"},
        {"start": 12.60, "end": 14.15, "text": "kỹ sư và diễn viên."},
        {"start": 14.64, "end": 16.28, "text": "Họ bơm hàng trăm xe giả,"},
        {"start": 16.35, "end": 17.62, "text": "phát sóng vô tuyến mồi,"},
        {"start": 17.70, "end": 18.82, "text": "bật loa vang cả đêm"},
        {"start": 18.82, "end": 20.25, "text": "xa hai mươi cây số."},
        {"start": 20.80, "end": 22.24, "text": "Trinh sát Đức mắc bẫy,"},
        {"start": 22.30, "end": 23.48, "text": "dồn quân giữ Calais,"},
        {"start": 23.58, "end": 24.40, "text": "giúp quân Đồng minh"},
        {"start": 24.40, "end": 25.95, "text": "đổ bộ bờ biển Normandy,"},
        {"start": 26.05, "end": 27.02, "text": "xoay chuyển cục diện"},
        {"start": 27.02, "end": 28.55, "text": "Thế chiến thứ hai!"},
    ]

    project = {
        "version": 1,
        "style": "B2",
        "width": 1080,
        "height": 1920,
        "fps": 30,
        "font": "fonts/Nunito.ttf",
        "voice": {
            "path": "narration.wav",
            "lead": LEAD,
            "tail": TAIL,
            "contains_sfx": False,
        },
        "music": {
            "path": "audio/audio/music/bgm-marty-gots-a-plan.mp3",
            "gain": 0.055,
        },
        "ambience": [
            {
                "path": "audio/audio/kresiek-amb-outside/amb_outdoor1_loop.ogg",
                "start": 0.00,
                "end": 20.50,
                "gain": 0.030,
                "loop": True,
                "fadeIn": 0.25,
                "fadeOut": 0.25,
            },
            {
                "path": "audio/audio/rubberduck-general-100-2/sfx100v2_loop_water_01.ogg",
                "start": 20.50,
                "end": 29.799,
                "gain": 0.034,
                "loop": True,
                "fadeIn": 0.25,
                "fadeOut": 0.45,
            },
        ],
        "sfx": [
            {"kind": "file", "path": "audio/audio/kenney-rpg/cloth2.ogg", "time": 0.90, "gain": 0.16, "role": "foley"},
            {"kind": "file", "path": "audio/audio/bart-squeak-toys/squeak toy/squeak toy - squeak1.wav", "time": 3.92, "gain": 0.18, "role": "foley"},
            {"kind": "file", "path": "audio/audio/rubberduck-general-100-2/sfx100v2_air_01.ogg", "time": 6.55, "duration": 1.40, "gain": 0.14, "fadeOut": 0.30, "role": "foley"},
            {"kind": "file", "path": "audio/audio/bart-squeak-toys/squeak toy/squeak toy - squeak1.wav", "time": 8.15, "gain": 0.19, "role": "foley"},
            {"kind": "file", "path": "audio/audio/kenney-rpg/bookOpen.ogg", "time": 9.72, "gain": 0.20, "role": "foley"},
            {"kind": "file", "path": "audio/audio/rubberduck-general-100-2/sfx100v2_air_01.ogg", "time": 14.65, "duration": 1.25, "gain": 0.13, "fadeOut": 0.25, "role": "foley"},
            {"kind": "file", "path": "audio/audio/kenney-interface/switch_002.ogg", "time": 16.36, "gain": 0.18, "role": "foley"},
            {"kind": "file", "path": "audio/audio/looneybits-engine-start/generic_car_startengine.wav", "time": 17.68, "duration": 1.45, "gain": 0.13, "fadeOut": 0.35, "role": "foley"},
            {"kind": "file", "path": "audio/audio/kenney-rpg/bookFlip1.ogg", "time": 20.56, "gain": 0.22, "role": "foley"},
            {"kind": "file", "path": "audio/audio/yaroslav-car-pass/car1.wav", "time": 20.90, "offset": 3.0, "duration": 2.20, "gain": 0.10, "fadeIn": 0.25, "fadeOut": 0.45, "role": "foley"},
            {"kind": "file", "path": "audio/audio/rubberduck-water-40/splash_02.ogg", "time": 24.45, "gain": 0.18, "role": "foley"},
            {"kind": "chime", "time": 27.10, "gain": 0.08},
        ],
        "captions": captions,
        "shots": shots,
        "reference_review": {
            "author_id": "antigravity-producer-main",
            "capability": {
                "mode": "sample_target",
                "environment": "Local Antigravity macOS studio (Node 20 + @napi-rs/canvas + FFmpeg + 2x supersampled B2 gouache generator + Edge-TTS Vietnamese voice)",
                "limitations": []
            }
        }
    }

    (BASE / "project.json").write_text(json.dumps(project, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Wrote grounded project.json successfully.")


if __name__ == "__main__":
    build()
