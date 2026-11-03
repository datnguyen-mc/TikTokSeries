#!/usr/bin/env python3
"""Global Film Bible (Single Source of Truth) for 'Kẻ Sống Sót: Bóng Ma'.

Provides reusable locks for:
- CHARACTER_LOCK (9 leads, 22 timeline/wardrobe looks, voice & identity rules)
- VEHICLE_LOCK (7 recurring vehicles with LHD cab, doors, seating & damage state)
- ENVIRONMENT_LOCK (53 recurring locations with 180-degree axis & geography)
- OBJECT_LOCK (33 persistent props with cross-scene state progression)
- PHYSICS_RULES (human, vehicle, object, and coastal/environmental physics)
- CINEMATIC_STYLE (16:9 widescreen, 24fps, shutter, color grade, clean frame)
- AUDIO_STYLE (Southern Vietnamese dialogue, mouth-map sync, 3rd-person narrator)
- OMNI_MODEL_CAPABILITIES (workflow routing, reference budgeting, studio-card guard)

Also provides `select_relevant_bible_slice(plan, shot)` so each generated shot prompt
injects ONLY the entities, vehicle specs, spatial axis, and physics rules active in that shot.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
_PLAN_PATH = BASE_DIR / "PHAN_CANH_V3.json"


def _load_canonical_plan() -> dict[str, Any]:
    if _PLAN_PATH.is_file():
        return json.loads(_PLAN_PATH.read_text(encoding="utf-8"))
    return {}


_CANON = _load_canonical_plan()

VEHICLE_LOCK: dict[str, dict[str, Any]] = {
    "COACH_BUS": {
        "id": "COACH_BUS",
        "name": "Intercity Coastal Coach",
        "type": "Old Vietnamese intercity passenger coach",
        "color_and_material": "Faded cream-and-blue painted sheet metal, dust-streaked lower flanks, weathered rubber window seals, no readable lettering or logos",
        "Configuration": "Left-hand drive cab (driver seated on LEFT behind large steering wheel), single folding passenger door on RIGHT flank just behind front wheel, twin axles with heavy road tyres",
        "locations": ["CROSSROAD", "BUS", "REST_STOP"],
        "keywords": ["coach", "bus", "passenger door"],
        "physics": "Air-brake hiss and nose dip on stopping, heavy suspension settling on sandy asphalt, folding door pneumatics.",
    },
    "MAY_MOTORBIKE": {
        "id": "MAY_MOTORBIKE",
        "name": "Town Patrol Motorcycle",
        "type": "Practical dark-colored Vietnamese commuter motorcycle",
        "color_and_material": "Matte dark body panels, steel front forks, upright handlebars, dual vinyl seat, rear footpegs",
        "Configuration": "Two-wheeled upright motorcycle; Mây at front handlebar controls, Sơn riding pillion behind her; two helmets secured before engine ignition",
        "locations": ["MOTORBIKE", "CLIFFROAD", "LIGHTHOUSE_BASE"],
        "keywords": ["motorcycle", "motorbike", "pillion", "handlebars"],
        "physics": "Natural two-wheel lean on winding coastal cliff road, suspension compression under two riders, tyres gripping paved incline.",
    },
    "BAY_VAN": {
        "id": "BAY_VAN",
        "name": "Medical Support Van",
        "type": "Compact weathered white utility van",
        "color_and_material": "Salt-faded white paint, steel cargo body, twin rear swing doors, warm practical interior lamp",
        "Configuration": "Stationary utility van parked behind market wall; rear cargo bay fitted with a clean mattress and medical support kit",
        "locations": ["HARBOUR_REAR", "VAN", "VAN_REAR"],
        "keywords": ["van", "mattress", "rear doors"],
        "physics": "Subtle chassis rock when someone steps into or out of the rear cargo bay; heavy metal door latch.",
    },
    "KIEN_WHITE_CAR": {
        "id": "KIEN_WHITE_CAR",
        "name": "White Executive Sedan",
        "type": "Four-door white luxury sedan",
        "color_and_material": "Gloss white exterior paint, tinted glass windows, grey leather rear bench seat",
        "Configuration": "Left-hand drive sedan parked on the west side of the harbour apron; rear street-side door used for passenger movement",
        "locations": ["HARBOUR", "WHITE_CAR"],
        "keywords": ["white car", "rear seat", "window motor"],
        "physics": "Smooth electric window motor, heavy car door seal and latch.",
    },
    "HAINGOC_BLACK_CAR": {
        "id": "HAINGOC_BLACK_CAR",
        "name": "Black Executive Sedan",
        "type": "Four-door black executive sedan",
        "color_and_material": "Deep black paint, chrome window trim, dark interior upholstery",
        "Configuration": "Left-hand drive sedan parked on the east side of the harbour apron opposite the white sedan",
        "locations": ["HARBOUR"],
        "keywords": ["black car"],
        "physics": "Stationary weight on concrete harbour apron.",
    },
    "RIVER_WORKBOAT": {
        "id": "RIVER_WORKBOAT",
        "name": "Wooden River Workboat",
        "type": "Low-profile wooden coastal/river utility boat",
        "color_and_material": "Weathered timber hull and wooden side rails, two transverse wooden bench seats, stern outboard motor, mooring rope at bow",
        "Configuration": "Open wooden hull with low side rails and a secured storage space beneath the bench seat",
        "locations": ["LAB_DOCK", "RIVER"],
        "keywords": ["boat", "workboat", "side rail", "hull", "mooring rope"],
        "physics": "Natural buoyancy and hull roll when stepped into; side rail depresses slightly under hand weight; stern wake and bow ripple on tidal river.",
    },
    "PRISON_TRANSPORT": {
        "id": "PRISON_TRANSPORT",
        "name": "Coastal Shuttle Van",
        "type": "Enclosed coastal passenger shuttle van",
        "color_and_material": "Clean neutral-toned metal body, screened side window on right flank, interior bench seats",
        "Configuration": "Interior compartment with bench seats facing each other and a screened right window looking out toward the seafront walkway",
        "locations": ["TRANSPORT", "TRANSPORT_VIEW"],
        "keywords": ["transport", "mesh window", "transfer"],
        "physics": "Steady road vibration and forward rolling motion parallel to the coastal walkway.",
    },
}

_LOCATION_AXES: dict[str, tuple[str, str]] = {
    "CROSSROAD": ("coastal_road", "180-degree axis from inland roadside looking south toward the sea; coach travels screen-left to screen-right in near lane; town road leads screen-right."),
    "STREET": ("town_exterior", "180-degree axis along Hòn Sóng main street; sea wall on south side, tube houses and coffee stall on landward side."),
    "STALL": ("stall_interior", "180-degree axis across Ông Bảy's coffee stall: counter landward, low stools and tables seaward, street reflected in counter mirror."),
    "STALL_REAR": ("town_alley", "180-degree axis inside covered rear lane behind coffee stall: map table beside rear door, bottle crates against wall."),
    "DUNE": ("coastal_path", "180-degree axis along sandy casuarina footpath: cabin uphill north, market path downhill south toward grey-blue sea."),
    "CABIN": ("cabin_interior", "180-degree axis inside one-room wooden cabin: porch door south (seaward), table under east window, cot west, rear exit north, tally-marked doorframe at entry."),
    "PORCH": ("cabin_exterior", "180-degree axis on south seaward porch: table and two stools center, dune path on left when facing the open sea below."),
    "POST": ("town_office", "180-degree axis inside town office: public desk in front, quiet study room behind, side meeting rooms off corridor."),
    "INTERVIEW": ("town_office", "180-degree axis across meeting table: two chairs facing each other across the table and recorder, camera stays on established side of table axis."),
    "HOLDING": ("town_office", "180-degree axis inside quiet back room: bench against wall, high window above, corridor light outside."),
    "CLINIC": ("clinic_interior", "180-degree axis inside town clinic: green-curtained steel beds on one side, locked sample cupboard and doctor's desk opposite."),
    "SILK": ("city_interior", "180-degree axis inside Bà Hai's silk shop: teak desk east, screened safe behind desk, rear stockroom door west."),
    "SILK_REAR": ("city_alley", "180-degree axis along narrow rain-wet rear alley outside the stockroom door beneath shallow awning."),
    "SILK_STORE": ("city_interior", "180-degree axis inside silk-shop rear stockroom: known shelf beside loading door, ledger and sealed tin stored together."),
    "ALLEY": ("city_alley", "180-degree axis along city rear lane looking toward flower shop at street level and tower across road."),
    "FLOWER": ("shop_interior", "180-degree axis inside Hạ's flower shop: wooden counter east, flower buckets under front window, street outside."),
    "FLOWER_BACK": ("shop_interior", "180-degree axis in flower-shop back room: small wooden table and kettle center, doorway toward main counter."),
    "FLOWER_FRONT": ("city_exterior", "180-degree axis on pavement outside flower shop: rolling shutter landward, kerb and parked motorbikes streetward."),
    "CITY_PIER": ("waterfront", "180-degree axis along city passenger pier walkway: glass wind rail on river side, ferries beyond."),
    "GARAGE": ("underground_garage", "180-degree axis in underground car park: ramp north, lift east, concrete pillar rows center, low maintenance exit door west."),
    "GARAGE_EXIT": ("city_alley", "180-degree axis at west maintenance exit steps leading out to sheltered city rear lane."),
    "MARKET": ("market_interior", "180-degree axis along narrow wet concrete fish-market aisle between foam boxes and crushed-ice fish crates."),
    "MARKET_ENTRY": ("market_exterior", "180-degree axis at landward fish-market rolling shutter with wheeled cart and stacked plastic baskets."),
    "MARKET_REAR": ("market_exterior", "180-degree axis at rear market exit opening onto safe residential lane."),
    "MARKET_ROOF": ("rooftop_overlook", "180-degree axis from low corrugated market roof looking down toward harbour apron and uphill lighthouse path."),
    "BUS": ("vehicle_interior", "180-degree axis inside overnight coach looking across center aisle: Sơn at left window seat near rear, Mây across aisle."),
    "REST_STOP": ("roadside_exterior", "180-degree axis under coach rest-stop awning: parked coach on road side, sheltered path toward changing rooms."),
    "REST_ROOM": ("room_interior", "180-degree axis inside private changing room: simple wall mirror and clothing hook."),
    "MOTEL": ("room_interior", "180-degree axis inside city motel room: bed on left, window table with borrowed laptop on right."),
    "LAB_ROOF": ("rooftop_overlook", "180-degree axis behind low roof wall overlooking factory loading yard via roof vent."),
    "LAB": ("factory_interior", "180-degree axis inside old fish-sauce factory workshop: loading aisle, sealed sample shelves, sliding screen, river door."),
    "LAB_DOCK": ("river_dock", "180-degree axis at river loading dock: rope-operated gate landward, wooden workboat moored on outer river side."),
    "RIVER": ("open_water", "180-degree axis aboard wooden workboat moving along tidal river channel between factory and coast."),
    "VIDEO_ROOM": ("phone_video_space", "180-degree axis inside phone video frame: plain bright room with small vent fan and blurred ferry emblem outside window."),
    "OLD_CORRIDOR": ("flashback_interior", "180-degree axis along old apartment corridor 25 years earlier: wooden front door and rain-lit stairwell window."),
    "HARBOUR": ("harbour_apron", "180-degree axis across Hòn Sóng harbour apron: sea south with moored blue wooden boats, market north, black car east, white car west, center painted seam, lighthouse service stair rising west."),
    "HARBOUR_REAR": ("harbour_lane", "180-degree axis in protected rear lane behind market wall: Bảy's van parked with rear doors facing clinic route."),
    "HARBOUR_SERVICE": ("lighthouse_approach", "180-degree axis at lower lighthouse maintenance gate behind west harbour apron with narrow stair rising above."),
    "HARBOUR_WALK": ("coastal_walkway", "180-degree axis along public seafront walkway under casuarina trees beside main transport road."),
    "VAN": ("vehicle_interior", "180-degree axis inside Bảy's stationary van cargo bay: mattress and medical bag inside, open rear doors facing safe lane."),
    "VAN_REAR": ("harbour_lane", "180-degree axis outside open rear doors of Bảy's stationary van with market wall behind."),
    "MOTORBIKE": ("harbour_lane", "180-degree axis beside stationary motorcycle in safe lane: Mây at front controls, Sơn pillion."),
    "CLIFFROAD": ("coastal_road", "180-degree axis along winding paved cliff road: motorcycle travels screen-left to screen-right uphill toward lighthouse, sea on south side."),
    "LIGHTHOUSE_BASE": ("lighthouse_approach", "180-degree axis at main iron entrance of old lighthouse: motorcycle space outside, spiral stair inside."),
    "LIGHTHOUSE_STAIR": ("lighthouse_interior", "180-degree axis on spiral stair inside lighthouse with continuous handrail leading up to gallery."),
    "LIGHTHOUSE": ("lighthouse_gallery", "180-degree axis on lighthouse gallery: main stair door east, service hatch north, inner masonry wall center, sea rail south, backup lamp aimed seaward."),
    "LIGHTHOUSE_SERVICE": ("lighthouse_interior", "180-degree axis on narrow maintenance stair below gallery: inner latch on hatch above, backup-light lever below final landing."),
    "WHITE_CAR": ("vehicle_interior", "180-degree axis inside rear of Kiên's white sedan: grey seats, street-side rear door on one side, opposite door closed."),
    "HA_HOME": ("house_interior", "180-degree axis inside Hạ's harbour house: salt-faded walls, old lighthouse photo, workbench, yard vase with white lilies."),
    "STALL_SITE": ("market_exterior", "180-degree axis at empty strip beside fish-market entrance with chalk marks on concrete."),
    "TRANSPORT": ("vehicle_interior", "180-degree axis inside transfer van: mesh window on right, Sơn seated facing front, Thành opposite with folder."),
    "TRANSPORT_VIEW": ("vehicle_pov", "180-degree POV looking out through right-side mesh window toward Hạ and Mây on public seafront walkway."),
    "FLOWER_STALL": ("shop_interior", "180-degree axis inside Hạ's completed flower stall at market entrance: counter with seven-mark wood strip fixed underneath, doorway toward coach stop."),
}

ENVIRONMENT_LOCK: dict[str, dict[str, Any]] = {}
for _loc_key, (_loc_desc, _loc_sound) in _CANON.get("locations", {}).items():
    _cat, _axis = _LOCATION_AXES.get(
        _loc_key,
        ("coastal_setting", "180-degree camera axis preserved consistently across connected shots."),
    )
    ENVIRONMENT_LOCK[_loc_key] = {
        "id": _loc_key,
        "category": _cat,
        "description": _loc_desc,
        "ambient_sound": _loc_sound,
        "orientation_axis": _axis,
    }

CHARACTER_LOCK: dict[str, dict[str, Any]] = {}
for _cid, _cdata in _CANON.get("identities", {}).items():
    _variants = {
        _lk: {"age": _age, "wardrobe": _outfit}
        for _lk, (_base, _age, _outfit) in _CANON.get("looks", {}).items()
        if _base == _cid
    }
    CHARACTER_LOCK[_cid] = {
        "id": _cid,
        "tag": _cdata["tag"],
        "name": _cdata["name"],
        "media_id": _cdata["media_id"],
        "identity": _cdata["identity"],
        "voice": _cdata["voice"],
        "looks": _variants,
    }

OBJECT_LOCK: dict[str, dict[str, Any]] = {
    _pk: {
        "id": _pk,
        "description": _pdesc,
        "persistent_rule": "Preserve exact size, material, hand assignment, and damage/open state across shots.",
    }
    for _pk, _pdesc in _CANON.get("props", {}).items()
}

PHYSICS_RULES: dict[str, str] = {
    "human": (
        "Natural weight transfer, knee/hip bend when reaching low objects, five distinct fingers per hand closing "
        "around carried props with real mass, steady foot contact without sliding, natural chest breathing and eye blinks."
    ),
    "vehicle": (
        "Realistic tire rolling and suspension compression, natural braking nose-dip, left-hand drive steering alignment, "
        "proper motorcycle lean and two-rider balance, realistic wooden boat buoyancy and hull roll on water."
    ),
    "object": (
        "Props never float, teleport, duplicate, or pass through fingers; hand-offs show both hands until receiver's fingers "
        "close; pocket watch, ledgers, USB drives, scarf pieces, and bags keep their exact established state."
    ),
    "environment": (
        "Consistent coastal wind direction on casuarina needles, hair, and clothing; natural water ripples and wakes; "
        "consistent shadow angles and practical lamp reflections."
    ),
}

CINEMATIC_STYLE: dict[str, Any] = {
    "aspect_ratio": "16:9",
    "frame_rate": 24,
    "genre": "photorealistic live-action Vietnamese coastal mystery and suspense drama",
    "color_grade": "cool shadows, restrained warm highlights, natural skin tones; no heavy teal-orange, artificial lens flare or beauty smoothing",
    "clean_frame_rule": "Single continuous shot from 0.0s to 10.0s with one camera setup and one location; never flash studio reference cards or broadcast overlays.",
}

AUDIO_STYLE: dict[str, Any] = {
    "dialogue_language": "Southern Vietnamese",
    "max_clip_syllables": 30,
    "max_syllables_per_second": 4.5,
    "narrator_syllables_per_second": 3.8,
    "narrator": _CANON.get("narrator", {}),
}

OMNI_MODEL_CAPABILITIES: dict[str, Any] = {
    "model_family": "omni_flash",
    "clip_duration_s": 10,
    "resolution": "720p",
    "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE",
    "max_reference_images": 7,
    "workflows": {
        "image_to_video_first_frame": "Used when transition == 'CONTINUE' to seamlessly extend the previous clip's final frame.",
        "ingredients_reference_to_video": "Used on editorial cuts (OPEN, CUT, MATCH, J, L) when named lead characters or photo references are present.",
        "text_to_video": "Used on editorial cuts when no named lead character or photo reference is present.",
    },
}

GLOBAL_FILM_BIBLE: dict[str, Any] = {
    "title": _CANON.get("title", "Kẻ Sống Sót: Bóng Ma"),
    "CHARACTER_LOCK": CHARACTER_LOCK,
    "VEHICLE_LOCK": VEHICLE_LOCK,
    "ENVIRONMENT_LOCK": ENVIRONMENT_LOCK,
    "OBJECT_LOCK": OBJECT_LOCK,
    "PHYSICS_RULES": PHYSICS_RULES,
    "CINEMATIC_STYLE": CINEMATIC_STYLE,
    "AUDIO_STYLE": AUDIO_STYLE,
    "OMNI_MODEL_CAPABILITIES": OMNI_MODEL_CAPABILITIES,
}


def select_relevant_bible_slice(plan: dict[str, Any], shot: dict[str, Any]) -> dict[str, Any]:
    """Return ONLY the subset of GLOBAL_FILM_BIBLE needed for `shot`."""
    loc_key = shot.get("location", "")
    env_entry = ENVIRONMENT_LOCK.get(loc_key, {})

    active_chars: dict[str, dict[str, Any]] = {}
    for look_key in shot.get("characters", []):
        base_id = plan["looks"][look_key][0]
        if base_id in CHARACTER_LOCK:
            active_chars[look_key] = {
                "base_id": base_id,
                "tag": CHARACTER_LOCK[base_id]["tag"],
                "name": CHARACTER_LOCK[base_id]["name"],
                "media_id": CHARACTER_LOCK[base_id]["media_id"],
                "look": CHARACTER_LOCK[base_id]["looks"].get(look_key, {}),
            }

    text_blob = " ".join(
        [
            str(shot.get("start_frame", "")),
            str(shot.get("action", "")),
            str(shot.get("end_frame", "")),
            str(shot.get("wardrobe_note", "")),
        ]
    ).lower()

    active_vehicles: list[dict[str, Any]] = []
    for v_id, v_spec in VEHICLE_LOCK.items():
        if loc_key in v_spec["locations"] or any(kw in text_blob for kw in v_spec["keywords"]):
            active_vehicles.append(v_spec)

    active_objects: dict[str, dict[str, Any]] = {
        p_key: OBJECT_LOCK[p_key]
        for p_key in shot.get("props", [])
        if p_key in OBJECT_LOCK
    }

    physics_slice = [PHYSICS_RULES["human"], PHYSICS_RULES["environment"]]
    if active_vehicles:
        physics_slice.append(PHYSICS_RULES["vehicle"])
    if active_objects:
        physics_slice.append(PHYSICS_RULES["object"])

    return {
        "shot_id": shot.get("id"),
        "location": env_entry,
        "characters": active_chars,
        "vehicles": active_vehicles,
        "objects": active_objects,
        "physics": physics_slice,
    }

