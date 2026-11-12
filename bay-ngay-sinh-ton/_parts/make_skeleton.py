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
    "FOREST_TODAY": "Cúc Phương primeval forest in northern Vietnam today, late afternoon: giant old trees with huge buttress roots, thick lianas, ferns and mossy limestone boulders, green-gold sunlight slanting through the canopy, a narrow paved visitor road glimpsed through the leaves.",
    "GUESTHOUSE_NIGHT": "Night inside a wooden stilt-house guesthouse room at the edge of the forest: warm yellow lamp light, woven bamboo walls, a low wooden table with a small hotpot bubbling on a portable gas stove, a window where silent lightning flickers over dark limestone peaks.",
    "CAVE_TODAY_STORM": "Night inside a large limestone cave today during a raging storm: a wide arched mouth, a huge stalactite shaped like an elephant, a dry earthen floor, a rock wall covered with hundreds of faded red-ochre hand stencils with one bigger hand in the middle and a slightly smaller hand beside it, sheets of rain and white lightning beyond the entrance, light only from a headlamp.",
    "STREAM_DAWN_PAST": "Misty dawn on a sandy bank of a clear jungle stream at the foot of a towering limestone cliff, more than ten thousand years ago: untouched giant trees, reeds, smooth river stones, birdsong, no roads, no buildings, no people.",
    "VALLEY_PAST": "A pristine limestone valley in the Stone Age by morning: a clear stream winding between reed beds, giant primeval trees, sandy banks printed with large three-toed animal tracks, mist lifting off karst peaks, no roads, no buildings, no trash.",
    "JUNGLE_PAST": "Dense primeval jungle beside a stream at midday in the Stone Age: lianas as thick as a wrist hanging from giant trees, clumps of bamboo, wild banana plants, mossy rocks, dappled sunlight on a carpet of leaves.",
    "STREAM_ROCK_PAST": "A wide jungle stream in the Stone Age in afternoon light: a big flat-topped boulder in the middle of the current, thick reeds on the near bank, a dense forest edge about twenty meters away on the far bank, sun glare on the water.",
    "CAVE_PAST_DUSK": "A large limestone cave more than ten thousand years ago at dusk, home of a small Stone Age clan: a wide arched mouth, a huge stalactite shaped like an elephant, bare rock walls with no handprints or drawings, a hearth fire in the middle, hides drying on poles, rattan baskets of snails, sleeping beds of dry leaves, a stream running below the entrance.",
    "CAVE_PAST_NIGHT": "Night inside the large Stone Age clan cave: the elephant-shaped stalactite, bare rock walls with no handprints, a hearth fire glowing red, sleeping beds of dry leaves, hides on poles, deep shadows beyond the firelight.",
    "CAVE_PAST_DAY": "Daytime inside the large Stone Age clan cave: soft daylight from the wide arched mouth, the elephant-shaped stalactite, bare rock walls with no handprints, a hearth fire in the middle, rattan baskets of snails, sleeping beds of dry leaves.",
    "CAVE_PAST_RAIN_NIGHT": "A rainy night inside the large Stone Age clan cave: wind blows rain in through the wide arched mouth, the hearth is only wet grey ash with a thin thread of smoke, the elephant-shaped stalactite, bare rock walls, people huddled on beds of dry leaves.",
    "CAVE_PAST_PREDAWN": "Blue pre-dawn light in a dry corner of the Stone Age clan cave under a low rock overhang: a flat stone work area, split dry bamboo, a pile of fluffy tinder, the cold wet hearth visible behind, rain easing outside the mouth.",
    "SHALLOWS_PAST": "A shallow rocky stretch of the jungle stream in the Stone Age, morning: round pebbles, clear ankle-deep water, flat stones covered with small dark snails, a big boulder on the bank, sunlight sparkling.",
    "CAVE_MOUTH_MORNING": "Morning at the wide arched mouth of the Stone Age clan cave: the elephant-shaped stalactite above, a flat earthen terrace where the clan gathers, the jungle and the stream below, soft sunlight.",
    "STREAM_POOL_PAST": "A slow deep pool of the jungle stream in the Stone Age under bright sun: a bank of flat rocks, clumps of bamboo, split bamboo strips and a half-woven funnel-shaped fish trap lying on the stones.",
    "CAVE_MOUTH_NOON": "High noon at the mouth of the Stone Age clan cave: hard overhead sunlight, short shadows, the clan gathered on the earthen terrace, the elephant-shaped stalactite above.",
    "CAVE_MOUTH_MIST": "Early misty morning at the mouth of the Stone Age clan cave: thick white mist over the jungle below, cool grey-blue light, an empty bed of dry leaves just inside the entrance.",
    "JUNGLE_DEEP": "Deep primeval jungle in the Stone Age in the morning: damp earth with fresh footprints, broken twigs, leaves turned pale side up, giant trunks and hanging lianas, shafts of light through the canopy.",
    "SINKHOLE": "A limestone sinkhole in the primeval jungle at midday: a pit about four meters deep with steep mossy rock walls, ferns and reeds hanging over the rim, a big tree right at the edge, a shaft of sunlight reaching the soft earthen bottom.",
    "STREAM_FLOOD_SIGNS": "A jungle stream bank in the Stone Age in late afternoon: the water suddenly brown and fast, branches and leaves racing past, reed beds and big rocks along the bank, the sun still bright overhead while black clouds cover the distant headwater peaks.",
    "CAVE_PAST_LATE": "Late afternoon inside the large Stone Age clan cave: golden light through the wide arched mouth, the elephant-shaped stalactite, bare rock walls, the clan grilling fish over the hearth, the stream below the entrance now loud and brown.",
    "CLIFF_NIGHT_FLOOD": "Night during a flash flood in the Stone Age: a narrow ledge-cave high on a limestone cliff lit by flickering torches, heavy rain, and far below a roaring brown flood surging over the stream banks toward the mouth of the lower cave.",
    "LOWER_CAVE_FLOOD": "Night in the flooding lower Stone Age cave and the cliff face above it: brown water pouring in through the wide mouth and rising around stone pillars, the elephant-shaped stalactite, rain lashing the cliff where a vine rope hangs down from torchlight high above.",
    "ROCK_IN_FLOOD": "Night at the foot of the limestone cliff during the flood: the flat top of a huge boulder just above churning brown water, rain lashing, torchlight from a ledge-cave high above, a vine rope hanging down the wet rock face.",
    "DAWN_AFTER_FLOOD": "Clear golden dawn after the flood, seen from a ledge-cave high on the limestone cliff: the valley below covered in mud and fallen trees, the stream back in its bed, mist rising off the jungle.",
    "CAVE_PAST_AFTER": "The lower Stone Age cave the morning after the flood: wet mud on the floor, the elephant-shaped stalactite, the bare damp rock wall in soft daylight, a flat grinding stone with red-ochre powder and a hollow reed tube.",
    "STREAM_AFTER": "The jungle stream in the Stone Age at midday after the flood: the water clear again, a gravel bar with drying driftwood, a bundle of grass set up as a target, children of the clan playing on the stones.",
    "CAVE_PAST_HANDS": "The lower Stone Age cave on the seventh day: the elephant-shaped stalactite and, on the rock wall, two fresh red-ochre hand stencils side by side, a big hand and a slightly smaller hand, with bare rock around them; a hearth fire burning.",
    "CAVE_MOUTH_STORM_COMING": "Late afternoon at the mouth of the Stone Age clan cave: black storm clouds rolling over the karst peaks, distant thunder, wind in the jungle, warm firelight behind, and on the inner wall two red-ochre hand stencils.",
    "CAVE_PAST_STORM": "A storm at night inside the lower Stone Age cave: white lightning flashing through the wide mouth onto the rock wall with two red-ochre hand stencils side by side and a small charcoal stick figure, the elephant-shaped stalactite, a flickering hearth fire, the clan standing back in the shadows.",
    "CAVE_TODAY_MORNING": "Early morning inside the same large limestone cave today after the storm: the elephant-shaped stalactite, the wall of hundreds of faded red-ochre hand stencils with one bigger hand in the middle and a slightly smaller hand right beside it, rescue ropes on the floor, flashlight beams in the dusty air.",
    "PORCH_TODAY": "The wooden porch of a stilt-house guesthouse at the forest edge today in late afternoon: worn plank steps, potted plants, a smartphone on a small tripod, limestone peaks glowing in the distance.",
    "CAVE_TODAY_DAY": "Morning inside the same large limestone cave today: sunlight slanting through the wide arched mouth onto the elephant-shaped stalactite and the wall of hundreds of faded red-ochre hand stencils, the bigger hand in the middle with a smaller hand beside it and a faint charcoal stick figure wearing a square box on its chest.",
    "CAVE_TWO_ERAS": "The same limestone cave mouth with the elephant-shaped stalactite in two times: today in bright morning sun with the wall of faded red hand stencils, and more than ten thousand years ago at night, lit by a hearth fire with the clan sitting around it and two fresh red hand stencils on the wall.",
}

SCENE_SETTING = {1: "FOREST_TODAY", 2: "GUESTHOUSE_NIGHT", 3: "CAVE_TODAY_STORM", 4: "VALLEY_PAST", 5: "JUNGLE_PAST",
                 6: "STREAM_ROCK_PAST", 7: "CAVE_PAST_DUSK", 8: "SHALLOWS_PAST", 9: "CAVE_PAST_RAIN_NIGHT",
                 10: "CAVE_PAST_DAY", 11: "CAVE_MOUTH_MORNING", 12: "CAVE_PAST_NIGHT", 13: "CAVE_MOUTH_MIST",
                 14: "SINKHOLE", 15: "STREAM_FLOOD_SIGNS", 16: "CAVE_PAST_LATE", 17: "CLIFF_NIGHT_FLOOD",
                 18: "ROCK_IN_FLOOD", 19: "CAVE_PAST_AFTER", 20: "STREAM_AFTER", 21: "CAVE_PAST_STORM",
                 22: "CAVE_TODAY_MORNING", 23: "PORCH_TODAY", 24: "CAVE_TODAY_DAY"}
CLIP_SETTING = {"03.4": "STREAM_DAWN_PAST", "07.4": "CAVE_PAST_NIGHT", "08.3": "CAVE_PAST_DAY", "08.4": "CAVE_PAST_DAY",
                "09.3": "CAVE_PAST_PREDAWN", "09.4": "CAVE_PAST_PREDAWN", "10.4": "CAVE_PAST_NIGHT",
                "11.2": "STREAM_POOL_PAST", "11.3": "CAVE_MOUTH_NOON", "11.4": "STREAM_POOL_PAST",
                "13.3": "JUNGLE_DEEP", "13.4": "SINKHOLE", "17.2": "LOWER_CAVE_FLOOD", "17.4": "LOWER_CAVE_FLOOD",
                "18.4": "CLIFF_NIGHT_FLOOD", "19.1": "DAWN_AFTER_FLOOD", "20.3": "CAVE_PAST_HANDS",
                "20.4": "CAVE_MOUTH_STORM_COMING", "24.4": "CAVE_TWO_ERAS"}

# Trang phục đổi theo truyện (thay phần cuối "; " của anchor).
KHANG = {
    "DIRTY": "dusty sweat-stained olive-green tactical shirt with rolled sleeves, khaki cargo trousers muddy at the knees, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera",
    "NO_BANDANA": "dusty sweat-stained olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, a black chest harness holding a small square chest camera, no bandana",
    "NO_CAMERA": "dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera",
    "NECKLACE": "dirty torn olive-green tactical shirt with rolled sleeves, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera, a necklace of small stream-snail shells",
    "RETURN": "torn mud-stained olive-green tactical shirt, muddy khaki cargo trousers, brown hiking boots, an empty black chest harness with no camera, a necklace of small stream-snail shells",
    "CLEAN": "plain grey cotton T-shirt, khaki cargo trousers, brown hiking boots, a necklace of small stream-snail shells",
}
ROAR_SPLINT = "a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, his left ankle splinted between two straight sticks bound with a red bandana, leaning on a wooden staff, barefoot"
MOON_NO_TUBE = "a long dark hide cloak over a knee-length bark-cloth tunic, empty-handed with no bamboo tube, barefoot"
MOON_NO_TUBE_CLIPS = {"09.1", "17.1", "18.4"}  # Snail holds the clan's fire tube in these moments
INTERCUT = {"17.2", "24.4"}
STREAM_NO_NECKLACE = "a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, no necklace, a woven rattan basket on her back, barefoot"


def khang_outfit(cid: str):
    s, k = int(cid[:2]), int(cid[3])
    key = (s, k)
    if key < (5, 1):
        return None
    if key < (14, 2):
        return KHANG["DIRTY"]
    if key < (18, 4):
        return KHANG["NO_BANDANA"]
    if key < (21, 3):
        return KHANG["NO_CAMERA"]
    if s < 22:
        return KHANG["NECKLACE"]
    return KHANG["RETURN"] if s == 22 else KHANG["CLEAN"]


def wardrobe(cid: str, chars: list[str]) -> dict:
    w = {}
    s, k = int(cid[:2]), int(cid[3])
    if "@Khang" in chars and khang_outfit(cid):
        w["@Khang"] = khang_outfit(cid)
    if "@Roar" in chars and (14, 3) <= (s, k) <= (20, 4):
        w["@Roar"] = ROAR_SPLINT
    if "@Stream" in chars and (s, k) >= (21, 3):
        w["@Stream"] = STREAM_NO_NECKLACE
    if "@Moon" in chars and cid in MOON_NO_TUBE_CLIPS:
        w["@Moon"] = MOON_NO_TUBE
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
