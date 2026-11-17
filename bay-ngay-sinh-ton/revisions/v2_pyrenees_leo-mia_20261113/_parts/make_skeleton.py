#!/usr/bin/env python3
"""Build _parts/skeleton_p{1..4}.json from _parts/DAN_Y.md + header.json.

Each clip gets its verbatim English turns (pace mapped to fast/normal/slow), the locked
setting, wardrobe and the speech plan the builder will use ("_plan", stripped at merge).
Shots, steps, tones and sfx are written by hand afterwards.

    python3 bay-ngay-sinh-ton/_parts/make_skeleton.py
"""
import copy
import importlib.util
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
spec = importlib.util.spec_from_file_location("builder", REPO / "flowkit/scripts/build_omni_horror_prompts.py")
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)

PACE = {"nhanh": "fast", "vừa": "normal", "chậm": "slow"}

# Bối cảnh khoá — dán nguyên văn vào "setting".
LOCKS = {
    "FOREST_TODAY": "A beech and fir forest in the French Pyrenees today, autumn afternoon: golden and copper leaves, mossy limestone boulders, a small clear stream, low golden sunlight slanting through the trees, and through a gap in the leaves a cable-car line with a small gondola gliding up the mountainside.",
    "CHALET_NIGHT": "Night inside a cozy wooden mountain chalet at the edge of the forest in the Pyrenees: warm yellow lamp light, pine-plank walls, a small table with a cheese fondue pot bubbling over a burner, a window where silent lightning flickers over dark rocky peaks.",
    "CAVE_TODAY_STORM": "Night inside a large limestone cave in the Pyrenees today during a raging storm: a wide arched mouth, a huge stalagmite shaped like a woolly mammoth, a dry earthen floor, a rock wall covered with hundreds of faded red-ochre hand stencils with one bigger hand in the middle and a slightly smaller hand right beside it, sheets of rain and white lightning beyond the entrance, light only from a headlamp.",
    "STREAM_DAWN_PAST": "Cold misty dawn about twenty-seven thousand years ago on a gravel bank beside a stream edged with ice, at the foot of a pale limestone cliff in a Pyrenees valley: snow on every mountain peak, frost on the grass, stunted pines and birches, no roads, no buildings, no people.",
    "VALLEY_PAST": "A wide Pyrenees valley during the Ice Age, about twenty-seven thousand years ago, in the morning: a blue-white glacier tongue spilling down from the peaks, cold grassy steppe with scattered birch thickets and stunted pines, an icy river winding over gravel bars, round footprints as big as car tires pressed into the snow, no roads, no buildings, no people.",
    "SHELTER_PAST": "A sheltered rock hollow under a pale limestone cliff in the Ice Age valley at midday: light snow on the ground, birch thickets, piles of dry pine branches, a flat stone, thin winter sunlight on the snow.",
    "STREAM_ROCK_PAST": "A wide icy river in the Ice Age valley in afternoon light: a big flat-topped boulder in the middle of the fast freezing current, thin shelf ice along the banks, dry reeds on the near bank, a dark pine forest edge about twenty meters away on the far bank, sun glare on the ice.",
    "CAVE_PAST_DUSK": "A large limestone cave about twenty-seven thousand years ago at dusk, home of a small Ice Age clan: a wide arched mouth, a huge stalagmite shaped like a woolly mammoth, bare rock walls with no handprints or drawings, a hearth fire in the middle, reindeer hides drying on poles, woven baskets, sleeping beds of dry grass and furs, an icy stream running below the entrance.",
    "CAVE_PAST_NIGHT": "Night inside the large Ice Age clan cave: the mammoth-shaped stalagmite, bare rock walls with no handprints, a hearth fire glowing red, sleeping beds of dry grass and furs, hides on poles, deep shadows beyond the firelight.",
    "ICE_STREAM_PAST": "A frozen stretch of stream in the Ice Age valley in the morning: clear ice over dim pebbles, leafless willow bushes along the banks, a thin layer of snow, sparkling sunlight.",
    "CAVE_PAST_BLIZZARD": "A blizzard night inside the large Ice Age clan cave: wind drives snow in through the wide arched mouth, the hearth is only cold grey ash with a thin thread of smoke, the mammoth-shaped stalagmite, bare rock walls, people huddled under furs on beds of dry grass.",
    "CAVE_PAST_PREDAWN": "Blue pre-dawn light in a dry corner of the Ice Age clan cave under a low rock overhang: a flat stone work area, dry birch wood, a pile of fluffy birch-bark tinder, the cold dead hearth visible behind, snow easing outside the mouth.",
    "CAVE_PAST_DAY": "Daytime inside the large Ice Age clan cave: soft daylight from the wide arched mouth, the mammoth-shaped stalagmite, bare rock walls with no handprints, a hearth fire burning red in the middle, sleeping beds of dry grass and furs.",
    "CAVE_MOUTH_MORNING": "Morning at the wide arched mouth of the Ice Age clan cave: the mammoth-shaped stalagmite inside, a flat earthen terrace where the clan gathers, the snowy valley and the icy stream below, pale sunlight.",
    "ICE_HOLES_PAST": "A frozen pool of the stream in the Ice Age valley under bright sun: several holes chopped through the thick clear ice, willow bushes on the bank, bundles of cut willow branches lying on the snow.",
    "CAVE_MOUTH_NOON": "High noon at the mouth of the Ice Age clan cave: hard bright sunlight on snow, short shadows, the clan gathered on the earthen terrace, the mammoth-shaped stalagmite inside.",
    "CAVE_MOUTH_MIST": "Early misty morning at the mouth of the Ice Age clan cave: thick white mist over the snowy valley below, cool grey-blue light, the mammoth-shaped stalagmite faint inside, an empty bed of furs just inside the entrance.",
    "PINE_FOREST_SNOW": "A snowy pine forest on the valley slope in the Ice Age, morning: deep fresh snow with a line of long-striding footprints, broken twigs, snow knocked off low branches, scattered grey boulders down the slope, shafts of cold sunlight through the trees.",
    "SINKHOLE": "A sinkhole in a snowy pine forest in the Ice Age at midday: a pit about three meters deep with steep walls of earth, rock and tangled roots, snow and collapsed earth at the bottom, a big pine tree right at the edge of the rim, slanting sunlight through the pines.",
    "RIVER_FLOOD_SIGNS": "The bank of the icy river in the Ice Age valley on a warm sunny afternoon under a clear blue sky: the water suddenly brown and muddy, racing fast, carrying broken chunks of ice and branches, gravel bars along the bank, the distant glacier tongue at the head of the valley.",
    "CAVE_PAST_LATE": "Late afternoon inside the large Ice Age clan cave: golden light through the wide arched mouth, the mammoth-shaped stalagmite, bare rock walls, the whole clan gathered around the hearth, and below the entrance the muddy river now loud, brown and high.",
    "CLIFF_NIGHT_FLOOD": "Moonlit night during a great flood in the Ice Age: a rock ledge in front of a small high cave on a limestone cliff, the clan huddled in furs with flickering torches, and far below a roaring brown flood full of ice chunks and broken trees surging through the valley toward the mouth of the lower cave.",
    "LOWER_CAVE_FLOOD": "Night inside the large lower Ice Age cave as it floods: muddy brown water pouring in through the wide mouth and spreading across the floor, the mammoth-shaped stalagmite, a dry rock ledge at chest height along the back wall, a beam of headlamp light in the dark, a braided hide rope hanging down the cliff above the entrance.",
    "ROCK_IN_FLOOD": "Moonlit night at the foot of the limestone cliff during the flood: the dry flat top of a tall boulder standing above churning brown water and drifting ice, the sheer wet cliff rising about six meters behind it, torchlight at the rim above, a braided hide rope hanging down the rock face.",
    "DAWN_AFTER_FLOOD": "Clear pink dawn after the flood, seen from the rock ledge high on the limestone cliff: the valley below covered in mud, stranded ice blocks and fallen trees, the river back in its bed, mist rising, snowy peaks glowing.",
    "CAVE_PAST_AFTER": "The large Ice Age clan cave the morning after the flood: mud and broken branches on the floor, a waterline stain along the lower walls, the mammoth-shaped stalagmite, the bare dry rock wall in the middle lit by a shaft of early sunlight, a freshly lit hearth, a large shell holding red-ochre powder and a hollow reed tube.",
    "RIVER_AFTER": "A dry grassy riverbank below the clan cave at midday after the flood: warm golden sunshine, the river running clear again, cracked dry mud, a reindeer-shaped target woven from dry grass standing on the bank.",
    "CAVE_PAST_HANDS": "Inside the large Ice Age clan cave on the seventh day: the mammoth-shaped stalagmite and, in the middle of the rock wall, two fresh red-ochre hand stencils side by side, a big hand and a slightly smaller hand, with bare rock around them; a hearth fire burning.",
    "CAVE_MOUTH_STORM_COMING": "Late afternoon at the mouth of the Ice Age clan cave: black storm clouds rolling over the snowy peaks, silent lightning in the distance, wind in the pines, warm firelight behind, and on the inner wall two red-ochre hand stencils.",
    "CAVE_PAST_STORM": "A storm at night inside the large Ice Age clan cave: white lightning flashing through the wide mouth onto the rock wall with two red-ochre hand stencils side by side and, beside them, a charcoal drawing of two stick figures holding hands, the mammoth-shaped stalagmite, a hearth fire, the clan standing back in the shadows.",
    "CAVE_TODAY_MORNING": "Early morning inside the same large limestone cave in the Pyrenees today after the storm: the mammoth-shaped stalagmite, the wall of hundreds of faded red-ochre hand stencils with one bigger hand in the middle and a slightly smaller hand right beside it, rescue ropes on the floor, flashlight beams in the dusty air, autumn forest beyond the mouth.",
    "PORCH_TODAY": "The wooden porch of a mountain chalet at the forest edge in the Pyrenees today, autumn evening at golden dusk: worn plank steps, golden leaves, a small fire in a stone ring on the lawn, a smartphone on a small tripod, rocky peaks glowing in the distance.",
    "CAVE_TODAY_DAY": "Daytime inside the same large limestone cave in the Pyrenees today: sunlight slanting through the wide arched mouth onto the mammoth-shaped stalagmite and the wall of hundreds of faded red-ochre hand stencils, the bigger hand in the middle with a smaller hand beside it, and next to them a faint old charcoal drawing of two stick figures holding hands, one with a small square box on its chest.",
    "CAVE_TWO_ERAS": "The same limestone cave with the mammoth-shaped stalagmite in two times: today in bright daylight with the wall of faded red hand stencils, and about twenty-seven thousand years ago at night, lit by a hearth fire with children of the clan sitting around it and two fresh red hand stencils on the wall.",
}

SCENE_SETTING = {1: "FOREST_TODAY", 2: "CHALET_NIGHT", 3: "CAVE_TODAY_STORM", 4: "VALLEY_PAST", 5: "SHELTER_PAST",
                 6: "STREAM_ROCK_PAST", 7: "CAVE_PAST_DUSK", 8: "ICE_STREAM_PAST", 9: "CAVE_PAST_BLIZZARD",
                 10: "CAVE_PAST_DAY", 11: "CAVE_MOUTH_MORNING", 12: "CAVE_PAST_NIGHT", 13: "CAVE_MOUTH_MIST",
                 14: "SINKHOLE", 15: "RIVER_FLOOD_SIGNS", 16: "CAVE_PAST_LATE", 17: "CLIFF_NIGHT_FLOOD",
                 18: "ROCK_IN_FLOOD", 19: "CAVE_PAST_AFTER", 20: "RIVER_AFTER", 21: "CAVE_PAST_STORM",
                 22: "CAVE_TODAY_MORNING", 23: "PORCH_TODAY", 24: "CAVE_TODAY_DAY"}
CLIP_SETTING = {"03.4": "STREAM_DAWN_PAST", "07.3": "CAVE_PAST_NIGHT", "07.4": "CAVE_PAST_NIGHT",
                "08.1": "VALLEY_PAST", "08.3": "CAVE_PAST_NIGHT", "08.4": "CAVE_PAST_NIGHT",
                "09.3": "CAVE_PAST_PREDAWN", "09.4": "CAVE_PAST_PREDAWN", "10.2": "ICE_STREAM_PAST",
                "10.4": "CAVE_PAST_NIGHT", "11.2": "ICE_HOLES_PAST", "11.3": "CAVE_MOUTH_NOON",
                "11.4": "ICE_HOLES_PAST", "13.2": "PINE_FOREST_SNOW", "13.3": "PINE_FOREST_SNOW",
                "13.4": "SINKHOLE", "17.2": "LOWER_CAVE_FLOOD", "17.4": "LOWER_CAVE_FLOOD",
                "18.4": "CLIFF_NIGHT_FLOOD", "19.1": "DAWN_AFTER_FLOOD", "20.3": "CAVE_PAST_HANDS",
                "20.4": "CAVE_MOUTH_STORM_COMING", "24.4": "CAVE_TWO_ERAS"}

# Trang phục đổi theo truyện (thay phần sau "; " cuối cùng của anchor).
LEO = {
    "DIRTY": "a dusty mud-streaked red softshell jacket over a grey fleece, muddy olive-green cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera",
    "CAPE": "a reindeer-hide cape with a grey fur collar over a dusty mud-streaked red softshell jacket, muddy olive-green cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera",
    "NO_BANDANA": "a reindeer-hide cape with a grey fur collar over a dusty mud-streaked red softshell jacket, muddy olive-green cargo trousers, brown hiking boots, no bandana on his wrists, a black chest harness holding a small square chest camera",
    "NO_CAMERA": "a reindeer-hide cape with a grey fur collar over a torn mud-stained red softshell jacket, muddy olive-green cargo trousers, brown hiking boots, an empty black chest harness with no camera",
    "CLEAN": "a plain navy knit sweater, dark jeans, brown hiking boots",
}
MIA = {
    "PAST": "a dusty teal down jacket, black hiking trousers, grey hiking boots, a cream knit beanie, a small red first-aid pouch on her belt",
    "CAPE": "a reindeer-hide cape with a grey fur collar over a dusty teal down jacket, black hiking trousers, grey hiking boots, a cream knit beanie, a small red first-aid pouch on her belt",
    "WET": "a reindeer-hide cape with a grey fur collar over a dusty teal down jacket, black hiking trousers soaked dark to the knees, wet grey hiking boots, a cream knit beanie",
    "HYPO": "wrapped in thick reindeer furs and a crinkled silver emergency blanket over a dusty teal down jacket, black hiking trousers, dry grey wool socks and no boots, a cream knit beanie",
    "NECKLACE": "a reindeer-hide cape with a grey fur collar over a dusty teal down jacket, black hiking trousers, grey hiking boots, a cream knit beanie, a necklace of pierced sea shells",
    "CLEAN": "a cream cable-knit sweater, dark jeans, grey hiking boots, a necklace of pierced sea shells",
}
ROAR_SPLINT = "a long-sleeved tunic of dark reindeer hide that fully covers his chest, fur-lined hide trousers, a necklace of animal teeth, a wooden spear-thrower at his belt, his left ankle splinted between two straight sticks bound with a red bandana, leaning on a wooden staff, fur-wrapped feet"
MOON_NO_HORN = "a long reindeer-hide cloak with a grey fur collar over a knee-length sewn hide tunic, a necklace of pierced sea shells, empty-handed with no horn, fur-wrapped feet"
MOON_NO_HORN_CLIPS = {"09.1", "17.1"}  # Pebble has the clan's fire horn in these moments
PEBBLE_STONE = "a small knee-length tunic of sewn hide with a fur hood covering both shoulders, hide leggings, a string of pierced snail shells around one wrist, a flat grey stone with a hole hanging on a leather cord on his chest, fur-wrapped feet"
INTERCUT = {"17.2", "24.4"}


def leo_outfit(key):
    if key < (4, 1):
        return None
    if key < (10, 2):
        return LEO["DIRTY"]
    if key < (14, 3):
        return LEO["CAPE"]
    if key < (18, 4):
        return LEO["NO_BANDANA"]
    if key[0] < 23:
        return LEO["NO_CAMERA"]
    return LEO["CLEAN"]


def mia_outfit(key):
    if key < (3, 4):
        return None
    if key < (10, 2):
        return MIA["PAST"]
    if key == (10, 3):
        return MIA["WET"]
    if key == (10, 4):
        return MIA["HYPO"]
    if key < (21, 1):
        return MIA["CAPE"]
    if key[0] < 23:
        return MIA["NECKLACE"]
    return MIA["CLEAN"]


def wardrobe(cid: str, chars: list[str]) -> dict:
    w = {}
    key = (int(cid[:2]), int(cid[3]))
    if "@Leo" in chars and leo_outfit(key):
        w["@Leo"] = leo_outfit(key)
    if "@Mia" in chars and mia_outfit(key):
        w["@Mia"] = mia_outfit(key)
    if "@Roar" in chars and (14, 3) <= key <= (21, 2):
        w["@Roar"] = ROAR_SPLINT
    if "@Moon" in chars and cid in MOON_NO_HORN_CLIPS:
        w["@Moon"] = MOON_NO_HORN
    if "@Pebble" in chars and key >= (20, 1):
        w["@Pebble"] = PEBBLE_STONE
    return w


def parse_outline() -> list[dict]:
    scenes, clip = [], None
    for line in (HERE / "DAN_Y.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## Cảnh (\d\d) · (.+?) — (.+)$", line)
        if m:
            scenes.append({"num": int(m.group(1)), "title": m.group(2), "time_label": m.group(3), "clips": []})
            continue
        m = re.match(r"^- \*\*Bối cảnh:\*\* (.+)$", line)
        if m and scenes:
            scenes[-1]["location"] = m.group(1)
            continue
        m = re.match(r"^- \*\*Clip (\d\d\.\d)\*\*", line)
        if m:
            clip = {"id": m.group(1), "turns": [], "_hinh": ""}
            scenes[-1]["clips"].append(clip)
            continue
        m = re.match(r"^  - \*Hình:\* (.+)$", line)
        if m and clip:
            clip["_hinh"] = m.group(1)
            continue
        m = re.match(r"^  - \*\*@(\w+)\*\* \(([^,)]+)(?:, ([^)]*))?\): (.+)$", line)
        if m and clip:
            clip["turns"].append({"speaker": "@" + m.group(1), "line": m.group(4), "pace": PACE[m.group(2).strip()],
                                  "_tone_vi": (m.group(3) or "").strip()})
    return scenes


def main():
    header = json.load(open(HERE / "header.json", encoding="utf-8"))
    scenes = parse_outline()
    over = []
    for sc in scenes:
        sc["setting"] = LOCKS[SCENE_SETTING[sc["num"]]]
        sc["_setting_key"] = SCENE_SETTING[sc["num"]]
        for c in sc["clips"]:
            c["chars"] = list(dict.fromkeys(t["speaker"] for t in c["turns"]))
            if c["id"] in CLIP_SETTING:
                c["setting"] = LOCKS[CLIP_SETTING[c["id"]]]
                c["_setting_key"] = CLIP_SETTING[c["id"]]
            if c["id"] in INTERCUT:
                c["intercut"] = True
            w = wardrobe(c["id"], c["chars"])
            if w:
                c["wardrobe"] = w
            # speech plan exactly as the builder computes it for a dialogue-only multi-shot clip
            probe = copy.deepcopy(c)
            probe.update({"steps": [""] * 15, "_dialogue_only": True})
            plan = B.speech_plan(header, probe, "cut", 15, clamp=False)
            c["_plan"] = [f"{sp} {a:.1f}–{b:.1f}s" for sp, _, a, b in plan]
            if plan[-1][3] > B.hard_end(15):
                over.append(f"{c['id']}: speech ends at {plan[-1][3]:.1f}s")
    parts = [scenes[0:6], scenes[6:12], scenes[12:18], scenes[18:24]]
    for k, part in enumerate(parts, 1):
        with open(HERE / f"skeleton_p{k}.json", "w", encoding="utf-8") as f:
            json.dump(part, f, ensure_ascii=False, indent=1)
    print(f"{sum(len(s['clips']) for s in scenes)} clips in {len(scenes)} scenes → skeleton_p1..4.json")
    print("\n".join(over) or "all speech plans end by 14.4s")


if __name__ == "__main__":
    main()
