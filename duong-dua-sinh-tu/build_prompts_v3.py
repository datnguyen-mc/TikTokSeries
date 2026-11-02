#!/usr/bin/env python3
"""Compile the 240-shot (40-minute) action film plan using the 10-Stage Google Flow Omni Pipeline:
GLOBAL_FILM_BIBLE -> SCENE_CONTEXT -> ENTITY_AND_OBJECT_STATE -> SHOT_TYPE_SELECTION ->
CAMERA_AND_ACTION_PLANNING -> DIALOGUE_AND_AUDIO_PLANNING -> REFERENCE_SELECTION ->
MODEL_SPECIFIC_PROMPT_COMPILATION -> AUTOMATED_VALIDATION -> FINAL_VIDEO_PROMPT.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from uuid import UUID

from film_bible import (
    CHARACTER_LOCK,
    ENVIRONMENT_LOCK,
    GLOBAL_FILM_BIBLE,
    OBJECT_LOCK,
    OMNI_MODEL_CAPABILITIES,
    PHYSICS_RULES,
    VEHICLE_LOCK,
    select_relevant_bible_slice,
)

BASE_DIR = Path(__file__).resolve().parent
CAMERAS = {
    'W': '35mm wide shot at human eye level, subject already moving at 0.0s. Preserve readable geography and screen direction.',
    'M': '50mm medium shot at eye level. Gesture, reaction and dialogue play in the same composition without quiet pause.',
    'C': '85mm close-up at eye level, natural shallow depth of field. Readable facial micro-expressions and natural lip sync, no orbit.',
    'I': '85mm mechanical/object detail insert shot. The featured vehicle mechanism or object moves decisively from 0.0s and stays spatially readable without forcing visible characters into frame.',
    'T': '35mm lateral tracking shot moving with the subject in the established direction. No whip pan, drone move or reverse-axis cut.',
    'H': '35mm controlled handheld medium-wide with kinetic energy. Keep the entire defensive action readable from one side of the axis.',
    'O': '50mm over-shoulder or point-of-view composition from the observer specified in the opening frame. Keep eyelines matched.',
    'P': '50mm steady, purposeful straight push-in, no lens change, no orbit. Tension builds while the final expression stays readable.',
    'E': '24mm wide-angle cinematic opening move: one smooth continuous low-angle lateral track pacing the moving vehicle along the established road axis with natural speed and parallax. No drone, no whip pan, no cut.',
}
SHUTTER = {'H': 'Crisp 150-degree shutter for sharp action'}
CLEAN_FRAME = ('Clean cinematic frame, never TV footage: no TV channel or broadcaster logo in any corner, no watermark, '
               'news ticker, lower-third, LIVE/REC badge, timestamp or other on-screen graphics. Screens and phones in the '
               'story never show a TV channel, news programme or broadcaster branding; story emblems stay simple unreadable shapes; '
               'handwriting, printed pages, signatures and screens in the story stay unreadable at this distance.')
BODY_STANDARD = ('Body mechanics: to pick something up from low down a person bends at the knees and hips with a visible reach, closes the stated '
                 'hand fully around it and lifts its real weight; objects never float, slide into a hand by themselves or pass through fingers; '
                 'when no hand is named the free hand acts and every carried prop stays in its established hand; in a hand-over both hands stay '
                 'visible until the receiver\'s fingers close; feet never slide; every hand keeps five natural fingers.')
FACE_STANDARD = ('Face and eyes: every visible named face stays faithful to its reference throughout the shot (eye shape and spacing, eyelids, nose bridge and tip, lips, '
                 'jaw, ears) and stays stable while turning or moving; identity marks stay exactly in place; natural blinks every few seconds, '
                 'both eyes together on the stated eyeline, no fixed gaze, no rolling or crossed eyes, tears only when written; '
                 'natural skin pores and a subtle chest and nostril movement with each breath. Never flash or cut to the standalone studio reference portrait sheet.')
VOICE_LABELS = {
    'RADIO': 'the radio voice',
    'EXTRA': 'the background speaker',
    'OFFICER': 'the assisting officer',
    'RYH': 'Ryh the shop owner',
    'TOHE': 'Tohe the race organizer',
    'INWE': 'Inwe the street racer',
    'DANNY': 'Danny the street racer',
    'FATHER': 'Ny Tran\'s father',
}
BROADCAST_WORDS = re.compile(r'\b(TV|television|broadcast\w*|newscast|news|tivi|truyền hình|thời sự|bản tin|phóng viên|báo đài)\b', re.I)
MAX_CLIP_SYLLABLES = 30
BEATS = re.compile(r'^Beat 1 \(0\.0–(\d+(?:\.\d)?)s\): .+ Beat 2 \(\1–(\d+(?:\.\d)?)s\): .+ Beat 3 \(\2–10\.0s\): .+$', re.S)
TRANSITIONS = {
    'OPEN': 'Cắt thiết lập thời gian/không gian',
    'CUT': 'Cắt dựng đúng vị trí/ánh nhìn',
    'CONTINUE': 'Nối đúng frame, hành động tiếp diễn',
    'MATCH': 'Match cut hình dạng/tư thế, không morph',
    'J': 'J-cut: âm mới đến trước hình',
    'L': 'L-cut: âm cũ đi qua cú cắt',
}
GENERIC_VOICES = {
    'RADIO': 'Radio dispatcher: concise Southern Vietnamese voice through tactical radio compression, off screen.',
    'EXTRA': 'The unnamed background person specified by the action: natural Southern Vietnamese voice, no new named lead character.',
    'OFFICER': 'Unnamed assisting officer: composed Southern Vietnamese voice, no new named lead character.',
    'RYH': 'Ryh, veteran garage owner: gruff, warm middle-aged Southern Vietnamese male voice.',
    'TOHE': 'Tohe, street race organizer: energetic, resonant Southern Vietnamese male voice.',
    'INWE': 'Inwe, rival street racer: confident Southern Vietnamese male voice.',
    'DANNY': 'Danny, rival street racer: sharp, cocky Southern Vietnamese male voice.',
    'FATHER': 'Elderly father in the courtyard: indignant elderly Southern Vietnamese male voice.',
    'NARRATOR': 'Narrator: an outside storyteller who is NOT a character in the film: one consistent mature Southern Vietnamese woman\'s voice, calm, low and warm, speaking about the person in the third person, used only to introduce a lead at first appearance. Every mouth in frame stays closed while she speaks; never lip-sync her words to anyone on screen.',
}
MAX_SYLLABLES_PER_SECOND = 4.5
NARRATOR_SYLLABLES_PER_SECOND = 3.8
LEAD_NAMES = r'(Tom|Micdo|Ami|Cevin|Cina|Seja|Onle|Ny Tran|Cela|Nese|Kinan|Verni)'
DUPLICATE_CHAR_PAIR = re.compile(rf'\b{LEAD_NAMES}\s+and\s+\1\b|\b{LEAD_NAMES}\b[^.;]*\beyes\s+(?:fixed|locked)\s+on\s+\2\b', re.I)
ADJACENT_LEAD_NAMES = re.compile(rf'\b{LEAD_NAMES}\s+{LEAD_NAMES}\b')
DOUBLE_ARTICLE_OR_RAW_LENS = re.compile(r'\bthe\s+moving\s+the\b|\bthe\s+the\b|\bin\s+the\s+[A-Z]\s+lens\s+geometry\b', re.I)
BOILERPLATE_INTENT = re.compile(r'Drive the dramatic momentum of Scene', re.I)
DRIVER_OUTSIDE_MOVING_VEHICLE = re.compile(r'positioned in the primary foreground plane beside the (?:rig 18|civic trio|eclipse|rx7|charger|supra)', re.I)
STOPPING_CAMERA_IN_PURSUIT = re.compile(r'decelerates with it and settles at eye level as it stops', re.I)
SELF_INTRO = re.compile(rf'\b(tôi|tui|tao|em|con|mình)\s+(là|tên)\s+{LEAD_NAMES}\b|\btên (tôi|tui|tao|em|con) là\b', re.I)
FIRST_PERSON = re.compile(r'\b(tôi|tui|tao|em|mình|ta)\b', re.I)
DETAIL_FIELDS = ('intent', 'composition', 'blocking', 'performance', 'focus', 'texture', 'sound_detail', 'rhythm')
DRAMA_FIELDS = ('dramatic_question_vi', 'turn_vi', 'hook_vi', 'payoff_or_setup_vi', 'tension')


def select_shot_references(plan: dict, c: dict) -> list[str]:
    """Stage 7 (Reference Selection): return ordered unique media_ids for visible characters and picture-only refs."""
    if c.get('camera') == 'I' and not c.get('characters') and not c.get('image_references'):
        return []
    mids = []
    for look_key in c.get('characters', []):
        base = base_key(plan, look_key)
        mid = plan['identities'][base]['media_id']
        if mid not in mids:
            mids.append(mid)
    for pic_key in c.get('image_references', []):
        mid = plan['identities'][pic_key]['media_id']
        if mid not in mids:
            mids.append(mid)
    return mids[:OMNI_MODEL_CAPABILITIES['ingredients']['max_references']]


def determine_omni_workflow(plan: dict, c: dict) -> str:
    """Stage 8 (Model Capability Mapping): 16:9 YouTube films cut continuously between shots and always use Ingredients R2V or Text-to-Video, never last-frame injection."""
    if c.get('workflow_override') in OMNI_MODEL_CAPABILITIES:
        return c['workflow_override']
    if c.get('camera') == 'I' and not c.get('characters') and not c.get('image_references'):
        return 'insert'
    if c.get('characters') or c.get('image_references'):
        return 'ingredients'
    return 'text'


def auto_repair_shot(plan: dict, c: dict, previous: dict | None = None) -> dict:
    """Stage 9a: Automatically repair safe, unambiguous prompt-generation formatting issues without altering screenplay intent."""
    repaired = copy.deepcopy(c)
    # 1. Deduplicate identical look keys while preserving order
    if repaired.get('characters'):
        repaired['characters'] = list(dict.fromkeys(repaired['characters']))
    # 2. If a detail/insert shot (`camera == 'I'`) has no visible characters, any `on` dialogue must be `off` screen
    if repaired.get('camera') == 'I' and not repaired.get('characters'):
        for d in repaired.get('dialogue', []):
            if d.get('mode') == 'on':
                d['mode'] = 'off'
    # 3. Repair accidental duplicate character pairs ('X and X') or driver-outside-moving-vehicle phrasing
    dup_and = re.compile(rf'\b{LEAD_NAMES}\s+and\s+\1\b', re.I)
    for field in ('start_frame', 'action', 'end_frame'):
        if isinstance(repaired.get(field), str):
            repaired[field] = dup_and.sub(r'\1', repaired[field])
            repaired[field] = DRIVER_OUTSIDE_MOVING_VEHICLE.sub(
                lambda m: m.group(0).replace('positioned in the primary foreground plane beside', 'seated inside the left-hand driver cockpit of'),
                repaired[field],
            )
    if isinstance(repaired.get('cinematic'), dict):
        for k, v in list(repaired['cinematic'].items()):
            if isinstance(v, str):
                repaired['cinematic'][k] = dup_and.sub(r'\1', v)
    return repaired


def edition(plan: dict) -> str:
    return '3.1' if plan.get('editorial_revision') == '3.1' else '3'


def syllables(text: str) -> int:
    """Vietnamese writes one syllable per space-separated word; punctuation is not spoken."""
    return len(re.findall(r'[^\W\d_]+', text))


def clip_id(scene: int, clip: int) -> str:
    return f'{scene:02d}.{clip}'


def ref(item: dict) -> str:
    return f"canh-{item['scene']:02d}/clip-{item['number']}.md"


def clock(seconds: int) -> str:
    return f'{seconds // 60:02d}:{seconds % 60:02d}'


def base_key(plan: dict, key: str) -> str:
    return plan['looks'][key][0]


def normalize(plan: dict) -> list[dict]:
    """Resolve explicit '=' handoff markers, retaining the source reference."""
    shots = []
    for scene in plan['scenes']:
        for original in scene['clips']:
            c = copy.deepcopy(original)
            c['scene'] = scene['number']
            c['id'] = clip_id(c['scene'], c['number'])
            c['story_time'] = c.get('story_time', scene['story_time'])
            c['previous'] = shots[-1]['id'] if shots else None
            if c['start_frame'] == '=':
                if not shots:
                    raise ValueError('First shot cannot inherit a missing frame')
                c['start_frame'] = shots[-1]['end_frame']
            shots.append(c)
    return shots


def first_appearances(plan: dict, shots: list[dict]) -> dict[str, str]:
    """Clip id where each lead identity is first visible; the narrator introduces them there."""
    first = {}
    for c in shots:
        for k in c['characters']:
            first.setdefault(base_key(plan, k), c['id'])
    return first


def validate(plan: dict, shots: list[dict]) -> None:
    errors = []
    if not plan.get('narrator', {}).get('voice'):
        errors.append('The narrator needs one locked voice description')
    if plan.get('schema_version') != 3 or plan.get('aspect_ratio') != '16:9':
        errors.append('Expected schema 3 and full-frame 16:9')
    if [s['number'] for s in plan['scenes']] != list(range(1, 41)):
        errors.append('Scenes must be exactly 01–40 in order')
    if len(plan['identities']) != 12:
        errors.append('Keep the twelve approved lead identities')
    for identity in plan['identities'].values():
        try:
            UUID(identity['media_id'])
        except (ValueError, KeyError):
            errors.append('Invalid reference UUID')
    for s in plan['scenes']:
        if [c['number'] for c in s['clips']] != list(range(1, 7)):
            errors.append(f"Scene {s['number']} needs six ordered clips")
        if edition(plan) == '3.1':
            drama = s.get('dramaturgy', {})
            if any(k not in drama for k in DRAMA_FIELDS):
                errors.append(f"Scene {s['number']}: missing dramatic progression")
            if not isinstance(drama.get('tension'), int) or not 1 <= drama.get('tension', 0) <= 5:
                errors.append(f"Scene {s['number']}: tension must be an editorial level from 1 to 5")
    seen_actions = {}
    seen_lines = {}
    for i, c in enumerate(shots):
        p = shots[i - 1] if i else None
        if edition(plan) == '3.1':
            detail = c.get('cinematic', {})
            if any(not isinstance(detail.get(k), str) or len(detail[k].strip()) < 12 for k in DETAIL_FIELDS):
                errors.append(f"{c['id']}: incomplete specific directing detail")
            words = sum(len(detail.get(k, '').split()) for k in DETAIL_FIELDS)
            if not 55 <= words <= 280:
                errors.append(f"{c['id']}: directing detail must be useful and bounded, got {words} words")
            beats = BEATS.match(c['action'])
            if not beats or not 0 < float(beats[1]) < float(beats[2]) < 10:
                errors.append(f"{c['id']}: action needs three timed beats chaining 0.0s to 10.0s")
            blocking = detail.get('blocking', '').strip().rstrip('.')
            if blocking and blocking in c['action']:
                errors.append(f"{c['id']}: blocking note replayed inside the action")
        if any(k in frame for frame in (c['start_frame'], c['end_frame']) for k in ('Final physical lock', 'Framing:')):
            errors.append(f"{c['id']}: start/end frame must be a state, not an action or camera note")
        written = [
            c['start_frame'], c['action'], c['end_frame'], c['lighting'], c.get('wardrobe_note', ''),
            *c.get('cinematic', {}).values(), *(d['text'] for d in c['dialogue'])
        ]
        if any(BROADCAST_WORDS.search(t) for t in written):
            errors.append(f"{c['id']}: TV/news wording invites a broadcaster logo or news graphics")
        if any(DUPLICATE_CHAR_PAIR.search(t) for t in written):
            errors.append(f"{c['id']}: duplicate character reference (e.g. 'X and X' or 'X eyes fixed on X')")
        if any(ADJACENT_LEAD_NAMES.search(t) for t in (c['start_frame'], c['action'], c['end_frame'], *c.get('cinematic', {}).values())):
            errors.append(f"{c['id']}: adjacent lead character names (e.g. 'Tom Tom' or 'Cevin Verni')")
        if any(DOUBLE_ARTICLE_OR_RAW_LENS.search(t) for t in (c['start_frame'], c['action'], c['end_frame'], *c.get('cinematic', {}).values())):
            errors.append(f"{c['id']}: double article ('the moving the' / 'the the') or raw single-letter lens code")
        if BOILERPLATE_INTENT.search(c.get('cinematic', {}).get('intent', '')):
            errors.append(f"{c['id']}: generic boilerplate dramatic intent")
        if c['location'] in ('HIGHWAY_NIGHT', 'RIG_CABIN', 'RACE_COCKPIT', 'LA_HILLS_ROAD', 'RAIL_CROSSING'):
            if any(DRIVER_OUTSIDE_MOVING_VEHICLE.search(t) for t in (c['start_frame'], c['action'], c['end_frame'])):
                errors.append(f"{c['id']}: driver described as outside/beside a moving highway/cockpit vehicle")
            if STOPPING_CAMERA_IN_PURSUIT.search(CAMERAS.get(c['camera'], '')):
                errors.append(f"{c['id']}: camera movement decelerating to a stop contradicts high-speed vehicle pursuit")
        if c['camera'] == 'I' and any(d['mode'] == 'on' for d in c['dialogue']):
            errors.append(f"{c['id']}: detail/insert shot (I) cannot require visible on-screen lip sync")
        wf = determine_omni_workflow(plan, c)
        cap = OMNI_MODEL_CAPABILITIES.get(wf)
        if not cap:
            errors.append(f"{c['id']}: unsupported Omni workflow {wf}")
        else:
            refs = select_shot_references(plan, c)
            if len(refs) > cap['max_references'] and wf == 'ingredients':
                errors.append(f"{c['id']}: exceeds max_references ({cap['max_references']}) for {wf}")
        if c['location'] not in plan['locations'] or c['camera'] not in CAMERAS:
            errors.append(f"{c['id']}: unknown location/camera")
        if c['transition'] not in TRANSITIONS:
            errors.append(f"{c['id']}: unknown transition")
        if c['number'] == 1 and c['transition'] == 'CONTINUE':
            errors.append(f"{c['id']}: scene entry must be an explicit editorial cut")
        for k in c['characters']:
            if k not in plan['looks']:
                errors.append(f"{c['id']}: unknown appearance {k}")
        if len({base_key(plan, k) for k in c['characters']}) != len(c['characters']):
            errors.append(f"{c['id']}: duplicate identity with two appearances")
        for k in c['props']:
            if k not in plan['props']:
                errors.append(f"{c['id']}: unknown prop {k}")
        for k in c.get('image_references', []):
            if k not in plan['identities']:
                errors.append(f"{c['id']}: unknown photograph identity {k}")
        if c['transition'] == 'CONTINUE':
            if not p or any(c[k] != p[k] for k in ('location', 'camera', 'story_time')):
                errors.append(f"{c['id']}: continuous shot changes location/camera/time")
            if p and c['start_frame'] != p['end_frame']:
                errors.append(f"{c['id']}: broken exact-frame handoff")
            if p and set(c['characters']) != set(p['characters']):
                errors.append(f"{c['id']}: new appearance needs a fresh reference cut")
        action = re.sub(r'\W+', ' ', c['action'].casefold()).strip()
        if action in seen_actions:
            errors.append(f"{c['id']}: action repeats {seen_actions[action]}")
        seen_actions[action] = c['id']
        cast_turns = [d for d in c['dialogue'] if d['speaker'] != 'NARRATOR']
        if not 1 <= len(c['dialogue']) or len(cast_turns) > 2 or len(c['dialogue']) - len(cast_turns) > 1:
            errors.append(f"{c['id']}: expected 1 or 2 dialogue turns, plus at most one narrator introduction")
        if sum(syllables(d['text']) for d in c['dialogue']) > MAX_CLIP_SYLLABLES:
            errors.append(f"{c['id']}: over {MAX_CLIP_SYLLABLES} spoken syllables in one 10 s take")
        spoken_until = 0.0
        for d in c['dialogue']:
            if '@' in d['text'] or '"' in d['text']:
                errors.append(f"{c['id']}: spoken text contains injected tag/quote")
            if ':' in d['text']:
                errors.append(f"{c['id']}: a colon inside a line cuts what the model reads aloud")
            if SELF_INTRO.search(d['text']):
                errors.append(f"{c['id']}: a character introduces themselves; leave introductions to the narrator")
            if d['speaker'] == 'NARRATOR' and FIRST_PERSON.search(d['text']):
                errors.append(f"{c['id']}: the narrator speaks in the third person, never as the character")
            if d['mode'] not in ('on', 'off', 'vo', 'device') or (d['speaker'] == 'NARRATOR' and d['mode'] != 'vo'):
                errors.append(f"{c['id']}: unknown voice mode")
            if syllables(d['text']) < 3:
                errors.append(f"{c['id']}: line too short to carry a beat")
            at = d.get('at')
            if not (isinstance(at, list) and len(at) == 2 and 0.2 <= at[0] < at[1] <= 9.8):
                errors.append(f"{c['id']}: every line needs an 'at' window inside 0.2–9.8s so Omni never clips its tail")
            else:
                if at[0] < spoken_until:
                    errors.append(f"{c['id']}: dialogue windows overlap or run out of order")
                if syllables(d['text']) / (at[1] - at[0]) > MAX_SYLLABLES_PER_SECOND:
                    errors.append(f"{c['id']}: line spoken faster than {MAX_SYLLABLES_PER_SECOND} syllables per second")
                if d['speaker'] == 'NARRATOR' and syllables(d['text']) / (at[1] - at[0]) > NARRATOR_SYLLABLES_PER_SECOND + 1e-9:
                    errors.append(f"{c['id']}: the locked narrator voice speaks at most {NARRATOR_SYLLABLES_PER_SECOND} syllables per second")
                spoken_until = at[1]
            spoken = re.sub(r'\W+', ' ', d['text'].casefold()).strip()
            if spoken in seen_lines:
                errors.append(f"{c['id']}: exact line repeats {seen_lines[spoken]}")
            seen_lines[spoken] = c['id']
            speaker = d['speaker']
            if speaker not in plan['looks'] and speaker not in GENERIC_VOICES:
                errors.append(f"{c['id']}: missing speaker identity")
            if d['mode'] == 'device' and speaker in plan['looks'] and \
                    base_key(plan, speaker) in {base_key(plan, k) for k in c['characters']}:
                errors.append(f"{c['id']}: a speaker in frame talks on screen (on/off), not as a device voice")
            if d['mode'] == 'on' and speaker in plan['looks']:
                visible = {base_key(plan, k) for k in c['characters']}
                if base_key(plan, speaker) not in visible:
                    errors.append(f"{c['id']}: visible speaker missing from cast")
    if len(shots) != 240 or len(shots) * plan['clip_seconds'] != 2400:
        errors.append('Expected 240 ten-second production clips (40 minutes)')
    first = first_appearances(plan, shots)
    introduced = set()
    for c in shots:
        for d in c['dialogue']:
            if d['speaker'] != 'NARRATOR':
                continue
            named = {b for b, cid in first.items() if cid == c['id'] and plan['identities'][b]['name'].casefold() in d['text'].casefold()}
            if not named:
                errors.append(f"{c['id']}: the narrator only introduces a lead at their first appearance")
            introduced |= named
    for b, cid in first.items():
        if b not in introduced:
            errors.append(f"{cid}: {plan['identities'][b]['name']} first appears without a narrator introduction")
    if errors:
        raise ValueError('\n'.join(errors))


def person_lock(plan: dict, key: str, c: dict) -> str:
    base, age, outfit = plan['looks'][key]
    identity = plan['identities'][base]
    face = identity['identity']
    return f"{identity['tag']} = {identity['name']}: same approved identity, age {age}; {face}. {outfit}. Voice: {identity['voice']}."


def dialogue_text(plan: dict, d: dict) -> str:
    if d['speaker'] in plan['looks']:
        identity = plan['identities'][base_key(plan, d['speaker'])]
        speaker = f"{identity['name']} ({identity['tag']})" if d['mode'] == 'on' else identity['name']
    else:
        speaker = {
            'RADIO': 'Bộ đàm',
            'EXTRA': 'Người trong cảnh',
            'OFFICER': 'Cán bộ hỗ trợ',
            'RYH': 'Ông chủ Ryh',
            'TOHE': 'Tohe (Tổ chức đua)',
            'INWE': 'Tay đua Inwe',
            'DANNY': 'Tay đua Danny',
            'FATHER': 'Bố của Ny Tran',
            'NARRATOR': 'Người dẫn chuyện',
        }[d['speaker']]
    mode = {'on': 'nói trong hình', 'off': 'ngoài khung hình', 'vo': 'lời dẫn ngoài hình', 'device': 'qua thiết bị'}[d['mode']]
    if d['speaker'] == 'NARRATOR':
        mode = 'giọng kể ngoài truyện, không phải nhân vật trong hình'
    start, end = d['at']
    return f"{start:.1f}–{end:.1f}s · {speaker}, {mode}: {d['text']}"


def mouth_map(plan: dict, c: dict) -> str:
    """Who may move their lips, and exactly when; every other mouth stays closed."""
    parts = []
    for d in c['dialogue']:
        a, b = d['at']
        if d['speaker'] == 'NARRATOR':
            parts.append(f'{a:.1f}–{b:.1f}s the narrator, off screen: every mouth in frame stays closed')
            continue
        name = (plan['identities'][base_key(plan, d['speaker'])]['name'] if d['speaker'] in plan['looks']
                else VOICE_LABELS[d['speaker']])
        parts.append({
            'on': f"{a:.1f}–{b:.1f}s only {name}'s lips move, shaping each Vietnamese syllable in sync with the voice, natural jaw and teeth, mouth closing as the line ends",
            'vo': f"{a:.1f}–{b:.1f}s {name}'s inner voice-over: every mouth in frame stays closed, {name}'s too",
            'off': f'{a:.1f}–{b:.1f}s {name} heard off screen: no visible mouth moves',
            'device': f'{a:.1f}–{b:.1f}s {name} through the device: no visible mouth moves',
        }[d['mode']])
    if not parts:
        return 'Mouth map: nobody speaks; every mouth in frame stays closed or relaxed.'
    return 'Mouth map: ' + '; '.join(parts) + '. Outside these windows every mouth in frame is closed or relaxed and listeners never mouth along.'


def spoken_line(plan: dict, d: dict) -> str:
    """Prompt form of a turn for Omni: English label and locked voice, the Vietnamese words after the last colon."""
    start, end = d['at']
    if d['speaker'] == 'NARRATOR':
        label = 'Narrator, off screen and not a character, in the locked narrator voice'
    elif d['speaker'] in plan['looks']:
        identity = plan['identities'][base_key(plan, d['speaker'])]
        how = {'on': 'says on screen', 'off': 'speaks off screen', 'vo': 'inner voice-over, mouth closed', 'device': 'through the device'}[d['mode']]
        label = f"{identity['name']} ({identity['tag']}) {how}, in the {identity['voice']}"
    else:
        label = {
            'RADIO': 'Radio voice through the handset',
            'EXTRA': 'The background speaker named in the action',
            'OFFICER': 'The assisting officer',
            'RYH': 'Ryh the shop owner',
            'TOHE': 'Tohe the race organizer',
            'INWE': 'Inwe the rival street racer',
            'DANNY': 'Danny the rival street racer',
            'FATHER': 'Elderly father in the courtyard',
        }[d['speaker']]
        label += {'on': ', on screen', 'off': ', off screen', 'vo': ', voice-over', 'device': ''}[d['mode']]
    return f"{start:.1f}–{end:.1f}s · {label}: {d['text']}"


def voice_block(plan: dict, c: dict) -> str:
    if not c['dialogue']:
        return 'No speech, narration or improvised vocal filler. Play the action and location sound.'
    modes = {d['mode'] for d in c['dialogue']}
    rendering = ' '.join(x for m, x in (
        ('vo', 'Voice-overs stay dry and close.'),
        ('off', 'Off-screen voices never add a face to the shot.'),
        ('device', "Device voices never add the caller's body to the shot.")
    ) if m in modes)
    prefixes = [plan['narrator']['voice'] if d['speaker'] == 'NARRATOR' else GENERIC_VOICES[d['speaker']]
                for d in c['dialogue'] if d['speaker'] in GENERIC_VOICES]
    prefix_block = ('\n'.join(dict.fromkeys(prefixes)) + '\n') if prefixes else ''
    lines_block = '\n'.join(spoken_line(plan, d) for d in c['dialogue'])
    timing = ('Each line is timed to its ACTION beat: speak it only inside its own seconds window, at a natural '
              'Southern Vietnamese pace with clear diction, while that beat\'s movement happens; lines never overlap '
              'and the picture never waits for speech.')
    return (
        f"{timing} {rendering}".rstrip() + "\n"
        f"{prefix_block}{lines_block}\n"
        f"Only words after the final colon are spoken. Never read names, tags or directions. No captions."
    )


def prop_detail(plan: dict, key: str, c: dict) -> str:
    scene_num = c.get('scene', 1)
    clip_num = c.get('number', 1)
    v_states = (c.get('entity_state') or {}).get('vehicles') or {}
    o_states = (c.get('entity_state') or {}).get('objects') or {}
    if key in VEHICLE_LOCK:
        v = VEHICLE_LOCK[key]
        cond = v_states.get(key) or 'intact operational condition'
        return (
            f"{plan['props'][key]} [VEHICLE_LOCK {key}: {v['exterior_color_material']}; {v['wheels_axles']}; "
            f"{v['interior_layout']}; state={cond}]"
        )
    if key in OBJECT_LOCK:
        o = OBJECT_LOCK[key]
        cond = o_states.get(key) or 'intact established state'
        return f"{plan['props'][key]} [OBJECT_LOCK {key}: {o['material_appearance']}; state={cond}]"
    return plan['props'][key]


def transition_text(c: dict, previous: dict | None) -> str:
    if previous is None:
        return 'Film opening. Begin directly at 0.0s inside the live night highway setting with the 18-wheel semi-truck already moving; no logo, title, recap, studio backdrop, or fade-in.'
    if c['transition'] == 'CONTINUE':
        return 'Begin directly at 0.0s in the exact established position, lens, axis, lighting and props from the preceding beat without injecting a static start-frame image; advance to the new action immediately at 0.0s and never replay the preceding gesture or words.'
    return {
        'OPEN': 'Begin directly at 0.0s in the stated time and place with the composition, lighting and movement already under way from the very first frame; no intro card, no reference portrait flash, and no transition effect.',
        'CUT': 'Begin directly at 0.0s in this single camera setup with natural momentum, preserving compatible screen direction and eyelines; no intro flash, no studio reference card, and no morph or duplicated gesture.',
        'MATCH': 'Begin directly at 0.0s in this new time and place with the related shape or pose already established in the opening frame; advance the action from 0.0s with no morph, dissolve, reference card flash, or replay of an earlier shot.',
        'J': 'Begin directly at 0.0s in this single location and camera setup with the location sound and movement already active from the very first frame; single-location take only, never show two locations or flash a reference card.',
        'L': 'Begin directly at 0.0s in this single location and camera setup while ambient sound settles naturally into the scene; single-location take only, never show two locations or flash a reference card.',
    }[c['transition']]


def render_prompt(plan: dict, c: dict, previous: dict | None, following: dict | None) -> str:
    continuous = c['transition'] == 'CONTINUE'
    head = '[FORMAT]'
    location, sound = plan['locations'][c['location']]
    sound = c.get('sound_override', sound)
    bible_slice = select_relevant_bible_slice(plan, c)
    env_axis = (c.get('spatial_state') or {}).get('axis') or bible_slice['environment'].get('orientation_axis', '')
    shot_type = c.get('shot_type') or (c.get('spatial_state') or {}).get('shot_type') or ('INSERT_DETAIL' if c['camera'] == 'I' else 'SCENE_SHOT')
    wf_mode = determine_omni_workflow(plan, c)
    physics_summary = ' '.join(bible_slice['physics_lines'])
    locks = '\n'.join(person_lock(plan, k, c) for k in c['characters']) or 'No named lead visible. Mechanical/vehicle/environment insert shot — do not add any lead character body to the frame.'
    picture_refs = '\n'.join(f"{plan['identities'][k]['tag']}: approved face for the PRINTED PHOTOGRAPH ONLY. Do not add this person physically to the room or street." for k in c.get('image_references', []))
    picture_refs = '\n[PICTURE-ONLY REFERENCES]\n' + picture_refs + '\n' if picture_refs else ''
    prop_text = '\n'.join(f'- {prop_detail(plan, p, c)}' for p in c['props']) or 'No new featured prop. Preserve already established carried items; introduce no extra symbolic objects.'
    note = c.get('wardrobe_note', '')
    if c.get('time_ellipsis'):
        note += '\nTime ellipsis: ' + c['time_ellipsis'] + '.'
    end = c['end_frame']
    if following:
        out = 'Hold this living composition in the same location and camera angle through 10.0s with natural breathing and ambient motion; never cut to another shot, another character, or a plain studio reference portrait at the end of the clip.'
    else:
        out = 'End the film on this living composition in the same location through 10.0s. Any title and final fade are added in post-production, never generated inside the image, and never cut to a studio reference portrait.'
    scene_obj = plan['scenes'][c['scene'] - 1]
    if c['scene'] == 1 and c['number'] == 1:
        scene_intro = f"\n[FILM OPENING INTRODUCTION — Mở đầu phim: {scene_obj['title']}]\nGrand opening shot of the film: at night on Interstate 10, a massive 18-wheel semi-truck hauls electronics cargo while three matte-black coupes with glowing green underglow close in from behind. Verni is already driving inside the left-hand cab seat at 0.0s as the narrator introduces him.\n"
    elif c['number'] == 1:
        first_line = f"first line at {c['dialogue'][0]['at'][0]:.1f}s" if c['dialogue'] else 'no dialogue'
        scene_intro = f"\n[SCENE OPENING HOOK — Mở cảnh {c['scene']:02d}: {scene_obj['title']}]\nScene goal: {scene_obj['purpose']} Establish the setting and dramatic stakes from the first frame; movement under way at 0.0s, {first_line}.\n"
    else:
        scene_intro = ''
    detail = c.get('cinematic', {})
    intent = f"\n[DRAMATIC INTENT — show through behaviour, never narrate this note]\n{detail['intent']}\n" if detail else ''
    staging = f"\n[BLOCKING AND PERFORMANCE]\nBlocking: {detail['blocking']}\nPerformance: {detail['performance']}\n" if detail else ''
    surface = f"\n[VISIBLE TEXTURE]\n{detail['texture']}\n" if detail else ''
    framing = f"\nComposition: {detail['composition']}\nFocus: {detail['focus']}" if detail else ''
    rhythm = f"\nAction rhythm: {detail['rhythm']}" if detail else ''
    sound_specific = f"\nForeground sound: {detail['sound_detail']}" if detail else ''
    if continuous:
        camera_contract = 'Keep the exact previous camera, lens and axis; no framing reset.'
    elif previous is None:
        camera_contract = "This first shot establishes the film's screen direction and geography. Never cut internally."
    else:
        camera_contract = 'One new coverage angle on the established side of the axis; positions, eyelines, prop hands and movement direction stay consistent with the story so far. Never cut internally.'
    shutter = SHUTTER.get(c['camera'], 'Natural 180-degree shutter')
    clip_avoid = f"\nIn this shot also do not show or do: {c['avoid']}." if c.get('avoid') else ''
    return f"""{head}
10 seconds, full-frame 16:9, 24 fps, photorealistic live-action high-velocity street-racing and undercover mystery drama, restrained naturalistic acting with micro-expressions, subtle breathing and natural eye movement, natural skin texture, subtle film grain. {shutter}. Grade: deep asphalt shadows, crisp neon and sodium street highlights, natural skin tones; no artificial lens flare or beauty smoothing. In a single continuous shot from 0.0s to 10.0s (Omni workflow: {wf_mode}, shot type: {shot_type}): ONE camera setup and ONE real story location throughout the entire clip. No scene cuts, no hard cuts, no montage, no recap, no closing fade, and never flash or cut to an attached character reference portrait or plain grey studio backdrop at the start or end of the clip. Spoken dialogue is Vietnamese with a natural Southern accent and accurate lip-sync; spoken lines follow a colon and are only spoken aloud, never shown as text.
{CLEAN_FRAME}

[CHARACTERS — approved identities and current appearances]
Use the attached reference images strictly for facial identity, hair, and wardrobe design inside the live story environment (or preserve the start frame when continuing). Only the listed characters and the unnamed people written into this shot appear in frame.
{locks}
{note.strip()}
{picture_refs}

[TIMELINE AND LOCATION]
Scene {c['scene']:02d}/40, clip {c['number']}/6; shot {c['id']}. Story time: {c['story_time']}.
{location}
Spatial geography & 180-degree axis: {env_axis}
{c['lighting']}
{scene_intro}{intent}

[CONTINUITY AT 0.0s — single uncut shot]
{transition_text(c, previous)}

[OPENING COMPOSITION AT 0.0s — START_STATE]
{c['start_frame']}

[CAMERA]
{CAMERAS[c['camera']]}
{camera_contract}{framing}

[ACTION — 0–10s, one evolving take]
{c['action']}
Play each beat once, in order, from 0.0s to 10.0s; no gesture is repeated and there is no quiet pause. Breathing and existing environmental motion continue naturally through 10.0s.{rhythm}
{staging}

[BODY, MOUTH AND FACE STANDARD]
{physics_summary}
{BODY_STANDARD}
{mouth_map(plan, c)}
{FACE_STANDARD}

[DIALOGUE]
{voice_block(plan, c)}

[PROPS]
Reference only; enact only the current ACTION, not a future handover.
{prop_text}
{surface}

[SOUND]
Location bed: {sound}.{sound_specific}
Keep diegetic continuity, dialogue clean and forward; every sound effect has a visible or established source. No generated score, stock sting or invented impact effect; ambient sound continues naturally through 10.0s.

[FINAL COMPOSITION AT 10.0s — END_STATE]
{end}
{out}

[AVOID]
Do not show or do any of the following: cutting to or flashing a standalone character reference portrait or plain grey studio backdrop at the start or end of the clip, showing a character turnaround sheet or split-screen, repeating any beat or line inside this clip or from adjacent clips, rushed, clipped or dragging speech, quiet pauses, exaggerated or theatrical acting, frozen tail frames, premature scene change, arbitrary slow motion or speed ramps, identity/age/costume drift, vehicle color/wheel/silhouette morphing, wrong prop owner, reversed movement axis, floating or sliding objects, objects passing through hands, extra or fused fingers, mouths moving outside their dialogue windows, lip-sync drift, facial morphing, drifting eyes, readable text, generated captions, logos, TV station or channel logos, broadcaster watermarks, news tickers, lower-thirds, LIVE/REC badges, timestamps, real actor likeness.{clip_avoid}
"""


def render_scene_readme(plan: dict, scene: dict, items: list[dict]) -> str:
    n = scene['number']
    start = (n - 1) * 60
    lines = [
        f"# {plan['title']} — Cảnh {n:02d}: {scene['title']}", '',
        f'**Bản {edition(plan)} · 6 clip × 10 giây · 16:9 đầy khung · nguồn PHAN_CANH_V3.json**', '',
        f"Phút {clock(start)}–{clock(start + 60)} · Thời gian truyện: {scene['story_time']}", '',
        scene['purpose'], '',
        'Một clip là một cú máy. Chỉ dùng frame cuối làm đầu vào khi bảng ghi **CONTINUE**; các hàng khác là cú cắt có chủ đích và đính lại reference. Shot chỉ có người nền, không có reference được chỉ định, dùng text-to-video. Không dùng frame cũ để kéo qua địa điểm mới.', '',
        '| Clip | Cách nối vào | Đầu clip | Hành động mới | Cuối clip | Thoại |',
        '|---|---|---|---|---|---|'
    ]
    if scene.get('dramaturgy'):
        d = scene['dramaturgy']
        lines[8:8] = [
            f"**Câu hỏi đang mở:** {d['dramatic_question_vi']}",
            f"**Móc vào cảnh:** {d['hook_vi']}",
            f"**Điểm bẻ:** {d['turn_vi']}",
            f"**Gieo / trả:** {d['payoff_or_setup_vi']}", ''
        ]
    for c in items:
        d = ' / '.join(dialogue_text(plan, x) for x in c['dialogue']) or '—'
        lines.append(f"| [{c['number']}](clip-{c['number']}.md) | {c['transition']} · {TRANSITIONS[c['transition']]} | {c['start_frame']} | {c['action']} | {c['end_frame']} | {d} |")
    if edition(plan) == '3.1':
        lines += ['', '## Phân cảnh chi tiết & Vật dụng mang theo (Chuẩn biên kịch 30 năm)', '']
        for c in items:
            sp = c.get('screenplay_vi', {})
            gear_vi = sp.get('gear_vi', '')
            beats_vi = sp.get('beats_vi', '')
            lines += [
                f"### Clip {c['number']} ({c['id']}) · {c['location']} · Góc máy {c['camera']}",
                f"- **Trang phục & Vật dụng mang theo:** {gear_vi}",
                f"- **Diễn biến 3 nhịp (0–10s):** {beats_vi}",
                f"- **Chỉ đạo diễn xuất:** {c['cinematic']['intent']} **Diễn xuất:** {c['cinematic']['performance']}",
                ""
            ]
    lines += [
        '', '**Âm nối sang cảnh sau:** ' + scene['outgoing_audio'], '',
        '[Bảng nối toàn phim](../BANG_NOI_CLIP.md) · [Kịch bản](../KICH_BAN_40_PHUT.md) · [Khóa và đạo cụ](../FLOW_PROMPTS.md)', '',
        'Kiểm tra video render: mặt/đồ/đạo cụ, ánh nhìn, hướng đi, âm nền, không lặp động tác ở mối nối. Prompt quy định ý đồ; video vẫn cần xem nối đôi trước khi chốt dựng.', ''
    ]
    return '\n'.join(lines)


def render_script(plan: dict, shots: list[dict]) -> str:
    lines = [
        f"# {plan['title']}",
        f'## Kịch bản phân cảnh chi tiết bản {edition(plan)} — Chuẩn biên kịch điện ảnh 30 năm', '',
        '**40 đơn vị sản xuất × 6 clip × 10 giây = 40 phút hình nguồn (240 clips).** Mỗi clip một cú máy, quản lý chặt chẽ trang phục, xe độ, bình NOS, giấy tờ xe và đạo cụ cầm tay xuyên suốt 240 phân cảnh.', '',
        'Nguồn duy nhất: `PHAN_CANH_V3.json`. Hành động/camera viết tiếng Anh cho prompt kèm bản phân cảnh tiếng Việt 3 nhịp chi tiết. Tái sinh bằng `python3 build_full_40_scenes.py`; kiểm tra bằng `python3 build_full_40_scenes.py --check`.', '',
        'Tom — sĩ quan cảnh sát chìm LAPD — thâm nhập vào giới đua xe đường phố của Micdo Toto để điều tra các vụ cướp xe container trên xa lộ Interstate 10. Giữa những trận đua 1/4 dặm sinh tử, mối tình với Ami Toto, cuộc chiến chống băng mô tô Light Saigon của Ny Tran và bi kịch của Seja cùng Cevin, Tom phải lựa chọn giữa nhiệm vụ cảnh sát và tình nghĩa anh em trên đường đua 10 giây cuối cùng.', '',
        '| Cảnh | Phút phim | Tên | Biến chuyển mới |', '|---|---|---|---|'
    ]
    for s in plan['scenes']:
        n = s['number']
        lines.append(f"| {n:02d} | {clock((n - 1) * 60)}–{clock(n * 60)} | {s['title']} | {s['purpose']} |")
    for s in plan['scenes']:
        n = s['number']
        lines += ['', f"### CẢNH {n:02d}: {s['title']}", f"*Thời gian truyện: {s['story_time']}*", s['purpose'], '']
        if s.get('dramaturgy'):
            d = s['dramaturgy']
            lines += [
                f"**Câu hỏi:** {d['dramatic_question_vi']}", f"**Móc vào:** {d['hook_vi']}",
                f"**Điểm bẻ:** {d['turn_vi']}", f"**Gieo / trả:** {d['payoff_or_setup_vi']}", ''
            ]
        for c in (x for x in shots if x['scene'] == n):
            d = ' / '.join(dialogue_text(plan, x) for x in c['dialogue']) or '—'
            sp = c.get('screenplay_vi', {})
            props_str = ', '.join(c['props']) if c['props'] else 'Không phát sinh đạo cụ mới'
            lines += [
                f"**Clip {c['number']} ({c['id']}) · {c['transition']} · {c['location']} · {c['camera']}**",
                f"- **Trang phục & Vật dụng mang theo:** {sp.get('gear_vi', c.get('wardrobe_note', ''))}",
                f"- **Mã đạo cụ khóa (Props):** `{props_str}`",
                f"- **Diễn biến phân cảnh 3 nhịp (Tiếng Việt):** {sp.get('beats_vi', '')}",
                f"- **Đầu (Start Frame):** {c['start_frame']}",
                f"- **Hành động 3 nhịp (Action Prompt):** {c['action']}",
                f"- **Thoại ({sum(syllables(x['text']) for x in c['dialogue'])} âm tiết):** {d}",
                f"- **Cuối (End Frame):** {c['end_frame']}", ''
            ]
            if c.get('cinematic'):
                detail = c['cinematic']
                labels = {
                    'intent': 'Ý đồ', 'composition': 'Bố cục', 'blocking': 'Vị trí / chuyển động',
                    'performance': 'Diễn xuất', 'focus': 'Điểm nét', 'texture': 'Chất liệu',
                    'sound_detail': 'Âm nổi', 'rhythm': 'Nhịp diễn'
                }
                lines += [f'- {labels[k]}: {detail[k]}' for k in DETAIL_FIELDS] + ['']
        lines.append('Âm nối sang cảnh sau: ' + s['outgoing_audio'])
    return '\n'.join(lines) + '\n'


def render_handoffs(plan: dict, shots: list[dict]) -> str:
    lines = [
        f'# Bảng nối 239 mối ghép — bản {edition(plan)}', '',
        'Mỗi hàng là một điểm cắt thực sự giữa hai clip, kể cả qua ranh giới cảnh. CONTINUE mới dùng khung cuối làm start frame; các hàng CUT/OPEN/MATCH/J/L dùng reference của shot mới. Không chèn lại nửa giây cuối clip trước và không phát lại thoại.', '',
        '| Từ → tới | Loại nối | Cuối clip trước | Đầu clip sau | Âm thanh / lưu ý dựng |',
        '|---|---|---|---|---|'
    ]
    for a, b in zip(shots, shots[1:]):
        bridge = plan['scenes'][a['scene'] - 1]['outgoing_audio'] if a['number'] == 6 else ''
        if b['transition'] == 'J':
            bridge += ' Cho âm địa điểm mới vào trước hình khoảng 0,25 giây.'
        elif b['transition'] == 'L':
            bridge += ' Giữ đuôi âm cũ qua hình mới khoảng 0,25 giây rồi hạ tự nhiên.'
        elif b['transition'] == 'CONTINUE':
            bridge += ' Giữ cùng ống kính/trục/vị trí. Tiếp động tác, không lặp đoạn kết.'
        else:
            bridge += ' Cắt theo tư thế/ánh nhìn được ghi, không morph, không thêm cảnh đệm.'
        lines.append(f"| [{a['id']}]({ref(a)}) → [{b['id']}]({ref(b)}) | {b['transition']} | {a['end_frame']} | {b['start_frame']} | {bridge.strip()} |")
    return '\n'.join(lines) + '\n'


def render_beatmap(plan: dict) -> str:
    lines = [
        '# Nhịp phim và câu hỏi giữ người xem — bản 3.1', '',
        'Mức áp lực 1–5 dưới đây là chỉ dẫn biên tập cho 40 cảnh (4 tập × 10 cảnh = 40 phút). Mỗi cảnh 6 clip × 10 giây = 1 phút.', '',
        '| Cảnh | Áp lực | Móc vào | Câu hỏi đang mở | Điểm bẻ | Gieo / trả |',
        '|---|---|---|---|---|---|'
    ]
    for s in plan['scenes']:
        d = s['dramaturgy']
        lines.append(f"| {s['number']:02d} · {s['title']} | {d['tension']}/5 | {d['hook_vi']} | {d['dramatic_question_vi']} | {d['turn_vi']} | {d['payoff_or_setup_vi']} |")
    lines += ['']
    return '\n'.join(lines)


def render_locks(plan: dict) -> str:
    lines = [
        f'# Khóa hình, đạo cụ và điểm nối — bản {edition(plan)}', '',
        'Master 16:9 đầy khung, 24 fps. Một clip một camera setup; thoại tiếng Việt giọng miền Nam. Không đóng băng cuối clip, không tự tạo nhạc riêng từng đoạn. Nhạc và title làm trên timeline dựng.', '',
        '**Cách tạo:** clip ghi CONTINUE mở bằng `Continue…`, dùng frame cuối clip trước; mọi cú cắt khác mở bằng `[FORMAT]`, đính lại các reference có mặt. Shot chỉ có người nền, không chỉ định reference, dùng text-to-video. Qua ranh giới cảnh luôn là cú cắt biên tập rõ, phù hợp runner hiện tại. Không kéo một start frame qua đổi địa điểm/tuổi/trang phục.', '',
        '**Khung hình sạch, không logo đài truyền hình, không nháy ảnh thẻ nhân vật:** mọi prompt cấm logo đài hoặc kênh ở góc hình, watermark, chữ chạy tin tức, lower-third, biểu tượng LIVE/REC, đồng hồ thời gian và tuyệt đối cấm chèn/nháy ảnh thẻ tham chiếu nhân vật nền xám ở đầu hoặc cuối clip.', '',
        f"**Giọng người dẫn chuyện (khóa cố định):** {plan['narrator']['voice_vi']}", '',
        '| Nhân vật | Handle | media_id đã có |', '|---|---|---|'
    ]
    for x in plan['identities'].values():
        lines.append(f"| {x['name']} | `{x['tag']}` | `{x['media_id']}` |")
    lines += ['', '## Biến thể dùng cùng danh tính', '']
    for k, (base, age, outfit) in plan['looks'].items():
        lines.append(f"- **{k}** → `{plan['identities'][base]['tag']}`, {age} tuổi: {outfit}.")
    lines += ['', '## Thư viện đạo cụ & Phương tiện', '']
    for k, v in plan['props'].items():
        lines.append(f'- **{k}:** {v}')
    lines += ['']
    return '\n'.join(lines)


def render_characters(plan: dict) -> str:
    arcs = {
        'TOM': 'Sĩ quan cảnh sát chìm LAPD thâm nhập giới đua xe đường phố. Giằng xé giữa nhiệm vụ pháp luật và tình cảm chân thành với Ami cùng sự kính trọng dành cho Micdo Toto.',
        'MICDO': 'Thủ lĩnh băng cướp xe tải và tay đua đường phố huyền thoại. Sống trọn vẹn từng phần tư dặm (10 giây), đặt gia đình và danh dự lên trên hết.',
        'AMI': 'Em gái của Micdo, chủ quán tạp hóa Toto. Dịu dàng nhưng kiên cường, yêu Tom thật lòng và đau đớn khi biết thân phận cảnh sát chìm của anh.',
        'CEVIN': 'Bạn thời thơ ấu và cánh tay phải nóng nảy của Micdo. Thầm thương Ami, luôn nghi ngờ Tom từ cái nhìn đầu tiên và bị thương nặng trong vụ cướp cuối.',
        'CINA': 'Bạn gái cá tính của Micdo và thành viên cốt cán trong đội đua xe – cướp container. Luôn sát cánh cùng Micdo trong mọi phi vụ.',
        'SEJA': 'Thiên tài toán học, máy tính và điện tử độ xe của nhóm (mắc chứng ADHD). Cùng Tom chế tạo chiếc Supra 10 giây, thua cược tại Race Wars và ngã xuống trước nhà Toto.',
        'ONLE': 'Thành viên kỳ cựu, thợ máy gầm bệ và tay lái bọc hậu vững vàng trong băng của Micdo.',
        'NYTRAN': 'Thủ lĩnh băng mô tô Light Saigon tại Little Saigon, đối thủ buôn lậu và đua xe tàn nhẫn của Micdo.',
        'CELA': 'Anh họ và đồng đảng thân cận luôn kề cận Ny Tran trong mọi cuộc vây ép và truy sát.',
        'NESE': 'Sĩ quan cảnh sát LAPD chỉ huy trực tiếp của Tom, hiểu rõ ranh giới mong manh của một cảnh sát chìm.',
        'KINAN': 'Đặc vụ FBI phối hợp điều tra các vụ cướp xe tải trên xa lộ, cứng rắn và nóng lòng phá án trước khi các tài xế tự vũ trang.',
        'VERNI': 'Tài xế xe container 18 bánh đường dài trên xa lộ Interstate 10, nạn nhân vụ cướp đầu phim và người tự vũ trang chống trả quyết liệt ở phi vụ cuối.',
    }
    shots = normalize(plan)
    first = first_appearances(plan, shots)
    lines = [
        f'# Mười hai nhân vật chính — hồ sơ thống nhất bản {edition(plan)}', '',
        'Phim hành động tốc độ & cảnh sát chìm 40 phút (40 cảnh × 6 clip = 240 clips). Giữ đồng nhất ngoại hình, trang phục, phương tiện và giọng nói miền Nam xuyên suốt toàn bộ 40 cảnh.', ''
    ]
    for key, x in plan['identities'].items():
        intro = next(d['text'] for c in shots if c['id'] == first[key] for d in c['dialogue'] if d['speaker'] == 'NARRATOR')
        lines += [
            f"## {x['name']} · {x['tag']}", '',
            arcs[key], '',
            f"Nhận diện: {x['identity']}.",
            f"Giọng xuyên phim: {x['voice']}.",
            f"Lời người dẫn chuyện khi xuất hiện lần đầu ({first[key]}): {intro}", '',
            'Biến thể và prompt ảnh tham chiếu:'
        ]
        for look, (base, age, outfit) in plan['looks'].items():
            if base == key:
                lines += [f'- **{look}:** Photorealistic reference of the SAME approved identity, age {age}, {outfit}. Plain grey studio background, full body and portrait, no text, no real actor likeness.']
        lines.append('')
    intros = [(c['id'], d['text']) for c in shots for d in c['dialogue'] if d['speaker'] == 'NARRATOR']
    lines += [
        f"## {plan['narrator']['name_vi']} · giọng kể ngoài truyện", '',
        f"Giọng khóa cố định: {plan['narrator']['voice_vi']}", '',
        'Các câu giới thiệu nhân vật chính, đọc ở ngôi thứ ba, mỗi câu ở clip đầu tiên nhân vật ra hình:'
    ]
    lines += [f'- {cid}: {text}' for cid, text in intros]
    lines += ['']
    return '\n'.join(lines)


def outputs(plan: dict, shots: list[dict]) -> dict[str, str]:
    result = {}
    for i, c in enumerate(shots):
        result[ref(c)] = render_prompt(plan, c, shots[i - 1] if i else None, shots[i + 1] if i + 1 < len(shots) else None)
    for s in plan['scenes']:
        n = s['number']
        folder = f'canh-{n:02d}'
        result[f'{folder}/README.md'] = render_scene_readme(plan, s, [c for c in shots if c['scene'] == n])
        result[f'{folder}/caption.md'] = f"# {plan['title']} · Cảnh {n:02d}: {s['title']}\n\n{s['purpose']}\n\nPhim hành động tốc độ 40 phút do AI tạo.\n\n#duongduasinhtu #phimhanhdong #10giaytudo #phimai\n"
    script_text = render_script(plan, shots)
    result['KICH_BAN_40_PHUT.md'] = script_text
    result['KICH_BAN_70_PHUT.md'] = script_text
    result['BANG_NOI_CLIP.md'] = render_handoffs(plan, shots)
    result['FLOW_PROMPTS.md'] = render_locks(plan)
    result['NHAN_VAT.md'] = render_characters(plan)
    if edition(plan) == '3.1':
        result['NHIP_PHIM_V3_1.md'] = render_beatmap(plan)
    manifest = {
        'version': 3,
        'editorial_revision': edition(plan),
        'source': 'PHAN_CANH_V3.json',
        'source_sha256': hashlib.sha256(json.dumps(plan, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
        'note': 'Expected prompt fingerprints for all 240 clips (40 scenes × 6 clips).',
        'clips': [
            {
                'id': c['id'],
                'prompt': ref(c),
                'sha256': hashlib.sha256(result[ref(c)].encode()).hexdigest(),
                'mode': 'ingredients' if c['characters'] or c.get('image_references') else 'text',
                'previous': c['previous'],
                'transition': c['transition'],
            }
            for c in shots
        ],
    }
    result['RENDER_MANIFEST_V3.json'] = json.dumps(manifest, ensure_ascii=False, indent=2) + '\n'
    return result


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate plan and generated files without writing')
    parser.add_argument('--validate-only', action='store_true', help='Validate editable plan without writing')
    parser.add_argument('--out-dir', type=Path, default=BASE_DIR)
    args = parser.parse_args(argv)
    plan = json.loads((BASE_DIR / 'PHAN_CANH_V3.json').read_text(encoding='utf-8'))
    shots = normalize(plan)
    validate(plan, shots)
    counts = Counter(c['transition'] for c in shots)
    if args.validate_only:
        print(f'PASS: 40 scenes, 240 unique actions, 239 handoffs; {dict(counts)}')
        return
    files = outputs(plan, shots)
    if args.check:
        stale = [name for name, text in files.items() if not (args.out_dir / name).is_file() or (args.out_dir / name).read_text(encoding='utf-8') != text]
        if stale:
            raise SystemExit('Missing/out-of-date outputs:\n' + '\n'.join(stale))
        print(f'PASS: {len(files)} generated files match canonical plan; 240 shots / 239 handoffs; {counts.get("CONTINUE", 0)} exact-frame continuations.')
        return
    for name, text in files.items():
        path = args.out_dir / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
    document_count = len(files) - 321
    print(f'Generated {len(files)} files: 240 shot prompts, 40 scene guides, 40 captions, {document_count} film documents and render manifest.')
    print(f'Validated 239 handoffs; {counts.get("CONTINUE", 0)} continuous takes, remaining seams are explicit editorial cuts.')


if __name__ == '__main__':
    main()

